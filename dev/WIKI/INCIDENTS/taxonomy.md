# Incident Taxonomy

Use this to decide when a bug or mistake deserves an incident entry.

| Incident Type | Trigger | Required Evidence | Typical Follow-Up |
| --- | --- | --- | --- |
| `runtime-selected-state` | selected/active/focused state changes layout or style unexpectedly | runtime evidence template, matched rules | update `RUNTIME/*` and owner route |
| `live-preview-hit-routing` | cursor, click, or edit route is blocked in CM6 | DOM chain, hit-routing audit, contract check | update `WORKFLOWS/live-preview-cm6.md` or contract |
| `table-widget-boundary` | markdown table widget is styled as theme table | DOM confirms `.cm-table-widget` or `table.cm-table` | update table workflow and selector cheatsheet |
| `owen-risk-accepted` | Owen explicitly chooses to proceed despite a known repo risk | runtime evidence, changed guard/contract, exact owner diff | keep the exception narrow and document why the risk was accepted |
| `pdf-layout-drift` | PDF header/footer/page/body layout changes unexpectedly | PDF fixture/export evidence | update PDF workflow or print owner docs |
| `plugin-dom-mismatch` | plugin selector behaves differently from fixture | real plugin DOM notes | update `PLUGINS/runtime-dom-notes.md` |
| `token-misuse` | literal values or one-off effects bypass tokens | source diff and visual target | update `TOKENS/*` or owner module |
| `late-repair-layer` | fix lands in late/allowed-late module instead of owner | owner map and cascade relation | update owner docs and remove repair layer |
| `release-process` | tag, release name, asset, or metadata mismatch | command output and release workflow | update release playbook/audit |

## Rule

If the same mistake could recur, create an incident or update an existing one before the work is considered complete.
