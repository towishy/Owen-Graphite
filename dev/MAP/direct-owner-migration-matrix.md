# Direct Owner Migration Matrix

This matrix records the direct-owner migration that retired the late polish/hotfix/overlay layer. New work should continue editing the source owner modules directly.

## Phase Matrix

| Phase | Goal | Artifact | Gate |
| ---: | --- | --- | --- |
| 0 | Freeze current release baseline | `dev/MAP/effective-baseline/v3.1.43/*` | bundle hashes, import order, source map, environment recorded |
| 1 | Define source ownership | `dev/MAP/owner-registry.json` | every high-risk surface has an owner module |
| 2 | Retire late layer | removed `src/polish/*` modules | no active late selectors/properties |
| 3 | Capture effective values | `capture_effective_snapshot.py` | screen/print, light/dark, pseudo, tokens captured |
| 4 | Capture provenance | `capture_provenance_snapshot.py` | matched rules map back to source modules |
| 5 | Cover settings | `build_style_settings_matrix.py` | every Style Settings value appears in at least one scenario |
| 6 | Review provenance | `capture_provenance_snapshot.py` + `dev/MAP/effective-source-map.json` | matched rules map back to owner modules |
| 7 | Migrate one surface | owner source edit + late rule removal | strict computed diff remains zero |
| 8 | Validate structure | provenance diff + late count | winning source moves toward owner modules |
| 9 | Repeat in small slices | per-surface migration | late dependency count trends down |

## Required Commands

```powershell
.\.venv\Scripts\python.exe dev\scripts\build_effective_source_map.py
.\.venv\Scripts\python.exe dev\scripts\build_effective_baseline.py
.\.venv\Scripts\python.exe dev\scripts\build_style_settings_matrix.py
.\.venv\Scripts\python.exe dev\scripts\capture_effective_snapshot.py --theme light --media screen --include-tokens
.\.venv\Scripts\python.exe dev\scripts\capture_effective_snapshot.py --theme dark --media screen --include-tokens
.\.venv\Scripts\python.exe dev\scripts\capture_provenance_snapshot.py --theme light --media screen
```

## Non-Negotiable Rule

New work should modify the owner module first. Reintroducing `src/polish/*` is treated as new migration debt and should be avoided unless a future compatibility issue has no direct-owner alternative.

## Migration Log

| Slice | Owner | Former late module | Validation |
| --- | --- | --- | --- |
| Live Preview spelling and grammar underline | `src/base/13-live-preview.css` | `src/polish/70-late-reading-nav-polish.css` | light/dark effective snapshot self-diff stayed zero |
| File explorer active file row | `src/chrome/37-tabs-file-explorer-search.css` | `src/polish/70-late-reading-nav-polish.css` | light/dark effective snapshot diff checked before baseline refresh |
| File explorer active parent folders | `src/chrome/37-tabs-file-explorer-search.css` | `src/polish/70-late-reading-nav-polish.css` | light/dark effective snapshot diff checked before baseline refresh |
| Reading link grammar | `src/base/12-reading-content.css`, `src/themes/50-dark.css` | `src/polish/70-late-reading-nav-polish.css` | light/dark effective snapshot diff checked before baseline refresh |
| Reading rhythm, status badges, and hr | `src/base/12-reading-content.css`, `src/surfaces/21-reading-callouts-lists.css`, `src/themes/50-dark.css`, `src/features/43-print-base.css` | `src/polish/70-late-reading-nav-polish.css` | light/dark effective snapshot diff checked before baseline refresh |
| Reading table screen polish and heading rhythm | `src/surfaces/20-reading-tables-code.css`, `src/base/12-reading-content.css`, `src/themes/50-dark.css` | `src/polish/70-late-reading-nav-polish.css` | light/dark effective snapshot diff checked before baseline refresh |
| PDF table color parity | `src/features/42-report-print-polish.css` | `src/polish/70-late-reading-nav-polish.css` | print fixture diff checked before baseline refresh |
| Relaxed document typography preset | `src/features/41-feature-presets.css` | `src/polish/70-late-reading-nav-polish.css` | relaxed screen light/dark fixture diff checked before baseline refresh |
| Relaxed document surfaces preset | `src/features/41-feature-presets.css` | `src/polish/70-late-reading-nav-polish.css` | relaxed screen light/dark and print fixture diff checked before baseline refresh |
| Global left-bar accessibility guard | `src/themes/51-accessibility-motion-contrast.css` | `src/polish/70-late-reading-nav-polish.css` | screen light/dark effective snapshot diff checked before baseline refresh |
| Overlay interaction polish | `src/chrome/36-floating-ui-glass-system.css` | `src/polish/71-overlay-layout-polish.css` | screen light/dark effective snapshot diff checked before baseline refresh |
| Reading and Live Preview width hotfixes | `src/base/12-reading-content.css`, `src/base/13-live-preview.css` | `src/polish/71-overlay-layout-polish.css` | screen light/dark effective snapshot diff checked before baseline refresh |
| Dark blockquote parity tokens | `src/themes/50-dark.css` | `src/polish/71-overlay-layout-polish.css` | screen light/dark effective snapshot diff checked before baseline refresh |
| Mobile reading responsiveness | `src/base/12-reading-content.css`, `src/surfaces/21-reading-callouts-lists.css`, `src/chrome/37-tabs-file-explorer-search.css` | `src/polish/71-overlay-layout-polish.css` | mobile light/dark effective snapshot diff checked before baseline refresh |
| Callout color and left-bar guard | `src/surfaces/21-reading-callouts-lists.css` | `src/polish/71-overlay-layout-polish.css` | screen light/dark effective snapshot diff checked before baseline refresh |
| Code labels and reading link hints | `src/surfaces/20-reading-tables-code.css`, `src/base/12-reading-content.css` | `src/polish/71-overlay-layout-polish.css` | screen light/dark effective snapshot diff checked before baseline refresh |
| Extended codeblock label mapping | `src/surfaces/20-reading-tables-code.css` | `src/polish/71-overlay-layout-polish.css` | screen light/dark effective snapshot diff checked before baseline refresh |
| Status/search/frontmatter readability | `src/chrome/36-floating-ui-glass-system.css`, `src/chrome/32-overlay-popover-dataview.css`, `src/chrome/30-workspace.css`, `src/base/13-live-preview.css` | `src/polish/71-overlay-layout-polish.css` | screen light/dark effective snapshot diff checked before baseline refresh |
| PDF frontmatter/properties hide | `src/features/43-print-base.css` | `src/polish/71-overlay-layout-polish.css` | print light/dark effective snapshot diff checked before baseline refresh |
| PDF heading hierarchy parity | `src/features/43-print-base.css` | `src/polish/71-overlay-layout-polish.css` | print light/dark effective snapshot diff checked before baseline refresh |
| PDF codeblock export and labels | `src/features/42-report-print-polish.css` | `src/polish/71-overlay-layout-polish.css` | print light/dark effective snapshot diff checked before baseline refresh |
| Screen heading hierarchy | `src/base/12-reading-content.css`, `src/themes/50-dark.css`, `src/base/13-live-preview.css` | `src/polish/71-overlay-layout-polish.css` | screen light/dark effective snapshot diff checked before baseline refresh |
| Workflow callout rhythm | `src/surfaces/21-reading-callouts-lists.css` | `src/polish/73-workflow-polish.css` | screen light/dark effective snapshot diff checked before baseline refresh |
| Workflow report tables and code affordance | `src/surfaces/20-reading-tables-code.css` | `src/polish/73-workflow-polish.css` | screen light/dark effective snapshot diff checked before baseline refresh |
| Workflow dark contrast | `src/themes/50-dark.css` | `src/polish/73-workflow-polish.css` | screen light/dark effective snapshot diff checked before baseline refresh |
| Workflow mobile density | `src/surfaces/21-reading-callouts-lists.css`, `src/surfaces/20-reading-tables-code.css` | `src/polish/73-workflow-polish.css` | 640px screen light/dark effective snapshot diff checked before baseline refresh |
| Workflow print title and code polish | `src/features/43-print-base.css`, `src/features/42-report-print-polish.css` | `src/polish/73-workflow-polish.css` | print light/dark effective snapshot diff checked before baseline refresh |
| Style Settings color swatch guards | `src/chrome/33-settings-controls.css` | `src/polish/72-a11y-regression-hotfixes.css` | screen light/dark effective snapshot diff and hit-routing audit checked before baseline refresh |
| CM6 table row inflation guard | `src/base/13-live-preview.css` | `src/polish/72-a11y-regression-hotfixes.css` | screen light/dark effective snapshot diff and hit-routing audit checked before baseline refresh |
| Callout alignment and long inline-code guards | `src/surfaces/21-reading-callouts-lists.css`, `src/base/13-live-preview.css` | `src/polish/72-a11y-regression-hotfixes.css` | screen light/dark effective snapshot diff and hit-routing audit checked before baseline refresh |
| Callout adjacent separators and checklist repair | `src/surfaces/21-reading-callouts-lists.css`, `src/base/13-live-preview.css` | `src/polish/72-a11y-regression-hotfixes.css` | screen light/dark effective snapshot diff and hit-routing audit checked before baseline refresh |
| Table Candidate A frosted ledger parity | `src/surfaces/20-reading-tables-code.css`, `src/base/13-live-preview.css`, `src/themes/50-dark.css` | `src/polish/72-a11y-regression-hotfixes.css` | screen light/dark effective snapshot diff and hit-routing audit checked before baseline refresh |
| Rendered heading breathing room | `src/base/12-reading-content.css` | `src/polish/72-a11y-regression-hotfixes.css` | screen light/dark effective snapshot diff checked before baseline refresh |
| Liquid list markers and task states | `src/surfaces/21-reading-callouts-lists.css`, `src/base/13-live-preview.css`, `src/themes/50-dark.css` | `src/polish/72-a11y-regression-hotfixes.css` | screen light/dark effective snapshot diff and hit-routing audit checked before baseline refresh |
| Live Preview list marker parity | `src/base/13-live-preview.css`, `src/themes/50-dark.css` | `src/polish/72-a11y-regression-hotfixes.css` | screen light/dark effective snapshot diff and hit-routing audit checked before baseline refresh |
| Native list restore and highlight alignment | `src/surfaces/21-reading-callouts-lists.css`, `src/base/13-live-preview.css`, `src/themes/50-dark.css` | `src/polish/72-a11y-regression-hotfixes.css` | screen light/dark effective snapshot diff and hit-routing audit checked before baseline refresh |
| Liquid Glass reading callout refresh | `src/surfaces/21-reading-callouts-lists.css`, `src/themes/50-dark.css` | `src/polish/72-a11y-regression-hotfixes.css` | screen light/dark effective snapshot diff checked before baseline refresh |
| Live Preview callout parity | `src/base/13-live-preview.css` | `src/polish/72-a11y-regression-hotfixes.css` | screen light/dark effective snapshot diff and hit-routing audit checked before baseline refresh |
| Code block cascade and print repair | `src/surfaces/20-reading-tables-code.css`, `src/base/13-live-preview.css`, `src/features/42-report-print-polish.css` | `src/polish/72-a11y-regression-hotfixes.css` | screen/print effective snapshot diff and hit-routing audit checked before baseline refresh |
