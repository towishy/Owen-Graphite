# Source MAP Risk Classification

Canonical MAP location: `dev/MAP`.

## Summary

- Version: `3.1.48`
- Source: `src/entry.css`
- Modules: 26
- Selectors: 2287
- Findings: 536
- Finding severity counts: critical=0, high=0, medium=461, low=75, info=0
- Module severity counts: critical=0, high=17, medium=5, low=3, info=1

## Module Risk Table

| Severity | Score | Module | Selectors | !important | :has | Reasons |
|---|---:|---|---:|---:|---:|---|
| info | 0 | `src/features/40-style-settings.css` | 0 | 0 | 0 | - |
| low | 2 | `src/tokens/00-light-tokens.css` | 6 | 0 | 0 | pdf-header-footer-sensitive |
| low | 2 | `src/tokens/01-dark-tokens.css` | 7 | 0 | 0 | pdf-header-footer-sensitive |
| medium | 18 | `src/base/10-base-workspace.css` | 17 | 0 | 0 | high-specificity, cm6-hit-routing-sensitive |
| high | 82 | `src/base/12-reading-content.css` | 106 | 0 | 6 | high-specificity, cm6-hit-routing-sensitive, has-selector, repeated-selector-in-file |
| high | 107 | `src/surfaces/20-reading-tables-code.css` | 152 | 0 | 4 | high-specificity, cm6-hit-routing-sensitive, has-selector, repeated-selector-in-file |
| high | 67 | `src/surfaces/21-reading-callouts-lists.css` | 121 | 0 | 3 | high-specificity, has-selector, repeated-selector-in-file |
| medium | 21 | `src/surfaces/22-reading-embeds-workspace.css` | 30 | 0 | 0 | high-specificity, cm6-hit-routing-sensitive |
| high | 72 | `src/themes/50-dark.css` | 87 | 0 | 0 | high-specificity |
| high | 33 | `src/features/43-print-base.css` | 63 | 0 | 0 | high-specificity, cm6-hit-routing-sensitive, repeated-selector-in-file |
| high | 219 | `src/base/13-live-preview.css` | 168 | 0 | 2 | high-specificity, cm6-hit-routing-sensitive, has-selector, repeated-selector-in-file |
| high | 79 | `src/features/41-feature-presets.css` | 306 | 0 | 0 | high-specificity, pdf-header-footer-sensitive, repeated-selector-in-file |
| medium | 23 | `src/chrome/30-workspace.css` | 125 | 0 | 0 | high-specificity, repeated-selector-in-file |
| medium | 18 | `src/chrome/31-navigation-tasks-search.css` | 40 | 0 | 0 | high-specificity |
| high | 66 | `src/chrome/32-overlay-popover-dataview.css` | 32 | 0 | 0 | high-specificity |
| high | 54 | `src/chrome/33-settings-controls.css` | 59 | 0 | 0 | high-specificity |
| high | 54 | `src/plugins/60-canvas-graph-link-panes.css` | 64 | 0 | 0 | high-specificity |
| high | 98 | `src/plugins/61-live-preview-mobile-plugin.css` | 56 | 0 | 7 | high-specificity, cm6-hit-routing-sensitive, has-selector |
| high | 168 | `src/features/42-report-print-polish.css` | 251 | 0 | 11 | high-specificity, cm6-hit-routing-sensitive, pdf-header-footer-sensitive, has-selector, repeated-selector-in-file |
| medium | 18 | `src/chrome/34-nav-ribbon-glass.css` | 21 | 0 | 0 | high-specificity |
| high | 43 | `src/chrome/35-editing-menu-tooltip-glass.css` | 78 | 0 | 0 | high-specificity, repeated-selector-in-file |
| high | 67 | `src/chrome/36-floating-ui-glass-system.css` | 113 | 0 | 0 | high-specificity, repeated-selector-in-file |
| high | 135 | `src/chrome/37-tabs-file-explorer-search.css` | 142 | 0 | 32 | high-specificity, has-selector, repeated-selector-in-file |
| low | 3 | `src/themes/51-accessibility-motion-contrast.css` | 16 | 0 | 0 | repeated-selector-in-file |
| high | 99 | `src/surfaces/23-liquid-glass-core.css` | 143 | 0 | 6 | high-specificity, cm6-hit-routing-sensitive, has-selector, repeated-selector-in-file |
| high | 141 | `src/surfaces/24-html-table-live-preview-glass.css` | 84 | 0 | 0 | high-specificity, cm6-hit-routing-sensitive, repeated-selector-in-file |

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
| medium | high-specificity | `src/base/12-reading-content.css:379` | specificity=(0, 9, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:408` | specificity=(0, 21, 15) |
| medium | high-specificity | `src/base/12-reading-content.css:430` | specificity=(0, 12, 3) |
| medium | high-specificity | `src/base/12-reading-content.css:500` | specificity=(0, 9, 17) |
| medium | cm6-hit-routing-sensitive | `src/base/12-reading-content.css:541` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/12-reading-content.css:561` | specificity=(0, 8, 3) |
| medium | cm6-hit-routing-sensitive | `src/base/12-reading-content.css:561` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/12-reading-content.css:574` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/12-reading-content.css:592` | specificity=(0, 14, 2) |
| medium | high-specificity | `src/base/12-reading-content.css:655` | specificity=(0, 8, 0) |
| medium | high-specificity | `src/base/12-reading-content.css:689` | specificity=(0, 12, 3) |
| medium | high-specificity | `src/base/12-reading-content.css:696` | specificity=(0, 24, 6) |
| medium | high-specificity | `src/base/12-reading-content.css:703` | specificity=(0, 12, 3) |
| medium | cm6-hit-routing-sensitive | `src/base/12-reading-content.css:786` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/12-reading-content.css:794` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:26` | specificity=(0, 42, 115) |
| medium | high-specificity | `src/base/13-live-preview.css:32` | specificity=(0, 8, 2) |
| medium | high-specificity | `src/base/13-live-preview.css:37` | specificity=(0, 9, 3) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:70` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:78` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:92` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:120` | specificity=(0, 9, 2) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:126` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:131` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:140` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:149` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:157` | specificity=(0, 8, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:157` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:163` | specificity=(0, 8, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:163` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:243` | specificity=(0, 12, 6) |
| medium | high-specificity | `src/base/13-live-preview.css:270` | specificity=(0, 9, 3) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:342` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:353` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:366` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:392` | specificity=(0, 11, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:402` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:408` | specificity=(0, 9, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:421` | specificity=(0, 9, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:421` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:445` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:482` | specificity=(0, 8, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:513` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:550` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:555` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:558` | specificity=(0, 8, 3) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:590` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:631` | specificity=(0, 9, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:636` | specificity=(0, 9, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:644` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:651` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | high-specificity | `src/base/13-live-preview.css:662` | specificity=(0, 24, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:681` | specificity=(0, 12, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:691` | specificity=(0, 15, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:698` | specificity=(0, 8, 3) |
| medium | high-specificity | `src/base/13-live-preview.css:701` | specificity=(0, 8, 3) |
| medium | high-specificity | `src/base/13-live-preview.css:704` | specificity=(0, 10, 3) |
| medium | high-specificity | `src/base/13-live-preview.css:709` | specificity=(0, 15, 0) |
| medium | high-specificity | `src/base/13-live-preview.css:730` | specificity=(0, 12, 0) |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:730` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:737` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:744` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:751` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:778` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:790` | CM6 rule declares vertical box or overlay-sensitive properties |
| medium | cm6-hit-routing-sensitive | `src/base/13-live-preview.css:828` | CM6 rule declares vertical box or overlay-sensitive properties |
