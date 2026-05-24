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
    "settings-controls": "settings",
    "mobile-narrow-layout": "mobile",
    "dataview-plugin-support": "plugin",
    "pdf-base": "pdf",
    "pdf-report-polish": "pdf",
    "pdf-marginalia": "pdf",
    "style-settings-contract": "settings",
    "shared-tokens": "tokens",
}


def literal_assignment(name: str):
    tree = ast.parse((ROOT / "dev" / "scripts" / "wiki_route.py").read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(isinstance(target, ast.Name) and target.id == name for target in node.targets):
                return ast.literal_eval(node.value)
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name) and node.target.id == name:
            return ast.literal_eval(node.value)
    raise AssertionError(f"wiki_route.py is missing {name}")


def route_keys() -> set[str]:
    return set(literal_assignment("ROUTES"))


def route_surfaces() -> dict[str, list[str]]:
    value = literal_assignment("ROUTE_SURFACES")
    return {str(key): [str(item) for item in items] for key, items in value.items()}


def main() -> int:
    try:
        registry = json.loads((ROOT / "dev" / "WIKI" / "MAP" / "owner-registry.json").read_text(encoding="utf-8"))
        surfaces = {surface["id"] for surface in registry["surfaces"]}
        routes = route_keys()
        route_surface_map = route_surfaces()
        missing_surfaces = sorted(surfaces - set(EXPECTED))
        missing_routes = sorted(set(EXPECTED.values()) - routes)
        missing_registry_links = sorted(surface for surface in EXPECTED if surface not in sum(route_surface_map.values(), []))
        unknown_registry_links = sorted(surface for values in route_surface_map.values() for surface in values if surface not in surfaces)
        missing_route_surface_keys = sorted(routes - set(route_surface_map))
        if missing_surfaces:
            raise AssertionError("owner registry surfaces missing route mapping: " + ", ".join(missing_surfaces))
        if missing_routes:
            raise AssertionError("wiki_route.py missing routes used by owner registry: " + ", ".join(missing_routes))
        if missing_registry_links:
            raise AssertionError("ROUTE_SURFACES missing owner registry surfaces: " + ", ".join(missing_registry_links))
        if unknown_registry_links:
            raise AssertionError("ROUTE_SURFACES references unknown owner registry surfaces: " + ", ".join(unknown_registry_links))
        if missing_route_surface_keys:
            raise AssertionError("ROUTE_SURFACES missing route keys: " + ", ".join(missing_route_surface_keys))
        print("OK: WIKI route coverage clean")
        return 0
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())