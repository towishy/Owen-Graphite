# Coverage Priority Plan

Generated from `dev/WIKI/MAP/unused-css-candidates.json`.

## Summary

- Matched selector parts: 2943
- Reserved no-match selector parts: 829
- State interaction backlog: 372
- Plugin runtime backlog: 89
- Print/PDF context backlog: 79
- Document fixture backlog: 55

## P0 State And Chrome Runtime

Capture resting and active runtime states before changing or deleting these selectors.

| Module | Priority Count | Reserved | Matched | Evidence scaffold |
| --- | ---: | ---: | ---: | --- |
| `src/chrome/37-tabs-file-explorer-search.css` | 81 | 85 | 103 | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface chrome --name chrome-37-tabs-file-explorer-search --state hovered --owner src/chrome/37-tabs-file-explorer-search.css` |
| `src/chrome/35-editing-menu-tooltip-glass.css` | 55 | 56 | 89 | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface chrome --name chrome-35-editing-menu-tooltip-glass --state hovered --owner src/chrome/35-editing-menu-tooltip-glass.css` |
| `src/chrome/33-settings-controls.css` | 53 | 54 | 113 | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface chrome --name chrome-33-settings-controls --state hovered --owner src/chrome/33-settings-controls.css` |
| `src/surfaces/23-liquid-glass-core.css` | 53 | 53 | 125 | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface chrome --name surfaces-23-liquid-glass-core --state hovered --owner src/surfaces/23-liquid-glass-core.css` |
| `src/chrome/32-overlay-popover-dataview.css` | 50 | 60 | 92 | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface chrome --name chrome-32-overlay-popover-dataview --state hovered --owner src/chrome/32-overlay-popover-dataview.css` |
| `src/chrome/36-floating-ui-glass-system.css` | 43 | 43 | 152 | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface chrome --name chrome-36-floating-ui-glass-system --state hovered --owner src/chrome/36-floating-ui-glass-system.css` |
| `src/chrome/30-workspace.css` | 36 | 51 | 136 | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface chrome --name chrome-30-workspace --state hovered --owner src/chrome/30-workspace.css` |
| `src/plugins/60-canvas-graph-link-panes.css` | 24 | 38 | 112 | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface chrome --name plugins-60-canvas-graph-link-panes --state hovered --owner src/plugins/60-canvas-graph-link-panes.css` |

## P1 Plugin Runtime

Prefer real plugin DOM. If unavailable, mark the capture as an approximation and keep the selector reserved.

| Module | Priority Count | Reserved | Matched | Evidence scaffold |
| --- | ---: | ---: | ---: | --- |
| `src/chrome/31-navigation-tasks-search.css` | 24 | 35 | 35 | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface plugin --name chrome-31-navigation-tasks-search --state rendered --owner src/chrome/31-navigation-tasks-search.css` |
| `src/plugins/61-live-preview-mobile-plugin.css` | 19 | 42 | 147 | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface plugin --name plugins-61-live-preview-mobile-plugin --state rendered --owner src/plugins/61-live-preview-mobile-plugin.css` |
| `src/plugins/60-canvas-graph-link-panes.css` | 14 | 38 | 112 | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface plugin --name plugins-60-canvas-graph-link-panes --state rendered --owner src/plugins/60-canvas-graph-link-panes.css` |
| `src/features/41-feature-presets.css` | 12 | 58 | 311 | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface plugin --name features-41-feature-presets --state rendered --owner src/features/41-feature-presets.css` |
| `src/chrome/30-workspace.css` | 10 | 51 | 136 | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface plugin --name chrome-30-workspace --state rendered --owner src/chrome/30-workspace.css` |
| `src/chrome/32-overlay-popover-dataview.css` | 4 | 60 | 92 | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface plugin --name chrome-32-overlay-popover-dataview --state rendered --owner src/chrome/32-overlay-popover-dataview.css` |

## P2 Print And PDF Context

Validate print media, report mode, header/footer state, and customer-delivery visibility before changing selector status.

| Module | Priority Count | Reserved | Matched | Evidence scaffold |
| --- | ---: | ---: | ---: | --- |
| `src/features/42-report-print-polish.css` | 32 | 32 | 357 | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface pdf --name features-42-report-print-polish --state print --owner src/features/42-report-print-polish.css` |
| `src/features/43-print-base.css` | 23 | 23 | 99 | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface pdf --name features-43-print-base --state print --owner src/features/43-print-base.css` |
| `src/features/41-feature-presets.css` | 22 | 58 | 311 | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface pdf --name features-41-feature-presets --state print --owner src/features/41-feature-presets.css` |
| `src/chrome/37-tabs-file-explorer-search.css` | 1 | 85 | 103 | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface pdf --name chrome-37-tabs-file-explorer-search --state print --owner src/chrome/37-tabs-file-explorer-search.css` |
| `src/surfaces/22-reading-embeds-workspace.css` | 1 | 25 | 44 | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface pdf --name surfaces-22-reading-embeds-workspace --state print --owner src/surfaces/22-reading-embeds-workspace.css` |

## P3 Document Content Fixtures

Add natural Markdown fixtures before treating these selectors as removal candidates.

| Module | Priority Count | Reserved | Matched | Evidence scaffold |
| --- | ---: | ---: | ---: | --- |
| `src/surfaces/21-reading-callouts-lists.css` | 25 | 29 | 130 | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface table --name surfaces-21-reading-callouts-lists --state rendered --owner src/surfaces/21-reading-callouts-lists.css` |
| `src/themes/50-dark.css` | 14 | 22 | 144 | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface table --name themes-50-dark --state rendered --owner src/themes/50-dark.css` |
| `src/base/12-reading-content.css` | 11 | 25 | 183 | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface table --name base-12-reading-content --state rendered --owner src/base/12-reading-content.css` |
| `src/surfaces/20-reading-tables-code.css` | 5 | 28 | 251 | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface table --name surfaces-20-reading-tables-code --state rendered --owner src/surfaces/20-reading-tables-code.css` |

## Required Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\build_unused_css_report.py
.\.venv\Scripts\python.exe dev\scripts\build_coverage_priority_plan.py --check
.\.venv\Scripts\python.exe dev\scripts\audit_runtime_evidence_requirements.py --strict
.\.venv\Scripts\python.exe dev\scripts\audit_docs_assets.py
```
