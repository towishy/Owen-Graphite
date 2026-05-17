# Source MAP Risk Classification

Canonical MAP location: `dev/MAP`.

## Summary

- Version: `3.1.42`
- Source: `src/entry.css`
- Modules: 30
- Selectors: 2255
- Findings: 557
- Finding severity counts: critical=0, high=0, medium=482, low=75, info=0
- Module severity counts: critical=0, high=17, medium=8, low=4, info=1

## Module Risk Table

| Severity | Score | Module | Selectors | !important | :has | Reasons |
|---|---:|---|---:|---:|---:|---|
| info | 0 | `src/features/40-style-settings.css` | 0 | 0 | 0 | - |
| low | 2 | `src/tokens/00-light-tokens.css` | 6 | 0 | 0 | pdf-header-footer-sensitive |
| low | 2 | `src/tokens/01-dark-tokens.css` | 7 | 0 | 0 | pdf-header-footer-sensitive |
| medium | 18 | `src/base/10-base-workspace.css` | 17 | 0 | 0 | high-specificity, cm6-hit-routing-sensitive |
| high | 63 | `src/base/12-reading-content.css` | 65 | 0 | 6 | high-specificity, cm6-hit-routing-sensitive, has-selector |
| medium | 18 | `src/surfaces/20-reading-tables-code.css` | 54 | 0 | 0 | high-specificity |
| high | 30 | `src/surfaces/21-reading-callouts-lists.css` | 38 | 0 | 0 | high-specificity |
| medium | 15 | `src/surfaces/22-reading-embeds-workspace.css` | 30 | 0 | 0 | high-specificity |
| high | 60 | `src/themes/50-dark.css` | 45 | 0 | 0 | high-specificity |
| medium | 25 | `src/features/43-print-base.css` | 47 | 0 | 0 | high-specificity, repeated-selector-in-file |
| high | 172 | `src/base/13-live-preview.css` | 116 | 0 | 0 | high-specificity, cm6-hit-routing-sensitive, repeated-selector-in-file |
| high | 76 | `src/features/41-feature-presets.css` | 275 | 0 | 0 | high-specificity, pdf-header-footer-sensitive, repeated-selector-in-file |
| medium | 23 | `src/chrome/30-workspace.css` | 122 | 0 | 0 | high-specificity, repeated-selector-in-file |
| medium | 18 | `src/chrome/31-navigation-tasks-search.css` | 40 | 0 | 0 | high-specificity |
| high | 66 | `src/chrome/32-overlay-popover-dataview.css` | 31 | 0 | 0 | high-specificity |
| high | 39 | `src/chrome/33-settings-controls.css` | 52 | 0 | 0 | high-specificity |
| high | 54 | `src/plugins/60-canvas-graph-link-panes.css` | 64 | 0 | 0 | high-specificity |
| high | 98 | `src/plugins/61-live-preview-mobile-plugin.css` | 56 | 0 | 7 | high-specificity, cm6-hit-routing-sensitive, has-selector |
| high | 88 | `src/features/42-report-print-polish.css` | 205 | 0 | 8 | high-specificity, cm6-hit-routing-sensitive, pdf-header-footer-sensitive, has-selector, repeated-selector-in-file |
| medium | 18 | `src/chrome/34-nav-ribbon-glass.css` | 21 | 0 | 0 | high-specificity |
| high | 43 | `src/chrome/35-editing-menu-tooltip-glass.css` | 78 | 0 | 0 | high-specificity, repeated-selector-in-file |
| high | 36 | `src/chrome/36-floating-ui-glass-system.css` | 74 | 0 | 0 | high-specificity, repeated-selector-in-file |
| medium | 24 | `src/chrome/37-tabs-file-explorer-search.css` | 66 | 0 | 0 | high-specificity |
| low | 3 | `src/themes/51-accessibility-motion-contrast.css` | 12 | 0 | 0 | repeated-selector-in-file |
| high | 165 | `src/polish/70-late-reading-nav-polish.css` | 111 | 0 | 32 | high-specificity, has-selector, repeated-selector-in-file |
| high | 157 | `src/polish/71-overlay-layout-polish.css` | 174 | 0 | 3 | high-specificity, cm6-hit-routing-sensitive, has-selector, repeated-selector-in-file |
| high | 99 | `src/surfaces/23-liquid-glass-core.css` | 143 | 0 | 6 | high-specificity, cm6-hit-routing-sensitive, has-selector, repeated-selector-in-file |
| high | 141 | `src/surfaces/24-html-table-live-preview-glass.css` | 84 | 0 | 0 | high-specificity, cm6-hit-routing-sensitive, repeated-selector-in-file |
| high | 188 | `src/polish/72-a11y-regression-hotfixes.css` | 187 | 0 | 9 | high-specificity, cm6-hit-routing-sensitive, has-selector, repeated-selector-in-file |
| low | 3 | `src/polish/73-workflow-polish.css` | 35 | 0 | 0 | repeated-selector-in-file |

## Findings

| Severity | Category | Location | Message |
|---|---|---|---|
| medium | high-specificity | `src/base/10-base-workspace.css:5` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/10-base-workspace.css:9` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/10-base-workspace.css:47` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/10-base-workspace.css:58` | specificity=(0, 11, 0) |
| medium | high-specificity | `src/base/10-base-workspace.css:64` | specificity=(0, 9, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/10-base-workspace.css:97` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/12-reading-content.css:51` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:62` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:87` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:105` | specificity=(0, 8, 3) |
| medium | high-specificity | `src/base/12-reading-content.css:126` | specificity=(0, 12, 3) |
| medium | high-specificity | `src/base/12-reading-content.css:222` | specificity=(0, 9, 17) |
| medium | cm6-hit-routing-sensitive | `src/base/12-reading-content.css:263` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/12-reading-content.css:283` | specificity=(0, 8, 3) |
| medium | cm6-hit-routing-sensitive | `src/base/12-reading-content.css:283` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/12-reading-content.css:296` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/12-reading-content.css:314` | specificity=(0, 14, 2) |
| medium | high-specificity | `src/base/12-reading-content.css:377` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:411` | specificity=(0, 12, 3) |
| medium | high-specificity | `src/base/12-reading-content.css:418` | specificity=(0, 24, 6) |
| medium | high-specificity | `src/base/12-reading-content.css:425` | specificity=(0, 12, 3) |
| medium | cm6-hit-routing-sensitive | `src/base/12-reading-content.css:508` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/12-reading-content.css:516` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:25` | specificity=(0, 31, 110) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:25` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:30` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:39` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:48` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:56` | specificity=(0, 8, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:56` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:89` | specificity=(0, 11, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:99` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:105` | specificity=(0, 9, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:118` | specificity=(0, 9, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:118` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:142` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:197` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:234` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:239` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:242` | specificity=(0, 8, 3) |
| medium | high-specificity | `src/base/13-live-preview.css:255` | specificity=(0, 9, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:260` | specificity=(0, 9, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:268` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:275` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:286` | specificity=(0, 24, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:305` | specificity=(0, 12, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:315` | specificity=(0, 15, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:322` | specificity=(0, 8, 3) |
| medium | high-specificity | `src/base/13-live-preview.css:325` | specificity=(0, 8, 3) |
| medium | high-specificity | `src/base/13-live-preview.css:328` | specificity=(0, 10, 3) |
| medium | high-specificity | `src/base/13-live-preview.css:333` | specificity=(0, 15, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:354` | specificity=(0, 12, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:354` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:361` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:368` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:375` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:402` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:414` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:439` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:446` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:454` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:486` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:492` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:571` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:581` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:589` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:598` | specificity=(0, 8, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:621` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:645` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:650` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:686` | specificity=(0, 14, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:686` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:695` | specificity=(0, 16, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:719` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:726` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:748` | specificity=(0, 8, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:757` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:774` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/chrome/30-workspace.css:25` | specificity=(0, 8, 3) |
| medium | high-specificity | `src/chrome/30-workspace.css:165` | specificity=(3, 3, 0) |
