# Recipe: Coverage Print PDF Context

## Route

- Owner: `src/features/41-feature-presets.css`, `src/features/42-report-print-polish.css`, or `src/features/43-print-base.css` by PDF surface.
- Contract: `dev/WIKI/MAP/pdf-header-footer-contract.md` and `dev/WIKI/MAP/live-preview-pdf-css-map/parity-guidelines.md` when tables/code/callouts are involved.
- Read: `WORKFLOWS/pdf.md`, `RUNTIME/pdf.md`, and `VISUAL-QA.md`.

## Steps

1. Pick one `print-pdf-context` reserved selector or one PDF visibility/header/footer combination.
2. Capture the screen state and print/PDF state separately; do not assume screen behavior proves print behavior.
3. Check header/footer overlap, page breaks, table/code wrapping, image borders, and compact report variants.
4. Keep report-specific closure in print owners and avoid changing screen selectors unintentionally.
5. Update the unused CSS report only after print evidence exists.

## Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_pdf_header_footer.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```