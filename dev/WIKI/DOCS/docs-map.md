# Docs Map

## Purpose Map

| Goal | Start Here | Then Check |
| --- | --- | --- |
| CSS bug fix | `dev/scripts/wiki_route.py <surface>` | owner contract, `WORKFLOWS/validation-matrix.md` |
| Runtime state issue | `runtime-evidence-template.md` | `runtime-evidence-schema.json`, relevant `RUNTIME/` guide |
| Style Settings option | `dev/scripts/wiki_route.py settings` | `MAP/settings-style-contract.md`, `DOCS/v3/style-settings-contract.md` |
| Unused CSS cleanup | `DOCS/v3/unused-css-roadmap.md` | `MAP/unused-css-candidates.md`, matching `RECIPES/coverage-*.md` |
| Plugin compatibility | `PLUGINS/coverage-matrix.md` | `PLUGINS/runtime-dom-notes.md`, `RUNTIME/plugins.md` |
| Release | `dev/scripts/wiki_route.py release` | `WORKFLOWS/release.md`, `DOCS/v3/release-plan.md` |
| Obsidian sync | `sync-obsidian.md` | `WORKFLOWS/release.md`, `dev/TEMP/last-sync.json` |
| WIKI/process change | `WORKFLOWS/wiki-maintenance.md` | `audit_wiki_consistency.py`, `audit_owner_risk_contracts.py` |

## Docs Routing

| Source | Use When | Notes |
| --- | --- | --- |
| `dev/WIKI/DOCS/v3/plugin-compatibility.md` | Plugin compatibility, supported plugin surfaces, known plugin caveats | Check before plugin-specific CSS changes. |
| `dev/WIKI/DOCS/v3/style-settings-contract.json` | Style Settings contract behavior | Check when changing settings contract or presets. |

## V3 Core Design And Cascade

| Source | Use When | Notes |
| --- | --- | --- |
| `dev/WIKI/DOCS/v3/design-spec.md` | Visual/design language, theme philosophy | Use before broad visual changes. |
| `dev/WIKI/DOCS/v3/cascade-research.md` | Cascade model, unlayered CSS rationale | Use before changing import order or specificity strategy. |
| `dev/WIKI/DOCS/v3/surface-state-matrix.md` | Surface states across UI patterns | Use before hover/active/focus surface changes. |
| `dev/WIKI/DOCS/v3/live-preview-editability.md` | Live Preview editability and CM6 behavior | Use before Live Preview source-mode changes. |

## Settings And Tokens

| Source | Use When | Notes |
| --- | --- | --- |
| `dev/WIKI/DOCS/v3/style-settings-contract.md` | User-facing Style Settings contract | Pair with `audit_style_settings_contract.py`. |
| `dev/WIKI/DOCS/v3/style-settings-contract.json` | Machine-readable settings contract | Do not handwave setting IDs/defaults. |
| `dev/WIKI/DOCS/v3/style-settings-presets.md` | Preset behavior and examples | Use before preset or customer-delivery changes. |
| `dev/WIKI/DOCS/v3/token-inventory.md` | Human-readable token inventory | Prefer tokens over repeated literal values. |
| `dev/WIKI/DOCS/v3/token-inventory.json` | Machine-readable token inventory | Use for token audits and automated checks. |

## Release And Change History

| Source | Use When | Notes |
| --- | --- | --- |
| `dev/WIKI/DOCS/v3/release-plan.md` | Release planning and scope | Check before version/release changes. |
| `dev/WIKI/DOCS/v3/release-notes-workflow.md` | Release notes process | Use before publishing release notes. |
| `dev/WIKI/DOCS/v3/feature-history.md` | Older feature intro archive | README should keep only the latest feature intros. |
| `dev/WIKI/DOCS/v3/unused-css-roadmap.md` | Cleanup roadmap | Use before removing candidate CSS. |

## Visual And Regression References

| Source | Use When | Notes |
| --- | --- | --- |
| `dev/WIKI/DOCS/v3/golden-image-scenarios.md` | Visual regression scenarios | Use before/after visual changes. |
| `dev/WIKI/DOCS/v3/visual-comparison-guide.md` | Comparing visual outputs | Use for screenshot review process. |
| `dev/WIKI/DOCS/v3/computed-fingerprint-v3.0.0-light.json` | Historical computed baseline | Use for fingerprint comparisons. |
| `dev/WIKI/DOCS/v3/computed-fingerprint-v3.0.0-dark.json` | Historical computed baseline | Use for fingerprint comparisons. |
| `dev/WIKI/DOCS/v3/pdf-marginalia-validation.md` | PDF marginalia validation | Pair with `pdf-header-footer-contract.md`. |
| `dev/WIKI/DOCS/v3/pdf-font-size-matrix.md` | PDF body/table/callout/code font-size policy and px conversion | Use before changing PDF readability presets. |

## Research Fixtures

| Source Family | Use When | Notes |
| --- | --- | --- |
| `dev/WIKI/DOCS/v3/research/table-callout-parity-fixture.html` | Table/callout parity checks | Useful before touching table/callout visual parity. |
| `dev/WIKI/DOCS/v3/research/chrome-ui-state-fixture.html` | Chrome, settings, overlay, and narrow state checks | Use before chrome/settings/overlay UX polish and visual state reviews. |
| `dev/WIKI/DOCS/v3/research/live-preview-pdf-parity-fixture.html` | LP/PDF parity checks | Use before cross-surface table/code/callout changes. |
| `dev/WIKI/DOCS/v3/research/pdf-heading-template-fixture.html` | 9-template PDF heading checks | Render with `audit_pdf_heading_templates.py --render`; review outputs under `dev/temp/pdf-heading-templates/`. |
| `dev/WIKI/DOCS/v3/research/pdf-marginalia-fixture.html` | PDF header/footer rendering | Use with PDF marginalia work. |
| `dev/WIKI/DOCS/v3/research/code-font-clarity-fixture.html` | Code font readability | Use before code block typography changes. |
| `dev/WIKI/DOCS/v3/research/coverage-priority-fixture.html` | Coverage priority fixture for plugin/chrome/settings/PDF selectors | Use before updating `MAP/unused-css-candidates.md` or `MAP/coverage-priority-plan.md`. |
| `dev/WIKI/DOCS/v3/research/*preview*.html/png` | Visual experiments | Treat as research references, not source owners. |
| `dev/WIKI/DOCS/v3/research/cascade-probe/*` | Cascade layer/unlayered experiments | Use before changing cascade strategy. |
| `dev/WIKI/DOCS/v3/research/golden-rig/obsidian-harness.html` | Harness for visual snapshots | Use for repeatable visual checks. |

## Editing Rule

If a docs file describes a behavior contract, update the matching MAP/WIKI workflow when the behavior changes. The retired `docs/v3` path must not be recreated; use `dev/WIKI/DOCS/v3`.
