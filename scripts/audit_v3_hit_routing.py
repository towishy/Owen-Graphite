"""Run validate_theme.live_preview_hit_routing_audit against dist/theme-v3.css.

This is a thin wrapper that reuses the same audit logic that protects
v2.30.14's theme.css, so v3 inherits the v2.22.99–108 hit-routing
regressions guarantee.

Exits with code 1 if any violation is detected.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_theme import live_preview_hit_routing_audit  # type: ignore


def main() -> int:
    bundle = ROOT / "dist" / "theme-v3.css"
    if not bundle.exists():
        print(f"ERROR: {bundle} does not exist. Run bundle_v3.py first.")
        return 2
    content = bundle.read_text(encoding="utf-8")

    # live_preview_hit_routing_audit calls fail() (which sys.exit(1)) on
    # any violation. If we reach the next line, no violations.
    live_preview_hit_routing_audit(content, str(bundle.relative_to(ROOT)))
    print(f"OK: live_preview_hit_routing_audit clean on {bundle.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
