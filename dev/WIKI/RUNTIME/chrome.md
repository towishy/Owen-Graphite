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

## Captured Runtime Facts

| Date | Surface | Runtime DOM | Source Owner | Evidence | Decision |
| --- | --- | --- | --- | --- | --- |
| 2026-07-22 | Root tab focus / active geometry | `.workspace-split.mod-root .workspace-tab-header-new-tab .clickable-icon`, `.workspace-tab-header.is-active > .workspace-tab-header-inner` | `src/surfaces/23-liquid-glass-core.css`, supported by `src/chrome/37-tabs-file-explorer-search.css` | `dev/TEMP/runtime-evidence/2026-07-22-chrome-top-icon-focus-and-active-tab-geometry.json` plus before/after fragments | Add a distinct 2px keyboard focus ring; make active tabs shrinkable; keep the active inner surface within the 33px header; nine-tab fixture has no overflow |
| 2026-05-25 | Overlay / command palette | `.prompt`, `.suggestion-item` | `src/chrome/32-overlay-popover-dataview.css`, `src/chrome/36-floating-ui-glass-system.css` | CDP capture in `dev/TEMP/runtime-evidence/2026-05-25-chrome-chrome-32-overlay-popover-dataview.json` and `2026-05-25-chrome-chrome-36-floating-ui-glass-system.json` | Real DOM confirms overlay hover/focus selectors are runtime-reserved |
| 2026-05-25 | Dataview table | `.block-language-dataview table tr`, `.markdown-rendered .dataview.table-view-table` | `src/chrome/32-overlay-popover-dataview.css` | Dataview 0.5.68 installed/enabled in `D:\Owen-WIKI`; CDP capture in `dev/TEMP/runtime-evidence/2026-05-25-chrome-chrome-32-overlay-popover-dataview.json` | Real DOM confirms Dataview table hover selectors are runtime-reserved |
| 2026-05-25 | Editor context menu | `.menu`, `.menu-item` | `src/chrome/35-editing-menu-tooltip-glass.css` | CDP capture in `dev/TEMP/runtime-evidence/2026-05-25-chrome-chrome-35-editing-menu-tooltip-glass.json` | Real DOM confirms menu hover selectors are runtime-reserved |
| 2026-05-25 | Tabs / file explorer | `.workspace-tab-header.is-active`, `.nav-file-title.is-active` | `src/chrome/37-tabs-file-explorer-search.css` | CDP capture in `dev/TEMP/runtime-evidence/2026-05-25-chrome-chrome-37-tabs-file-explorer-search.json` | Real DOM confirms selected/hover tab and nav selectors are runtime-reserved |
| 2026-05-25 | Settings controls | `.modal.mod-settings`, `.setting-item`, `.checkbox-container` | `src/chrome/33-settings-controls.css`, `src/chrome/36-floating-ui-glass-system.css` | CDP capture in `dev/TEMP/runtime-evidence/2026-05-25-chrome-chrome-33-settings-controls.json` | Real DOM confirms settings hover/control selectors are runtime-reserved |
| 2026-05-25 | Workspace shell / top chrome | `.workspace`, `.view-header`, `.side-dock-ribbon-action` | `src/chrome/30-workspace.css`, `src/surfaces/23-liquid-glass-core.css` | CDP capture in `dev/TEMP/runtime-evidence/2026-05-25-chrome-chrome-30-workspace.json` and `2026-05-25-chrome-surfaces-23-liquid-glass-core.json` | Real DOM confirms workspace/top chrome selectors are runtime-reserved |

## Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_core_principles.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```
