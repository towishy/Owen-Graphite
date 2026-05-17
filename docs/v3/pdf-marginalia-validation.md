# PDF Marginalia Validation

This document records the lightweight validation baseline for Owen Graphite PDF header/footer marginalia.

## Fixture

- HTML fixture: `docs/v3/research/pdf-marginalia-fixture.html`
- Theme source loaded by fixture: `theme.css`
- DOM target: `.markdown-preview-view .markdown-rendered`
- Body classes: `theme-light ogd-pdf-header-enabled ogd-pdf-footer-enabled ogd-pdf-label-segmented ogd-pdf-label-badge ogd-pdf-header-key-graphite ogd-pdf-header-value-sky ogd-pdf-footer-key-rose ogd-pdf-footer-value-amber ogd-pdf-label-standard ogd-pdf-header-top-right`

## Current Baseline Checks

Run the fixture with print media emulation and verify:

| Check | Expected |
| --- | --- |
| Reading/screen media | header/footer generated content is not visible |
| Print media single-label header | `.markdown-rendered::before` resolves `--ogd-pdf-header-text` |
| Print media single-label footer | `.markdown-rendered > :last-child::after` resolves `--ogd-pdf-footer-text` |
| Print media segmented labels | key/value mode keeps adjacent segments on one line |
| Header geometry | `position:absolute`, top/right token geometry, no fixed positioning |
| Footer geometry | `position:absolute`, `left:50%`, `translateX(-50%)`, bottom offset token |
| Long text safety | `white-space:nowrap`, `overflow:hidden`, `text-overflow:ellipsis` |
| Footer reserve | final block keeps millimeter `margin-bottom` reserve |

## 2026-05-17 Fixture Result

Validated against `theme.css` after the `v3.1.36` Key/Value PDF marginalia UI and sizing update.

| Check | Result |
| --- | --- |
| Browser screen media | `::before` and `::after` generated content resolved to `none` |
| Browser print media header | key `"prepared by"` rendered Graphite and value `"Owen Graphite"` rendered Sky |
| Browser print media footer | key `"confidential"` rendered Rose and value `"internal use only"` rendered Amber |
| Segmented badge height | header about `24.9px`, footer about `25.4px`, giving the badge strip more presence than the first `22px` sample |
| Segmented spacing | header fixed segments are slightly narrower; footer key/value are content-sized around the center seam with measured seam gap `0px` |
| Header safety | absolute positioning, `nowrap`, hidden overflow, ellipsis confirmed |
| Footer safety | absolute positioning, centered seam, hidden overflow, ellipsis confirmed |
| Footer reserve | final block reserve resolved from `28mm` to browser pixels |
| Edge headless PDF | generated `dev/TEMP/pdf-marginalia-segmented-fixture.pdf` (`207937` bytes) |

The generated PDF is intentionally kept in `dev/TEMP` as a local validation artifact and is not part of the repository sync surface.

## Key/Value 1쌍 Mode

The product-safe key/value mode is limited to one adjacent key/value pair per surface:

```text
[ prepared by ][ Owen Graphite ]
[ confidential ][ internal use only ]
```

Style Settings model:

- `ogd-pdf-label-layout`: choose `단일 라벨` or `Key/Value 1쌍`.
- `ogd-pdf-header-text`: single-label text, or segmented key.
- `ogd-pdf-header-value`: segmented header value.
- `ogd-pdf-footer-text`: single-label text, or segmented key.
- `ogd-pdf-footer-value`: segmented footer value.
- `ogd-pdf-marginalia-style`: includes the `붙은 배지` sample style.
- `ogd-pdf-header-key-palette` / `ogd-pdf-header-value-palette`: choose the header key and value colors independently.
- `ogd-pdf-footer-key-palette` / `ogd-pdf-footer-value-palette`: choose the footer key and value colors independently, so footer classification can differ from the header.

## Footer Extra Sentence Feasibility

Adding a second footer input is safe only if it remains a single-line append to the existing footer label.

Difficulty: low to medium. The CSS itself is simple, but the project contract and audit script must be updated together so the feature does not reopen old PDF failures.

Recommended shape if implemented later:

```css
--ogd-pdf-footer-text: "Confidential";
--ogd-pdf-footer-note: "End of Document";
content: var(--ogd-pdf-footer-text, "") " - " var(--ogd-pdf-footer-note, "");
```

Avoid a second visual line. Multiline generated content (`\A`), extra footer pseudo anchors, page counters, margin boxes, and fixed positioning would reopen the Chromium PDF failure modes this contract is meant to prevent.

Implementation checklist if this feature is approved:

- Add `ogd-pdf-footer-note` as a `variable-text` Style Settings entry with `quotes: true`.
- Add `--ogd-pdf-footer-note: ""` to light tokens.
- Keep a single footer anchor pseudo and append the note inside the existing `content` declaration.
- Update `audit_pdf_header_footer.py` to allow the exact single-line append contract.
- Add one validation scenario for empty note, filled note, and long note clipping.

## Manual Obsidian Export Checks

When validating inside Obsidian, export the following notes to PDF after syncing the theme:

| Scenario | Expected |
| --- | --- |
| short note, header only | header appears once; screen view stays clean |
| long note, footer only | footer appears below final content only |
| table as final block | table does not overlap footer label |
| code block as final block | footer reserve remains outside code surface |
| list as final block | list markers do not affect footer label |
| long footer text | label stays one line and clips with ellipsis |
