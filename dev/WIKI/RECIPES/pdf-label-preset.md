# Recipe: PDF Labels And Presets

## Route

- Owner: `src/features/41-feature-presets.css` for PDF marginalia and presets.
- Related: `src/features/42-report-print-polish.css` and `43-print-base.css` for print/report closure.
- Read: `WORKFLOWS/pdf.md`, `MAP/pdf-header-footer-contract.md`, `RUNTIME/pdf.md`.

## Steps

1. Identify whether the change is setting metadata, preset class, label layout, or print body behavior.
2. Keep header/footer owner rules in `41-feature-presets.css`.
3. Update Style Settings contract if ids/defaults/options change.
4. Verify screen and print scopes remain separate.

## Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_style_settings_contract.py
.\.venv\Scripts\python.exe dev\scripts\audit_pdf_header_footer.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```
