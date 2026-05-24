# Workflow: Live Preview CM6

## Owner

Start with `src/base/13-live-preview.css`.

## Before Editing

- Read `dev/WIKI/MAP/cm6-hit-routing-contract.md`.
- Confirm whether the target is a source line, rendered widget, HTML embed, or Obsidian core widget.

## Avoid

- Vertical margin/padding on hit-routed `.cm-line` variants.
- Active line outlines, transforms, or shadows that affect click routing.
- Styling `.cm-table-widget` geometry.

## Required Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_v3_hit_routing.py
.\.venv\Scripts\python.exe dev\scripts\audit_core_principles.py
```
