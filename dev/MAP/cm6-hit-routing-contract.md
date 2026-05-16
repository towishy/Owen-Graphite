# CM6 Hit-Routing Contract

This is the MAP contract for CodeMirror 6 Live Preview hit routing.

Live Preview routes mouse clicks through CSS box geometry. Rules that add vertical boxes, overlays, or pointer-event blockers to the wrong CM6 element can make clicks land in adjacent widgets instead of the intended text line.

## Hard Rules

- Do not add non-zero vertical `margin*` to direct block-widget selectors such as `.cm-callout`, `.cm-table-widget`, or `.cm-embed-block.cm-callout`.
- Do not add non-zero vertical `margin*` or `padding*` to direct HyperMD `.cm-line` variants such as `.HyperMD-table-row`, `.HyperMD-callout`, `.HyperMD-codeblock*`, or `.HyperMD-header-*`.
- Do not add `outline`, non-trivial `box-shadow`, `transform`, or vertical padding to `.cm-active.cm-line`.
- Do not combine `overflow-x: auto` and `max-width: 100%` on `.cm-embed-block` or `.cm-html-embed`.
- Do not set `pointer-events: none` on `.cm-content` or top-level `.cm-line` text routing surfaces.

## Review Path

Run:

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_v3_hit_routing.py
.\.venv\Scripts\python.exe dev\scripts\build_src_map.py
```

Any MAP finding in the `cm6-hit-routing-sensitive` category must be checked against this contract before release.