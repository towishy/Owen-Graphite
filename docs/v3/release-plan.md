# v3 Release Record (latest: v3.1.5)

**Status**: Current stable / rollback baseline = `v3.1.5` (2026-05-16). Original v3.0.0 from-scratch rewrite shipped 2026-05-16; superseded by the v3.0.x hotfix chain and the v3.1.x feature/lint chain (file-explorer hover, scanner multicolumn cleanup, H1 sizing across reading/live-preview/print, PDF specificity hardening, build-time dedup, lint warning cleanup, minAppVersion 1.12.0). v2 source/dev/scripts/docs/screenshots remain fully purged.

## What shipped (latest)

| Item | Value |
| --- | --- |
| `manifest.json` version | `3.1.5` |
| `minAppVersion` | `1.6.0` (unchanged) |
| `dist/theme-v3.css` lines / declaration-level `!important` | 16,479 / 0 |
| `theme.css` | sourced verbatim from `dist/theme-v3.css` |
| Live Preview hit-routing audit | clean |
| Duplicate-selector audit | informational only |
| Release ZIP | `dist/Owen-Graphite-3.1.5.zip` |

## What was removed

- `dev/` (v2 source, ~60+ files).
- v2 scripts: `bundle_theme.py`, `validate_theme.py`, `analyze_theme_css.py`, `diff_guard.py`, `who_added.py`, `hit_routing_probe.py`, `visual_regression.py`, `contrast_audit.py`, `generate_screenshots.py`, `build_selector_provenance.py`, `changelog_lint.py`, `find_safe_duplicate_selectors.py`.
- v2 docs: `liquid-glass-migration-checklist.md`, `liquid-glass-token-map.md`, `liquid-glass-core-principles.md`, `liquid-glass-hover-study-sample.html`, `liquid-glass-token-map.md`, `css-important-audit.md`, `style-settings.md`, `qa-checklist.md`, `ai-document-guide.md`, `community-scanner-acknowledgments.md`.
- v2 fixtures: `docs/fixtures/` entire tree.
- v2 release artifacts: `dist/Owen-Graphite-2.30.*.zip`, `dist/theme-v3.no-important.css`.
- v2 screenshots: `screenshots/golden/v2.30.14/` and `screenshots/readme/v2.*.svg`.

## v3 toolchain (canonical)

| Concern | Tool |
| --- | --- |
| Bundle src → dist/theme-v3.css | `dev/scripts/bundle_v3.py` |
| Promote bundle to root `theme.css` | `Copy-Item dist\theme-v3.css theme.css -Force` (Windows) |
| Live Preview hit-routing audit | `dev/scripts/audit_v3_hit_routing.py` |
| Cross-module duplicate selectors | `dev/scripts/v3_audit_duplicate_selectors.py` |
| Computed-style fingerprint | `dev/scripts/capture_computed_fingerprint.py` + `dev/scripts/fp_diff_summary.py` |
| Strip `!important` from src/ | `dev/scripts/v3_strip_important_src.py` (comment-safe) |
| Build release ZIP | `dev/scripts/build_release.py` |
| Sync to Obsidian vault | `dev/scripts/sync_obsidian_theme.py` |
| Pre-commit hook | `dev/scripts/hooks/pre-commit` (bundle + hit-routing) |

## Release procedure for future v3.x.y

1. Edit `src/` only. Never hand-edit `theme.css`.
2. `python dev/scripts/bundle_v3.py` — must end with `OK: bundled ... !important=N` where N is only comment-counts.
3. `python dev/scripts/audit_v3_hit_routing.py` — must be clean.
4. (Optional) re-capture fingerprint to confirm 0 diff against baseline.
5. Bump `manifest.json` version, add `CHANGELOG.md` entry.
6. `python dev/scripts/build_release.py` — emits `dist/Owen-Graphite-<version>.zip`.
7. Commit, tag `<version>` (and optionally `v<version>`), push tag.
8. CI (`.github/workflows/release.yml`) builds the GitHub Release.

## Style Settings + minAppVersion

- 37 Style Settings option names unchanged from v2.30.14 — Style Settings configs migrate without user action.
- Token contract: 255 `--ogd-*` token names preserved.
- `minAppVersion: 1.6.0` unchanged.
