# Workflow: Release

## Steps

```powershell
.\.venv\Scripts\python.exe dev\scripts\bundle_v3.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
.\.venv\Scripts\python.exe dev\scripts\build_release.py
.\.venv\Scripts\python.exe dev\scripts\audit_release_zip.py
```

## Before Publishing

- Confirm `manifest.json` version.
- Confirm `theme.css` matches `dist/theme-v3.css`.
- Confirm source usage map is fresh.
- Confirm core principles gate passes.
