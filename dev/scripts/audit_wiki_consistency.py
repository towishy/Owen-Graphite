#!/usr/bin/env python3
"""Audit consistency of Owen Graphite WIKI operating rules."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


REQUIRED_FILES = [
    "dev/WIKI/VISUAL-QA.md",
    "dev/WIKI/OWNER-DECISION-TREE.md",
    "dev/WIKI/SELECTOR-OWNER-CHEATSHEET.md",
    "dev/WIKI/MAP/diff-stability.md",
    "dev/WIKI/MAP/coverage-priority-plan.md",
    "dev/WIKI/MAP/route-registry.json",
    "dev/WIKI/MAP/route-registry.md",
    "dev/WIKI/MAP/theme-css-risk-summary.json",
    "dev/WIKI/runtime-evidence-template.md",
    "dev/WIKI/runtime-evidence-schema.json",
    "dev/WIKI/runtime-evidence-storage.md",
    "dev/WIKI/runtime-evidence-registry.json",
    "dev/WIKI/RUNTIME/README.md",
    "dev/WIKI/RUNTIME/table.md",
    "dev/WIKI/RUNTIME/chrome.md",
    "dev/WIKI/RUNTIME/pdf.md",
    "dev/WIKI/RUNTIME/plugins.md",
    "dev/WIKI/TOKENS/usage-guide.md",
    "dev/WIKI/TOKENS/state-token-map.md",
    "dev/WIKI/PLUGINS/compatibility-matrix.md",
    "dev/WIKI/PLUGINS/coverage-matrix.md",
    "dev/WIKI/PLUGINS/runtime-dom-notes.md",
    "dev/WIKI/RECIPES/README.md",
    "dev/WIKI/RECIPES/reading-heading-spacing.md",
    "dev/WIKI/RECIPES/live-preview-spacing.md",
    "dev/WIKI/RECIPES/rendered-table-polish.md",
    "dev/WIKI/RECIPES/pdf-label-preset.md",
    "dev/WIKI/RECIPES/top-chrome-state.md",
    "dev/WIKI/RECIPES/style-settings-option.md",
    "dev/WIKI/INCIDENTS/README.md",
    "dev/WIKI/INCIDENTS/incident-template.md",
    "dev/WIKI/INCIDENTS/taxonomy.md",
    "dev/WIKI/PROMPTS/work-summary.md",
    "dev/WIKI/SRC/validation-matrix.md",
    "dev/WIKI/WORKFLOWS/release.md",
    "dev/WIKI/WORKFLOWS/validation-matrix.md",
    "dev/WIKI/WORKFLOWS/wiki-maintenance.md",
]

REQUIRED_TEXT = {
    ".github/copilot-instructions.md": [
        "consult `dev/WIKI` first",
        "Owen's explicit instruction",
        "numeric semver",
        "never use a leading `v` prefix",
    ],
    "dev/WIKI/README.md": [
        "OWNER-DECISION-TREE.md",
        "SELECTOR-OWNER-CHEATSHEET.md",
        "VISUAL-QA.md",
        "runtime-evidence-template.md",
        "runtime-evidence-schema.json",
        "runtime-evidence-storage.md",
        "Owen can explicitly accept",
        "TOKENS/",
        "PLUGINS/",
        "numeric semver tags only",
    ],
    "dev/WIKI/INDEX.md": [
        "OWNER-DECISION-TREE.md",
        "SELECTOR-OWNER-CHEATSHEET.md",
        "VISUAL-QA.md",
        "runtime-evidence-template.md",
        "runtime-evidence-registry.json",
        "SRC/validation-matrix.md",
        "MAP/coverage-priority-plan.md",
        "TOKENS/usage-guide.md",
        "PLUGINS/compatibility-matrix.md",
        "PLUGINS/coverage-matrix.md",
        "RUNTIME/README.md",
        "RECIPES/README.md",
        "INCIDENTS/incident-template.md",
        "INCIDENTS/taxonomy.md",
        "dev/scripts/wiki_route.py",
        "dev/scripts/wiki_route.py <surface> --commands",
        "MAP/route-registry.json",
        "MAP/route-registry.md",
        "dev/scripts/audit_route_registry.py",
        "dev/scripts/build_route_registry_doc.py --check",
        "validation_plan.py --surface",
        "validation_plan.py --surface chrome --surface settings",
        "validation_plan.py --json",
        "finish_work.py --full-check",
        "dev/scripts/start_work.py",
        "dev/scripts/finish_work.py",
        "dev/scripts/validation_plan.py",
        "dev/scripts/new_runtime_evidence.py",
        "dev/scripts/new_incident.py",
        "dev/scripts/work_summary.py",
        "dev/scripts/build_coverage_priority_plan.py",
        "dev/scripts/audit_mobile_owner.py",
        "dev/scripts/audit_owner_risk_contracts.py",
        "dev/scripts/audit_wiki_route_coverage.py",
        "dev/scripts/audit_selector_owner_cheatsheet.py",
        "dev/scripts/audit_runtime_evidence_requirements.py",
        "dev/scripts/promote_evidence.py",
        "PROMPTS/work-summary.md",
        "WORKFLOWS/validation-matrix.md",
    ],
    "dev/WIKI/audits.md": [
        "wiki_route.py --list",
        "wiki_route.py mobile",
        "wiki_route.py settings --commands",
        "validation_plan.py --surface",
        "validation_plan.py --surface chrome --surface settings",
        "validation_plan.py --surface chrome --json",
        "validation_plan.py --full-check --run-safe",
        "finish_work.py --surface chrome --full-check",
        "finish_work.py --full-check",
        "build_coverage_priority_plan.py --check",
        "validation_plan.py --run-safe",
        "audit_owner_risk_contracts.py",
        "audit_route_registry.py",
        "test_route_workflow.py",
        "audit_selector_owner_cheatsheet.py",
        "build_route_registry_doc.py --check",
        "audit_wiki_consistency.py",
    ],
    "dev/WIKI/MAP/diff-stability.md": [
        "sorted keys",
        "theme-css-risk-summary.json",
        "selector-key order",
        "fix the generator ordering",
    ],
    "dev/WIKI/MAP/coverage-priority-plan.md": [
        "P0 State And Chrome Runtime",
        "P1 Plugin Runtime",
        "P2 Print And PDF Context",
        "Runtime evidence",
        "build_coverage_priority_plan.py --check",
    ],
    "dev/WIKI/VISUAL-QA.md": [
        "Liquid Glass Acceptance",
        "Required View Matrix",
        "runtime-evidence-template.md",
    ],
    "dev/WIKI/WORKFLOWS/release.md": [
        "git tag <version>",
        "Never run `git tag v<version>`",
        "gh release view <version>",
    ],
    "dev/WIKI/OWNER-DECISION-TREE.md": [
        "runtime evidence",
        "Obsidian core",
        "Owen explicitly accepts the risk",
        "SELECTOR-OWNER-CHEATSHEET.md",
        "If ownership is still unclear",
    ],
    "dev/WIKI/CORE-PRINCIPLES.md": [
        "Owen Risk Acceptance",
        "product-owner risk acceptance",
        "change the boundary documentation and audit rule",
    ],
    "dev/WIKI/SELECTOR-OWNER-CHEATSHEET.md": [
        ".cm-table-widget",
        "Obsidian core",
        "OWNER-DECISION-TREE.md",
    ],
    "dev/WIKI/runtime-evidence-template.md": [
        "Required Evidence",
        "runtime-evidence-schema.json",
        "Matched rules",
        "If this template cannot be filled",
    ],
    "dev/WIKI/runtime-evidence-storage.md": [
        "dev/TEMP/runtime-evidence",
        "new_runtime_evidence.py",
        "--strict",
        "promote_evidence.py",
        "Permanent Evidence",
        "Minimum Metadata",
        "runtime-evidence-schema.json",
        "runtime-evidence-registry.json",
    ],
    "dev/WIKI/runtime-evidence-registry.json": [
        "owen-graphite/runtime-evidence-registry/1",
        "src/chrome/32-overlay-popover-dataview.css",
        "src/plugins/60-canvas-graph-link-panes.css",
        "runtime-reserved",
    ],
    "dev/WIKI/RUNTIME/README.md": [
        "table.md",
        "chrome.md",
        "pdf.md",
        "plugins.md",
    ],
    "dev/WIKI/TOKENS/usage-guide.md": [
        "Use tokens before adding literal colors",
        "Do not create a token to hide a one-off repair",
    ],
    "dev/WIKI/TOKENS/state-token-map.md": [
        "Resting glass",
        "Hover",
        "Print",
    ],
    "dev/WIKI/PLUGINS/compatibility-matrix.md": [
        "Dataview",
        "coverage-matrix.md",
        "src/chrome/32-overlay-popover-dataview.css",
        "Mermaid",
        "does not transfer ownership",
    ],
    "dev/WIKI/WORKFLOWS/validation-matrix.md": [
        "Change Type",
        "Full Release-Confidence Set",
        "wiki_route.py <surface>",
        "--run-safe",
        "--surface <surface>",
        "--surface chrome --surface settings",
        "--json",
        "last-validation.json",
        "finish_work.py --full-check",
        "never builds release ZIPs",
        "pre-commit hook",
    ],
    "dev/WIKI/WORKFLOWS/wiki-maintenance.md": [
        "WIKI Maintenance",
        "audit_owner_risk_contracts.py",
        "audit_route_registry.py",
        "test_route_workflow.py",
        "route-registry.json",
        "route-registry.md",
        "build_route_registry_doc.py --check",
        "build_source_usage_map.py --check",
        "build_coverage_priority_plan.py --check",
    ],
    "dev/WIKI/PLUGINS/coverage-matrix.md": [
        "Real DOM Captured",
        "Fixture Exists",
        "Owner Confirmed",
        "Unused CSS Bucket Covered",
    ],
    "dev/WIKI/DOCS/docs-map.md": [
        "Purpose Map",
        "Runtime state issue",
        "WIKI/process change",
    ],
    "dev/WIKI/PROMPTS/work-summary.md": [
        "WIKI consulted",
        "Owner modules changed",
        "work_summary.py",
        "last-sync.json",
        "changelog candidate",
        "--sync",
        "Obsidian synced",
    ],
    "dev/WIKI/RECIPES/README.md": [
        "reading-heading-spacing.md",
        "live-preview-spacing.md",
        "style-settings-option.md",
    ],
    "dev/WIKI/INCIDENTS/README.md": [
        "Existing Incidents",
        "Required Fields For New Incidents",
        "incident-template.md",
        "taxonomy.md",
        "new_incident.py",
        "--evidence",
        "promote_evidence.py",
        "Evidence source and runtime schema link.",
        "Owner decision",
        "Forbidden fix pattern.",
        "Regression check.",
    ],
    "dev/WIKI/INCIDENTS/taxonomy.md": [
        "runtime-selected-state",
        "owen-risk-accepted",
        "release-process",
        "create an incident",
    ],
    "dev/WIKI/SRC/validation-matrix.md": [
        "Source Family",
        "Minimum Checks",
        "Runtime Rule",
    ],
    "CONTRIBUTING.md": [
        "WIKI 확인",
        "dev/WIKI/README.md",
    ],
}

SRC_DOCS = [
    "dev/WIKI/SRC/base.md",
    "dev/WIKI/SRC/surfaces.md",
    "dev/WIKI/SRC/features.md",
    "dev/WIKI/SRC/chrome.md",
    "dev/WIKI/SRC/plugins.md",
    "dev/WIKI/SRC/themes.md",
    "dev/WIKI/SRC/tokens.md",
]

FORBIDDEN_INDEX_TEXT = [
    "DEV/",
    "dev/MAP/",
    "docs/v3/",
]

RUNTIME_EVIDENCE_STATUSES = {"captured", "partial", "unavailable", "needed"}
RUNTIME_EVIDENCE_DECISIONS = {"runtime-reserved", "do-not-remove", "needs-capture", "candidate-review"}
RUNTIME_EVIDENCE_SURFACES = {"chrome", "plugin", "table", "pdf", "live-preview", "mobile", "settings"}


def fail(message: str) -> None:
    raise AssertionError(message)


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def assert_required_files() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        fail("missing WIKI consistency files: " + ", ".join(missing))
    print("OK: WIKI consistency files exist")


def assert_required_text() -> None:
    missing: list[str] = []
    for path, needles in REQUIRED_TEXT.items():
        text = read(path)
        for needle in needles:
            if needle not in text:
                missing.append(f"{path}: {needle!r}")
    if missing:
        fail("required WIKI text missing: " + "; ".join(missing))
    print("OK: WIKI required text present")


def assert_src_docs_have_validation_matrix() -> None:
    missing = [path for path in SRC_DOCS if "SRC/validation-matrix.md" not in read(path)]
    if missing:
        fail("SRC docs missing validation matrix link: " + ", ".join(missing))
    print("OK: SRC docs link validation matrix")


def assert_release_workflow_paths() -> None:
    workflow = read(".github/workflows/release.yml")
    if "dev/MAP/" in workflow:
        fail("release workflow still references dev/MAP")
    if "dev/WIKI/MAP/map-info-classification.md" not in workflow:
        fail("release workflow missing dev/WIKI/MAP artifacts")
    release_check = read("dev/scripts/release_check.py")
    if "leading v is ignored" in release_check:
        fail("release_check help must not imply v-prefixed tags are accepted")
    print("OK: release workflow uses WIKI paths and numeric tag language")


def assert_helper_and_generator_stability() -> None:
    wiki_route = read("dev/scripts/wiki_route.py")
    route_registry = read("dev/WIKI/MAP/route-registry.json")
    build_src_map = read("dev/scripts/build_src_map.py")
    light_tokens = read("src/tokens/00-light-tokens.css")
    required_routes = ["table", "live-preview", "pdf", "chrome", "plugin", "mobile", "tokens", "settings", "docs", "release"]
    missing_routes = [route for route in required_routes if f'"{route}"' not in route_registry]
    if missing_routes:
        fail("route-registry.json missing routes: " + ", ".join(missing_routes))
    if "route_registry" not in wiki_route:
        fail("wiki_route.py must load route registry metadata")
    if "sort_keys=True" not in build_src_map or "stable_selector_entries" not in build_src_map:
        fail("build_src_map.py must keep generated JSON output stable")
    for token in ("--ogd-focus-ring-border", "--ogd-focus-ring-halo", "--ogd-media-frame-bg"):
        if token not in light_tokens:
            fail(f"src/tokens/00-light-tokens.css missing shared token {token}")
    sync_script = read("dev/scripts/sync_obsidian_theme.py")
    if "copy_with_fallback" not in sync_script or "retrying with chunk copy" not in sync_script:
        fail("sync_obsidian_theme.py must keep chunk-copy fallback for WinError 483")
    release_check = read("dev/scripts/release_check.py")
    if "--include-sync" not in release_check or "--sync-target" not in release_check:
        fail("release_check.py must expose optional Obsidian sync validation")
    for script in (
        "dev/scripts/new_runtime_evidence.py",
        "dev/scripts/work_summary.py",
        "dev/scripts/build_coverage_priority_plan.py",
        "dev/scripts/build_route_registry_doc.py",
        "dev/scripts/audit_mobile_owner.py",
        "dev/scripts/test_route_workflow.py",
    ):
        if not (ROOT / script).is_file():
            fail(f"missing helper script: {script}")
    for script in (
        "dev/scripts/start_work.py",
        "dev/scripts/finish_work.py",
        "dev/scripts/validation_plan.py",
        "dev/scripts/release_preflight.py",
        "dev/scripts/audit_route_registry.py",
        "dev/scripts/audit_owner_risk_contracts.py",
        "dev/scripts/audit_wiki_route_coverage.py",
        "dev/scripts/audit_selector_owner_cheatsheet.py",
        "dev/scripts/audit_runtime_evidence_requirements.py",
        "dev/scripts/promote_evidence.py",
    ):
        if not (ROOT / script).is_file():
            fail(f"missing process script: {script}")
    if "last-sync.json" not in sync_script:
        fail("sync_obsidian_theme.py must record dev/TEMP/last-sync.json")
    coverage_plan = read("dev/scripts/build_coverage_priority_plan.py")
    if "runtime-evidence-registry.json" not in coverage_plan or "Runtime evidence" not in coverage_plan:
        fail("build_coverage_priority_plan.py must read runtime evidence registry")
    if "last_sync_summary" not in read("dev/scripts/work_summary.py"):
        fail("work_summary.py must read last sync state")
    if "--evidence" not in read("dev/scripts/new_incident.py"):
        fail("new_incident.py must support --evidence")
    validation_plan = read("dev/scripts/validation_plan.py")
    if "--run-safe" not in validation_plan or "build_release.py" not in validation_plan:
        fail("validation_plan.py must keep bounded --run-safe behavior")
    if "--surface" not in validation_plan or "--full-check" not in validation_plan or "--json" not in validation_plan or "action=\"append\"" not in validation_plan:
        fail("validation_plan.py must support route-aware and full-check planning")
    if "last-validation.json" not in validation_plan or "validation_summary" not in read("dev/scripts/work_summary.py"):
        fail("validation_plan.py/work_summary.py must maintain validation result summaries")
    if "--full-check" not in read("dev/scripts/finish_work.py"):
        fail("finish_work.py must expose --full-check")
    pre_commit = read("dev/scripts/hooks/pre-commit")
    if "validation_plan.py --run-safe" not in pre_commit or "audit_runtime_evidence_requirements.py --strict" not in pre_commit:
        fail("pre-commit hook must use diff-aware validation and strict runtime evidence checks")
    if "--verify-only" not in read("dev/scripts/sync_obsidian_theme.py"):
        fail("sync_obsidian_theme.py must support --verify-only")
    print("OK: helper routes, shared tokens, and MAP stability checks present")


def assert_wiki_schema() -> None:
    problems: list[str] = []
    for path in sorted((ROOT / "dev" / "WIKI" / "RECIPES").glob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        for heading in ("## Route", "## Steps", "## Checks"):
            if heading not in text:
                problems.append(f"{path.relative_to(ROOT).as_posix()} missing {heading}")
    for path in sorted((ROOT / "dev" / "WIKI" / "RUNTIME").glob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        if "Evidence" not in text and "Capture" not in text:
            problems.append(f"{path.relative_to(ROOT).as_posix()} missing Evidence/Capture section")
    for path in sorted((ROOT / "dev" / "WIKI" / "WORKFLOWS").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if "dev\\scripts" not in text and "dev/scripts" not in text:
            problems.append(f"{path.relative_to(ROOT).as_posix()} missing script command")
    if problems:
        fail("WIKI schema issues: " + "; ".join(problems))
    print("OK: WIKI recipe/runtime/workflow schema clean")


def assert_runtime_evidence_registry() -> None:
    path = ROOT / "dev" / "WIKI" / "runtime-evidence-registry.json"
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"runtime evidence registry invalid JSON: {exc}")
    if payload.get("schema") != "owen-graphite/runtime-evidence-registry/1":
        fail(f"runtime evidence registry unexpected schema: {payload.get('schema')!r}")
    entries = payload.get("entries")
    if not isinstance(entries, list) or not entries:
        fail("runtime evidence registry must contain non-empty entries list")
    seen: set[str] = set()
    problems: list[str] = []
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            problems.append(f"entry {index} must be object")
            continue
        missing = [key for key in ("module", "surface", "status", "decision", "evidence", "summary") if key not in entry]
        if missing:
            problems.append(f"entry {index} missing {', '.join(missing)}")
            continue
        module = str(entry["module"])
        surface = str(entry["surface"])
        status = str(entry["status"])
        decision = str(entry["decision"])
        evidence = str(entry["evidence"])
        summary = str(entry["summary"])
        if module in seen:
            problems.append(f"duplicate module {module}")
        seen.add(module)
        if not module.startswith("src/") or not (ROOT / module).is_file():
            problems.append(f"entry {module} must reference an existing src module")
        if surface not in RUNTIME_EVIDENCE_SURFACES:
            problems.append(f"entry {module} has unknown surface {surface!r}")
        if status not in RUNTIME_EVIDENCE_STATUSES:
            problems.append(f"entry {module} has unknown status {status!r}")
        if decision not in RUNTIME_EVIDENCE_DECISIONS:
            problems.append(f"entry {module} has unknown decision {decision!r}")
        if not evidence.startswith("dev/TEMP/runtime-evidence/") or not evidence.endswith(".json"):
            problems.append(f"entry {module} evidence must point at dev/TEMP/runtime-evidence/*.json")
        if not summary.strip():
            problems.append(f"entry {module} summary must be non-empty")
    if problems:
        fail("runtime evidence registry issues: " + "; ".join(problems))
    print("OK: runtime evidence registry schema clean")


def assert_index_has_no_legacy_routes() -> None:
    index = read("dev/WIKI/INDEX.md")
    offenders = [text for text in FORBIDDEN_INDEX_TEXT if text in index]
    if offenders:
        fail("WIKI index contains legacy routes: " + ", ".join(offenders))
    print("OK: WIKI index has no legacy routes")


def main() -> int:
    try:
        assert_required_files()
        assert_required_text()
        assert_src_docs_have_validation_matrix()
        assert_release_workflow_paths()
        assert_helper_and_generator_stability()
        assert_wiki_schema()
        assert_runtime_evidence_registry()
        assert_index_has_no_legacy_routes()
        print("OK: WIKI consistency audit clean")
        return 0
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
