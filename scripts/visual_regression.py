#!/usr/bin/env python3
"""Capture HTML fixture screenshots with Playwright when it is available.

This script is optional and intentionally not part of the default validator.
Install Playwright separately when visual regression snapshots are needed:

    python -m pip install playwright
    python -m playwright install chromium
    python scripts/visual_regression.py
"""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURES = [
    "docs/fixtures/table-preview.html",
    "docs/fixtures/callout-preview.html",
    "docs/fixtures/search-input-glass-preview.html",
    "docs/fixtures/tab-glass-preview.html",
    "docs/fixtures/reference-list-polish-preview.html",
]


def fixture_url(path: Path) -> str:
    return path.resolve().as_uri()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "screenshots" / "fixture-regression")
    parser.add_argument("--width", type=int, default=1280)
    parser.add_argument("--height", type=int, default=900)
    parser.add_argument("fixtures", nargs="*", help="Fixture HTML paths relative to the repository root.")
    args = parser.parse_args()

    try:
        from playwright.sync_api import sync_playwright
    except ModuleNotFoundError:
        print("ERROR: Playwright is not installed. Run: python -m pip install playwright && python -m playwright install chromium")
        return 2

    fixtures = args.fixtures or DEFAULT_FIXTURES
    args.output_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={"width": args.width, "height": args.height}, device_scale_factor=1)
        for rel in fixtures:
            source = ROOT / rel
            if not source.is_file():
                print(f"SKIP: missing fixture {rel}")
                continue
            page.goto(fixture_url(source), wait_until="networkidle")
            output = args.output_dir / f"{source.stem}-{args.width}x{args.height}.png"
            page.screenshot(path=output, full_page=True)
            print(f"OK: captured {rel} -> {output.relative_to(ROOT)}")
        browser.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
