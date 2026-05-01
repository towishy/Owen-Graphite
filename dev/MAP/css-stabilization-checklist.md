# CSS Stabilization Checklist (MAP-driven)

## Goal Gates
- Rollback baseline: `v2.22.21` is the current retained release/tag baseline
- MAP gate: critical = 0, high = 0
- Validation gate: `python scripts/validate_theme.py --ci` must pass
- Build gate: `python scripts/build_release.py` must produce `dist/Owen-Graphite-<version>.zip`

## Daily Workflow
1. Refresh MAP baseline.
   - Command: `/Users/owen/Work/owen-graphite/.venv/bin/python scripts/analyze_theme_css.py`
2. Review top findings in `dev/MAP/theme-css-risk-map.html`.
3. Patch only high-impact blocks first.
   - Prefer removing structural overrides from core chrome selectors.
4. Re-run MAP and compare severity counts.
5. Run full validator.
   - Command: `/Users/owen/Work/owen-graphite/.venv/bin/python scripts/validate_theme.py --ci`
6. Build release ZIP after validation passes.
   - Command: `/Users/owen/Work/owen-graphite/.venv/bin/python scripts/build_release.py`

## Core Chrome Do/Do Not
- Do keep decorative-only changes on core chrome: background, border, shadow, color.
- Do not force core chrome structure: display, width/height, overflow, position, transform, z-index.
- Do not use broad selectors on critical chrome areas (`[role="tab"]`, tab header containers, titlebar, sidebar toggles).

## Pre-release Quick Checks
- `dev/MAP/theme-css-risk-map.json` has zero critical/high.
- `scripts/validate_theme.py --ci` is green.
- `scripts/validate_theme.py --ci` must report `table inflation guards clean`.
- `dist/Owen-Graphite-<version>.zip` exists and opens correctly.
- No unexpected structural overrides were reintroduced in `theme.css`.

## Regression Watchlist
- Live Preview table cell editor chain (`td > .table-cell-wrapper > .cm-editor > .cm-scroller > .cm-content > .cm-line/.cm-active.cm-line`)
- Embedded table paragraph margin reset (`.cm-embed-block table :is(td, th) > p`)
- Empty trailing table lines (`.cm-active.cm-line:empty`, `br:only-child`)
- Ribbon icon blocks
- Sidebar toggle reset blocks (macOS and desktop)
- Workspace tab header shaping blocks
- Reduced-motion transform reset blocks
