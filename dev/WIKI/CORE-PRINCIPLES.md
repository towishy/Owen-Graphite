# Core Principles

## WIKI First

- Before any code writing, feature improvement, bug fix, cleanup, or review, read `dev/WIKI/README.md`, `dev/WIKI/QUICK-ROUTING.md`, and the relevant workflow.
- Use `dev/WIKI/MAP/source-usage-map.md` and the linked risk contracts to locate ownership before touching source.
- If the WIKI does not explain the surface, update the WIKI or MAP as part of the change instead of relying on memory.

## Direct Owner First

- Identify the source owner before editing.
- Edit the owner module directly.
- Remove or merge conflicting follow-up rules instead of adding another rule later in the cascade.

## Owen Risk Acceptance

- If Owen explicitly instructs the agent to proceed despite a known repository risk, treat that as product-owner risk acceptance.
- Risk acceptance does not authorize silent late repair layers; update the relevant WIKI contract, guard, runtime evidence, and owner notes in the same change.
- Prefer the direct owner even under risk acceptance. If a core boundary changes, change the boundary documentation and audit rule before changing behavior.

## No Late Repair Layer

- Do not use late visual modules as a repair layer.
- `allowed-late` means a documented cascade role, not new ownership.
- Do not reintroduce `src/polish`.

## Obsidian Core Boundaries

- Markdown table widget geometry is core-owned.
- Do not style `.cm-table-widget` or `table.cm-table` geometry unless Owen explicitly accepts the risk and the change updates the contract, evidence, and guard path.
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
