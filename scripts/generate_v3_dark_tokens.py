#!/usr/bin/env python3
"""Extract all `.theme-dark { --ogd-*: ...; }` declarations from dev/*.css and
emit a single consolidated src/tokens/01-dark-tokens.css for the v3 rewrite.

Selection rules:
- Only blocks whose selector list contains no descendant combinator (no
  whitespace inside the selector) but does mention `.theme-dark`. This
  matches the global dark-defaults patterns used in v2.30.14:
  `.theme-dark`, `body.theme-dark`, `body:not(.is-mobile).theme-dark`,
  `body.theme-dark.ogd-spacing-relaxed`, etc.
- Descendant variants (e.g. `body.theme-dark :is(.markdown-rendered, ...)`)
  are intentionally not collected here — they belong in src/themes/50-dark.css
  or the relevant surface/feature module later (S5 - S8).
- Only `--ogd-*` custom property declarations. Obsidian core variable
  overrides (e.g. `--background-primary` in `.theme-dark`) are also collected
  because Obsidian core dark colors are part of the theme contract.
- First-write-wins per token name across the bundle traversal order. The
  traversal order matches dev/_order.txt so the result mirrors the cascade
  the v2.30.14 bundle produces.

The output file is regenerated in-place; do not hand-edit. If the v3 dark
defaults need to drift from v2.30.14, edit a separate src/themes/50-dark.css
override and document the decision in docs/v3/design-spec.md.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEV = ROOT / "dev"
ORDER_FILE = DEV / "_order.txt"
OUT_PATH = ROOT / "src" / "tokens" / "01-dark-tokens.css"

# Match a single CSS declaration of the form `<prop>: <value>;` where prop is
# either a custom property or an Obsidian core variable we mirror in dark mode.
DECL_RE = re.compile(
    r"(--[a-z0-9-]+)\s*:\s*([^;{}]+?)\s*(?:!important)?\s*;",
    re.IGNORECASE | re.DOTALL,
)

# Whitelist of core Obsidian variables that are part of the dark contract.
# Anything outside `--ogd-*` and this list is skipped to keep the tokens
# layer focused; broader overrides live in src/themes/50-dark.css.
CORE_VAR_WHITELIST = {
    # background
    "--background-primary",
    "--background-primary-alt",
    "--background-secondary",
    "--background-secondary-alt",
    "--background-modifier-border",
    "--background-modifier-border-hover",
    "--background-modifier-hover",
    "--background-modifier-active-hover",
    # text
    "--text-normal",
    "--text-muted",
    "--text-faint",
    "--text-accent",
    "--text-accent-hover",
    "--text-on-accent",
    "--text-on-accent-inverted",
    "--text-selection",
    # interactive
    "--interactive-normal",
    "--interactive-hover",
    "--interactive-accent",
    "--interactive-accent-rgb",
    "--interactive-accent-hover",
    "--interactive-success",
    # chrome
    "--titlebar-background",
    "--titlebar-background-focused",
    "--ribbon-background",
    "--tab-container-background",
    "--tab-background-active",
    "--tab-outline-color",
    "--divider-color",
    "--scrollbar-bg",
    "--scrollbar-thumb-bg",
    "--scrollbar-active-thumb-bg",
    # header
    "--header-accent",
    "--header-accent-dark",
    "--header-text",
    "--header-muted",
    "--header-line",
    "--header-bg-soft",
    # blockquote
    "--blockquote-border-color",
    "--blockquote-background-color",
    "--blockquote-color",
    # callout
    "--callout-title-color",
    "--callout-content-color",
    # code
    "--code-background",
    "--code-normal",
    "--code-comment",
    "--code-function",
    "--code-important",
    "--code-keyword",
    "--code-property",
    "--code-punctuation",
    "--code-string",
    "--code-tag",
    "--code-value",
}


def iter_blocks(css: str):
    """Yield (selector, body) at depth 0 across at-rule boundaries.

    Re-implementation of scripts/extract_token_inventory.py's walker, trimmed
    to the parts this generator needs. Comments are stripped during scan.
    """
    i = 0
    n = len(css)
    while i < n:
        if css.startswith("/*", i):
            j = css.find("*/", i + 2)
            if j == -1:
                return
            i = j + 2
            continue
        ch = css[i]
        if ch.isspace():
            i += 1
            continue
        if ch == "@":
            # find header end (`;` or `{`)
            j = i
            while j < n and css[j] not in ";{":
                j += 1
            if j >= n:
                return
            if css[j] == ";":
                i = j + 1
                continue
            depth = 1
            i = j + 1
            block_start = i
            while i < n and depth > 0:
                if css.startswith("/*", i):
                    end = css.find("*/", i + 2)
                    if end == -1:
                        return
                    i = end + 2
                    continue
                c = css[i]
                if c == "{":
                    depth += 1
                elif c == "}":
                    depth -= 1
                    if depth == 0:
                        break
                i += 1
            inner = css[block_start:i]
            for s, b in iter_blocks(inner):
                yield s, b
            i += 1
            continue
        # plain selector block
        sel_start = i
        while i < n and css[i] != "{":
            if css.startswith("/*", i):
                end = css.find("*/", i + 2)
                if end == -1:
                    return
                i = end + 2
                continue
            if css[i] == "}":
                i += 1
                continue
            i += 1
        if i >= n:
            return
        selector = " ".join(css[sel_start:i].split())
        i += 1
        body_start = i
        depth = 1
        while i < n and depth > 0:
            if css.startswith("/*", i):
                end = css.find("*/", i + 2)
                if end == -1:
                    return
                i = end + 2
                continue
            c = css[i]
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    break
            i += 1
        yield selector, css[body_start:i]
        i += 1


def is_global_theme_dark(selector: str) -> bool:
    """True for selectors that target the dark theme globally on a single
    element (no descendant combinator). Examples that match:

    - `.theme-dark`
    - `body.theme-dark`
    - `body:not(.is-mobile).theme-dark`
    - `body.theme-dark.ogd-spacing-relaxed`

    Examples that do NOT match:

    - `body.theme-dark :is(.markdown-rendered, .foo)` (descendant)
    - `.theme-dark .callout` (descendant)
    - `.theme-dark, .theme-light` (comma list — handled by splitting before
      calling this function)
    """
    s = selector.strip()
    if not s:
        return False
    # Reject descendant combinators (any whitespace inside selector).
    if any(ch.isspace() for ch in s):
        return False
    # Reject child / sibling combinators too.
    if any(ch in s for ch in (">", "+", "~")):
        return False
    return ".theme-dark" in s


def split_selector_list(selector: str) -> list[str]:
    """Naively split on top-level commas. CSS does not nest commas inside
    selectors (only inside `:is(...)` etc.), so we respect parens."""
    parts: list[str] = []
    depth = 0
    current: list[str] = []
    for ch in selector:
        if ch == "(":
            depth += 1
            current.append(ch)
        elif ch == ")":
            depth = max(0, depth - 1)
            current.append(ch)
        elif ch == "," and depth == 0:
            parts.append("".join(current).strip())
            current = []
        else:
            current.append(ch)
    if current:
        parts.append("".join(current).strip())
    return [p for p in parts if p]


def main() -> int:
    order = [
        line.strip()
        for line in ORDER_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    ]

    # Group declarations by canonical selector. For each (selector, name) we
    # keep the first value we see (cascade-order-respecting).
    # decls_by_selector: selector -> dict[name -> value]
    decls_by_selector: dict[str, dict[str, str]] = {}
    selector_order: list[str] = []  # preserves first-seen order
    ogd_token_set: set[str] = set()
    core_override_set: set[str] = set()

    for filename in order:
        css_path = DEV / filename
        if not css_path.is_file():
            continue
        css = css_path.read_text(encoding="utf-8")
        for raw_selector, body in iter_blocks(css):
            # A block can have a comma-separated selector list. We process each
            # sub-selector independently because some sub-selectors may target
            # the dark theme globally and some may not.
            for sub_selector in split_selector_list(raw_selector):
                if not is_global_theme_dark(sub_selector):
                    continue
                bucket = decls_by_selector.get(sub_selector)
                if bucket is None:
                    bucket = {}
                    decls_by_selector[sub_selector] = bucket
                    selector_order.append(sub_selector)
                for m in DECL_RE.finditer(body):
                    name = m.group(1)
                    value = " ".join(m.group(2).split())
                    is_ogd = name.startswith("--ogd-")
                    if not is_ogd and name not in CORE_VAR_WHITELIST:
                        continue
                    if name in bucket:
                        continue
                    bucket[name] = value
                    if is_ogd:
                        ogd_token_set.add(name)
                    else:
                        core_override_set.add(name)

    # Drop selectors that ended up with no relevant declarations.
    selector_order = [s for s in selector_order if decls_by_selector[s]]

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    lines.append("/* Owen Graphite v3 — dark theme tokens.")
    lines.append(" *")
    lines.append(" * AUTO-GENERATED by scripts/generate_v3_dark_tokens.py from dev/*.css.")
    lines.append(" * Do not hand-edit. Re-run the generator after touching the dev/ source.")
    lines.append(" *")
    lines.append(" * Selection rule: only `--ogd-*` declarations (plus a small whitelist of")
    lines.append(" * Obsidian core variables) that live in a non-descendant selector that")
    lines.append(" * mentions `.theme-dark`. Descendant overrides live in their respective")
    lines.append(" * surface / feature / theme modules (S5 - S8).")
    lines.append(" *")
    lines.append(f" * Unique --ogd-* tokens: {len(ogd_token_set)}.")
    lines.append(f" * Unique core overrides: {len(core_override_set)}.")
    lines.append(f" * Selector groups: {len(selector_order)}.")
    lines.append(" */")
    lines.append("")

    for sel in selector_order:
        bucket = decls_by_selector[sel]
        ogd = sorted(k for k in bucket if k.startswith("--ogd-"))
        core = sorted(k for k in bucket if not k.startswith("--ogd-"))
        lines.append(f"{sel} {{")
        if core:
            lines.append("  /* core variable overrides */")
            for name in core:
                lines.append(f"  {name}: {bucket[name]};")
            if ogd:
                lines.append("")
        if ogd:
            lines.append("  /* --ogd-* tokens */")
            for name in ogd:
                lines.append(f"  {name}: {bucket[name]};")
        lines.append("}")
        lines.append("")

    OUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(
        f"OK: wrote {OUT_PATH.relative_to(ROOT)} "
        f"({len(ogd_token_set)} unique --ogd-* tokens, "
        f"{len(core_override_set)} core overrides, "
        f"{len(selector_order)} selector groups)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
