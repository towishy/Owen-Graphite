# Cascade Ownership

This MAP is based on `src/entry.css`, which is the authoritative v3 import order. The theme is intentionally unlayered; file order plus specificity is the cascade strategy.

## Import Order Groups

| Rank | Imports | Parity role |
| --- | --- | --- |
| 00 | `src/features/40-style-settings.css` | Defines user-facing style classes, including `ogd-pdf-*` classes. |
| 01 | `src/tokens/00-light-tokens.css`, `src/tokens/01-dark-tokens.css` | Shared bridge tokens. Any cross-surface setting should start here when possible. |
| 02-04 | `src/base/10-base-workspace.css`, `src/base/12-reading-content.css`, `src/surfaces/20-reading-tables-code.css`, `src/surfaces/21-reading-callouts-lists.css`, `src/surfaces/22-reading-embeds-workspace.css`, `src/themes/50-dark.css`, `src/features/43-print-base.css` | Base reading and print primitives. These are early enough to be overridden later. |
| 05 | `src/base/13-live-preview.css` | Main Live Preview owner for CM6 line geometry, source-line code blocks, callouts, tables, links, inline code, and headings. |
| 06 | `src/features/41-feature-presets.css` | Style Settings class behavior. Owns many `ogd-pdf-*` presets and code theme presets. |
| 07-09 | `src/chrome/*`, `src/plugins/*`, `src/features/42-report-print-polish.css` | Workspace/plugin polish plus print/report refinements. `42-report-print-polish.css` is a major PDF owner. |
| 10a-10c | `src/themes/51-accessibility-motion-contrast.css`, `src/surfaces/23-liquid-glass-core.css`, `src/surfaces/24-html-table-live-preview-glass.css` | Final imported owners after late polish retirement. New LP/PDF fixes should stay in their direct owner modules. |

## Live Preview Ownership

| Area | Primary files | Root selectors |
| --- | --- | --- |
| CM6 editor base | `src/base/10-base-workspace.css` | `.markdown-source-view.mod-cm6 .cm-content`, `.markdown-source-view.mod-cm6 .cm-line` |
| Headings and source lines | `src/base/13-live-preview.css` | `.markdown-source-view.mod-cm6 .cm-line.HyperMD-header-*` |
| Source code blocks | `src/base/12-reading-content.css`, `src/base/13-live-preview.css`, `src/surfaces/20-reading-tables-code.css` | `.markdown-source-view.mod-cm6 .cm-line.HyperMD-codeblock*` |
| Rendered code widgets | `src/base/13-live-preview.css`, `src/surfaces/20-reading-tables-code.css` | `.markdown-source-view.mod-cm6 :is(.cm-preview-code-block, .cm-hmd-codeblock) pre` |
| Callout widgets | `src/base/13-live-preview.css`, `src/surfaces/23-liquid-glass-core.css`, `src/plugins/61-live-preview-mobile-plugin.css` | `.markdown-source-view.mod-cm6 .cm-callout`, `.markdown-source-view.mod-cm6 .cm-line.HyperMD-callout` |
| Table widgets | `src/base/13-live-preview.css`, `src/surfaces/23-liquid-glass-core.css`, `src/surfaces/24-html-table-live-preview-glass.css`, `src/plugins/61-live-preview-mobile-plugin.css` | `.markdown-source-view.mod-cm6 .cm-table-widget`, `.markdown-source-view.mod-cm6 :is(.cm-html-embed, .cm-embed-block) table` |
| Mobile LP constraints | `src/plugins/61-live-preview-mobile-plugin.css` | `.markdown-source-view.mod-cm6 ...` within mobile/media rules |

## Export PDF Ownership

| Area | Primary files | Root selectors |
| --- | --- | --- |
| Page size and print base | `src/features/43-print-base.css` | `@media print`, `@page`, `.markdown-rendered`, `.markdown-preview-view` |
| PDF Style Settings | `src/features/40-style-settings.css`, `src/features/41-feature-presets.css` | `body.ogd-pdf-*` |
| PDF header/footer marginalia | `src/features/41-feature-presets.css` | `body.ogd-pdf-header-enabled`, `body.ogd-pdf-footer-enabled`, `.markdown-rendered::before`, `.markdown-rendered > :last-child::after` |
| Report print polish | `src/features/42-report-print-polish.css` | `@media print` + tables, callouts, images, figures, links, code blocks |
| Print fallback and direct-owner closure | `src/features/42-report-print-polish.css`, `src/features/43-print-base.css` | `@media print` rules for code, H1, layout, and PDF-safe fallbacks |

## High-Risk Cascade Points

| Point | Risk | Current guidance |
| --- | --- | --- |
| `src/features/41-feature-presets.css` | Preset classes can outrank generic print rules. | When adding PDF typography or palette presets, include matching final print guards if needed. |
| `src/surfaces/23-liquid-glass-core.css` | Imported late after some print files; may affect LP widgets after base LP rules. | Keep LP glass rules scoped to `.markdown-source-view.mod-cm6` or non-print contexts unless intentionally shared. |
