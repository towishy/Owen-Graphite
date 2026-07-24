# Source MAP Risk Classification

Canonical MAP location: `dev/WIKI/MAP`.

## Summary

- Version: `3.1.92`
- Source: `src/entry.css`
- Modules: 26
- Selectors: 2671
- Findings: 650
- Finding severity counts: critical=0, high=0, medium=539, low=111, info=0
- Module severity counts: critical=0, high=17, medium=5, low=3, info=1

## Module Risk Table

| Severity | Score | Module | Selectors | !important | :has | Reasons |
|---|---:|---|---:|---:|---:|---|
| info | 0 | `src/features/40-style-settings.css` | 0 | 0 | 0 | - |
| low | 2 | `src/tokens/00-light-tokens.css` | 6 | 0 | 0 | pdf-header-footer-sensitive |
| low | 2 | `src/tokens/01-dark-tokens.css` | 7 | 0 | 0 | pdf-header-footer-sensitive |
| medium | 18 | `src/base/10-base-workspace.css` | 17 | 0 | 0 | high-specificity, cm6-hit-routing-sensitive |
| high | 92 | `src/base/12-reading-content.css` | 162 | 0 | 6 | high-specificity, cm6-hit-routing-sensitive, has-selector, repeated-selector-in-file |
| high | 110 | `src/surfaces/20-reading-tables-code.css` | 153 | 0 | 4 | high-specificity, cm6-hit-routing-sensitive, has-selector, repeated-selector-in-file |
| high | 67 | `src/surfaces/21-reading-callouts-lists.css` | 122 | 0 | 3 | high-specificity, has-selector, repeated-selector-in-file |
| medium | 21 | `src/surfaces/22-reading-embeds-workspace.css` | 30 | 0 | 0 | high-specificity, cm6-hit-routing-sensitive |
| high | 69 | `src/themes/50-dark.css` | 95 | 0 | 0 | high-specificity |
| high | 39 | `src/features/43-print-base.css` | 116 | 0 | 0 | high-specificity, cm6-hit-routing-sensitive, repeated-selector-in-file |
| high | 229 | `src/base/13-live-preview.css` | 192 | 0 | 2 | high-specificity, cm6-hit-routing-sensitive, has-selector, repeated-selector-in-file |
| high | 104 | `src/features/41-feature-presets.css` | 310 | 0 | 0 | high-specificity, pdf-header-footer-sensitive, repeated-selector-in-file |
| medium | 23 | `src/chrome/30-workspace.css` | 127 | 0 | 0 | high-specificity, repeated-selector-in-file |
| medium | 18 | `src/chrome/31-navigation-tasks-search.css` | 47 | 0 | 0 | high-specificity |
| high | 78 | `src/chrome/32-overlay-popover-dataview.css` | 37 | 0 | 0 | high-specificity |
| high | 91 | `src/chrome/33-settings-controls.css` | 102 | 0 | 2 | high-specificity, has-selector |
| high | 57 | `src/plugins/60-canvas-graph-link-panes.css` | 64 | 0 | 0 | high-specificity |
| high | 106 | `src/plugins/61-live-preview-mobile-plugin.css` | 68 | 0 | 7 | high-specificity, cm6-hit-routing-sensitive, has-selector, repeated-selector-in-file |
| high | 176 | `src/features/42-report-print-polish.css` | 265 | 0 | 11 | high-specificity, cm6-hit-routing-sensitive, pdf-header-footer-sensitive, has-selector, repeated-selector-in-file |
| medium | 18 | `src/chrome/34-nav-ribbon-glass.css` | 25 | 0 | 0 | high-specificity |
| high | 66 | `src/chrome/35-editing-menu-tooltip-glass.css` | 118 | 0 | 1 | high-specificity, cm6-hit-routing-sensitive, has-selector, repeated-selector-in-file |
| high | 73 | `src/chrome/36-floating-ui-glass-system.css` | 121 | 0 | 0 | high-specificity, repeated-selector-in-file |
| high | 385 | `src/chrome/37-tabs-file-explorer-search.css` | 233 | 0 | 102 | high-specificity, has-selector, repeated-selector-in-file |
| low | 10 | `src/themes/51-accessibility-motion-contrast.css` | 20 | 0 | 0 | high-specificity, repeated-selector-in-file |
| high | 117 | `src/surfaces/23-liquid-glass-core.css` | 171 | 0 | 6 | high-specificity, has-selector, repeated-selector-in-file |
| high | 109 | `src/surfaces/24-html-table-live-preview-glass.css` | 63 | 0 | 0 | high-specificity, cm6-hit-routing-sensitive, repeated-selector-in-file |

## Findings

| Severity | Category | Location | Message |
|---|---|---|---|
| medium | high-specificity | `src/base/10-base-workspace.css:5` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/10-base-workspace.css:9` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/10-base-workspace.css:47` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/10-base-workspace.css:58` | specificity=(0, 11, 0) |
| medium | high-specificity | `src/base/10-base-workspace.css:64` | specificity=(0, 9, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/10-base-workspace.css:92` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/12-reading-content.css:37` | specificity=(0, 8, 3) |
| medium | high-specificity | `src/base/12-reading-content.css:55` | specificity=(0, 8, 9) |
| medium | high-specificity | `src/base/12-reading-content.css:103` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:132` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:157` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:175` | specificity=(0, 8, 3) |
| medium | high-specificity | `src/base/12-reading-content.css:245` | specificity=(0, 14, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:249` | specificity=(0, 10, 4) |
| medium | high-specificity | `src/base/12-reading-content.css:688` | specificity=(0, 8, 4) |
| medium | high-specificity | `src/base/12-reading-content.css:709` | specificity=(0, 12, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:713` | specificity=(0, 12, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:920` | specificity=(0, 9, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:949` | specificity=(0, 21, 15) |
| medium | high-specificity | `src/base/12-reading-content.css:985` | specificity=(0, 12, 3) |
| medium | high-specificity | `src/base/12-reading-content.css:1041` | specificity=(0, 9, 17) |
| medium | cm6-hit-routing-sensitive | `src/base/12-reading-content.css:1082` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/12-reading-content.css:1102` | specificity=(0, 8, 3) |
| medium | cm6-hit-routing-sensitive | `src/base/12-reading-content.css:1102` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/12-reading-content.css:1115` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/12-reading-content.css:1133` | specificity=(0, 14, 2) |
| medium | high-specificity | `src/base/12-reading-content.css:1196` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:1230` | specificity=(0, 12, 3) |
| medium | high-specificity | `src/base/12-reading-content.css:1237` | specificity=(0, 24, 6) |
| medium | high-specificity | `src/base/12-reading-content.css:1244` | specificity=(0, 12, 3) |
| medium | cm6-hit-routing-sensitive | `src/base/12-reading-content.css:1327` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/12-reading-content.css:1335` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:29` | specificity=(0, 15, 5) |
| medium | high-specificity | `src/base/13-live-preview.css:35` | specificity=(0, 8, 2) |
| medium | high-specificity | `src/base/13-live-preview.css:40` | specificity=(0, 9, 3) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:73` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:81` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:95` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:120` | specificity=(0, 9, 2) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:126` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:131` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:140` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:148` | specificity=(0, 10, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:148` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:149` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:157` | specificity=(0, 8, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:157` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:303` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:325` | specificity=(0, 8, 2) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:354` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:361` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:374` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:400` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:407` | specificity=(0, 16, 4) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:433` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:458` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:465` | specificity=(0, 8, 4) |
| medium | high-specificity | `src/base/13-live-preview.css:500` | specificity=(0, 12, 6) |
| medium | high-specificity | `src/base/13-live-preview.css:527` | specificity=(0, 9, 3) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:599` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:610` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:623` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:649` | specificity=(0, 11, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:659` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:665` | specificity=(0, 9, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:678` | specificity=(0, 9, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:678` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:702` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:739` | specificity=(0, 8, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:770` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:801` | specificity=(0, 9, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:806` | specificity=(0, 9, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:814` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:821` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:832` | specificity=(0, 24, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:851` | specificity=(0, 12, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:861` | specificity=(0, 15, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:866` | specificity=(0, 15, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:887` | specificity=(0, 12, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:887` | CM6 rule declares vertical box or overlay-sensitive properties |
