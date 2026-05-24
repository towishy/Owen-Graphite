# Quick Routing

| Work Area | Start Here | Read Also | Never Do |
| --- | --- | --- | --- |
| Reading typography/headings/links | `src/base/12-reading-content.css` | `SRC/base.md` | Patch from late visual modules |
| Reading/rendered tables | `src/surfaces/20-reading-tables-code.css` | `WORKFLOWS/table.md` | Mix with `.cm-table-widget` |
| Live Preview CM6 line geometry | `src/base/13-live-preview.css` | `WORKFLOWS/live-preview-cm6.md` | Add vertical hitbox changes blindly |
| LP HTML table embed | `src/base/13-live-preview.css`, `src/surfaces/24-html-table-live-preview-glass.css` | `WORKFLOWS/table.md` | Omit `:not(.cm-table-widget):not(.cm-table)` |
| Markdown table widget | Obsidian core | `INCIDENTS/table-row-inflation.md` | Theme geometry styling |
| PDF header/footer | `src/features/41-feature-presets.css` | `WORKFLOWS/pdf.md` | Put owner rules in `42-report-print-polish` |
| PDF/report tables/code | `src/features/42-report-print-polish.css` | `MAP/risk-contracts.md` | Affect screen unintentionally |
| Workspace chrome | `src/chrome/30`, `31`, `34`, `37` | `WORKFLOWS/chrome-ui.md` | Fix from overlay modules |
| Overlay/menu/search | `src/chrome/32`, `35`, `36` | `SRC/chrome.md` | Treat as workspace chrome owner |
| Settings UI controls | `src/chrome/33-settings-controls.css` | `MAP/settings-style-contract.md`, `RECIPES/style-settings-option.md` | Put settings control rules in overlay owners |
| Style Settings metadata | `src/features/40-style-settings.css`, `dev/WIKI/DOCS/v3/style-settings-contract.json` | `MAP/settings-style-contract.md` | Change metadata without updating contract docs |
| Release | `dev/scripts/build_release.py` | `WORKFLOWS/release.md` | Release without gates |

If the owner is still unclear, use `OWNER-DECISION-TREE.md` before searching or editing source.
