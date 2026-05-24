# Runtime: Plugins

Use this when the selector belongs to a plugin or plugin-like generated DOM.

## Plugin Routes

| Plugin / Surface | Typical Selectors | Owner Route |
| --- | --- | --- |
| Dataview | `.dataview`, `.table-view-table` | `src/plugins/*` or overlay support when scoped |
| Tasks | `.task-list-item`, checkbox markers | `src/surfaces/21-reading-callouts-lists.css` or plugin support |
| Canvas | `.canvas-*` | `src/plugins/60-canvas-graph-link-panes.css` |
| Graph | graph controls/classes | `src/plugins/60-canvas-graph-link-panes.css` |
| Mermaid | `.mermaid`, SVG/image output | `src/plugins/61-live-preview-mobile-plugin.css` when plugin-specific |
| Bookmarks/Outline/Search | Obsidian chrome lists | `src/chrome/*` by owner |

## Evidence

- Plugin enabled state and version when available.
- DOM chain from real plugin output or a fixture that matches it.
- Matched rules and source owner mapping.
- Confirmation the rule does not affect core Reading/Live Preview geometry unintentionally.

## Rule

Plugin CSS should not become the owner for core document geometry. If the fix also affects ordinary Markdown, route it through the core owner first.
