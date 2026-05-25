#!/usr/bin/env python3
"""Audit owner-registry risk contract coverage."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "dev" / "WIKI" / "MAP" / "owner-registry.json"


def main() -> int:
    try:
        registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        missing_contracts: list[str] = []
        missing_files: list[str] = []
        for surface in registry.get("surfaces", []):
            surface_id = str(surface.get("id", "<unknown>"))
            contracts = surface.get("riskContracts", [])
            if not contracts:
                missing_contracts.append(surface_id)
                continue
            for contract in contracts:
                contract_path = str(contract)
                if contract_path.startswith("dev/") and not (ROOT / contract_path).is_file():
                    missing_files.append(f"{surface_id}:{contract_path}")
        support_problems: list[str] = []
        for support in registry.get("supportModules", []):
            module = str(support.get("module", ""))
            if not module or not support.get("role") or not support.get("description"):
                support_problems.append(module or "<unknown>")
            elif module.startswith(("src/", "dev/")) and not (ROOT / module).is_file():
                missing_files.append(f"support:{module}")
        if missing_contracts:
            raise AssertionError("owner surfaces missing riskContracts: " + ", ".join(missing_contracts))
        if missing_files:
            raise AssertionError("owner surfaces reference missing risk contract files: " + ", ".join(missing_files))
        if support_problems:
            raise AssertionError("supportModules missing module/role/description: " + ", ".join(support_problems))
        print("OK: owner risk contract coverage clean")
        return 0
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())