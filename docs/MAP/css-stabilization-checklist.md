# CSS Stabilization Checklist (MAP-driven)

## Goal Gates
- MAP gate: critical = 0, high = 0
- Validation gate: `python scripts/validate_theme.py --ci` must pass
- Build gate: `python scripts/build_release.py` must produce `dist/Owen-Graphite-<version>.zip`

## Daily Workflow
1. Refresh MAP baseline.
   - Command: `/Users/owen/Work/owen-graphite/.venv/bin/python scripts/analyze_theme_css.py`
2. Review top findings in `docs/MAP/theme-css-risk-map.html`.
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
- `docs/MAP/theme-css-risk-map.json` has zero critical/high.
- `scripts/validate_theme.py --ci` is green.
- `dist/Owen-Graphite-<version>.zip` exists and opens correctly.
- No unexpected structural overrides were reintroduced in `theme.css`.

## Regression Watchlist
- Ribbon icon blocks
- Sidebar toggle reset blocks (macOS and desktop)
- Workspace tab header shaping blocks
- Reduced-motion transform reset blocks
