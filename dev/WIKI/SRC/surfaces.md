# SRC: Surfaces

- `src/surfaces/20-reading-tables-code.css`: rendered tables and code primitives.
- `src/surfaces/21-reading-callouts-lists.css`: callouts, blockquotes, lists.
- `src/surfaces/22-reading-embeds-workspace.css`: embeds and workspace support surfaces.
- `src/surfaces/23-liquid-glass-core.css`: late visual glass surface for allowed rendered/non-core surfaces.
- `src/surfaces/24-html-table-live-preview-glass.css`: Live Preview HTML table embeds only.

Do not use surfaces as a catch-all repair layer.

Minimum checks: `SRC/validation-matrix.md`, `audit_direct_owner_guard.py`, `audit_lp_pdf_selector_ownership.py`, `release_check.py --skip-bundle`.
