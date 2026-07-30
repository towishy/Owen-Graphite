# Workflow: Chrome And UI

## Owners

- Workspace/nav/status/ribbon: `src/chrome/30`, `31`, `34`, `37`.
- Overlay/menu/search/modal: `src/chrome/32`, `35`, `36`.
- Mobile/narrow workspace overflow: `src/chrome/30`; plugin/mobile embed behavior: `src/plugins/61`.
- Accessibility/motion: `src/themes/51-accessibility-motion-contrast.css`.

## Contract

Read `dev/WIKI/MAP/top-chrome-icon-background-contract.md` before top chrome icon changes.
- Canonical vertical Frosted ScrollArea is owned by Owen Editor `frosted-scrollbars.ts` and `styles.css`. Its adapter preserves each Obsidian native scroll viewport for wheel, touch, and keyboard input, then renders the Foundation `root / viewport / rail / grip` structure as an overlay with a 2px rail, fixed `6px x 44px` grip, three-line handle, `10px x 44px` hover/drag state, rail click, and pointer drag. Graphite must not approximate this component with global native `::-webkit-scrollbar` material or hide pane scrollbars from scoped chrome modules.

## Avoid

- Fixing workspace chrome from overlay modules.
- Broad `body:not(.is-mobile)` additions without checking duplicate groups.
- Hidden focus/hover regressions without runtime state checks.

## Required Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\wiki_route.py chrome
.\.venv\Scripts\python.exe dev\scripts\audit_core_principles.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```
