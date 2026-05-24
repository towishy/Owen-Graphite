#!/usr/bin/env python3
"""Process gate for Owen Graphite core principles.

This script intentionally overlaps with smaller audits. Its job is to catch
core-principle violations even when a contributor forgets the working rules.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
PYTHON = sys.executable

REQUIRED_WIKI_FILES = [
    ".github/copilot-instructions.md",
    "dev/WIKI/README.md",
    "dev/WIKI/INDEX.md",
    "dev/WIKI/CORE-PRINCIPLES.md",
    "dev/WIKI/STRUCTURE.md",
    "dev/WIKI/QUICK-ROUTING.md",
    "dev/WIKI/OWNER-DECISION-TREE.md",
    "dev/WIKI/MAP/source-usage-map.md",
    "dev/WIKI/MAP/owner-registry.json",
    "dev/WIKI/effective-baseline/v3.1.43/baseline-metadata.json",
    "dev/WIKI/DOCS/README.md",
    "dev/WIKI/DOCS/docs-map.md",
    "dev/WIKI/DOCS/v3/style-settings-contract.json",
    "dev/WIKI/DOCS/v3/release-plan.md",
    "dev/WIKI/DOCS/v3/research/golden-rig/obsidian-harness.html",
    "dev/WIKI/SRC/validation-matrix.md",
    "dev/WIKI/INCIDENTS/README.md",
    "dev/WIKI/INCIDENTS/incident-template.md",
    "dev/WIKI/runtime-evidence-template.md",
    "dev/WIKI/runtime-debug-protocol.md",
    "dev/WIKI/runtime-debug-snippets/table-cell-dump.js",
    "dev/WIKI/runtime-debug-snippets/matched-rules-dump.js",
    "dev/WIKI/PROMPTS/before-edit.md",
    "dev/WIKI/PROMPTS/review-core-principles.md",
]

FORBIDDEN_LEGACY_PATHS = [
    "dev/LLM-WIKI",
    "dev/MAP",
    "dev/effective-baseline",
    "dev/WIKI/DEV",
    "docs/v3",
]


def run(label: str, command: list[str]) -> None:
    print(f"-- {label}")
    subprocess.run(command, cwd=ROOT, check=True)


def fail(message: str) -> None:
    raise AssertionError(message)


def assert_no_src_polish() -> None:
    polish_dir = SRC / "polish"
    if polish_dir.exists():
        fail("src/polish exists; late polish layer must not be reintroduced")
    entry = (SRC / "entry.css").read_text(encoding="utf-8").lower()
    if "./polish/" in entry or "src/polish" in entry:
        fail("src/entry.css imports or references src/polish")
    print("OK: no src/polish layer")


def strip_comments(text: str) -> str:
    import re

    return re.sub(r"/\*.*?\*/", lambda match: "\n" * match.group(0).count("\n"), text, flags=re.S)


def assert_zero_important_in_src() -> None:
    offenders: list[str] = []
    for path in sorted(SRC.rglob("*.css")):
        clean = strip_comments(path.read_text(encoding="utf-8"))
        if "!important" in clean:
            rel = path.relative_to(ROOT).as_posix()
            offenders.append(rel)
    if offenders:
        fail("!important found in src CSS: " + ", ".join(offenders))
    print("OK: zero !important in src CSS")


def assert_owner_modules_exist() -> None:
    import json

    registry = json.loads((ROOT / "dev" / "WIKI" / "MAP" / "owner-registry.json").read_text(encoding="utf-8"))
    missing: list[str] = []
    for surface in registry["surfaces"]:
        for key in ("ownerModules", "allowedLateModules"):
            for module in surface.get(key, []):
                if module.startswith(("src/", "dev/")) and not (ROOT / module).is_file():
                    missing.append(f"{surface['id']}:{module}")
        for contract in surface.get("riskContracts", []):
            if contract.startswith("dev/") and not (ROOT / contract).is_file():
                missing.append(f"{surface['id']}:{contract}")
    if missing:
        fail("owner-registry references missing files: " + ", ".join(missing))
    print("OK: owner registry modules exist")


def assert_wiki_exists() -> None:
    missing = [path for path in REQUIRED_WIKI_FILES if not (ROOT / path).is_file()]
    if missing:
        fail("required WIKI files are missing: " + ", ".join(missing))
    print("OK: required WIKI files exist")


def assert_no_legacy_wiki_paths() -> None:
    present = [path for path in FORBIDDEN_LEGACY_PATHS if (ROOT / path).exists()]
    if present:
        fail("legacy folders must not be recreated: " + ", ".join(present))
    print("OK: legacy WIKI paths absent")


def assert_numeric_release_tag_policy() -> None:
    workflow = (ROOT / ".github" / "workflows" / "release.yml").read_text(encoding="utf-8")
    release_workflow = (ROOT / "dev" / "WIKI" / "WORKFLOWS" / "release.md").read_text(encoding="utf-8")
    copilot_instructions = (ROOT / ".github" / "copilot-instructions.md").read_text(encoding="utf-8")
    if '"[0-9]+.[0-9]+.[0-9]+"' not in workflow:
        fail("release workflow must trigger on numeric semver tags only")
    for path, text in (
        ("dev/WIKI/WORKFLOWS/release.md", release_workflow),
        (".github/copilot-instructions.md", copilot_instructions),
    ):
        low = text.lower()
        if "numeric semver" not in low or "v` prefix" not in low:
            fail(f"{path} must explicitly forbid v-prefixed release tags")
    print("OK: numeric release tag policy enforced")


def main() -> int:
    try:
        assert_no_src_polish()
        assert_zero_important_in_src()
        assert_owner_modules_exist()
        assert_wiki_exists()
        assert_no_legacy_wiki_paths()
        assert_numeric_release_tag_policy()
        run("WIKI consistency", [PYTHON, "dev/scripts/audit_wiki_consistency.py"])
        run("WIKI route coverage", [PYTHON, "dev/scripts/audit_wiki_route_coverage.py"])
        run("owner risk contracts", [PYTHON, "dev/scripts/audit_owner_risk_contracts.py"])
        run("selector owner cheatsheet", [PYTHON, "dev/scripts/audit_selector_owner_cheatsheet.py"])
        run("source usage map freshness", [PYTHON, "dev/scripts/build_source_usage_map.py", "--check"])
        run("direct owner guard", [PYTHON, "dev/scripts/audit_direct_owner_guard.py"])
        run("mobile owner guard", [PYTHON, "dev/scripts/audit_mobile_owner.py"])
        run("runtime evidence advisory", [PYTHON, "dev/scripts/audit_runtime_evidence_requirements.py"])
        run("LP/PDF selector ownership", [PYTHON, "dev/scripts/audit_lp_pdf_selector_ownership.py"])
        run("Live Preview hit routing", [PYTHON, "dev/scripts/audit_v3_hit_routing.py"])
        print("OK: core principles process gate clean")
        return 0
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())