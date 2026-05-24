# Runtime Evidence Example: Plugin DOM

Use this as a completed example for plugin-generated DOM. Values are illustrative; capture fresh values from the real plugin when making a compatibility claim.

## Capture Header

| Field | Value |
| --- | --- |
| Issue | Dataview table hover state appears denser than rendered Markdown tables |
| Surface | Plugin |
| Runtime state | hovered |
| Obsidian version | 1.12.x |
| OS | Windows |
| Theme version | current working tree |
| Vault/theme path | `C:\OWEN\Drive\Obsidian\.obsidian\themes\Owen Graphite` |
| Repro note | Enable Dataview, render a query table, hover a row inside `.block-language-dataview`. |

## Required Evidence

1. DOM chain: `.markdown-rendered > .block-language-dataview > .dataview.table-view-table > tbody > tr:hover`.
2. Bounding rect chain: table row, cells, and plugin wrapper keep stable height on hover.
3. Computed geometry: table layout, padding, line-height, border-spacing, background, box-shadow, and overflow.
4. Matched rules: Dataview scoped rules map to `src/chrome/32-overlay-popover-dataview.css`; shared rendered table primitives map to `src/surfaces/20-reading-tables-code.css` only when selector is not plugin-scoped.
5. Inline style check: plugin does not inject inline padding or row height in this state.
6. Owner mapping: plugin-specific DOM route first; core table owner only for ordinary Markdown table behavior.
7. Screenshot/state note: hover state captured with plugin enabled and query output visible.

## Decision

| Question | Answer |
| --- | --- |
| Is a theme rule responsible? | Yes, plugin-scoped Dataview presentation. |
| If yes, which source owner? | `src/chrome/32-overlay-popover-dataview.css`, with table parity contract when table primitives are shared. |
| Is an inline/core rule responsible? | No inline row geometry observed. |
| Is CSS allowed by a risk contract? | Yes, plugin route plus `dev/WIKI/MAP/live-preview-pdf-css-map/parity-guidelines.md` for table parity. |
| Which workflow applies? | `RUNTIME/plugins.md` and `PLUGINS/runtime-dom-notes.md`. |
| Which audit proves the change? | `audit_core_principles.py`, `release_check.py --skip-bundle`, plus real plugin runtime recheck. |