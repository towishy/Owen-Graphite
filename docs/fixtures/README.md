# Owen Graphite Design Fixtures

This directory tracks approved visual references used before changing Owen Graphite chrome CSS. Treat these files as design baselines, not release CSS.

## Approved Core Samples

| Sample | Role | Use When |
|---|---|---|
| [Liquid Glass Hover Study](../liquid-glass-hover-study-sample.html) | Primary core design reference | Judging liquid glass hover behavior, transparent panels, rim light, and shadow depth |
| [Liquid Glass Core State Matrix](liquid-glass-core-state-matrix.html) | Approved Owen Graphite Liquid Glass core reference | Comparing lens depth, rim light, refraction illusion, ribbon, tab, file row, command palette, popover, tooltip, modal, and sidebar toggle states before CSS implementation |
| [Refero Inspired Glass States](refero-inspired-glass-states.html) | Approved state comparison fixture | Comparing default, hover, active, selected, and dark/light glass state treatments |
| [Community Theme Search Focus](community-theme-search-focus.html) | Modal search focus regression fixture | Checking that community theme browser search stays visually calm while general search focus remains visible |

## Review Rules

- New chrome or interaction design ideas need a fixture before CSS changes.
- Fixtures should show light and dark states when the change affects both modes.
- Compare new work against the Liquid Glass Hover Study first, then against the state fixture.
- A fixture can inform implementation only after explicit user approval.
