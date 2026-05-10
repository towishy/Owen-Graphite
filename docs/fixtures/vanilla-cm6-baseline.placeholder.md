# Vanilla CM6 baseline — planned (v2.22.110+)

This file is a placeholder. The real artefact will be a JSON snapshot of
key computed-style values for a vanilla Obsidian Live Preview, captured
once per supported Obsidian version.

## What the snapshot will contain

```json
{
  "obsidian": "1.6.7",
  "selectors": {
    ".HyperMD-table-row": {
      "margin-top": "0px",
      "margin-bottom": "0px",
      "padding-top": "0px",
      "padding-bottom": "0px"
    },
    ".cm-callout": { "margin-top": "0px", "margin-bottom": "0px" },
    ".cm-active.cm-line": { "outline-width": "0px", "box-shadow": "none" }
  }
}
```

## How it will be used

1. CI renders the same DOM with vanilla theme → records baseline.
2. CI renders the DOM with Owen Graphite `theme.css` → records actual.
3. Any selector whose Owen Graphite value diverges from baseline must
   either be on a documented exception list or fail the build.

## Why deferred

The static `live_preview_hit_routing_audit` already covers every
regression we have observed. A computed-style baseline catches a
*different* class of regression (e.g. unintended `line-height` drift)
and is worth doing once we have a Playwright host (see
`scripts/hit_routing_probe.py`).

## Owner

Tracked in `dev/stabilization-optimization-list.md` under "Future
tooling".
