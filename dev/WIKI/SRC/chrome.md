# SRC: Chrome

- `src/chrome/30-workspace.css`: workspace shell and broad chrome.
- `src/chrome/31-navigation-tasks-search.css`: navigation, tasks, search base.
- `src/chrome/32-overlay-popover-dataview.css`: dataview, popovers, overlay search.
- `src/chrome/33-settings-controls.css`: settings and controls. Read `MAP/settings-style-contract.md` before changing settings pane UI.
- `src/chrome/34-nav-ribbon-glass.css`: ribbon and top nav glass.
- `src/chrome/35-editing-menu-tooltip-glass.css`: editing toolbar, tooltip glass, and the desktop bottom document frame/status-bar layout.
- `src/chrome/36-floating-ui-glass-system.css`: floating UI and overlay surfaces.
- `src/chrome/37-tabs-file-explorer-search.css`: tabs and file explorer.

Check owner before adding broad `body:not(.is-mobile)` selectors.

Minimum checks: `SRC/validation-matrix.md`, `audit_core_principles.py`, `release_check.py --skip-bundle`, plus runtime evidence for hover/focus/active states.
