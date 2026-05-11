# CSS Stabilization Checklist (MAP-driven)

## Goal Gates

- Rollback baseline: `v2.22.120` is the current retained release/tag baseline
- MAP gate: critical = 0, high = 0, medium = 0
- Current MAP baseline: `critical=0`, `high=0`, `medium=0`, `low=0`, `info=103`; remaining info findings are allowed only when they are documented chrome guards or accessibility fallbacks.
- MAP intentionally classifies print-only chrome hiding and reduced-motion transform resets as info-level guards.
- Validation gate: `python scripts/validate_theme.py --ci` must pass
- Build gate: `python scripts/build_release.py` must produce `dist/Owen-Graphite-<version>.zip`

## Daily Workflow

1. Refresh MAP baseline.
   - Command: `python scripts/analyze_theme_css.py`
2. Review top findings in `dev/MAP/theme-css-risk-map.html`.
3. Patch only high-impact blocks first.
   - Prefer removing structural overrides from core chrome selectors.
4. Re-run MAP and compare severity counts.
5. Run full validator.
   - Command: `python scripts/validate_theme.py --ci`
6. Build release ZIP after validation passes.
   - Command: `python scripts/build_release.py`

## Core Chrome Do/Do Not

- Do keep decorative-only changes on core chrome: background, border, shadow, color.
- Do not force core chrome structure: display, width/height, overflow, position, transform, z-index.
- Do not use broad selectors on critical chrome areas (`[role="tab"]`, tab header containers, titlebar, sidebar toggles).

## Pre-release Quick Checks

- `dev/MAP/theme-css-risk-map.json` has zero critical/high/medium.
- `scripts/validate_theme.py --ci` is green.
- `scripts/validate_theme.py --ci` must report `table inflation guards clean`.
- `dist/Owen-Graphite-<version>.zip` exists and opens correctly.
- No unexpected structural overrides were reintroduced in `theme.css`.

## Regression Watchlist

- Live Preview table cell editor chain (`td > .table-cell-wrapper > .cm-editor > .cm-scroller > .cm-content > .cm-line/.cm-active.cm-line`)
- Live Preview heading/paragraph editability map: `dev/MAP/live-preview-editability-css-map.md`
- Live Preview heading rhythm must not be created by expanding active heading line-box padding; use hitbox-external spacing.
- Embedded table paragraph margin reset (`.cm-embed-block table :is(td, th) > p`)
- Empty trailing table lines (`.cm-active.cm-line:empty`, `br:only-child`)
- Rendered CM6 text spans should not be broadly forced to `pointer-events: none` without DOM verification.
- Ribbon icon blocks
- Sidebar toggle reset blocks (macOS and desktop)
- Workspace tab header shaping blocks
- Reduced-motion transform reset blocks

## v2.22.26 MAP Info Classification

Preserve these info-level guards unless a visual regression proves otherwise:

- Ribbon, sidebar toggle, workspace tab, and workspace frame glass/shadow ownership that stays decorative-only.
- Print-only chrome hiding and print layout isolation blocks.
- `prefers-reduced-motion`, `prefers-contrast`, and `forced-colors` accessibility fallbacks.

Safe next reduction candidates:

- Repeated editing toolbar/submenu surface declarations in `09b-editing-menu-tooltip-glass.css`, only when specificity and right-click behavior remain unchanged.
- Ribbon and vault footer token consolidation in `09a-nav-ribbon-glass.css`, only through variable reuse or identical selector compaction.
- Chrome selected-state cleanup that replaces left-edge inset accents with full-surface border/ring treatments.
