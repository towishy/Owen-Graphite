#!/usr/bin/env python3
"""STUB — Headless CM6 hit-routing probe (planned for v2.22.110+).

Goal:
  Render a real CM6 instance with `theme.css` applied and call
  `document.elementFromPoint(x, y)` at the centre of every paragraph
  rect in `dev/test-samples/click-to-edit-regression.md`. Fail when
  the returned element is not the expected `.cm-line` for that row.

Why a stub now:
  - Owen Graphite is CSS-only and the existing pipeline is offline
    Python; pulling in Playwright + an Obsidian-like CM6 host is a
    multi-hour task that we should plan deliberately.
  - The static guard (`live_preview_hit_routing_audit`) already covers
    every regression we have seen; this dynamic probe is the belt for
    the suspenders.

Plan:
  1. Add a `dev/fixtures/cm6-host.html` page that loads CM6 + Obsidian
     stubs (`.markdown-source-view.mod-cm6`) and renders a fixed
     Markdown sample with predictable line ids.
  2. Use Playwright (`playwright install chromium`) headless.
  3. For each `data-line-id` the probe:
       const rect = el.getBoundingClientRect();
       const hit = document.elementFromPoint(rect.left + 24, rect.top + rect.height/2);
       expect(hit.closest('.cm-line')).toBe(el);
  4. Wire into CI as a separate job (`probe-hit-routing`).

Until then this stub exits 0 with a notice so other tooling can call
it without breaking.
"""
from __future__ import annotations

import sys


def main() -> int:
    print(
        "hit_routing_probe: STUB — dynamic probe not yet implemented.\n"
        "  Static coverage lives in scripts/validate_theme.py "
        "(live_preview_hit_routing_audit) and scripts/diff_guard.py.\n"
        "  See scripts/hit_routing_probe.py docstring for the rollout plan."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
