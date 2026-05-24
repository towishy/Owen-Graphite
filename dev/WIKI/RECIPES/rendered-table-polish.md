# Recipe: Rendered Table Polish

## Route

- Owner: `src/surfaces/20-reading-tables-code.css`.
- Read: `WORKFLOWS/table.md`, `SELECTOR-OWNER-CHEATSHEET.md`.
- Avoid: mixing rendered table selectors with `.cm-table-widget` or `table.cm-table`.

## Steps

1. Confirm the table is Reading/rendered, not LP markdown widget.
2. Edit rendered table owner.
3. Keep report/PDF closure in `src/features/42-report-print-polish.css` only when print/report scoped.
4. If selection or edit state is involved, use `RUNTIME/table.md`.

## Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_direct_owner_guard.py
.\.venv\Scripts\python.exe dev\scripts\audit_lp_pdf_selector_ownership.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```
