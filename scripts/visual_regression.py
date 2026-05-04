#!/usr/bin/env python3
"""Capture HTML fixture screenshots with Playwright when it is available.

This script is optional and intentionally not part of the default validator.
Install Playwright separately when visual regression snapshots are needed:

    python -m pip install playwright
    python -m playwright install chromium
    python scripts/visual_regression.py

Captured files are local QA artifacts. The default output directory is
dev/temp/visual-regression, which is intentionally ignored by Git.
"""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURES = [
    "screenshots/readme/v2.22.31-liquid-glass-overview.svg",
    "docs/fixtures/table-preview.html",
    "docs/fixtures/callout-preview.html",
    "docs/fixtures/search-input-glass-preview.html",
    "docs/fixtures/tab-glass-preview.html",
    "docs/fixtures/reference-list-polish-preview.html",
]

README_SVG_REQUIRED_TEXT = [
    "Owen Graphite",
    "위키형 표",
    "보고서형 표",
    "프로스트 아쿠아 포커스",
]


def fixture_url(path: Path) -> str:
    return path.resolve().as_uri()


def smoke_svg_page(page, rel: str, screenshot_bytes: bytes) -> list[str]:
    failures: list[str] = []
    svg = page.locator("svg").first
    if svg.count() == 0:
        return [f"{rel}: missing rendered <svg> root"]

    box = svg.bounding_box()
    if not box or box["width"] < 100 or box["height"] < 100:
        failures.append(f"{rel}: rendered SVG bounds are too small")
    if len(screenshot_bytes) < 5000:
        failures.append(f"{rel}: screenshot is unexpectedly small")

    page_text = page.locator("body").inner_text()
    if rel.endswith("v2.22.31-liquid-glass-overview.svg"):
        missing = [text for text in README_SVG_REQUIRED_TEXT if text not in page_text]
        if missing:
            failures.append(f"{rel}: missing rendered labels: {', '.join(missing)}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dev" / "temp" / "visual-regression")
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
            if source.suffix.lower() == ".svg":
                svg = page.locator("svg").first
                if svg.count() == 0:
                    print(f"ERROR: {rel}: missing rendered <svg> root")
                    browser.close()
                    return 1
                screenshot_bytes = svg.screenshot(path=output, timeout=10000)
                failures = smoke_svg_page(page, rel, screenshot_bytes)
                if failures:
                    for failure in failures:
                        print(f"ERROR: {failure}")
                    browser.close()
                    return 1
            else:
                screenshot_bytes = page.screenshot(path=output, full_page=True, timeout=10000)
            print(f"OK: captured {rel} -> {output.relative_to(ROOT)}")
        browser.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
