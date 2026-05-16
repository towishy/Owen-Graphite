#!/usr/bin/env python3
"""Capture a computed-style fingerprint of the Owen Graphite theme.

For every element in docs/v3/research/golden-rig/obsidian-harness.html that carries a
`data-fp-id` attribute, we record the value of a fixed list of CSS properties
resolved by the browser. The result is written to
`docs/v3/computed-fingerprint-<version>-<theme>.json`.

This file is the primary regression contract for the v3 rewrite:
the new src/ tree must produce a bit-identical fingerprint against the same
harness file. Any diff is a candidate visual regression.

Usage:
    python -m pip install playwright
    python -m playwright install chromium
    python dev/scripts/capture_computed_fingerprint.py
    python dev/scripts/capture_computed_fingerprint.py --theme dark
    python dev/scripts/capture_computed_fingerprint.py --diff baseline.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HARNESS = ROOT / "docs" / "v3" / "research" / "golden-rig" / "obsidian-harness.html"
MANIFEST = ROOT / "manifest.json"

# Properties we sample per element. Kept small enough to stay readable in diff
# output and large enough to detect any visible regression.
FINGERPRINT_PROPS = [
    # color + typography
    "color",
    "background-color",
    "background-image",
    "font-family",
    "font-size",
    "font-weight",
    "font-style",
    "line-height",
    "letter-spacing",
    "text-align",
    "text-decoration-line",
    "text-decoration-color",
    "text-transform",
    # box model
    "padding-top",
    "padding-right",
    "padding-bottom",
    "padding-left",
    "margin-top",
    "margin-right",
    "margin-bottom",
    "margin-left",
    "border-top-width",
    "border-right-width",
    "border-bottom-width",
    "border-left-width",
    "border-top-color",
    "border-right-color",
    "border-bottom-color",
    "border-left-color",
    "border-top-style",
    "border-right-style",
    "border-bottom-style",
    "border-left-style",
    "border-top-left-radius",
    "border-top-right-radius",
    "border-bottom-left-radius",
    "border-bottom-right-radius",
    # decoration / state
    "box-shadow",
    "opacity",
    "backdrop-filter",
    "filter",
    "outline-color",
    "outline-style",
    "outline-width",
    "outline-offset",
    # layout
    "display",
    "position",
    "visibility",
    "z-index",
    "cursor",
    "pointer-events",
]


def read_version() -> str:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))["version"]


def sanitize_for_filename(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]", "-", value)


JS_COLLECT = r"""
([props]) => {
  const nodes = Array.from(document.querySelectorAll('[data-fp-id]'));
  const out = {};
  for (const node of nodes) {
    const id = node.getAttribute('data-fp-id');
    const cs = window.getComputedStyle(node);
    const entry = {};
    for (const prop of props) {
      entry[prop] = cs.getPropertyValue(prop).trim();
    }
    out[id] = entry;
  }
  return out;
}
"""


def capture(theme: str, version: str, out_path: Path, build: str = "v2") -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ModuleNotFoundError:
        print(
            "ERROR: Playwright is not installed. Run: "
            "python -m pip install playwright && python -m playwright install chromium"
        )
        sys.exit(2)

    if not HARNESS.is_file():
        print(f"ERROR: harness file not found: {HARNESS}")
        sys.exit(1)

    url = HARNESS.as_uri()
    if build == "v3":
        url = f"{url}?build=v3"

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        context = browser.new_context(
            viewport={"width": 1440, "height": 2400},
            device_scale_factor=1,
        )
        page = context.new_page()
        page.goto(url, wait_until="networkidle")
        # Apply theme class. The harness ships with theme-light by default.
        page.evaluate(
            "(t) => { document.body.classList.remove('theme-light','theme-dark'); "
            "document.body.classList.add(t === 'dark' ? 'theme-dark' : 'theme-light'); }",
            theme,
        )
        # Give the browser a beat to re-evaluate.
        page.wait_for_timeout(200)
        data = page.evaluate(JS_COLLECT, [FINGERPRINT_PROPS])
        browser.close()

    payload = {
        "schema": "owen-graphite/computed-fingerprint/1",
        "version": version,
        "theme": theme,
        "build": build,
        "harness": str(HARNESS.relative_to(ROOT)).replace("\\", "/"),
        "props": FINGERPRINT_PROPS,
        "elements": data,
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    print(f"OK: captured {len(data)} elements x {len(FINGERPRINT_PROPS)} props -> {out_path.relative_to(ROOT)}")


def diff_fingerprints(baseline_path: Path, candidate_path: Path) -> int:
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    candidate = json.loads(candidate_path.read_text(encoding="utf-8"))
    b_elems = baseline.get("elements", {})
    c_elems = candidate.get("elements", {})
    failures: list[str] = []

    missing = sorted(set(b_elems) - set(c_elems))
    added = sorted(set(c_elems) - set(b_elems))
    for m in missing:
        failures.append(f"MISSING element in candidate: {m}")
    for a in added:
        failures.append(f"EXTRA element in candidate: {a}")

    for elem_id in sorted(set(b_elems) & set(c_elems)):
        b_props = b_elems[elem_id]
        c_props = c_elems[elem_id]
        for prop in sorted(set(b_props) | set(c_props)):
            bv = b_props.get(prop, "<absent>")
            cv = c_props.get(prop, "<absent>")
            if bv != cv:
                failures.append(f"  {elem_id} :: {prop}\n    - {bv}\n    + {cv}")

    if not failures:
        print(f"OK: fingerprints match ({len(b_elems)} elements)")
        return 0
    print(f"DIFF: {len(failures)} mismatching entries")
    for f in failures[:200]:
        print(f)
    if len(failures) > 200:
        print(f"... (+{len(failures) - 200} more) ...")
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--theme", choices=["light", "dark", "both"], default="both")
    parser.add_argument(
        "--build",
        choices=["v2", "v3"],
        default="v2",
        help="Which theme bundle to load in the harness. v3 = dist/theme-v3.css (default canonical), legacy = theme.css copy.",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=ROOT / "docs" / "v3",
        help="Directory for the JSON fingerprint output.",
    )
    parser.add_argument(
        "--version",
        default=None,
        help="Override the version string used in the filename. Defaults to manifest.json version.",
    )
    parser.add_argument(
        "--diff",
        type=Path,
        default=None,
        help="Path to a baseline JSON to diff against the freshly captured candidate.",
    )
    args = parser.parse_args()

    version = args.version or read_version()
    themes = ["light", "dark"] if args.theme == "both" else [args.theme]
    captured: list[Path] = []
    build_suffix = "" if args.build == "v2" else f"-{args.build}"
    for t in themes:
        filename = f"computed-fingerprint-v{sanitize_for_filename(version)}{build_suffix}-{t}.json"
        out_path = args.out_dir / filename
        capture(t, version, out_path, build=args.build)
        captured.append(out_path)

    if args.diff:
        if len(captured) != 1:
            print("ERROR: --diff requires --theme light or --theme dark (not both).")
            return 2
        return diff_fingerprints(args.diff, captured[0])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
