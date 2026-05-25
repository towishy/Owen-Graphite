#!/usr/bin/env python3
"""Print WIKI routing guidance for Owen Graphite work surfaces."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from route_registry import check_command, check_note, common_read, route_for, route_names, route_surfaces, support_modules


ROOT = Path(__file__).resolve().parents[2]


def existing(path: str) -> str:
    rel = path.split()[0]
    if rel.startswith("dev/") or rel.startswith("README"):
        return "OK" if (ROOT / rel).exists() else "MISSING"
    return "INFO"


def registry_surfaces(surface: str) -> list[dict[str, object]]:
    wanted = set(route_surfaces().get(surface, []))
    if not wanted:
        return []
    registry = json.loads((ROOT / "dev" / "WIKI" / "MAP" / "owner-registry.json").read_text(encoding="utf-8"))
    return [item for item in registry.get("surfaces", []) if item.get("id") in wanted]


def print_route(surface: str, route: dict[str, object]) -> None:
    print(f"# WIKI route: {surface}")
    print(f"Owner: {route['owner']}")
    print("\nRead first:")
    for item in common_read() + list(route["read"]):
        print(f"- [{existing(item)}] {item}")
    print("\nContracts / boundaries:")
    for item in route["contracts"]:
        print(f"- {item}")
    registry_items = registry_surfaces(surface)
    if registry_items:
        print("\nOwner registry surfaces:")
        for item in registry_items:
            owners = ", ".join(str(value) for value in item.get("ownerModules", []))
            contracts = ", ".join(str(value) for value in item.get("riskContracts", []))
            print(f"- {item['id']}: owners={owners}; contracts={contracts}")
    modules = support_modules()
    if modules:
        print("\nRegistered support modules (not owners; not repair layers):")
        for item in modules:
            print(f"- {item['module']}: {item['role']}")
    print("\nChecks:")
    for check in route["checks"]:
        command = check_command(check)
        note = check_note(check)
        suffix = f" ({note})" if note else ""
        print(f"- .\\.venv\\Scripts\\python.exe {command}{suffix}")


def print_commands(route: dict[str, object]) -> None:
    for check in route["checks"]:
        print(f".\\.venv\\Scripts\\python.exe {check_command(check)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("surface", nargs="?", choices=route_names(), help="Work surface to route.")
    parser.add_argument("--list", action="store_true", help="List available surfaces.")
    parser.add_argument("--commands", action="store_true", help="Print only the route's check commands.")
    args = parser.parse_args()

    if args.list or not args.surface:
        print("Available surfaces:")
        for key in route_names():
            print(f"- {key}")
        return 0 if args.list else 1

    route = route_for(args.surface)
    if args.commands:
        print_commands(route)
    else:
        print_route(args.surface, route)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())