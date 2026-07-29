# Coverage Priority Plan

Generated from `dev/WIKI/MAP/unused-css-candidates.json`.

## Summary

- Matched selector parts: 3412
- Reserved no-match selector parts: 689
- State interaction backlog: 430
- Plugin runtime backlog: 57
- Print/PDF context backlog: 26
- Document fixture backlog: 0

## P0 State And Chrome Runtime

Capture resting and active runtime states before changing or deleting these selectors.

| Module | Priority Count | Reserved | Matched | Runtime evidence | Evidence scaffold |
| --- | ---: | ---: | ---: | --- | --- |
| `src/chrome/33-settings-controls.css` | 122 | 186 | 138 | captured; runtime-reserved (`dev/TEMP/runtime-evidence/2026-05-25-chrome-settings-live-preview-runtime-validation.json`) | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface chrome --name chrome-33-settings-controls --state hovered --owner src/chrome/33-settings-controls.css` |
| `src/chrome/37-tabs-file-explorer-search.css` | 75 | 75 | 171 | captured; runtime-reserved (`dev/TEMP/runtime-evidence/2026-05-25-chrome-settings-live-preview-runtime-validation.json`) | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface chrome --name chrome-37-tabs-file-explorer-search --state hovered --owner src/chrome/37-tabs-file-explorer-search.css` |
| `src/surfaces/23-liquid-glass-core.css` | 67 | 67 | 124 | captured; runtime-reserved (`dev/TEMP/runtime-evidence/2026-05-25-chrome-surfaces-23-liquid-glass-core.json`) | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface chrome --name surfaces-23-liquid-glass-core --state hovered --owner src/surfaces/23-liquid-glass-core.css` |
| `src/chrome/35-editing-menu-tooltip-glass.css` | 56 | 56 | 98 | captured; runtime-reserved (`dev/TEMP/runtime-evidence/2026-07-24-chrome-right-sidebar-bottom-frame.json`) | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface chrome --name chrome-35-editing-menu-tooltip-glass --state hovered --owner src/chrome/35-editing-menu-tooltip-glass.css` |
| `src/chrome/32-overlay-popover-dataview.css` | 50 | 50 | 102 | captured; runtime-reserved (`dev/TEMP/runtime-evidence/2026-05-25-chrome-settings-live-preview-runtime-validation.json`) | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface chrome --name chrome-32-overlay-popover-dataview --state hovered --owner src/chrome/32-overlay-popover-dataview.css` |
| `src/chrome/36-floating-ui-glass-system.css` | 35 | 35 | 156 | captured; runtime-reserved (`dev/TEMP/runtime-evidence/2026-05-25-chrome-settings-live-preview-runtime-validation.json`) | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface chrome --name chrome-36-floating-ui-glass-system --state hovered --owner src/chrome/36-floating-ui-glass-system.css` |
| `src/chrome/30-workspace.css` | 29 | 29 | 158 | captured; runtime-reserved (`dev/TEMP/runtime-evidence/2026-05-25-chrome-chrome-30-workspace.json`) | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface chrome --name chrome-30-workspace --state hovered --owner src/chrome/30-workspace.css` |
| `src/plugins/60-canvas-graph-link-panes.css` | 24 | 24 | 128 | partial; runtime-reserved (`dev/TEMP/runtime-evidence/2026-05-25-plugin-plugins-60-canvas-graph-link-panes.json`) | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface chrome --name plugins-60-canvas-graph-link-panes --state hovered --owner src/plugins/60-canvas-graph-link-panes.css` |

## P1 Plugin Runtime

Prefer real plugin DOM. If unavailable, mark the capture as an approximation and keep the selector reserved.

| Module | Priority Count | Reserved | Matched | Runtime evidence | Evidence scaffold |
| --- | ---: | ---: | ---: | --- | --- |
| `src/chrome/33-settings-controls.css` | 52 | 186 | 138 | captured; runtime-reserved (`dev/TEMP/runtime-evidence/2026-05-25-chrome-settings-live-preview-runtime-validation.json`) | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface plugin --name chrome-33-settings-controls --state rendered --owner src/chrome/33-settings-controls.css` |
| `src/chrome/31-navigation-tasks-search.css` | 4 | 15 | 59 | captured; runtime-reserved (`dev/TEMP/runtime-evidence/2026-07-24-chrome-link-pane-collapse-icons.json`) | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface plugin --name chrome-31-navigation-tasks-search --state rendered --owner src/chrome/31-navigation-tasks-search.css` |
| `src/plugins/61-live-preview-mobile-plugin.css` | 1 | 23 | 168 | needed | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface plugin --name plugins-61-live-preview-mobile-plugin --state rendered --owner src/plugins/61-live-preview-mobile-plugin.css` |

## P2 Print And PDF Context

Validate print media, report mode, header/footer state, and customer-delivery visibility before changing selector status.

| Module | Priority Count | Reserved | Matched | Runtime evidence | Evidence scaffold |
| --- | ---: | ---: | ---: | --- | --- |
| `src/chrome/33-settings-controls.css` | 12 | 186 | 138 | captured; runtime-reserved (`dev/TEMP/runtime-evidence/2026-05-25-chrome-settings-live-preview-runtime-validation.json`) | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface pdf --name chrome-33-settings-controls --state print --owner src/chrome/33-settings-controls.css` |
| `src/features/43-print-base.css` | 6 | 6 | 177 | needed | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface pdf --name features-43-print-base --state print --owner src/features/43-print-base.css` |
| `src/features/41-feature-presets.css` | 4 | 17 | 331 | needed | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface pdf --name features-41-feature-presets --state print --owner src/features/41-feature-presets.css` |
| `src/base/13-live-preview.css` | 2 | 20 | 218 | captured; runtime-reserved (`dev/TEMP/runtime-evidence/2026-05-25-chrome-settings-live-preview-runtime-validation.json`) | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface pdf --name base-13-live-preview --state print --owner src/base/13-live-preview.css` |
| `src/themes/50-dark.css` | 2 | 18 | 159 | needed | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface pdf --name themes-50-dark --state print --owner src/themes/50-dark.css` |

## P3 Document Content Fixtures

Add natural Markdown fixtures before treating these selectors as removal candidates.

| Module | Priority Count | Reserved | Matched | Runtime evidence | Evidence scaffold |
| --- | ---: | ---: | ---: | --- | --- |

## Required Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\build_unused_css_report.py
.\.venv\Scripts\python.exe dev\scripts\build_coverage_priority_plan.py --check
.\.venv\Scripts\python.exe dev\scripts\audit_runtime_evidence_requirements.py --strict
.\.venv\Scripts\python.exe dev\scripts\audit_docs_assets.py
```
