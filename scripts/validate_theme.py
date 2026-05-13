#!/usr/bin/env python3
"""Cross-platform validation for the Owen Graphite Obsidian theme."""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import struct
import subprocess
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_STYLE_SETTINGS_OPTIONS = 37
DEFAULT_TARGETS = [
    Path(r"H:\Obsidian\.obsidian\themes\Owen Graphite"),
    Path(r"D:\JAELE\Obsidian\.obsidian\themes\Owen Graphite"),
    Path.home() / "Work" / "Obsidian" / ".obsidian" / "themes" / "Owen Graphite",
    Path.home() / "work" / "Obsidian" / ".obsidian" / "themes" / "Owen Graphite",
]

REQUIRED_FILES = [
    "theme.css",
    "manifest.json",
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
    "dev/MAP/css-stabilization-checklist.md",
    "dev/MAP/map-info-classification.md",
    "dev/MAP/theme-css-risk-map.html",
    "dev/MAP/theme-css-risk-map.json",
    "scripts/analyze_theme_css.py",
    "scripts/bundle_theme.py",
    "scripts/contrast_audit.py",
    "scripts/sync_obsidian_theme.py",
    "scripts/visual_regression.py",
    "dev/README.md",
    "dev/stabilization-optimization-list.md",
    "dev/temp/.gitignore",
    "dev/test-samples/liquid-glass-table-focus-sample.md",
    "dev/test-samples/owen-editor-feature-sample.md",
    "dev/test-samples/owen-graphite-sample.md",
    "docs/css-important-audit.md",
    "docs/fixtures/README.md",
    "docs/fixtures/community-theme-search-focus.html",
    "docs/fixtures/liquid-glass-core-state-matrix.html",
    "docs/fixtures/refero-inspired-glass-states.html",
    "docs/fixtures/right-sidebar-pane-glass.html",
    "docs/liquid-glass-core-principles.md",
    "docs/liquid-glass-token-map.md",
    "docs/qa-checklist.md",
    "dev/_order.txt",
    "dev/00-settings.css",
    "dev/01-tokens.css",
    "dev/02-base-workspace.css",
    "dev/03-reading-content.css",
    "dev/03a-reading-tables-code.css",
    "dev/03b-reading-callouts-lists.css",
    "dev/03c-reading-embeds-workspace.css",
    "dev/04-dark-mode.css",
    "dev/04-print-base.css",
    "dev/05-live-preview.css",
    "dev/06-feature-presets.css",
    "dev/07-plugin-workspace.css",
    "dev/07a-navigation-tasks-search.css",
    "dev/07b-overlay-popover-dataview.css",
    "dev/07c-settings-controls.css",
    "dev/07d-canvas-graph-link-panes.css",
    "dev/07e-live-preview-mobile-plugin.css",
    "dev/08-report-print-polish.css",
    "dev/09a-nav-ribbon-glass.css",
    "dev/09b-editing-menu-tooltip-glass.css",
    "dev/09c-floating-ui-glass-system.css",
    "dev/09d-tabs-file-explorer-search.css",
    "dev/10a-accessibility-motion-contrast.css",
    "dev/10b-late-reading-nav-polish.css",
    "dev/10c-overlay-layout-polish.css",
    "dev/10d-liquid-glass-core.css",
    "dev/10e-html-table-live-preview-glass.css",
    "dev/10-a11y-regression-hotfixes.css",
    "screenshots/light.png",
    "screenshots/dark.png",
    "screenshots/report.png",
    "screenshots/readme/v2.22.31-liquid-glass-overview.svg",
    "screenshots/readme/v2.12-preview-light.png",
    "screenshots/readme/v2.12-preview-dark.png",
]

PNG_SIZES = {
    "screenshots/light.png": (512, 438),
    "screenshots/dark.png": (512, 438),
    "screenshots/report.png": (512, 438),
}

RELEASE_ASSETS = [
    "theme.css",
    "manifest.json",
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
    "dev/MAP/map-info-classification.md",
    "dev/MAP/theme-css-risk-map.html",
    "dev/MAP/theme-css-risk-map.json",
    "screenshots/light.png",
    "screenshots/dark.png",
    "screenshots/report.png",
]

RELEASE_WORKFLOW_ASSETS = [
    asset for asset in RELEASE_ASSETS
]

FORBIDDEN_LIVE_PREVIEW_RULES = {
    re.compile(r"(?:body\s+)?\.markdown-source-view\.mod-cm6\s+\.cm-line\s*\{[^}]*margin-(?:top|bottom)\s*:\s*(?:[1-9]|0\.[1-9]|[a-zA-Z_-])[^;}]*", re.S): "non-zero margin on CM6 .cm-line",
    re.compile(r"(?:body\s+)?\.markdown-source-view\.mod-cm6\s+\.cm-line\s*\{[^}]*line-height\s*:\s*(?:[0-9]|var\(|calc\(|normal\b)[^;}]+", re.S): "global line-height override on CM6 .cm-line",
    re.compile(r"(?:body\s+)?\.markdown-source-view\.mod-cm6\s+\.cm-content\s*\{[^}]*overflow-wrap\s*:\s*anywhere", re.S): "overflow-wrap:anywhere on CM6 .cm-content",
    re.compile(r"(?:body\s+)?\.markdown-source-view\.mod-cm6\s+\.cm-content\s*\{[^}]*word-break\s*:\s*keep-all", re.S): "word-break:keep-all on CM6 .cm-content",
    re.compile(r"(?:body\s+)?\.markdown-source-view\.mod-cm6\s+[^{}]*HyperMD-header-[3-6][^{}]*\{[^}]*z-index\s*:\s*(?:-?\d+|var\()[^;}]+", re.S): "stacking z-index on Live Preview H3-H6",
}

# v2.22.101-108 hit-routing regression family. CM6 block widgets and
# HyperMD-* `.cm-line` variants extend their hit-target across any
# vertical margin/padding — paragraph clicks land in that gap and the
# caret routes to the widget instead of the paragraph. Forbid non-zero
# vertical margin on block widgets and non-zero vertical margin/padding
# on HyperMD-* cm-line variants. The selector must target the element
# DIRECTLY (descendant rules like `.cm-callout .callout-content` are
# allowed to set margin freely).
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
_NONZERO_VALUE_RE = re.compile(r"^\s*(?!0(?:\s|;|$|!|px|em|rem|%))[^;]+")


def _split_top_level_commas(selector_list: str) -> list[str]:
    """Split a comma-separated selector list, ignoring commas inside
    parentheses (e.g. inside `:is(...)` or `:where(...)`)."""
    parts = []
    depth = 0
    current = []
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
    """Return True if any top-level comma-separated selector targets `token`
    directly — i.e. the selector ends with the token (with optional `:pseudo`
    / `.class` / `[attr]` modifiers) at the top level, OR ends with a
    positive `:is(...)`/`:where(...)`/`:matches(...)` group that contains the
    token. Occurrences inside `:not(...)` (negation) or followed by a
    descendant combinator are NOT counted."""
    pseudo_tail_re = re.compile(r"(?:\.[\w-]+|:[\w-]+(?:\([^)]*\))?|\[[^\]]+\])*")
    for sel in _split_top_level_commas(selector_list):
        sel = sel.strip()
        if token not in sel:
            continue
        # Walk char by char tracking a stack of paren contexts. Each entry on
        # the stack is the pseudo-class function name preceding the `(`, or
        # None if the `(` is not directly preceded by `:fname`.
        stack: list[str | None] = []
        i = 0
        n = len(sel)
        last_top_level_end = -1
        # For tracking `:is(...)`-at-tail: record (close_pos, accepts) for each
        # closed positive group containing the token.
        positive_group_closes: list[int] = []
        positive_group_open_at: dict[int, int] = {}
        while i < n:
            ch = sel[i]
            if ch == "(":
                # Find pseudo-class name preceding this paren.
                j = i - 1
                while j >= 0 and (sel[j].isalnum() or sel[j] in "-_"):
                    j -= 1
                fname = sel[j + 1 : i] if j + 1 < i and j >= 0 and sel[j] == ":" else None
                stack.append(fname)
                if fname in ("is", "where", "matches"):
                    positive_group_open_at[len(stack) - 1] = i
                i += 1
                continue
            if ch == ")":
                if stack:
                    depth_idx = len(stack) - 1
                    fname = stack.pop()
                    # Nothing else to record here.
                i += 1
                continue
            if sel.startswith(token, i) and (
                token.startswith(".") or i == 0 or not (sel[i - 1].isalnum() or sel[i - 1] in "-_")
            ):
                end = i + len(token)
                # Only count if every enclosing paren context is positive
                # (`:is`/`:where`/`:matches`). If any enclosing context is
                # `:not` or a non-pseudo paren, skip.
                if all(name in ("is", "where", "matches") for name in stack):
                    if not stack:
                        last_top_level_end = end
                    else:
                        # Inside a positive group — the group's closing paren
                        # must terminate the selector (with only pseudo tail).
                        # We'll evaluate after the loop using positive_group_open_at.
                        # Mark the outermost positive group containing this token.
                        outermost = 0
                        positive_group_closes.append(outermost)  # placeholder; recomputed below
                i = end
                continue
            i += 1
        if last_top_level_end >= 0:
            tail = sel[last_top_level_end:]
            if pseudo_tail_re.fullmatch(tail):
                return True
        # Fallback: detect `...:is(... token ...)<pseudo-tail>$` pattern by a
        # second, simpler scan — find each `:is(...)`/`:where(...)`/`:matches(...)`
        # group at the outermost level, check if it contains the token (outside
        # `:not`), and if its close is followed only by a pseudo tail.
        for grp_match in re.finditer(r":(?:is|where|matches)\(", sel):
            start = grp_match.end() - 1  # position of `(`
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
            close_pos = j  # position right after `)`
            inner = sel[start + 1 : close_pos - 1]
            # Strip out `:not(...)` sub-groups inside `inner` to avoid matching
            # negated tokens.
            inner_stripped = re.sub(r":not\([^)]*\)", "", inner)
            # Check that any top-level comma-separated alt in inner ends with token.
            for alt in _split_top_level_commas(inner_stripped):
                alt = alt.strip()
                if token not in alt:
                    continue
                # alt ends with token + pseudo tail?
                idx = alt.rfind(token)
                tail = alt[idx + len(token) :]
                if pseudo_tail_re.fullmatch(tail):
                    # And the `:is(...)` group must terminate the selector.
                    selector_tail = sel[close_pos:]
                    if pseudo_tail_re.fullmatch(selector_tail):
                        return True
    return False


def _has_nonzero_vertical_box(body: str, properties: tuple) -> str | None:
    """Return the offending property declaration if `body` declares a non-zero
    vertical margin/padding among `properties`, else None."""
    for decl in body.split(";"):
        decl = decl.strip()
        if not decl or ":" not in decl:
            continue
        prop, _, value = decl.partition(":")
        prop = prop.strip().lower()
        value = value.strip()
        if prop not in properties:
            continue
        # margin/padding shorthand: top is value[0], bottom is value[2] (or [0])
        # We flag if any of top/bottom is non-zero.
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


def _is_nonzero(value: str) -> bool:
    value = value.strip()
    if not value:
        return False
    if value in ("0", "auto"):
        return False
    if re.fullmatch(r"0(?:px|em|rem|%|vh|vw|pt)", value):
        return False
    return True


def live_preview_hit_routing_audit(content: str, source_label: str) -> None:
    """Scan top-level CSS rules and flag any rule whose selector targets a
    Live Preview block widget or HyperMD-* cm-line variant directly and
    declares a non-zero vertical margin (widgets) or non-zero vertical
    margin/padding (cm-line variants).

    Additional categories codify recurring CM6 hit-routing regressions
    (v2.22.99–108):
      - active line: `.cm-active.cm-line`, `.cm-focused .cm-active` must
        not declare `outline`, `box-shadow`, `transform`, vertical
        padding — these all extend the hit-target or create visual
        overlays that capture clicks.
      - embed BFC: `.cm-embed-block`, `.cm-html-embed` must not declare
        the lethal `overflow-x:auto + max-width:100%` BFC pair, which
        creates a hit-target gap above tables/embeds.
      - content overflow: `.cm-content`, `.cm-line` must not be forced
        to `pointer-events:none` (kills click-to-edit on rendered text).

    Multiple violations are accumulated and reported together so a single
    pass surfaces every regression a patch introduces.
    """
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
        # Only consider rules anchored to the CM6 editor scope.
        if "markdown-source-view.mod-cm6" not in selectors:
            continue
        # Category 1: block widget — non-zero vertical margin.
        for token in LIVE_PREVIEW_WIDGET_DIRECT_TOKENS:
            if _selector_targets_token_directly(selectors, token):
                offender = _has_nonzero_vertical_box(body, margin_props)
                if offender:
                    failures.append(
                        f"non-zero vertical margin on CM6 block widget ({token}) — "
                        f"bleeds hit-target. Body: `{offender}`. Move spacing to "
                        f"the natural blank `.cm-line` between blocks."
                    )
                break
        # Category 2: HyperMD-* cm-line variant — non-zero vertical margin/padding.
        for token in LIVE_PREVIEW_HYPERMD_DIRECT_TOKENS:
            if _selector_targets_token_directly(selectors, token):
                offender = _has_nonzero_vertical_box(body, margin_padding_props)
                if offender:
                    failures.append(
                        f"non-zero vertical margin/padding on HyperMD-* cm-line "
                        f"({token}) — bleeds hit-target. Body: `{offender}`."
                    )
                break
        # Category 3: active line — outline/box-shadow/transform forbidden.
        for token in (".cm-active.cm-line", ".cm-active .cm-line"):
            if _selector_targets_token_directly(selectors, token):
                bad = _declares_any(
                    body,
                    ("outline", "box-shadow", "transform",
                     "padding", "padding-top", "padding-bottom"),
                )
                if bad:
                    failures.append(
                        f"forbidden visual on active CM6 line ({token}) — "
                        f"`{bad}`. Active line outline/shadow/transform/vertical "
                        f"padding extends the hit-target and steals clicks "
                        f"(v2.22.104 regression)."
                    )
                break
        # Category 4: embed BFC pair on .cm-embed-block.
        for token in (".cm-embed-block", ".cm-html-embed"):
            if _selector_targets_token_directly(selectors, token):
                if _declares_pair(body, "overflow-x", "auto") and \
                        _declares_pair(body, "max-width", "100%"):
                    failures.append(
                        f"lethal BFC pair on embed wrapper ({token}) — "
                        f"`overflow-x:auto + max-width:100%`. Creates the "
                        f"v2.22.106 hit-target gap above tables/embeds."
                    )
                break
        # Category 5: pointer-events:none on .cm-content / .cm-line text.
        for token in (".cm-content", ".cm-line"):
            if _selector_targets_token_directly(selectors, token):
                if re.search(r"pointer-events\s*:\s*none\b", body):
                    failures.append(
                        f"pointer-events:none on rendered CM6 text ({token}) — "
                        f"kills click-to-edit. Use native `.cm-line * {{ pointer-events: auto }}` instead."
                    )
                break
    if failures:
        joined = "\n  - ".join(failures)
        fail(f"{source_label}: Live Preview hit-routing regressions:\n  - {joined}")


def _declares_any(body: str, properties: tuple) -> str | None:
    """Return the first declaration whose property is in `properties` and
    whose value is non-zero / non-`none`."""
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
    """Check if `body` declares `prop: ...value_token...`."""
    pattern = re.compile(rf"\b{re.escape(prop)}\s*:\s*[^;]*\b{re.escape(value_token)}\b")
    return bool(pattern.search(body))

FORBIDDEN_READING_VIEW_RULES = {
    re.compile(r"\.markdown-rendered\s*\{[^}]*overflow-wrap\s*:\s*anywhere", re.S): "overflow-wrap:anywhere on global .markdown-rendered",
}

REQUIRED_READING_VIEW_GUARDS = [
    "body .markdown-preview-section > div",
    "body .markdown-rendered > div",
    "body .markdown-rendered p",
    "overflow-wrap: break-word !important",
]

REQUIRED_LIVE_PREVIEW_WIDTH_GUARDS = [
    "body .markdown-source-view.mod-cm6 .cm-sizer",
    "body .markdown-source-view.mod-cm6 .cm-contentContainer",
    "body .markdown-source-view.mod-cm6 .cm-content",
    "body .markdown-source-view.mod-cm6 .cm-line",
    "align-self: stretch !important",
    "min-height: calc(100vh - 220px) !important",
    "cursor: text !important",
]

REQUIRED_READABLE_COLUMN_GUARDS = [
    "body .markdown-preview-view.is-readable-line-width .markdown-preview-sizer",
    "body .markdown-reading-view.is-readable-line-width .markdown-preview-sizer",
    "body .markdown-source-view.is-readable-line-width .cm-contentContainer",
    "body .markdown-source-view.is-readable-line-width .cm-sizer",
    "body .markdown-rendered.is-readable-line-width",
    ":is(.markdown-preview-sizer, .markdown-preview-section, .cm-sizer, .cm-contentContainer, .CodeMirror-sizer, .cm-content)",
    "margin-left: 0 !important",
    "margin-right: auto !important",
]

REQUIRED_TABLE_INFLATION_GUARDS = [
    ".cm-embed-block table :is(td, th) > p",
    ".cm-embed-block.cm-table-widget",
    ".table-cell-wrapper,",
    ".cm-active.cm-line",
    ".cm-active.cm-line:empty",
    "line-height: 0 !important",
]

TABLE_INFLATION_HEADER_GUARD_PATTERNS = {
    re.compile(
        r"\)\s*:is\(\s*td\s*,\s*th\s*\)\s*:is\(\s*"
        r"\.table-cell-wrapper\s*,\s*\.cm-editor\s*,\s*\.cm-scroller\s*,\s*"
        r"\.cm-content\s*,\s*\.cm-line\s*,\s*\.cm-active\.cm-line",
        re.S,
    ): "editable table body/header cell editor chain reset",
    re.compile(
        r"\)\s*:is\(\s*table\s*,\s*thead\s*,\s*tbody\s*,\s*tr\s*,\s*td\s*,\s*th\s*\)\s*\{\s*"
        r"min-height:\s*0\s*!important;\s*height:\s*auto\s*!important;",
        re.S,
    ): "table structure reset includes thead/th",
    re.compile(
        r"\)\s*:is\(\s*td\s*,\s*th\s*\)\s*:is\(\s*"
        r"\.cm-line:empty\s*,\s*\.cm-active\.cm-line:empty",
        re.S,
    ): "empty trailing line reset covers body/header cells",
    re.compile(
        r"\)\s*:is\(\s*td\s*,\s*th\s*\)\s*:is\(\s*"
        r"\.cm-line:has\(br:only-child\)\s*,\s*\.cm-active\.cm-line:has\(br:only-child\)",
        re.S,
    ): "br-only trailing line reset covers body/header cells",
}

EDITABLE_TABLE_SAMPLE_SECTIONS = [
    "Risk Matrix",
    "Numeric Metrics",
]

LIQUID_GLASS_SMOKE_SECTIONS = [
    "Wiki Table Baseline",
    "Report Table Baseline",
    "Frost Aqua Focus Sweep",
]

README_REPRESENTATIVE_SVG = "screenshots/readme/v2.22.31-liquid-glass-overview.svg"

LIQUID_GLASS_FOCUS_GUARDS = [
    ".clickable-icon",
    ".view-action",
    ".editingToolbarButton",
    ".document-search-container",
    ".workspace-tab-header",
    ".nav-file-title",
    ".nav-folder-title",
    ".tree-item-self",
    ".vertical-tab-nav-item",
    ".setting-item",
    ".metadata-property",
    "--ogd-lg-frost-rim",
    "--ogd-lg-frost-halo",
    "--ogd-lg-shadow-focus",
]

CORE_CHROME_PROTECTED_SELECTOR_LABELS = {
    "[role=tab]",
    ".workspace-tabs",
    ".workspace-tab-header-container",
    ".workspace-tab-header",
    ".workspace-tab-container",
    ".titlebar",
    ".titlebar-button",
    ".sidebar-toggle-button",
    ".workspace-ribbon",
    ".workspace-ribbon-collapse-btn",
    ".side-dock-ribbon",
}

CORE_CHROME_STRUCTURAL_PROPERTIES = {
    "display",
    "visibility",
    "opacity",
    "height",
    "width",
    "min-height",
    "max-height",
    "min-width",
    "max-width",
    "overflow",
    "overflow-x",
    "overflow-y",
    "position",
    "top",
    "right",
    "bottom",
    "left",
    "inset",
    "z-index",
    "transform",
    "translate",
    "scale",
    "pointer-events",
    "flex",
    "flex-direction",
    "flex-basis",
    "flex-grow",
    "flex-shrink",
    "order",
    "grid-area",
}

PRINT_BLOCK_OWNERSHIP = {
    "dev/04-print-base.css": 1,
    "dev/06-feature-presets.css": 2,
    "dev/07-plugin-workspace.css": 2,
    "dev/07e-live-preview-mobile-plugin.css": 1,
    "dev/08-report-print-polish.css": 2,
    "dev/09c-floating-ui-glass-system.css": 1,
    "dev/10b-late-reading-nav-polish.css": 2,
    "dev/10c-overlay-layout-polish.css": 1,
}

MAX_DEV_MODULE_LINES = 1500
MAX_DEV_MODULE_IMPORTANT = 550


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def ok(message: str) -> None:
    print(f"OK: {message}")


def read_text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def required_files() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file() or (ROOT / path).stat().st_size == 0]
    if missing:
        fail(f"missing required files: {', '.join(missing)}")
    ok("required files present")


def manifest_and_versions() -> str:
    manifest = json.loads(read_text("manifest.json"))
    version = manifest.get("version", "")
    version_re = r"\d+\.\d+(?:\.\d+)?"
    if not re.fullmatch(version_re, version):
        fail(f"manifest version must be X.Y or X.Y.Z, got {version!r}")
    if manifest.get("name") != "Owen Graphite":
        fail("manifest name mismatch")
    if not manifest.get("minAppVersion"):
        fail("manifest missing minAppVersion")
    ok(f"manifest.json version={version}")

    changelog = read_text("CHANGELOG.md")
    readme = read_text("README.md")
    changelog_match = re.search(rf"^## \[({version_re})\]", changelog, flags=re.M)
    if not changelog_match:
        fail("CHANGELOG missing latest version header")
    if changelog_match.group(1) != version:
        fail(f"CHANGELOG latest header {changelog_match.group(1)} does not match manifest {version}")
    readme_match = re.search(rf"\| \*\*버전\*\* \| `({version_re})`", readme)
    if not readme_match:
        fail("README missing top-level version row")
    if readme_match.group(1) != version:
        fail(f"README version {readme_match.group(1)} does not match manifest {version}")
    if f"| **v{version}** |" not in readme:
        fail(f"README change log table missing latest row for v{version}")
    ok("version markers aligned")
    return version


def no_stale_legacy_markers() -> None:
    legacy_pattern = re.compile(r"v?1\.7\.6")
    stale_hits: list[str] = []
    skip_dirs = {
        ".git",
        ".venv",
        "dist",
        "__pycache__",
        ".mypy_cache",
        ".pytest_cache",
        ".ruff_cache",
        ".idea",
        ".vscode",
    }
    max_scan_bytes = 1_500_000
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT).as_posix()
        if path.is_dir() or rel == ".DS_Store":
            continue
        if any(part in skip_dirs for part in path.parts):
            continue
        try:
            if path.stat().st_size > max_scan_bytes:
                continue
        except OSError:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if legacy_pattern.search(content):
            stale_hits.append(rel)
    if stale_hits:
        fail(f"stale legacy marker found in: {', '.join(stale_hits)}")
    ok("no stale legacy markers")


def style_settings_count() -> None:
    theme = read_text("theme.css")
    readme = read_text("README.md")
    settings_match = re.search(r"/\* @settings(?P<body>.*?)\*/", theme, flags=re.S)
    if not settings_match:
        fail("theme.css missing Style Settings block")
    body = settings_match.group("body")
    # YAML lint: every `description:` / `title:` / `default:` value that begins
    # with a YAML-special character (backtick, *, &, !, |, >, %, @, ?, :, -, #)
    # must be quoted, otherwise the Style Settings plugin (js-yaml) raises
    # bad-indentation errors which silently break the entire UI.
    YAML_SPECIAL_PREFIX = set("`*&!|>%@?:-#")
    for lineno, line in enumerate(body.splitlines(), start=1):
        m = re.match(r"\s*(description|title|default):\s*(.+)$", line)
        if not m:
            continue
        key, value = m.group(1), m.group(2).strip()
        if not value:
            continue
        # Already quoted -> ok.
        if value.startswith(('"', "'")):
            continue
        # Numeric/bool/null literals are fine.
        if re.fullmatch(r"-?\d+(\.\d+)?|true|false|null|on|off|yes|no", value, re.I):
            continue
        if value[0] in YAML_SPECIAL_PREFIX:
            fail(
                f"@settings {key} starts with YAML-special char {value[0]!r} "
                f"and must be quoted (line {lineno} inside @settings block): {value[:60]}"
            )
    blocks = re.split(r"\n\s*-\s*\n", body)
    option_ids = []
    for block in blocks:
        id_match = re.search(r"^\s*id:\s*([a-zA-Z0-9_-]+)", block, flags=re.M)
        if not id_match or id_match.group(1) == "owen-graphite-document":
            continue
        type_match = re.search(r"^\s*type:\s*([a-zA-Z0-9_-]+)", block, flags=re.M)
        if type_match and type_match.group(1) == "heading":
            continue
        option_ids.append(id_match.group(1))
    option_count = len(set(option_ids))
    if option_count != EXPECTED_STYLE_SETTINGS_OPTIONS:
        fail(f"expected {EXPECTED_STYLE_SETTINGS_OPTIONS} Style Settings options, got {option_count}")
    if f"{EXPECTED_STYLE_SETTINGS_OPTIONS}개 옵션" not in readme or f"{EXPECTED_STYLE_SETTINGS_OPTIONS}%20options" not in readme:
        fail(f"README missing {EXPECTED_STYLE_SETTINGS_OPTIONS} options text/badge")
    ok(f"Style Settings option count={option_count} (YAML lint clean)")


def style_settings_binding_guards() -> None:
    theme = read_text("theme.css")
    settings_match = re.search(r"/\* @settings(?P<body>.*?)\*/", theme, flags=re.S)
    if not settings_match:
        fail("theme.css missing Style Settings block")
    settings_body = settings_match.group("body")
    css_body = theme[: settings_match.start()] + theme[settings_match.end() :]

    failures: list[str] = []
    blocks = re.split(r"\n\s*-\s*\n", settings_body)
    for block in blocks:
        id_match = re.search(r"^\s*id:\s*([a-zA-Z0-9_-]+)", block, flags=re.M)
        type_match = re.search(r"^\s*type:\s*([a-zA-Z0-9_-]+)", block, flags=re.M)
        if not id_match or not type_match:
            continue
        setting_id = id_match.group(1)
        setting_type = type_match.group(1)
        if setting_id == "owen-graphite-document" or setting_type == "heading":
            continue

        if setting_type == "class-toggle":
            if f".{setting_id}" not in css_body:
                failures.append(f"{setting_id}: class-toggle has no CSS selector")
        elif setting_type == "class-select":
            values = re.findall(r"^\s*value:\s*([a-zA-Z0-9_-]+)", block, flags=re.M)
            missing = [value for value in values if f".{value}" not in css_body]
            if missing:
                failures.append(f"{setting_id}: class-select values missing CSS selectors: {', '.join(missing)}")
        elif setting_type.startswith("variable-"):
            if f"--{setting_id}" not in css_body:
                failures.append(f"{setting_id}: variable setting has no CSS variable usage")

    if failures:
        fail("Style Settings binding guards failed:\n" + "\n".join(failures))
    ok("Style Settings bindings clean")


def png_dimensions() -> None:
    for path, expected in PNG_SIZES.items():
        data = (ROOT / path).read_bytes()[:24]
        if not data.startswith(b"\x89PNG\r\n\x1a\n"):
            fail(f"{path} is not a PNG")
        width, height = struct.unpack(">II", data[16:24])
        if (width, height) != expected:
            fail(f"{path} expected {expected[0]}x{expected[1]}, got {width}x{height}")
    ok("screenshot PNG dimensions match expected sizes")


def readme_svg_asset_guards() -> None:
    readme = read_text("README.md")
    links = re.findall(r"!\[[^\]]+\]\((screenshots/readme/[^)\s]+?\.svg)(?:\?[^)]*)?\)", readme)
    if README_REPRESENTATIVE_SVG not in links:
        fail(f"README missing representative SVG: {README_REPRESENTATIVE_SVG}")

    failures: list[str] = []
    for rel in sorted(set(links)):
        path = ROOT / rel
        if not path.is_file():
            failures.append(f"{rel}: referenced SVG is missing")
            continue
        content = path.read_text(encoding="utf-8")
        if "<svg" not in content[:300]:
            failures.append(f"{rel}: missing <svg> root near start")
        if not re.search(r"\bwidth=\"\d+\"", content) or not re.search(r"\bheight=\"\d+\"", content):
            failures.append(f"{rel}: missing numeric width/height")
        if "viewBox=" not in content:
            failures.append(f"{rel}: missing viewBox")
        if re.search(r"\brx=\"[^\"]*\s+[^\"]*\"", content):
            failures.append(f"{rel}: rx must not use CSS shorthand values")

    representative = read_text(README_REPRESENTATIVE_SVG)
    required_labels = ["<title", "<desc", "위키형 표", "보고서형 표", "프로스트 아쿠아 포커스"]
    missing_labels = [label for label in required_labels if label not in representative]
    if missing_labels:
        failures.append(f"{README_REPRESENTATIVE_SVG}: missing labels: {', '.join(missing_labels)}")

    if failures:
        fail("README SVG guards failed:\n" + "\n".join(failures))
    ok(f"README SVG guards clean ({len(set(links))} SVG links)")


def visual_regression_script_guards() -> None:
    script = read_text("scripts/visual_regression.py")
    required_tokens = [
        README_REPRESENTATIVE_SVG,
        "docs/fixtures/community-theme-search-focus.html",
        "docs/fixtures/right-sidebar-pane-glass.html",
        "README_SVG_REQUIRED_TEXT",
        "HTML_FIXTURE_REQUIRED_TEXT",
        "dev/temp/visual-regression",
        "smoke_svg_page",
        "smoke_html_page",
        "위키형 표",
        "보고서형 표",
        "프로스트 아쿠아 포커스",
        "커뮤니티 테마 검색 calm focus",
        "오른쪽 pane glass parity",
        "백링크 설명 카드",
        "Explicit Light",
        "Explicit Dark",
    ]
    missing = [token for token in required_tokens if token not in script]
    if missing:
        fail(f"scripts/visual_regression.py missing README SVG smoke guards: {', '.join(missing)}")
    ok("visual regression README SVG smoke guards clean")


def release_workflow_assets() -> None:
    workflow = read_text(".github/workflows/release.yml")
    validate_workflow = read_text(".github/workflows/validate.yml")
    missing = [asset for asset in RELEASE_WORKFLOW_ASSETS if not re.search(rf"^\s+{re.escape(asset)}\s*$", workflow, flags=re.M)]
    if missing:
        fail(f"release workflow missing assets: {', '.join(missing)}")
    if re.search(r"^\s+docs/fixtures/README\.md\s*$", workflow, flags=re.M):
        fail("release workflow must not upload docs/fixtures/README.md separately because it collides with README.md")
    if "dist/Owen-Graphite-*.zip" not in workflow:
        fail("release workflow missing generated zip asset")
    if "python scripts/validate_theme.py --ci" not in workflow:
        fail("release workflow must run Python validator")
    if "python scripts/build_release.py" not in workflow:
        fail("release workflow must build release ZIP with Python")
    if validate_workflow.count("python scripts/validate_theme.py --ci") != 1:
        fail("validate workflow must call the Python validator exactly once")
    if any(token in validate_workflow for token in ["jq ", "ruby", "validate_theme.rb"]):
        fail("validate workflow should rely on Python validation only")
    ok("release workflow includes theme files and zip asset")


def python_only_scripts() -> None:
    ruby_scripts = sorted(path.relative_to(ROOT).as_posix() for path in (ROOT / "scripts").glob("*.rb"))
    if ruby_scripts:
        fail(f"Ruby scripts are not allowed: {', '.join(ruby_scripts)}")
    gitignore = read_text(".gitignore")
    required_ignores = ["dist/", ".venv/", "__pycache__/", "*.py[cod]", "dev/temp/*", "!dev/temp/.gitignore"]
    missing = [item for item in required_ignores if item not in gitignore]
    if missing:
        fail(f".gitignore missing Python/release artifacts: {', '.join(missing)}")
    ok("scripts are Python-only and local artifacts are ignored")


def dev_temp_policy() -> None:
    temp_ignore = read_text("dev/temp/.gitignore")
    required_rules = ["*", "!.gitignore"]
    missing = [rule for rule in required_rules if rule not in temp_ignore.splitlines()]
    if missing:
        fail(f"dev/temp/.gitignore missing temp cleanup rules: {', '.join(missing)}")
    visual_output = ROOT / "dev" / "temp" / "visual-regression"
    if visual_output.exists():
        leftovers = sorted(
            path.relative_to(ROOT).as_posix()
            for path in visual_output.rglob("*")
            if path.is_file()
        )
        if leftovers:
            fail("visual regression temp output must be cleaned before validation: " + ", ".join(leftovers))
    result = subprocess.run(["git", "ls-files", "dev/temp"], cwd=ROOT, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        fail(f"unable to inspect tracked dev/temp files:\n{result.stdout}{result.stderr}")
    allowed = {"dev/temp/.gitignore"}
    tracked = {line.strip().replace("\\", "/") for line in result.stdout.splitlines() if line.strip()}
    extra = sorted(tracked - allowed)
    if extra:
        fail(f"dev/temp must stay empty in commits: {', '.join(extra)}")
    ok("dev/temp request artifact policy clean")


def git_tracking_policy() -> None:
    if not (ROOT / ".git").exists():
        ok("git tracking policy skipped")
        return

    result = subprocess.run(["git", "ls-files"], cwd=ROOT, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        fail(f"unable to inspect tracked files:\n{result.stdout}{result.stderr}")
    tracked = {line.strip().replace("\\", "/") for line in result.stdout.splitlines() if line.strip()}
    missing_required = [path for path in REQUIRED_FILES if path not in tracked]
    if missing_required:
        fail("required files must be tracked by Git: " + ", ".join(missing_required))

    required_gitignore_exceptions = [
        "!docs/fixtures/**",
        "!docs/qa-checklist.md",
        "!docs/css-important-audit.md",
        "!docs/liquid-glass-token-map.md",
    ]
    gitignore = read_text(".gitignore")
    missing_exceptions = [item for item in required_gitignore_exceptions if item not in gitignore]
    if missing_exceptions:
        fail(".gitignore missing docs fixture exceptions: " + ", ".join(missing_exceptions))

    probe = subprocess.run(
        ["git", "check-ignore", "-q", "--", "docs/fixtures/new-fixture-policy-probe.html"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if probe.returncode == 0:
        fail("docs/fixtures/*.html must not be ignored; new fixtures should not require git add -f")
    if probe.returncode not in {0, 1}:
        fail(f"unable to check docs fixture ignore policy:\n{probe.stdout}{probe.stderr}")
    ok("git tracking and docs fixture ignore policy clean")


def dev_bundle_current() -> None:
    script = ROOT / "scripts" / "bundle_theme.py"
    spec = importlib.util.spec_from_file_location("bundle_theme", script)
    if spec is None or spec.loader is None:
        fail("unable to load scripts/bundle_theme.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    if (ROOT / "theme.css").read_bytes() != module.bundle_bytes():
        fail("theme.css is not up to date with dev CSS modules; run scripts/bundle_theme.py")
    ok("dev CSS bundle matches theme.css")


def dev_css_module_set_clean() -> None:
    script = ROOT / "scripts" / "bundle_theme.py"
    spec = importlib.util.spec_from_file_location("bundle_theme", script)
    if spec is None or spec.loader is None:
        fail("unable to load scripts/bundle_theme.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    ordered_paths = module.ordered_module_paths()
    ordered_rel = [path.relative_to(ROOT).as_posix() for path in ordered_paths]
    duplicate_rel = sorted({path for path in ordered_rel if ordered_rel.count(path) > 1})
    if duplicate_rel:
        fail(f"duplicate CSS modules in dev/_order.txt: {', '.join(duplicate_rel)}")

    listed = set(ordered_rel)
    actual = sorted(path.relative_to(ROOT).as_posix() for path in (ROOT / "dev").glob("*.css"))
    orphan = [path for path in actual if path not in listed]
    if orphan:
        fail(f"dev CSS files not listed in dev/_order.txt: {', '.join(orphan)}")
    ok(f"dev CSS module set clean ({len(ordered_rel)} modules)")


def css_regression_guards() -> None:
    css_paths = sorted((ROOT / "dev").glob("*.css")) + [ROOT / "theme.css"]
    forbidden = [
        (re.compile(r"\.theme-dark\s+body\."), "invalid .theme-dark body.* selector"),
        (re.compile(r"transition\s*:\s*all\b", re.I), "transition: all"),
        (re.compile(r"transform\s*:\s*translateY\(-(?:2|1|0\.5)px\)"), "direct hover lift transform; use --ogd-hover-lift variables"),
        (re.compile(r"transform\s*:\s*translateX\((?:1|0\.5)px\)"), "direct hover shift transform; use --ogd-hover-shift variables"),
        (re.compile(r"transform\s*:\s*translateY\(0\)\s*scale\(0\.99\)"), "direct press lift transform; use --ogd-press-lift"),
    ]
    failures: list[str] = []
    for path in css_paths:
        rel = path.relative_to(ROOT).as_posix()
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            for pattern, description in forbidden:
                if pattern.search(line):
                    failures.append(f"{rel}:{lineno}: {description}")
    if failures:
        fail("CSS regression guards failed:\n" + "\n".join(failures))
    ok("CSS regression guards clean")


def core_chrome_structure_guards() -> None:
    script = ROOT / "scripts" / "analyze_theme_css.py"
    spec = importlib.util.spec_from_file_location("analyze_theme_css", script)
    if spec is None or spec.loader is None:
        fail("unable to load scripts/analyze_theme_css.py")
    analyzer = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = analyzer
    spec.loader.exec_module(analyzer)

    failures: list[str] = []
    for path in sorted((ROOT / "dev").glob("*.css")):
        rel = path.relative_to(ROOT).as_posix()
        rules = analyzer.parse_rules(path.read_text(encoding="utf-8"))
        for rule in rules:
            if "@media print" in rule.context:
                continue
            if "prefers-reduced-motion" in rule.context and "reduce" in rule.context:
                continue
            selector_labels = {label for label, _ in analyzer.matched_core_selectors(rule.selector)}
            protected_labels = selector_labels & CORE_CHROME_PROTECTED_SELECTOR_LABELS
            if not protected_labels:
                continue
            for declaration in rule.declarations:
                if declaration.property_name not in CORE_CHROME_STRUCTURAL_PROPERTIES:
                    continue
                failures.append(
                    f"{rel}:{declaration.line}: {', '.join(sorted(protected_labels))} "
                    f"must not set {declaration.property_name}: {declaration.value} "
                    f"in selector {rule.selector!r}"
                )

    if failures:
        fail("core chrome structure guards failed:\n" + "\n".join(failures))
    ok("core chrome structure guards clean")


def css_has_guards() -> None:
    css_paths = sorted((ROOT / "dev").glob("*.css")) + [ROOT / "theme.css"]
    failures: list[str] = []
    for path in css_paths:
        rel = path.relative_to(ROOT).as_posix()
        support_stack: list[bool] = []
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            has_support_header = "@supports" in line and "selector(" in line and ":has(" in line
            if ":has(" in line and not has_support_header and not any(support_stack):
                failures.append(f"{rel}:{lineno}: :has() selector must be wrapped in @supports selector(...)")

            next_open_support = has_support_header
            for char in line:
                if char == "{":
                    inherited = support_stack[-1] if support_stack else False
                    support_stack.append(next_open_support or inherited)
                    next_open_support = False
                elif char == "}" and support_stack:
                    support_stack.pop()

    if failures:
        fail("CSS :has() guards failed:\n" + "\n".join(failures))
    ok("CSS :has() guards clean")


def css_print_ownership_guards() -> None:
    css_paths = sorted((ROOT / "dev").glob("*.css"))
    failures: list[str] = []
    total_blocks = 0
    for path in css_paths:
        rel = path.relative_to(ROOT).as_posix()
        content = path.read_text(encoding="utf-8")
        print_count = len(re.findall(r"@media\s+print\b", content))
        total_blocks += print_count
        expected = PRINT_BLOCK_OWNERSHIP.get(rel, 0)
        if print_count != expected:
            if expected:
                failures.append(f"{rel}: expected {expected} @media print block(s), found {print_count}")
            elif print_count:
                failures.append(f"{rel}: unexpected @media print block(s); use an approved print owner module")

    missing_owner_files = [rel for rel in PRINT_BLOCK_OWNERSHIP if not (ROOT / rel).is_file()]
    if missing_owner_files:
        failures.extend(f"{rel}: print owner file is missing" for rel in missing_owner_files)

    theme_count = len(re.findall(r"@media\s+print\b", read_text("theme.css")))
    if theme_count != total_blocks:
        failures.append(f"theme.css: expected {total_blocks} bundled @media print block(s), found {theme_count}")

    if failures:
        fail("CSS print ownership guards failed:\n" + "\n".join(failures))
    ok(f"CSS print ownership clean ({total_blocks} blocks)")


def css_risk_inventory() -> None:
    module_paths = sorted((ROOT / "dev").glob("*.css"))
    direct_backdrop = 0
    has_selectors = 0
    has_support_probes = 0
    print_blocks: list[str] = []
    for path in module_paths:
        content = path.read_text(encoding="utf-8")
        direct_backdrop += sum(
            len(re.findall(r"backdrop-filter\s*:\s*blur\(", line))
            for line in content.splitlines()
            if "@supports" not in line
        )
        has_selectors += sum(line.count(":has(") for line in content.splitlines() if "@supports" not in line)
        has_support_probes += sum(line.count(":has(") for line in content.splitlines() if "@supports" in line)
        print_count = len(re.findall(r"@media\s+print\b", content))
        if print_count:
            print_blocks.append(f"{path.name}={print_count}")

    theme = read_text("theme.css")
    required_glass_guards = [
        "body:not(.is-mobile):is(.ogd-glass-off, .ogd-glass-reduced)",
        ".menu .menu-item",
        ".tooltip",
        ".suggestion-container",
        "backdrop-filter: none !important",
    ]
    missing = [guard for guard in required_glass_guards if guard not in theme]
    if missing:
        fail(f"theme.css missing glass fallback guards: {', '.join(missing)}")

    print_summary = ", ".join(print_blocks) if print_blocks else "none"
    ok(
        "CSS risk inventory: "
        f"direct backdrop-filter={direct_backdrop}, "
        f":has()={has_selectors}, "
        f":has supports={has_support_probes}, "
        f"print blocks=({print_summary})"
    )


def css_variable_usage_guards() -> None:
    failures: list[str] = []
    glass_paths = sorted((ROOT / "dev").glob("09*.css")) + [ROOT / "theme.css"]
    for path in glass_paths:
        rel = path.relative_to(ROOT).as_posix()
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            stripped = line.strip()
            if "backdrop-filter:" not in stripped or "@supports" in stripped:
                continue
            if "none" in stripped or "var(--ogd-glass-filter" in stripped:
                continue
            failures.append(f"{rel}:{lineno}: backdrop-filter must use --ogd-glass-filter variables or none")

    theme = read_text("theme.css")
    required_design_tokens = [
        "--ogd-glass-surface-bg:",
        "--ogd-glass-toolbar-bg:",
        "--ogd-glass-control-bg:",
        "--ogd-glass-control-hover-bg:",
        "--ogd-hover-lift:",
        "--ogd-hover-lift-subtle:",
        "--ogd-hover-shift:",
        "--ogd-press-lift:",
        "body.ogd-motion-off",
        "body.ogd-motion-subtle",
        "body.ogd-motion-standard",
    ]
    missing = [token for token in required_design_tokens if token not in theme]
    if missing:
        failures.append(f"theme.css missing glass/motion tokens/classes: {', '.join(missing)}")

    if failures:
        fail("CSS variable usage guards failed:\n" + "\n".join(failures))
    ok("CSS variable usage guards clean")


def _unescaped_quote_count(line: str) -> int:
    count = 0
    escaped = False
    for char in line:
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == '"':
            count += 1
    return count


def css_string_sanity_guards() -> None:
    failures: list[str] = []
    css_paths = sorted((ROOT / "dev").glob("*.css")) + [ROOT / "theme.css"]
    for path in css_paths:
        rel = path.relative_to(ROOT).as_posix()
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if "content:" not in line:
                continue
            if _unescaped_quote_count(line) % 2:
                failures.append(f"{rel}:{lineno}: unbalanced quote in CSS content declaration")
    if failures:
        fail("CSS string sanity guards failed:\n" + "\n".join(failures))
    ok("CSS string sanity guards clean")


def generated_text_sanity_guards() -> None:
    failures: list[str] = []
    paths = sorted((ROOT / "dev").glob("*.css")) + [ROOT / "dev" / "README.md", ROOT / "theme.css"]
    broken_tokens = ("\ufffd", "沅", "蹂", "寃")
    for path in paths:
        rel = path.relative_to(ROOT).as_posix()
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if any(token in line for token in broken_tokens):
                failures.append(f"{rel}:{lineno}: mojibake marker found")
            if "??" in line and ("/*" in line or line.strip().startswith("*") or line.strip().startswith("-")):
                failures.append(f"{rel}:{lineno}: suspicious replacement marker in comment")
    if failures:
        fail("Generated text sanity guards failed:\n" + "\n".join(failures))
    ok("generated text sanity guards clean")


def liquid_glass_documentation_guards() -> None:
    token_map = read_text("docs/liquid-glass-token-map.md")
    important_audit = read_text("docs/css-important-audit.md")
    failures: list[str] = []

    token_requirements = [
        "liquid-glass-hover-study-sample.html",
        "fixtures/liquid-glass-core-state-matrix.html",
        "--ogd-lg-surface-bg",
        "--ogd-lg-shadow-focus",
        "--ogd-table-surface",
        "Frost Aqua Focus Sweep",
    ]
    for token in token_requirements:
        if token not in token_map:
            failures.append(f"docs/liquid-glass-token-map.md missing {token}")

    audit_requirements = [
        "dev/09b-editing-menu-tooltip-glass.css",
        "dev/06-feature-presets.css",
        "dev/07-plugin-workspace.css",
        "dev/10d-liquid-glass-core.css",
    ]
    for token in audit_requirements:
        if token not in important_audit:
            failures.append(f"docs/css-important-audit.md missing {token}")

    if failures:
        fail("liquid glass documentation guards failed:\n" + "\n".join(failures))
    ok("liquid glass documentation guards clean")


def liquid_glass_focus_guards() -> None:
    theme = read_text("theme.css")
    missing = [token for token in LIQUID_GLASS_FOCUS_GUARDS if token not in theme]
    if missing:
        fail(f"theme.css missing liquid glass focus guards: {', '.join(missing)}")
    ok("liquid glass focus sweep guards clean")


def css_complexity_inventory() -> None:
    theme = read_text("theme.css")
    theme_lines = theme.count("\n") + 1
    important_count = theme.count("!important")
    module_summaries: list[tuple[int, str, int]] = []
    failures: list[str] = []
    for path in sorted((ROOT / "dev").glob("*.css")):
        content = path.read_text(encoding="utf-8")
        line_count = content.count("\n") + 1
        module_important = content.count("!important")
        module_summaries.append((line_count, path.name, module_important))
        if line_count > MAX_DEV_MODULE_LINES:
            failures.append(f"{path.name}: {line_count} lines exceeds budget {MAX_DEV_MODULE_LINES}")
        if module_important > MAX_DEV_MODULE_IMPORTANT:
            failures.append(f"{path.name}: {module_important} !important exceeds budget {MAX_DEV_MODULE_IMPORTANT}")
    if failures:
        fail("CSS complexity budget exceeded:\n" + "\n".join(failures))
    largest = ", ".join(
        f"{name}={lines} lines/{important} !important"
        for lines, name, important in sorted(module_summaries, reverse=True)[:3]
    )
    ok(f"CSS complexity inventory: theme={theme_lines} lines, !important={important_count}, largest modules=({largest})")


def contrast_audit() -> None:
    script = ROOT / "scripts" / "contrast_audit.py"
    spec = importlib.util.spec_from_file_location("contrast_audit", script)
    if spec is None or spec.loader is None:
        fail("unable to load scripts/contrast_audit.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    failures = []
    for pair in module.PAIRS:
        ratio = module.contrast_ratio(pair.foreground, pair.background)
        if ratio < pair.minimum:
            failures.append(f"{pair.name} ({ratio:.2f}:1)")
    if failures:
        fail(f"contrast audit failed: {', '.join(failures)}")
    ok(f"contrast audit passed ({len(module.PAIRS)} pairs)")


def release_zip_if_present(version: str) -> None:
    zip_path = ROOT / "dist" / f"Owen-Graphite-{version}.zip"
    if not zip_path.exists():
        ok("release ZIP content check skipped")
        return
    expected = [f"Owen Graphite/{asset}" for asset in RELEASE_ASSETS]
    with zipfile.ZipFile(zip_path) as archive:
        names = archive.namelist()
        zipped_manifest = json.loads(archive.read("Owen Graphite/manifest.json").decode("utf-8"))
    missing = [name for name in expected if name not in names]
    extra = [name for name in names if name not in expected]
    if missing:
        fail(f"release ZIP missing assets: {', '.join(missing)}")
    if extra:
        fail(f"release ZIP has unexpected assets: {', '.join(extra)}")
    if zipped_manifest.get("version") != version:
        fail(f"release ZIP manifest version {zipped_manifest.get('version')} does not match {version}")
    ok("release ZIP contents match expected manual install package")


def live_preview_guards() -> None:
    css_sources = {
        "theme.css": read_text("theme.css"),
    }
    for path, content in css_sources.items():
        for pattern, description in FORBIDDEN_LIVE_PREVIEW_RULES.items():
            if pattern.search(content):
                fail(f"{path}: {description}")
        live_preview_hit_routing_audit(content, path)
    ok("Live Preview editability guards clean")


def reading_view_layout_guards() -> None:
    theme = read_text("theme.css")
    for pattern, description in FORBIDDEN_READING_VIEW_RULES.items():
        if pattern.search(theme):
            fail(f"theme.css: {description}")
    missing = [guard for guard in REQUIRED_READING_VIEW_GUARDS if guard not in theme]
    if missing:
        fail(f"theme.css missing Reading View layout guards: {', '.join(missing)}")
    ok("Reading View layout guards clean")


def live_preview_width_guards() -> None:
    theme = read_text("theme.css")
    missing = [guard for guard in REQUIRED_LIVE_PREVIEW_WIDTH_GUARDS if guard not in theme]
    if missing:
        fail(f"theme.css missing Live Preview width guards: {', '.join(missing)}")
    ok("Live Preview width guards clean")


def readable_column_guards() -> None:
    theme = read_text("theme.css")
    missing = [guard for guard in REQUIRED_READABLE_COLUMN_GUARDS if guard not in theme]
    if missing:
        fail(f"theme.css missing readable column guards: {', '.join(missing)}")
    ok("readable column alignment guards clean")


def table_inflation_guards() -> None:
    theme = read_text("theme.css")
    missing = [guard for guard in REQUIRED_TABLE_INFLATION_GUARDS if guard not in theme]
    if missing:
        fail(f"theme.css missing table inflation guards: {', '.join(missing)}")
    missing_header_guards = [
        description
        for pattern, description in TABLE_INFLATION_HEADER_GUARD_PATTERNS.items()
        if not pattern.search(theme)
    ]
    if missing_header_guards:
        fail("theme.css missing table header inflation guards: " + ", ".join(missing_header_guards))
    ok("table inflation guards clean")


def editable_table_sample_guards() -> None:
    sample = read_text("dev/test-samples/owen-editor-feature-sample.md")
    failures = []
    for section in EDITABLE_TABLE_SAMPLE_SECTIONS:
        match = re.search(rf"^## {re.escape(section)}\n(?P<body>.*?)(?=^## |\Z)", sample, re.M | re.S)
        if not match:
            failures.append(f"missing section: {section}")
            continue
        body = match.group("body")
        if "<table" in body.lower():
            failures.append(f"{section} uses HTML table instead of editable Markdown table")
        if not re.search(r"^\|.+\|\s*$", body, re.M) or not re.search(r"^\|\s*:?-{3,}:?", body, re.M):
            failures.append(f"{section} missing Markdown table header/alignment rows")
    if failures:
        fail("editable table sample guards failed:\n" + "\n".join(failures))
    ok("editable table sample guards clean")


def liquid_glass_sample_guards() -> None:
    sample = read_text("dev/test-samples/liquid-glass-table-focus-sample.md")
    failures: list[str] = []
    for section in LIQUID_GLASS_SMOKE_SECTIONS:
        if not re.search(rf"^## {re.escape(section)}$", sample, re.M):
            failures.append(f"missing section: {section}")
    if "ogd-report-mode" not in sample:
        failures.append("missing report-mode toggle guidance")
    if "document-search-container" not in sample:
        failures.append("missing document search focus target")
    if len(re.findall(r"^\|.+\|\s*$", sample, re.M)) < 8:
        failures.append("missing Markdown table smoke rows")
    if "좌측 세로 line/rail" not in sample:
        failures.append("missing no-left-rail regression note")
    if failures:
        fail("liquid glass sample guards failed:\n" + "\n".join(failures))
    ok("liquid glass table/focus sample guards clean")


def qa_checklist_guards() -> None:
    checklist = read_text("docs/qa-checklist.md")
    required_tokens = [
        "## Side Pane Smoke Matrix",
        "Backlinks",
        "Outgoing links",
        "Outline",
        "Bookmarks",
        "Tags",
        "Search",
        "docs/fixtures/right-sidebar-pane-glass.html",
        "git add -f",
    ]
    missing = [token for token in required_tokens if token not in checklist]
    if missing:
        fail("QA checklist missing side pane smoke guards: " + ", ".join(missing))
    ok("QA checklist side pane smoke guards clean")


def diff_check() -> None:
    result = subprocess.run(["git", "diff", "--check"], cwd=ROOT, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        fail(f"git diff --check failed:\n{result.stdout}{result.stderr}")
    ok("git diff --check clean")


def target_sync_check(target: Path | None, ci: bool) -> None:
    if ci:
        ok("target vault sync check skipped")
        return
    candidates = [target] if target else DEFAULT_TARGETS
    existing = next((candidate for candidate in candidates if candidate and candidate.exists()), None)
    if not existing:
        ok("target vault sync check skipped")
        return
    for rel in RELEASE_ASSETS:
        source = (ROOT / rel).read_bytes()
        target_data = (existing / rel).read_bytes()
        if source != target_data:
            fail(f"target vault asset differs: {existing / rel}")
    ok("target vault release assets are synchronized")


def release_checklist(version: str, ci: bool) -> None:
    zip_path = ROOT / "dist" / f"Owen-Graphite-{version}.zip"
    print("\nRelease checklist")
    print(f"- version: {version}")
    print("- required files: present")
    print(f"- Style Settings: {EXPECTED_STYLE_SETTINGS_OPTIONS} functional options")
    print("- screenshots: dimensions verified")
    print(f"- release ZIP: {'present' if zip_path.exists() else 'not built yet'}")
    print("- target vault sync: skipped in CI" if ci else "- target vault sync: checked when target exists")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ci", action="store_true", help="Skip local vault synchronization checks.")
    parser.add_argument("--target", type=Path, help="Optional Obsidian theme folder to compare theme.css and manifest.json against.")
    args = parser.parse_args()

    required_files()
    version = manifest_and_versions()
    no_stale_legacy_markers()
    style_settings_count()
    style_settings_binding_guards()
    png_dimensions()
    readme_svg_asset_guards()
    visual_regression_script_guards()
    release_workflow_assets()
    python_only_scripts()
    dev_temp_policy()
    git_tracking_policy()
    dev_bundle_current()
    dev_css_module_set_clean()
    css_regression_guards()
    core_chrome_structure_guards()
    css_has_guards()
    css_print_ownership_guards()
    css_risk_inventory()
    css_variable_usage_guards()
    css_string_sanity_guards()
    generated_text_sanity_guards()
    liquid_glass_documentation_guards()
    liquid_glass_focus_guards()
    css_complexity_inventory()
    contrast_audit()
    release_zip_if_present(version)
    live_preview_guards()
    reading_view_layout_guards()
    live_preview_width_guards()
    readable_column_guards()
    table_inflation_guards()
    editable_table_sample_guards()
    liquid_glass_sample_guards()
    qa_checklist_guards()
    diff_check()
    target_sync_check(args.target, args.ci)
    release_checklist(version, args.ci)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())