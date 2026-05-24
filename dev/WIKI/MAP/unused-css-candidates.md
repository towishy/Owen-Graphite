# Unused CSS Candidate Report

Version: 3.1.56
Bundle SHA256: `b41bae62035aa141a9985b0be58af31e8c902f46d8eb4aa030e1751cbde9d0b6`
Coverage scenarios: 33

## Summary

| Classification | Count |
| --- | ---: |
| invalid-query | 3 |
| matched | 2673 |
| reserved | 1067 |

## Candidate Selectors

No low-risk no-match selectors were found in the current coverage matrix.

## Reserved No-Match Selectors

Reserved no-match selectors: 1067. These need purpose-built coverage before removal.

### Reserved Reason Summary

| Reason | Count |
| --- | ---: |
| obsidian-style-or-semantic-selector | 1034 |
| document-content-selector | 777 |
| reserved-module | 488 |
| state-pseudo | 353 |
| reserved-at-context | 148 |
| token-or-variable | 1 |

### Reserved Bucket Summary

| Bucket | Count | Meaning |
| --- | ---: | --- |
| state-interaction | 353 | State pseudo selectors (:hover/:focus/etc.) that static DOM coverage cannot fully prove. |
| print-pdf-context | 237 | Print/PDF and PDF Style Settings selectors reserved for print-specific validation. |
| obsidian-chrome-runtime | 192 | Obsidian app chrome/runtime DOM such as workspace, nav, search, modal, menu, tooltip, or status surfaces. |
| style-setting-class | 119 | Body-class Style Settings variants that are valid only under selected settings. |
| plugin-runtime | 90 | Plugin/runtime DOM such as Canvas, Dataview, Mermaid, Graph, Bases, Pickr, or Editing Toolbar. |
| document-content-fixture-gap | 58 | Document/content semantics that need more purpose-built fixture DOM before removal review. |
| live-preview-runtime | 18 | CodeMirror/Live Preview runtime DOM and editor-generated classes. |

### Reserved Decision Policy

Current low-risk removal candidates: 0.
Reserved selectors are not deletion approval; each bucket below defines the required next validation step.

| Bucket | Decision | Next action |
| --- | --- | --- |
| state-interaction | do-not-remove | Validate through interactive state coverage or keep reserved. |
| print-pdf-context | do-not-remove | Validate through PDF/print scenario coverage before any removal review. |
| obsidian-chrome-runtime | runtime-reserved | Validate in Obsidian app chrome runtime or keep reserved. |
| style-setting-class | do-not-remove | Keep reserved unless the Style Settings contract removes the class. |
| plugin-runtime | runtime-reserved | Validate in Obsidian/plugin runtime or keep reserved. |
| document-content-fixture-gap | needs-purpose-built-fixture | Add natural document fixture coverage when real document evidence exists; otherwise keep as coverage backlog. |
| live-preview-runtime | runtime-reserved | Validate with CodeMirror/Live Preview runtime DOM or keep reserved. |

### Coverage Backlog Policy

- `document-content-fixture-gap`: Keep as coverage backlog unless a natural Obsidian document fixture can represent the selector without synthetic DOM overreach.
- `invalid-query`: Do not use invalid-query rows as deletion evidence; pseudo-element-only selectors and browser query limitations require manual or visual/context validation.

### Coverage Gap Hotspots

| Module | reserved | static | state | matched | Top buckets | Top reserved reasons |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| src/features/41-feature-presets.css | 221 | 209 | 12 | 148 | print-pdf-context=117, style-setting-class=78, state-interaction=12, plugin-runtime=12 | obsidian-style-or-semantic-selector=221, document-content-selector=199, reserved-at-context=27, state-pseudo=12 |
| src/features/42-report-print-polish.css | 87 | 87 | 0 | 302 | print-pdf-context=87 | document-content-selector=87, obsidian-style-or-semantic-selector=87, reserved-at-context=86 |
| src/chrome/37-tabs-file-explorer-search.css | 86 | 68 | 18 | 101 | obsidian-chrome-runtime=64, state-interaction=18, plugin-runtime=3, print-pdf-context=1 | document-content-selector=86, obsidian-style-or-semantic-selector=86, reserved-module=86, state-pseudo=18 |
| src/chrome/30-workspace.css | 59 | 30 | 29 | 125 | state-interaction=29, plugin-runtime=10, style-setting-class=10, obsidian-chrome-runtime=7 | reserved-module=59, obsidian-style-or-semantic-selector=42, document-content-selector=40, state-pseudo=29 |
| src/chrome/35-editing-menu-tooltip-glass.css | 56 | 29 | 27 | 89 | obsidian-chrome-runtime=28, state-interaction=27, plugin-runtime=1 | document-content-selector=56, obsidian-style-or-semantic-selector=56, reserved-module=56, state-pseudo=27 |
| src/chrome/33-settings-controls.css | 54 | 20 | 34 | 113 | state-interaction=34, obsidian-chrome-runtime=19, plugin-runtime=1 | obsidian-style-or-semantic-selector=54, reserved-module=54, state-pseudo=34, document-content-selector=24 |
| src/surfaces/23-liquid-glass-core.css | 54 | 23 | 31 | 124 | state-interaction=31, obsidian-chrome-runtime=22, document-content-fixture-gap=1 | document-content-selector=54, obsidian-style-or-semantic-selector=54, state-pseudo=31 |
| src/chrome/36-floating-ui-glass-system.css | 48 | 8 | 40 | 147 | state-interaction=40, obsidian-chrome-runtime=7, plugin-runtime=1 | reserved-module=48, obsidian-style-or-semantic-selector=47, state-pseudo=40, document-content-selector=34 |
| src/plugins/61-live-preview-mobile-plugin.css | 46 | 23 | 23 | 136 | state-interaction=23, plugin-runtime=19, print-pdf-context=4 | reserved-module=46, obsidian-style-or-semantic-selector=44, state-pseudo=23, document-content-selector=13 |
| src/chrome/32-overlay-popover-dataview.css | 42 | 10 | 32 | 92 | state-interaction=32, style-setting-class=6, plugin-runtime=4 | obsidian-style-or-semantic-selector=42, reserved-module=42, state-pseudo=32, document-content-selector=12 |
| src/base/13-live-preview.css | 39 | 32 | 7 | 146 | style-setting-class=22, live-preview-runtime=10, state-interaction=7 | obsidian-style-or-semantic-selector=39, document-content-selector=31, state-pseudo=7 |
| src/plugins/60-canvas-graph-link-panes.css | 38 | 14 | 24 | 112 | state-interaction=24, plugin-runtime=14 | reserved-module=38, obsidian-style-or-semantic-selector=36, state-pseudo=24 |

### Reserved Selector Samples

Representative no-match selectors from the largest hotspots. Static no-match selectors are shown before state-only hover/focus examples. These are examples for coverage planning, not removal approval.

#### src/features/41-feature-presets.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 20 | style-setting-class | `body.ogd-drop-cap .markdown-rendered > p:first-of-type::first-letter` | document-content-selector, obsidian-style-or-semantic-selector |
| 20 | style-setting-class | `body.ogd-drop-cap .markdown-rendered h1 + p::first-letter` | document-content-selector, obsidian-style-or-semantic-selector |
| 28 | style-setting-class | `body.ogd-indent-paragraph .markdown-rendered p` | document-content-selector, obsidian-style-or-semantic-selector |
| 34 | style-setting-class | `body.ogd-indent-paragraph .markdown-rendered .callout p` | document-content-selector, obsidian-style-or-semantic-selector |
| 34 | style-setting-class | `body.ogd-indent-paragraph .markdown-rendered :is(h1, h2, h3, h4, h5, h6) + p` | document-content-selector, obsidian-style-or-semantic-selector |
| 34 | style-setting-class | `body.ogd-indent-paragraph .markdown-rendered blockquote p` | document-content-selector, obsidian-style-or-semantic-selector |
| 34 | style-setting-class | `body.ogd-indent-paragraph .markdown-rendered li p` | document-content-selector, obsidian-style-or-semantic-selector |
| 41 | style-setting-class | `body.ogd-serif-body .markdown-rendered` | document-content-selector, obsidian-style-or-semantic-selector |

#### src/features/42-report-print-polish.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 65 | print-pdf-context | `.markdown-source-view.mod-cm6 :is(.cm-html-embed, .cm-embed-block:not(.cm-callout):not(.cm-table-widget)) table.compact-table:not(.cm-table):not(.cm-table-widget)` | document-content-selector, obsidian-style-or-semantic-selector |
| 527 | print-pdf-context | `body .markdown-preview-view.markdown-rendered h3:first-of-type + .table-wrapper table tbody tr:nth-child(4) td:first-child` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 538 | print-pdf-context | `body .markdown-preview-view.markdown-rendered h3:first-of-type + .table-wrapper table tbody tr:nth-child(5) td:first-child` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 555 | print-pdf-context | `body .markdown-preview-view .table-wrapper + p:has(> strong:first-child)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 555 | print-pdf-context | `body .markdown-preview-view table + p:has(> strong:first-child)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 592 | print-pdf-context | `body.ogd-pdf-screen-delivery` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 633 | print-pdf-context | `body.ogd-pdf-screen-delivery :is(.markdown-rendered, .markdown-preview-view.markdown-rendered, .markdown-reading-view .markdown-rendered)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |
| 633 | print-pdf-context | `body.ogd-pdf-screen-delivery :is(.markdown-rendered, .markdown-preview-view.markdown-rendered, .markdown-reading-view .markdown-rendered) :is(p, li, dd, dt, blockquote):not(table *)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context |

#### src/chrome/37-tabs-file-explorer-search.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 637 | print-pdf-context | `body:not(.is-mobile) .workspace-leaf-content[data-type="file-explorer"] .nav-file-title[data-path$=".pdf" i] .nav-file-title-content::before` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 42 | obsidian-chrome-runtime | `body:not(.is-mobile).ogd-glass-off` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 238 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-leaf-content[data-type="file-explorer"] .nav-file-tag` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 618 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-leaf-content[data-type="file-explorer"] .nav-file-title[data-path$=".mdx" i] .nav-file-title-content::before` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 619 | plugin-runtime | `body:not(.is-mobile) .workspace-leaf-content[data-type="file-explorer"] .nav-file-title[data-path$=".canvas" i] .nav-file-title-content::before` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 620 | plugin-runtime | `body:not(.is-mobile) .workspace-leaf-content[data-type="file-explorer"] .nav-file-title[data-path$=".excalidraw" i] .nav-file-title-content::before` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 621 | plugin-runtime | `body:not(.is-mobile) .workspace-leaf-content[data-type="file-explorer"] .nav-file-title:is([data-path$=".mmd" i], [data-path$=".mermaid" i]) .nav-file-title-content::before` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 622 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-leaf-content[data-type="file-explorer"] .nav-file-title[data-path$=".html" i] .nav-file-title-content::before` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |

#### src/chrome/30-workspace.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 462 | print-pdf-context | `body.ogd-print-avoid-breaks .markdown-rendered :is(.callout, blockquote, table, pre, figure, img, .mermaid, .markdown-embed)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context, reserved-module |
| 467 | print-pdf-context | `body.ogd-print-avoid-breaks .markdown-rendered :is(h2, h3, h4)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context, reserved-module |
| 472 | print-pdf-context | `body.ogd-print-avoid-breaks .markdown-rendered :is(h2, h3, h4) + :is(p, ul, ol, blockquote, .callout, table)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context, reserved-module |
| 556 | style-setting-class | `body.ogd-modern-tables .markdown-rendered table` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 563 | style-setting-class | `body.ogd-modern-tables .markdown-rendered table th` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 567 | style-setting-class | `body.ogd-modern-tables .markdown-rendered table td` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 579 | style-setting-class | `body.ogd-modern-tables .markdown-rendered table td:first-child` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 579 | style-setting-class | `body.ogd-modern-tables .markdown-rendered table th:first-child` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |

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
| 542 | document-content-fixture-gap | `body:not(.is-mobile).ogd-glass-off` | document-content-selector, obsidian-style-or-semantic-selector |
| 256 | obsidian-chrome-runtime | `body:not(.is-mobile) :is(.workspace-split.mod-left-split, .workspace-split.mod-right-split) .workspace-tab-header :is(.workspace-tab-header-inner, .workspace-tab-header-inner-icon)` | document-content-selector, obsidian-style-or-semantic-selector |
| 1329 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-tabs .workspace-tab-header :is(.workspace-tab-header-inner-close-button, .workspace-tab-header-inner-icon)` | document-content-selector, obsidian-style-or-semantic-selector |
| 1376 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .view-header` | document-content-selector, obsidian-style-or-semantic-selector |
| 1376 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-tab-header-container` | document-content-selector, obsidian-style-or-semantic-selector |
| 1384 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-tab-header-container` | document-content-selector, obsidian-style-or-semantic-selector |
| 1394 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-tabs .workspace-tab-header .workspace-tab-header-inner` | document-content-selector, obsidian-style-or-semantic-selector |
| 1417 | obsidian-chrome-runtime | `body:not(.is-mobile) .workspace-split.mod-root .workspace-tabs .workspace-tab-header.is-active` | document-content-selector, obsidian-style-or-semantic-selector |

#### src/chrome/36-floating-ui-glass-system.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 275 | obsidian-chrome-runtime | `body:not(.is-mobile) .status-bar > :is(.status-bar-item, .status-bar-item-segment) :is(svg, .svg-icon, .clickable-icon, .status-bar-item-icon)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 293 | obsidian-chrome-runtime | `body:not(.is-mobile) .status-bar > .status-bar-item :is(.status-bar-item, .status-bar-item-segment)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 496 | obsidian-chrome-runtime | `body:not(.is-mobile).ogd-glass-off` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 507 | obsidian-chrome-runtime | `body:not(.is-mobile).ogd-glass-off` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 533 | obsidian-chrome-runtime | `body:not(.is-mobile).ogd-glass-standard` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 638 | plugin-runtime | `body:not(.is-mobile).ogd-glass-off :is(.prompt, .modal, .popover.hover-popover, .notice, .notice-container .notice, #editingToolbarModalBar, .editingToolbarModalBar, .editingToolbarPopover, .editingToolbarPopoverItems, .editingToolbarSubmenu, .editingToolbarMenu)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 832 | obsidian-chrome-runtime | `.workspace-leaf-content[data-type="search"] .search-empty-state` | obsidian-style-or-semantic-selector, reserved-module |
| 978 | obsidian-chrome-runtime | `.theme-dark .workspace-leaf-content[data-type="search"] .search-empty-state` | obsidian-style-or-semantic-selector, reserved-module |

#### src/plugins/61-live-preview-mobile-plugin.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 394 | print-pdf-context | `body.ogd-print-avoid-breaks .markdown-preview-view :is(.markdown-embed, .internal-embed, iframe, video, audio)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context, reserved-module |
| 394 | print-pdf-context | `body.ogd-print-avoid-breaks .markdown-rendered :is(.markdown-embed, .internal-embed, iframe, video, audio)` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context, reserved-module |
| 399 | print-pdf-context | `body.ogd-print-avoid-breaks .markdown-preview-view .mermaid` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context, reserved-module |
| 399 | print-pdf-context | `body.ogd-print-avoid-breaks .markdown-rendered .mermaid` | document-content-selector, obsidian-style-or-semantic-selector, reserved-at-context, reserved-module |
| 91 | plugin-runtime | `.markdown-source-view.mod-cm6 .mermaid svg :is(.nodeLabel, .nodeLabel *, .edgeLabel :is(div, span, p), .label :is(div, span, p))` | document-content-selector, obsidian-style-or-semantic-selector, reserved-module |
| 267 | plugin-runtime | `.workspace-leaf-content[data-type="bookmarks"]` | obsidian-style-or-semantic-selector, reserved-module |
| 274 | plugin-runtime | `.workspace-leaf-content[data-type="bookmarks"] .tree-item-self` | obsidian-style-or-semantic-selector, reserved-module |
| 289 | plugin-runtime | `.bookmarks-view .tree-item-self.is-active` | obsidian-style-or-semantic-selector, reserved-module |

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

#### src/base/13-live-preview.css

| Line | Bucket | Selector part | Reasons |
| ---: | --- | --- | --- |
| 730 | style-setting-class | `body.ogd-spacing-relaxed .markdown-source-view.mod-cm6 .cm-line.HyperMD-header-2` | document-content-selector, obsidian-style-or-semantic-selector |
| 737 | style-setting-class | `body.ogd-spacing-relaxed .markdown-source-view.mod-cm6 .cm-line.HyperMD-header-3` | document-content-selector, obsidian-style-or-semantic-selector |
| 744 | style-setting-class | `body.ogd-spacing-relaxed .markdown-source-view.mod-cm6 .cm-line.HyperMD-header-4` | document-content-selector, obsidian-style-or-semantic-selector |
| 749 | style-setting-class | `body.ogd-spacing-relaxed .markdown-source-view.mod-cm6 .cm-header-2` | document-content-selector, obsidian-style-or-semantic-selector |
| 755 | style-setting-class | `body.ogd-spacing-relaxed .markdown-source-view.mod-cm6 .cm-header-3` | document-content-selector, obsidian-style-or-semantic-selector |
| 761 | style-setting-class | `body.ogd-spacing-relaxed .markdown-source-view.mod-cm6 .cm-header-4` | document-content-selector, obsidian-style-or-semantic-selector |
| 771 | style-setting-class | `body.ogd-spacing-relaxed .markdown-source-view.mod-cm6 .cm-line.HyperMD-quote:not(.HyperMD-callout)` | document-content-selector, obsidian-style-or-semantic-selector |
| 791 | style-setting-class | `body.ogd-spacing-relaxed .markdown-source-view.mod-cm6 .cm-line.HyperMD-callout` | document-content-selector, obsidian-style-or-semantic-selector |

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
| src/base/13-live-preview.css | 0 | 39 | 0 | 146 |
| src/chrome/30-workspace.css | 0 | 59 | 0 | 125 |
| src/chrome/31-navigation-tasks-search.css | 0 | 32 | 0 | 35 |
| src/chrome/32-overlay-popover-dataview.css | 0 | 42 | 0 | 92 |
| src/chrome/33-settings-controls.css | 0 | 54 | 0 | 113 |
| src/chrome/34-nav-ribbon-glass.css | 0 | 23 | 0 | 14 |
| src/chrome/35-editing-menu-tooltip-glass.css | 0 | 56 | 0 | 89 |
| src/chrome/36-floating-ui-glass-system.css | 0 | 48 | 0 | 147 |
| src/chrome/37-tabs-file-explorer-search.css | 0 | 86 | 0 | 101 |
| src/features/41-feature-presets.css | 0 | 221 | 0 | 148 |
| src/features/42-report-print-polish.css | 0 | 87 | 0 | 302 |
| src/features/43-print-base.css | 0 | 24 | 0 | 98 |
| src/plugins/60-canvas-graph-link-panes.css | 0 | 38 | 0 | 112 |
| src/plugins/61-live-preview-mobile-plugin.css | 0 | 46 | 0 | 136 |
| src/surfaces/20-reading-tables-code.css | 0 | 33 | 1 | 246 |
| src/surfaces/21-reading-callouts-lists.css | 0 | 29 | 0 | 130 |
| src/surfaces/22-reading-embeds-workspace.css | 0 | 25 | 2 | 44 |
| src/surfaces/23-liquid-glass-core.css | 0 | 54 | 0 | 124 |
| src/surfaces/24-html-table-live-preview-glass.css | 0 | 10 | 0 | 70 |
| src/themes/50-dark.css | 0 | 22 | 0 | 144 |
| src/themes/51-accessibility-motion-contrast.css | 0 | 3 | 0 | 17 |
| src/tokens/00-light-tokens.css | 0 | 3 | 0 | 4 |
| src/tokens/01-dark-tokens.css | 0 | 1 | 0 | 6 |
