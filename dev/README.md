# Owen Graphite Dev CSS Modules

Obsidian loads `theme.css` as the theme entrypoint. Files in this folder are the development source modules; they are concatenated into `theme.css` by `scripts/bundle_theme.py`.

## Workflow

1. Edit the relevant module in `dev/`.
2. Run `python scripts/bundle_theme.py` to regenerate `theme.css`.
3. Run `python scripts/validate_theme.py` before syncing or releasing.
4. Run `python scripts/sync_obsidian_theme.py` to apply the validated theme to the detected local Obsidian vault.

Use `python scripts/bundle_theme.py --check` to verify that `theme.css` still matches the module bundle.

## Module Order

The cascade order is explicit in `_order.txt`. Do not rely on filename sorting alone; update `_order.txt` when adding or moving a module.

## Current Modules

- `00-settings.css`: Style Settings metadata and file index.
- `01-tokens.css`: root variables, Obsidian token aliases, and palette defaults.
- `02-base-workspace.css`: base body, workspace, tabs, and navigation chrome.
- `03-reading-content.css`: reading view typography, headings, links, lists, callouts, code, and tables.
- `04-dark-mode.css`: early dark-mode palette and component overrides.
- `04-print-base.css`: base print rules, page breaks, URL expansion, and print chrome hiding.
- `05-live-preview.css`: CM6 / Live Preview parity rules.
- `06-feature-presets.css`: report options, spacing, accent, code theme, eye-care, and auto-dark presets.
- `07-plugin-workspace.css`: plugin surfaces and workspace integration patches.
- `08-report-print-polish.css`: report/PDF output polish and print hardening.
- `09a-nav-ribbon-glass.css`: ribbon, breadcrumb, and workspace frame glass rules.
- `09b-editing-menu-tooltip-glass.css`: editing toolbar, context menu, tooltip, settings, search suggestions, and workspace frame glass rules.
- `09c-floating-ui-glass-system.css`: shared floating UI glass tokens, intensity presets, controls, notices, modals, and fallback behavior.
- `09d-tabs-file-explorer-search.css`: workspace tabs, final file explorer hover/active surfaces, and search pane glass rules.
- `10-a11y-regression-hotfixes.css`: late accessibility rules, interaction polish, and regression hotfixes.

Most splits are mechanical and order-preserving. Functional fixes should still happen in `dev/`, then be bundled into `theme.css`.

## Selector Notes

Obsidian usually applies theme and Style Settings classes to `body`. Combine those classes on the same selector, for example `body.theme-dark.ogd-zebra`, not `.theme-dark body.ogd-zebra`.

Use `:has()` only for progressive enhancement. Rules that depend on parent lookup should either be non-critical or guarded with `@supports selector(...)` so older Electron builds degrade by losing only the enhancement.

## Stability Notes

- Menu and right-click regressions should be checked first in `09b-editing-menu-tooltip-glass.css`. Keep `.menu .menu-item` dimensions stable between rest and hover states.
- Glass intensity classes are centralized in `09c-floating-ui-glass-system.css`. Any direct `backdrop-filter` rule in earlier glass modules must still respect `ogd-glass-off` and `ogd-glass-reduced` through late overrides.
- Hover/press motion is centralized through `--ogd-hover-lift`, `--ogd-hover-lift-subtle`, `--ogd-hover-shift`, and `--ogd-press-lift`. Use the `ogd-motion-*` classes instead of direct lift/shift transforms.
- Print rules are intentionally split by purpose. `04-print-base.css` owns base page setup; `06-feature-presets.css` owns report/preset print features; `07-plugin-workspace.css` owns plugin/workspace print behavior; `08-report-print-polish.css` owns report/PDF output polish; `09c-floating-ui-glass-system.css` owns print glass isolation after glass variables are declared; `10-a11y-regression-hotfixes.css` owns late print regression guards only.

## Validation Guards

`scripts/validate_theme.py` fails on orphan `dev/*.css` files, duplicate module order entries, `.theme-dark body.*` selectors, `transition: all`, unguarded `:has()` selectors, print blocks outside the approved owner modules, broken Style Settings bindings, and glass/motion rules that bypass central variables.
It also reports direct `backdrop-filter`, guarded `:has()`, print-block counts, and CSS complexity so risky areas stay visible before larger design changes.
