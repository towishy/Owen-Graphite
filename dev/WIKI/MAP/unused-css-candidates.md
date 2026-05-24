# Unused CSS Candidate Report

Version: 3.1.58
Bundle SHA256: `48726f5c1349a53f9543c3a0b1a97724e4d78d2c40f335730e9ec4a6c3f4a4f8`
Coverage scenarios: 190

## Summary

| Classification | Count |
| --- | ---: |
| invalid-query | 3 |
| matched | 2943 |
| reserved | 829 |

## Candidate Selectors

No low-risk no-match selectors were found in the current coverage matrix.

## Reserved No-Match Selectors

Reserved no-match selectors: 829. These need purpose-built coverage before removal.

### Reserved Reason Summary

| Reason | Count |
| --- | ---: |
| obsidian-style-or-semantic-selector | 796 |
| document-content-selector | 524 |
| reserved-module | 488 |
| state-pseudo | 372 |
| reserved-at-context | 77 |
| token-or-variable | 1 |

### Reserved Bucket Summary

| Bucket | Count | Meaning | Recipe |
| --- | ---: | --- | --- |
| state-interaction | 372 | State pseudo selectors (:hover/:focus/etc.) that static DOM coverage cannot fully prove. | `dev/WIKI/RECIPES/coverage-state-interaction.md` |
| obsidian-chrome-runtime | 185 | Obsidian app chrome/runtime DOM such as workspace, nav, search, modal, menu, tooltip, or status surfaces. | `dev/WIKI/RECIPES/coverage-state-interaction.md` |
| plugin-runtime | 89 | Plugin/runtime DOM such as Canvas, Dataview, Mermaid, Graph, Bases, Pickr, or Editing Toolbar. | `dev/WIKI/RECIPES/coverage-plugin-runtime.md` |
| print-pdf-context | 79 | Print/PDF and PDF Style Settings selectors reserved for print-specific validation. | `dev/WIKI/RECIPES/coverage-print-pdf-context.md` |
| document-content-fixture-gap | 55 | Document/content semantics that need more purpose-built fixture DOM before removal review. | `dev/WIKI/RECIPES/coverage-document-content-fixture.md` |
| style-setting-class | 32 | Body-class Style Settings variants that are valid only under selected settings. | `OWNER-DECISION-TREE.md` |
| live-preview-runtime | 17 | CodeMirror/Live Preview runtime DOM and editor-generated classes. | `dev/WIKI/RECIPES/live-preview-spacing.md` |

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
| src/chrome/37-tabs-file-explorer-search.css | 85 | 66 | 19 | 103 | obsidian-chrome-runtime=62, state-interaction=19, plugin-runtime=3, print-pdf-context=1 | document-content-selector=85, obsidian-style-or-semantic-selector=85, reserved-module=85, state-pseudo=19 |
| src/chrome/32-overlay-popover-dataview.css | 60 | 10 | 50 | 92 | state-interaction=50, style-setting-class=6, plugin-runtime=4 | obsidian-style-or-semantic-selector=60, reserved-module=60, state-pseudo=50, document-content-selector=15 |
| src/features/41-feature-presets.css | 58 | 47 | 11 | 311 | print-pdf-context=22, plugin-runtime=12, state-interaction=11, style-setting-class=11 | obsidian-style-or-semantic-selector=58, document-content-selector=36, reserved-at-context=19, state-pseudo=11 |
| src/chrome/35-editing-menu-tooltip-glass.css | 56 | 29 | 27 | 89 | obsidian-chrome-runtime=28, state-interaction=27, plugin-runtime=1 | document-content-selector=56, obsidian-style-or-semantic-selector=56, reserved-module=56, state-pseudo=27 |
| src/chrome/33-settings-controls.css | 54 | 20 | 34 | 113 | state-interaction=34, obsidian-chrome-runtime=19, plugin-runtime=1 | obsidian-style-or-semantic-selector=54, reserved-module=54, state-pseudo=34, document-content-selector=24 |
| src/surfaces/23-liquid-glass-core.css | 53 | 22 | 31 | 125 | state-interaction=31, obsidian-chrome-runtime=22 | document-content-selector=53, obsidian-style-or-semantic-selector=53, state-pseudo=31 |
| src/chrome/30-workspace.css | 51 | 22 | 29 | 136 | state-interaction=29, plugin-runtime=10, obsidian-chrome-runtime=7, style-setting-class=5 | reserved-module=51, obsidian-style-or-semantic-selector=34, document-content-selector=32, state-pseudo=29 |
| src/chrome/36-floating-ui-glass-system.css | 43 | 4 | 39 | 152 | state-interaction=39, obsidian-chrome-runtime=4 | reserved-module=43, obsidian-style-or-semantic-selector=42, state-pseudo=39, document-content-selector=29 |
| src/plugins/61-live-preview-mobile-plugin.css | 42 | 19 | 23 | 147 | state-interaction=23, plugin-runtime=19 | reserved-module=42, obsidian-style-or-semantic-selector=40, state-pseudo=23, document-content-selector=9 |
| src/plugins/60-canvas-graph-link-panes.css | 38 | 14 | 24 | 112 | state-interaction=24, plugin-runtime=14 | reserved-module=38, obsidian-style-or-semantic-selector=36, state-pseudo=24 |
| src/chrome/31-navigation-tasks-search.css | 35 | 24 | 11 | 35 | plugin-runtime=24, state-interaction=11 | reserved-module=35, obsidian-style-or-semantic-selector=34, document-content-selector=22, state-pseudo=11 |
| src/features/42-report-print-polish.css | 32 | 32 | 0 | 357 | print-pdf-context=32 | document-content-selector=32, obsidian-style-or-semantic-selector=32, reserved-at-context=31 |

### Reserved Selector Samples

Representative no-match selectors from the largest hotspots. Static no-match selectors are shown before state-only hover/focus examples. These are examples for coverage planning, not removal approval.

#### src/chrome/37-tabs-file-explorer-search.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 642 | print-pdf-context | `body:not(.is-mobile) .workspace-leaf-content[data-type="file-explorer"] .nav-file-title[data-path$=".pdf" i] .nav-file-title-content::before` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 238 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-leaf-content[data-type="file-explorer"] .nav-file-tag` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 623 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-leaf-content[data-type="file-explorer"] .nav-file-title[data-path$=".mdx" i] .nav-file-title-content::before` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 624 | plugin-runtime | `body:not(.is-mobile) .workspace-leaf-content[data-type="file-explorer"] .nav-file-title[data-path$=".canvas" i] .nav-file-title-content::before` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 625 | plugin-runtime | `body:not(.is-mobile) .workspace-leaf-content[data-type="file-explorer"] .nav-file-title[data-path$=".excalidraw" i] .nav-file-title-content::before` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 626 | plugin-runtime | `body:not(.is-mobile) .workspace-leaf-content[data-type="file-explorer"] .nav-file-title:is([data-path$=".mmd" i], [data-path$=".mermaid" i]) .nav-file-title-content::before` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 627 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-leaf-content[data-type="file-explorer"] .nav-file-title[data-path$=".html" i] .nav-file-title-content::before` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 628 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-leaf-content[data-type="file-explorer"] .nav-file-title[data-path$=".xml" i] .nav-file-title-content::before` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |

#### src/chrome/32-overlay-popover-dataview.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 133 | style-setting-class | `body.ogd-zebra-disabled-permanently .block-language-dataview table tbody tr:nth-child(even) td` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 133 | style-setting-class | `body.ogd-zebra-disabled-permanently .markdown-rendered .dataview.dataview-table tbody tr:nth-child(even) td` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 133 | style-setting-class | `body.ogd-zebra-disabled-permanently .markdown-rendered .dataview.table-view-table tbody tr:nth-child(even) td` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 226 | style-setting-class | `body.theme-dark.ogd-zebra-disabled-permanently .block-language-dataview table tbody tr:nth-child(even) td` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 226 | style-setting-class | `body.theme-dark.ogd-zebra-disabled-permanently .markdown-rendered .dataview.dataview-table tbody tr:nth-child(even) td` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 226 | style-setting-class | `body.theme-dark.ogd-zebra-disabled-permanently .markdown-rendered .dataview.table-view-table tbody tr:nth-child(even) td` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 24 | plugin-runtime | `.modal-title` | obsidian-style-or-semantic-selector, reserved-module |
| 24 | plugin-runtime | `.prompt-title` | obsidian-style-or-semantic-selector, reserved-module |

#### src/features/41-feature-presets.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 423 | print-pdf-context | `body.ogd-pdf-segment-value-violet` | document-content-selector, obsidian-style-or-semantic-selector |
| 428 | print-pdf-context | `body.ogd-pdf-segment-value-rose` | document-content-selector, obsidian-style-or-semantic-selector |
| 433 | print-pdf-context | `body.ogd-pdf-segment-value-amber` | document-content-selector, obsidian-style-or-semantic-selector |
| 686 | print-pdf-context | `body.ogd-pdf-header-top-center:is(.ogd-pdf-label-segmented, .ogd-pdf-label-segmented-dual) .markdown-rendered::before` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 691 | print-pdf-context | `body.ogd-pdf-header-enabled.ogd-pdf-header-top-center:is(.ogd-pdf-label-segmented, .ogd-pdf-label-segmented-dual) .markdown-rendered::after` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 762 | print-pdf-context | `body.ogd-pdf-header-enabled.ogd-pdf-header-top-center:is(.ogd-pdf-label-segmented-dual, .ogd-pdf-label-segmented.ogd-pdf-header-dual-pair) .markdown-rendered::after` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 767 | print-pdf-context | `body.ogd-pdf-header-top-center:is(.ogd-pdf-label-segmented-dual, .ogd-pdf-label-segmented.ogd-pdf-header-dual-pair) .markdown-rendered::before` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 772 | print-pdf-context | `body.ogd-pdf-header-enabled.ogd-pdf-header-top-center:is(.ogd-pdf-label-segmented-dual, .ogd-pdf-label-segmented.ogd-pdf-header-dual-pair)::before` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |

#### src/chrome/35-editing-menu-tooltip-glass.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 333 | obsidian-chrome-runtime | `body:not(.is-mobile) :is(.view-header-breadcrumb-separator, .view-header-breadcrumb-separator span)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 368 | obsidian-chrome-runtime | `body:not(.is-mobile).theme-dark :is(.view-header-breadcrumb-separator, .view-header-breadcrumb-separator span)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 404 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-leaf-content` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 434 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-leaf-content > .view-header` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 443 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-leaf-content > .view-content` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 447 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-leaf-content > .view-content :is(.markdown-source-view.mod-cm6 .cm-scroller, .markdown-preview-view .markdown-preview-sizer, .markdown-reading-view .markdown-preview-sizer)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 456 | plugin-runtime | `body:not(.is-mobile) .editingToolbarModalBar` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 461 | obsidian-chrome-runtime | `body:not(.is-mobile).owen-editor-toolbar-top .owen-editor-glass-toolbar.mod-top` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |

#### src/chrome/33-settings-controls.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 39 | obsidian-chrome-runtime | `body.css-settings-manager .style-settings-container .setting-item.setting-item-heading` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 51 | obsidian-chrome-runtime | `body.css-settings-manager .style-settings-container .setting-item.setting-item-heading::before` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 55 | obsidian-chrome-runtime | `body.css-settings-manager .style-settings-container .setting-item.setting-item-heading .setting-item-info` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 55 | obsidian-chrome-runtime | `body:not(.is-mobile) .modal.mod-settings :is(.vertical-tab-content, .vertical-tab-content-container) .setting-item.setting-item-heading .setting-item-info` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 62 | obsidian-chrome-runtime | `body.css-settings-manager .style-settings-container .setting-item.setting-item-heading .setting-item-name` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 62 | obsidian-chrome-runtime | `body:not(.is-mobile) .modal.mod-settings :is(.vertical-tab-content, .vertical-tab-content-container) .setting-item.setting-item-heading .setting-item-name` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 173 | obsidian-chrome-runtime | `body.css-settings-manager :is(.style-settings-import, .style-settings-export, .style-settings-copy, .style-settings-download, .style-settings-import-label)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 173 | obsidian-chrome-runtime | `body:not(.is-mobile) .modal-style-settings :is(.style-settings-import, .style-settings-export, .style-settings-copy, .style-settings-download, .style-settings-import-label)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |

#### src/surfaces/23-liquid-glass-core.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 256 | obsidian-chrome-runtime | `body:not(.is-mobile) :is(.workspace-split.mod-left-split, .workspace-split.mod-right-split) .workspace-tab-header :is(.workspace-tab-header-inner, .workspace-tab-header-inner-icon)` | document-content-selector, obsidian-style-or-semantic-selector |
| 1329 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-tabs .workspace-tab-header :is(.workspace-tab-header-inner-close-button, .workspace-tab-header-inner-icon)` | document-content-selector, obsidian-style-or-semantic-selector |
| 1376 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .view-header` | document-content-selector, obsidian-style-or-semantic-selector |
| 1376 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-tab-header-container` | document-content-selector, obsidian-style-or-semantic-selector |
| 1384 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-tab-header-container` | document-content-selector, obsidian-style-or-semantic-selector |
| 1394 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-tabs .workspace-tab-header .workspace-tab-header-inner` | document-content-selector, obsidian-style-or-semantic-selector |
| 1417 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-tabs .workspace-tab-header.is-active` | document-content-selector, obsidian-style-or-semantic-selector |
| 1423 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-tabs .workspace-tab-header.is-active::after` | document-content-selector, obsidian-style-or-semantic-selector |

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

#### src/chrome/36-floating-ui-glass-system.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 275 | obsidian-chrome-runtime | `body:not(.is-mobile) .status-bar > :is(.status-bar-item, .status-bar-item-segment) :is(svg, .svg-icon, .clickable-icon, .status-bar-item-icon)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 293 | obsidian-chrome-runtime | `body:not(.is-mobile) .status-bar > .status-bar-item :is(.status-bar-item, .status-bar-item-segment)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 832 | obsidian-chrome-runtime | `.workspace-leaf-content[data-type="search"] .search-empty-state` | obsidian-style-or-semantic-selector, reserved-module |
| 978 | obsidian-chrome-runtime | `.theme-dark .workspace-leaf-content[data-type="search"] .search-empty-state` | obsidian-style-or-semantic-selector, reserved-module |
| 133 | state-interaction | `body:not(.is-mobile) .metadata-container .metadata-property:is(:hover, :focus-within)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 137 | state-interaction | `body:not(.is-mobile).theme-dark .metadata-container .metadata-property:is(:hover, :focus-within)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 150 | state-interaction | `body:not(.is-mobile) :is(.canvas-control-item, .canvas-card-menu .clickable-icon):hover` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 207 | state-interaction | `body:not(.is-mobile) .modal .modal-close-button:is(:hover, :focus-visible)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |

#### src/plugins/61-live-preview-mobile-plugin.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 97 | plugin-runtime | `.markdown-source-view.mod-cm6 .mermaid svg :is(.nodeLabel, .nodeLabel *, .edgeLabel :is(div, span, p), .label :is(div, span, p))` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 274 | plugin-runtime | `.workspace-leaf-content[data-type="bookmarks"]` | obsidian-style-or-semantic-selector, reserved-module |
| 281 | plugin-runtime | `.workspace-leaf-content[data-type="bookmarks"] .tree-item-self` | obsidian-style-or-semantic-selector, reserved-module |
| 296 | plugin-runtime | `.bookmarks-view .tree-item-self.is-active` | obsidian-style-or-semantic-selector, reserved-module |
| 347 | plugin-runtime | `.markdown-preview-view iframe` | obsidian-style-or-semantic-selector, reserved-module |
| 347 | plugin-runtime | `.markdown-preview-view video` | obsidian-style-or-semantic-selector, reserved-module |
| 347 | plugin-runtime | `.markdown-reading-view iframe` | obsidian-style-or-semantic-selector, reserved-module |
| 347 | plugin-runtime | `.markdown-reading-view video` | obsidian-style-or-semantic-selector, reserved-module |

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

#### src/features/42-report-print-polish.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 65 | print-pdf-context | `.markdown-source-view.mod-cm6 :is(.cm-html-embed, .cm-embed-block:not(.cm-callout):not(.cm-table-widget)) table.compact-table:not(.cm-table):not(.cm-table-widget)` | document-content-selector, obsidian-style-or-semantic-selector |
| 527 | print-pdf-context | `body .markdown-preview-view.markdown-rendered h3:first-of-type + .table-wrapper table tbody tr:nth-child(4) td:first-child` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 538 | print-pdf-context | `body .markdown-preview-view.markdown-rendered h3:first-of-type + .table-wrapper table tbody tr:nth-child(5) td:first-child` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 555 | print-pdf-context | `body .markdown-preview-view .table-wrapper + p:has(> strong:first-child)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 555 | print-pdf-context | `body .markdown-preview-view table + p:has(> strong:first-child)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 749 | print-pdf-context | `body :is(.markdown-rendered, .markdown-preview-view, .markdown-reading-view) hr` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 862 | print-pdf-context | `body.ogd-pdf-compact :is(.markdown-rendered, .markdown-preview-view.markdown-rendered, .markdown-reading-view .markdown-rendered) hr` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 863 | print-pdf-context | `body.ogd-pdf-compact :is(.markdown-rendered, .markdown-preview-view.markdown-rendered, .markdown-reading-view .markdown-rendered) .callout + hr` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |

### Invalid Query Selectors

Invalid-query rows are query-coverage exclusions, not CSS syntax failures and not deletion evidence.

| Reason | Count | Meaning |
| --- | ---: | --- |
| pseudo-element-only-not-dom-queryable | 3 | The selector targets a pseudo-element only, so it has no DOM element to count with querySelectorAll(). |

| Module | Line | Selector part | Reason | Meaning |
| --- | ---: | --- | --- | --- |
| src/surfaces/20-reading-tables-code.css | 62 | `::selection` | pseudo-element-only-not-dom-queryable | The selector targets a pseudo-element only, so it has no DOM element to count with querySelectorAll(). |
| src/surfaces/22-reading-embeds-workspace.css | 238 | `::-webkit-scrollbar` | pseudo-element-only-not-dom-queryable | The selector targets a pseudo-element only, so it has no DOM element to count with querySelectorAll(). |
| src/surfaces/22-reading-embeds-workspace.css | 243 | `::-webkit-scrollbar-thumb` | pseudo-element-only-not-dom-queryable | The selector targets a pseudo-element only, so it has no DOM element to count with querySelectorAll(). |

## Module Summary

| Module | candidate | reserved | invalid-query | matched |
| --- | ---: | ---: | ---: | ---: |
| src/base/10-base-workspace.css | 0 | 7 | 0 | 47 |
| src/base/12-reading-content.css | 0 | 25 | 0 | 183 |
| src/base/13-live-preview.css | 0 | 26 | 0 | 159 |
| src/chrome/30-workspace.css | 0 | 51 | 0 | 136 |
| src/chrome/31-navigation-tasks-search.css | 0 | 35 | 0 | 35 |
| src/chrome/32-overlay-popover-dataview.css | 0 | 60 | 0 | 92 |
| src/chrome/33-settings-controls.css | 0 | 54 | 0 | 113 |
| src/chrome/34-nav-ribbon-glass.css | 0 | 23 | 0 | 14 |
| src/chrome/35-editing-menu-tooltip-glass.css | 0 | 56 | 0 | 89 |
| src/chrome/36-floating-ui-glass-system.css | 0 | 43 | 0 | 152 |
| src/chrome/37-tabs-file-explorer-search.css | 0 | 85 | 0 | 103 |
| src/features/41-feature-presets.css | 0 | 58 | 0 | 311 |
| src/features/42-report-print-polish.css | 0 | 32 | 0 | 357 |
| src/features/43-print-base.css | 0 | 23 | 0 | 99 |
| src/plugins/60-canvas-graph-link-panes.css | 0 | 38 | 0 | 112 |
| src/plugins/61-live-preview-mobile-plugin.css | 0 | 42 | 0 | 147 |
| src/surfaces/20-reading-tables-code.css | 0 | 28 | 1 | 251 |
| src/surfaces/21-reading-callouts-lists.css | 0 | 29 | 0 | 130 |
| src/surfaces/22-reading-embeds-workspace.css | 0 | 25 | 2 | 44 |
| src/surfaces/23-liquid-glass-core.css | 0 | 53 | 0 | 125 |
| src/surfaces/24-html-table-live-preview-glass.css | 0 | 10 | 0 | 70 |
| src/themes/50-dark.css | 0 | 22 | 0 | 144 |
| src/themes/51-accessibility-motion-contrast.css | 0 | 3 | 0 | 17 |
| src/tokens/00-light-tokens.css | 0 | 0 | 0 | 7 |
| src/tokens/01-dark-tokens.css | 0 | 1 | 0 | 6 |
