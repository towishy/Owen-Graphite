# Runtime: PDF

Use this for PDF export, print preview, report mode, page labels, page breaks, and PDF-only visibility.

## Surface Split

| Target | Owner | Contract |
| --- | --- | --- |
| PDF header/footer labels | `src/features/41-feature-presets.css` | `MAP/pdf-header-footer-contract.md` |
| Base print page behavior | `src/features/43-print-base.css` | release check |
| PDF heading templates | `src/features/43-print-base.css` | 9-template computed audit and rendered PDF/PNG set |
| Report table/code/callout closure | `src/features/42-report-print-polish.css` | LP/PDF parity map |
| Token color/spacing | `src/tokens/*` | Style Settings/PDF audit when setting-facing |

## Required Capture

- Print media or PDF export path.
- Report mode classes and enabled Style Settings presets.
- Header/footer text, palette, and page position.
- Table/page-break sample if content flow changes.
- Confirmation that screen layout is not affected by print-only changes.
- For heading-template changes, all nine `ogd-heading-*` classes rendered from `dev/WIKI/DOCS/v3/research/pdf-heading-template-fixture.html`.

## Heading Template Contract

- H1-H4 must preserve descending typography, remain visible, and fit the print width without horizontal overflow.
- H1/H2 must not use shadows or backdrop filters in print.
- A heading with an accent line or frame must use square geometry. Rounded corner plus accent line/frame combinations are forbidden.
- The fixture metadata label and date must remain separated and aligned to opposite edges.
- `--render` writes one PDF, one PNG preview, and `manifest.json` per template under `dev/temp/pdf-heading-templates/`.

## Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_pdf_header_footer.py
.\.venv\Scripts\python.exe dev\scripts\audit_pdf_heading_templates.py --render
.\.venv\Scripts\python.exe dev\scripts\audit_visual_quality_fixture.py --static-only
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```
