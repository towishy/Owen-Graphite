#!/usr/bin/env python3
"""Audit coverage between owner registry surfaces and wiki_route routes."""

from __future__ import annotations

import ast
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EXPECTED = {
    "reading-typography": "table",
    "reading-tables-code": "table",
    "reading-callouts-lists": "table",
    "live-preview-cm6": "live-preview",
    "live-preview-rendered-widgets": "live-preview",
    "workspace-chrome": "chrome",
    "overlay-menu-search": "chrome",
    "mobile-narrow-layout": "mobile",
    "dataview-plugin-support": "plugin",
    "pdf-base": "pdf",
    "pdf-report-polish": "pdf",
    "pdf-marginalia": "pdf",
    "style-settings-contract": "docs",
    "shared-tokens": "tokens",
}


def route_keys() -> set[str]:
    tree = ast.parse((ROOT / "dev" / "scripts" / "wiki_route.py").read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(isinstance(target, ast.Name) and target.id == "ROUTES" for target in node.targets):
                value = ast.literal_eval(node.value)
                return set(value)
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name) and node.target.id == "ROUTES":
            value = ast.literal_eval(node.value)
            return set(value)
    raise AssertionError("wiki_route.py is missing ROUTES")


def main() -> int:
    try:
        registry = json.loads((ROOT / "dev" / "WIKI" / "MAP" / "owner-registry.json").read_text(encoding="utf-8"))
        surfaces = {surface["id"] for surface in registry["surfaces"]}
        routes = route_keys()
        missing_surfaces = sorted(surfaces - set(EXPECTED))
        missing_routes = sorted(set(EXPECTED.values()) - routes)
        if missing_surfaces:
            raise AssertionError("owner registry surfaces missing route mapping: " + ", ".join(missing_surfaces))
        if missing_routes:
            raise AssertionError("wiki_route.py missing routes used by owner registry: " + ", ".join(missing_routes))
        print("OK: WIKI route coverage clean")
        return 0
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())