# Future Improvements

This backlog focuses on making Live Preview and Export PDF parity easier to maintain.

## High Priority

1. Add a selector ownership audit.
   - Implemented: `dev/scripts/audit_lp_pdf_selector_ownership.py`
   - Inputs: `src/entry.css`, all imported `src/**/*.css` modules.
   - Output: selectors grouped by surface (`lp-source`, `lp-widget`, `reading`, `pdf-print`, `shared-token`), with optional JSON via `--json-output`.
   - Fails when direct `.cm-line.HyperMD-*` rules add forbidden vertical margin/padding outside the reviewed frontmatter/quote exceptions.
   - Included in `dev/scripts/release_check.py`.

2. Add a token parity audit.
   - Proposed script: `dev/scripts/audit_lp_pdf_token_parity.py`
   - Track `--ogd-code-*`, `--ogd-codeblock-*`, `--ogd-table-*`, `--ogd-pdf-*`, `--ogd-img-*`, `--ogd-figure-*`.
   - Report token status: `shared`, `lp-only`, `pdf-only`, `print-only-intentional`, `deprecated`.

3. Expand visual fixture contracts.
   - Keep `docs/v3/research/code-font-clarity-fixture.html` covering both `.token.*` and `.cm-*` syntax spans.
   - Implemented: `docs/v3/research/table-callout-parity-fixture.html` covers LP markdown table widget, LP HTML embed table, Reading View, and PDF table/callout paths.
   - Implemented: `dev/scripts/audit_lp_pdf_computed_styles.py` checks table/callout computed styles under screen and print media when Playwright is available.

4. Generate a selector map artifact.
   - Extend current MAP tooling to emit `dev/MAP/live-preview-pdf-css-map/generated-selector-index.json`.
   - Include selector, file, context, token references, specificity, import rank, and sensitive-contract tags.

## Medium Priority

1. Move shared codeblock contract comments closer to tokens.
   - Current ownership is split across tokens, surfaces, base LP, print polish, and late polish.
   - A short token block comment can reduce future accidental divergence.

2. Add per-feature parity notes to `docs/v3/golden-image-scenarios.md`.
   - Mark scenarios as `lp-source`, `lp-widget`, `reading`, `pdf`, or `cross-surface`.

3. Add a MAP freshness check.
   - If `src/base/13-live-preview.css`, `src/features/42-report-print-polish.css`, `src/features/43-print-base.css`, `src/surfaces/20-reading-tables-code.css`, or `src/surfaces/21-reading-callouts-lists.css` changes, require a human check of this folder.

4. Add a preset specificity checklist.
   - PDF preset classes such as `ogd-pdf-font-comfortable` can outrank generic print rules.
   - Future rules should record whether preset-specific print closure is required.

## Lower Priority

1. Add screenshots to this MAP folder.
   - Store tiny annotated PNGs only if they stay stable and do not bloat the repo.

2. Add a style-settings-to-selector generated table.
   - Parse `src/features/40-style-settings.css` and connect each class to its owner selectors.

3. Add a release checklist item.
   - Before release, check whether any cross-surface visual feature changed without MAP updates.

## Known Open Questions

- Should PDF export preview have an optional on-screen simulation class, or should it remain strictly print-only?
- Should LP widget codeblocks and source-line codeblocks share one named codeblock token contract, or should source-line geometry stay intentionally separate?
- How much visual difference is acceptable for callouts and tables where LP interactivity requires geometry constraints that PDF does not have?
