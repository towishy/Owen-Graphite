# Source MAP Risk Classification

Canonical MAP location: `dev/WIKI/MAP`.

## Summary

- Version: `3.1.102`
- Source: `src/entry.css`
- Modules: 26
- Selectors: 2663
- Findings: 692
- Finding severity counts: critical=0, high=0, medium=547, low=145, info=0
- Module severity counts: critical=0, high=17, medium=5, low=3, info=1

## Module Risk Table

| Severity | Score | Module | Selectors | !important | :has | Reasons |
|---|---:|---|---:|---:|---:|---|
| info | 0 | `src/features/40-style-settings.css` | 0 | 0 | 0 | - |
| low | 2 | `src/tokens/00-light-tokens.css` | 6 | 0 | 0 | pdf-header-footer-sensitive |
| low | 2 | `src/tokens/01-dark-tokens.css` | 4 | 0 | 0 | pdf-header-footer-sensitive |
| medium | 18 | `src/base/10-base-workspace.css` | 18 | 0 | 0 | high-specificity, cm6-hit-routing-sensitive |
| high | 81 | `src/base/12-reading-content.css` | 161 | 0 | 2 | high-specificity, cm6-hit-routing-sensitive, has-selector, repeated-selector-in-file |
| high | 103 | `src/surfaces/20-reading-tables-code.css` | 154 | 0 | 2 | high-specificity, cm6-hit-routing-sensitive, has-selector, repeated-selector-in-file |
| high | 62 | `src/surfaces/21-reading-callouts-lists.css` | 119 | 0 | 2 | high-specificity, has-selector, repeated-selector-in-file |
| medium | 21 | `src/surfaces/22-reading-embeds-workspace.css` | 27 | 0 | 0 | high-specificity, cm6-hit-routing-sensitive |
| high | 69 | `src/themes/50-dark.css` | 95 | 0 | 0 | high-specificity |
| high | 39 | `src/features/43-print-base.css` | 116 | 0 | 0 | high-specificity, cm6-hit-routing-sensitive, repeated-selector-in-file |
| high | 227 | `src/base/13-live-preview.css` | 193 | 0 | 1 | high-specificity, cm6-hit-routing-sensitive, has-selector, repeated-selector-in-file |
| high | 89 | `src/features/41-feature-presets.css` | 295 | 0 | 0 | high-specificity, pdf-header-footer-sensitive, repeated-selector-in-file |
| medium | 20 | `src/chrome/30-workspace.css` | 118 | 0 | 0 | high-specificity, repeated-selector-in-file |
| medium | 18 | `src/chrome/31-navigation-tasks-search.css` | 47 | 0 | 0 | high-specificity |
| high | 78 | `src/chrome/32-overlay-popover-dataview.css` | 37 | 0 | 0 | high-specificity |
| high | 281 | `src/chrome/33-settings-controls.css` | 199 | 0 | 41 | high-specificity, has-selector, repeated-selector-in-file |
| high | 57 | `src/plugins/60-canvas-graph-link-panes.css` | 64 | 0 | 0 | high-specificity |
| high | 106 | `src/plugins/61-live-preview-mobile-plugin.css` | 68 | 0 | 7 | high-specificity, cm6-hit-routing-sensitive, has-selector, repeated-selector-in-file |
| high | 162 | `src/features/42-report-print-polish.css` | 209 | 0 | 9 | high-specificity, cm6-hit-routing-sensitive, has-selector, repeated-selector-in-file |
| medium | 18 | `src/chrome/34-nav-ribbon-glass.css` | 27 | 0 | 0 | high-specificity |
| high | 60 | `src/chrome/35-editing-menu-tooltip-glass.css` | 110 | 0 | 1 | high-specificity, cm6-hit-routing-sensitive, has-selector, repeated-selector-in-file |
| high | 55 | `src/chrome/36-floating-ui-glass-system.css` | 104 | 0 | 0 | high-specificity, repeated-selector-in-file |
| high | 391 | `src/chrome/37-tabs-file-explorer-search.css` | 231 | 0 | 102 | high-specificity, has-selector, repeated-selector-in-file |
| low | 10 | `src/themes/51-accessibility-motion-contrast.css` | 20 | 0 | 0 | high-specificity, repeated-selector-in-file |
| high | 114 | `src/surfaces/23-liquid-glass-core.css` | 190 | 0 | 7 | high-specificity, has-selector, repeated-selector-in-file |
| high | 66 | `src/surfaces/24-html-table-live-preview-glass.css` | 51 | 0 | 0 | high-specificity, cm6-hit-routing-sensitive, repeated-selector-in-file |

## Findings

| Severity | Category | Location | Message |
|---|---|---|---|
| medium | high-specificity | `src/base/10-base-workspace.css:5` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/10-base-workspace.css:9` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/10-base-workspace.css:47` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/10-base-workspace.css:58` | specificity=(0, 11, 0) |
| medium | high-specificity | `src/base/10-base-workspace.css:68` | specificity=(0, 9, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/10-base-workspace.css:96` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/12-reading-content.css:37` | specificity=(0, 8, 3) |
| medium | high-specificity | `src/base/12-reading-content.css:55` | specificity=(0, 8, 9) |
| medium | high-specificity | `src/base/12-reading-content.css:103` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:132` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:157` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:175` | specificity=(0, 8, 3) |
| medium | high-specificity | `src/base/12-reading-content.css:245` | specificity=(0, 14, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:249` | specificity=(0, 10, 4) |
| medium | high-specificity | `src/base/12-reading-content.css:682` | specificity=(0, 8, 4) |
| medium | high-specificity | `src/base/12-reading-content.css:703` | specificity=(0, 12, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:707` | specificity=(0, 12, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:911` | specificity=(0, 9, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:936` | specificity=(0, 21, 15) |
| medium | high-specificity | `src/base/12-reading-content.css:1028` | specificity=(0, 9, 17) |
| medium | cm6-hit-routing-sensitive | `src/base/12-reading-content.css:1069` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/12-reading-content.css:1089` | specificity=(0, 8, 3) |
| medium | cm6-hit-routing-sensitive | `src/base/12-reading-content.css:1089` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/12-reading-content.css:1102` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/12-reading-content.css:1120` | specificity=(0, 14, 2) |
| medium | high-specificity | `src/base/12-reading-content.css:1183` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:1216` | specificity=(0, 12, 3) |
| medium | high-specificity | `src/base/12-reading-content.css:1223` | specificity=(0, 24, 6) |
| medium | high-specificity | `src/base/12-reading-content.css:1230` | specificity=(0, 12, 3) |
| medium | cm6-hit-routing-sensitive | `src/base/12-reading-content.css:1313` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/12-reading-content.css:1321` | CM6 rule declares vertical box or overlay-sensitive properties |
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
| medium | high-specificity | `src/base/13-live-preview.css:148` | specificity=(0, 8, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:148` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:149` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:157` | specificity=(0, 8, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:157` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:292` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:314` | specificity=(0, 8, 2) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:343` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:350` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:363` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:389` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:396` | specificity=(0, 16, 4) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:422` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:447` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:454` | specificity=(0, 8, 4) |
| medium | high-specificity | `src/base/13-live-preview.css:489` | specificity=(0, 12, 6) |
| medium | high-specificity | `src/base/13-live-preview.css:516` | specificity=(0, 9, 3) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:588` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:599` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:612` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:638` | specificity=(0, 11, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:648` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:654` | specificity=(0, 9, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:667` | specificity=(0, 9, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:667` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:691` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:722` | specificity=(0, 8, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:753` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:784` | specificity=(0, 9, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:789` | specificity=(0, 9, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:797` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:804` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:815` | specificity=(0, 24, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:834` | specificity=(0, 12, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:844` | specificity=(0, 15, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:849` | specificity=(0, 15, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:870` | specificity=(0, 12, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:870` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:877` | CM6 rule declares vertical box or overlay-sensitive properties |
