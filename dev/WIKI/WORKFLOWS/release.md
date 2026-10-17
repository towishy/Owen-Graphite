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
- Consolidate decoration longhands only when all four constituents are present
  with static values. Combining a `var()` declaration into a shorthand can
  change invalid-at-computed-value behavior for the other constituents.
- Factor selector alternatives only when their specificity and matching sets
  are unchanged. In particular, keep `:has(+ table)` and
  `:has(+ .table-wrapper)` separate: their type/class weights differ.
- An installed Edge can run optional visual checks without a browser download:
  `release_check.py --include-visual --browser-channel msedge`.

- Confirm `manifest.json` version.
- Run `dev/scripts/release_preflight.py --version <version>` before tagging.
- Use numeric semver tags and GitHub Release names only, for example `3.1.57`; never use a leading `v` prefix.
- Confirm `theme.css` matches `dist/theme-v3.css`.
- Confirm source usage map is fresh.
- Confirm core principles gate passes.

## CSS Lint Follow-Up (2026-10-17, Unreleased)

The follow-up to 3.1.102 removes two code-wrapper selector branches already
covered by descendant branches with the same specificity, factors the shared
CM6 empty-line `:has(br:only-child)` outside `:is()`, and removes two
comment-only rules. The active-line alternative stays inside `:is()` so its
specificity contribution is preserved. No declarations, settings metadata,
minimum host version, or optional companion behavior change in that first pass.

The second pass consolidates callout and icon geometry into their existing
owner rules, removes a list-note margin rule fully overridden under the same
`@supports`, removes six longhands shadowed by later shorthands, and drops five
identical static background-color repetitions. It retains the effective
margin, background clipping, HTML table header dividers, and variable-invalidity
behavior. It does not add DOM hooks or a companion dependency.

Measured with Stylelint 17.16.0 and `stylelint-config-obsidianmd` 0.1.0,
without rule overrides or inline suppressions:

| Diagnostic | 3.1.102 baseline | First pass | Second pass |
| --- | ---: | ---: | ---: |
| All warnings | 246 | 243 | 242 |
| `selector-pseudo-class-disallowed-list` (`:has()`) | 178 | 175 | 174 |
| Partial-support `text-decoration` warnings | 60 | 60 | 60 |
| Partial-support `clip-path` warnings | 8 | 8 | 8 |
| All standard-rule errors | 13601 | 13598 | 13579 |
| `block-no-empty` errors | 2 | 0 | 0 |
| `no-descending-specificity` errors | 723 | 722 | 722 |
| `declaration-block-no-shorthand-property-overrides` errors | 6 | 6 | 0 |
| `declaration-block-no-redundant-longhand-properties` errors | 64 | 64 | 59 |

The complete official configuration still exits with code 2. Its existing
formatting, naming, vendor-prefix, cascade, deprecated-property, and other
diagnostics have not been disabled or declared resolved. These counts describe
the compact shipping bundle, not the readable source; dependency/browser-data
updates or a different input file can change them.

Validation used Edge 155.0.4283.45: both selector pairs match the same fixture
elements and pass 312 competing-specificity/source-order cases. Eight
screen/print, light/dark, and auto-dark scenarios compare 475 elements, 60
computed properties, and `::before`/`::after`, with zero differences. This is
browser fixture evidence, not an installed-Obsidian runtime capture.

For the second pass, the same browser compares 144 scenarios across the compact
bundle and readable, undeduplicated source: screen/print, light/dark, LTR/RTL,
700/701/1280px widths, and default/valid/invalid variable values. Each scenario
compares 828 elements, 65 computed properties, and both pseudo-elements, with
zero differences. Two representative light/dark viewport screenshots are
byte-identical. These checks include callouts, marked notes after lists,
nested blockquotes, view titles, HTML tables, and excluded markdown widgets.
The Obsidian CDP endpoint was unavailable, so no actual-app DOM-hook substitution
or runtime validation is claimed.

Seven persistent cleanup contracts in `dev/scripts/test_css_cleanup.py` pass;
the full existing test discovery passes 22 tests. The cleanup contracts reproduce
the original duplicate-owner and shadowed-declaration failures before editing
and are included automatically in `release_check.py`.

The source-usage and core-principles gates pass. The aggregate release check
stops at the docs/assets audit on broken or out-of-repository links in the
managed `docs/wiki-design/` copies. Do not edit those copies or bypass that
gate to present this follow-up as release-ready.

### Alternative Approaches And Boundaries

- Prefer additional direct-owner deduplication when matching sets, specificity,
  media/support conditions, rule order, and computed values can all be proved
  equivalent. Do not remove a more-specific branch merely because a broader
  selector matches the same elements.
- Replace a relational selector with an existing stable class or attribute
  only after actual Obsidian DOM evidence proves the same state coverage.
  State styling must still work when optional plugins are disabled.
- Companion-managed state classes can replace some dynamic ancestor queries,
  but require a separately approved ownership change: initial state,
  updates, unload cleanup, specificity, and theme-only fallback must be tested.
  Making the companion mandatory is not an equivalent CSS cleanup.
- SVG, masks, borders, or pseudo-elements may replace individual clipped
  shapes, but are not a blanket fix. Verify shape, resizing, hit targets,
  shadows, focus rings, and print output; the replacement may have its own
  support advisory.
- Keep progressive fallbacks and `@supports` for genuinely required features.
  They improve compatibility but do not erase static lint warnings. Do not
  replace variable-driven decoration longhands, change the minimum app
  version, or disable a rule solely to reduce a counter.
