# v3 Release Record (latest: v3.1.58)

**Status**: Current stable / rollback baseline = `v3.1.58` (2026-05-24). Original v3.0.0 from-scratch rewrite shipped 2026-05-16; superseded by the v3.0.x hotfix chain and the v3.1.x feature/lint chain (file-explorer hover and extension type badges, scanner multicolumn cleanup, H1 sizing across reading/live-preview/print, PDF marginalia hardening, build-time dedup, CSS validator cleanup, MAP risk tooling, Key/Value PDF labels, dual PDF header Key/Value pairs, Live Preview/PDF quality parity fixture, codeblock font/color parity, Live Preview/PDF CSS MAP, README feature screenshot, README English community-review summary, PDF document-title hiding, PDF H1 liquid-glass plate polish, Live Preview H1 scale bump, Obsidian vault sync target discovery, direct-owner CSS baseline tooling, unused CSS candidate reporting, minAppVersion 1.12.0, release confidence docs, release-check automation, issue templates, image border polish, Live Preview image embed rim coverage, liquid-glass image shadow polish, settings heading liquid bars, search focus Liquid Aqua rim, README visual tour screenshots, top tab attached liquid-glass polish, connected workspace chrome polish, Live Preview codeblock header editability polish, file-explorer action icon glass polish, transparent root view header tuning, active tab backline cleanup, customer-delivery screen PDF visibility preset, Style Settings import/export glass polish, Validate workflow dependency setup, WIKI-first operational routing, and WIKI workflow automation helpers). v2 source/dev/scripts/docs/screenshots remain fully purged.

## What shipped (latest)

| Item | Value |
| --- | --- |
| `manifest.json` version | `3.1.58` |
| `minAppVersion` | `1.12.0` |
| `dist/theme-v3.css` lines / `!important` scanner count | 18,237 / 5 |
| `theme.css` | sourced verbatim from `dist/theme-v3.css` |
| Live Preview hit-routing audit | clean |
| Duplicate-selector audit | informational only |
| Release ZIP | `dist/Owen-Graphite-3.1.58.zip` |

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
| Local release validation sequence | `dev/scripts/release_check.py` |
| Live Preview hit-routing audit | `dev/scripts/audit_v3_hit_routing.py` |
| Cross-module duplicate selectors | `dev/scripts/v3_audit_duplicate_selectors.py` |
| Computed-style fingerprint | `dev/scripts/capture_computed_fingerprint.py` + `dev/scripts/fp_diff_summary.py` |
| Strip `!important` from src/ | `dev/scripts/v3_strip_important_src.py` (comment-safe) |
| Build release ZIP | `dev/scripts/build_release.py` |
| Build release notes from CHANGELOG | `dev/scripts/build_release_notes.py` |
| Release metadata contract | `dev/scripts/audit_release_metadata.py` |
| Release ZIP install contract | `dev/scripts/audit_release_zip.py` |
| Style Settings contract | `dev/scripts/audit_style_settings_contract.py` |
| Docs/assets link contract | `dev/scripts/audit_docs_assets.py` |
| CSS compatibility/budget guard | `dev/scripts/audit_css_compat_budget.py` |
| Sync to Obsidian vault | `dev/scripts/sync_obsidian_theme.py` |
| Pre-commit hook | `dev/scripts/hooks/pre-commit` (bundle freshness + metadata/style/docs/CSS/PDF/LP audits) |
| CI validation | `.github/workflows/validate.yml` via `dev/scripts/release_check.py` |
| Visual quality smoke check | `dev/scripts/audit_visual_quality_fixture.py` (LP/PDF parity + image/body + code font fixtures; local browser render when available) |
| Direct-owner baseline/source map | `dev/scripts/build_effective_source_map.py` + `dev/scripts/build_effective_baseline.py` |
| Direct-owner Style Settings coverage | `dev/scripts/build_style_settings_matrix.py` |
| Effective/provenance snapshots | `dev/scripts/capture_effective_snapshot.py` + `dev/scripts/capture_provenance_snapshot.py` |
| Owner migration diff gate | `dev/scripts/diff_effective_snapshot.py` |
| Unused CSS candidate report | `dev/scripts/build_unused_css_report.py` |

## Release procedure for future v3.x.y

1. Edit `src/` only. Never hand-edit `theme.css`.
2. `python dev/scripts/bundle_v3.py` — must end with `OK: bundled ... !important=N` where N is only comment-counts.
3. Promote the bundle to `theme.css`.
4. Bump `manifest.json` version, add `CHANGELOG.md` entry, and update README/release-plan references.
5. `python dev/scripts/release_check.py --tag <version>` — runs bundle freshness, release metadata, Style Settings, docs/assets, CSS budget, LP hit-routing, PDF header/footer, and duplicate selector threshold checks.
6. `python dev/scripts/audit_visual_quality_fixture.py --static-only` for LP/PDF parity, image/body, and code font fixture contracts; omit `--static-only` locally to render screenshot/PDF with Chrome or Edge.
7. For direct-owner migrations, refresh effective source/baseline artifacts and confirm provenance maps back to owner modules.
8. Before unused CSS removal, run `python dev/scripts/build_unused_css_report.py`; only `candidate` selectors are eligible for removal, and `reserved` selectors require purpose-built coverage first.
9. `python dev/scripts/build_release_notes.py --output dist/release-notes-<version>.md` — builds release notes from the latest CHANGELOG section.
10. `python dev/scripts/build_release.py` — emits `dist/Owen-Graphite-<version>.zip`.
11. `python dev/scripts/audit_release_zip.py` — verifies the manual-install ZIP contains the expected install tree and fresh `theme.css`.
12. Commit, tag `<version>` using numeric semver only, and push the numeric tag. Do not use a leading `v` prefix in the tag or GitHub Release name.
13. CI (`.github/workflows/release.yml`) validates, builds release notes, builds the ZIP, audits it, and publishes the GitHub Release.

## README Feature Intro Procedure

- `README.md`의 `2. 신기능 소개`에는 최신 3개 신기능만 유지합니다.
- 4번째로 밀린 신기능 소개는 `dev/WIKI/DOCS/v3/feature-history.md`로 옮기고, README의 마지막 신기능 소개 아래에서 해당 문서로 링크합니다.
- 각 신기능 소개는 기능을 보여주는 SVG 이미지와 짧은 소개 중심으로 작성합니다.
- README용 신기능 이미지는 Owen Graphite liquid glass 원칙을 따르고, 한국어 문서에서는 이미지 라벨도 한국어를 기본으로 합니다.

## Style Settings + minAppVersion

- Current v3 Style Settings contract is recorded in `dev/WIKI/DOCS/v3/style-settings-contract.md`.
- Current token inventory is recorded in `dev/WIKI/DOCS/v3/token-inventory.md`.
- `minAppVersion: 1.12.0`.
