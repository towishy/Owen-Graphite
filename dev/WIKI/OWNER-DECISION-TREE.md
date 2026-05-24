# Owner Decision Tree

Use this when `QUICK-ROUTING.md` is not enough. Stop at the first true statement, then read the listed workflow and risk contract before editing.

## Decision Tree

1. Is the target a published release, version, ZIP, or GitHub Release?
   - Owner: release workflow and metadata files.
   - Read: `WORKFLOWS/release.md`, `DOCS/v3/release-plan.md`.
   - Gate: `release_check.py --tag <version>` and numeric semver tag only.

2. Is the target a selected, hovered, focused, active, or runtime-only state?
   - Owner: unknown until runtime evidence maps the matched rule.
   - Read: `runtime-evidence-template.md`, `runtime-debug.md`.
   - Gate: capture DOM/computed evidence before changing CSS.

3. Is the target `.cm-table-widget`, `table.cm-table`, or a markdown table cell editor?
   - Owner: Obsidian core for widget geometry.
   - Read: `WORKFLOWS/table.md`, `INCIDENTS/table-row-inflation.md`, `MAP/cm6-hit-routing-contract.md`.
   - Gate: do not theme widget geometry.

4. Is the target an HTML table embed in Live Preview?
   - Owner: `src/base/13-live-preview.css` and `src/surfaces/24-html-table-live-preview-glass.css`.
   - Read: `WORKFLOWS/table.md`.
   - Gate: selectors must exclude `.cm-table-widget` and `table.cm-table`.

5. Is the target a rendered Reading View table, code block, callout, list, or embed?
   - Owner: `src/surfaces/*` according to `SRC/surfaces.md`.
   - Read: `SRC/validation-matrix.md`.
   - Gate: table/code/callout checks plus owner guard.

6. Is the target PDF/report output, page labels, or print behavior?
   - Owner: `src/features/41-feature-presets.css`, `42-report-print-polish.css`, or `43-print-base.css` according to surface.
   - Read: `WORKFLOWS/pdf.md`, `MAP/pdf-header-footer-contract.md`.
   - Gate: PDF header/footer contract and release check.

7. Is the target tabs, ribbon, explorer, search, menu, tooltip, modal, or settings chrome?
   - Owner: `src/chrome/*` according to `SRC/chrome.md`.
   - Read: `WORKFLOWS/chrome-ui.md`, `MAP/top-chrome-icon-background-contract.md` when top chrome is involved.
   - Gate: screenshot/runtime evidence for interactive states.

8. Is the target a Style Settings id, title, default, preset, or contract?
   - Owner: `src/features/40-style-settings.css` plus `DOCS/v3/style-settings-contract.json`.
   - Read: `WORKFLOWS/docs-assets.md`, `DOCS/docs-map.md`.
   - Gate: Style Settings contract audit.

9. If none of the above fits:
   - Search `MAP/source-usage-map.md`, `MAP/owner-registry.json`, `SELECTOR-OWNER-CHEATSHEET.md`, and `SRC/validation-matrix.md`.
   - If ownership is still unclear, update WIKI/MAP before changing source.
