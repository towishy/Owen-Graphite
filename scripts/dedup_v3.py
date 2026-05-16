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

Run after `scripts/bundle_v3.py`. The dedup is idempotent.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
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
