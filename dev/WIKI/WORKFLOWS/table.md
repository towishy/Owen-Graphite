# Workflow: Table Changes

## First Decision

- Rendered/Reading table: edit `src/surfaces/20-reading-tables-code.css`.
- PDF/report table: edit `src/features/42-report-print-polish.css` only in print/report scope.
- Live Preview HTML table: edit `src/base/13-live-preview.css` or `src/surfaces/24-html-table-live-preview-glass.css`.
- Markdown table widget: core-owned; do not style geometry.

## Required Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_direct_owner_guard.py
.\.venv\Scripts\python.exe dev\scripts\audit_lp_pdf_selector_ownership.py
.\.venv\Scripts\python.exe dev\scripts\audit_v3_hit_routing.py
```

## Selector Rules

Allowed LP HTML table selector shape:

```css
.markdown-source-view.mod-cm6 ... table:not(.cm-table):not(.cm-table-widget)
```

Forbidden:

```css
.markdown-source-view.mod-cm6 .cm-table-widget ...
.markdown-source-view.mod-cm6 table.cm-table ...
.HyperMD-table-row ... td
```

## Runtime Issues

If selected-cell or hover behavior changes row height, run `DEV/runtime-debug.md` before editing.
