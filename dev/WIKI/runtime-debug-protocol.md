# Runtime Debug Protocol

Use this when static audits pass but a selected, hovered, focused, or active runtime state still fails.

## Required Steps

1. Reproduce the issue in Obsidian with the exact runtime state active.
2. Run `runtime-debug-snippets/table-cell-dump.js` when the issue is table/cell geometry.
3. Run `runtime-debug-snippets/matched-rules-dump.js` to capture theme/core matched rules.
4. Inspect inline `style` first. Inline geometry means the issue may not be solvable by ordinary owner CSS.
5. If a theme rule is responsible, map the bundle line through `effective-source-map.json` and edit the source owner.
6. If an Obsidian core rule is responsible, do not override it unless an owner contract explicitly permits it.
7. Re-run the same runtime state after editing; static audits alone are insufficient.

## Outputs To Preserve

- DOM chain: tag, class, inline style, text preview.
- Rect chain: x/y/width/height for the target and parents.
- Computed geometry: display, position, width, height, min/max height, padding, line-height, vertical-align, overflow, transform.
- Matched rules: selector and CSS text for geometry-affecting declarations.

## Snippets

- `dev/WIKI/runtime-debug-snippets/table-cell-dump.js`
- `dev/WIKI/runtime-debug-snippets/matched-rules-dump.js`

