# Source MAP Risk Classification

Canonical MAP location: `dev/WIKI/MAP`.

## Summary

- Version: `3.1.61`
- Source: `src/entry.css`
- Modules: 26
- Selectors: 2389
- Findings: 549
- Finding severity counts: critical=0, high=0, medium=471, low=78, info=0
- Module severity counts: critical=0, high=17, medium=5, low=3, info=1

## Module Risk Table

| Severity | Score | Module | Selectors | !important | :has | Reasons |
|---|---:|---|---:|---:|---:|---|
| info | 0 | `src/features/40-style-settings.css` | 0 | 0 | 0 | - |
| low | 2 | `src/tokens/00-light-tokens.css` | 6 | 0 | 0 | pdf-header-footer-sensitive |
| low | 2 | `src/tokens/01-dark-tokens.css` | 7 | 0 | 0 | pdf-header-footer-sensitive |
| medium | 18 | `src/base/10-base-workspace.css` | 17 | 0 | 0 | high-specificity, cm6-hit-routing-sensitive |
| high | 82 | `src/base/12-reading-content.css` | 106 | 0 | 6 | high-specificity, cm6-hit-routing-sensitive, has-selector, repeated-selector-in-file |
| high | 110 | `src/surfaces/20-reading-tables-code.css` | 153 | 0 | 4 | high-specificity, cm6-hit-routing-sensitive, has-selector, repeated-selector-in-file |
| high | 67 | `src/surfaces/21-reading-callouts-lists.css` | 121 | 0 | 3 | high-specificity, has-selector, repeated-selector-in-file |
| medium | 21 | `src/surfaces/22-reading-embeds-workspace.css` | 30 | 0 | 0 | high-specificity, cm6-hit-routing-sensitive |
| high | 66 | `src/themes/50-dark.css` | 87 | 0 | 0 | high-specificity |
| high | 33 | `src/features/43-print-base.css` | 63 | 0 | 0 | high-specificity, cm6-hit-routing-sensitive, repeated-selector-in-file |
| high | 204 | `src/base/13-live-preview.css` | 160 | 0 | 2 | high-specificity, cm6-hit-routing-sensitive, has-selector, repeated-selector-in-file |
| high | 89 | `src/features/41-feature-presets.css` | 310 | 0 | 0 | high-specificity, pdf-header-footer-sensitive, repeated-selector-in-file |
| medium | 23 | `src/chrome/30-workspace.css` | 127 | 0 | 0 | high-specificity, repeated-selector-in-file |
| medium | 18 | `src/chrome/31-navigation-tasks-search.css` | 43 | 0 | 0 | high-specificity |
| high | 78 | `src/chrome/32-overlay-popover-dataview.css` | 37 | 0 | 0 | high-specificity |
| high | 78 | `src/chrome/33-settings-controls.css` | 73 | 0 | 0 | high-specificity |
| high | 57 | `src/plugins/60-canvas-graph-link-panes.css` | 64 | 0 | 0 | high-specificity |
| high | 106 | `src/plugins/61-live-preview-mobile-plugin.css` | 67 | 0 | 7 | high-specificity, cm6-hit-routing-sensitive, has-selector, repeated-selector-in-file |
| high | 162 | `src/features/42-report-print-polish.css` | 266 | 0 | 11 | high-specificity, cm6-hit-routing-sensitive, pdf-header-footer-sensitive, has-selector, repeated-selector-in-file |
| medium | 18 | `src/chrome/34-nav-ribbon-glass.css` | 25 | 0 | 0 | high-specificity |
| high | 61 | `src/chrome/35-editing-menu-tooltip-glass.css` | 110 | 0 | 0 | high-specificity, cm6-hit-routing-sensitive, repeated-selector-in-file |
| high | 70 | `src/chrome/36-floating-ui-glass-system.css` | 117 | 0 | 0 | high-specificity, repeated-selector-in-file |
| high | 144 | `src/chrome/37-tabs-file-explorer-search.css` | 167 | 0 | 32 | high-specificity, has-selector, repeated-selector-in-file |
| low | 3 | `src/themes/51-accessibility-motion-contrast.css` | 16 | 0 | 0 | repeated-selector-in-file |
| high | 96 | `src/surfaces/23-liquid-glass-core.css` | 154 | 0 | 6 | high-specificity, has-selector, repeated-selector-in-file |
| high | 109 | `src/surfaces/24-html-table-live-preview-glass.css` | 63 | 0 | 0 | high-specificity, cm6-hit-routing-sensitive, repeated-selector-in-file |

## Findings

| Severity | Category | Location | Message |
|---|---|---|---|
| medium | high-specificity | `src/base/10-base-workspace.css:5` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/10-base-workspace.css:9` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/10-base-workspace.css:47` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/10-base-workspace.css:58` | specificity=(0, 11, 0) |
| medium | high-specificity | `src/base/10-base-workspace.css:64` | specificity=(0, 9, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/10-base-workspace.css:97` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/12-reading-content.css:37` | specificity=(0, 8, 3) |
| medium | high-specificity | `src/base/12-reading-content.css:55` | specificity=(0, 8, 9) |
| medium | high-specificity | `src/base/12-reading-content.css:103` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:132` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:157` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:175` | specificity=(0, 8, 3) |
| medium | high-specificity | `src/base/12-reading-content.css:245` | specificity=(0, 14, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:249` | specificity=(0, 10, 4) |
| medium | high-specificity | `src/base/12-reading-content.css:383` | specificity=(0, 9, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:412` | specificity=(0, 21, 15) |
| medium | high-specificity | `src/base/12-reading-content.css:434` | specificity=(0, 12, 3) |
| medium | high-specificity | `src/base/12-reading-content.css:504` | specificity=(0, 9, 17) |
| medium | cm6-hit-routing-sensitive | `src/base/12-reading-content.css:545` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/12-reading-content.css:565` | specificity=(0, 8, 3) |
| medium | cm6-hit-routing-sensitive | `src/base/12-reading-content.css:565` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/12-reading-content.css:578` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/12-reading-content.css:596` | specificity=(0, 14, 2) |
| medium | high-specificity | `src/base/12-reading-content.css:659` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:693` | specificity=(0, 12, 3) |
| medium | high-specificity | `src/base/12-reading-content.css:700` | specificity=(0, 24, 6) |
| medium | high-specificity | `src/base/12-reading-content.css:707` | specificity=(0, 12, 3) |
| medium | cm6-hit-routing-sensitive | `src/base/12-reading-content.css:790` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/12-reading-content.css:798` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:26` | specificity=(0, 42, 115) |
| medium | high-specificity | `src/base/13-live-preview.css:32` | specificity=(0, 8, 2) |
| medium | high-specificity | `src/base/13-live-preview.css:37` | specificity=(0, 9, 3) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:70` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:78` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:92` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:117` | specificity=(0, 9, 2) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:123` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:128` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:137` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:146` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:148` | specificity=(0, 10, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:148` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:154` | specificity=(0, 8, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:154` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:210` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:217` | specificity=(0, 8, 4) |
| medium | high-specificity | `src/base/13-live-preview.css:252` | specificity=(0, 12, 6) |
| medium | high-specificity | `src/base/13-live-preview.css:279` | specificity=(0, 9, 3) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:351` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:362` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:375` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:401` | specificity=(0, 11, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:411` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:417` | specificity=(0, 9, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:430` | specificity=(0, 9, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:430` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:454` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:491` | specificity=(0, 8, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:522` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:553` | specificity=(0, 9, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:558` | specificity=(0, 9, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:566` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:573` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:584` | specificity=(0, 24, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:603` | specificity=(0, 12, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:613` | specificity=(0, 15, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:618` | specificity=(0, 15, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:639` | specificity=(0, 12, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:639` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:646` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:653` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:660` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:687` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:699` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:737` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:744` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:752` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:761` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:767` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:846` | CM6 rule declares vertical box or overlay-sensitive properties |
