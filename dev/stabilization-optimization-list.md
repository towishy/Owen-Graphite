# DEV Stabilization and Optimization List

This list is the operating checklist for changes under `dev/`. Use it before broad CSS work, after focused optimization passes, and before committing generated artifacts.

## Stabilization Gates

- Start from a clean working tree unless the active task explicitly depends on existing edits.
- Edit source modules under `dev/`; do not hand-edit `theme.css`.
- Keep `dev/_order.txt` as the single source of cascade order.
- Regenerate `theme.css` with `python scripts/bundle_theme.py` after CSS edits.
- Regenerate the MAP with `python scripts/analyze_theme_css.py` after selector or cascade changes.
- Run `python scripts/validate_theme.py --ci` before committing.
- Rebuild the release ZIP only when runtime or release assets changed.
- Sync to the local Obsidian theme after runtime CSS changes have validated.

## Optimization Priorities

- Prefer selector compaction where target sets are identical and specificity is preserved.
- Prefer token reuse for repeated surfaces, colors, radii, shadows, and motion values.
- Prefer deleting obsolete fallback rules only when validation and surrounding history make ownership clear.
- Keep one optimization pass focused on one module or one behavior family.
- Regenerate generated artifacts in the same commit as the dev CSS change.

## Safe Compaction Patterns

- Alias groups: use `:is()` for repeated callout types, language badges, plugin aliases, or equivalent state selectors.
- View wrappers: use `:is(.markdown-rendered, .markdown-preview-view, .markdown-reading-view)` when declarations are identical across views.
- Pseudo-element pairs: use `:is(selector-a, selector-b)::before` and `::after` for identical reset blocks.
- Attribute aliases: group equivalent `[data-callout="..."]`, `[data-path^="..."]`, and language class aliases.
- Control states: group only when rest, hover, active, selected, and focus states already share the same declarations.

## High-Risk Areas

- Context menus and right-click behavior in `09b-editing-menu-tooltip-glass.css`.
- Live Preview editability and table cell editor chains.
- Print and PDF ownership across `04-print-base.css`, `06-feature-presets.css`, `08-report-print-polish.css`, `10b-late-reading-nav-polish.css`, and `10c-overlay-layout-polish.css`.
- Workspace tab/header layout in `09d-tabs-file-explorer-search.css`.
- Readable column width and mobile layout guards.
- Direct `backdrop-filter`, direct transform motion, and unguarded `:has()` selectors.

## Module Focus Map

- `01-tokens.css`: add or refine shared tokens before repeating literal values elsewhere.
- `03*`: reading typography, tables, callouts, embeds, and workspace reading parity.
- `05` and `07e`: Live Preview/mobile stability and editability-sensitive rules.
- `06`: feature presets, report mode, spacing, accent, code theme, eye-care, and auto-dark options.
- `07*`: plugin and workspace parity surfaces.
- `08`: report/PDF output polish.
- `09*`: glass surfaces, ribbon, toolbar, menus, tabs, file explorer, and search pane polish.
- `10*`: accessibility, motion, late reading/nav polish, overlay layout, and regression hotfixes.

## Commit Checklist

- `git diff --check` is clean.
- `python scripts/bundle_theme.py --check` passes or `theme.css` has been regenerated.
- `python scripts/analyze_theme_css.py` has refreshed `dev/MAP/theme-css-risk-map.*` when CSS changed.
- `python scripts/validate_theme.py --ci` passes.
- `get_errors` is clean for edited source files and generated artifacts.
- `dev/temp/` contains no tracked request artifacts beyond `dev/temp/.gitignore`.
- Commit message names the optimized module or stabilized behavior.

## Stop Conditions

- A selector change alters specificity in a high-risk area without a clear reason.
- A validation guard fails and the root cause is not understood.
- A generated artifact changes without a matching source or script reason.
- A visual behavior is known to be fragile and cannot be verified in the current pass.
