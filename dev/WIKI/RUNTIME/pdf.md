# Runtime: PDF

Use this for PDF export, print preview, report mode, page labels, page breaks, and PDF-only visibility.

## Surface Split

| Target | Owner | Contract |
| --- | --- | --- |
| PDF header/footer labels | `src/features/41-feature-presets.css` | `MAP/pdf-header-footer-contract.md` |
| Base print page behavior | `src/features/43-print-base.css` | release check |
| Report table/code/callout closure | `src/features/42-report-print-polish.css` | LP/PDF parity map |
| Token color/spacing | `src/tokens/*` | Style Settings/PDF audit when setting-facing |

## Required Capture

- Print media or PDF export path.
- Report mode classes and enabled Style Settings presets.
- Header/footer text, palette, and page position.
- Table/page-break sample if content flow changes.
- Confirmation that screen layout is not affected by print-only changes.

## Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_pdf_header_footer.py
.\.venv\Scripts\python.exe dev\scripts\audit_visual_quality_fixture.py --static-only
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```
