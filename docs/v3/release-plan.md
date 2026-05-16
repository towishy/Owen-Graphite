# v3.0.0 Release Plan

**Status**: Drafted 2026-05-16 after S11.5–S11.8 completion. Requires user
sign-off before any of the destructive steps run.

## Where we stand right now

| Item | State |
| --- | --- |
| `v3-rewrite` branch head | `0da19ec` (origin/v3-rewrite up to date) |
| `src/` declaration-level `!important` | 0 |
| `dist/theme-v3.css` lines / `!important` (declaration) | 16,509 / 0 |
| Computed fingerprint diff vs v2.30.14 (light / dark) | 0 / 0 |
| Hit-routing audit | clean |
| `scripts/validate_theme.py` (v2 invariants) | pass |
| Duplicate-selector audit (`scripts/v3_audit_duplicate_selectors.py`) | 1 safe in-file dup, intentional |
| User vault verification (hover / focus / plugin / canvas) | confirmed 2026-05-16 |
| Spec-defined Non-Goals respected (no new design, no new features, 37 Style Settings names unchanged, minAppVersion 1.6 unchanged) | yes |

## Open questions for the user (before any release step runs)

1. **Version number**: `3.0.0` (jump per `docs/v3/design-spec.md` line 173-174) vs `3.0.0-beta.0` (one round of public beta first)?
2. **`theme.css` replacement**: Obsidian themes must ship as `theme.css` at the
   repo root. The v3 release requires overwriting the current `theme.css`
   (v2.30.14) with the v3 bundle (`dist/theme-v3.css`). Confirm we are
   willing to do this on the `v3-rewrite` branch before merging to `main`.
3. **Source layout going forward**: keep `dev/` archived in the repo for
   history, or move it to a separate branch / git-archive? `src/` is now the
   authoritative source for v3.
4. **Pre-release tag vs draft release**: cut `v3.0.0` tag immediately on
   merge, or push a `v3.0.0-rc.0` tag first for the community theme PR?
5. **Changelog / release notes** to ship: Korean + English, or Korean only?
   Final phrasing of the headline ("Zero !important, identical pixels")?

## Proposed release sequence (each step gated by the next answer above)

### Step R0 — finalize the v3 build (no destructive action)

1. Re-run the full verification suite on `v3-rewrite` HEAD:
   - `scripts/bundle_v3.py` -> bundle clean
   - `scripts/capture_computed_fingerprint.py --build v3 --theme both`
   - `scripts/fp_diff_summary.py` (light + dark, expect 0 diffs)
   - `scripts/audit_v3_hit_routing.py`
   - `scripts/validate_theme.py` (v2 invariants)
2. Commit any drift the suite catches.

### Step R1 — promote the v3 bundle to `theme.css` on `v3-rewrite`

1. `Copy-Item dist\theme-v3.css theme.css -Force`
2. Bump `manifest.json` version to the answer of question 1
   (`3.0.0` or `3.0.0-beta.0`).
3. Re-run `scripts/validate_theme.py` — note: this will now validate the
   v3-derived `theme.css`. v2.30.14 invariants that referenced v2-specific
   guards may need to be re-evaluated; expect to update the script in this
   step so it owns the v3 invariants from R1 onward.
4. Update `CHANGELOG.md` with the v3.0 headline release notes (drafted in
   step R5 below).
5. Commit with message `v3 [R1] promote dist/theme-v3.css to theme.css for
   v3.0 release`.

### Step R2 — community scanner check

Per `docs/v3/design-spec.md` S11 deliverable. There is no local scanner
binary; the check runs server-side on theme PR submission. We pre-empt it
by running our local audits (already clean) and by reviewing
`docs/community-scanner-acknowledgments.md`, which now distinguishes the
v3 zero-`!important` state from the v2.30.x history.

If the user wants a manual local audit pass:

- `scripts/v3_audit_duplicate_selectors.py` (already clean)
- `scripts/analyze_theme_css.py` (existing v2 audit, useful sanity)
- `scripts/contrast_audit.py` (a11y contrast check)

### Step R3 — golden image regeneration (optional, per spec line 173)

`docs/v3/golden-image-scenarios.md` defines 66 visual scenarios.
Regenerate them against the new `theme.css` and diff to confirm zero
visual delta. If `scripts/generate_screenshots.py` is the regeneration
entry point, run it. Skip if the user trusts the harness fingerprint =
0 result.

### Step R4 — merge `v3-rewrite` to `main`

1. `git checkout main`
2. `git merge --no-ff v3-rewrite -m "v3.0.0 from-scratch rewrite"`
3. Resolve any conflicts (expected: `theme.css`, `manifest.json`,
   `CHANGELOG.md` — all should resolve cleanly because `v3-rewrite` is
   ahead on every file).
4. Do not push yet.

### Step R5 — release artifacts

1. `scripts/build_release.py` -> produces
   `dist/Owen-Graphite-3.0.0.zip` (or `-beta.0` suffix per question 1).
2. Tag the merge commit: `git tag v3.0.0` (per the v2 convention of
   numeric-only tags, also create `3.0.0` — confirm with user).
3. Draft GitHub release notes (Korean + English headline:
   "v3.0.0 — Zero !important, identical pixels.").

### Step R6 — push

1. `git push origin main`
2. `git push origin v3.0.0` (and `3.0.0` if tagged)
3. Upload `dist/Owen-Graphite-3.0.0.zip` to the GitHub release.
4. Open community theme update PR if the directory listing requires it
   (per Obsidian Community Themes repo conventions; the user has done
   this for v2.x previously).

## Rollback plan

`v3-rewrite` history is preserved indefinitely. If a critical regression
surfaces post-release:

1. `git checkout main && git revert -m 1 <merge-commit-sha>` to restore
   v2.30.14 as the head of `main`.
2. Re-publish the v2.30.14 ZIP from `dist/Owen-Graphite-2.30.zip` (kept
   per `/memories/repo/v2-30-baseline.md`).
3. File issue against `v3-rewrite` for the regression and continue work
   on the branch.

## What this plan deliberately does NOT do

Per `docs/v3/design-spec.md` Non-Goals (lines 175-184):

- No new design language.
- No new features.
- No Style Settings option additions / removals / renames (the 37 v2 options
  stay byte-identical).
- No `minAppVersion` change (stays 1.6.0).
- No new plugin support.

Any of those is deferred to v3.1+.
