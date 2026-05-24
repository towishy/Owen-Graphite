# Recipe: Coverage State Interaction

## Route

- Owner: the surface owner returned by `dev/scripts/wiki_route.py <surface>`.
- Contract: use the relevant `dev/WIKI/MAP/*-contract.md`; for chrome, use `top-chrome-icon-background-contract.md` when top chrome is involved.
- Read: `runtime-evidence-template.md`, `runtime-evidence-example-selected-tab.md`, and the relevant `RUNTIME/` surface guide.

## Steps

1. Pick one reserved selector bucketed as `state-interaction` in `dev/WIKI/MAP/unused-css-candidates.md`.
2. Capture resting and hovered/focused/active/selected states with DOM chain, rects, computed geometry, matched rules, and inline style check.
3. Confirm the owner module from the matched theme rule before editing or deleting anything.
4. Update the fixture or runtime evidence note before changing selector status.
5. Remove CSS only when the evidence proves the selector is unused in the real runtime state.

## Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_runtime_evidence_requirements.py --strict
.\.venv\Scripts\python.exe dev\scripts\audit_core_principles.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```