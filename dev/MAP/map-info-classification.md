# MAP Info Classification

Current MAP gate baseline after the v2.22.79-v2.22.94 workstream: `critical=0`, `high=1`, `medium=0`, `low=1`, `info=102`.

Live Preview editability has a separate map because the core chrome MAP does not model CM6 line hitbox geometry: `dev/MAP/live-preview-editability-css-map.md`.

The remaining 70 findings are informational triage signals. They are not release blockers, but they identify core chrome surfaces that should be reviewed carefully before Windows or Obsidian chrome changes ship.

## Severity Baseline

| Severity | Count | Release Meaning |
|---|---:|---|
| critical | 0 | No blocking chrome structural regression detected |
| high | 1 | Mermaid Live Preview control selector touches `.clickable-icon` structural properties; review before release |
| medium | 0 | No medium-risk chrome structural regression detected |
| low | 1 | Mermaid control active transform |
| info | 102 | Decorative or intentional chrome touches to monitor |

## Current High/Low Findings

| Severity | Module | Selector Family | Classification |
|---|---|---|---|
| high | `dev/07e-live-preview-mobile-plugin.css` | Mermaid controls scoped `.clickable-icon` | Hidden scoped structural risk; not the current heading editability bug |
| low | `dev/07e-live-preview-mobile-plugin.css` | Mermaid control `:active` transform | Low-risk active feedback |

## Module Distribution

| Module | Info Findings | Classification |
|---|---:|---|
| `dev/09b-editing-menu-tooltip-glass.css` | 16 | Preserve: floating/editing/menu glass ownership |
| `dev/09a-nav-ribbon-glass.css` | 15 | Preserve: ribbon and sidebar toggle glass ownership |
| `dev/09d-tabs-file-explorer-search.css` | 8 | Review before tab/file explorer chrome edits |
| `dev/07d-canvas-graph-link-panes.css` | 8 | Preserve: graph/canvas control polish |
| `dev/10a-accessibility-motion-contrast.css` | 6 | Preserve: focus and high-contrast accessibility layer |
| `dev/02-base-workspace.css` | 5 | Stable base workspace ownership |
| `dev/06-feature-presets.css` | 4 | Preserve: file type icon cue presets |
| `dev/09c-floating-ui-glass-system.css` | 4 | Preserve: shared floating glass controls |
| `dev/03c-reading-embeds-workspace.css` | 2 | Stable reading/workspace bridge rules |
| `dev/04-print-base.css` | 1 | Intentional print-only chrome hiding |
| `dev/10c-overlay-layout-polish.css` | 1 | Stable late overlay layout polish |

## Selector Distribution

| Selector Family | Hits | Interpretation |
|---|---:|---|
| `.clickable-icon` | 38 | Mostly decorative icon glass/shadow/color touches |
| `.workspace-tab-header` | 27 | Tab chrome requires Windows parity review before changes |
| `.workspace-ribbon` | 9 | Ribbon glass is expected, but structure must remain untouched |
| `.side-dock-ribbon` | 9 | Side dock ribbon glass is expected |
| `.workspace-tab-header-container` | 8 | Container touches should stay decorative |
| `.sidebar-toggle-button` | 6 | Toggle visual styling only; no placement or sizing changes |
| `.workspace-tabs` | 4 | Workspace tab frame touches require caution |
| `[role=tab]` | 2 | Accessibility/focus use only; no broad structural styling |
| `.workspace-tab-container` | 2 | Container layout changes require separate Windows validation |
| `.titlebar` | 1 | Print-only hiding is allowed for PDF export |

## Property Distribution

| Property | Hits | Classification |
|---|---:|---|
| `box-shadow` | 33 | Core glass depth, preserve |
| `background` | 24 | Core glass surface, preserve |
| `color` | 20 | Readability/state styling, preserve |
| `border` | 12 | Full-surface ring/border treatment, preserve |
| `border-color` | 11 | State/rim treatment, preserve |
| `border-radius` | 10 | Chrome surface shape, preserve |
| `background-color` | 4 | Decorative tint, preserve |
| `outline` | 2 | Accessibility/focus treatment, preserve |
| `display` | 1 | Allowed print-only chrome hiding |
| `transform` | 1 | Allowed reduced-motion reset |
| `font-weight` | 1 | Active/readability cue |

## Action Guidance

- Preserve decorative glass/shadow findings unless a visual regression is confirmed.
- Treat new non-print structural properties on tabs, titlebar, sidebar toggles, and ribbon as release blockers.
- Use `scripts/validate_theme.py --ci` to enforce the core chrome structure guard before release.
- If MAP info count changes, update this classification after running `scripts/analyze_theme_css.py`.
