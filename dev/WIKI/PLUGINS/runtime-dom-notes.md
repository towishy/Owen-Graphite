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
