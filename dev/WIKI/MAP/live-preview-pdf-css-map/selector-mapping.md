# Selector Mapping

Use this file when changing a visual feature in Live Preview or PDF. Find the feature row, update both sides when parity is expected, and record intentional differences when parity is not expected.

## Code Blocks

| Concern | Live Preview selector path | Export PDF selector path | Shared tokens / notes |
| --- | --- | --- | --- |
| Source-line codeblock text | `.markdown-source-view.mod-cm6 .cm-line.HyperMD-codeblock` | `.markdown-rendered pre code`, `.markdown-preview-view.markdown-rendered pre code` in `@media print` | `--ogd-code-font-family`, `--ogd-code-font-size`, `--ogd-code-print-font-size`, `--ogd-code-font-weight`, `--ogd-code-line-height`, `--ogd-code-print-line-height` |
| Source-line fence header | `.markdown-source-view.mod-cm6 .cm-line.HyperMD-codeblock-begin` and child `.cm-hmd-codeblock` | `pre[class*="language-"]::before`, `pre[class*="language-"]::after`, `.code-block-flair` | LP cannot use vertical padding on direct HyperMD lines. Use `min-height`/`line-height` only. |
| Rendered LP code widget | `.markdown-source-view.mod-cm6 :is(.cm-preview-code-block, .cm-hmd-codeblock) pre`, `.code-block-flair` | Same PDF `pre`/`code` print rules | This path is the common source of missed LP fixes because it is not a direct `.cm-line.HyperMD-codeblock`. |
| Syntax colors | `.cm-keyword`, `.cm-string`, `.cm-property`, `.cm-number`, `.cm-comment`, etc. | `.token.keyword`, `.token.string`, `.token.property`, plus `.cm-*` classes preserved in exported markup | Map both Prism `.token.*` and CodeMirror `.cm-*` classes to the same `--ogd-code-*` color tokens. |
| Code surface | LP line gradients and widget `pre` background | PDF `pre` background and print-safe borders | `--ogd-codeblock-bg`, `--ogd-codeblock-border`, `--ogd-codeblock-header-border`, `--ogd-codeblock-code-padding` |

## Tables

| Concern | Live Preview selector path | Export PDF selector path | Shared tokens / notes |
| --- | --- | --- | --- |
| Markdown table widget | `.markdown-source-view.mod-cm6 .cm-table-widget`, `table.cm-table` | `.markdown-rendered table`, `.markdown-preview-view table` in `@media print` | Live Preview is the baseline. PDF `print-fit-table`/`wide-table` should preserve LP-like padding, font size, and line-height unless page-fit requires a documented exception. |
| HTML table embed | `.markdown-source-view.mod-cm6 :is(.cm-html-embed, .cm-embed-block) table` | `.markdown-rendered table:is(.ogd-html-table, .wide-table, .print-fit-table, ...)` | LP table widgets must avoid unsafe overflow/margin combinations from the hit-routing contract. `dev/WIKI/DOCS/v3/research/table-callout-parity-fixture.html` covers this path separately from `.cm-table-widget`. |
| Header repetition | Not applicable to continuous LP | `thead { display: table-header-group; }` | Intentional PDF-only behavior. |
| Horizontal overflow | LP may use local scroll affordances | PDF uses wrapping/fit utilities | `print-fit-table`, `wrap-table`, `nowrap-code-table` require PDF fixture coverage. |

## Callouts

| Concern | Live Preview selector path | Export PDF selector path | Shared tokens / notes |
| --- | --- | --- | --- |
| Callout widget | `.markdown-source-view.mod-cm6 .cm-callout` | `.markdown-rendered .callout` in print | LP widgets cannot receive vertical margin that changes click geometry. |
| Source callout line | `.markdown-source-view.mod-cm6 .cm-line.HyperMD-callout` | No direct equivalent; PDF receives rendered callout DOM | Direct source-line rules are LP-only. Use rendered callout tokens for parity. |
| Icons and title rhythm | `.callout-title`, `.callout-icon`, CM6 widget descendants | `.markdown-rendered .callout-title`, `.callout-icon` in `@media print` | Print should be static; hover/active transitions are LP-only. |

Table and callout parity is covered by:

- `dev/WIKI/DOCS/v3/research/table-callout-parity-fixture.html`
- `dev/scripts/audit_visual_quality_fixture.py`
- `dev/scripts/audit_lp_pdf_computed_styles.py`

## Headings And Body Rhythm

| Concern | Live Preview selector path | Export PDF selector path | Shared tokens / notes |
| --- | --- | --- | --- |
| Headings | `.markdown-source-view.mod-cm6 .cm-line.HyperMD-header-*`, `.cm-header-*` | `.markdown-rendered h1` ... `h6` in `@media print` | LP controls editor line hitboxes; PDF controls page hierarchy and breaks. Do not force exact line-height parity. |
| Body text | `.markdown-source-view.mod-cm6 .cm-line` and rendered widgets | `.markdown-rendered p`, `.markdown-rendered li` | Use text tokens for color; allow PDF line-height to differ for print readability. |
| Page breaks | None | `page-break-before`, `page-break-after`, `page-break-inside` | Intentional PDF-only behavior. |

## Links, Images, And Figures

| Concern | Live Preview selector path | Export PDF selector path | Shared tokens / notes |
| --- | --- | --- | --- |
| Internal links | `.cm-hmd-internal-link`, `.markdown-rendered a.internal-link` | `.markdown-rendered a` in print | LP can use chips/hover; PDF must remain printable. |
| External link URLs | LP uses normal link affordance | `a[href^="http"]::after` for inline URL expansion unless clean/reference mode is active | Controlled by `ogd-pdf-link-mode`. |
| Images | `.markdown-rendered img`, embed widgets | `.markdown-rendered img`, `.ogd-figure-*`, `.ogd-img-*` in print | PDF owns sizing, object-fit, page-break, and caption flow more strongly. |
| Figures | Rendered DOM / embeds | `figure`, `figcaption`, `.ogd-figure-wide`, `.ogd-figure-compact`, `.ogd-figure-keep` | PDF utilities should be documented in fixture and scenario docs. |

## PDF Marginalia

PDF header/footer settings have no Live Preview parity target by design. They are print-only.

| Setting class | Owner | Notes |
| --- | --- | --- |
| `body.ogd-pdf-header-enabled` | `src/features/41-feature-presets.css` | Uses `.markdown-rendered::before` as print anchor. |
| `body.ogd-pdf-footer-enabled` | `src/features/41-feature-presets.css` | Uses `.markdown-rendered > :last-child::after` as print anchor. |
| `ogd-pdf-label-*`, `ogd-pdf-header-*`, `ogd-pdf-footer-*` | `src/features/41-feature-presets.css`, `src/tokens/*` | Must stay print-only unless a new preview contract is written. |
