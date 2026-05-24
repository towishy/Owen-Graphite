# Recipe: Coverage Document Content Fixture

## Route

- Owner: `src/base/12-reading-content.css`, `src/surfaces/20-reading-tables-code.css`, or `src/surfaces/21-reading-callouts-lists.css` by rendered content surface.
- Contract: `dev/WIKI/MAP/reading-content-contract.md` and `dev/WIKI/MAP/live-preview-pdf-css-map/parity-guidelines.md` for table/code/callout parity.
- Read: `WORKFLOWS/table.md`, `SRC/base.md`, and `SRC/surfaces.md`.

## Steps

1. Pick one `document-content-fixture-gap` selector from `dev/WIKI/MAP/unused-css-candidates.md`.
2. Add or identify a natural Markdown fixture that includes the real document structure, not synthetic selector-only DOM.
3. Cover long paragraphs, nested lists, callouts, task items, embeds, Mermaid output, HTML tables, and neighboring code/table blocks when relevant.
4. Confirm the selector still belongs to the rendered content owner and does not affect Live Preview widget geometry.
5. Rebuild the unused CSS report; delete CSS only when the selector becomes a true low-risk candidate.

## Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\build_unused_css_report.py
.\.venv\Scripts\python.exe dev\scripts\audit_core_principles.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```