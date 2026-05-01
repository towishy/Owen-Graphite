# Owen Graphite QA Checklist

Use this checklist after CSS changes, before syncing a build to Obsidian or cutting a release.

## Build Gates

1. Run `python scripts/bundle_theme.py --check`.
2. Run `python scripts/validate_theme.py`.
3. Run `python scripts/build_release.py`.
4. If testing in a local vault, run `python scripts/sync_obsidian_theme.py`.

## Obsidian Interaction Checks

- Right-click a note, file explorer item, and editor selection. The context menu should open immediately and menu rows should not resize on hover.
- Open Settings and Style Settings. Hover left navigation rows, right pane setting rows, buttons, dropdowns, sliders, and color pickers.
- Open command palette and search suggestions. Selected and hovered rows should be visible without shifting the list.
- Hover file explorer folders/files, active file rows, ribbon icons, workspace tabs, breadcrumbs, and status bar segments.
- Toggle Desktop Glass intensity: Off, Reduced, Subtle, Standard, Strong.
- Toggle Desktop Hover motion: Off, Subtle, Standard.
- Enable OS reduced motion, then confirm hover/press movement is removed while colors and focus states remain visible.

## Reading And Editing Checks

- Live Preview remains editable across blank lines, headings, tables, callouts, embeds, and code blocks.
- Reading View and Live Preview have comparable paragraph, heading, and table rhythm.
- Long URLs, code tokens, and table cells wrap or scroll without expanding the document column unexpectedly.
- Dataview, Canvas, Graph, Bookmarks, Outline, and Search panes keep usable spacing and contrast.

## Print/PDF Checks

- Export a short report to PDF using A3 landscape and confirm H1 page breaks, repeated table headers, and first-page header labels.
- Check report tables, risk tables, status badges, callouts, Mermaid blocks, code blocks, images, and footnotes.
- Confirm print output has no glass blur, decorative hover transforms, or UI chrome.

## Regression Watchlist

- Context menu clickability and row hit targets.
- Settings modal row height and hover movement.
- Search suggestion selected row contrast.
- File explorer active-file visibility in light and dark modes.
- Table widget editability in Live Preview.
- PDF page breaks around tables, callouts, and headings.
