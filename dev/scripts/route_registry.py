#!/usr/bin/env python3
"""Load WIKI route metadata from the generated MAP route registry."""

from __future__ import annotations

import json
import shlex
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
ROUTE_REGISTRY = ROOT / "dev" / "WIKI" / "MAP" / "route-registry.json"
OWNER_REGISTRY = ROOT / "dev" / "WIKI" / "MAP" / "owner-registry.json"


def load_route_registry() -> dict[str, Any]:
    return json.loads(ROUTE_REGISTRY.read_text(encoding="utf-8"))


def load_owner_registry() -> dict[str, Any]:
    return json.loads(OWNER_REGISTRY.read_text(encoding="utf-8"))


def routes() -> dict[str, dict[str, Any]]:
    return load_route_registry().get("routes", {})


def common_read() -> list[str]:
    return [str(item) for item in load_route_registry().get("commonRead", [])]


def route_names() -> list[str]:
    return sorted(routes())


def route_for(surface: str) -> dict[str, Any]:
    data = routes()
    if surface not in data:
        raise KeyError(surface)
    return data[surface]


def route_surfaces() -> dict[str, list[str]]:
    return {name: [str(item) for item in route.get("surfaces", [])] for name, route in routes().items()}


def check_command(check: str | dict[str, Any]) -> str:
    if isinstance(check, str):
        return check
    return str(check.get("command", ""))


def check_note(check: str | dict[str, Any]) -> str:
    if isinstance(check, str):
        return ""
    return str(check.get("note", ""))


def route_check_commands(route: dict[str, Any]) -> list[str]:
    return [command for command in (check_command(check) for check in route.get("checks", [])) if command]


def command_parts(command: str) -> list[str]:
    return shlex.split(command, posix=False)


def command_script(command: str) -> str:
    parts = command_parts(command)
    return parts[0] if parts else ""


def support_modules() -> list[dict[str, Any]]:
    return list(load_owner_registry().get("supportModules", []))