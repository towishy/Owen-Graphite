# Selector Owner Cheatsheet

Use this for quick selector-to-owner routing. If a selector appears in a runtime matched rule, map it here first, then confirm with `MAP/source-usage-map.md` and `MAP/owner-registry.json`.

| Selector / Pattern | Owner | Read Also | Rule |
| --- | --- | --- | --- |
| `.markdown-rendered table`, `.markdown-preview-view table` | `src/surfaces/20-reading-tables-code.css` | `WORKFLOWS/table.md` | Rendered tables only. |
| `.markdown-source-view.mod-cm6 ... table:not(.cm-table):not(.cm-table-widget)` | `src/base/13-live-preview.css`, `src/surfaces/24-html-table-live-preview-glass.css` | `WORKFLOWS/table.md` | LP HTML embeds only. |
| `.cm-table-widget`, `table.cm-table` | Obsidian core | `INCIDENTS/table-row-inflation.md` | Do not style theme geometry. |
| `.HyperMD-table-row` | Obsidian/CM6 hit routing | `MAP/cm6-hit-routing-contract.md` | Do not route table fixes through descendants. |
| `.cm-line`, `.cm-content`, `.cm-editor`, `.cm-scroller` | `src/base/13-live-preview.css` | `WORKFLOWS/live-preview-cm6.md` | Scope carefully; nested editors exist. |
| `.callout`, `.markdown-rendered blockquote`, task list selectors | `src/surfaces/21-reading-callouts-lists.css` | `SRC/surfaces.md` | Avoid left rails. |
| `pre`, `code`, `.cm-preview-code-block`, `.token.*`, `.cm-*` syntax | `src/surfaces/20-reading-tables-code.css` plus PDF closure when print scoped | `DOCS/v3/golden-image-scenarios.md` | Keep LP/Reading/PDF parity. |
| `.workspace-tab-header`, `.mod-root`, `.workspace-leaf` | `src/chrome/30-workspace.css`, `src/chrome/37-tabs-file-explorer-search.css` | `WORKFLOWS/chrome-ui.md` | Runtime states need evidence. |
| `.nav-file`, `.nav-folder`, file explorer action icons | `src/chrome/37-tabs-file-explorer-search.css` | `SRC/chrome.md` | Do not fix from overlay modules. |
| `.workspace-ribbon`, `.side-dock-ribbon`, ribbon icons | `src/chrome/34-nav-ribbon-glass.css` | `MAP/top-chrome-icon-background-contract.md` | Top chrome contract applies. |
| `.menu`, `.suggestion-container`, `.popover`, `.modal`, `.prompt` | `src/chrome/32-overlay-popover-dataview.css`, `35`, `36` | `SRC/chrome.md` | Overlay owner, not workspace owner. |
| `.setting-item`, `.setting-tab-container`, Style Settings controls | `src/chrome/33-settings-controls.css`, `src/features/40-style-settings.css` | `WORKFLOWS/docs-assets.md` | Contract audit for settings metadata. |
| `body.ogd-report-mode`, `@media print`, `@page` | `src/features/42-report-print-polish.css`, `43-print-base.css` | `WORKFLOWS/pdf.md` | Print scope must not leak to screen. |
| `ogd-pdf-header-*`, `ogd-pdf-footer-*` | `src/features/41-feature-presets.css` | `MAP/pdf-header-footer-contract.md` | Marginalia owner stays in presets. |
| `.dataview`, `.task-list-item`, `.canvas`, `.graph-view`, `.mermaid` | `src/chrome/32-overlay-popover-dataview.css` for Dataview, `src/plugins/60-canvas-graph-link-panes.css` for Canvas/Graph, `src/plugins/61-live-preview-mobile-plugin.css` for Mermaid/mobile/plugin embeds | `PLUGINS/compatibility-matrix.md` | Plugin CSS does not own core document geometry. |

If a selector is not listed, use `OWNER-DECISION-TREE.md` and update this cheatsheet after the owner is confirmed.
