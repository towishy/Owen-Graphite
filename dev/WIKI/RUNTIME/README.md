# Runtime Evidence Library

Use these notes when static audits pass but the user-visible state is still wrong. Start with `runtime-evidence-template.md`, then open the surface-specific note below.

| Surface | File | Use When |
| --- | --- | --- |
| Tables and cell editors | `table.md` | selected cells, row height, LP table widget, HTML table embeds |
| Chrome and workspace UI | `chrome.md` | tabs, ribbon, explorer, search, hover/focus/active states |
| PDF and print | `pdf.md` | PDF labels, page breaks, print-only layout |
| Plugins | `plugins.md` | Dataview, Tasks, Canvas, Graph, Mermaid, plugin DOM |

Runtime evidence is required before CSS changes for selected, hovered, focused, active, editing, collapsed, expanded, plugin-generated, or inline-style states.
