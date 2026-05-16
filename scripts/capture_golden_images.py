#!/usr/bin/env python3
"""Capture per-region pixel golden images of the Owen Graphite theme.

Uses dev/v3/golden-rig/obsidian-harness.html. Every section with the
`data-fp-region="<id>"` attribute is screenshotted into
`screenshots/golden/v<version>/<theme>/<id>.png`.

This is the secondary safety net for the v3 rewrite. The primary safety net is
`scripts/capture_computed_fingerprint.py` because pixel diffs drift with GPU
and font rendering. Use this for human-eye review and large layout regressions.

Usage:
    python -m pip install playwright
    python -m playwright install chromium
    python scripts/capture_golden_images.py
    python scripts/capture_golden_images.py --theme dark
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HARNESS = ROOT / "dev" / "v3" / "golden-rig" / "obsidian-harness.html"
MANIFEST = ROOT / "manifest.json"


def read_version() -> str:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))["version"]


def sanitize_for_filename(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]", "-", value)


def capture(theme: str, out_dir: Path) -> int:
    try:
        from playwright.sync_api import sync_playwright
    except ModuleNotFoundError:
        print(
            "ERROR: Playwright is not installed. Run: "
            "python -m pip install playwright && python -m playwright install chromium"
        )
        return 2

    if not HARNESS.is_file():
        print(f"ERROR: harness file not found: {HARNESS}")
        return 1

    out_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        context = browser.new_context(
            viewport={"width": 1440, "height": 900},
            device_scale_factor=2,
        )
        page = context.new_page()
        page.goto(HARNESS.as_uri(), wait_until="networkidle")
        page.evaluate(
            "(t) => { document.body.classList.remove('theme-light','theme-dark'); "
            "document.body.classList.add(t === 'dark' ? 'theme-dark' : 'theme-light'); }",
            theme,
        )
        page.wait_for_timeout(200)

        regions = page.evaluate(
            """
            () => Array.from(document.querySelectorAll('[data-fp-region]'))
              .map(el => el.getAttribute('data-fp-region'))
            """
        )

        full_path = out_dir / "_full-page.png"
        page.screenshot(path=str(full_path), full_page=True)
        print(f"OK: full page -> {full_path.relative_to(ROOT)}")

        for region in regions:
            locator = page.locator(f'[data-fp-region="{region}"]')
            if locator.count() == 0:
                print(f"SKIP: region not found: {region}")
                continue
            target = out_dir / f"{region}.png"
            locator.screenshot(path=str(target))
            print(f"OK: {region} -> {target.relative_to(ROOT)}")
        browser.close()
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--theme", choices=["light", "dark", "both"], default="both")
    parser.add_argument(
        "--out-root",
        type=Path,
        default=ROOT / "screenshots" / "golden",
    )
    parser.add_argument("--version", default=None)
    args = parser.parse_args()

    version = args.version or read_version()
    themes = ["light", "dark"] if args.theme == "both" else [args.theme]
    for t in themes:
        out_dir = args.out_root / f"v{sanitize_for_filename(version)}" / t
        rc = capture(t, out_dir)
        if rc != 0:
            return rc
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
