# Core Principles

## WIKI First

- Before any code writing, feature improvement, bug fix, cleanup, or review, read `dev/WIKI/README.md`, `dev/WIKI/QUICK-ROUTING.md`, and the relevant workflow.
- Use `dev/WIKI/MAP/source-usage-map.md` and the linked risk contracts to locate ownership before touching source.
- If the WIKI does not explain the surface, update the WIKI or MAP as part of the change instead of relying on memory.

## Direct Owner First

- Identify the source owner before editing.
- Edit the owner module directly.
- Remove or merge conflicting follow-up rules instead of adding another rule later in the cascade.

## No Late Repair Layer

- Do not use late visual modules as a repair layer.
- `allowed-late` means a documented cascade role, not new ownership.
- Do not reintroduce `src/polish`.

## Obsidian Core Boundaries

- Markdown table widget geometry is core-owned.
- Do not style `.cm-table-widget` or `table.cm-table` geometry.
- Do not route table fixes through `.HyperMD-table-row` descendants.

## Evidence Before Runtime Fixes

- For selected, focused, hovered, or active state bugs, collect runtime DOM/computed evidence first.
- If inline style is responsible, do not assume ordinary CSS can fix it.
- Verify with the same runtime state after editing.

## Required Gates

Run these before commit:

```powershell
.\.venv\Scripts\python.exe dev\scripts\build_source_usage_map.py --check
.\.venv\Scripts\python.exe dev\scripts\audit_core_principles.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```
