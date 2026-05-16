"""Render screenshots/readme/v2.30-cover-1200x800.svg to a 1200x800 PNG.

Used to produce the Obsidian community theme cover image. Output is JPEG/PNG
compatible (we emit PNG). The upload form recommends 1200x800 (3:2).
"""
from __future__ import annotations

from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
SVG_PATH = ROOT / "screenshots" / "readme" / "v2.30-cover-1200x800.svg"
PNG_PATH = ROOT / "screenshots" / "readme" / "v2.30-cover-1200x800.png"


def main() -> int:
    if not SVG_PATH.exists():
        raise SystemExit(f"missing: {SVG_PATH}")

    svg_markup = SVG_PATH.read_text(encoding="utf-8")
    html = (
        "<!doctype html><html><head><meta charset='utf-8'>"
        "<style>html,body{margin:0;padding:0;background:#e9eef5;}"
        "svg{display:block;}</style></head><body>"
        f"{svg_markup}"
        "</body></html>"
    )

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            viewport={"width": 1200, "height": 800},
            device_scale_factor=2,
        )
        page = context.new_page()
        page.set_content(html, wait_until="load")
        page.wait_for_timeout(120)
        page.screenshot(
            path=str(PNG_PATH),
            clip={"x": 0, "y": 0, "width": 1200, "height": 800},
            omit_background=False,
        )
        browser.close()

    print(f"OK: wrote {PNG_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
