"""Live Preview hit-routing audit for dist/theme-v3.css.

Scans top-level CSS rules and flags any rule whose selector targets a Live
Preview block widget or HyperMD-* cm-line variant directly and declares a
non-zero vertical margin (widgets) or non-zero vertical margin/padding
(cm-line variants).

Additional categories codify recurring CM6 hit-routing regressions:
  - active line: `.cm-active.cm-line` must not declare `outline`,
    `box-shadow`, `transform`, or vertical padding - these extend the
    hit-target or create overlays that capture clicks.
  - embed BFC: `.cm-embed-block`, `.cm-html-embed` must not declare the
    lethal `overflow-x:auto + max-width:100%` BFC pair, which creates a
    hit-target gap above tables/embeds.
  - content overflow: `.cm-content`, `.cm-line` must not be forced to
    `pointer-events:none` (kills click-to-edit on rendered text).

Multiple violations are accumulated and reported together so a single
pass surfaces every regression a patch introduces.

Exits with code 1 if any violation is detected, 0 otherwise.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

LIVE_PREVIEW_WIDGET_DIRECT_TOKENS = (
    ".cm-callout",
    ".cm-table-widget",
    ".cm-embed-block.cm-callout",
)
LIVE_PREVIEW_HYPERMD_DIRECT_TOKENS = (
    ".HyperMD-table-row",
    ".HyperMD-callout",
    ".HyperMD-codeblock",
    ".HyperMD-codeblock-begin",
    ".HyperMD-codeblock-end",
    ".HyperMD-header-1",
    ".HyperMD-header-2",
    ".HyperMD-header-3",
    ".HyperMD-header-4",
    ".HyperMD-header-5",
    ".HyperMD-header-6",
)
_RULE_RE = re.compile(r"([^{}]+?)\{([^{}]*)\}", re.S)


def _split_top_level_commas(selector_list: str) -> list[str]:
    parts: list[str] = []
    depth = 0
    current: list[str] = []
    for ch in selector_list:
        if ch == "(":
            depth += 1
            current.append(ch)
        elif ch == ")":
            depth -= 1
            current.append(ch)
        elif ch == "," and depth == 0:
            parts.append("".join(current))
            current = []
        else:
            current.append(ch)
    if current:
        parts.append("".join(current))
    return parts


def _selector_targets_token_directly(selector_list: str, token: str) -> bool:
    pseudo_tail_re = re.compile(r"(?:\.[\w-]+|:[\w-]+(?:\([^)]*\))?|\[[^\]]+\])*")
    for sel in _split_top_level_commas(selector_list):
        sel = sel.strip()
        if token not in sel:
            continue
        stack: list[str | None] = []
        i = 0
        n = len(sel)
        last_top_level_end = -1
        while i < n:
            ch = sel[i]
            if ch == "(":
                j = i - 1
                while j >= 0 and (sel[j].isalnum() or sel[j] in "-_"):
                    j -= 1
                fname = sel[j + 1 : i] if j + 1 < i and j >= 0 and sel[j] == ":" else None
                stack.append(fname)
                i += 1
                continue
            if ch == ")":
                if stack:
                    stack.pop()
                i += 1
                continue
            if sel.startswith(token, i) and (
                token.startswith(".") or i == 0 or not (sel[i - 1].isalnum() or sel[i - 1] in "-_")
            ):
                end = i + len(token)
                if all(name in ("is", "where", "matches") for name in stack):
                    if not stack:
                        last_top_level_end = end
                i = end
                continue
            i += 1
        if last_top_level_end >= 0:
            tail = sel[last_top_level_end:]
            if pseudo_tail_re.fullmatch(tail):
                return True
        for grp_match in re.finditer(r":(?:is|where|matches)\(", sel):
            start = grp_match.end() - 1
            depth = 1
            j = start + 1
            while j < n and depth > 0:
                if sel[j] == "(":
                    depth += 1
                elif sel[j] == ")":
                    depth -= 1
                j += 1
            if depth != 0:
                continue
            close_pos = j
            inner = sel[start + 1 : close_pos - 1]
            inner_stripped = re.sub(r":not\([^)]*\)", "", inner)
            for alt in _split_top_level_commas(inner_stripped):
                alt = alt.strip()
                if token not in alt:
                    continue
                idx = alt.rfind(token)
                tail = alt[idx + len(token) :]
                if pseudo_tail_re.fullmatch(tail):
                    selector_tail = sel[close_pos:]
                    if pseudo_tail_re.fullmatch(selector_tail):
                        return True
    return False


def _is_nonzero(value: str) -> bool:
    value = value.strip()
    if not value or value in ("0", "auto"):
        return False
    if re.fullmatch(r"0(?:px|em|rem|%|vh|vw|pt)", value):
        return False
    return True


def _has_nonzero_vertical_box(body: str, properties: tuple) -> str | None:
    for decl in body.split(";"):
        decl = decl.strip()
        if not decl or ":" not in decl:
            continue
        prop, _, value = decl.partition(":")
        prop = prop.strip().lower()
        value = value.strip()
        if prop not in properties:
            continue
        if prop in ("margin", "padding"):
            tokens = [t for t in re.split(r"\s+", value) if t and not t.startswith("!")]
            if not tokens:
                continue
            top = tokens[0]
            bottom = tokens[2] if len(tokens) >= 3 else top
            if _is_nonzero(top) or _is_nonzero(bottom):
                return decl
        else:
            value_no_bang = value.split("!")[0].strip()
            if _is_nonzero(value_no_bang):
                return decl
    return None


def _declares_any(body: str, properties: tuple) -> str | None:
    for decl in body.split(";"):
        decl = decl.strip()
        if not decl or ":" not in decl:
            continue
        prop, _, value = decl.partition(":")
        prop = prop.strip().lower()
        if prop not in properties:
            continue
        value_no_bang = value.split("!")[0].strip()
        if value_no_bang in ("", "0", "none", "auto", "unset", "initial", "revert"):
            continue
        if re.fullmatch(r"0(?:px|em|rem|%|vh|vw|pt)?", value_no_bang):
            continue
        return decl
    return None


def _declares_pair(body: str, prop: str, value_token: str) -> bool:
    pattern = re.compile(
        rf"\b{re.escape(prop)}\s*:\s*[^;]*\b{re.escape(value_token)}\b"
    )
    return bool(pattern.search(body))


def live_preview_hit_routing_audit(content: str, source_label: str) -> list[str]:
    margin_props = (
        "margin", "margin-top", "margin-bottom", "margin-block",
        "margin-block-start", "margin-block-end",
    )
    margin_padding_props = margin_props + (
        "padding", "padding-top", "padding-bottom", "padding-block",
        "padding-block-start", "padding-block-end",
    )
    failures: list[str] = []
    for match in _RULE_RE.finditer(content):
        selectors = match.group(1)
        body = match.group(2)
        if "markdown-source-view.mod-cm6" not in selectors:
            continue
        for token in LIVE_PREVIEW_WIDGET_DIRECT_TOKENS:
            if _selector_targets_token_directly(selectors, token):
                offender = _has_nonzero_vertical_box(body, margin_props)
                if offender:
                    failures.append(
                        f"non-zero vertical margin on CM6 block widget ({token}) - "
                        f"bleeds hit-target. Body: `{offender}`."
                    )
                break
        for token in LIVE_PREVIEW_HYPERMD_DIRECT_TOKENS:
            if _selector_targets_token_directly(selectors, token):
                offender = _has_nonzero_vertical_box(body, margin_padding_props)
                if offender:
                    failures.append(
                        f"non-zero vertical margin/padding on HyperMD-* cm-line "
                        f"({token}) - Body: `{offender}`."
                    )
                break
        for token in (".cm-active.cm-line", ".cm-active .cm-line"):
            if _selector_targets_token_directly(selectors, token):
                bad = _declares_any(
                    body,
                    ("outline", "box-shadow", "transform",
                     "padding", "padding-top", "padding-bottom"),
                )
                if bad:
                    failures.append(
                        f"forbidden visual on active CM6 line ({token}) - `{bad}`."
                    )
                break
        for token in (".cm-embed-block", ".cm-html-embed"):
            if _selector_targets_token_directly(selectors, token):
                if _declares_pair(body, "overflow-x", "auto") and \
                        _declares_pair(body, "max-width", "100%"):
                    failures.append(
                        f"lethal BFC pair on embed wrapper ({token}) - "
                        f"`overflow-x:auto + max-width:100%`."
                    )
                break
        for token in (".cm-content", ".cm-line"):
            if _selector_targets_token_directly(selectors, token):
                if re.search(r"pointer-events\s*:\s*none\b", body):
                    failures.append(
                        f"pointer-events:none on rendered CM6 text ({token}) - "
                        f"kills click-to-edit."
                    )
                break
    return failures


def main() -> int:
    bundle = ROOT / "dist" / "theme-v3.css"
    if not bundle.exists():
        print(f"ERROR: {bundle} does not exist. Run bundle_v3.py first.")
        return 2
    content = bundle.read_text(encoding="utf-8")
    failures = live_preview_hit_routing_audit(content, str(bundle.relative_to(ROOT)))
    if failures:
        print(f"FAIL: {bundle.name} hit-routing violations:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print(f"OK: live_preview_hit_routing_audit clean on {bundle.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
