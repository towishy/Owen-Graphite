# Incident: Table Row Inflation

## Symptom

Selecting a table cell caused the row to grow unexpectedly.

## Wrong Approach

- Repeated selector guesses.
- Late or high-specificity geometry resets.
- Confusing rendered tables, Live Preview HTML tables, and markdown table widgets.

## Correct Process

1. Identify whether the table is rendered, LP HTML embed, or LP markdown widget.
2. Capture runtime DOM/computed style for the selected cell.
3. Map matched theme rule back through `effective-source-map.json`.
4. Edit the owner only.
5. Run core gates and verify the same runtime state.

## Prevention

- `source-usage-map.md` Table Selector Rules.
- Runtime debug snippets.
- `audit_core_principles.py`.

## Risk-Accepted Exception

On 2026-05-25, Owen explicitly accepted the risk of styling `.cm-table-widget table.table-editor` to match Live Preview HTML table visibility. This exception requires the `owen-risk-accepted: cm-table-widget` marker, before/after runtime evidence, and direct-owner/hit-routing audits. Keep future widget changes narrow and evidence-backed.
