# CM6 Hit-Routing Contract

> **The single source of truth for what Owen Graphite CSS may and may not
> declare on CodeMirror 6 (`.markdown-source-view.mod-cm6`) elements.**
> Codified after the v2.22.99–108 click-to-edit regression marathon.
> Enforced by `scripts/validate_theme.py` (`live_preview_hit_routing_audit`)
> and `scripts/diff_guard.py`.

## Why this exists

Live Preview routes mouse clicks to a CM6 line / widget via plain CSS box
geometry. **Any vertical box on the wrong element extends its hit-target
across adjacent paragraphs, so the caret silently lands inside the widget
instead of where the user clicked.** The rule is invisible until a user
reports "I have to double-click to edit this line".

Between v2.22.99 and v2.22.108 we shipped seven incremental fixes for the
same root cause. This contract captures the rule once so future patches
fail at lint time instead of in a user's vault.

## Forbidden categories (hard ERRORs)

### 1. Block widget vertical margin
Selectors that **target one of these tokens directly** must not declare
non-zero `margin`, `margin-top`, `margin-bottom`, `margin-block*`:

- `.cm-callout`
- `.cm-table-widget`
- `.cm-embed-block.cm-callout`

Vertical rhythm comes from the **natural blank `.cm-line`** that always
sits between a paragraph and a block widget. Horizontal margin/padding is
fine.

### 2. HyperMD `.cm-line` vertical box
Same rule, plus padding, applies to source-line variants:

- `.HyperMD-table-row`
- `.HyperMD-callout`
- `.HyperMD-codeblock`, `.HyperMD-codeblock-begin`, `.HyperMD-codeblock-end`
- `.HyperMD-header-1` through `.HyperMD-header-6`

Forbidden: non-zero `margin*` and `padding*` on the top/bottom axes.
Horizontal `padding-left/right` is fine and is how the callout / heading
indent is drawn.

### 3. Active line visual overlay
On `.cm-active.cm-line` (or `.cm-active .cm-line`):

- No `outline` (extends the hit-target).
- No `box-shadow` whose offset is non-zero (overlay captures clicks).
- No `transform` (creates a new stacking context that swallows clicks).
- No vertical `padding`.

This codifies v2.22.104.

### 4. Embed wrapper BFC pair
`.cm-embed-block`, `.cm-html-embed` must not declare both
`overflow-x: auto` AND `max-width: 100%` on the same rule. Together they
create a block formatting context whose top edge becomes a click sink
above the wrapped element. v2.22.106.

### 5. `pointer-events: none` on rendered text
`.cm-content`, `.cm-line` (top-level) must never set
`pointer-events: none`. CM6 routes clicks through the rendered span tree;
disabling pointer events kills click-to-edit. Use the native cascade
(`.cm-line * { pointer-events: auto }`) instead.

## Allowed: descendant rules

Rules of the form `.cm-callout .callout-content { margin-top: 0.5em }`
are **fine**. The guard only flags rules that *target the widget itself*.
Descendant rules style the widget's interior and don't extend its
hit-target.

## How to add a new chrome rule for a CM6 widget

1. Read this file.
2. Decide whether the rule targets a widget directly or a descendant.
3. Use **horizontal** padding/margin and **`border`/`background`/`box-shadow`
   without negative offset** for visual treatment.
4. Run:
   ```bash
   .venv/bin/python scripts/diff_guard.py --staged
   .venv/bin/python scripts/validate_theme.py --ci
   ```
   Both must be green.
5. In `CHANGELOG.md` under the new version, list the selector tokens the
   patch touched (a `### Selectors touched` line). `scripts/changelog_lint.py`
   enforces this.
6. After commit, `python scripts/build_selector_provenance.py` rebuilds
   the index so `scripts/who_added.py` can find the new rule.

## Module ownership (informational)

| Module | Allowed scope |
| --- | --- |
| `dev/05-live-preview.css` | `.markdown-source-view.mod-cm6 *` and HyperMD-* tokens |
| `dev/03*.css` | Reading view (`.markdown-rendered`, `.markdown-preview-view`) |
| `dev/08-report-print-polish.css` | `@media print`, `@page` only |
| `dev/10-a11y-regression-hotfixes.css` | EOF append-only hotfixes |

If a rule needs to bridge two scopes, put it in `10-a11y-regression-hotfixes.css`
as a documented EOF block.

## Reference

- v2.22.101: heading `.cm-line` padding 0.16–0.42em → 0.
- v2.22.102: forced `.cm-line *` pointer-events:auto block removed.
- v2.22.103: `.cm-line:empty` 0.45em compaction removed.
- v2.22.104: `.cm-active.cm-line` glass focus outline+shadow removed.
- v2.22.105: `.HyperMD-table-row` cm-line margin removed.
- v2.22.106: `.cm-embed-block { overflow-x:auto; max-width:100% }` BFC + `.cm-table-widget` margin removed.
- v2.22.107: `.cm-callout` widget margin removed (Report Notice cascade).
- v2.22.108: `.cm-callout, .HyperMD-callout` legacy margin + spacing-relaxed bleeders removed; `live_preview_hit_routing_audit` added.
- v2.22.109: full guard family (categories 3–5), `diff_guard.py`, selector provenance, changelog lint, this contract document, regression sample.
