# Recipe: Live Preview Spacing / Hit Routing

## Route

- Owner: `src/base/13-live-preview.css`.
- Read: `WORKFLOWS/live-preview-cm6.md`, `MAP/cm6-hit-routing-contract.md`.
- Avoid: vertical margin/padding changes on hit-routed CM6 lines without evidence.

## Steps

1. Determine whether the target is `.cm-line`, `.HyperMD-*`, widget, or embed.
2. If selected/focused/active, fill `runtime-evidence-template.md` first.
3. Keep geometry inside the owner module.
4. For markdown table widgets, stop and read `RUNTIME/table.md`.

## Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_v3_hit_routing.py
.\.venv\Scripts\python.exe dev\scripts\audit_core_principles.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```
