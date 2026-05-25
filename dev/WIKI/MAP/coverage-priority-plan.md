# Coverage Priority Plan

Generated from `dev/WIKI/MAP/unused-css-candidates.json`.

## Summary

- Matched selector parts: 3337
- Reserved no-match selector parts: 446
- State interaction backlog: 373
- Plugin runtime backlog: 0
- Print/PDF context backlog: 0
- Document fixture backlog: 0

## P0 State And Chrome Runtime

Capture resting and active runtime states before changing or deleting these selectors.

| Module | Priority Count | Reserved | Matched | Runtime evidence | Evidence scaffold |
| --- | ---: | ---: | ---: | --- | --- |
| `src/chrome/32-overlay-popover-dataview.css` | 50 | 50 | 102 | captured; runtime-reserved (`dev/TEMP/runtime-evidence/2026-05-25-chrome-settings-live-preview-runtime-validation.json`) | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface chrome --name chrome-32-overlay-popover-dataview --state hovered --owner src/chrome/32-overlay-popover-dataview.css` |
| `src/surfaces/23-liquid-glass-core.css` | 49 | 49 | 129 | captured; runtime-reserved (`dev/TEMP/runtime-evidence/2026-05-25-chrome-surfaces-23-liquid-glass-core.json`) | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface chrome --name surfaces-23-liquid-glass-core --state hovered --owner src/surfaces/23-liquid-glass-core.css` |
| `src/chrome/35-editing-menu-tooltip-glass.css` | 45 | 45 | 100 | captured; runtime-reserved (`dev/TEMP/runtime-evidence/2026-05-25-chrome-chrome-35-editing-menu-tooltip-glass.json`) | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface chrome --name chrome-35-editing-menu-tooltip-glass --state hovered --owner src/chrome/35-editing-menu-tooltip-glass.css` |
| `src/chrome/36-floating-ui-glass-system.css` | 39 | 39 | 156 | captured; runtime-reserved (`dev/TEMP/runtime-evidence/2026-05-25-chrome-settings-live-preview-runtime-validation.json`) | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface chrome --name chrome-36-floating-ui-glass-system --state hovered --owner src/chrome/36-floating-ui-glass-system.css` |
| `src/chrome/37-tabs-file-explorer-search.css` | 37 | 37 | 151 | captured; runtime-reserved (`dev/TEMP/runtime-evidence/2026-05-25-chrome-settings-live-preview-runtime-validation.json`) | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface chrome --name chrome-37-tabs-file-explorer-search --state hovered --owner src/chrome/37-tabs-file-explorer-search.css` |
| `src/chrome/33-settings-controls.css` | 34 | 34 | 133 | captured; runtime-reserved (`dev/TEMP/runtime-evidence/2026-05-25-chrome-settings-live-preview-runtime-validation.json`) | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface chrome --name chrome-33-settings-controls --state hovered --owner src/chrome/33-settings-controls.css` |
| `src/chrome/30-workspace.css` | 29 | 29 | 158 | captured; runtime-reserved (`dev/TEMP/runtime-evidence/2026-05-25-chrome-chrome-30-workspace.json`) | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface chrome --name chrome-30-workspace --state hovered --owner src/chrome/30-workspace.css` |
| `src/plugins/60-canvas-graph-link-panes.css` | 24 | 24 | 128 | partial; runtime-reserved (`dev/TEMP/runtime-evidence/2026-05-25-plugin-plugins-60-canvas-graph-link-panes.json`) | `.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface chrome --name plugins-60-canvas-graph-link-panes --state hovered --owner src/plugins/60-canvas-graph-link-panes.css` |

## P1 Plugin Runtime

Prefer real plugin DOM. If unavailable, mark the capture as an approximation and keep the selector reserved.

| Module | Priority Count | Reserved | Matched | Runtime evidence | Evidence scaffold |
| --- | ---: | ---: | ---: | --- | --- |

## P2 Print And PDF Context

Validate print media, report mode, header/footer state, and customer-delivery visibility before changing selector status.

| Module | Priority Count | Reserved | Matched | Runtime evidence | Evidence scaffold |
| --- | ---: | ---: | ---: | --- | --- |

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
