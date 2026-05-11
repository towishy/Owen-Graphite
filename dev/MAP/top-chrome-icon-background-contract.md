# Top Chrome Icon And Background Contract

This document records the working contract for Owen Graphite top chrome changes: title/tab backgrounds, root view headers, tab buttons, and top action icons. This area is high risk because a background-only change can still make icons disappear through contrast, inherited color, stacking, or broad selector side effects.

## Scope

Top chrome includes these related layers:

- Root document frame: `.workspace-split.mod-root`, `.mod-root .workspace-leaf`, `.mod-root .workspace-tabs`.
- Tab strip surfaces: `.workspace-tab-header-container`, `.workspace-tab-header`, `.workspace-tab-header-inner`.
- View header surfaces: `.view-header`, `.view-header-title-container`, `.view-actions`, `.view-header-nav-buttons`.
- Top icon controls: `.workspace-tab-header-container .clickable-icon`, `.workspace-tab-header-new-tab`, `.workspace-tab-header-tab-list`, `.view-header .view-action`, `.view-header .clickable-icon`, `.sidebar-toggle-button`.
- Sidebar toggle controls such as `.sidebar-toggle-button.mod-left` can sit outside `.workspace-tab-header-container`; do not assume every top icon is a descendant of the tab header container.
- Some sidebar toggles render the visible button fill on a child `.clickable-icon` or `.clickable-icon.side-dock-ribbon-action`; if the wrapper rule has no visible effect, inspect and patch that child slot without touching SVG/color/opacity.
- Right-side top controls such as `.workspace-tab-header-tab-list` and `.sidebar-toggle-button.mod-right` also inherit shared top icon hover rules; include their child clickable slots when removing blue rim artifacts.
- Side pane tab headers on both `.workspace-split.mod-left-split` and `.workspace-split.mod-right-split` should share the same neutral outline-only treatment; do not fix only one side when both panes expose tab icons.
- Selected side pane tab icons may use the same frosted document-selection pill as root active tabs, but only on `.workspace-tab-header.is-active`; hover/focus states should remain neutral.

## Current Layer Ownership

- `02-base-workspace.css` gives broad workspace/tab containers `--background-secondary` and document content `--background-primary`.
- `09a-nav-ribbon-glass.css` softens root tab/header frame lines without owning icon visibility.
- `09b-editing-menu-tooltip-glass.css` removes broad frame borders and makes side panes transparent/glass.
- `10d-liquid-glass-core.css` is the final owner for top icon slot behavior, attached tab shape, and late root tab/header cleanup.

The important consequence: root header and tab strip background corrections must be made at the surface layer only. They must not redefine top icon controls unless the task is explicitly about icons.

## Implementation History And Lessons

The top chrome work settled into three stable layers after several risky attempts:

1. Root document chrome: `.workspace-split.mod-root .workspace-tab-header-container` and `.workspace-split.mod-root .view-header` should match `var(--background-primary)` so the editor tab strip does not inherit the secondary/sidebar tint.
2. Shared side pane controls: left and right side pane top slots should use neutral outline-only glass at rest and on hover/focus/pressed states. This includes direct tab headers, new-tab buttons, tab-list buttons, and sidebar toggle child `.clickable-icon` slots.
3. Selected document state: active root tabs and explicitly selected left side pane tab icons may use the stronger frosted document-selection pill with a shallow sky rim.

The key lesson is that top icon regressions were not caused by missing SVG rules. They were caused by changing the wrong parent surface, grouping surfaces with icon controls, or letting transparent icon slots sit on a competing background. Recovery patches aimed at `color`, `stroke`, `fill`, or `opacity` made the area more fragile and should be avoided.

## Current Implemented Pattern

The current stable implementation lives in `10d-liquid-glass-core.css` near the late top chrome block:

- Root tab/header cleanup uses root-only selectors and sets the strip/header to `var(--background-primary)`.
- Root active document tabs use `.workspace-split.mod-root .workspace-tabs .workspace-tab-header.is-active .workspace-tab-header-inner` for the selected-document pill.
- Side pane top slots use `:is(.workspace-split.mod-left-split, .workspace-split.mod-right-split)` for neutral parity across both panes.
- Sidebar toggles include wrapper and child slots such as `.sidebar-toggle-button.mod-left .clickable-icon` and `.sidebar-toggle-button.mod-right .clickable-icon` because the visible fill may live on the child.
- Left side selected tab icons use `.workspace-split.mod-left-split .workspace-tab-header.is-active .workspace-tab-header-inner` for the selected-document pill, while hover/focus states remain neutral.
- Dark mode mirrors only the same surface-level background, border, and box-shadow properties.

This pattern intentionally does not touch `.workspace-tab-header-inner-icon`, SVG descendants, glyph color inheritance, layout, opacity, display, visibility, or z-index.

## Change Recipe

Use this sequence for future top chrome changes:

1. Identify whether the visible problem is root tab strip, root view header, root active tab, side pane tab header, new-tab button, tab-list button, or sidebar toggle.
2. Patch only the confirmed surface in `10d-liquid-glass-core.css`, after earlier competing chrome rules.
3. Keep hover/focus/pressed states neutral unless the task explicitly asks for a selected/accented state.
4. Use the selected-document frosted pill only for `.workspace-tab-header.is-active`, not for generic hover.
5. Bundle with `scripts/bundle_theme.py`, validate with `scripts/validate_theme.py`, then sync to the local Obsidian vault before visual testing.
6. If icons disappear, revert the last surface patch and inspect parent backgrounds before considering any icon selector.

## Icon Visibility Model

Top icons are intentionally quiet at rest:

- Resting icon button backgrounds are transparent.
- Resting borders and shadows are transparent/none.
- The visible glyph comes from Obsidian/core theme color inheritance.
- Hover/active states may receive a small glass slot and soft rim.
- Hover, active, pressed, and expanded states should stay neutral graphite/gray in the top chrome unless a task explicitly asks for an accent. Avoid blue outline rings on shared top controls.

Because the resting button surface is transparent, any parent background change can affect perceived icon visibility. A pale, tinted, or glassy parent may be safe; a competing gradient, overlay, opacity, color reset, or stacking change can make the glyph appear missing even when the SVG is still present.

## Safe Change Rules

For background mismatch fixes in the root editor top strip:

- Prefer the narrowest root-only surface selector, for example `.workspace-split.mod-root .view-header`.
- Prefer `background` over `background-color` when overriding an earlier gradient layer.
- Prefer semantic Obsidian variables such as `var(--background-primary)` or `var(--background-secondary)` before hardcoded colors.
- For root tab strip color mismatch, prefer matching `.workspace-split.mod-root .workspace-tab-header-container` to `var(--background-primary)` before making the whole strip transparent; full transparency can reveal OS/titlebar tint behind the workspace.
- Keep changes inside `@media (min-width: 701px)` and `body:not(.is-mobile)` unless mobile was explicitly tested.
- Mirror dark-mode only when the same visual issue is confirmed in dark mode.
- Touch tab container, active tab, and view header as separate surfaces; do not group them with icons.

For active tab line cleanup:

- Target `.workspace-split.mod-root .workspace-tabs .workspace-tab-header.is-active` for top border color.
- Target `.workspace-split.mod-root .workspace-tabs .workspace-tab-header.is-active .workspace-tab-header-inner` for inner border or shadow.
- Do not use `.workspace-tab-header-container .clickable-icon` in a tab-line cleanup rule.

## Unsafe Change Rules

Avoid these in background-only or tab-line tasks:

- Broad top chrome groups that combine `.view-header`, `.workspace-tab-header-container`, `.clickable-icon`, `.view-action`, and `.sidebar-toggle-button`.
- Any `opacity` changes on titlebar, tab strip, view header, or icon controls.
- Any `display`, `visibility`, `position`, `z-index`, `filter`, or `transform` changes on top icon controls.
- Any `color`, `stroke`, `fill`, or SVG rule intended as a recovery patch after a background change.
- Parent-level opacity or filter changes; they affect child SVG glyphs even when the selector does not mention SVG.
- Replacing icon slot backgrounds and root header backgrounds in the same patch.

If icons disappear after a background patch, first revert the background patch. Do not add icon recovery selectors until the actual layer is identified.

## Debug Order

When a top background color looks wrong but icons must remain untouched:

1. Check whether the visible mismatch is from `.view-header`, `.view-header-title-container`, `.workspace-tab-header-container`, or `.workspace-tab-header-inner`.
2. Check whether the unwanted color is `background`, `background-color`, `box-shadow`, `border`, or an inherited parent surface showing through transparency.
3. Override only the confirmed surface, preferably in `10d-liquid-glass-core.css` near the existing top chrome cleanup block.
4. Run `scripts/bundle_theme.py` and `scripts/validate_theme.py`.
5. Sync to the local Obsidian vault and visually confirm on Windows and macOS Obsidian when possible.

## Visual Acceptance Checklist

A safe top chrome patch must satisfy all of these:

- Root view header background matches the intended editor/document surface.
- Active tab line artifacts are gone only where requested.
- Top icons remain visible at rest.
- Top icons still show hover/active feedback.
- New tab, tab list, view actions, back/forward nav, and sidebar toggle buttons all remain clickable.
- Light mode and dark mode do not lose icon contrast.
- Windows and macOS Obsidian chrome remain visually coherent.

## Current Known Good Direction

The safest confirmed direction is to leave icon selectors untouched and patch only root surfaces. A narrow example is:

```css
@media (min-width: 701px) {
  body:not(.is-mobile) .workspace-split.mod-root .view-header {
    background: var(--background-primary, #ffffff) !important;
  }

  body:not(.is-mobile) .workspace-split.mod-root .workspace-tabs .workspace-tab-header.is-active .workspace-tab-header-inner {
    border-color: transparent !important;
    box-shadow: none !important;
  }
}
```

This pattern is acceptable because it does not touch `.clickable-icon`, `.view-action`, SVG glyphs, color inheritance, opacity, or layout.
