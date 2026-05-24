# Workflow: Release

## Standard Steps

```powershell
.\.venv\Scripts\python.exe dev\scripts\bundle_v3.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
.\.venv\Scripts\python.exe dev\scripts\build_release.py
.\.venv\Scripts\python.exe dev\scripts\audit_release_zip.py
```

## Publish Playbook

Replace `<version>` with numeric semver only, for example `3.1.58`.

```powershell
.\.venv\Scripts\python.exe dev\scripts\bundle_v3.py
Copy-Item dist\theme-v3.css theme.css -Force
.\.venv\Scripts\python.exe dev\scripts\build_source_usage_map.py --check
.\.venv\Scripts\python.exe dev\scripts\audit_core_principles.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --tag <version> --skip-bundle
.\.venv\Scripts\python.exe dev\scripts\build_release.py
.\.venv\Scripts\python.exe dev\scripts\audit_release_zip.py
git status --short
git add -A
git commit -m "chore: release Owen Graphite <version>"
git push origin main
git tag <version>
git push origin <version>
gh run list --workflow Release --limit 1 --json databaseId,status,conclusion,headBranch,url
gh release view <version> --json tagName,name,url,isDraft,isPrerelease
```

Never run `git tag v<version>` and never publish a `v<version>` GitHub Release.

## Before Publishing

- Confirm `manifest.json` version.
- Use numeric semver tags and GitHub Release names only, for example `3.1.57`; never use a leading `v` prefix.
- Confirm `theme.css` matches `dist/theme-v3.css`.
- Confirm source usage map is fresh.
- Confirm core principles gate passes.
