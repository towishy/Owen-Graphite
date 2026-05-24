# Workflow: Chrome And UI

## Owners

- Workspace/nav/status/ribbon: `src/chrome/30`, `31`, `34`, `37`.
- Overlay/menu/search/modal: `src/chrome/32`, `35`, `36`.
- Accessibility/motion: `src/themes/51-accessibility-motion-contrast.css`.

## Contract

Read `dev/WIKI/MAP/top-chrome-icon-background-contract.md` before top chrome icon changes.

## Avoid

- Fixing workspace chrome from overlay modules.
- Broad `body:not(.is-mobile)` additions without checking duplicate groups.
- Hidden focus/hover regressions without runtime state checks.
