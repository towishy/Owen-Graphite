---
title: Click-to-edit regression sample
purpose: Manual + future-headless smoke test for CM6 hit-routing
related: dev/MAP/cm6-hit-routing-contract.md
versions:
  - v2.22.101  # heading→paragraph
  - v2.22.103  # blank-line compaction
  - v2.22.104  # active-line outline
  - v2.22.105  # table row margin
  - v2.22.106  # embed BFC + table widget margin
  - v2.22.107  # callout widget margin
  - v2.22.108  # legacy callout/table margin in 05 + spacing-relaxed
---

# Click-to-edit regression sample

Open this file in **Live Preview**. For each scenario click on the
**target row** at the indicated column and verify the caret lands on the
target row, not on the adjacent block.

If any scenario regresses, the offending CSS rule will almost certainly
violate one of the categories in
[CM6 Hit-Routing Contract](../MAP/cm6-hit-routing-contract.md). Run:

```bash
.venv/bin/python scripts/diff_guard.py --staged
.venv/bin/python scripts/validate_theme.py --ci
```

---

## Scenario 1 — heading → paragraph (v2.22.101)

### Heading immediately above this paragraph
Click here. The caret must land in this paragraph, not in the heading
above. (Earlier `HyperMD-header-*` cm-line vertical padding bled
upward.)

## Scenario 2 — blank line between two headings (v2.22.103)

### First heading

### Second heading

Click on the empty line between the two headings. The caret must land
on the empty line, not absorb into one of the headings.

## Scenario 3 — paragraph above table (v2.22.105 / v2.22.106)

This paragraph sits directly above a table. Click on this exact line
of text — the caret must remain in this paragraph and not jump into
the table cell or the cm-table-widget gap.

| Col A | Col B |
| --- | --- |
| 1 | 2 |
| 3 | 4 |

The paragraph below the table also needs to be clickable.

## Scenario 4 — paragraph above callout (v2.22.107 / v2.22.108)

This paragraph sits directly above a callout. Click on this line.

> [!info] Sample callout
> Body of the callout. Click on this body line — caret must remain
> here and not jump to the previous paragraph or to the next.

This paragraph sits directly below the callout. Click on this line.

## Scenario 5 — active line focus (v2.22.104)

Click anywhere in this paragraph, then click on the line below.

The active line must accept the click without the previous active line
trapping it via outline / box-shadow / transform.

## Scenario 6 — embed above paragraph (v2.22.106)

![[liquid-glass-core-state-matrix.html]]

This paragraph follows the embed. Click on this line — caret must
land here, not in the embed wrapper.

## Scenario 7 — spacing-relaxed preset (v2.22.108)

Enable **Style Settings → Owen Graphite → Spacing → Relaxed**, then
re-run scenarios 3 and 4. The bigger blank-line rhythm must not
re-introduce hit-target bleed.
