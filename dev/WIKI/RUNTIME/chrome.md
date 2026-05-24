# Runtime: Chrome

Use this for tabs, ribbon, explorer, search, settings, menus, modals, tooltips, and popovers.

## Capture States

| State | Evidence |
| --- | --- |
| Hover | rect before/after, shadow, background, transform |
| Focus | outline, outline-offset, box-shadow, contrast |
| Active | selected class, background/rim, z-index, adjacent surfaces |
| Split panes | root tab container, leaf, header, content edge |
| Mobile/narrow | viewport width, mobile classes, overflow |

## Owner Route

- Tabs/file explorer: `src/chrome/37-tabs-file-explorer-search.css`.
- Workspace shell: `src/chrome/30-workspace.css`.
- Ribbon/top nav: `src/chrome/34-nav-ribbon-glass.css` plus top chrome contract.
- Search/tasks/navigation: `src/chrome/31-navigation-tasks-search.css`.
- Overlays/popovers/modals: `src/chrome/32`, `35`, `36`.
- Settings controls: `src/chrome/33-settings-controls.css`.

## Rule

Do not fix top chrome from overlay modules. Do not add broad `body:not(.is-mobile)` selectors without checking existing owner and cascade relation.

## Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_core_principles.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```
