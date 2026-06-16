# Owen Graphite Source Usage Map

Generated from `src/entry.css`, `dev/WIKI/MAP/owner-registry.json`, and `dev/WIKI/MAP/effective-source-map.json`.

Canonical WIKI location: `dev/WIKI/MAP/source-usage-map.md`. Machine provenance remains in `dev/WIKI/MAP`.

## Summary

- Source modules: 26
- Source CSS lines: 19431
- Parsed CSS rules: 2536
- Selector parts: 3967
- Hard core-owner violations: 10

## Surface Totals

- `callout-list`: 434 rules
- `cm6`: 352 rules
- `code`: 1019 rules
- `lp-html-table`: 83 rules
- `lp-markdown-table-widget-reference`: 94 rules
- `overlay-search`: 285 rules
- `print-pdf`: 529 rules
- `reading-rendered`: 1177 rules
- `table`: 1129 rules
- `workspace-chrome`: 591 rules

## Quick Routing

Use this table before editing. Start at the owner module, then inspect allowed-late modules only when the owner registry explicitly allows them.

| Work Area | Start Here | Allowed Follow-Up | Must Check |
| --- | --- | --- | --- |
| Reading typography, links, headings | `src/base/12-reading-content.css` | theme overrides in `src/themes/50-dark.css` when dark-only | `reading-typography` owner surface |
| Reading/rendered tables and code | `src/surfaces/20-reading-tables-code.css` | `src/features/42-report-print-polish.css` for print/report only | `Table Selector Rules` below |
| Live Preview CM6 line geometry | `src/base/13-live-preview.css` | none | `dev/WIKI/MAP/cm6-hit-routing-contract.md` |
| Live Preview markdown table widget | Obsidian core, no theme geometry owner | none | Do not style `.cm-table-widget` or `table.cm-table` |
| Live Preview HTML table embed | `src/base/13-live-preview.css`, `src/surfaces/24-html-table-live-preview-glass.css` | `src/features/42-report-print-polish.css` utilities only | Must include `:not(.cm-table-widget)` and `:not(.cm-table)` |
| PDF header/footer marginalia | `src/features/41-feature-presets.css`, `src/tokens/00-light-tokens.css`, `src/tokens/01-dark-tokens.css` | none | `dev/WIKI/MAP/pdf-header-footer-contract.md` |
| Workspace chrome | `src/chrome/30-workspace.css`, `src/chrome/31-navigation-tasks-search.css`, `src/chrome/34-nav-ribbon-glass.css`, `src/chrome/37-tabs-file-explorer-search.css` | none | `dev/WIKI/MAP/top-chrome-icon-background-contract.md` |
| Menus, popovers, search, modals | `src/chrome/32-overlay-popover-dataview.css`, `src/chrome/35-editing-menu-tooltip-glass.css`, `src/chrome/36-floating-ui-glass-system.css` | none | overlay/search selectors in this map |

## Core Principle Workflow

Before editing CSS:

1. Identify the target surface in `Quick Routing`.
2. Open the owner module first; do not start from a later visual module.
3. Read linked risk contracts when the target is CM6, table, PDF, or top chrome.
4. Remove or merge conflicting follow-up rules instead of adding a new override.
5. Run `build_source_usage_map.py --check` and `audit_core_principles.py` before commit.

Forbidden workflow:

- Adding a new late fix because the owner was hard to locate.
- Styling Obsidian-owned markdown table widget geometry.
- Reintroducing `src/polish/*` or `!important`.
- Treating allowed-late modules as broad ownership permission.

## Known Failure Modes

These are real failure patterns that should stop work until the owner and runtime evidence are clear.

| Failure Mode | Symptom | Root Risk | Correct Response |
| --- | --- | --- | --- |
| Broad CM6 editor selector | Nested editors inside widgets inherit page-level geometry | `.cm-content`, `.cm-line`, `.cm-editor`, or `.cm-scroller` selectors can hit embedded editors | Narrow the owner selector or inspect runtime DOM before editing |
| Markdown table widget styled as theme table | Selecting a markdown table cell changes row geometry or hit routing | `.cm-table-widget` / `table.cm-table` belongs to Obsidian core | Do not style widget geometry; target rendered tables or HTML embeds only |
| Rendered table and LP widget grouped together | A table fix works in Reading View but breaks Live Preview editing | Selector group mixes `.markdown-rendered table` with source-mode widgets | Split by surface and owner before changing properties |
| Late visual module used as repair layer | A fix only works because it wins late in cascade | Owner module remains wrong and future edits become unpredictable | Move the rule to the owner and remove the late correction |
| Sync/debug confusion | CSS appears unchanged after a fix | Vault path, theme cache, or runtime DOM not verified | Compare repo/vault CSS and capture computed styles before more edits |
| Inline/runtime height | CSS changes do not affect selected row height | Obsidian runtime may set inline style or non-theme DOM state | Use Runtime Debug Protocol; do not add stronger CSS blindly |

## Runtime Debug Protocol

See `dev/WIKI/runtime-debug-protocol.md` and the snippets in `dev/WIKI/runtime-debug-snippets/`.

## If You Touch X

| Selector Or Feature | Owner First | Also Inspect | Never Do |
| --- | --- | --- | --- |
| `.markdown-rendered table`, `.markdown-preview-view table` | `src/surfaces/20-reading-tables-code.css` | `src/features/42-report-print-polish.css`, `src/surfaces/23-liquid-glass-core.css` | Mix with `.cm-table-widget` |
| `.cm-table-widget`, `table.cm-table` | Obsidian core | runtime DOM, `cm6-hit-routing-contract.md` | Add theme geometry or visual table styling |
| LP HTML `<table>` embed | `src/base/13-live-preview.css`, `src/surfaces/24-html-table-live-preview-glass.css` | `src/features/42-report-print-polish.css` utilities | Omit `:not(.cm-table-widget):not(.cm-table)` |
| `.cm-line`, `.HyperMD-*` | `src/base/13-live-preview.css` | `cm6-hit-routing-contract.md` | Add vertical margin/padding to hit-routed lines |
| Callouts and blockquotes | `src/surfaces/21-reading-callouts-lists.css` | `src/base/13-live-preview.css`, `src/surfaces/23-liquid-glass-core.css` | Add left rails or late visual repair without owner edit |
| Code blocks | `src/surfaces/20-reading-tables-code.css` | `src/base/13-live-preview.css`, `src/features/42-report-print-polish.css` | Split LP/Reading/PDF parity without checking map |
| `ogd-pdf-header-*`, `ogd-pdf-footer-*` | `src/features/41-feature-presets.css` | token files, `pdf-header-footer-contract.md` | Put header/footer owner rules in `42-report-print-polish` |
| Top tabs/ribbon/sidebar icons | `src/chrome/34-nav-ribbon-glass.css`, `src/chrome/37-tabs-file-explorer-search.css` | `top-chrome-icon-background-contract.md` | Add broad top-chrome selectors in overlay modules |
| Menus, suggestions, modals, popovers | `src/chrome/32-overlay-popover-dataview.css`, `src/chrome/35-editing-menu-tooltip-glass.css`, `src/chrome/36-floating-ui-glass-system.css` | accessibility/motion module | Treat overlay state as workspace chrome owner |

## Audit Coverage Matrix

| Audit | Catches | Does Not Catch |
| --- | --- | --- |
| `build_source_usage_map.py --check` | Stale source map, missing generated overview | Runtime visual regressions |
| `audit_core_principles.py` | Missing map, `src/polish`, `!important`, owner registry drift, core guard, selector ownership, hit routing | Inline Obsidian runtime styles |
| `audit_direct_owner_guard.py` | `.cm-table-widget` / `table.cm-table` direct styling, generic LP table selectors, PDF header/footer owner drift | Semantic owner disputes outside encoded rules |
| `audit_lp_pdf_selector_ownership.py` | LP/PDF selector ownership distribution | Whether a visual change looks correct |
| `audit_v3_hit_routing.py` | Known CM6 hit-routing hazards | Rendered Reading View table aesthetics |
| `audit_pdf_header_footer.py` | PDF marginalia owner contract | Non-marginalia PDF typography |
| `v3_audit_duplicate_selectors.py` | In-file duplicate and cross-file selector groups | Whether duplicate intent is valid |
| Runtime DevTools protocol | Actual selected/hover/focus DOM and computed style | Static owner drift unless matched rule is mapped back |

## Audit Blind Spot Follow-Ups

| Blind Spot | Required Follow-Up |
| --- | --- |
| Runtime inline style | Run `matched-rules-dump.js`; inspect `style` before adding CSS |
| Obsidian internal DOM change | Capture DOM chain and compare with core contracts |
| Vault plugin/snippet influence | Inspect `.obsidian/appearance.json`, enabled snippets, and plugin CSS/JS |
| Visual-only layout shift | Create or update a fixture/screenshot audit before changing CSS |
| OS/version-specific behavior | Record OS, Obsidian version, theme path, and runtime state |

## Change Type Checklists

### Table

- Open `src/surfaces/20-reading-tables-code.css` first for rendered tables.
- Open `src/base/13-live-preview.css` or `src/surfaces/24-html-table-live-preview-glass.css` for Live Preview HTML tables.
- Run `audit_direct_owner_guard.py`, `audit_lp_pdf_selector_ownership.py`, and `audit_v3_hit_routing.py`.

### Live Preview

- Open `src/base/13-live-preview.css` first.
- Read `dev/WIKI/MAP/cm6-hit-routing-contract.md` before changing geometry.
- Run `audit_v3_hit_routing.py` and `audit_core_principles.py`.

### PDF

- Open `src/features/43-print-base.css`, `src/features/41-feature-presets.css`, or `src/features/42-report-print-polish.css` according to the surface.
- Read `dev/WIKI/MAP/pdf-header-footer-contract.md` for marginalia.
- Run `audit_pdf_header_footer.py` and `release_check.py --skip-bundle`.

### Chrome/UI

- Open `src/chrome/*` owner modules according to `Quick Routing`.
- Read `dev/WIKI/MAP/top-chrome-icon-background-contract.md` for top chrome icons.
- Run `audit_core_principles.py` and screenshot/runtime checks for interactive states.

### Docs/README

- Update docs and sample assets in the documented locations.
- Run `audit_docs_assets.py` and `audit_readme_svg_layout.py`.

### Release

- Run `bundle_v3.py`, `release_check.py --skip-bundle`, and `build_release.py`.
- Run `audit_release_zip.py` before publishing.


## Cascade And Ownership Map

| # | Module | Bundle Lines | Source Lines | Primary Owners | Major Labels | Cascade Relation |
| ---: | --- | --- | ---: | --- | --- | --- |
| 1 | `src/features/40-style-settings.css` | 45-818 | 832 | style-settings-contract | metadata/tokens | after `None`; before `src/tokens/00-light-tokens.css` |
| 2 | `src/tokens/00-light-tokens.css` | 822-1088 | 266 | pdf-marginalia, shared-tokens | callout-list:1, code:5, print-pdf:2, table:1, workspace-chrome:1 | after `src/features/40-style-settings.css`; before `src/tokens/01-dark-tokens.css` |
| 3 | `src/tokens/01-dark-tokens.css` | 1091-1306 | 230 | pdf-marginalia, shared-tokens | callout-list:2, code:2, overlay-search:1, print-pdf:1, table:7, workspace-chrome:1 | after `src/tokens/00-light-tokens.css`; before `src/base/10-base-workspace.css` |
| 4 | `src/base/10-base-workspace.css` | 1310-1444 | 131 | support: base/embed workspace primitives | cm6:5, code:5, overlay-search:5, reading-rendered:7, table:8, workspace-chrome:5 | after `src/tokens/01-dark-tokens.css`; before `src/base/12-reading-content.css` |
| 5 | `src/base/12-reading-content.css` | 1448-2377 | 1393 | reading-typography | callout-list:29, cm6:9, code:113, overlay-search:1, print-pdf:14, reading-rendered:133, table:19, workspace-chrome:4 | after `src/base/10-base-workspace.css`; before `src/surfaces/20-reading-tables-code.css` |
| 6 | `src/surfaces/20-reading-tables-code.css` | 2381-3418 | 1126 | reading-tables-code, dataview-plugin-support (allowed-late) | cm6:24, code:143, print-pdf:9, reading-rendered:130, table:53, workspace-chrome:77 | after `src/base/12-reading-content.css`; before `src/surfaces/21-reading-callouts-lists.css` |
| 7 | `src/surfaces/21-reading-callouts-lists.css` | 3422-4264 | 877 | reading-callouts-lists | callout-list:106, cm6:3, code:71, reading-rendered:122, table:9, workspace-chrome:1 | after `src/surfaces/20-reading-tables-code.css`; before `src/surfaces/22-reading-embeds-workspace.css` |
| 8 | `src/surfaces/22-reading-embeds-workspace.css` | 4268-4496 | 248 | support: reading embed/workspace primitives | callout-list:4, cm6:6, code:5, overlay-search:1, reading-rendered:18, table:5, workspace-chrome:6 | after `src/surfaces/21-reading-callouts-lists.css`; before `src/themes/50-dark.css` |
| 9 | `src/themes/50-dark.css` | 4500-4996 | 606 | support: dark theme support | callout-list:35, cm6:6, code:48, overlay-search:3, print-pdf:2, reading-rendered:85, table:91, workspace-chrome:4 | after `src/surfaces/22-reading-embeds-workspace.css`; before `src/features/43-print-base.css` |
| 10 | `src/features/43-print-base.css` | 5000-5370 | 680 | pdf-base | callout-list:28, cm6:1, code:81, print-pdf:92, reading-rendered:87, table:8, workspace-chrome:1 | after `src/themes/50-dark.css`; before `src/base/13-live-preview.css` |
| 11 | `src/base/13-live-preview.css` | 5374-6447 | 1337 | live-preview-cm6, live-preview-rendered-widgets | callout-list:30, cm6:184, code:41, lp-html-table:18, lp-markdown-table-widget-reference:29, print-pdf:11, reading-rendered:10, table:71 | after `src/features/43-print-base.css`; before `src/features/41-feature-presets.css` |
| 12 | `src/features/41-feature-presets.css` | 6451-8032 | 1592 | pdf-marginalia | callout-list:24, cm6:4, code:81, overlay-search:2, print-pdf:157, reading-rendered:127, table:38, workspace-chrome:11 | after `src/base/13-live-preview.css`; before `src/chrome/30-workspace.css` |
| 13 | `src/chrome/30-workspace.css` | 8036-8817 | 696 | workspace-chrome, mobile-narrow-layout | callout-list:26, cm6:3, code:22, overlay-search:4, print-pdf:3, reading-rendered:69, table:68, workspace-chrome:6 | after `src/features/41-feature-presets.css`; before `src/chrome/31-navigation-tasks-search.css` |
| 14 | `src/chrome/31-navigation-tasks-search.css` | 8821-9021 | 201 | workspace-chrome | callout-list:21, cm6:1, code:2, overlay-search:2, reading-rendered:25, table:20, workspace-chrome:16 | after `src/chrome/30-workspace.css`; before `src/chrome/32-overlay-popover-dataview.css` |
| 15 | `src/chrome/32-overlay-popover-dataview.css` | 9025-9331 | 350 | overlay-menu-search, dataview-plugin-support | code:24, overlay-search:15, reading-rendered:24, table:24 | after `src/chrome/31-navigation-tasks-search.css`; before `src/chrome/33-settings-controls.css` |
| 16 | `src/chrome/33-settings-controls.css` | 9335-9764 | 437 | settings-controls | overlay-search:61, table:76 | after `src/chrome/32-overlay-popover-dataview.css`; before `src/plugins/60-canvas-graph-link-panes.css` |
| 17 | `src/plugins/60-canvas-graph-link-panes.css` | 9768-10161 | 393 | support: external/plugin support | code:2, overlay-search:27, table:48, workspace-chrome:12 | after `src/chrome/33-settings-controls.css`; before `src/plugins/61-live-preview-mobile-plugin.css` |
| 18 | `src/plugins/61-live-preview-mobile-plugin.css` | 10165-10682 | 532 | mobile-narrow-layout | callout-list:1, cm6:23, code:27, overlay-search:6, print-pdf:2, reading-rendered:27, table:36, workspace-chrome:16 | after `src/plugins/60-canvas-graph-link-panes.css`; before `src/features/42-report-print-polish.css` |
| 19 | `src/features/42-report-print-polish.css` | 10686-12744 | 2078 | reading-tables-code (allowed-late), pdf-base (allowed-late), pdf-report-polish | callout-list:60, cm6:3, code:260, lp-html-table:2, lp-markdown-table-widget-reference:2, print-pdf:211, reading-rendered:261, table:125, workspace-chrome:52 | after `src/plugins/61-live-preview-mobile-plugin.css`; before `src/chrome/34-nav-ribbon-glass.css` |
| 20 | `src/chrome/34-nav-ribbon-glass.css` | 12748-13009 | 263 | workspace-chrome | cm6:1, code:3, reading-rendered:1, table:13, workspace-chrome:23 | after `src/features/42-report-print-polish.css`; before `src/chrome/35-editing-menu-tooltip-glass.css` |
| 21 | `src/chrome/35-editing-menu-tooltip-glass.css` | 13013-14092 | 1083 | overlay-menu-search | cm6:6, code:6, overlay-search:35, reading-rendered:6, table:32, workspace-chrome:45 | after `src/chrome/34-nav-ribbon-glass.css`; before `src/chrome/36-floating-ui-glass-system.css` |
| 22 | `src/chrome/36-floating-ui-glass-system.css` | 14096-15148 | 1037 | overlay-menu-search | code:4, overlay-search:62, print-pdf:1, reading-rendered:4, table:64, workspace-chrome:26 | after `src/chrome/35-editing-menu-tooltip-glass.css`; before `src/chrome/37-tabs-file-explorer-search.css` |
| 23 | `src/chrome/37-tabs-file-explorer-search.css` | 15152-16079 | 979 | workspace-chrome | overlay-search:10, table:143, workspace-chrome:190 | after `src/chrome/36-floating-ui-glass-system.css`; before `src/themes/51-accessibility-motion-contrast.css` |
| 24 | `src/themes/51-accessibility-motion-contrast.css` | 16083-16251 | 170 | support: accessibility/motion/contrast support | callout-list:4, cm6:4, code:11, overlay-search:7, print-pdf:2, reading-rendered:2, table:4, workspace-chrome:7 | after `src/chrome/37-tabs-file-explorer-search.css`; before `src/surfaces/23-liquid-glass-core.css` |
| 25 | `src/surfaces/23-liquid-glass-core.css` | 16255-17926 | 1656 | reading-callouts-lists (allowed-late), live-preview-rendered-widgets | cm6:6, code:49, overlay-search:43, print-pdf:7, reading-rendered:39, table:103, workspace-chrome:87 | after `src/themes/51-accessibility-motion-contrast.css`; before `src/surfaces/24-html-table-live-preview-glass.css` |
| 26 | `src/surfaces/24-html-table-live-preview-glass.css` | 17930-18169 | 238 | live-preview-rendered-widgets | callout-list:63, cm6:63, code:14, lp-html-table:63, lp-markdown-table-widget-reference:63, print-pdf:15, table:63 | after `src/surfaces/23-liquid-glass-core.css`; before `None` |

## Table Code Map

Table-related rules are intentionally split by surface:

- Reading/rendered tables: `src/surfaces/20-reading-tables-code.css`; report/print extensions in `src/features/42-report-print-polish.css`.
- Live Preview markdown table widgets: Obsidian core-owned; theme CSS must not style `.cm-table-widget` / `table.cm-table` geometry.
- Live Preview HTML table embeds: `src/base/13-live-preview.css`, `src/surfaces/24-html-table-live-preview-glass.css`, and utility hooks in `src/features/42-report-print-polish.css`.
- Late visual table surface: `src/surfaces/23-liquid-glass-core.css` for rendered/non-core surfaces only.

| Module | Table Rules | LP HTML Table Rules | Reading/Rendered Rules | Print/PDF Rules |
| --- | ---: | ---: | ---: | ---: |
| `src/tokens/00-light-tokens.css` | 1 | 0 | 0 | 2 |
| `src/tokens/01-dark-tokens.css` | 7 | 0 | 0 | 1 |
| `src/base/10-base-workspace.css` | 8 | 0 | 7 | 0 |
| `src/base/12-reading-content.css` | 19 | 0 | 133 | 14 |
| `src/surfaces/20-reading-tables-code.css` | 53 | 0 | 130 | 9 |
| `src/surfaces/21-reading-callouts-lists.css` | 9 | 0 | 122 | 0 |
| `src/surfaces/22-reading-embeds-workspace.css` | 5 | 0 | 18 | 0 |
| `src/themes/50-dark.css` | 91 | 0 | 85 | 2 |
| `src/features/43-print-base.css` | 8 | 0 | 87 | 92 |
| `src/base/13-live-preview.css` | 71 | 18 | 10 | 11 |
| `src/features/41-feature-presets.css` | 38 | 0 | 127 | 157 |
| `src/chrome/30-workspace.css` | 68 | 0 | 69 | 3 |
| `src/chrome/31-navigation-tasks-search.css` | 20 | 0 | 25 | 0 |
| `src/chrome/32-overlay-popover-dataview.css` | 24 | 0 | 24 | 0 |
| `src/chrome/33-settings-controls.css` | 76 | 0 | 0 | 0 |
| `src/plugins/60-canvas-graph-link-panes.css` | 48 | 0 | 0 | 0 |
| `src/plugins/61-live-preview-mobile-plugin.css` | 36 | 0 | 27 | 2 |
| `src/features/42-report-print-polish.css` | 125 | 2 | 261 | 211 |
| `src/chrome/34-nav-ribbon-glass.css` | 13 | 0 | 1 | 0 |
| `src/chrome/35-editing-menu-tooltip-glass.css` | 32 | 0 | 6 | 0 |
| `src/chrome/36-floating-ui-glass-system.css` | 64 | 0 | 4 | 1 |
| `src/chrome/37-tabs-file-explorer-search.css` | 143 | 0 | 0 | 0 |
| `src/themes/51-accessibility-motion-contrast.css` | 4 | 0 | 2 | 2 |
| `src/surfaces/23-liquid-glass-core.css` | 103 | 0 | 39 | 7 |
| `src/surfaces/24-html-table-live-preview-glass.css` | 63 | 63 | 0 | 15 |

## Table Selector Rules

Allowed:

- Rendered tables in `src/surfaces/20-reading-tables-code.css`: `:is(.markdown-rendered, .markdown-preview-view, .markdown-reading-view) table ...`
- Print/report table extensions in `src/features/42-report-print-polish.css` when the rule is print/report scoped.
- Live Preview HTML table embeds with both guards: `.markdown-source-view.mod-cm6 ... table:not(.cm-table):not(.cm-table-widget)`.

Forbidden:

- `.markdown-source-view.mod-cm6 .cm-table-widget ...`
- `.markdown-source-view.mod-cm6 table.cm-table ...`
- `.HyperMD-table-row ... td/th/tr/table/.table-cell-wrapper` geometry rules.
- Generic `.markdown-source-view.mod-cm6 ... table` without both `:not(.cm-table-widget)` and `:not(.cm-table)`.

## Table Selector Reverse Index

| Pattern | Owner | Purpose | Status |
| --- | --- | --- | --- |
| `.markdown-rendered table / .markdown-preview-view table` | src/surfaces/20-reading-tables-code.css | Reading/rendered table primitives and ordinary table surfaces | allowed |
| `.markdown-source-view.mod-cm6 ... table:not(.cm-table):not(.cm-table-widget)` | src/base/13-live-preview.css and src/surfaces/24-html-table-live-preview-glass.css | Live Preview HTML table embeds only | allowed with both guards |
| `.cm-table-widget / table.cm-table` | Obsidian core | Live Preview markdown table widget geometry | forbidden for theme geometry |
| `body.ogd-report-mode ... table / @media print table` | src/features/42-report-print-polish.css | Report/PDF table output and print-safe adjustments | allowed in report/print scope |
| `table caption / .table-caption / .table-source` | src/surfaces/23-liquid-glass-core.css and src/features/42-report-print-polish.css | Rendered captions and report notes | allowed for rendered/report surfaces |

## Risk Contracts

| Contract | Applies To | When To Read |
| --- | --- | --- |
| `dev/WIKI/MAP/cm6-hit-routing-contract.md` | CM6 line geometry, Live Preview widgets | Before editing `src/base/13-live-preview.css` or LP widgets |
| `dev/WIKI/MAP/live-preview-pdf-css-map/parity-guidelines.md` | LP/PDF parity, tables, code, callouts | Before changing table/code/callout behavior across LP/Reading/PDF |
| `dev/WIKI/MAP/pdf-header-footer-contract.md` | PDF marginalia | Before touching `ogd-pdf-header-*` or `ogd-pdf-footer-*` |
| `dev/WIKI/MAP/top-chrome-icon-background-contract.md` | Top chrome/ribbon icon surfaces | Before touching titlebar, tabs, ribbon icons |

## Risk Contract Coverage Gaps

All owner surfaces have at least one risk contract.

## Allowed-Late Does Not Mean New Owner

`allowed-late` modules exist to preserve validated cascade order or print/report closure. They do not authorize new broad fixes. If a behavior has a clear owner, edit the owner first and use allowed-late modules only for their registered surface.

## Registered Support Modules

These modules have explicit support roles in `owner-registry.json`. They are not primary owners and must not be used as repair layers.

- `src/base/10-base-workspace.css`: base/embed workspace primitives; labels {'cm6': 5, 'code': 5, 'overlay-search': 5, 'reading-rendered': 7, 'table': 8, 'workspace-chrome': 5}
- `src/surfaces/22-reading-embeds-workspace.css`: reading embed/workspace primitives; labels {'callout-list': 4, 'cm6': 6, 'code': 5, 'overlay-search': 1, 'reading-rendered': 18, 'table': 5, 'workspace-chrome': 6}
- `src/themes/50-dark.css`: dark theme support; labels {'callout-list': 35, 'cm6': 6, 'code': 48, 'overlay-search': 3, 'print-pdf': 2, 'reading-rendered': 85, 'table': 91, 'workspace-chrome': 4}
- `src/plugins/60-canvas-graph-link-panes.css`: external/plugin support; labels {'code': 2, 'overlay-search': 27, 'table': 48, 'workspace-chrome': 12}
- `src/themes/51-accessibility-motion-contrast.css`: accessibility/motion/contrast support; labels {'callout-list': 4, 'cm6': 4, 'code': 11, 'overlay-search': 7, 'print-pdf': 2, 'reading-rendered': 2, 'table': 4, 'workspace-chrome': 7}

## Related Maps And Artifacts

- `dev/WIKI/MAP/theme-css-risk-map.html`: visual HTML risk map for selector density and risk review.
- `dev/WIKI/MAP/theme-css-risk-map.json`: machine-readable version of the risk map.
- `dev/WIKI/MAP/selector-provenance.json`: source selector provenance data.
- `dev/WIKI/MAP/unused-css-candidates.md`: unused/reserved selector analysis.
- `dev/WIKI/MAP/effective-source-map.json`: bundle line to source module mapping.

## Recent Incident Notes

| Incident | Wrong Approach | Correct Process | Gate |
| --- | --- | --- | --- |
| Table row expands when a cell is selected | Repeated selector guesses and late geometry resets | Capture runtime DOM/computed style, map matched rule to owner, edit owner only | `audit_core_principles.py`, runtime debug protocol |
| Table code hard to locate | Searching ad hoc selector fragments | Use `Table Selector Reverse Index`, `How To Find Table Code Quickly`, and source usage JSON | `build_source_usage_map.py --check` |

## How To Find Table Code Quickly

```powershell
.\.venv\Scripts\python.exe dev\scripts\build_source_usage_map.py --check
Select-String -Path src\**\*.css -Pattern 'table|td|th|tr|caption|cm-table-widget|table\.cm-table|HyperMD-table-row'
.\.venv\Scripts\python.exe dev\scripts\audit_direct_owner_guard.py
.\.venv\Scripts\python.exe dev\scripts\audit_lp_pdf_selector_ownership.py
```

## Core Principle Status

Hard violations detected:
- `src/base/13-live-preview.css` line 413: `body .markdown-source-view.mod-cm6 .cm-table-widget.markdown-rendered table.table-editor`
- `src/base/13-live-preview.css` line 414: `body .markdown-source-view.mod-cm6 .cm-table-widget.markdown-rendered table.table-editor :is(thead, tbody, tr)`
- `src/base/13-live-preview.css` line 415: `body .markdown-source-view.mod-cm6 .cm-table-widget.markdown-rendered table.table-editor :is(th, td)`
- `src/base/13-live-preview.css` line 416: `body .markdown-source-view.mod-cm6 .cm-table-widget.markdown-rendered table.table-editor th`
- `src/base/13-live-preview.css` line 417: `body .markdown-source-view.mod-cm6 .cm-table-widget.markdown-rendered table.table-editor tbody tr:hover :is(th, td)`
- `src/base/13-live-preview.css` line 418: `body.theme-dark .markdown-source-view.mod-cm6 .cm-table-widget.markdown-rendered table.table-editor`
- `src/base/13-live-preview.css` line 419: `body.theme-dark .markdown-source-view.mod-cm6 .cm-table-widget.markdown-rendered table.table-editor :is(thead, tbody, tr)`
- `src/base/13-live-preview.css` line 420: `body.theme-dark .markdown-source-view.mod-cm6 .cm-table-widget.markdown-rendered table.table-editor :is(th, td)`
- `src/base/13-live-preview.css` line 421: `body.theme-dark .markdown-source-view.mod-cm6 .cm-table-widget.markdown-rendered table.table-editor th`
- `src/base/13-live-preview.css` line 422: `body.theme-dark .markdown-source-view.mod-cm6 .cm-table-widget.markdown-rendered table.table-editor tbody tr:hover :is(th, td)`

This map is descriptive. It does not replace `audit_direct_owner_guard.py`, `audit_v3_hit_routing.py`, `audit_lp_pdf_selector_ownership.py`, or `release_check.py`.

