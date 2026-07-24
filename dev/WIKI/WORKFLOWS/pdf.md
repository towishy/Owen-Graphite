# Workflow: PDF And Report Output

## Owners

- PDF base: `src/features/43-print-base.css`.
- PDF marginalia header/footer: `src/features/41-feature-presets.css` and token files.
- Report/PDF polish: `src/features/42-report-print-polish.css`.

## Contracts

- `dev/WIKI/MAP/pdf-header-footer-contract.md`
- `dev/WIKI/MAP/live-preview-pdf-css-map/parity-guidelines.md`

## Avoid

- Header/footer owner selectors outside `41-feature-presets.css`.
- Screen-wide side effects from print-only fixes.
- Table changes that bypass `20-reading-tables-code.css` owner without print/report reason.
- Rounded corners on heading surfaces that also carry an accent line or frame.

## Required Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_pdf_header_footer.py
.\.venv\Scripts\python.exe dev\scripts\audit_pdf_heading_templates.py --render
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```
