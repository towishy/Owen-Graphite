# Plugin Runtime DOM Notes

Use this to record plugin DOM facts that static fixtures cannot prove.

## Capture Template

| Field | Value |
| --- | --- |
| Plugin / Surface |  |
| Obsidian version |  |
| Plugin version |  |
| Runtime state |  |
| DOM root selector |  |
| Matched theme rule |  |
| Source owner |  |
| Fixture gap |  |

## Evidence Rules

- Prefer real plugin DOM for plugin compatibility changes.
- If real DOM is unavailable, mark the fixture as an approximation.
- Do not remove reserved selectors from unused CSS reports solely because fixtures do not match plugin DOM.
- Update `compatibility-matrix.md` when a plugin route changes.

## Route Examples

| Plugin / Surface | DOM root selector | Source owner | Fixture gap |
| --- | --- | --- | --- |
| Dataview table | `.block-language-dataview .table-view-table` | `src/chrome/32-overlay-popover-dataview.css` first; `src/surfaces/20-reading-tables-code.css` only for shared table primitives | Needs real Dataview query output before removing reserved selectors |
| Canvas card/node | `.canvas-wrapper .canvas-node` | `src/plugins/60-canvas-graph-link-panes.css` | Needs real Canvas board state for zoom/selection/drag classes |
| Mermaid render | `.mermaid svg` or plugin-rendered image wrapper | `src/plugins/61-live-preview-mobile-plugin.css` when plugin-specific; rendered content owner when ordinary document flow changes | Needs actual rendered SVG/image output, not markdown source text |

See `dev/WIKI/runtime-evidence-example-plugin-dom.md` for the expected evidence shape.

Track coverage status in `dev/WIKI/PLUGINS/coverage-matrix.md` after adding real DOM evidence or fixture coverage.

## Captured Runtime Facts

| Date | Plugin / Surface | Runtime DOM | Source Owner | Evidence | Decision |
| --- | --- | --- | --- | --- | --- |
| 2026-05-25 | Canvas | `.canvas-wrapper`, `.canvas-node`, `.canvas-control-item`, `.canvas-card-menu-button`, `.canvas-edges path` | `src/plugins/60-canvas-graph-link-panes.css` | CDP capture in `dev/TEMP/runtime-evidence/2026-05-25-plugin-plugins-60-canvas-graph-link-panes.json`; temporary `_owen-runtime-cdp-capture.canvas` was removed after capture | Real DOM confirms Canvas support selectors are runtime-reserved; owner CSS now covers current `.canvas-card-menu-button` and `.canvas-edges path:hover` DOM |
| 2026-05-25 | Graph controls | `.workspace-leaf-content[data-type="graph"] .graph-controls`, `.graph-controls-button` | `src/plugins/60-canvas-graph-link-panes.css` | CDP capture in `dev/TEMP/runtime-evidence/2026-05-25-plugin-plugins-60-canvas-graph-link-panes.json` | Real DOM confirms graph control selectors are runtime-reserved in light and dark mode; graph canvas color visual states still need separate capture |
| 2026-05-25 | Backlinks / Outgoing links | `.backlink-pane .tree-item-self`, `.outgoing-link-pane .tree-item-self` | `src/plugins/60-canvas-graph-link-panes.css` | CDP capture in `dev/TEMP/runtime-evidence/2026-05-25-plugin-plugins-60-canvas-graph-link-panes.json` | Real DOM confirms row hover selectors are runtime-reserved |
| 2026-05-25 | Global Search results | `.search-result-file-title`, `.search-result-file-match` | `src/plugins/60-canvas-graph-link-panes.css` for link-pane/search polish; chrome/search owner for core search controls | CDP capture in `dev/TEMP/runtime-evidence/2026-05-25-plugin-plugins-60-canvas-graph-link-panes.json` | Real DOM confirms result row hover selectors are runtime-reserved |
| 2026-05-25 | Dataview | `.block-language-dataview table tr`, `.markdown-rendered .dataview.table-view-table` | `src/chrome/32-overlay-popover-dataview.css` for Dataview table hover support | Dataview 0.5.68 installed/enabled in `D:\Owen-WIKI`; CDP capture in `dev/TEMP/runtime-evidence/2026-05-25-chrome-chrome-32-overlay-popover-dataview.json`; temporary `_owen-runtime-dataview-capture.md` was removed after capture | Real DOM confirms Dataview table hover selectors are runtime-reserved |
