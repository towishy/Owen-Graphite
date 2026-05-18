# Unused CSS Candidate Report

Version: 3.1.43
Bundle SHA256: `1271f83e746de9ab87414ffa58121534b8ad92f932116e5dde11290cd57f6396`
Coverage scenarios: 189

## Summary

| Classification | Count |
| --- | ---: |
| invalid-query | 3 |
| matched | 2910 |
| reserved | 699 |

## Candidate Selectors

No low-risk no-match selectors were found in the current coverage matrix.

## Reserved No-Match Selectors

Reserved no-match selectors: 699. These need purpose-built coverage before removal.

### Reserved Reason Summary

| Reason | Count |
| --- | ---: |
| obsidian-style-or-semantic-selector | 666 |
| document-content-selector | 410 |
| reserved-module | 364 |
| state-pseudo | 350 |
| reserved-at-context | 69 |
| token-or-variable | 1 |

### Reserved Bucket Summary

| Bucket | Count | Meaning |
| --- | ---: | --- |
| state-interaction | 350 | State pseudo selectors (:hover/:focus/etc.) that static DOM coverage cannot fully prove. |
| obsidian-chrome-runtime | 92 | Obsidian app chrome/runtime DOM such as workspace, nav, search, modal, menu, tooltip, or status surfaces. |
| plugin-runtime | 84 | Plugin/runtime DOM such as Canvas, Dataview, Mermaid, Graph, Bases, Pickr, or Editing Toolbar. |
| print-pdf-context | 69 | Print/PDF and PDF Style Settings selectors reserved for print-specific validation. |
| document-content-fixture-gap | 55 | Document/content semantics that need more purpose-built fixture DOM before removal review. |
| style-setting-class | 35 | Body-class Style Settings variants that are valid only under selected settings. |
| live-preview-runtime | 14 | CodeMirror/Live Preview runtime DOM and editor-generated classes. |

### Reserved Decision Policy

Current low-risk removal candidates: 0.
Reserved selectors are not deletion approval; each bucket below defines the required next validation step.

| Bucket | Decision | Next action |
| --- | --- | --- |
| state-interaction | do-not-remove | Validate through interactive state coverage or keep reserved. |
| obsidian-chrome-runtime | runtime-reserved | Validate in Obsidian app chrome runtime or keep reserved. |
| plugin-runtime | runtime-reserved | Validate in Obsidian/plugin runtime or keep reserved. |
| print-pdf-context | do-not-remove | Validate through PDF/print scenario coverage before any removal review. |
| document-content-fixture-gap | needs-purpose-built-fixture | Add natural document fixture coverage when real document evidence exists; otherwise keep as coverage backlog. |
| style-setting-class | do-not-remove | Keep reserved unless the Style Settings contract removes the class. |
| live-preview-runtime | runtime-reserved | Validate with CodeMirror/Live Preview runtime DOM or keep reserved. |

### Coverage Backlog Policy

- `document-content-fixture-gap`: Keep as coverage backlog unless a natural Obsidian document fixture can represent the selector without synthetic DOM overreach.
- `invalid-query`: Do not use invalid-query rows as deletion evidence; pseudo-element-only selectors and browser query limitations require manual or visual/context validation.

### Coverage Gap Hotspots

| Module | reserved | static | state | matched | Top buckets | Top reserved reasons |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| src/chrome/30-workspace.css | 51 | 22 | 29 | 133 | state-interaction=29, plugin-runtime=10, obsidian-chrome-runtime=7, style-setting-class=5 | reserved-module=51, obsidian-style-or-semantic-selector=34, document-content-selector=32, state-pseudo=29 |
| src/features/41-feature-presets.css | 50 | 39 | 11 | 309 | print-pdf-context=14, plugin-runtime=12, state-interaction=11, style-setting-class=11 | obsidian-style-or-semantic-selector=50, document-content-selector=28, state-pseudo=11, reserved-at-context=11 |
| src/surfaces/23-liquid-glass-core.css | 49 | 17 | 32 | 134 | state-interaction=32, obsidian-chrome-runtime=15, style-setting-class=2 | document-content-selector=49, obsidian-style-or-semantic-selector=49, state-pseudo=32 |
| src/chrome/32-overlay-popover-dataview.css | 42 | 10 | 32 | 92 | state-interaction=32, style-setting-class=6, plugin-runtime=4 | obsidian-style-or-semantic-selector=42, reserved-module=42, state-pseudo=32, document-content-selector=12 |
| src/plugins/61-live-preview-mobile-plugin.css | 41 | 18 | 23 | 130 | state-interaction=23, plugin-runtime=18 | reserved-module=41, obsidian-style-or-semantic-selector=39, state-pseudo=23, document-content-selector=8 |
| src/chrome/36-floating-ui-glass-system.css | 41 | 2 | 39 | 147 | state-interaction=39, obsidian-chrome-runtime=2 | reserved-module=41, obsidian-style-or-semantic-selector=40, state-pseudo=39, document-content-selector=27 |
| src/chrome/35-editing-menu-tooltip-glass.css | 40 | 16 | 24 | 67 | state-interaction=24, obsidian-chrome-runtime=16 | document-content-selector=40, obsidian-style-or-semantic-selector=40, reserved-module=40, state-pseudo=24 |
| src/plugins/60-canvas-graph-link-panes.css | 38 | 14 | 24 | 112 | state-interaction=24, plugin-runtime=14 | reserved-module=38, obsidian-style-or-semantic-selector=36, state-pseudo=24 |
| src/chrome/31-navigation-tasks-search.css | 32 | 24 | 8 | 35 | plugin-runtime=24, state-interaction=8 | reserved-module=32, obsidian-style-or-semantic-selector=31, document-content-selector=19, state-pseudo=8 |
| src/chrome/33-settings-controls.css | 31 | 1 | 30 | 107 | state-interaction=30, plugin-runtime=1 | obsidian-style-or-semantic-selector=31, reserved-module=31, state-pseudo=30, document-content-selector=1 |
| src/base/13-live-preview.css | 31 | 20 | 11 | 179 | state-interaction=11, style-setting-class=11, live-preview-runtime=9 | obsidian-style-or-semantic-selector=31, document-content-selector=23, state-pseudo=11 |
| src/features/42-report-print-polish.css | 31 | 31 | 0 | 350 | print-pdf-context=31 | document-content-selector=31, obsidian-style-or-semantic-selector=31, reserved-at-context=31 |

### Reserved Selector Samples

Representative no-match selectors from the largest hotspots. Static no-match selectors are shown before state-only hover/focus examples. These are examples for coverage planning, not removal approval.

#### src/chrome/30-workspace.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 585 | style-setting-class | `body.theme-dark.ogd-modern-tables .markdown-rendered table` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 591 | style-setting-class | `body.theme-dark.ogd-modern-tables .markdown-rendered table th` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 595 | style-setting-class | `body.theme-dark.ogd-modern-tables .markdown-rendered table td` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 606 | style-setting-class | `body.theme-dark.ogd-modern-tables .markdown-rendered table td:first-child` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 606 | style-setting-class | `body.theme-dark.ogd-modern-tables .markdown-rendered table th:first-child` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 355 | plugin-runtime | `.markdown-rendered .mermaid svg .nodeLabel :is(span, p)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 365 | plugin-runtime | `.markdown-rendered .mermaid svg .edgeLabel foreignObject > div` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 371 | plugin-runtime | `.markdown-rendered .mermaid svg .cluster .nodeLabel` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |

#### src/features/41-feature-presets.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 415 | print-pdf-context | `body.ogd-pdf-segment-value-violet` | document-content-selector, obsidian-style-or-semantic-selector |
| 420 | print-pdf-context | `body.ogd-pdf-segment-value-rose` | document-content-selector, obsidian-style-or-semantic-selector |
| 425 | print-pdf-context | `body.ogd-pdf-segment-value-amber` | document-content-selector, obsidian-style-or-semantic-selector |
| 678 | print-pdf-context | `body.ogd-pdf-header-top-center:is(.ogd-pdf-label-segmented, .ogd-pdf-label-segmented-dual) .markdown-rendered::before` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 683 | print-pdf-context | `body.ogd-pdf-header-enabled.ogd-pdf-header-top-center:is(.ogd-pdf-label-segmented, .ogd-pdf-label-segmented-dual) .markdown-rendered::after` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 754 | print-pdf-context | `body.ogd-pdf-header-enabled.ogd-pdf-header-top-center:is(.ogd-pdf-label-segmented-dual, .ogd-pdf-label-segmented.ogd-pdf-header-dual-pair) .markdown-rendered::after` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 759 | print-pdf-context | `body.ogd-pdf-header-top-center:is(.ogd-pdf-label-segmented-dual, .ogd-pdf-label-segmented.ogd-pdf-header-dual-pair) .markdown-rendered::before` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 764 | print-pdf-context | `body.ogd-pdf-header-enabled.ogd-pdf-header-top-center:is(.ogd-pdf-label-segmented-dual, .ogd-pdf-label-segmented.ogd-pdf-header-dual-pair)::before` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |

#### src/surfaces/23-liquid-glass-core.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 568 | style-setting-class | `body.ogd-zebra-disabled-permanently .markdown-source-view.mod-cm6 :is(.cm-table-widget, table.cm-table) tbody tr:nth-child(even) td` | document-content-selector, obsidian-style-or-semantic-selector |
| 1470 | style-setting-class | `body.ogd-zebra-disabled-permanently:not(.ogd-report-mode) .markdown-source-view.mod-cm6 :is(.cm-table-widget, table.cm-table) tbody tr:nth-child(even) td` | document-content-selector, obsidian-style-or-semantic-selector |
| 240 | obsidian-chrome-runtime | `body:not(.is-mobile) :is(.workspace-split.mod-left-split, .workspace-split.mod-right-split) .workspace-tab-header :is(.workspace-tab-header-inner, .workspace-tab-header-inner-icon)` | document-content-selector, obsidian-style-or-semantic-selector |
| 1235 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-tabs .workspace-tab-header :is(.workspace-tab-header-inner-close-button, .workspace-tab-header-inner-icon)` | document-content-selector, obsidian-style-or-semantic-selector |
| 1268 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .view-header` | document-content-selector, obsidian-style-or-semantic-selector |
| 1268 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-tab-header-container` | document-content-selector, obsidian-style-or-semantic-selector |
| 1272 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-tab-header-container` | document-content-selector, obsidian-style-or-semantic-selector |
| 1278 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-tabs .workspace-tab-header .workspace-tab-header-inner` | document-content-selector, obsidian-style-or-semantic-selector |

#### src/chrome/32-overlay-popover-dataview.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 125 | style-setting-class | `body.ogd-zebra-disabled-permanently .block-language-dataview table tbody tr:nth-child(even) td` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 125 | style-setting-class | `body.ogd-zebra-disabled-permanently .markdown-rendered .dataview.dataview-table tbody tr:nth-child(even) td` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 125 | style-setting-class | `body.ogd-zebra-disabled-permanently .markdown-rendered .dataview.table-view-table tbody tr:nth-child(even) td` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 198 | style-setting-class | `body.theme-dark.ogd-zebra-disabled-permanently .block-language-dataview table tbody tr:nth-child(even) td` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 198 | style-setting-class | `body.theme-dark.ogd-zebra-disabled-permanently .markdown-rendered .dataview.dataview-table tbody tr:nth-child(even) td` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 198 | style-setting-class | `body.theme-dark.ogd-zebra-disabled-permanently .markdown-rendered .dataview.table-view-table tbody tr:nth-child(even) td` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 24 | plugin-runtime | `.modal-title` | obsidian-style-or-semantic-selector, reserved-module |
| 24 | plugin-runtime | `.prompt-title` | obsidian-style-or-semantic-selector, reserved-module |

#### src/plugins/61-live-preview-mobile-plugin.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 204 | plugin-runtime | `.workspace-leaf-content[data-type="bookmarks"]` | obsidian-style-or-semantic-selector, reserved-module |
| 211 | plugin-runtime | `.workspace-leaf-content[data-type="bookmarks"] .tree-item-self` | obsidian-style-or-semantic-selector, reserved-module |
| 226 | plugin-runtime | `.bookmarks-view .tree-item-self.is-active` | obsidian-style-or-semantic-selector, reserved-module |
| 277 | plugin-runtime | `.markdown-preview-view iframe` | obsidian-style-or-semantic-selector, reserved-module |
| 277 | plugin-runtime | `.markdown-preview-view video` | obsidian-style-or-semantic-selector, reserved-module |
| 277 | plugin-runtime | `.markdown-reading-view iframe` | obsidian-style-or-semantic-selector, reserved-module |
| 277 | plugin-runtime | `.markdown-reading-view video` | obsidian-style-or-semantic-selector, reserved-module |
| 277 | plugin-runtime | `.markdown-rendered iframe` | obsidian-style-or-semantic-selector, reserved-module |

#### src/chrome/36-floating-ui-glass-system.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 772 | obsidian-chrome-runtime | `.workspace-leaf-content[data-type="search"] .search-empty-state` | obsidian-style-or-semantic-selector, reserved-module |
| 918 | obsidian-chrome-runtime | `.theme-dark .workspace-leaf-content[data-type="search"] .search-empty-state` | obsidian-style-or-semantic-selector, reserved-module |
| 127 | state-interaction | `body:not(.is-mobile) .metadata-container .metadata-property:is(:hover, :focus-within)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 131 | state-interaction | `body:not(.is-mobile).theme-dark .metadata-container .metadata-property:is(:hover, :focus-within)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 144 | state-interaction | `body:not(.is-mobile) :is(.canvas-control-item, .canvas-card-menu .clickable-icon):hover` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 201 | state-interaction | `body:not(.is-mobile) .modal .modal-close-button:is(:hover, :focus-visible)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 208 | state-interaction | `body:not(.is-mobile).theme-dark .modal .modal-close-button:is(:hover, :focus-visible)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 235 | state-interaction | `body:not(.is-mobile) .status-bar .status-bar-item-segment:hover` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |

#### src/chrome/35-editing-menu-tooltip-glass.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 349 | obsidian-chrome-runtime | `body:not(.is-mobile) :is(.view-header-breadcrumb-separator, .view-header-breadcrumb-separator span)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 384 | obsidian-chrome-runtime | `body:not(.is-mobile).theme-dark :is(.view-header-breadcrumb-separator, .view-header-breadcrumb-separator span)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 417 | obsidian-chrome-runtime | `body.mod-macos:not(.is-mobile) :is(.sidebar-toggle-button.mod-left, .sidebar-toggle-button.mod-right)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 421 | obsidian-chrome-runtime | `body.mod-macos:not(.is-mobile) :is(.sidebar-toggle-button.mod-left, .sidebar-toggle-button.mod-right)::after` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 461 | obsidian-chrome-runtime | `body:not(.is-mobile) .modal.mod-settings .vertical-tab-content .setting-item` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 461 | obsidian-chrome-runtime | `body:not(.is-mobile) .modal.mod-settings .vertical-tab-nav-item` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 484 | obsidian-chrome-runtime | `body:not(.is-mobile) .modal.mod-settings .vertical-tab-nav-item.is-active` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 503 | obsidian-chrome-runtime | `body:not(.is-mobile).theme-dark .modal.mod-settings .vertical-tab-nav-item.is-active` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |

#### src/plugins/60-canvas-graph-link-panes.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 79 | plugin-runtime | `.graph-view.color-circle` | obsidian-style-or-semantic-selector, reserved-module |
| 79 | plugin-runtime | `.graph-view.color-fill-highlight` | obsidian-style-or-semantic-selector, reserved-module |
| 83 | plugin-runtime | `.graph-view.color-arrow` | obsidian-style-or-semantic-selector, reserved-module |
| 87 | plugin-runtime | `.graph-view.color-arrow-highlight` | obsidian-style-or-semantic-selector, reserved-module |
| 87 | plugin-runtime | `.graph-view.color-line-highlight` | obsidian-style-or-semantic-selector, reserved-module |
| 101 | plugin-runtime | `.workspace-leaf-content[data-type="localgraph"] :is(.graph-controls, .graph-control-section, .graph-control-group)` | obsidian-style-or-semantic-selector, reserved-module |
| 117 | plugin-runtime | `.workspace-leaf-content[data-type="localgraph"] :is(.graph-control-button, .clickable-icon, button)` | obsidian-style-or-semantic-selector, reserved-module |
| 290 | plugin-runtime | `.theme-dark .graph-view.color-circle` | obsidian-style-or-semantic-selector, reserved-module |

#### src/chrome/31-navigation-tasks-search.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 116 | plugin-runtime | `.markdown-source-view.mod-cm6 .HyperMD-task-line[data-task]:not([data-task=" "])` | obsidian-style-or-semantic-selector, reserved-module |
| 119 | plugin-runtime | `.markdown-rendered li.task-list-item[data-task] input[type="checkbox"]` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 124 | plugin-runtime | `.markdown-rendered li.task-list-item[data-task="/"] input[type="checkbox"]` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 124 | plugin-runtime | `.markdown-rendered li.task-list-item[data-task=">"] input[type="checkbox"]` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 128 | plugin-runtime | `.markdown-rendered li.task-list-item[data-task="!"] input[type="checkbox"]` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 132 | plugin-runtime | `.markdown-rendered li.task-list-item[data-task="?"] input[type="checkbox"]` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 136 | plugin-runtime | `.markdown-rendered li.task-list-item[data-task="-"] input[type="checkbox"]` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 140 | plugin-runtime | `.markdown-rendered li.task-list-item[data-task="*"] input[type="checkbox"]` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |

#### src/chrome/33-settings-controls.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 223 | plugin-runtime | `body.css-settings-manager .style-settings-container .setting-item[data-id="ogd-accent"] .pickr .pcr-button` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 70 | state-interaction | `.modal .setting-item-control select option:focus` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 70 | state-interaction | `.modal .setting-item-control select option:hover` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 70 | state-interaction | `.setting-item-control select option:focus` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 70 | state-interaction | `.setting-item-control select option:hover` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 82 | state-interaction | `.setting-item-control .dropdown:focus-visible` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 82 | state-interaction | `.setting-item-control input:focus` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 82 | state-interaction | `.setting-item-control select:focus` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |

#### src/base/13-live-preview.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 714 | style-setting-class | `body.ogd-zebra-disabled-permanently .markdown-source-view.mod-cm6 :is(.cm-table-widget, table.cm-table) tbody tr:nth-child(even) td` | document-content-selector, obsidian-style-or-semantic-selector |
| 926 | style-setting-class | `body.theme-dark.ogd-spacing-relaxed .markdown-source-view.mod-cm6 .cm-line.HyperMD-codeblock` | document-content-selector, obsidian-style-or-semantic-selector |
| 946 | style-setting-class | `body.theme-dark.ogd-spacing-relaxed .markdown-source-view.mod-cm6 .cm-line.HyperMD-codeblock-begin` | document-content-selector, obsidian-style-or-semantic-selector |
| 953 | style-setting-class | `body.theme-dark.ogd-spacing-relaxed .markdown-source-view.mod-cm6 .cm-line.HyperMD-codeblock-end` | document-content-selector, obsidian-style-or-semantic-selector |
| 1023 | style-setting-class | `body.theme-dark.ogd-spacing-relaxed .markdown-source-view.mod-cm6` | document-content-selector, obsidian-style-or-semantic-selector |
| 1027 | style-setting-class | `body.theme-dark.ogd-spacing-relaxed .markdown-source-view.mod-cm6 :is(.cm-line.HyperMD-header-3, .cm-line.HyperMD-header-4)` | document-content-selector, obsidian-style-or-semantic-selector |
| 1031 | style-setting-class | `body.theme-dark.ogd-spacing-relaxed .markdown-source-view.mod-cm6 :is(.cm-header-3, .cm-header-4)` | document-content-selector, obsidian-style-or-semantic-selector |
| 1037 | style-setting-class | `body.theme-dark.ogd-spacing-relaxed .markdown-source-view.mod-cm6 :is(.cm-callout, .cm-embed-block.cm-callout, .cm-line.HyperMD-quote:not(.HyperMD-callout), .cm-table-widget, table.cm-table)` | document-content-selector, obsidian-style-or-semantic-selector |

#### src/features/42-report-print-polish.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 536 | print-pdf-context | `body .markdown-preview-view.markdown-rendered h3:first-of-type + .table-wrapper table tbody tr:nth-child(4) td:first-child` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 547 | print-pdf-context | `body .markdown-preview-view.markdown-rendered h3:first-of-type + .table-wrapper table tbody tr:nth-child(5) td:first-child` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 564 | print-pdf-context | `body .markdown-preview-view .table-wrapper + p:has(> strong:first-child)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 564 | print-pdf-context | `body .markdown-preview-view table + p:has(> strong:first-child)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 769 | print-pdf-context | `body :is(.markdown-rendered, .markdown-preview-view, .markdown-reading-view) hr` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 882 | print-pdf-context | `body.ogd-pdf-compact :is(.markdown-rendered, .markdown-preview-view.markdown-rendered, .markdown-reading-view .markdown-rendered) hr` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 883 | print-pdf-context | `body.ogd-pdf-compact :is(.markdown-rendered, .markdown-preview-view.markdown-rendered, .markdown-reading-view .markdown-rendered) .callout + hr` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 962 | print-pdf-context | `body.ogd-pdf-compact :is( .markdown-rendered, .markdown-preview-view.markdown-rendered, .markdown-reading-view .markdown-rendered ) table:is(.compact-table, .print-fit-table, .wide-table)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |

### Invalid Query Selectors

Invalid-query rows are query-coverage exclusions, not CSS syntax failures and not deletion evidence.

| Reason | Count | Meaning |
| --- | ---: | --- |
| pseudo-element-only-not-dom-queryable | 3 | The selector targets a pseudo-element only, so it has no DOM element to count with querySelectorAll(). |

| Module | Line | Selector part | Reason | Meaning |
| --- | ---: | --- | --- | --- |
| src/surfaces/20-reading-tables-code.css | 62 | `::selection` | pseudo-element-only-not-dom-queryable | The selector targets a pseudo-element only, so it has no DOM element to count with querySelectorAll(). |
| src/surfaces/22-reading-embeds-workspace.css | 222 | `::-webkit-scrollbar` | pseudo-element-only-not-dom-queryable | The selector targets a pseudo-element only, so it has no DOM element to count with querySelectorAll(). |
| src/surfaces/22-reading-embeds-workspace.css | 227 | `::-webkit-scrollbar-thumb` | pseudo-element-only-not-dom-queryable | The selector targets a pseudo-element only, so it has no DOM element to count with querySelectorAll(). |

## Module Summary

| Module | candidate | reserved | invalid-query | matched |
| --- | ---: | ---: | ---: | ---: |
| src/base/10-base-workspace.css | 0 | 7 | 0 | 47 |
| src/base/12-reading-content.css | 0 | 25 | 0 | 183 |
| src/base/13-live-preview.css | 0 | 31 | 0 | 179 |
| src/chrome/30-workspace.css | 0 | 51 | 0 | 133 |
| src/chrome/31-navigation-tasks-search.css | 0 | 32 | 0 | 35 |
| src/chrome/32-overlay-popover-dataview.css | 0 | 42 | 0 | 92 |
| src/chrome/33-settings-controls.css | 0 | 31 | 0 | 107 |
| src/chrome/34-nav-ribbon-glass.css | 0 | 19 | 0 | 14 |
| src/chrome/35-editing-menu-tooltip-glass.css | 0 | 40 | 0 | 67 |
| src/chrome/36-floating-ui-glass-system.css | 0 | 41 | 0 | 147 |
| src/chrome/37-tabs-file-explorer-search.css | 0 | 28 | 0 | 90 |
| src/features/41-feature-presets.css | 0 | 50 | 0 | 309 |
| src/features/42-report-print-polish.css | 0 | 31 | 0 | 350 |
| src/features/43-print-base.css | 0 | 23 | 0 | 99 |
| src/plugins/60-canvas-graph-link-panes.css | 0 | 38 | 0 | 112 |
| src/plugins/61-live-preview-mobile-plugin.css | 0 | 41 | 0 | 130 |
| src/surfaces/20-reading-tables-code.css | 0 | 27 | 1 | 251 |
| src/surfaces/21-reading-callouts-lists.css | 0 | 29 | 0 | 130 |
| src/surfaces/22-reading-embeds-workspace.css | 0 | 24 | 2 | 42 |
| src/surfaces/23-liquid-glass-core.css | 0 | 49 | 0 | 134 |
| src/surfaces/24-html-table-live-preview-glass.css | 0 | 15 | 0 | 86 |
| src/themes/50-dark.css | 0 | 21 | 0 | 143 |
| src/themes/51-accessibility-motion-contrast.css | 0 | 3 | 0 | 17 |
| src/tokens/00-light-tokens.css | 0 | 0 | 0 | 7 |
| src/tokens/01-dark-tokens.css | 0 | 1 | 0 | 6 |
