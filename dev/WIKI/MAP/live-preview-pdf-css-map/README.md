# Live Preview To Export PDF CSS MAP

This folder documents how Owen Graphite maps Obsidian Live Preview CSS to Export PDF CSS.

The goal is practical maintenance: when a visual setting is changed in Live Preview, this MAP should make it clear whether a matching PDF rule, token, fixture, or audit must also change.

## Documents

- `cascade-ownership.md`: import order, owner files, late-cascade rules, and known override points.
- `selector-mapping.md`: element-by-element mapping between Live Preview selectors and PDF selectors.
- `parity-guidelines.md`: rules for keeping both surfaces aligned without breaking CM6 hit routing or Chromium print.
- `future-improvements.md`: backlog for audits, fixtures, and refactors.
- `lp-pdf-css-map.json`: compact machine-readable index for future scripts or review tooling.

## Related Contracts

- `dev/WIKI/MAP/cm6-hit-routing-contract.md`
- `dev/WIKI/MAP/pdf-header-footer-contract.md`
- `dev/WIKI/MAP/css-stabilization-checklist.md`

## Working Model

Owen Graphite has three rendering surfaces that can look similar but are not the same DOM:

| Surface | Root | Typical CSS owner | Notes |
| --- | --- | --- | --- |
| Live Preview source lines | `.markdown-source-view.mod-cm6 .cm-line.HyperMD-*` | `src/base/13-live-preview.css` | Must preserve CM6 click routing. No vertical margin/padding on direct HyperMD lines. |
| Live Preview rendered widgets | `.markdown-source-view.mod-cm6 :is(.cm-preview-code-block, .cm-hmd-codeblock, .cm-callout, .cm-table-widget, .cm-html-embed)` | `src/base/13-live-preview.css`, `src/surfaces/23-liquid-glass-core.css`, `src/surfaces/24-html-table-live-preview-glass.css` | Looks close to Reading View but still lives inside CM6. |
| Export PDF | `@media print` + `.markdown-rendered` / `.markdown-preview-view.markdown-rendered` | `src/features/43-print-base.css`, `src/features/41-feature-presets.css`, `src/features/42-report-print-polish.css` | Chromium print has its own limitations. Final print fixes should stay in direct owner modules. |

The safest parity path is token first, selector second, fixture third:

1. Put shared intent in `--ogd-*` tokens.
2. Map Live Preview and PDF selectors to those tokens explicitly.
3. Add or update a visual fixture that covers both DOM paths.
4. Run hit-routing and print audits before release.
