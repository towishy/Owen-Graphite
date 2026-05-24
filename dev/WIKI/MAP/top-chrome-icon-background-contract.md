# Top Chrome Icon And Background Contract

This is the MAP contract for top chrome changes.

Top chrome includes root tab strips, view headers, side pane headers, tab buttons, sidebar toggles, and their clickable icon slots. This area is high risk because background-only changes can still make icons disappear through contrast, inheritance, stacking, or broad selector side effects.

## Safe Change Rules

- Patch the narrowest confirmed surface: root tab strip, root view header, active tab, side pane tab header, new-tab button, tab-list button, or sidebar toggle.
- Keep hover/focus/pressed states neutral unless the task explicitly asks for an accented selected state.
- Use the selected-document frosted pill only for `.workspace-tab-header.is-active`, not generic hover.
- Do not patch SVG descendants, glyph `stroke`, `fill`, `opacity`, layout, visibility, or `z-index` unless the visible bug is proven to live there.
- If icons disappear, inspect parent backgrounds and clickable child slots before changing icon glyph rules.

## Current Source Owners

- `src/chrome/34-nav-ribbon-glass.css`: root ribbon and navigation glass refinements.
- `src/chrome/35-editing-menu-tooltip-glass.css`: editing menu and tooltip glass refinements.
- `src/chrome/36-floating-ui-glass-system.css`: floating UI glass system.
- `src/surfaces/23-liquid-glass-core.css`: final liquid glass surface and top chrome ownership.

Run `dev/scripts/build_src_map.py` after broad top chrome edits so `dev/WIKI/MAP/theme-css-risk-map.json` records the changed risk surface.