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
    if check.get("command"):
        return str(check.get("command", ""))
    script = str(check.get("script", ""))
    args = [str(arg) for arg in check.get("args", [])]
    return " ".join([script, *args]).strip()


def check_note(check: str | dict[str, Any]) -> str:
    if isinstance(check, str):
        return ""
    return str(check.get("note", ""))


def route_check_commands(route: dict[str, Any]) -> list[str]:
    return [command for command in (check_command(check) for check in route.get("checks", [])) if command]


def normalized_check(check: str | dict[str, Any]) -> dict[str, Any]:
    if isinstance(check, str):
        parts = command_parts(check)
        return {
            "script": parts[0] if parts else "",
            "args": parts[1:],
            "safe": "<" not in check and ">" not in check,
            "requiresPlaceholder": "<" in check or ">" in check,
            "note": "",
            "command": check,
        }
    command = check_command(check)
    return {
        "script": str(check.get("script") or command_script(command)),
        "args": [str(arg) for arg in check.get("args", command_parts(command)[1:])],
        "safe": bool(check.get("safe", True)),
        "requiresPlaceholder": bool(check.get("requiresPlaceholder", False)),
        "note": check_note(check),
        "command": command,
    }


def route_check_models(route: dict[str, Any]) -> list[dict[str, Any]]:
    return [normalized_check(check) for check in route.get("checks", [])]


def command_parts(command: str) -> list[str]:
    return shlex.split(command, posix=False)


def command_script(command: str) -> str:
    parts = command_parts(command)
    return parts[0] if parts else ""


def support_modules() -> list[dict[str, Any]]:
    return list(load_owner_registry().get("supportModules", []))