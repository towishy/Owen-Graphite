#!/usr/bin/env python3
"""Capture raw matched CSS rule provenance for effective snapshot targets."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "manifest.json"
DEFAULT_FIXTURE = ROOT / "dev" / "WIKI" / "DOCS" / "v3" / "research" / "golden-rig" / "obsidian-harness.html"


def version() -> str:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))["version"]


def load_line_map(release: str) -> dict[int, dict[str, object]]:
    path = ROOT / "dev" / "WIKI" / "MAP" / "effective-source-map.json"
    if not path.is_file():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    line_map: dict[int, dict[str, object]] = {}
    for source_range in payload.get("ranges", []):
        start = int(source_range.get("bundleStartLine", 0))
        end = int(source_range.get("bundleEndLine", 0))
        for dist_line in range(start, end + 1):
            line_map[dist_line] = {
                "module": source_range.get("module"),
                "module_line": int(source_range.get("sourceStartLine", 1)) + (dist_line - start),
                "dist_line": dist_line,
            }
    return line_map


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--theme", choices=["light", "dark"], default="light")
    parser.add_argument("--media", choices=["screen", "print"], default="screen")
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()
    try:
        from playwright.sync_api import sync_playwright
    except ModuleNotFoundError:
        print("FAIL: Playwright is not installed", file=sys.stderr)
        return 2
    release = version()
    line_map = load_line_map(release)
    fixture = args.fixture if args.fixture.is_absolute() else ROOT / args.fixture
    fixture = fixture.resolve()
    if not fixture.is_file():
        print(f"FAIL: fixture not found: {fixture}", file=sys.stderr)
        return 1
    url = fixture.as_uri()
    if fixture == DEFAULT_FIXTURE.resolve():
        url = f"{url}?build=v3"
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 1400})
        cdp = page.context.new_cdp_session(page)
        cdp.send("DOM.enable")
        cdp.send("CSS.enable")
        page.goto(url, wait_until="networkidle")
        page.evaluate("(theme) => { document.body.classList.remove('theme-light','theme-dark'); document.body.classList.add(theme === 'dark' ? 'theme-dark' : 'theme-light'); }", args.theme)
        if args.media == "print":
            page.emulate_media(media="print")
        ids = page.evaluate("Array.from(document.querySelectorAll('[data-fp-id], [data-check]')).map(n => ({id: n.getAttribute('data-fp-id') || n.getAttribute('data-check'), attr: n.hasAttribute('data-fp-id') ? 'data-fp-id' : 'data-check'}))")
        doc = cdp.send("DOM.getDocument", {"depth": -1, "pierce": True})["root"]["nodeId"]
        targets = {}
        for item in ids:
            selector = f"[{item['attr']}=\"{item['id']}\"]"
            node_id = cdp.send("DOM.querySelector", {"nodeId": doc, "selector": selector}).get("nodeId")
            if not node_id:
                continue
            matched = cdp.send("CSS.getMatchedStylesForNode", {"nodeId": node_id})
            rules = []
            for match in matched.get("matchedCSSRules", []):
                rule = match.get("rule", {})
                style = rule.get("style", {})
                start_line = None
                source = None
                if style.get("range"):
                    start_line = int(style["range"].get("startLine", 0)) + 1
                    mapped = line_map.get(start_line)
                    if mapped:
                        source = {"module": mapped["module"], "module_line": mapped["module_line"], "dist_line": start_line}
                declarations = []
                for prop in style.get("cssProperties", []):
                    if not prop.get("name") or prop.get("disabled"):
                        continue
                    declarations.append({"name": prop.get("name"), "value": prop.get("value"), "important": bool(prop.get("important"))})
                rules.append({"selector": rule.get("selectorList", {}).get("text", ""), "origin": rule.get("origin"), "source": source, "declarations": declarations})
            targets[item["id"]] = {"selector": selector, "rules": rules}
        browser.close()
    out = args.out or (ROOT / "dev" / "WIKI" / "effective-baseline" / f"v{release}" / "provenance" / f"{fixture.stem}-{args.media}-{args.theme}.json")
    if not out.is_absolute():
        out = ROOT / out
    payload = {"schema": "owen-graphite/provenance-snapshot/1", "version": release, "fixture": fixture.relative_to(ROOT).as_posix(), "theme": args.theme, "media": args.media, "targets": targets}
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"OK: captured provenance for {len(targets)} targets -> {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())