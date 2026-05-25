#!/usr/bin/env python3
"""Build the human-readable WIKI route registry bridge document."""

from __future__ import annotations

import argparse
from pathlib import Path

from route_registry import ROOT, check_command, check_note, common_read, normalized_check, routes, support_modules


OUT = ROOT / "dev" / "WIKI" / "MAP" / "route-registry.md"


def render() -> str:
    lines: list[str] = []
    lines.append("# WIKI Route Registry")
    lines.append("")
    lines.append("Generated from `dev/WIKI/MAP/route-registry.json`.")
    lines.append("")
    lines.append("## Common Reading")
    lines.append("")
    for item in common_read():
        lines.append(f"- `{item}`")
    lines.append("")
    lines.append("## Routes")
    lines.append("")
    lines.append("| Route | Owner | Owner Surfaces | Checks |")
    lines.append("| --- | --- | --- | --- |")
    for name, route in sorted(routes().items()):
        owner = str(route.get("owner", "")).replace("|", "\\|")
        surfaces = ", ".join(f"`{item}`" for item in route.get("surfaces", [])) or "n/a"
        checks = ", ".join(f"`{check_command(check)}`" for check in route.get("checks", []))
        lines.append(f"| `{name}` | {owner} | {surfaces} | {checks} |")
    lines.append("")
    lines.append("## Route Details")
    lines.append("")
    for name, route in sorted(routes().items()):
        lines.append(f"### {name}")
        lines.append("")
        lines.append("Read:")
        lines.append("")
        for item in route.get("read", []):
            lines.append(f"- `{item}`")
        lines.append("")
        lines.append("Contracts:")
        lines.append("")
        for item in route.get("contracts", []):
            lines.append(f"- `{item}`")
        lines.append("")
        lines.append("Checks:")
        lines.append("")
        for check in route.get("checks", []):
            model = normalized_check(check)
            note = check_note(check)
            metadata = ["safe" if model["safe"] else "manual"]
            if model["requiresPlaceholder"]:
                metadata.append("requires placeholder")
            if note:
                metadata.append(note)
            suffix = f" ({'; '.join(metadata)})"
            lines.append(f"- `{check_command(check)}`{suffix}")
        lines.append("")
    modules = support_modules()
    if modules:
        lines.append("## Registered Support Modules")
        lines.append("")
        lines.append("Support modules are not primary owners and must not be used as repair layers.")
        lines.append("")
        for item in modules:
            lines.append(f"- `{item['module']}`: {item['role']}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if the generated document is stale.")
    args = parser.parse_args()
    content = render()
    if args.check:
        if not OUT.is_file() or OUT.read_text(encoding="utf-8") != content:
            print(f"FAIL: {OUT.relative_to(ROOT)} is stale; run build_route_registry_doc.py")
            return 1
        print(f"OK: {OUT.relative_to(ROOT)} is fresh")
        return 0
    OUT.write_text(content, encoding="utf-8")
    print(f"OK: wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())