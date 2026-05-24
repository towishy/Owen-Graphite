# Workflow: Docs And Assets

## Owners

- README/docs copy: root README files and `dev/WIKI/DOCS/`.
- Docs corpus routing: `dev/WIKI/DOCS/docs-map.md`.
- Generated sample assets: follow user memory preferences and use `dev/temp/` unless publishing is requested.
- README feature intros: keep latest three in README, older entries in `dev/WIKI/DOCS/v3/feature-history.md`.

## Before Editing

- If changing Style Settings documentation, read `dev/WIKI/DOCS/v3/style-settings-contract.md` and `dev/WIKI/DOCS/v3/style-settings-contract.json`.
- If changing visual claims or screenshots, read `dev/WIKI/DOCS/v3/golden-image-scenarios.md` and `dev/WIKI/DOCS/v3/visual-comparison-guide.md`.
- If changing release copy, read `dev/WIKI/DOCS/v3/release-notes-workflow.md` and `dev/WIKI/DOCS/v3/release-plan.md`.
- If changing plugin support text, read `dev/WIKI/DOCS/v3/plugin-compatibility.md`.

## Required Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_docs_assets.py
.\.venv\Scripts\python.exe dev\scripts\audit_readme_svg_layout.py
```
