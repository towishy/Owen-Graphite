# Workflow: Release

## Standard Steps

```powershell
.\.venv\Scripts\python.exe dev\scripts\bundle_v3.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
.\.venv\Scripts\python.exe dev\scripts\build_release.py
.\.venv\Scripts\python.exe dev\scripts\audit_release_zip.py
.\.venv\Scripts\python.exe compat\owen-graphite-style-settings-l10n\test.py
.\.venv\Scripts\python.exe dev\scripts\build_companion_release.py
```

For a scripted dry run of the publish playbook, use:

```powershell
.\.venv\Scripts\python.exe dev\scripts\release_publish.py --version <version>
```

Add `--publish` only after the version metadata is final and the dry run is clean.

## Publish Playbook

Replace `<version>` with numeric semver only, for example `3.1.58`.

```powershell
.\.venv\Scripts\python.exe dev\scripts\bundle_v3.py
Copy-Item dist\theme-v3.css theme.css -Force
.\.venv\Scripts\python.exe dev\scripts\release_preflight.py --version <version>
.\.venv\Scripts\python.exe dev\scripts\build_source_usage_map.py --check
.\.venv\Scripts\python.exe dev\scripts\audit_core_principles.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --tag <version> --skip-bundle
.\.venv\Scripts\python.exe dev\scripts\build_release.py
.\.venv\Scripts\python.exe dev\scripts\audit_release_zip.py
.\.venv\Scripts\python.exe compat\owen-graphite-style-settings-l10n\test.py
.\.venv\Scripts\python.exe dev\scripts\build_companion_release.py
git status --short
git add -A
git commit -m "chore: release Owen Graphite <version>"
git push origin main
git tag <version>
git push origin <version>
gh run list --workflow Release --limit 1 --json databaseId,status,conclusion,headBranch,url
gh release view <version> --json tagName,name,url,isDraft,isPrerelease
.\.venv\Scripts\python.exe dev\scripts\check_release_status.py --version <version> --wait --require-complete
```

Never run `git tag v<version>` and never publish a `v<version>` GitHub Release.

## Before Publishing

- Install the pinned build dependencies from `requirements.txt`. Release CSS uses
  RCSSmin for syntax-only compression: declaration order and values are not
  optimized or reordered. Style Settings comments and source-module boundaries
  are preserved; `src/` stays readable.
- Bundle output always uses LF on Windows and CI. Freshness checks compare
  bytes so a line-ending conversion cannot silently change the release asset.
- For a readable diagnostic copy, run `bundle_v3.py --readable --out
  dev/TEMP/theme-readable.css`. Do not promote that copy as a release artifact.
- Compact bundle provenance maps to the owning module, not an invented original
  source line. `capture_provenance_snapshot.py` reports `module_line: null` for
  compact output; inspect the matched selector in the readable owner module.
- Warning reduction must preserve rendering, metadata and the minimum app
  version. Broad partial-support advisories and required relational selectors
  are not suppressed just to obtain a zero-warning report.
- An installed Edge can run optional visual checks without a browser download:
  `release_check.py --include-visual --browser-channel msedge`.

- Confirm `manifest.json` version.
- Run `dev/scripts/release_preflight.py --version <version>` before tagging.
- Use numeric semver tags and GitHub Release names only, for example `3.1.57`; never use a leading `v` prefix.
- Confirm `theme.css` matches `dist/theme-v3.css`.
- Confirm source usage map is fresh.
- Confirm core principles gate passes.
