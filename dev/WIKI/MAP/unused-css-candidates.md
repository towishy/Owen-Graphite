# Unused CSS Candidate Report

Version: 3.1.62
Bundle SHA256: `411721f6b4741416f0a8ee3792293507205580ce6ae18074a78f2c6a7efd854e`
Coverage scenarios: 201

## Summary

| Classification | Count |
| --- | ---: |
| invalid-query | 3 |
| matched | 3337 |
| reserved | 456 |

## Candidate Selectors

No low-risk no-match selectors were found in the current coverage matrix.

## Reserved No-Match Selectors

Reserved no-match selectors: 456. These need purpose-built coverage before removal.

### Reserved Reason Summary

| Reason | Count |
| --- | ---: |
| obsidian-style-or-semantic-selector | 428 |
| state-pseudo | 383 |
| reserved-module | 309 |
| document-content-selector | 260 |
| reserved-at-context | 5 |

### Reserved Bucket Summary

| Bucket | Count | Meaning | Recipe |
| --- | ---: | --- | --- |
| state-interaction | 383 | State pseudo selectors (:hover/:focus/etc.) that static DOM coverage cannot fully prove. | `dev/WIKI/RECIPES/coverage-state-interaction.md` |
| obsidian-chrome-runtime | 65 | Obsidian app chrome/runtime DOM such as workspace, nav, search, modal, menu, tooltip, or status surfaces. | `dev/WIKI/RECIPES/coverage-state-interaction.md` |
| live-preview-runtime | 8 | CodeMirror/Live Preview runtime DOM and editor-generated classes. | `dev/WIKI/RECIPES/live-preview-spacing.md` |

### Reserved Decision Policy

Current low-risk removal candidates: 0.
Reserved selectors are not deletion approval; each bucket below defines the required next validation step.

| Bucket | Decision | Next action |
| --- | --- | --- |
| state-interaction | do-not-remove | Validate through interactive state coverage or keep reserved. |
| obsidian-chrome-runtime | runtime-reserved | Validate in Obsidian app chrome runtime or keep reserved. |
| live-preview-runtime | runtime-reserved | Validate with CodeMirror/Live Preview runtime DOM or keep reserved. |

### Coverage Backlog Policy

- `document-content-fixture-gap`: Keep as coverage backlog unless a natural Obsidian document fixture can represent the selector without synthetic DOM overreach.
- `invalid-query`: Do not use invalid-query rows as deletion evidence; pseudo-element-only selectors and browser query limitations require manual or visual/context validation.

### Coverage Gap Hotspots

| Module | reserved | static | state | matched | Top buckets | Top reserved reasons |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| src/surfaces/23-liquid-glass-core.css | 53 | 18 | 35 | 129 | state-interaction=35, obsidian-chrome-runtime=18 | document-content-selector=53, obsidian-style-or-semantic-selector=53, state-pseudo=35 |
| src/chrome/32-overlay-popover-dataview.css | 50 | 0 | 50 | 102 | state-interaction=50 | obsidian-style-or-semantic-selector=50, reserved-module=50, state-pseudo=50, document-content-selector=9 |
| src/chrome/35-editing-menu-tooltip-glass.css | 45 | 18 | 27 | 100 | state-interaction=27, obsidian-chrome-runtime=18 | document-content-selector=45, obsidian-style-or-semantic-selector=45, reserved-module=45, state-pseudo=27 |
| src/chrome/33-settings-controls.css | 40 | 0 | 40 | 133 | state-interaction=40 | obsidian-style-or-semantic-selector=40, reserved-module=40, state-pseudo=40, document-content-selector=10 |
| src/chrome/36-floating-ui-glass-system.css | 39 | 0 | 39 | 156 | state-interaction=39 | reserved-module=39, state-pseudo=39, obsidian-style-or-semantic-selector=38, document-content-selector=27 |
| src/chrome/37-tabs-file-explorer-search.css | 37 | 18 | 19 | 151 | state-interaction=19, obsidian-chrome-runtime=18 | document-content-selector=37, obsidian-style-or-semantic-selector=37, reserved-module=37, state-pseudo=19 |
| src/chrome/30-workspace.css | 29 | 0 | 29 | 158 | state-interaction=29 | reserved-module=29, state-pseudo=29, document-content-selector=16, obsidian-style-or-semantic-selector=12 |
| src/plugins/60-canvas-graph-link-panes.css | 24 | 0 | 24 | 128 | state-interaction=24 | reserved-module=24, state-pseudo=24, obsidian-style-or-semantic-selector=22 |
| src/plugins/61-live-preview-mobile-plugin.css | 22 | 0 | 22 | 167 | state-interaction=22 | reserved-module=22, state-pseudo=22, obsidian-style-or-semantic-selector=20, document-content-selector=8 |
| src/surfaces/22-reading-embeds-workspace.css | 18 | 1 | 17 | 51 | state-interaction=17, obsidian-chrome-runtime=1 | state-pseudo=17, obsidian-style-or-semantic-selector=15 |
| src/base/13-live-preview.css | 16 | 8 | 8 | 180 | live-preview-runtime=8, state-interaction=8 | obsidian-style-or-semantic-selector=16, document-content-selector=12, state-pseudo=8 |
| src/features/41-feature-presets.css | 13 | 2 | 11 | 356 | state-interaction=11, obsidian-chrome-runtime=2 | obsidian-style-or-semantic-selector=13, state-pseudo=11, document-content-selector=4, reserved-at-context=1 |

### Reserved Selector Samples

Representative no-match selectors from the largest hotspots. Static no-match selectors are shown before state-only hover/focus examples. These are examples for coverage planning, not removal approval.

#### src/surfaces/23-liquid-glass-core.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 1373 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .view-header` | document-content-selector, obsidian-style-or-semantic-selector |
| 1373 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-tab-header-container` | document-content-selector, obsidian-style-or-semantic-selector |
| 1381 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-tab-header-container` | document-content-selector, obsidian-style-or-semantic-selector |
| 1391 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-tabs .workspace-tab-header .workspace-tab-header-inner` | document-content-selector, obsidian-style-or-semantic-selector |
| 1414 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-tabs .workspace-tab-header.is-active` | document-content-selector, obsidian-style-or-semantic-selector |
| 1420 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-tabs .workspace-tab-header.is-active::after` | document-content-selector, obsidian-style-or-semantic-selector |
| 1420 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-tabs .workspace-tab-header.is-active::before` | document-content-selector, obsidian-style-or-semantic-selector |
| 1437 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-tabs .workspace-tab-header.is-active .workspace-tab-header-inner` | document-content-selector, obsidian-style-or-semantic-selector |

#### src/chrome/32-overlay-popover-dataview.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 42 | state-interaction | `.modal input[type="search"]:focus-visible` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 42 | state-interaction | `.modal input[type="text"]:focus-visible` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 42 | state-interaction | `.modal textarea:focus-visible` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 42 | state-interaction | `.prompt-input:focus-visible` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 68 | state-interaction | `.menu-item:hover` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 138 | state-interaction | `.block-language-dataview table tr:hover td` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 138 | state-interaction | `.markdown-rendered .dataview.dataview-table tr:hover td` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 138 | state-interaction | `.markdown-rendered .dataview.table-view-table tr:hover td` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |

#### src/chrome/35-editing-menu-tooltip-glass.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 333 | obsidian-chrome-runtime | `body:not(.is-mobile) :is(.view-header-breadcrumb-separator, .view-header-breadcrumb-separator span)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 368 | obsidian-chrome-runtime | `body:not(.is-mobile).theme-dark :is(.view-header-breadcrumb-separator, .view-header-breadcrumb-separator span)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 434 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-leaf-content > .view-header` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 443 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-leaf-content > .view-content` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 447 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-leaf-content > .view-content :is(.markdown-source-view.mod-cm6 .cm-scroller, .markdown-preview-view .markdown-preview-sizer, .markdown-reading-view .markdown-preview-sizer)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 461 | obsidian-chrome-runtime | `body:not(.is-mobile).owen-editor-toolbar-top .owen-editor-glass-toolbar.mod-top` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 466 | obsidian-chrome-runtime | `body:not(.is-mobile).owen-editor-toolbar-bottom .owen-editor-glass-toolbar.mod-bottom` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 472 | obsidian-chrome-runtime | `body:not(.is-mobile).owen-editor-toolbar-offset.owen-editor-toolbar-top .workspace-leaf-content[data-type="markdown"] .markdown-reading-view .markdown-preview-sizer` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |

#### src/chrome/33-settings-controls.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 112 | state-interaction | `.modal .setting-item-control select option:focus` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 112 | state-interaction | `.modal .setting-item-control select option:hover` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 112 | state-interaction | `.setting-item-control select option:focus` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 112 | state-interaction | `.setting-item-control select option:hover` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 124 | state-interaction | `.setting-item-control .dropdown:focus-visible` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 124 | state-interaction | `.setting-item-control input:focus` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 124 | state-interaction | `.setting-item-control select:focus` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 124 | state-interaction | `.setting-item-control textarea:focus` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |

#### src/chrome/36-floating-ui-glass-system.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 133 | state-interaction | `body:not(.is-mobile) .metadata-container .metadata-property:is(:hover, :focus-within)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 137 | state-interaction | `body:not(.is-mobile).theme-dark .metadata-container .metadata-property:is(:hover, :focus-within)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 150 | state-interaction | `body:not(.is-mobile) :is(.canvas-control-item, .canvas-card-menu .clickable-icon):hover` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 207 | state-interaction | `body:not(.is-mobile) .modal .modal-close-button:is(:hover, :focus-visible)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 214 | state-interaction | `body:not(.is-mobile).theme-dark .modal .modal-close-button:is(:hover, :focus-visible)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 241 | state-interaction | `body:not(.is-mobile) .status-bar .status-bar-item-segment:hover` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 321 | state-interaction | `body:not(.is-mobile) .modal.mod-settings :is(.vertical-tab-content, .vertical-tab-content-container) .setting-item:is(:hover, :focus-within)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 321 | state-interaction | `body:not(.is-mobile) .modal.mod-settings :is(.vertical-tab-content, .vertical-tab-content-container) > .setting-item:is(:hover, :focus-within)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |

#### src/chrome/37-tabs-file-explorer-search.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 753 | obsidian-chrome-runtime | `body:not(.is-mobile) .nav-folder:has(.is-active) > .nav-folder-title[data-path*="/"]` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 759 | obsidian-chrome-runtime | `body:not(.is-mobile) .nav-folder:has(.is-active) > .nav-folder-title[data-path*="/"]::before` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 764 | obsidian-chrome-runtime | `body:not(.is-mobile) .nav-folder:has(.is-active) > .nav-folder-title[data-path*="/"] .nav-folder-title-content` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 769 | obsidian-chrome-runtime | `body:not(.is-mobile) .nav-folder:has(.is-active) > .nav-folder-title[data-path*="/"] .nav-folder-title-content::before` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 820 | obsidian-chrome-runtime | `body:not(.is-mobile).theme-dark .nav-folder:has(.is-active) > .nav-folder-title[data-path*="/"]` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 826 | obsidian-chrome-runtime | `body:not(.is-mobile).theme-dark .nav-folder:has(.is-active) > .nav-folder-title[data-path*="/"]::before` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 831 | obsidian-chrome-runtime | `body:not(.is-mobile).theme-dark .nav-folder:has(.is-active) > .nav-folder-title[data-path*="/"] .nav-folder-title-content` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 836 | obsidian-chrome-runtime | `body:not(.is-mobile).theme-dark .nav-folder:has(.is-active) > .nav-folder-title[data-path*="/"] .nav-folder-title-content::before` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |

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
| 188 | state-interaction | `.markdown-source-view.mod-cm6 .cm-embed-block:has(.mermaid) :is(.mermaid-controls, .mermaid-control, .mermaid-toolbar) :is(.mermaid-button, button, .clickable-icon):is(:hover, :focus-visible)` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 191 | state-interaction | `.markdown-source-view.mod-cm6 .cm-embed-block:has(.mermaid) :is(.mermaid-controls, .mermaid-control, .mermaid-toolbar) :is(.mermaid-button:not([class~="clickable-icon"]), button:not([class~="clickable-icon"])):active` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 288 | state-interaction | `.bookmarks-view .tree-item-self:hover` | reserved-module, state-pseudo |
| 288 | state-interaction | `.outline .tree-item-self:hover` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 288 | state-interaction | `.outline-view .tree-item-self:hover` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 288 | state-interaction | `.workspace-leaf-content[data-type="bookmarks"] .tree-item-self:hover` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 288 | state-interaction | `.workspace-leaf-content[data-type="outline"] .tree-item-self:hover` | obsidian-style-or-semantic-selector, reserved-module, state-pseudo |
| 330 | state-interaction | `.base-table tr:hover td` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module, state-pseudo |

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

#### src/base/13-live-preview.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 253 | live-preview-runtime | `body .markdown-source-view.mod-cm6 .cm-table-widget.markdown-rendered table.table-editor` | document-content-selector, obsidian-style-or-semantic-selector |
| 254 | live-preview-runtime | `body .markdown-source-view.mod-cm6 .cm-table-widget.markdown-rendered table.table-editor :is(thead, tbody, tr)` | document-content-selector, obsidian-style-or-semantic-selector |
| 255 | live-preview-runtime | `body .markdown-source-view.mod-cm6 .cm-table-widget.markdown-rendered table.table-editor :is(th, td)` | document-content-selector, obsidian-style-or-semantic-selector |
| 256 | live-preview-runtime | `body .markdown-source-view.mod-cm6 .cm-table-widget.markdown-rendered table.table-editor th` | document-content-selector, obsidian-style-or-semantic-selector |
| 258 | live-preview-runtime | `body.theme-dark .markdown-source-view.mod-cm6 .cm-table-widget.markdown-rendered table.table-editor` | document-content-selector, obsidian-style-or-semantic-selector |
| 259 | live-preview-runtime | `body.theme-dark .markdown-source-view.mod-cm6 .cm-table-widget.markdown-rendered table.table-editor :is(thead, tbody, tr)` | document-content-selector, obsidian-style-or-semantic-selector |
| 260 | live-preview-runtime | `body.theme-dark .markdown-source-view.mod-cm6 .cm-table-widget.markdown-rendered table.table-editor :is(th, td)` | document-content-selector, obsidian-style-or-semantic-selector |
| 261 | live-preview-runtime | `body.theme-dark .markdown-source-view.mod-cm6 .cm-table-widget.markdown-rendered table.table-editor th` | document-content-selector, obsidian-style-or-semantic-selector |

#### src/features/41-feature-presets.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 1070 | obsidian-chrome-runtime | `.workspace-tab-header[data-type="markdown"] .workspace-tab-header-inner-icon` | obsidian-style-or-semantic-selector |
| 1079 | obsidian-chrome-runtime | `.workspace-tab-header[data-type="image"] .workspace-tab-header-inner-icon` | obsidian-style-or-semantic-selector |
| 102 | state-interaction | `.markdown-rendered .callout:is([data-callout="secret"], [data-callout="hidden"]):hover .callout-content` | obsidian-style-or-semantic-selector, state-pseudo |
| 102 | state-interaction | `.markdown-rendered .ogd-blur:hover` | obsidian-style-or-semantic-selector, state-pseudo |
| 130 | state-interaction | `.markdown-rendered .footnote-ref a:hover` | obsidian-style-or-semantic-selector, state-pseudo |
| 130 | state-interaction | `.markdown-rendered a.footnote-link:hover` | obsidian-style-or-semantic-selector, state-pseudo |
| 149 | state-interaction | `.markdown-rendered img:not(.emoji):not(.callout-icon img):hover` | document-content-selector, obsidian-style-or-semantic-selector, state-pseudo |
| 1134 | state-interaction | `.block-language-dataview table tr:hover td` | document-content-selector, obsidian-style-or-semantic-selector, state-pseudo |

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
| src/base/12-reading-content.css | 0 | 10 | 0 | 198 |
| src/base/13-live-preview.css | 0 | 16 | 0 | 180 |
| src/chrome/30-workspace.css | 0 | 29 | 0 | 158 |
| src/chrome/31-navigation-tasks-search.css | 0 | 11 | 0 | 59 |
| src/chrome/32-overlay-popover-dataview.css | 0 | 50 | 0 | 102 |
| src/chrome/33-settings-controls.css | 0 | 40 | 0 | 133 |
| src/chrome/34-nav-ribbon-glass.css | 0 | 12 | 0 | 25 |
| src/chrome/35-editing-menu-tooltip-glass.css | 0 | 45 | 0 | 100 |
| src/chrome/36-floating-ui-glass-system.css | 0 | 39 | 0 | 156 |
| src/chrome/37-tabs-file-explorer-search.css | 0 | 37 | 0 | 151 |
| src/features/41-feature-presets.css | 0 | 13 | 0 | 356 |
| src/features/42-report-print-polish.css | 0 | 0 | 0 | 387 |
| src/features/43-print-base.css | 0 | 0 | 0 | 122 |
| src/plugins/60-canvas-graph-link-panes.css | 0 | 24 | 0 | 128 |
| src/plugins/61-live-preview-mobile-plugin.css | 0 | 22 | 0 | 167 |
| src/surfaces/20-reading-tables-code.css | 0 | 8 | 1 | 271 |
| src/surfaces/21-reading-callouts-lists.css | 0 | 3 | 0 | 156 |
| src/surfaces/22-reading-embeds-workspace.css | 0 | 18 | 2 | 51 |
| src/surfaces/23-liquid-glass-core.css | 0 | 53 | 0 | 129 |
| src/surfaces/24-html-table-live-preview-glass.css | 0 | 9 | 0 | 71 |
| src/themes/50-dark.css | 0 | 7 | 0 | 159 |
| src/themes/51-accessibility-motion-contrast.css | 0 | 3 | 0 | 17 |
| src/tokens/00-light-tokens.css | 0 | 0 | 0 | 7 |
| src/tokens/01-dark-tokens.css | 0 | 0 | 0 | 7 |
