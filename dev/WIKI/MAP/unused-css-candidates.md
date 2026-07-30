# Unused CSS Candidate Report

Version: 3.1.95
Bundle SHA256: `ad7d8509dddd7b664af414df269ecd5072a16396562a90db76cc930808e8c208`
Coverage scenarios: 207

## Summary

| Classification | Count |
| --- | ---: |
| invalid-query | 3 |
| matched | 3412 |
| reserved | 689 |

## Candidate Selectors

No low-risk no-match selectors were found in the current coverage matrix.

## Reserved No-Match Selectors

Reserved no-match selectors: 689. These need purpose-built coverage before removal.

### Reserved Reason Summary

| Reason | Count |
| --- | ---: |
| obsidian-style-or-semantic-selector | 649 |
| reserved-module | 505 |
| document-content-selector | 488 |
| state-pseudo | 430 |
| reserved-at-context | 17 |

### Reserved Bucket Summary

| Bucket | Count | Meaning | Recipe |
| --- | ---: | --- | --- |
| state-interaction | 430 | State pseudo selectors (:hover/:focus/etc.) that static DOM coverage cannot fully prove. | `dev/WIKI/RECIPES/coverage-state-interaction.md` |
| obsidian-chrome-runtime | 157 | Obsidian app chrome/runtime DOM such as workspace, nav, search, modal, menu, tooltip, or status surfaces. | `dev/WIKI/RECIPES/coverage-state-interaction.md` |
| plugin-runtime | 57 | Plugin/runtime DOM such as Canvas, Dataview, Mermaid, Graph, Bases, Pickr, or Editing Toolbar. | `dev/WIKI/RECIPES/coverage-plugin-runtime.md` |
| print-pdf-context | 26 | Print/PDF and PDF Style Settings selectors reserved for print-specific validation. | `dev/WIKI/RECIPES/coverage-print-pdf-context.md` |
| style-setting-class | 15 | Body-class Style Settings variants that are valid only under selected settings. | `OWNER-DECISION-TREE.md` |
| live-preview-runtime | 4 | CodeMirror/Live Preview runtime DOM and editor-generated classes. | `dev/WIKI/RECIPES/live-preview-spacing.md` |

### Reserved Decision Policy

Current low-risk removal candidates: 0.
Reserved selectors are not deletion approval; each bucket below defines the required next validation step.

| Bucket | Decision | Next action |
| --- | --- | --- |
| state-interaction | do-not-remove | Validate through interactive state coverage or keep reserved. |
| obsidian-chrome-runtime | runtime-reserved | Validate in Obsidian app chrome runtime or keep reserved. |
| plugin-runtime | runtime-reserved | Validate in Obsidian/plugin runtime or keep reserved. |
| print-pdf-context | do-not-remove | Validate through PDF/print scenario coverage before any removal review. |
| style-setting-class | do-not-remove | Keep reserved unless the Style Settings contract removes the class. |
| live-preview-runtime | runtime-reserved | Validate with CodeMirror/Live Preview runtime DOM or keep reserved. |

### Coverage Backlog Policy

- `document-content-fixture-gap`: Keep as coverage backlog unless a natural Obsidian document fixture can represent the selector without synthetic DOM overreach.
- `invalid-query`: Do not use invalid-query rows as deletion evidence; pseudo-element-only selectors and browser query limitations require manual or visual/context validation.

### Coverage Gap Hotspots

| Module | reserved | static | state | matched | Top buckets | Top reserved reasons |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| src/chrome/33-settings-controls.css | 186 | 119 | 67 | 138 | state-interaction=67, obsidian-chrome-runtime=55, plugin-runtime=52, print-pdf-context=12 | reserved-module=186, obsidian-style-or-semantic-selector=174, document-content-selector=152, state-pseudo=67 |
| src/chrome/37-tabs-file-explorer-search.css | 75 | 40 | 35 | 171 | obsidian-chrome-runtime=40, state-interaction=35 | document-content-selector=75, obsidian-style-or-semantic-selector=75, reserved-module=75, state-pseudo=35 |
| src/surfaces/23-liquid-glass-core.css | 67 | 23 | 44 | 124 | state-interaction=44, obsidian-chrome-runtime=23 | document-content-selector=67, obsidian-style-or-semantic-selector=67, state-pseudo=44 |
| src/chrome/35-editing-menu-tooltip-glass.css | 56 | 26 | 30 | 98 | state-interaction=30, obsidian-chrome-runtime=26 | document-content-selector=56, obsidian-style-or-semantic-selector=56, reserved-module=56, state-pseudo=30 |
| src/chrome/32-overlay-popover-dataview.css | 50 | 0 | 50 | 102 | state-interaction=50 | obsidian-style-or-semantic-selector=50, reserved-module=50, state-pseudo=50, document-content-selector=9 |
| src/chrome/36-floating-ui-glass-system.css | 35 | 2 | 33 | 156 | state-interaction=33, obsidian-chrome-runtime=2 | reserved-module=35, obsidian-style-or-semantic-selector=34, state-pseudo=33, document-content-selector=23 |
| src/chrome/30-workspace.css | 29 | 0 | 29 | 158 | state-interaction=29 | reserved-module=29, state-pseudo=29, document-content-selector=16, obsidian-style-or-semantic-selector=12 |
| src/plugins/60-canvas-graph-link-panes.css | 24 | 0 | 24 | 128 | state-interaction=24 | reserved-module=24, state-pseudo=24, obsidian-style-or-semantic-selector=22 |
| src/plugins/61-live-preview-mobile-plugin.css | 23 | 1 | 22 | 168 | state-interaction=22, plugin-runtime=1 | reserved-module=23, state-pseudo=22, obsidian-style-or-semantic-selector=21, document-content-selector=8 |
| src/base/13-live-preview.css | 20 | 12 | 8 | 218 | state-interaction=8, style-setting-class=6, live-preview-runtime=4, print-pdf-context=2 | obsidian-style-or-semantic-selector=20, document-content-selector=16, state-pseudo=8 |
| src/surfaces/22-reading-embeds-workspace.css | 18 | 1 | 17 | 51 | state-interaction=17, obsidian-chrome-runtime=1 | state-pseudo=17, obsidian-style-or-semantic-selector=15 |
| src/themes/50-dark.css | 18 | 12 | 6 | 159 | style-setting-class=9, state-interaction=6, print-pdf-context=2, obsidian-chrome-runtime=1 | obsidian-style-or-semantic-selector=18, document-content-selector=13, state-pseudo=6 |

### Reserved Selector Samples

Representative no-match selectors from the largest hotspots. Static no-match selectors are shown before state-only hover/focus examples. These are examples for coverage planning, not removal approval.

#### src/chrome/33-settings-controls.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 758 | print-pdf-context | `body.css-settings-manager .style-settings-heading[data-id="ogd-settings-pdf-marginalia"]` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 843 | print-pdf-context | `body.theme-dark.css-settings-manager .style-settings-heading[data-id="ogd-settings-pdf-marginalia"]` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 848 | print-pdf-context | `body.css-settings-manager .style-settings-heading[data-id="owen-graphite-document"] + .style-settings-container .setting-item[data-id="ogd-pdf-readability"]` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 852 | print-pdf-context | `html[lang^="ko"] body.css-settings-manager .style-settings-heading[data-id="owen-graphite-document"] + .style-settings-container .setting-item[data-id="ogd-pdf-readability"]` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 864 | print-pdf-context | `body.css-settings-manager .style-settings-heading[data-id="owen-graphite-document"] + .style-settings-container .setting-item[data-id="ogd-pdf-readability"] > .setting-item-info > .setting-item-description` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 873 | print-pdf-context | `body.css-settings-manager .style-settings-heading[data-id="owen-graphite-document"] + .style-settings-container .setting-item[data-id="ogd-pdf-readability"] > .setting-item-control` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 889 | print-pdf-context | `body.css-settings-manager .style-settings-heading[data-id="owen-graphite-document"] + .style-settings-container .setting-item[data-id="ogd-pdf-readability"] > .setting-item-control::before` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 919 | print-pdf-context | `body.css-settings-manager .style-settings-heading[data-id="owen-graphite-document"] + .style-settings-container .setting-item[data-id="ogd-pdf-readability"] > .setting-item-control::after` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |

#### src/chrome/37-tabs-file-explorer-search.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 316 | obsidian-chrome-runtime | `body:not(.is-mobile) .nav-folder-title.is-collapsed .nav-folder-title-content::before` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 401 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-leaf-content[data-type="file-explorer"] .nav-folder-children .nav-folder-children .nav-folder:has(> .nav-folder-title[data-path]):has(> .nav-folder-children > .nav-file .nav-file-title.is-active) > .nav-folder-children > .nav-file > .nav-file-title` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 407 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-leaf-content[data-type="file-explorer"] .nav-folder:has(> .nav-folder-title[data-path]):has(> .nav-folder-children > .nav-file .nav-file-title.is-active) > .nav-folder-children > .nav-file > .nav-file-title:not(.is-active) .nav-file-title-content` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 411 | obsidian-chrome-runtime | `body:not(.is-mobile) .nav-folder.mod-root > .nav-folder-children > .nav-folder + .nav-folder > .nav-folder-title` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 559 | obsidian-chrome-runtime | `body:not(.is-mobile).theme-dark .workspace-leaf-content[data-type="file-explorer"] .nav-folder:has(> .nav-folder-title[data-path]):has(> .nav-folder-children > .nav-file .nav-file-title.is-active) > .nav-folder-children > .nav-file > .nav-file-title:not(.is-active) .nav-file-title-content` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 751 | obsidian-chrome-runtime | `body:not(.is-mobile) .nav-folder:has(.is-active):not(:has(> .nav-folder-children > .nav-file .nav-file-title.is-active)) > .nav-folder-title[data-path]:not([data-path*="/"])` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 772 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-leaf-content[data-type="file-explorer"] .nav-folder:has(> .nav-folder-title[data-path]):has(> .nav-folder-children > .nav-file .nav-file-title.is-active) > .nav-folder-children > .nav-file > .nav-file-title:not(.is-active) .nav-file-title-content` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 801 | obsidian-chrome-runtime | `body:not(.is-mobile) .nav-folder:has(.is-active):not(:has(> .nav-folder-children > .nav-file .nav-file-title.is-active)) > .nav-folder-title[data-path]:not([data-path*="/"]) .nav-folder-title-content` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |

#### src/surfaces/23-liquid-glass-core.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 251 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-leaf-content[data-type="bookmarks"] > .view-content` | document-content-selector, obsidian-style-or-semantic-selector |
| 265 | obsidian-chrome-runtime | `body:not(.is-mobile) :is( .workspace-leaf-content[data-type="backlink"], .workspace-leaf-content[data-type="outgoing-link"], .workspace-leaf-content[data-type="outline"], .workspace-leaf-content[data-type="tag"], .workspace-leaf-content[data-type="all-properties"] ) > .view-content` | document-content-selector, obsidian-style-or-semantic-selector |
| 279 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-leaf-content[data-type="bookmarks"] .bookmarks-pane-empty` | document-content-selector, obsidian-style-or-semantic-selector |
| 1320 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .view-header` | document-content-selector, obsidian-style-or-semantic-selector |
| 1320 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-tab-header-container` | document-content-selector, obsidian-style-or-semantic-selector |
| 1328 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-tab-header-container` | document-content-selector, obsidian-style-or-semantic-selector |
| 1338 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-tabs .workspace-tab-header .workspace-tab-header-inner` | document-content-selector, obsidian-style-or-semantic-selector |
| 1362 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-tabs .workspace-tab-header.is-active` | document-content-selector, obsidian-style-or-semantic-selector |

#### src/chrome/35-editing-menu-tooltip-glass.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 341 | obsidian-chrome-runtime | `body:not(.is-mobile) :is(.view-header-breadcrumb-separator, .view-header-breadcrumb-separator span)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 376 | obsidian-chrome-runtime | `body:not(.is-mobile).theme-dark :is(.view-header-breadcrumb-separator, .view-header-breadcrumb-separator span)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 437 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-leaf-content > .view-header` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 446 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-leaf-content > .view-content` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 450 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-leaf-content > .view-content :is(.markdown-source-view.mod-cm6 .cm-scroller, .markdown-preview-view .markdown-preview-sizer, .markdown-reading-view .markdown-preview-sizer)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 464 | obsidian-chrome-runtime | `body:not(.is-mobile).owen-editor-toolbar-top .owen-editor-glass-toolbar.mod-top` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 469 | obsidian-chrome-runtime | `body:not(.is-mobile).owen-editor-toolbar-bottom .owen-editor-glass-toolbar.mod-bottom` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 478 | obsidian-chrome-runtime | `body:not(.is-mobile) .owen-editor-glass-toolbar` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |

#### src/chrome/32-overlay-popover-dataview.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 42 | state-interaction | `.modal input[type="search"]:not(.modal.owen-editor-palette-modal input[type="search"]):focus-visible` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 42 | state-interaction | `.modal input[type="text"]:focus-visible` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 42 | state-interaction | `.modal textarea:focus-visible` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 42 | state-interaction | `.prompt-input:focus-visible` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 68 | state-interaction | `.menu-item:hover` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 138 | state-interaction | `.block-language-dataview table tr:hover td` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 138 | state-interaction | `.markdown-rendered .dataview.dataview-table tr:hover td` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 138 | state-interaction | `.markdown-rendered .dataview.table-view-table tr:hover td` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |

#### src/chrome/36-floating-ui-glass-system.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 87 | obsidian-chrome-runtime | `body:not(.is-mobile) :is(.notice, .notice-container .notice) :is(.notice-message, .notice-content)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 93 | obsidian-chrome-runtime | `body:not(.is-mobile) .modal.owen-editor-palette-modal .owen-editor-command-detail-preview` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 139 | state-interaction | `body:not(.is-mobile) .metadata-container .metadata-property:is(:hover, :focus-within)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 143 | state-interaction | `body:not(.is-mobile).theme-dark .metadata-container .metadata-property:is(:hover, :focus-within)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 156 | state-interaction | `body:not(.is-mobile) :is(.canvas-control-item, .canvas-card-menu .clickable-icon):hover` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 198 | state-interaction | `body:not(.is-mobile) .modal .modal-close-button:is(:hover, :focus-visible)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 205 | state-interaction | `body:not(.is-mobile).theme-dark .modal .modal-close-button:is(:hover, :focus-visible)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 232 | state-interaction | `body:not(.is-mobile) .status-bar .status-bar-item-segment:hover` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |

#### src/chrome/30-workspace.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 28 | state-interaction | `.theme-dark .block-language-dataview table tr:hover td` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 28 | state-interaction | `.theme-dark .markdown-rendered .dataview.table-view-table tr:hover td` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 63 | state-interaction | `.theme-dark .kanban-plugin__item:hover` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 78 | state-interaction | `.theme-dark .bases-card:hover` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 135 | state-interaction | `.markdown-rendered a.internal-link:hover` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 147 | state-interaction | `.theme-dark .markdown-rendered a.internal-link:hover` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 164 | state-interaction | `.markdown-rendered pre[class*="language-"]:hover::after` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 256 | state-interaction | `input[data-task="x"]:checked` | reserved-module, state-pseudo |

#### src/plugins/60-canvas-graph-link-panes.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 27 | state-interaction | `.canvas-node:hover .canvas-node-container` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 27 | state-interaction | `.canvas-node:hover .canvas-node-content` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 51 | state-interaction | `.canvas-edge:hover .canvas-edge-path` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 51 | state-interaction | `.canvas-edges path:hover` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 70 | state-interaction | `.canvas-card-menu :is(.clickable-icon, .canvas-card-menu-button):hover` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 70 | state-interaction | `.canvas-control-item:hover` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 146 | state-interaction | `.backlink-pane .tree-item-self:hover` | reserved-module, state-pseudo |
| 146 | state-interaction | `.outgoing-link-pane .tree-item-self:hover` | reserved-module, state-pseudo |

#### src/plugins/61-live-preview-mobile-plugin.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 530 | plugin-runtime | `.is-mobile .owen-editor-glass-toolbar.is-mobile-compact .owen-editor-toolbar-button` | obsidian-style-or-semantic-selector, reserved-module |
| 188 | state-interaction | `.markdown-source-view.mod-cm6 .cm-embed-block:has(.mermaid) :is(.mermaid-controls, .mermaid-control, .mermaid-toolbar) :is(.mermaid-button, button, .clickable-icon):is(:hover, :focus-visible)` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 191 | state-interaction | `.markdown-source-view.mod-cm6 .cm-embed-block:has(.mermaid) :is(.mermaid-controls, .mermaid-control, .mermaid-toolbar) :is(.mermaid-button:not([class~="clickable-icon"]), button:not([class~="clickable-icon"])):active` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 288 | state-interaction | `.bookmarks-view .tree-item-self:hover` | reserved-module, state-pseudo |
| 288 | state-interaction | `.outline .tree-item-self:hover` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 288 | state-interaction | `.outline-view .tree-item-self:hover` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 288 | state-interaction | `.workspace-leaf-content[data-type="bookmarks"] .tree-item-self:hover` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 288 | state-interaction | `.workspace-leaf-content[data-type="outline"] .tree-item-self:hover` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |

#### src/base/13-live-preview.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 374 | print-pdf-context | `body.theme-dark:is(.ogd-heading-printclean, .ogd-heading-keyline, .ogd-heading-bracket, .ogd-heading-quiet-ledger, .ogd-heading-focus-bar, .ogd-heading-double-rule, .ogd-heading-tag-ribbon, .ogd-heading-number-stamp, .ogd-heading-grid-index) .markdown-source-view.mod-cm6` | document-content-selector, obsidian-style-or-semantic-selector |
| 379 | print-pdf-context | `body.theme-dark.ogd-heading-printclean .markdown-source-view.mod-cm6` | document-content-selector, obsidian-style-or-semantic-selector |
| 379 | style-setting-class | `body.theme-dark.ogd-heading-quiet-ledger .markdown-source-view.mod-cm6` | document-content-selector, obsidian-style-or-semantic-selector |
| 383 | style-setting-class | `body.theme-dark.ogd-heading-bracket .markdown-source-view.mod-cm6` | document-content-selector, obsidian-style-or-semantic-selector |
| 387 | style-setting-class | `body.theme-dark.ogd-heading-double-rule .markdown-source-view.mod-cm6` | document-content-selector, obsidian-style-or-semantic-selector |
| 391 | style-setting-class | `body.theme-dark.ogd-heading-tag-ribbon .markdown-source-view.mod-cm6` | document-content-selector, obsidian-style-or-semantic-selector |
| 396 | style-setting-class | `body.theme-dark.ogd-heading-number-stamp .markdown-source-view.mod-cm6` | document-content-selector, obsidian-style-or-semantic-selector |
| 400 | style-setting-class | `body.theme-dark.ogd-heading-grid-index .markdown-source-view.mod-cm6` | document-content-selector, obsidian-style-or-semantic-selector |

#### src/surfaces/22-reading-embeds-workspace.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 167 | obsidian-chrome-runtime | `.markdown-source-view.mod-cm6 .cm-hmd-internal-link .cm-formatting-link` | obsidian-style-or-semantic-selector |
| 234 | state-interaction | `.cm-content:focus` | obsidian-style-or-semantic-selector, state-pseudo |
| 234 | state-interaction | `.cm-content:focus-visible` | obsidian-style-or-semantic-selector, state-pseudo |
| 234 | state-interaction | `.cm-editor:focus` | obsidian-style-or-semantic-selector, state-pseudo |
| 234 | state-interaction | `.cm-editor:focus-visible` | obsidian-style-or-semantic-selector, state-pseudo |
| 234 | state-interaction | `.cm-scroller:focus` | obsidian-style-or-semantic-selector, state-pseudo |
| 234 | state-interaction | `.cm-scroller:focus-visible` | obsidian-style-or-semantic-selector, state-pseudo |
| 234 | state-interaction | `.markdown-reading-view:focus` | obsidian-style-or-semantic-selector, state-pseudo |

#### src/themes/50-dark.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 208 | print-pdf-context | `body.theme-dark:is(.ogd-heading-printclean, .ogd-heading-keyline, .ogd-heading-bracket, .ogd-heading-quiet-ledger, .ogd-heading-focus-bar, .ogd-heading-double-rule, .ogd-heading-tag-ribbon, .ogd-heading-number-stamp, .ogd-heading-grid-index) :is(.markdown-rendered, .markdown-preview-view.markdown-rendered, .markdown-reading-view .markdown-rendered)` | document-content-selector, obsidian-style-or-semantic-selector |
| 216 | print-pdf-context | `body.theme-dark.ogd-heading-printclean :is(.markdown-rendered, .markdown-preview-view.markdown-rendered, .markdown-reading-view .markdown-rendered)` | document-content-selector, obsidian-style-or-semantic-selector |
| 216 | style-setting-class | `body.theme-dark.ogd-heading-quiet-ledger :is(.markdown-rendered, .markdown-preview-view.markdown-rendered, .markdown-reading-view .markdown-rendered)` | document-content-selector, obsidian-style-or-semantic-selector |
| 223 | style-setting-class | `body.theme-dark.ogd-heading-bracket :is(.markdown-rendered, .markdown-preview-view.markdown-rendered, .markdown-reading-view .markdown-rendered)` | document-content-selector, obsidian-style-or-semantic-selector |
| 223 | style-setting-class | `body.theme-dark.ogd-heading-focus-bar :is(.markdown-rendered, .markdown-preview-view.markdown-rendered, .markdown-reading-view .markdown-rendered)` | document-content-selector, obsidian-style-or-semantic-selector |
| 223 | style-setting-class | `body.theme-dark.ogd-heading-keyline :is(.markdown-rendered, .markdown-preview-view.markdown-rendered, .markdown-reading-view .markdown-rendered)` | document-content-selector, obsidian-style-or-semantic-selector |
| 228 | style-setting-class | `body.theme-dark.ogd-heading-bracket :is(.markdown-rendered, .markdown-preview-view.markdown-rendered, .markdown-reading-view .markdown-rendered)` | document-content-selector, obsidian-style-or-semantic-selector |
| 233 | style-setting-class | `body.theme-dark.ogd-heading-double-rule :is(.markdown-rendered, .markdown-preview-view.markdown-rendered, .markdown-reading-view .markdown-rendered)` | document-content-selector, obsidian-style-or-semantic-selector |

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
| src/base/10-base-workspace.css | 0 | 7 | 0 | 49 |
| src/base/12-reading-content.css | 0 | 10 | 0 | 268 |
| src/base/13-live-preview.css | 0 | 20 | 0 | 218 |
| src/chrome/30-workspace.css | 0 | 29 | 0 | 158 |
| src/chrome/31-navigation-tasks-search.css | 0 | 15 | 0 | 59 |
| src/chrome/32-overlay-popover-dataview.css | 0 | 50 | 0 | 102 |
| src/chrome/33-settings-controls.css | 0 | 186 | 0 | 138 |
| src/chrome/34-nav-ribbon-glass.css | 0 | 12 | 0 | 25 |
| src/chrome/35-editing-menu-tooltip-glass.css | 0 | 56 | 0 | 98 |
| src/chrome/36-floating-ui-glass-system.css | 0 | 35 | 0 | 156 |
| src/chrome/37-tabs-file-explorer-search.css | 0 | 75 | 0 | 171 |
| src/features/41-feature-presets.css | 0 | 17 | 0 | 331 |
| src/features/42-report-print-polish.css | 0 | 0 | 0 | 319 |
| src/features/43-print-base.css | 0 | 6 | 0 | 177 |
| src/plugins/60-canvas-graph-link-panes.css | 0 | 24 | 0 | 128 |
| src/plugins/61-live-preview-mobile-plugin.css | 0 | 23 | 0 | 168 |
| src/surfaces/20-reading-tables-code.css | 0 | 8 | 1 | 271 |
| src/surfaces/21-reading-callouts-lists.css | 0 | 3 | 0 | 157 |
| src/surfaces/22-reading-embeds-workspace.css | 0 | 18 | 2 | 51 |
| src/surfaces/23-liquid-glass-core.css | 0 | 67 | 0 | 124 |
| src/surfaces/24-html-table-live-preview-glass.css | 0 | 5 | 0 | 52 |
| src/themes/50-dark.css | 0 | 18 | 0 | 159 |
| src/themes/51-accessibility-motion-contrast.css | 0 | 5 | 0 | 19 |
| src/tokens/00-light-tokens.css | 0 | 0 | 0 | 7 |
| src/tokens/01-dark-tokens.css | 0 | 0 | 0 | 7 |
