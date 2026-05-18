#!/usr/bin/env python3
"""Capture effective computed values, pseudo styles, and --ogd-* tokens."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "manifest.json"
DEFAULT_FIXTURE = ROOT / "docs" / "v3" / "research" / "golden-rig" / "obsidian-harness.html"
V3_BUNDLE = ROOT / "dist" / "theme-v3.css"
PROPS = [
    "display", "position", "visibility", "pointer-events", "color", "background-color", "background-image",
    "font-family", "font-size", "font-weight", "font-style", "line-height", "letter-spacing", "text-align",
    "margin-top", "margin-right", "margin-bottom", "margin-left", "padding-top", "padding-right", "padding-bottom", "padding-left",
    "border-top-width", "border-right-width", "border-bottom-width", "border-left-width", "border-top-color", "border-right-color", "border-bottom-color", "border-left-color",
    "border-top-left-radius", "border-top-right-radius", "border-bottom-left-radius", "border-bottom-right-radius", "box-shadow", "opacity", "backdrop-filter", "filter", "outline-color", "outline-style", "outline-width", "z-index", "content", "white-space", "overflow-wrap", "text-overflow",
]
JS_COLLECT = r"""
({props, includeTokens}) => {
  let nodes = Array.from(document.querySelectorAll('[data-fp-id], [data-check]'));
  if (nodes.length === 0) {
    nodes = Array.from(document.querySelectorAll('body, .markdown-rendered, .markdown-rendered > :last-child'));
  }
  const readStyle = (node, pseudo = null) => {
    const cs = getComputedStyle(node, pseudo);
    const out = {};
    for (const prop of props) out[prop] = cs.getPropertyValue(prop).trim();
    if (includeTokens) {
      out.__tokens = {};
      for (let i = 0; i < cs.length; i++) {
        const name = cs.item(i);
        if (name.startsWith('--ogd-')) out.__tokens[name] = cs.getPropertyValue(name).trim();
      }
    }
    return out;
  };
  const out = {};
  for (const node of nodes) {
    const id = node.getAttribute('data-fp-id') || node.getAttribute('data-check') || `auto-${node.tagName.toLowerCase()}-${Object.keys(out).length + 1}`;
    const selector = node.hasAttribute('data-fp-id') || node.hasAttribute('data-check')
      ? `[${node.hasAttribute('data-fp-id') ? 'data-fp-id' : 'data-check'}="${id}"]`
      : id;
    out[id] = { selector, element: readStyle(node), before: readStyle(node, '::before'), after: readStyle(node, '::after') };
  }
  return out;
}
"""


def version() -> str:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))["version"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--theme", choices=["light", "dark"], default="light")
    parser.add_argument("--media", choices=["screen", "print"], default="screen")
    parser.add_argument("--build", choices=["theme", "v3"], default="v3")
    parser.add_argument("--include-tokens", action="store_true")
    parser.add_argument("--out", type=Path, default=None)
    parser.add_argument("--viewport-width", type=int, default=1440)
    parser.add_argument("--viewport-height", type=int, default=1400)
    args = parser.parse_args()
    try:
        from playwright.sync_api import sync_playwright
    except ModuleNotFoundError:
        print("FAIL: Playwright is not installed", file=sys.stderr)
        return 2
    fixture = args.fixture if args.fixture.is_absolute() else ROOT / args.fixture
    fixture = fixture.resolve()
    if not fixture.is_file():
        print(f"FAIL: fixture not found: {fixture}", file=sys.stderr)
        return 1
    url = fixture.as_uri()
    if args.build == "v3" and fixture == DEFAULT_FIXTURE.resolve():
        url = f"{url}?build=v3"
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={"width": args.viewport_width, "height": args.viewport_height}, device_scale_factor=1)
        page.goto(url, wait_until="networkidle")
        if args.build == "v3" and fixture != DEFAULT_FIXTURE.resolve():
            page.evaluate(
                r"""
                async (href) => {
                  const links = Array.from(document.querySelectorAll('link[rel="stylesheet"]'))
                    .filter((link) => /(?:^|\/)theme\.css(?:$|[?#])/.test(link.getAttribute('href') || link.href));
                  const targets = links.length ? links : [document.head.appendChild(document.createElement('link'))];
                  await Promise.all(targets.map((link) => new Promise((resolve, reject) => {
                    link.rel = 'stylesheet';
                    link.onload = resolve;
                    link.onerror = reject;
                    link.href = href;
                  })));
                }
                """,
                V3_BUNDLE.as_uri(),
            )
        page.evaluate("(theme) => { document.body.classList.remove('theme-light','theme-dark'); document.body.classList.add(theme === 'dark' ? 'theme-dark' : 'theme-light'); }", args.theme)
        if args.media == "print":
            page.emulate_media(media="print")
        page.wait_for_timeout(100)
        data = page.evaluate(JS_COLLECT, {"props": PROPS, "includeTokens": args.include_tokens})
        browser.close()
    release = version()
    out = args.out or (ROOT / "dev" / "MAP" / "effective-baseline" / f"v{release}" / "computed" / f"{fixture.stem}-{args.media}-{args.theme}.json")
    if not out.is_absolute():
        out = ROOT / out
    payload = {"schema": "owen-graphite/effective-snapshot/1", "version": release, "fixture": fixture.relative_to(ROOT).as_posix(), "theme": args.theme, "media": args.media, "props": PROPS, "targets": data}
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"OK: captured {len(data)} targets -> {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())