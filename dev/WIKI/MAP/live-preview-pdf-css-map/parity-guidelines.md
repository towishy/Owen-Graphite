# Parity Guidelines

These rules should be followed when changing any CSS that affects both Live Preview and Export PDF.

## Golden Rule

Live Preview is the source of truth. Export PDF should follow the Live Preview result as closely as print constraints allow.

Do not assume that Reading View parity means Live Preview parity. Obsidian Live Preview has at least two separate DOM paths:

- source lines: `.cm-line.HyperMD-*`
- rendered widgets: `.cm-preview-code-block`, `.cm-hmd-codeblock`, `.cm-callout`, `.cm-table-widget`, `.cm-html-embed`, `.cm-embed-block`

PDF export uses rendered DOM under print media. A fix may need all three paths.

## Required Review Steps

1. Identify the visual feature and its DOM path: source line, rendered LP widget, Reading View, PDF export, or print-only marginalia.
2. Check whether the setting should be shared by token. If yes, put intent in `src/tokens/00-light-tokens.css` and `src/tokens/01-dark-tokens.css` first.
3. Map selectors explicitly:
   - LP source line selector.
   - LP rendered widget selector.
   - Reading/PDF selector.
   - Final print override if late screen rules can win.
4. Update `dev/WIKI/DOCS/v3/research/*fixture.html` or add a fixture when the change has visual risk.
5. Run the required audits.

## Live Preview Safety Rules

- Never add non-zero vertical `margin*` or `padding*` to direct `.cm-line.HyperMD-*` selectors.
- For visual spacing on direct codeblock lines, prefer `min-height` and `line-height`.
- Do not add `pointer-events: none` to `.cm-content` or top-level `.cm-line` surfaces.
- Do not add `outline`, heavy `box-shadow`, `transform`, or vertical padding to `.cm-active.cm-line`.
- Keep `.cm-embed-block` overflow changes compatible with `dev/WIKI/MAP/cm6-hit-routing-contract.md`.

## PDF Safety Rules

- Put print-only behavior inside `@media print`.
- When a screen rule touches `pre code`, tables, headings, or spacing, add a matching print guard in the relevant print owner if needed.
- `body.ogd-pdf-*` preset classes can outrank generic print rules. Match their specificity when closing print cascade.
- Do not use unsupported print margin boxes, `string-set`, generated multiline labels, fixed positioning, viewport units, or backdrop filters for PDF marginalia.
- Use `print-color-adjust: exact` for surfaces that must retain color.

## Codeblock Parity Pattern

Use this pattern for future codeblock work:

1. Tokens: `--ogd-code-*` and `--ogd-codeblock-*` define intent.
2. Reading/PDF: `pre`, `pre code`, `pre[class*="language-"]::before`, `pre[class*="language-"]::after` consume tokens.
3. Live Preview source lines: `.cm-line.HyperMD-codeblock*` consumes typography/color tokens but avoids vertical padding.
4. Live Preview rendered widgets: `.cm-preview-code-block pre`, `.cm-hmd-codeblock pre`, `.code-block-flair` consume the same header/surface tokens.
5. Syntax color parity maps both `.token.*` and `.cm-*` classes to the same `--ogd-code-*` variables.
6. Print typography must close both generic and preset-specific selectors, including `body:is(.ogd-pdf-font-comfortable, .ogd-pdf-font-large) ... pre code`.
7. Editable header titles are owned by the `owen-graphite-style-settings-l10n` compatibility-ID companion. It stores `title="..."` after the fence language token, uses `title=""` for an explicitly blank but clickable header, and must reject stale line updates rather than searching and rewriting a different block.
8. The Reading View trigger uses `.ogd-codeblock-title`; the Live Preview trigger augments Obsidian's `.code-block-flair` as `.ogd-codeblock-title-trigger`. Both keep the copy-action reservation on the right and consume the existing codeblock header height and typography tokens.

## Heading Template Parity Pattern

Style Settings option `ogd-heading-template` maps to body classes `ogd-heading-printclean`, `ogd-heading-keyline`, `ogd-heading-bracket`, `ogd-heading-quiet-ledger`, `ogd-heading-focus-bar`, `ogd-heading-double-rule`, `ogd-heading-tag-ribbon`, `ogd-heading-number-stamp`, and `ogd-heading-grid-index`.

Use this pattern for heading-template work:

1. Metadata: `src/features/40-style-settings.css` and `dev/WIKI/DOCS/v3/style-settings-contract.json` define the class-select values.
2. Reading View: `src/base/12-reading-content.css` owns rendered H1-H4 template surfaces.
3. Live Preview source lines: `src/base/13-live-preview.css` owns `.cm-header-1` through `.cm-header-4` inline parity only; do not add vertical margin or padding to direct `.cm-line.HyperMD-header-*` selectors.
4. PDF export: `src/features/43-print-base.css` owns print-safe H1-H4 template output.
5. Late closure: `src/features/41-feature-presets.css`, `src/features/42-report-print-polish.css`, and `src/themes/51-accessibility-motion-contrast.css` must not reset selected heading-template borders or pseudo rules.
6. Vertical accents are allowed only for explicitly selected heading templates and must remain scoped to `body.ogd-heading-*` selectors. Any H1/H2 surface carrying an accent line or frame must remain square; rounded corner plus accent line/frame combinations are forbidden.
7. CSS compatibility budget is 20,500 lines and 1,025,000 bytes after the 2026-07-24 direct-owner UI Foundation pass expanded the PDF, chrome, sidebar, and runtime-state surfaces. The gate's normalized UTF-8 metric is 20,353 lines and 991,905 bytes, retaining limited headroom; raw aqua, `!important`, `@layer`, and print compatibility budgets remain unchanged.
8. `ogd-heading-tag-ribbon` and `ogd-heading-grid-index` set `display: flex` on H1/H2 and repurpose `::before` as an in-flow flex item (ribbon/number-block shape) instead of the absolute-positioned kicker used by the other templates; PDF mirrors this with a static, hardcoded counter fallback (`content: "01"`) instead of `counter(ogd-h1-counter, ...)` to match the existing `ogd-heading-bracket`/`ogd-heading-focus-bar` print precedent.
9. Numeric H1 labels are template-specific. `ogd-heading-bracket`, `ogd-heading-focus-bar`, `ogd-heading-number-stamp`, and `ogd-heading-grid-index` must keep their H1 pseudo-content removed across Reading View and PDF; H2-H4 remain unlabeled accent markers.
10. `dev/scripts/audit_pdf_heading_templates.py --render` is the required print check for heading-template work. It validates computed geometry for all nine classes and writes reviewable PDFs, PNG previews, and a manifest under `dev/temp/pdf-heading-templates/`.

## Documentation Rule

When a visual feature is changed in one surface and expected to match another, update this MAP if any of these changed:

- root selector path
- owner file
- shared token name
- approved divergence rationale
- required fixture/audit command

## Minimum Validation Commands

```powershell
.\.venv\Scripts\python.exe dev\scripts\build_release.py
.\.venv\Scripts\python.exe dev\scripts\bundle_v3.py --check
.\.venv\Scripts\python.exe dev\scripts\audit_visual_quality_fixture.py
.\.venv\Scripts\python.exe dev\scripts\audit_lp_pdf_computed_styles.py
.\.venv\Scripts\python.exe dev\scripts\audit_v3_hit_routing.py
.\.venv\Scripts\python.exe dev\scripts\audit_css_compat_budget.py
```

If PDF marginalia, docs, or release packaging changed, also run:

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_docs_assets.py
.\.venv\Scripts\python.exe dev\scripts\audit_pdf_header_footer.py
.\.venv\Scripts\python.exe dev\scripts\audit_release_zip.py
```
