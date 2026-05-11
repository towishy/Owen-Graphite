# MAP Info Classification

<!-- markdownlint-disable MD060 -->

Current MAP gate baseline after the v2.22.130 Mermaid control cleanup: `critical=0`, `high=0`, `medium=0`, `low=0`, `info=103`.

Live Preview editability has a separate map because the core chrome MAP does not model CM6 line hitbox geometry: `dev/MAP/live-preview-editability-css-map.md`.

The remaining 103 findings are informational triage signals. They are not release blockers, but they identify core chrome surfaces that should be reviewed carefully before Windows or Obsidian chrome changes ship.

## Severity Baseline

| Severity | Count | Release Meaning |
|---|---:|---|
| critical | 0 | No blocking chrome structural regression detected |
| high | 0 | No high-risk chrome structural finding remains |
| medium | 0 | No medium-risk chrome structural regression detected |
| low | 0 | No low-risk active transform finding remains |
| info | 103 | Decorative or intentional chrome touches to monitor |

## Current High/Low Findings

| Severity | Module | Selector Family | Classification |
|---|---|---|---|
| none | - | - | No current high or low findings after the Mermaid control selector split |

## Module Distribution

| Module | Info Findings | Classification |
|---|---:|---|
| `dev/10d-liquid-glass-core.css` | 35 | Preserve: shared Liquid Glass focus, chrome, and state ownership |
| `dev/09a-nav-ribbon-glass.css` | 15 | Preserve: ribbon and sidebar toggle glass ownership |
| `dev/09b-editing-menu-tooltip-glass.css` | 12 | Preserve: floating/editing/menu glass ownership |
| `dev/09d-tabs-file-explorer-search.css` | 8 | Review before tab/file explorer chrome edits |
| `dev/07d-canvas-graph-link-panes.css` | 8 | Preserve: graph/canvas control polish |
| `dev/10a-accessibility-motion-contrast.css` | 6 | Preserve: focus and high-contrast accessibility layer |
| `dev/02-base-workspace.css` | 5 | Stable base workspace ownership |
| `dev/06-feature-presets.css` | 4 | Preserve: file type icon cue presets |
| `dev/09c-floating-ui-glass-system.css` | 4 | Preserve: shared floating glass controls |
| `dev/07e-live-preview-mobile-plugin.css` | 2 | Preserve: Mermaid decorative-only control styling |
| `dev/03c-reading-embeds-workspace.css` | 2 | Stable reading/workspace bridge rules |
| `dev/04-print-base.css` | 1 | Intentional print-only chrome hiding |
| `dev/10c-overlay-layout-polish.css` | 1 | Stable late overlay layout polish |

## Selector Distribution

| Selector Family | Hits | Interpretation |
|---|---:|---|
| `.workspace-tab-header` | 54 | Tab chrome requires Windows parity review before changes |
| `.clickable-icon` | 51 | Mostly decorative icon glass/shadow/color touches |
| `.workspace-ribbon` | 17 | Ribbon glass is expected, but structure must remain untouched |
| `.side-dock-ribbon` | 17 | Side dock ribbon glass is expected |
| `.workspace-tab-header-container` | 16 | Container touches should stay decorative |
| `.workspace-tabs` | 15 | Workspace tab frame touches require caution |
| `.sidebar-toggle-button` | 12 | Toggle visual styling only; no placement or sizing changes |
| `[role=tab]` | 3 | Accessibility/focus use only; no broad structural styling |
| `.workspace-tab-container` | 2 | Container layout changes require separate Windows validation |
| `.titlebar` | 1 | Print-only hiding is allowed for PDF export |

## Property Distribution

| Property | Hits | Classification |
|---|---:|---|
| `box-shadow` | 55 | Core glass depth, preserve |
| `background` | 42 | Core glass surface, preserve |
| `border-color` | 34 | State/rim treatment, preserve |
| `color` | 30 | Readability/state styling, preserve |
| `outline` | 17 | Accessibility/focus treatment, preserve |
| `border` | 14 | Full-surface ring/border treatment, preserve |
| `border-radius` | 14 | Chrome surface shape, preserve |
| `background-color` | 4 | Decorative tint, preserve |
| `font-weight` | 4 | Active/readability cue |
| `display` | 1 | Allowed print-only chrome hiding |
| `transform` | 1 | Allowed reduced-motion reset |

## Action Guidance

- Preserve decorative glass/shadow findings unless a visual regression is confirmed.
- Treat new non-print structural properties on tabs, titlebar, sidebar toggles, and ribbon as release blockers.
- Use `scripts/validate_theme.py --ci` to enforce the core chrome structure guard before release.
- If MAP info count changes, update this classification after running `scripts/analyze_theme_css.py`.
