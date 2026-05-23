#!/usr/bin/env python3
"""Audit README SVG images for text overflow and edge-hugging controls.

This is intentionally conservative: generated README SVGs should keep text and
icon controls comfortably inside their visual containers. The audit uses a real
browser layout engine via Playwright so Korean text metrics and SVG transforms
are measured after rendering, not guessed from source strings.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
SVG_LINK_RE = re.compile(r"!\[[^\]]*\]\((screenshots/readme/[^)]+\.svg)\)")

VIEWPORT_MARGIN = 8
SIDEBAR_SPLIT_X = 300
SIDEBAR_SPLIT_GUARD = 8
MAX_TEXT_WIDTH = 560
MIN_TOOLBAR_MARGIN = 8


def readme_svg_paths() -> list[Path]:
    text = README.read_text(encoding="utf-8")
    paths: list[Path] = []
    for match in SVG_LINK_RE.finditer(text):
        rel = unquote(match.group(1).split("#", 1)[0])
        path = ROOT / rel
        if path not in paths:
            paths.append(path)
    return paths


def launch_browser(playwright):
    launch_errors: list[str] = []
    for kwargs in ({}, {"channel": "msedge"}, {"channel": "chrome"}):
        try:
            return playwright.chromium.launch(headless=True, **kwargs)
        except PlaywrightError as exc:
            label = kwargs.get("channel", "bundled chromium")
            launch_errors.append(f"{label}: {str(exc).splitlines()[0]}")
    raise RuntimeError("unable to launch a Chromium browser for SVG layout audit: " + "; ".join(launch_errors))


def audit_svg(page, path: Path) -> list[str]:
    page.goto(path.as_uri(), wait_until="load")
    return page.locator("svg").evaluate(
        r"""
        (svg, options) => {
          const svgBox = svg.getBoundingClientRect();
          const width = Number(svg.getAttribute('width') || svg.viewBox.baseVal.width || svgBox.width);
          const height = Number(svg.getAttribute('height') || svg.viewBox.baseVal.height || svgBox.height);
          const issues = [];
          const relBox = (node) => {
            const box = node.getBoundingClientRect();
            return {
              left: box.left - svgBox.left,
              top: box.top - svgBox.top,
              right: box.right - svgBox.left,
              bottom: box.bottom - svgBox.top,
              width: box.width,
              height: box.height,
            };
          };
          const label = (node) => (node.textContent || node.tagName).trim().replace(/\s+/g, ' ').slice(0, 80);
          const fmt = (box) => `left=${Math.round(box.left)} top=${Math.round(box.top)} right=${Math.round(box.right)} bottom=${Math.round(box.bottom)} width=${Math.round(box.width)}`;

          for (const node of svg.querySelectorAll('text')) {
            const box = relBox(node);
            if (box.left < options.viewportMargin || box.top < options.viewportMargin || box.right > width - options.viewportMargin || box.bottom > height - options.viewportMargin) {
              issues.push(`text touches viewport edge: ${label(node)} (${fmt(box)})`);
            }
            if (box.width > options.maxTextWidth) {
              issues.push(`text too wide; wrap or shorten: ${label(node)} (${fmt(box)})`);
            }
          }

          for (const node of svg.querySelectorAll('g[filter*="buttonShadow"]')) {
            const box = relBox(node);
            if (box.left < options.viewportMargin || box.top < options.viewportMargin || box.right > width - options.viewportMargin || box.bottom > height - options.viewportMargin) {
              issues.push(`control touches viewport edge: ${fmt(box)}`);
            }
            if (box.left < options.sidebarSplitX && box.right > options.sidebarSplitX - options.sidebarSplitGuard) {
              issues.push(`control hugs sidebar boundary near x=${options.sidebarSplitX}: ${fmt(box)}`);
            }
          }

          const toolbar = svg.querySelector('[data-ogd-audit="toolbar"]');
          if (toolbar) {
            const toolbarBox = relBox(toolbar);
            const controls = Array.from(svg.querySelectorAll('[data-ogd-audit="toolbar-controls"] > g[filter*="buttonShadow"]')).map(relBox);
            for (const box of controls) {
              if (box.left < toolbarBox.left + options.minToolbarMargin || box.right > toolbarBox.right - options.minToolbarMargin || box.top < toolbarBox.top + options.minToolbarMargin || box.bottom > toolbarBox.bottom - options.minToolbarMargin) {
                issues.push(`toolbar control lacks internal margin: ${fmt(box)} inside ${fmt(toolbarBox)}`);
              }
            }
          }

          const filledToolbarPaths = Array.from(svg.querySelectorAll('[data-ogd-audit="toolbar-controls"] path')).filter((node) => getComputedStyle(node).fill !== 'none');
          if (filledToolbarPaths.length) {
            issues.push(`toolbar has ${filledToolbarPaths.length} filled path icons; use outline icons or explicit fill=none`);
          }

          return issues;
        }
        """,
        {
            "viewportMargin": VIEWPORT_MARGIN,
            "sidebarSplitX": SIDEBAR_SPLIT_X,
            "sidebarSplitGuard": SIDEBAR_SPLIT_GUARD,
            "maxTextWidth": MAX_TEXT_WIDTH,
            "minToolbarMargin": MIN_TOOLBAR_MARGIN,
        },
    )


def main() -> int:
    try:
        paths = readme_svg_paths()
        if not paths:
            raise AssertionError("README.md does not reference any screenshots/readme/*.svg images")
        missing = [path for path in paths if not path.is_file()]
        if missing:
            raise FileNotFoundError("missing README SVG assets: " + ", ".join(str(path.relative_to(ROOT)) for path in missing))

        failures: list[str] = []
        with sync_playwright() as playwright:
            browser = launch_browser(playwright)
            page = browser.new_page(viewport={"width": 2200, "height": 900}, device_scale_factor=1)
            for path in paths:
                for issue in audit_svg(page, path):
                    failures.append(f"{path.relative_to(ROOT)}: {issue}")
            browser.close()

        if failures:
            raise AssertionError("README SVG layout issues:\n" + "\n".join(failures[:60]))

        print(f"OK: README SVG layout audit clean ({len(paths)} SVG files)")
        return 0
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
