# v3 Release Record (latest: v3.1.39)

**Status**: Current stable / rollback baseline = `v3.1.39` (2026-05-17). Original v3.0.0 from-scratch rewrite shipped 2026-05-16; superseded by the v3.0.x hotfix chain and the v3.1.x feature/lint chain (file-explorer hover, scanner multicolumn cleanup, H1 sizing across reading/live-preview/print, PDF marginalia hardening, build-time dedup, CSS validator cleanup, MAP risk tooling, Key/Value PDF labels, dual PDF header Key/Value pairs, Live Preview/PDF quality parity fixture, codeblock font/color parity, Live Preview/PDF CSS MAP, README feature screenshot, minAppVersion 1.12.0). v2 source/dev/scripts/docs/screenshots remain fully purged.

## What shipped (latest)

| Item | Value |
| --- | --- |
| `manifest.json` version | `3.1.39` |
| `minAppVersion` | `1.12.0` |
| `dist/theme-v3.css` lines / `!important` scanner count | 17,316 / 7 |
| `theme.css` | sourced verbatim from `dist/theme-v3.css` |
| Live Preview hit-routing audit | clean |
| Duplicate-selector audit | informational only |
| Release ZIP | `dist/Owen-Graphite-3.1.39.zip` |

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
| Release metadata contract | `dev/scripts/audit_release_metadata.py` |
| Release ZIP install contract | `dev/scripts/audit_release_zip.py` |
| Style Settings contract | `dev/scripts/audit_style_settings_contract.py` |
| Docs/assets link contract | `dev/scripts/audit_docs_assets.py` |
| CSS compatibility/budget guard | `dev/scripts/audit_css_compat_budget.py` |
| Sync to Obsidian vault | `dev/scripts/sync_obsidian_theme.py` |
| Pre-commit hook | `dev/scripts/hooks/pre-commit` (bundle freshness + metadata/style/docs/CSS/PDF/LP audits) |
| CI validation | `.github/workflows/validate.yml` (fresh bundle + `theme.css` freshness + metadata/style/docs/CSS/PDF/LP audits) |
| Visual quality smoke check | `dev/scripts/audit_visual_quality_fixture.py` (LP/PDF parity + image/body + code font fixtures; local browser render when available) |

## Release procedure for future v3.x.y

1. Edit `src/` only. Never hand-edit `theme.css`.
2. `python dev/scripts/bundle_v3.py` — must end with `OK: bundled ... !important=N` where N is only comment-counts.
3. Verify `theme.css` is the promoted copy of `dist/theme-v3.css` before commit.
4. `python dev/scripts/audit_release_metadata.py` — version references must agree across manifest, README, changelog, screenshots docs, and release-plan.
5. `python dev/scripts/audit_style_settings_contract.py` — Style Settings CSS metadata must match `docs/v3/style-settings-contract.json`.
6. `python dev/scripts/audit_docs_assets.py` — local Markdown links and README image assets must resolve.
7. `python dev/scripts/audit_css_compat_budget.py` — unlayered/zero-important contract, bundle budget, and known browser-compat exceptions must hold.
8. `python dev/scripts/audit_v3_hit_routing.py` — must be clean.
9. `python dev/scripts/audit_pdf_header_footer.py` — must be clean after any print/report/PDF settings change.
10. `python dev/scripts/build_src_map.py` — refreshes the MAP baseline.
11. (Optional) re-capture fingerprint to confirm 0 diff against baseline.
12. Bump `manifest.json` version, add `CHANGELOG.md` entry.
13. `python dev/scripts/audit_visual_quality_fixture.py --static-only` for LP/PDF parity, image/body, and code font fixture contracts; omit `--static-only` locally to render screenshot/PDF with Chrome or Edge.
14. `python dev/scripts/build_release.py` — emits `dist/Owen-Graphite-<version>.zip`.
15. `python dev/scripts/audit_release_zip.py` — verifies the manual-install ZIP contains the expected install tree and fresh `theme.css`.
16. Commit, tag `<version>` (and optionally `v<version>`), push tag.
17. CI (`.github/workflows/release.yml`) builds the GitHub Release.

## Style Settings + minAppVersion

- Current v3 Style Settings contract is recorded in `docs/v3/style-settings-contract.md`.
- Current token inventory is recorded in `docs/v3/token-inventory.md`.
- `minAppVersion: 1.12.0`.
