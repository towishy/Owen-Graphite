# Owen Graphite Copilot Instructions

Before any code writing, feature improvement, bug fix, cleanup, or review in this repository, consult `dev/WIKI` first.

Required entrypoints:

1. `dev/WIKI/README.md`
2. `dev/WIKI/CORE-PRINCIPLES.md`
3. `dev/WIKI/QUICK-ROUTING.md`
4. The relevant file under `dev/WIKI/WORKFLOWS/`
5. `dev/WIKI/MAP/source-usage-map.md` or the relevant risk contract when touching CSS ownership, cascade, Live Preview, PDF, tables, or chrome

Hard rules:

- Identify the owner before editing source.
- Edit the owner module directly; do not add late repair layers.
- Do not recreate `dev/MAP`, `dev/LLM-WIKI`, `dev/effective-baseline`, `dev/WIKI/DEV`, or `docs/v3`.
- Do not style Obsidian-owned markdown table widget geometry (`.cm-table-widget` or `table.cm-table`).
- For runtime states such as selected, hovered, focused, or active UI, collect runtime evidence before changing CSS.

Required validation for code changes:

```powershell
.\.venv\Scripts\python.exe dev\scripts\build_source_usage_map.py --check
.\.venv\Scripts\python.exe dev\scripts\audit_core_principles.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```
