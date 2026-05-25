# WIKI Route Registry

Generated from `dev/WIKI/MAP/route-registry.json`.

## Common Reading

- `dev/WIKI/README.md`
- `dev/WIKI/CORE-PRINCIPLES.md`
- `dev/WIKI/QUICK-ROUTING.md`

## Routes

| Route | Owner | Owner Surfaces | Checks |
| --- | --- | --- | --- |
| `chrome` | src/chrome/* according to dev/WIKI/SRC/chrome.md | `workspace-chrome`, `overlay-menu-search` | `dev/scripts/audit_core_principles.py`, `dev/scripts/release_check.py --skip-bundle` |
| `docs` | dev/WIKI/DOCS/*, README files, screenshots/readme/* by publication target | n/a | `dev/scripts/audit_docs_assets.py`, `dev/scripts/audit_readme_svg_layout.py` |
| `live-preview` | src/base/13-live-preview.css | `live-preview-cm6`, `live-preview-rendered-widgets` | `dev/scripts/audit_v3_hit_routing.py`, `dev/scripts/audit_core_principles.py` |
| `mobile` | src/chrome/30-workspace.css for general mobile layout; src/plugins/61-live-preview-mobile-plugin.css for plugin/mobile embeds | `mobile-narrow-layout` | `dev/scripts/audit_core_principles.py`, `dev/scripts/release_check.py --skip-bundle` |
| `pdf` | src/features/41-feature-presets.css, src/features/42-report-print-polish.css, or src/features/43-print-base.css by surface | `pdf-base`, `pdf-report-polish`, `pdf-marginalia` | `dev/scripts/audit_pdf_header_footer.py`, `dev/scripts/release_check.py --skip-bundle` |
| `plugin` | src/plugins/* for plugin-specific DOM; Dataview tables/inline fields currently route to src/chrome/32-overlay-popover-dataview.css; core document geometry stays with core owners | `dataview-plugin-support` | `dev/scripts/audit_core_principles.py`, `dev/scripts/release_check.py --skip-bundle` |
| `release` | manifest.json, CHANGELOG.md, README.md, dev/WIKI/DOCS/v3/release-plan.md, dev/scripts/build_release.py | n/a | `dev/scripts/release_check.py --tag <version>`, `dev/scripts/audit_release_zip.py` |
| `settings` | src/chrome/33-settings-controls.css for settings UI controls; src/features/40-style-settings.css and dev/WIKI/DOCS/v3/style-settings-contract.json for Style Settings metadata | `settings-controls`, `style-settings-contract` | `dev/scripts/audit_style_settings_contract.py`, `dev/scripts/audit_core_principles.py`, `dev/scripts/release_check.py --skip-bundle` |
| `table` | Rendered: src/surfaces/20-reading-tables-code.css; LP HTML: src/base/13-live-preview.css + src/surfaces/24-html-table-live-preview-glass.css; LP markdown widget: Obsidian core | `reading-typography`, `reading-tables-code`, `reading-callouts-lists`, `live-preview-rendered-widgets` | `dev/scripts/audit_direct_owner_guard.py`, `dev/scripts/audit_v3_hit_routing.py`, `dev/scripts/audit_lp_pdf_selector_ownership.py` |
| `tokens` | src/tokens/00-light-tokens.css and src/tokens/01-dark-tokens.css | `shared-tokens` | `dev/scripts/audit_style_settings_contract.py`, `dev/scripts/release_check.py --skip-bundle` |

## Route Details

### chrome

Read:

- `dev/WIKI/WORKFLOWS/chrome-ui.md`
- `dev/WIKI/RUNTIME/chrome.md`
- `dev/WIKI/SELECTOR-OWNER-CHEATSHEET.md`

Contracts:

- `dev/WIKI/MAP/top-chrome-icon-background-contract.md when top chrome is involved`

Checks:

- `dev/scripts/audit_core_principles.py` (safe)
- `dev/scripts/release_check.py --skip-bundle` (safe)

### docs

Read:

- `dev/WIKI/WORKFLOWS/docs-assets.md`
- `dev/WIKI/DOCS/docs-map.md`
- `dev/WIKI/VISUAL-QA.md`

Contracts:

- `dev/WIKI/STRUCTURE.md`

Checks:

- `dev/scripts/audit_docs_assets.py` (safe)
- `dev/scripts/audit_readme_svg_layout.py` (safe)

### live-preview

Read:

- `dev/WIKI/WORKFLOWS/live-preview-cm6.md`
- `dev/WIKI/RUNTIME/table.md`
- `dev/WIKI/runtime-evidence-template.md`

Contracts:

- `dev/WIKI/MAP/cm6-hit-routing-contract.md`

Checks:

- `dev/scripts/audit_v3_hit_routing.py` (safe)
- `dev/scripts/audit_core_principles.py` (safe)

### mobile

Read:

- `dev/WIKI/WORKFLOWS/chrome-ui.md`
- `dev/WIKI/RUNTIME/chrome.md`
- `dev/WIKI/VISUAL-QA.md`

Contracts:

- `dev/WIKI/SRC/validation-matrix.md`

Checks:

- `dev/scripts/audit_core_principles.py` (safe)
- `dev/scripts/release_check.py --skip-bundle` (safe)

### pdf

Read:

- `dev/WIKI/WORKFLOWS/pdf.md`
- `dev/WIKI/RUNTIME/pdf.md`
- `dev/WIKI/RECIPES/pdf-label-preset.md`

Contracts:

- `dev/WIKI/MAP/pdf-header-footer-contract.md`

Checks:

- `dev/scripts/audit_pdf_header_footer.py` (safe)
- `dev/scripts/release_check.py --skip-bundle` (safe)

### plugin

Read:

- `dev/WIKI/PLUGINS/compatibility-matrix.md`
- `dev/WIKI/PLUGINS/runtime-dom-notes.md`
- `dev/WIKI/RUNTIME/plugins.md`

Contracts:

- `dev/WIKI/SELECTOR-OWNER-CHEATSHEET.md`

Checks:

- `dev/scripts/audit_core_principles.py` (safe)
- `dev/scripts/release_check.py --skip-bundle` (safe)

### release

Read:

- `dev/WIKI/WORKFLOWS/release.md`
- `dev/WIKI/DOCS/v3/release-plan.md`

Contracts:

- `numeric semver tag only; no leading v prefix`

Checks:

- `dev/scripts/release_check.py --tag <version>` (manual; requires placeholder)
- `dev/scripts/audit_release_zip.py` (safe)

### settings

Read:

- `dev/WIKI/RECIPES/style-settings-option.md`
- `dev/WIKI/DOCS/v3/style-settings-contract.md`
- `dev/WIKI/TOKENS/usage-guide.md`

Contracts:

- `dev/WIKI/MAP/settings-style-contract.md`

Checks:

- `dev/scripts/audit_style_settings_contract.py` (safe)
- `dev/scripts/audit_core_principles.py` (safe)
- `dev/scripts/release_check.py --skip-bundle` (safe)

### table

Read:

- `dev/WIKI/WORKFLOWS/table.md`
- `dev/WIKI/RUNTIME/table.md`
- `dev/WIKI/SELECTOR-OWNER-CHEATSHEET.md`

Contracts:

- `dev/WIKI/MAP/cm6-hit-routing-contract.md`
- `dev/WIKI/MAP/live-preview-pdf-css-map/parity-guidelines.md`

Checks:

- `dev/scripts/audit_direct_owner_guard.py` (safe)
- `dev/scripts/audit_v3_hit_routing.py` (safe)
- `dev/scripts/audit_lp_pdf_selector_ownership.py` (safe)

### tokens

Read:

- `dev/WIKI/TOKENS/usage-guide.md`
- `dev/WIKI/TOKENS/state-token-map.md`
- `dev/WIKI/VISUAL-QA.md`

Contracts:

- `dev/WIKI/SRC/validation-matrix.md`

Checks:

- `dev/scripts/audit_style_settings_contract.py` (safe; when setting-facing)
- `dev/scripts/release_check.py --skip-bundle` (safe)

## Registered Support Modules

Support modules are not primary owners and must not be used as repair layers.

- `src/base/10-base-workspace.css`: base/embed workspace primitives
- `src/surfaces/22-reading-embeds-workspace.css`: reading embed/workspace primitives
- `src/themes/50-dark.css`: dark theme support
- `src/plugins/60-canvas-graph-link-panes.css`: external/plugin support
- `src/themes/51-accessibility-motion-contrast.css`: accessibility/motion/contrast support
