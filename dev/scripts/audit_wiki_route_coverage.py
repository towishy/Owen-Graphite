#!/usr/bin/env python3
"""Audit coverage between owner registry surfaces and the route registry."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from route_registry import route_surfaces


ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    try:
        registry = json.loads((ROOT / "dev" / "WIKI" / "MAP" / "owner-registry.json").read_text(encoding="utf-8"))
        surfaces = {surface["id"] for surface in registry["surfaces"]}
        route_surface_map = route_surfaces()
        linked_surfaces = {surface for values in route_surface_map.values() for surface in values}
        missing_registry_links = sorted(surfaces - linked_surfaces)
        unknown_registry_links = sorted(surface for values in route_surface_map.values() for surface in values if surface not in surfaces)
        if missing_registry_links:
            raise AssertionError("route registry missing owner registry surfaces: " + ", ".join(missing_registry_links))
        if unknown_registry_links:
            raise AssertionError("route registry references unknown owner registry surfaces: " + ", ".join(unknown_registry_links))
        print("OK: WIKI route coverage clean")
        return 0
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())