# Source MAP Risk Classification

Canonical MAP location: `dev/WIKI/MAP`.

## Summary

- Version: `3.1.68`
- Source: `src/entry.css`
- Modules: 26
- Selectors: 2419
- Findings: 592
- Finding severity counts: critical=0, high=0, medium=490, low=102, info=0
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
| high | 204 | `src/base/13-live-preview.css` | 157 | 0 | 2 | high-specificity, cm6-hit-routing-sensitive, has-selector, repeated-selector-in-file |
| high | 89 | `src/features/41-feature-presets.css` | 310 | 0 | 0 | high-specificity, pdf-header-footer-sensitive, repeated-selector-in-file |
| medium | 23 | `src/chrome/30-workspace.css` | 127 | 0 | 0 | high-specificity, repeated-selector-in-file |
| medium | 18 | `src/chrome/31-navigation-tasks-search.css` | 43 | 0 | 0 | high-specificity |
| high | 78 | `src/chrome/32-overlay-popover-dataview.css` | 37 | 0 | 0 | high-specificity |
| high | 82 | `src/chrome/33-settings-controls.css` | 79 | 0 | 2 | high-specificity, has-selector |
| high | 57 | `src/plugins/60-canvas-graph-link-panes.css` | 64 | 0 | 0 | high-specificity |
| high | 106 | `src/plugins/61-live-preview-mobile-plugin.css` | 67 | 0 | 7 | high-specificity, cm6-hit-routing-sensitive, has-selector, repeated-selector-in-file |
| high | 161 | `src/features/42-report-print-polish.css` | 265 | 0 | 11 | high-specificity, cm6-hit-routing-sensitive, pdf-header-footer-sensitive, has-selector, repeated-selector-in-file |
| medium | 18 | `src/chrome/34-nav-ribbon-glass.css` | 25 | 0 | 0 | high-specificity |
| high | 61 | `src/chrome/35-editing-menu-tooltip-glass.css` | 110 | 0 | 0 | high-specificity, cm6-hit-routing-sensitive, repeated-selector-in-file |
| high | 70 | `src/chrome/36-floating-ui-glass-system.css` | 117 | 0 | 0 | high-specificity, repeated-selector-in-file |
| high | 296 | `src/chrome/37-tabs-file-explorer-search.css` | 191 | 0 | 79 | high-specificity, has-selector, repeated-selector-in-file |
| low | 3 | `src/themes/51-accessibility-motion-contrast.css` | 16 | 0 | 0 | repeated-selector-in-file |
| high | 96 | `src/surfaces/23-liquid-glass-core.css` | 158 | 0 | 6 | high-specificity, has-selector, repeated-selector-in-file |
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
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:209` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:216` | specificity=(0, 8, 4) |
| medium | high-specificity | `src/base/13-live-preview.css:251` | specificity=(0, 12, 6) |
| medium | high-specificity | `src/base/13-live-preview.css:278` | specificity=(0, 9, 3) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:350` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:361` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:374` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:400` | specificity=(0, 11, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:410` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:416` | specificity=(0, 9, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:429` | specificity=(0, 9, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:429` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:453` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:490` | specificity=(0, 8, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:521` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:552` | specificity=(0, 9, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:557` | specificity=(0, 9, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:565` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:572` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:583` | specificity=(0, 24, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:602` | specificity=(0, 12, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:612` | specificity=(0, 15, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:617` | specificity=(0, 15, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:638` | specificity=(0, 12, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:638` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:645` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:652` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:659` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:686` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:698` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:736` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:743` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:751` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:760` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:766` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:845` | CM6 rule declares vertical box or overlay-sensitive properties |
