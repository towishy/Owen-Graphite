#!/usr/bin/env python3
"""Post-process pass on dist/theme-v3.css that merges duplicate selectors within
the same @-rule context.

Strategy:
- Parse the bundle into a tree of (rule | at_block | comment | whitespace).
- Within each scope (top-level + each @-rule body), find rules whose selector
  (whitespace-normalized) appears more than once.
- Merge their declaration bodies into the LAST occurrence, in source order.
  - Keeping the merged block at the latest position preserves cascade against
    intermediate rules of HIGHER specificity (those still win because the merged
    properties were already being overwritten by them at the original later
    position). Intermediate rules of EQUAL specificity targeting the same
    elements + properties are out of scope for v3 (the cascade is built on
    file-import order + selector specificity precisely to avoid that pattern).
- Same-selector duplicates inside *different* @-rule scopes (e.g., one inside
  @media print, one outside) are NEVER merged.

Output overwrites dist/theme-v3.css in place. A summary line reports the merge
count so the operator can sanity-check.

Run after `dev/scripts/bundle_v3.py`. The dedup is idempotent.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "dist" / "theme-v3.css"

WS_RE = re.compile(r"\s+")


def normalize_selector(text: str) -> str:
    # Strip leading/trailing whitespace and collapse internal runs of whitespace
    # so that `body  :is(.a,\n .b)` and `body :is(.a, .b)` compare equal.
    return WS_RE.sub(" ", text).strip()


def split_top_level(css: str):
    """Yield (kind, prelude, body, start, end) units at brace depth 0.

    kinds:
      - 'comment'      : /* ... */
      - 'ws'           : whitespace run
      - 'at_statement' : @import url(...); etc.
      - 'at_block'     : @media (...) { ... }
      - 'rule'         : selector { ... }
      - 'raw'          : stray character (e.g., spurious '}')
    """
    n = len(css)
    i = 0
    while i < n:
        c = css[i]
        # whitespace run
        if c in " \t\r\n":
            j = i
            while j < n and css[j] in " \t\r\n":
                j += 1
            yield ("ws", css[i:j], "", i, j)
            i = j
            continue
        # comment
        if css.startswith("/*", i):
            j = css.find("*/", i + 2)
            j = n if j < 0 else j + 2
            yield ("comment", css[i:j], "", i, j)
            i = j
            continue
        # at-rule
        if c == "@":
            j = _scan_to_semi_or_brace(css, i)
            if j is None:
                yield ("raw", css[i:], "", i, n)
                i = n
                continue
            stop = css[j]
            if stop == ";":
                yield ("at_statement", css[i : j + 1], "", i, j + 1)
                i = j + 1
                continue
            # stop == '{'
            end = _scan_matching_brace(css, j)
            prelude = css[i:j]
            body = css[j + 1 : end]
            yield ("at_block", prelude, body, i, end + 1)
            i = end + 1
            continue
        # stray close brace — pass through verbatim
        if c == "}":
            yield ("raw", c, "", i, i + 1)
            i += 1
            continue
        # normal rule: scan selector until '{'
        j = _scan_to_brace(css, i)
        if j is None:
            yield ("raw", css[i:], "", i, n)
            i = n
            continue
        end = _scan_matching_brace(css, j)
        selector = css[i:j]
        body = css[j + 1 : end]
        yield ("rule", selector, body, i, end + 1)
        i = end + 1


def _scan_to_brace(css: str, start: int) -> int | None:
    """Find the next '{' at the current nesting (string/comment-safe). Returns
    None if not found."""
    n = len(css)
    j = start
    in_str = None
    while j < n:
        c = css[j]
        if in_str:
            if c == "\\":
                j += 2
                continue
            if c == in_str:
                in_str = None
            j += 1
            continue
        if css.startswith("/*", j):
            k = css.find("*/", j + 2)
            j = n if k < 0 else k + 2
            continue
        if c in ("'", '"'):
            in_str = c
            j += 1
            continue
        if c == "{":
            return j
        if c == "}":
            return None
        j += 1
    return None


def _scan_to_semi_or_brace(css: str, start: int) -> int | None:
    """Find next ';' or '{' at depth 0 (string/comment-safe)."""
    n = len(css)
    j = start
    in_str = None
    while j < n:
        c = css[j]
        if in_str:
            if c == "\\":
                j += 2
                continue
            if c == in_str:
                in_str = None
            j += 1
            continue
        if css.startswith("/*", j):
            k = css.find("*/", j + 2)
            j = n if k < 0 else k + 2
            continue
        if c in ("'", '"'):
            in_str = c
            j += 1
            continue
        if c in ("{", ";"):
            return j
        j += 1
    return None


def _scan_matching_brace(css: str, brace_idx: int) -> int:
    """Given the index of an opening '{', return the index of its matching
    '}'. String- and comment-safe."""
    n = len(css)
    assert css[brace_idx] == "{"
    depth = 1
    j = brace_idx + 1
    in_str = None
    while j < n:
        c = css[j]
        if in_str:
            if c == "\\":
                j += 2
                continue
            if c == in_str:
                in_str = None
            j += 1
            continue
        if css.startswith("/*", j):
            k = css.find("*/", j + 2)
            j = n if k < 0 else k + 2
            continue
        if c in ("'", '"'):
            in_str = c
            j += 1
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return j
        j += 1
    raise ValueError(f"unmatched '{{' at offset {brace_idx}")


def render_body(body: str) -> str:
    """Reassemble a parsed body, preserving original text for inner units."""
    out = []
    for kind, prelude, body_inner, _, _ in split_top_level(body):
        out.append(_render_unit(kind, prelude, body_inner))
    return "".join(out)


def _render_unit(kind: str, prelude: str, body: str) -> str:
    if kind in ("comment", "ws", "at_statement", "raw"):
        return prelude
    if kind == "rule":
        return f"{prelude}{{{body}}}"
    if kind == "at_block":
        return f"{prelude}{{{body}}}"
    raise AssertionError(kind)


def dedup_scope(css: str) -> tuple[str, int]:
    """Dedup top-level same-selector duplicates within this scope. Recurse
    into @-rule bodies. Returns (new_css, merges_applied)."""
    units = list(split_top_level(css))
    # First, recurse into at_blocks
    merges = 0
    for idx, (kind, prelude, body, s, e) in enumerate(units):
        if kind == "at_block":
            new_body, inner_merges = dedup_scope(body)
            merges += inner_merges
            units[idx] = (kind, prelude, new_body, s, e)
    # Then, dedup top-level rules
    by_selector: dict[str, list[int]] = {}
    for idx, (kind, prelude, _, _, _) in enumerate(units):
        if kind != "rule":
            continue
        key = normalize_selector(prelude)
        by_selector.setdefault(key, []).append(idx)
    to_delete: set[int] = set()
    for _, idxs in by_selector.items():
        if len(idxs) < 2:
            continue
        # Merge all into the LAST occurrence, in source order.
        last_idx = idxs[-1]
        last_kind, last_sel, last_body, last_s, last_e = units[last_idx]
        combined_parts: list[str] = []
        for i in idxs:
            body = units[i][2]
            combined_parts.append(body)
        merged_body = _merge_bodies(combined_parts)
        units[last_idx] = (last_kind, last_sel, merged_body, last_s, last_e)
        for i in idxs[:-1]:
            to_delete.add(i)
            merges += 1
    # v3.1.4 — property-level dedup pass.
    # Even rules that were NOT merged across files can pick up duplicate
    # property declarations (some authored, some accumulated through earlier
    # merge passes that ran before this hardening). Walk every plain rule's
    # body and keep only the LAST occurrence of each property name — the same
    # cascade outcome the browser would produce, but visible to the
    # community-theme lint validator which warns on intra-rule duplicates.
    for idx, unit in enumerate(units):
        if idx in to_delete:
            continue
        kind, prelude, body, s, e = unit
        if kind != "rule":
            continue
        new_body = _dedup_declarations(body)
        if new_body != body:
            units[idx] = (kind, prelude, new_body, s, e)
    # Reassemble
    out_parts: list[str] = []
    prev_kind = None
    for idx, unit in enumerate(units):
        if idx in to_delete:
            # Collapse the following whitespace/comment block belonging only to
            # the deleted rule to avoid leaving large blank holes. We only swallow
            # immediate trailing whitespace, not comments — comments may be
            # documentation that should survive.
            j = idx + 1
            while j < len(units) and units[j][0] == "ws":
                to_delete.add(j)
                j += 1
            continue
        out_parts.append(_render_unit(unit[0], unit[1], unit[2]))
    return "".join(out_parts), merges


def _merge_bodies(bodies: list[str]) -> str:
    """Concatenate rule bodies, ensuring each piece ends with a newline and a
    trailing semicolon (where appropriate)."""
    pieces: list[str] = []
    for body in bodies:
        b = body.rstrip()
        if not b:
            continue
        # ensure trailing semicolon (declarations only, not for blocks that
        # already end in a brace from nested at-rules — but inside selector
        # bodies, that won't happen).
        if not b.endswith(";") and not b.endswith("}"):
            b = b + ";"
        pieces.append(b)
    # Indent the merged content with a single newline join so it's readable.
    inner = "\n  ".join(pieces)
    return f"\n  {inner}\n"


_PROP_NAME_RE = re.compile(r"\s*(--[A-Za-z0-9_-]+|-?[A-Za-z_][A-Za-z0-9_-]*)\s*$")


def _split_declarations(body: str) -> list[tuple[str, str]]:
    """Split a CSS rule body into ordered (kind, text) tokens where kind is
    one of: 'decl', 'comment', 'ws', 'other'. Brace-/paren-/string-/comment-
    safe. The 'other' kind is returned for any unexpected at-rule or stray
    construct so callers can bail out of property dedup safely.
    """
    out: list[tuple[str, str]] = []
    n = len(body)
    i = 0
    buf: list[str] = []

    def flush_decl():
        if buf:
            text = "".join(buf)
            buf.clear()
            stripped = text.strip()
            if stripped:
                out.append(("decl", text))
            else:
                out.append(("ws", text))

    while i < n:
        c = body[i]
        # comment
        if body.startswith("/*", i):
            flush_decl()
            j = body.find("*/", i + 2)
            j = n if j < 0 else j + 2
            out.append(("comment", body[i:j]))
            i = j
            continue
        # string literal — copy contents into buf verbatim
        if c in ('"', "'"):
            buf.append(c)
            j = i + 1
            while j < n:
                cc = body[j]
                if cc == "\\" and j + 1 < n:
                    buf.append(body[j : j + 2])
                    j += 2
                    continue
                buf.append(cc)
                j += 1
                if cc == c:
                    break
            i = j
            continue
        # parenthesized group — copy contents into buf, do not split on ;
        if c == "(":
            depth = 1
            buf.append(c)
            j = i + 1
            while j < n and depth > 0:
                cc = body[j]
                if body.startswith("/*", j):
                    k = body.find("*/", j + 2)
                    k = n if k < 0 else k + 2
                    buf.append(body[j:k])
                    j = k
                    continue
                if cc in ('"', "'"):
                    buf.append(cc)
                    k = j + 1
                    while k < n:
                        cc2 = body[k]
                        if cc2 == "\\" and k + 1 < n:
                            buf.append(body[k : k + 2])
                            k += 2
                            continue
                        buf.append(cc2)
                        k += 1
                        if cc2 == cc:
                            break
                    j = k
                    continue
                if cc == "(":
                    depth += 1
                elif cc == ")":
                    depth -= 1
                buf.append(cc)
                j += 1
            i = j
            continue
        # at-rule inside a rule body — abort cleanly by emitting an 'other'
        # token so the caller can choose to leave the body untouched.
        if c == "@":
            flush_decl()
            # consume to end of body — leave as a single 'other' token
            out.append(("other", body[i:]))
            return out
        # stray brace — abort
        if c in ("{", "}"):
            flush_decl()
            out.append(("other", body[i:]))
            return out
        if c == ";":
            buf.append(c)
            text = "".join(buf)
            buf.clear()
            if text.strip():
                out.append(("decl", text))
            else:
                out.append(("ws", text))
            i += 1
            continue
        buf.append(c)
        i += 1
    flush_decl()
    return out


def _decl_property(decl_text: str) -> str | None:
    """Extract the property name from a declaration string. Returns None if
    the declaration is malformed or not a plain property declaration."""
    s = decl_text.strip()
    if not s:
        return None
    # Drop trailing semicolon for matching.
    if s.endswith(";"):
        s = s[:-1].rstrip()
    # Skip leading comments.
    while s.startswith("/*"):
        end = s.find("*/")
        if end < 0:
            return None
        s = s[end + 2 :].lstrip()
    if not s:
        return None
    # Find the first ':' that is NOT inside parens — but property names
    # cannot contain '(' before ':' anyway, so the very first ':' is fine.
    colon = s.find(":")
    if colon < 0:
        return None
    name = s[:colon].rstrip()
    m = _PROP_NAME_RE.fullmatch(name)
    if not m:
        return None
    return m.group(1).lower()


def _dedup_declarations(body: str) -> str:
    """Within a rule body, keep only the LAST occurrence of each property
    declaration. Preserves comments and whitespace runs. Returns the body
    unchanged if it contains nested at-rules or other constructs the safe
    parser cannot reason about."""
    items = _split_declarations(body)
    # If any 'other' token appears, do not touch this body.
    if any(kind == "other" for kind, _ in items):
        return body
    # Walk to find last index of each property; mark earlier 'decl's as
    # dropped. Comments and whitespace between a dropped decl and the next
    # surviving token are preserved (they may carry author intent).
    last_idx_for: dict[str, int] = {}
    drop: set[int] = set()
    for idx, (kind, text) in enumerate(items):
        if kind != "decl":
            continue
        prop = _decl_property(text)
        if prop is None:
            continue
        if prop in last_idx_for:
            drop.add(last_idx_for[prop])
        last_idx_for[prop] = idx
    if not drop:
        return body
    out: list[str] = []
    pending_ws: list[str] = []
    for idx, (kind, text) in enumerate(items):
        if idx in drop:
            # Skip the dropped declaration. Also skip any *immediately*
            # following whitespace run that exists solely to separate it
            # from the next token (otherwise the file fills with blank
            # lines). Comments are always preserved.
            pending_ws = []
            # Peek ahead and consume one ws run.
            # (handled below by setting a flag)
            _ = idx  # no-op
            # consume next ws via index manipulation: easier to track
            # via flag
            drop_next_ws = True
            # Mark the drop_next_ws state by appending a sentinel to
            # pending_ws — but we are inside a for-loop; simpler approach
            # below.
            # Use a more direct approach: rebuild via while-loop instead.
            pass
        else:
            out.append(text)
    # Simpler rebuild: iterate with index and look-ahead to skip one
    # following whitespace-only token after each dropped declaration.
    out = []
    i = 0
    nitems = len(items)
    while i < nitems:
        kind, text = items[i]
        if i in drop:
            # Skip this dropped declaration.
            i += 1
            # Consume an immediately-following whitespace run (if any) to
            # avoid leaving large blank holes.
            if i < nitems and items[i][0] == "ws":
                i += 1
            continue
        out.append(text)
        i += 1
    return "".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--in", dest="src", type=Path, default=DIST)
    parser.add_argument("--out", type=Path, default=None)
    parser.add_argument("--check", action="store_true",
                        help="Report merges that would be applied; do not write.")
    args = parser.parse_args()
    src: Path = args.src
    out: Path = args.out or src
    if not src.is_file():
        print(f"ERROR: input not found: {src}")
        return 1
    text = src.read_text(encoding="utf-8")
    new_text, merges = dedup_scope(text)
    if args.check:
        print(f"OK: would merge {merges} duplicate-selector blocks in {src.relative_to(ROOT)}")
        return 0
    out.write_text(new_text, encoding="utf-8")
    line_count = new_text.count("\n") + 1
    bang_count = new_text.count("!important")
    print(
        f"OK: dedupped {out.relative_to(ROOT)} "
        f"({line_count} lines, !important={bang_count}, merges={merges})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
