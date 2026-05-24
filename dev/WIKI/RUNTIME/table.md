# Runtime: Tables

Use this for table row height, selected cells, nested editors, and LP/Reading/PDF parity.

## First Split The Surface

| Runtime DOM | Owner Route | Rule |
| --- | --- | --- |
| `.cm-table-widget`, `table.cm-table` | Obsidian core | Do not style theme geometry. |
| LP HTML embed table | `src/base/13-live-preview.css`, `src/surfaces/24-html-table-live-preview-glass.css` | Must exclude `.cm-table-widget` and `.cm-table`. |
| Rendered Reading table | `src/surfaces/20-reading-tables-code.css` | Keep rendered table owner. |
| Report/PDF table | `src/features/42-report-print-polish.css` | Print/report scope only. |

## Required Capture

1. Run `runtime-debug-snippets/table-cell-dump.js`.
2. Run `runtime-debug-snippets/matched-rules-dump.js`.
3. Record whether inline `style` sets width/height/min-height.
4. Map matched theme selectors to `SELECTOR-OWNER-CHEATSHEET.md`.
5. If the path is `.cm-table-widget`, stop before adding CSS.

## Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_direct_owner_guard.py
.\.venv\Scripts\python.exe dev\scripts\audit_v3_hit_routing.py
.\.venv\Scripts\python.exe dev\scripts\audit_lp_pdf_selector_ownership.py
```
