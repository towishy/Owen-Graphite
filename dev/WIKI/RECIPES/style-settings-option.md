# Recipe: Style Settings Option

## Route

- Owner: `src/features/40-style-settings.css` for metadata.
- Contract: `dev/WIKI/DOCS/v3/style-settings-contract.json` and `.md`.
- Read: `WORKFLOWS/docs-assets.md`, `TOKENS/usage-guide.md` when values are visual.

## Steps

1. Add or change the setting metadata in `40-style-settings.css`.
2. Update the JSON and Markdown contract together.
3. If the setting controls visual behavior, route the actual CSS to the owner module.
4. Update presets/docs if user-facing behavior changes.

## Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_style_settings_contract.py
.\.venv\Scripts\python.exe dev\scripts\audit_docs_assets.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```
