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
- In `dev/test-samples/owen-editor-feature-sample.md`, click cells under `Risk Matrix` and `Numeric Metrics`; the table should remain a Markdown table widget and allow cell-level editing.
- Click a deliberate HTML `<table>` utility sample; raw HTML activation is expected Obsidian behavior and should be treated as output-focused, not cell-editable, table usage.
- Reading View and Live Preview have comparable paragraph, heading, and table rhythm.
- Long URLs, code tokens, and table cells wrap or scroll without expanding the document column unexpectedly.
- Dataview, Canvas, Graph, Bookmarks, Outline, and Search panes keep usable spacing and contrast.

## Test Sample Smoke Matrix

| Sample | Sections | Expected Result |
|---|---|---|
| `dev/test-samples/owen-editor-feature-sample.md` | `Risk Matrix`, `Numeric Metrics` | Markdown table widget stays editable cell by cell in Live Preview |
| `dev/test-samples/owen-editor-feature-sample.md` | `Feature Coverage Snapshot`, `Risk Register`, `Decision Matrix` | HTML utility tables render as output-focused tables; raw HTML activation on click is expected |
| `dev/test-samples/owen-editor-feature-sample.md` | `Callout Gallery`, `Status Badges`, `Highlight Palette` | Callouts, badges, marks, keyboard tags, and blur spans keep spacing and contrast |
| `dev/test-samples/owen-graphite-sample.md` | `Table Utility Samples` | Markdown, comparison, compact, numeric, risk, wrap, token, and scroll table variants remain visually distinct |
| `dev/test-samples/owen-graphite-sample.md` | `Mermaid Sample`, `Code Blocks`, `Print/PDF Checks` | Mermaid, code labels, report spacing, and PDF-friendly utilities render without width inflation |

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
- Editable sample tables accidentally converted back to HTML `<table>` blocks.
- Core chrome selectors gaining non-print structural CSS properties such as `display`, `position`, `width`, `height`, `overflow`, `transform`, `pointer-events`, or `z-index`.
- PDF page breaks around tables, callouts, and headings.
