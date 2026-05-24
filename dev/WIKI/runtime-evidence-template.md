# Runtime Evidence Template

Use this before changing CSS for selected, hovered, focused, active, collapsed, expanded, plugin-generated, or Obsidian runtime states.

## Capture Header

| Field | Value |
| --- | --- |
| Issue |  |
| Surface | Reading / Live Preview / PDF / Chrome / Plugin / Mobile |
| Runtime state | selected / hovered / focused / active / editing / print / other |
| Obsidian version |  |
| OS |  |
| Theme version |  |
| Vault/theme path |  |
| Repro note |  |

## Required Evidence

1. DOM chain for the target and parents.
2. Bounding rect chain: x, y, width, height.
3. Computed geometry: display, position, width, height, min/max height, margin, padding, line-height, overflow, transform.
4. Matched rules that set geometry, visual state, or hit routing.
5. Inline style check.
6. Owner mapping from matched theme rule to source module.
7. Screenshot or short note confirming the exact runtime state.

## Snippets

Use these first when the issue touches table/cell geometry:

```text
dev/WIKI/runtime-debug-snippets/table-cell-dump.js
dev/WIKI/runtime-debug-snippets/matched-rules-dump.js
```

## Decision

| Question | Answer |
| --- | --- |
| Is a theme rule responsible? |  |
| If yes, which source owner? |  |
| Is an inline/core rule responsible? |  |
| Is CSS allowed by a risk contract? |  |
| Which workflow applies? |  |
| Which audit proves the change? |  |

## Rule

If this template cannot be filled, do not patch the CSS. Gather evidence first or update the relevant WIKI incident with the blocker.
