# Recipe: Top Chrome Active / Hover State

## Route

- Owners: `src/chrome/34-nav-ribbon-glass.css`, `src/chrome/37-tabs-file-explorer-search.css`, and related chrome owners.
- Read: `WORKFLOWS/chrome-ui.md`, `MAP/top-chrome-icon-background-contract.md`, `RUNTIME/chrome.md`.
- Avoid: fixing top chrome from overlay modules.

## Steps

1. Identify tab, ribbon, explorer, search, or toolbar surface.
2. Capture hover/focus/active runtime state before changing CSS.
3. Edit the owner module directly.
4. Keep resting state quiet; reserve shallow color for active/hover.

## Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_core_principles.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```
