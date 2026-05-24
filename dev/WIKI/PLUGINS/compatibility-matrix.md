# Plugin Compatibility Matrix

Use this before changing plugin-specific CSS or public compatibility claims.

| Plugin / Surface | Owner Route | Check | Risk |
| --- | --- | --- | --- |
| Dataview | `src/chrome/32-overlay-popover-dataview.css` for Dataview tables/inline fields; rendered table owner only for ordinary Markdown tables | table layout, sticky header, zebra, number alignment | table fixes leaking to core widgets |
| Tasks | callout/list owner plus plugin support when plugin DOM-specific | checkbox, completed/ongoing markers, callout nesting | list spacing drift |
| Canvas | `src/plugins/60-canvas-graph-link-panes.css` | card, edge, toolbar contrast | workspace chrome collision |
| Graph | `src/plugins/60-canvas-graph-link-panes.css` | controls and background contrast | low contrast in dark mode |
| Mermaid | `src/plugins/61-live-preview-mobile-plugin.css` or image/embed owner | SVG/image clipping and overflow | diagram cropping in Live Preview/PDF |
| Bookmarks | chrome/list owner | active/hover row height | runtime list state drift |
| Outline | chrome/list owner | active/hover row, indentation | left rail regression |
| Search | chrome/search owner | focus rim, match highlight, result row | aggressive focus color |

## Rule

A plugin selector can justify plugin-specific support, but it does not transfer ownership of core Reading, Live Preview, table, PDF, or chrome geometry.
