#!/usr/bin/env python3
"""Audit the WIKI route registry schema, links, and command references."""

from __future__ import annotations

import sys
from route_registry import ROOT, check_command, command_script, common_read, load_owner_registry, load_route_registry, normalized_check, routes


REQUIRED_ROUTE_FIELDS = {"owner", "read", "contracts", "checks", "surfaces"}


def path_exists(reference: str) -> bool:
    rel = reference.split()[0]
    if rel.startswith(("dev/", ".github/", "README", "CONTRIBUTING")):
        return (ROOT / rel).exists()
    return True


def audit() -> list[str]:
    problems: list[str] = []
    registry = load_route_registry()
    owner_registry = load_owner_registry()
    owner_surfaces = {str(item.get("id", "")) for item in owner_registry.get("surfaces", [])}

    if registry.get("schema") != "owen-graphite/route-registry/1":
        problems.append("route-registry.json has an unexpected schema")
    if not common_read():
        problems.append("route-registry.json commonRead is empty")
    for item in common_read():
        if not path_exists(item):
            problems.append(f"commonRead missing file: {item}")

    for name, route in routes().items():
        missing = sorted(REQUIRED_ROUTE_FIELDS - set(route))
        if missing:
            problems.append(f"{name}: missing fields {', '.join(missing)}")
            continue
        if not str(route.get("owner", "")).strip():
            problems.append(f"{name}: owner is empty")
        for field in ("read", "contracts"):
            values = route.get(field, [])
            if not isinstance(values, list) or not values:
                problems.append(f"{name}: {field} must be a non-empty list")
                continue
            for value in values:
                text = str(value)
                if not path_exists(text):
                    problems.append(f"{name}: {field} missing file: {text}")
        checks = route.get("checks", [])
        if not isinstance(checks, list) or not checks:
            problems.append(f"{name}: checks must be a non-empty list")
        for check in checks:
            if isinstance(check, str) or "command" in check:
                problems.append(f"{name}: checks must use structured script/args/safe fields")
                continue
            command = check_command(check)
            model = normalized_check(check)
            script = str(model["script"] or command_script(command))
            if not command:
                problems.append(f"{name}: empty check command")
                continue
            if not script:
                problems.append(f"{name}: check missing script")
            if "args" not in check or not isinstance(check.get("args"), list):
                problems.append(f"{name}: check {script} args must be a list")
            if "safe" not in check or not isinstance(check.get("safe"), bool):
                problems.append(f"{name}: check {script} safe must be boolean")
            has_placeholder = any("<" in str(arg) or ">" in str(arg) for arg in model["args"])
            if has_placeholder and not model["requiresPlaceholder"]:
                problems.append(f"{name}: check {script} has placeholder args but requiresPlaceholder is not true")
            if has_placeholder and model["safe"]:
                problems.append(f"{name}: check {script} has placeholder args but safe is true")
            if script.startswith("dev/") and not (ROOT / script).is_file():
                problems.append(f"{name}: check script missing: {script}")
        for surface in route.get("surfaces", []):
            if str(surface) not in owner_surfaces:
                problems.append(f"{name}: unknown owner surface {surface}")
    return problems


def main() -> int:
    problems = audit()
    if problems:
        print("FAIL: route registry audit failed", file=sys.stderr)
        for problem in problems:
            print(f"- {problem}", file=sys.stderr)
        return 1
    print("OK: route registry audit clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())