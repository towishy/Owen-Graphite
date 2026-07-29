#!/usr/bin/env python3
"""Build a source usage and ownership map for Owen Graphite CSS."""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MAP = ROOT / "dev" / "WIKI" / "MAP"
WIKI = ROOT / "dev" / "WIKI"
OWNER_REGISTRY = MAP / "owner-registry.json"
EFFECTIVE_SOURCE_MAP = MAP / "effective-source-map.json"
OUT_JSON = WIKI / "MAP" / "source-usage-map.json"
OUT_MD = WIKI / "MAP" / "source-usage-map.md"
OUT_RUNTIME_MD = WIKI / "runtime-debug-protocol.md"
SNIPPET_DIR = WIKI / "runtime-debug-snippets"
TABLE_CELL_SNIPPET = SNIPPET_DIR / "table-cell-dump.js"
MATCHED_RULES_SNIPPET = SNIPPET_DIR / "matched-rules-dump.js"

TABLE_TERMS = ("table", "td", "th", "tr", "tbody", "thead", "caption", "cm-table-widget", "table.cm-table", "HyperMD-table-row")
CM6_TERMS = ("markdown-source-view.mod-cm6", "cm-line", "HyperMD-", "cm-content", "cm-editor", "cm-scroller")
PRINT_TERMS = ("@media print", "@page", "ogd-pdf", "print")

CHANGE_TYPE_COMMANDS = {
    "Table": [
        "Open `src/surfaces/20-reading-tables-code.css` first for rendered tables.",
        "Open `src/base/13-live-preview.css` or `src/surfaces/24-html-table-live-preview-glass.css` for Live Preview HTML tables.",
        "Run `audit_direct_owner_guard.py`, `audit_lp_pdf_selector_ownership.py`, and `audit_v3_hit_routing.py`.",
    ],
    "Live Preview": [
        "Open `src/base/13-live-preview.css` first.",
        "Read `dev/WIKI/MAP/cm6-hit-routing-contract.md` before changing geometry.",
        "Run `audit_v3_hit_routing.py` and `audit_core_principles.py`.",
    ],
    "PDF": [
        "Open `src/features/43-print-base.css`, `src/features/41-feature-presets.css`, or `src/features/42-report-print-polish.css` according to the surface.",
        "Read `dev/WIKI/MAP/pdf-header-footer-contract.md` for marginalia.",
        "Run `audit_pdf_header_footer.py` and `release_check.py --skip-bundle`.",
    ],
    "Chrome/UI": [
        "Open `src/chrome/*` owner modules according to `Quick Routing`.",
        "Read `dev/WIKI/MAP/top-chrome-icon-background-contract.md` for top chrome icons.",
        "Run `audit_core_principles.py` and screenshot/runtime checks for interactive states.",
    ],
    "Docs/README": [
        "Update docs and sample assets in the documented locations.",
        "Run `audit_docs_assets.py` and `audit_readme_svg_layout.py`.",
    ],
    "Release": [
        "Run `bundle_v3.py`, `release_check.py --skip-bundle`, and `build_release.py`.",
        "Run `audit_release_zip.py` before publishing.",
    ],
}


def load_build_src_map_module():
    script = ROOT / "dev" / "scripts" / "build_src_map.py"
    spec = importlib.util.spec_from_file_location("build_src_map", script)
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to load build_src_map.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def split_selector_list(selector: str) -> list[str]:
    parts: list[str] = []
    buffer: list[str] = []
    depth = 0
    for char in selector:
        if char == "(":
            depth += 1
        elif char == ")" and depth:
            depth -= 1
        if char == "," and depth == 0:
            part = "".join(buffer).strip()
            if part:
                parts.append(part)
            buffer = []
        else:
            buffer.append(char)
    part = "".join(buffer).strip()
    if part:
        parts.append(part)
    return parts


def strip_not_pseudos(selector: str) -> str:
    output: list[str] = []
    index = 0
    while index < len(selector):
        if selector[index : index + 5].lower() == ":not(":
            depth = 0
            while index < len(selector):
                if selector[index] == "(":
                    depth += 1
                elif selector[index] == ")":
                    depth -= 1
                    if depth == 0:
                        index += 1
                        break
                index += 1
        else:
            output.append(selector[index])
            index += 1
    return "".join(output)


def strip_comments_keep_lines(text: str) -> str:
    import re

    return re.sub(r"/\*.*?\*/", lambda match: "\n" * match.group(0).count("\n"), text, flags=re.S)


def owner_maps() -> tuple[dict[str, list[str]], dict[str, dict[str, object]], dict[str, dict[str, object]]]:
    registry = json.loads(OWNER_REGISTRY.read_text(encoding="utf-8"))
    by_module: dict[str, list[str]] = defaultdict(list)
    by_surface: dict[str, dict[str, object]] = {}
    for surface in registry["surfaces"]:
        by_surface[surface["id"]] = surface
        for module in surface["ownerModules"]:
            if module.startswith("src/"):
                by_module[module].append(surface["id"])
        for module in surface.get("allowedLateModules", []):
            if module.startswith("src/"):
                by_module[module].append(f"{surface['id']} (allowed-late)")
    support_by_module = {str(item["module"]): item for item in registry.get("supportModules", [])}
    return dict(by_module), by_surface, support_by_module


def bundle_ranges() -> dict[str, dict[str, int]]:
    data = json.loads(EFFECTIVE_SOURCE_MAP.read_text(encoding="utf-8"))
    return {
        item["module"]: {
            "bundleStartLine": item["bundleStartLine"],
            "bundleEndLine": item["bundleEndLine"],
            "sourceStartLine": item["sourceStartLine"],
            "sourceEndLine": item["sourceEndLine"],
        }
        for item in data["ranges"]
    }


def classify(selector: str, body: str, at_context: str) -> set[str]:
    selector_parts = split_selector_list(selector)
    selector_text = " ".join(selector_parts)
    text = f"{selector_text} {body} {at_context}"
    low = text.lower()
    labels: set[str] = set()
    selector_low = selector_text.lower()
    if any(term.lower() in selector_low for term in TABLE_TERMS):
        labels.add("table")
    if ".markdown-source-view.mod-cm6" in low and "table" in low and ":not(.cm-table-widget)" in low and ":not(.cm-table)" in low:
        labels.add("lp-html-table")
    if "cm-table-widget" in low or "table.cm-table" in low:
        labels.add("lp-markdown-table-widget-reference")
    if "markdown-rendered" in low or "markdown-preview-view" in low or "markdown-reading-view" in low:
        labels.add("reading-rendered")
    if any(term.lower() in low for term in CM6_TERMS):
        labels.add("cm6")
    if any(term.lower() in low for term in PRINT_TERMS):
        labels.add("print-pdf")
    if "pre" in low or "code" in low or "language-" in low:
        labels.add("code")
    if "callout" in low or "blockquote" in low or "task-list" in low:
        labels.add("callout-list")
    if any(term in low for term in ("workspace-", "nav-", "ribbon", "status-bar", "side-dock")):
        labels.add("workspace-chrome")
    if any(term in low for term in ("menu", "suggestion", "popover", "tooltip", "modal", "prompt", "search")):
        labels.add("overlay-search")
    return labels


def direct_core_table_violation(selector_part: str) -> bool:
    no_not = strip_not_pseudos(selector_part).lower()
    return ".cm-table-widget" in no_not or "table.cm-table" in no_not


def classify_support_module(module: dict[str, object], support_by_module: dict[str, dict[str, object]]) -> str:
    path = str(module["module"])
    support = support_by_module.get(path)
    if support:
        return f"registered support: {support.get('role', 'support module')}"
    labels = set(module["labels"])
    if path.startswith("src/tokens/") or path.startswith("src/themes/"):
        return "intentional support: theme/tokens layer"
    if path.startswith("src/plugins/"):
        return "external/plugin specific support"
    if path in {"src/base/10-base-workspace.css", "src/surfaces/22-reading-embeds-workspace.css"}:
        return "intentional support: base/embed workspace primitives"
    if path == "src/chrome/33-settings-controls.css":
        return "possible owner registry gap: settings controls"
    if "workspace-chrome" in labels or "overlay-search" in labels:
        return "possible owner registry gap: chrome/overlay support"
    return "needs review"


def table_selector_index() -> list[dict[str, str]]:
        return [
                {
                        "pattern": ".markdown-rendered table / .markdown-preview-view table",
                        "owner": "src/surfaces/20-reading-tables-code.css",
                        "purpose": "Reading/rendered table primitives and ordinary table surfaces",
                        "status": "allowed",
                },
                {
                        "pattern": ".markdown-source-view.mod-cm6 ... table:not(.cm-table):not(.cm-table-widget)",
                        "owner": "src/base/13-live-preview.css and src/surfaces/24-html-table-live-preview-glass.css",
                        "purpose": "Live Preview HTML table embeds only",
                        "status": "allowed with both guards",
                },
                {
                        "pattern": ".cm-table-widget / table.cm-table",
                        "owner": "Obsidian core",
                        "purpose": "Live Preview markdown table widget geometry",
                        "status": "forbidden for theme geometry",
                },
                {
                    "pattern": "@media print table",
                    "owner": "src/features/42-report-print-polish.css",
                    "purpose": "PDF table output and print-safe adjustments",
                    "status": "allowed in print scope",
                },
                {
                        "pattern": "table caption / .table-caption / .table-source",
                        "owner": "src/surfaces/23-liquid-glass-core.css and src/features/42-report-print-polish.css",
                        "purpose": "Rendered captions and print notes",
                        "status": "allowed for rendered/print surfaces",
                },
        ]


def render_table_cell_snippet() -> str:
        return """(() => {
    const cell = [...document.querySelectorAll('td, th')]
        .find(el => el.getBoundingClientRect().height > 90) ||
        document.activeElement?.closest?.('td, th');
    if (!cell) { copy('NO_CELL_FOUND'); return 'NO_CELL_FOUND'; }
    const nodes = [];
    for (let el = cell; el && nodes.length < 12; el = el.parentElement) nodes.push(el);
    const out = nodes.map(el => {
        const cs = getComputedStyle(el);
        const r = el.getBoundingClientRect();
        return {
            tag: el.tagName,
            cls: String(el.className || ''),
            text: el.textContent?.trim().slice(0, 80),
            style: el.getAttribute('style'),
            rect: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
            computed: {
                display: cs.display,
                position: cs.position,
                width: cs.width,
                height: cs.height,
                minHeight: cs.minHeight,
                maxHeight: cs.maxHeight,
                padding: cs.padding,
                margin: cs.margin,
                lineHeight: cs.lineHeight,
                verticalAlign: cs.verticalAlign,
                overflow: cs.overflow,
                transform: cs.transform
            }
        };
    });
    copy(JSON.stringify(out, null, 2));
    return out;
})();
"""


def render_matched_rules_snippet() -> str:
        return """(() => {
    const target = [...document.querySelectorAll('td, th')]
        .find(el => el.getBoundingClientRect().height > 90) ||
        document.activeElement?.closest?.('td, th') ||
        document.activeElement;
    if (!target) { copy('NO_TARGET_FOUND'); return 'NO_TARGET_FOUND'; }
    const nodes = [target, ...target.querySelectorAll?.('*') || []].slice(0, 20);
    const out = nodes.map(el => {
        const matched = [];
        for (const sheet of [...document.styleSheets]) {
            let rules;
            try { rules = sheet.cssRules; } catch { continue; }
            for (const rule of [...rules]) {
                if (!rule.selectorText) continue;
                try {
                    if (el.matches(rule.selectorText) && /height|min-height|max-height|vertical-align|padding|line-height|display|position|transform|width|max-width/.test(rule.style.cssText)) {
                        matched.push({ selector: rule.selectorText, css: rule.style.cssText });
                    }
                } catch {}
            }
        }
        const cs = getComputedStyle(el);
        return {
            tag: el.tagName,
            cls: String(el.className || ''),
            style: el.getAttribute('style'),
            computed: { height: cs.height, minHeight: cs.minHeight, maxHeight: cs.maxHeight, padding: cs.padding, lineHeight: cs.lineHeight, display: cs.display, position: cs.position, verticalAlign: cs.verticalAlign, width: cs.width, maxWidth: cs.maxWidth },
            matched: matched.slice(-50)
        };
    });
    copy(JSON.stringify(out, null, 2));
    return out;
})();
"""


def render_runtime_debug_protocol() -> str:
        return """# Runtime Debug Protocol

Use this when static audits pass but a selected, hovered, focused, or active runtime state still fails.

## Required Steps

1. Reproduce the issue in Obsidian with the exact runtime state active.
2. If the CDP endpoint is closed while Obsidian is already running, close the existing Obsidian processes and reopen Obsidian with `--remote-debugging-port=9222` before capturing evidence.
3. Run `runtime-debug-snippets/table-cell-dump.js` when the issue is table/cell geometry.
4. Run `runtime-debug-snippets/matched-rules-dump.js` to capture theme/core matched rules.
5. Inspect inline `style` first. Inline geometry means the issue may not be solvable by ordinary owner CSS.
6. If a theme rule is responsible, map the bundle line through `effective-source-map.json` and edit the source owner.
7. If an Obsidian core rule is responsible, do not override it unless an owner contract explicitly permits it.
8. Re-run the same runtime state after editing; static audits alone are insufficient.

## Outputs To Preserve

- DOM chain: tag, class, inline style, text preview.
- Rect chain: x/y/width/height for the target and parents.
- Computed geometry: display, position, width, height, min/max height, padding, line-height, vertical-align, overflow, transform.
- Matched rules: selector and CSS text for geometry-affecting declarations.

## Snippets

- `dev/WIKI/runtime-debug-snippets/table-cell-dump.js`
- `dev/WIKI/runtime-debug-snippets/matched-rules-dump.js`
"""


def build() -> tuple[dict[str, object], str]:
    build_src_map = load_build_src_map_module()
    imports = build_src_map.import_order()
    owners_by_module, surfaces, support_by_module = owner_maps()
    ranges = bundle_ranges()

    modules: list[dict[str, object]] = []
    table_rules: list[dict[str, object]] = []
    hard_violations: list[dict[str, object]] = []
    totals = Counter()

    for index, item in enumerate(imports):
        module = item["module"]
        path = ROOT / module
        css = path.read_text(encoding="utf-8")
        rules = build_src_map.tokenize_blocks(strip_comments_keep_lines(css))
        label_counts = Counter()
        selector_parts = 0
        for rule in rules:
            labels = classify(rule.selector, rule.body, rule.at_context)
            for label in labels:
                label_counts[label] += 1
            parts = split_selector_list(rule.selector)
            selector_parts += len(parts)
            for part in parts:
                if direct_core_table_violation(part):
                    hard_violations.append({"module": module, "line": rule.line, "selector": part})
            if "table" in labels:
                table_rules.append(
                    {
                        "module": module,
                        "line": rule.line,
                        "context": rule.at_context,
                        "labels": sorted(labels),
                        "selector": rule.selector,
                    }
                )

        range_info = ranges.get(module, {})
        source_lines = css.count("\n") + 1
        record = {
            "index": index + 1,
            "module": module,
            "legacyId": item.get("legacy_id", ""),
            "sourceLines": source_lines,
            "bundleStartLine": range_info.get("bundleStartLine"),
            "bundleEndLine": range_info.get("bundleEndLine"),
            "rules": len(rules),
            "selectorParts": selector_parts,
            "labels": dict(sorted(label_counts.items())),
            "ownerSurfaces": owners_by_module.get(module, []),
            "supportRole": str(support_by_module.get(module, {}).get("role", "")),
            "previousModule": imports[index - 1]["module"] if index > 0 else None,
            "nextModule": imports[index + 1]["module"] if index + 1 < len(imports) else None,
        }
        modules.append(record)
        totals["sourceLines"] += source_lines
        totals["rules"] += len(rules)
        totals["selectorParts"] += selector_parts
        for label, count in label_counts.items():
            totals[f"label:{label}"] += count

    data = {
        "schema": "owen-graphite/source-usage-map/1",
        "moduleCount": len(modules),
        "sourceLines": totals["sourceLines"],
        "rules": totals["rules"],
        "selectorParts": totals["selectorParts"],
        "labelTotals": {key.removeprefix("label:"): value for key, value in sorted(totals.items()) if key.startswith("label:")},
        "hardViolations": hard_violations,
        "modules": modules,
        "tableRules": table_rules,
        "tableSelectorIndex": table_selector_index(),
        "ownerRegistryGaps": [
            {
                "module": module["module"],
                "classification": classify_support_module(module, support_by_module),
                "labels": module["labels"],
            }
            for module in modules
            if not module["ownerSurfaces"] and module["module"] not in support_by_module
        ],
        "supportModules": [
            {
                "module": module["module"],
                "role": module["supportRole"],
                "labels": module["labels"],
            }
            for module in modules
            if module["module"] in support_by_module
        ],
        "riskContractGaps": [
            {
                "surface": surface_id,
                "description": surface.get("description", ""),
                "ownerModules": surface.get("ownerModules", []),
            }
            for surface_id, surface in surfaces.items()
            if not surface.get("riskContracts")
        ],
        "surfaces": surfaces,
    }
    return data, render_markdown(data)


def render_markdown(data: dict[str, object]) -> str:
    modules = data["modules"]
    label_totals = data["labelTotals"]
    unregistered = [module for module in modules if not module["ownerSurfaces"] and not module.get("supportRole")]
    lines: list[str] = []
    lines.append("# Owen Graphite Source Usage Map")
    lines.append("")
    lines.append("Generated from `src/entry.css`, `dev/WIKI/MAP/owner-registry.json`, and `dev/WIKI/MAP/effective-source-map.json`.")
    lines.append("")
    lines.append("Canonical WIKI location: `dev/WIKI/MAP/source-usage-map.md`. Machine provenance remains in `dev/WIKI/MAP`.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Source modules: {data['moduleCount']}")
    lines.append(f"- Source CSS lines: {data['sourceLines']}")
    lines.append(f"- Parsed CSS rules: {data['rules']}")
    lines.append(f"- Selector parts: {data['selectorParts']}")
    lines.append(f"- Hard core-owner violations: {len(data['hardViolations'])}")
    lines.append("")
    lines.append("## Surface Totals")
    lines.append("")
    for label, count in sorted(label_totals.items()):
        lines.append(f"- `{label}`: {count} rules")
    lines.append("")
    lines.append("## Quick Routing")
    lines.append("")
    lines.append("Use this table before editing. Start at the owner module, then inspect allowed-late modules only when the owner registry explicitly allows them.")
    lines.append("")
    lines.append("| Work Area | Start Here | Allowed Follow-Up | Must Check |")
    lines.append("| --- | --- | --- | --- |")
    lines.append("| Reading typography, links, headings | `src/base/12-reading-content.css` | theme overrides in `src/themes/50-dark.css` when dark-only | `reading-typography` owner surface |")
    lines.append("| Reading/rendered tables and code | `src/surfaces/20-reading-tables-code.css` | `src/features/42-report-print-polish.css` for print/report only | `Table Selector Rules` below |")
    lines.append("| Live Preview CM6 line geometry | `src/base/13-live-preview.css` | none | `dev/WIKI/MAP/cm6-hit-routing-contract.md` |")
    lines.append("| Live Preview markdown table widget | Obsidian core, no theme geometry owner | none | Do not style `.cm-table-widget` or `table.cm-table` |")
    lines.append("| Live Preview HTML table embed | `src/base/13-live-preview.css`, `src/surfaces/24-html-table-live-preview-glass.css` | `src/features/42-report-print-polish.css` utilities only | Must include `:not(.cm-table-widget)` and `:not(.cm-table)` |")
    lines.append("| PDF header/footer marginalia | `src/features/41-feature-presets.css`, `src/tokens/00-light-tokens.css`, `src/tokens/01-dark-tokens.css` | none | `dev/WIKI/MAP/pdf-header-footer-contract.md` |")
    lines.append("| Workspace chrome | `src/chrome/30-workspace.css`, `src/chrome/31-navigation-tasks-search.css`, `src/chrome/34-nav-ribbon-glass.css`, `src/chrome/37-tabs-file-explorer-search.css` | none | `dev/WIKI/MAP/top-chrome-icon-background-contract.md` |")
    lines.append("| Menus, popovers, search, modals | `src/chrome/32-overlay-popover-dataview.css`, `src/chrome/35-editing-menu-tooltip-glass.css`, `src/chrome/36-floating-ui-glass-system.css` | none | overlay/search selectors in this map |")
    lines.append("")
    lines.append("## Core Principle Workflow")
    lines.append("")
    lines.append("Before editing CSS:")
    lines.append("")
    lines.append("1. Identify the target surface in `Quick Routing`.")
    lines.append("2. Open the owner module first; do not start from a later visual module.")
    lines.append("3. Read linked risk contracts when the target is CM6, table, PDF, or top chrome.")
    lines.append("4. Remove or merge conflicting follow-up rules instead of adding a new override.")
    lines.append("5. Run `build_source_usage_map.py --check` and `audit_core_principles.py` before commit.")
    lines.append("")
    lines.append("Forbidden workflow:")
    lines.append("")
    lines.append("- Adding a new late fix because the owner was hard to locate.")
    lines.append("- Styling Obsidian-owned markdown table widget geometry.")
    lines.append("- Reintroducing `src/polish/*` or `!important`.")
    lines.append("- Treating allowed-late modules as broad ownership permission.")
    lines.append("")
    lines.append("## Known Failure Modes")
    lines.append("")
    lines.append("These are real failure patterns that should stop work until the owner and runtime evidence are clear.")
    lines.append("")
    lines.append("| Failure Mode | Symptom | Root Risk | Correct Response |")
    lines.append("| --- | --- | --- | --- |")
    lines.append("| Broad CM6 editor selector | Nested editors inside widgets inherit page-level geometry | `.cm-content`, `.cm-line`, `.cm-editor`, or `.cm-scroller` selectors can hit embedded editors | Narrow the owner selector or inspect runtime DOM before editing |")
    lines.append("| Markdown table widget styled as theme table | Selecting a markdown table cell changes row geometry or hit routing | `.cm-table-widget` / `table.cm-table` belongs to Obsidian core | Do not style widget geometry; target rendered tables or HTML embeds only |")
    lines.append("| Rendered table and LP widget grouped together | A table fix works in Reading View but breaks Live Preview editing | Selector group mixes `.markdown-rendered table` with source-mode widgets | Split by surface and owner before changing properties |")
    lines.append("| Late visual module used as repair layer | A fix only works because it wins late in cascade | Owner module remains wrong and future edits become unpredictable | Move the rule to the owner and remove the late correction |")
    lines.append("| Sync/debug confusion | CSS appears unchanged after a fix | Vault path, theme cache, or runtime DOM not verified | Compare repo/vault CSS and capture computed styles before more edits |")
    lines.append("| Inline/runtime height | CSS changes do not affect selected row height | Obsidian runtime may set inline style or non-theme DOM state | Use Runtime Debug Protocol; do not add stronger CSS blindly |")
    lines.append("")
    lines.append("## Runtime Debug Protocol")
    lines.append("")
    lines.append("See `dev/WIKI/runtime-debug-protocol.md` and the snippets in `dev/WIKI/runtime-debug-snippets/`.")
    lines.append("")
    lines.append("## If You Touch X")
    lines.append("")
    lines.append("| Selector Or Feature | Owner First | Also Inspect | Never Do |")
    lines.append("| --- | --- | --- | --- |")
    lines.append("| `.markdown-rendered table`, `.markdown-preview-view table` | `src/surfaces/20-reading-tables-code.css` | `src/features/42-report-print-polish.css`, `src/surfaces/23-liquid-glass-core.css` | Mix with `.cm-table-widget` |")
    lines.append("| `.cm-table-widget`, `table.cm-table` | Obsidian core | runtime DOM, `cm6-hit-routing-contract.md` | Add theme geometry or visual table styling |")
    lines.append("| LP HTML `<table>` embed | `src/base/13-live-preview.css`, `src/surfaces/24-html-table-live-preview-glass.css` | `src/features/42-report-print-polish.css` utilities | Omit `:not(.cm-table-widget):not(.cm-table)` |")
    lines.append("| `.cm-line`, `.HyperMD-*` | `src/base/13-live-preview.css` | `cm6-hit-routing-contract.md` | Add vertical margin/padding to hit-routed lines |")
    lines.append("| Callouts and blockquotes | `src/surfaces/21-reading-callouts-lists.css` | `src/base/13-live-preview.css`, `src/surfaces/23-liquid-glass-core.css` | Add left rails or late visual repair without owner edit |")
    lines.append("| Code blocks | `src/surfaces/20-reading-tables-code.css` | `src/base/13-live-preview.css`, `src/features/42-report-print-polish.css` | Split LP/Reading/PDF parity without checking map |")
    lines.append("| `ogd-pdf-header-*`, `ogd-pdf-footer-*` | `src/features/41-feature-presets.css` | token files, `pdf-header-footer-contract.md` | Put header/footer owner rules in `42-report-print-polish` |")
    lines.append("| Top tabs/ribbon/sidebar icons | `src/chrome/34-nav-ribbon-glass.css`, `src/chrome/37-tabs-file-explorer-search.css` | `top-chrome-icon-background-contract.md` | Add broad top-chrome selectors in overlay modules |")
    lines.append("| Menus, suggestions, modals, popovers | `src/chrome/32-overlay-popover-dataview.css`, `src/chrome/35-editing-menu-tooltip-glass.css`, `src/chrome/36-floating-ui-glass-system.css` | accessibility/motion module | Treat overlay state as workspace chrome owner |")
    lines.append("")
    lines.append("## Audit Coverage Matrix")
    lines.append("")
    lines.append("| Audit | Catches | Does Not Catch |")
    lines.append("| --- | --- | --- |")
    lines.append("| `build_source_usage_map.py --check` | Stale source map, missing generated overview | Runtime visual regressions |")
    lines.append("| `audit_core_principles.py` | Missing map, `src/polish`, `!important`, owner registry drift, core guard, selector ownership, hit routing | Inline Obsidian runtime styles |")
    lines.append("| `audit_direct_owner_guard.py` | `.cm-table-widget` / `table.cm-table` direct styling, generic LP table selectors, PDF header/footer owner drift | Semantic owner disputes outside encoded rules |")
    lines.append("| `audit_lp_pdf_selector_ownership.py` | LP/PDF selector ownership distribution | Whether a visual change looks correct |")
    lines.append("| `audit_v3_hit_routing.py` | Known CM6 hit-routing hazards | Rendered Reading View table aesthetics |")
    lines.append("| `audit_pdf_header_footer.py` | PDF marginalia owner contract | Non-marginalia PDF typography |")
    lines.append("| `v3_audit_duplicate_selectors.py` | In-file duplicate and cross-file selector groups | Whether duplicate intent is valid |")
    lines.append("| Runtime DevTools protocol | Actual selected/hover/focus DOM and computed style | Static owner drift unless matched rule is mapped back |")
    lines.append("")
    lines.append("## Audit Blind Spot Follow-Ups")
    lines.append("")
    lines.append("| Blind Spot | Required Follow-Up |")
    lines.append("| --- | --- |")
    lines.append("| Runtime inline style | Run `matched-rules-dump.js`; inspect `style` before adding CSS |")
    lines.append("| Obsidian internal DOM change | Capture DOM chain and compare with core contracts |")
    lines.append("| Vault plugin/snippet influence | Inspect `.obsidian/appearance.json`, enabled snippets, and plugin CSS/JS |")
    lines.append("| Visual-only layout shift | Create or update a fixture/screenshot audit before changing CSS |")
    lines.append("| OS/version-specific behavior | Record OS, Obsidian version, theme path, and runtime state |")
    lines.append("")
    lines.append("## Change Type Checklists")
    lines.append("")
    for change_type, steps in CHANGE_TYPE_COMMANDS.items():
        lines.append(f"### {change_type}")
        lines.append("")
        for step in steps:
            lines.append(f"- {step}")
        lines.append("")
    lines.append("")
    lines.append("## Cascade And Ownership Map")
    lines.append("")
    lines.append("| # | Module | Bundle Lines | Source Lines | Primary Owners | Major Labels | Cascade Relation |")
    lines.append("| ---: | --- | --- | ---: | --- | --- | --- |")
    for module in modules:
        bundle = f"{module['bundleStartLine']}-{module['bundleEndLine']}" if module.get("bundleStartLine") else "-"
        owners = ", ".join(module["ownerSurfaces"])
        if not owners:
            owners = f"support: {module['supportRole']}" if module.get("supportRole") else "unregistered/support"
        labels = ", ".join(f"{label}:{count}" for label, count in module["labels"].items()) or "metadata/tokens"
        relation = f"after `{module['previousModule']}`; before `{module['nextModule']}`"
        lines.append(f"| {module['index']} | `{module['module']}` | {bundle} | {module['sourceLines']} | {owners} | {labels} | {relation} |")
    lines.append("")
    lines.append("## Table Code Map")
    lines.append("")
    lines.append("Table-related rules are intentionally split by surface:")
    lines.append("")
    lines.append("- Reading/rendered tables: `src/surfaces/20-reading-tables-code.css`; report/print extensions in `src/features/42-report-print-polish.css`.")
    lines.append("- Live Preview markdown table widgets: Obsidian core-owned; theme CSS must not style `.cm-table-widget` / `table.cm-table` geometry.")
    lines.append("- Live Preview HTML table embeds: `src/base/13-live-preview.css`, `src/surfaces/24-html-table-live-preview-glass.css`, and utility hooks in `src/features/42-report-print-polish.css`.")
    lines.append("- Late visual table surface: `src/surfaces/23-liquid-glass-core.css` for rendered/non-core surfaces only.")
    lines.append("")
    lines.append("| Module | Table Rules | LP HTML Table Rules | Reading/Rendered Rules | Print/PDF Rules |")
    lines.append("| --- | ---: | ---: | ---: | ---: |")
    for module in modules:
        labels = module["labels"]
        table_count = labels.get("table", 0)
        if not table_count:
            continue
        lines.append(
            f"| `{module['module']}` | {table_count} | {labels.get('lp-html-table', 0)} | {labels.get('reading-rendered', 0)} | {labels.get('print-pdf', 0)} |"
        )
    lines.append("")
    lines.append("## Table Selector Rules")
    lines.append("")
    lines.append("Allowed:")
    lines.append("")
    lines.append("- Rendered tables in `src/surfaces/20-reading-tables-code.css`: `:is(.markdown-rendered, .markdown-preview-view, .markdown-reading-view) table ...`")
    lines.append("- Print/report table extensions in `src/features/42-report-print-polish.css` when the rule is print/report scoped.")
    lines.append("- Live Preview HTML table embeds with both guards: `.markdown-source-view.mod-cm6 ... table:not(.cm-table):not(.cm-table-widget)`.")
    lines.append("")
    lines.append("Forbidden:")
    lines.append("")
    lines.append("- `.markdown-source-view.mod-cm6 .cm-table-widget ...`")
    lines.append("- `.markdown-source-view.mod-cm6 table.cm-table ...`")
    lines.append("- `.HyperMD-table-row ... td/th/tr/table/.table-cell-wrapper` geometry rules.")
    lines.append("- Generic `.markdown-source-view.mod-cm6 ... table` without both `:not(.cm-table-widget)` and `:not(.cm-table)`.")
    lines.append("")
    lines.append("## Table Selector Reverse Index")
    lines.append("")
    lines.append("| Pattern | Owner | Purpose | Status |")
    lines.append("| --- | --- | --- | --- |")
    for item in data["tableSelectorIndex"]:
        lines.append(f"| `{item['pattern']}` | {item['owner']} | {item['purpose']} | {item['status']} |")
    lines.append("")
    lines.append("## Risk Contracts")
    lines.append("")
    lines.append("| Contract | Applies To | When To Read |")
    lines.append("| --- | --- | --- |")
    lines.append("| `dev/WIKI/MAP/cm6-hit-routing-contract.md` | CM6 line geometry, Live Preview widgets | Before editing `src/base/13-live-preview.css` or LP widgets |")
    lines.append("| `dev/WIKI/MAP/live-preview-pdf-css-map/parity-guidelines.md` | LP/PDF parity, tables, code, callouts | Before changing table/code/callout behavior across LP/Reading/PDF |")
    lines.append("| `dev/WIKI/MAP/pdf-header-footer-contract.md` | PDF marginalia | Before touching `ogd-pdf-header-*` or `ogd-pdf-footer-*` |")
    lines.append("| `dev/WIKI/MAP/top-chrome-icon-background-contract.md` | Top chrome/ribbon icon surfaces | Before touching titlebar, tabs, ribbon icons |")
    lines.append("")
    lines.append("## Risk Contract Coverage Gaps")
    lines.append("")
    if data["riskContractGaps"]:
        lines.append("Surfaces without explicit `riskContracts` in `owner-registry.json`:")
        lines.append("")
        for item in data["riskContractGaps"]:
            lines.append(f"- `{item['surface']}`: {item['description']} Owners: {', '.join(item['ownerModules'])}")
    else:
        lines.append("All owner surfaces have at least one risk contract.")
    lines.append("")
    lines.append("## Allowed-Late Does Not Mean New Owner")
    lines.append("")
    lines.append("`allowed-late` modules exist to preserve validated cascade order or print/report closure. They do not authorize new broad fixes. If a behavior has a clear owner, edit the owner first and use allowed-late modules only for their registered surface.")
    lines.append("")
    if data.get("supportModules"):
        lines.append("## Registered Support Modules")
        lines.append("")
        lines.append("These modules have explicit support roles in `owner-registry.json`. They are not primary owners and must not be used as repair layers.")
        lines.append("")
        for item in data["supportModules"]:
            lines.append(f"- `{item['module']}`: {item['role']}; labels {item['labels'] or {}}")
        lines.append("")
    if unregistered:
        lines.append("## Unregistered/Support Modules")
        lines.append("")
        lines.append("These modules are not primary owners in `owner-registry.json`. They may be valid support modules, but new ownership should not be inferred from their presence without updating the registry.")
        lines.append("")
        for item in data["ownerRegistryGaps"]:
            lines.append(f"- `{item['module']}`: {item['classification']}; labels {item['labels'] or {}}")
        lines.append("")
    lines.append("## Related Maps And Artifacts")
    lines.append("")
    lines.append("- `dev/WIKI/MAP/theme-css-risk-map.html`: visual HTML risk map for selector density and risk review.")
    lines.append("- `dev/WIKI/MAP/theme-css-risk-map.json`: machine-readable version of the risk map.")
    lines.append("- `dev/WIKI/MAP/selector-provenance.json`: source selector provenance data.")
    lines.append("- `dev/WIKI/MAP/unused-css-candidates.md`: unused/reserved selector analysis.")
    lines.append("- `dev/WIKI/MAP/effective-source-map.json`: bundle line to source module mapping.")
    lines.append("")
    lines.append("## Recent Incident Notes")
    lines.append("")
    lines.append("| Incident | Wrong Approach | Correct Process | Gate |")
    lines.append("| --- | --- | --- | --- |")
    lines.append("| Table row expands when a cell is selected | Repeated selector guesses and late geometry resets | Capture runtime DOM/computed style, map matched rule to owner, edit owner only | `audit_core_principles.py`, runtime debug protocol |")
    lines.append("| Table code hard to locate | Searching ad hoc selector fragments | Use `Table Selector Reverse Index`, `How To Find Table Code Quickly`, and source usage JSON | `build_source_usage_map.py --check` |")
    lines.append("")
    lines.append("## How To Find Table Code Quickly")
    lines.append("")
    lines.append("```powershell")
    lines.append(".\\.venv\\Scripts\\python.exe dev\\scripts\\build_source_usage_map.py --check")
    lines.append("Select-String -Path src\\**\\*.css -Pattern 'table|td|th|tr|caption|cm-table-widget|table\\.cm-table|HyperMD-table-row'")
    lines.append(".\\.venv\\Scripts\\python.exe dev\\scripts\\audit_direct_owner_guard.py")
    lines.append(".\\.venv\\Scripts\\python.exe dev\\scripts\\audit_lp_pdf_selector_ownership.py")
    lines.append("```")
    lines.append("")
    lines.append("## Core Principle Status")
    lines.append("")
    if data["hardViolations"]:
        lines.append("Hard violations detected:")
        for item in data["hardViolations"]:
            lines.append(f"- `{item['module']}` line {item['line']}: `{item['selector']}`")
    else:
        lines.append("No hard core-owner selector violations were detected by this map builder.")
    lines.append("")
    lines.append("This map is descriptive. It does not replace `audit_direct_owner_guard.py`, `audit_v3_hit_routing.py`, `audit_lp_pdf_selector_ownership.py`, or `release_check.py`.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if generated map artifacts are stale.")
    args = parser.parse_args()
    data, markdown = build()
    json_text = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    markdown_text = markdown + "\n"
    runtime_text = render_runtime_debug_protocol() + "\n"
    table_snippet_text = render_table_cell_snippet()
    matched_snippet_text = render_matched_rules_snippet()
    if args.check:
        stale: list[str] = []
        if not OUT_JSON.is_file() or OUT_JSON.read_text(encoding="utf-8") != json_text:
            stale.append(OUT_JSON.relative_to(ROOT).as_posix())
        if not OUT_MD.is_file() or OUT_MD.read_text(encoding="utf-8") != markdown_text:
            stale.append(OUT_MD.relative_to(ROOT).as_posix())
        if not OUT_RUNTIME_MD.is_file() or OUT_RUNTIME_MD.read_text(encoding="utf-8") != runtime_text:
            stale.append(OUT_RUNTIME_MD.relative_to(ROOT).as_posix())
        if not TABLE_CELL_SNIPPET.is_file() or TABLE_CELL_SNIPPET.read_text(encoding="utf-8") != table_snippet_text:
            stale.append(TABLE_CELL_SNIPPET.relative_to(ROOT).as_posix())
        if not MATCHED_RULES_SNIPPET.is_file() or MATCHED_RULES_SNIPPET.read_text(encoding="utf-8") != matched_snippet_text:
            stale.append(MATCHED_RULES_SNIPPET.relative_to(ROOT).as_posix())
        if stale:
            print("FAIL: source usage map stale:")
            for item in stale:
                print(f"  - {item}")
            print("Re-run: python dev/scripts/build_source_usage_map.py")
            return 1
        print("OK: source usage map is fresh")
        return 0
    OUT_JSON.write_text(json_text, encoding="utf-8")
    OUT_MD.write_text(markdown_text, encoding="utf-8")
    SNIPPET_DIR.mkdir(parents=True, exist_ok=True)
    OUT_RUNTIME_MD.write_text(runtime_text, encoding="utf-8")
    TABLE_CELL_SNIPPET.write_text(table_snippet_text, encoding="utf-8")
    MATCHED_RULES_SNIPPET.write_text(matched_snippet_text, encoding="utf-8")
    print(f"OK: wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"OK: wrote {OUT_MD.relative_to(ROOT)}")
    print(f"OK: wrote {OUT_RUNTIME_MD.relative_to(ROOT)}")
    print(f"OK: wrote {TABLE_CELL_SNIPPET.relative_to(ROOT)}")
    print(f"OK: wrote {MATCHED_RULES_SNIPPET.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())