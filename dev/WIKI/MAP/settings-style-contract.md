# Risk Contract: Settings And Style Settings

Applies to Obsidian settings controls and Style Settings metadata.

## Owners

- Obsidian settings panes, setting rows, toggles, sliders, dropdowns, and settings search presentation: `src/chrome/33-settings-controls.css`.
- Style Settings metadata, ids, defaults, options, and user-facing compatibility: `src/features/40-style-settings.css` and `dev/WIKI/DOCS/v3/style-settings-contract.json`.

## Boundaries

- Do not put setting control presentation in overlay or workspace chrome owners unless the selector belongs to those surfaces.
- A setting option is not complete until CSS metadata, the contract JSON, and docs agree.
- Use tokens for repeated setting UI colors, spacing, and focus states instead of local literals.

## Evidence

- For settings UI changes, capture the setting pane state and any focused/hovered control involved.
- For Style Settings changes, record the setting id, default, option values, and generated body class.

## Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_style_settings_contract.py
.\.venv\Scripts\python.exe dev\scripts\audit_core_principles.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```