#!/usr/bin/env python3
"""Audit consistency of Owen Graphite WIKI operating rules."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


REQUIRED_FILES = [
    "dev/WIKI/VISUAL-QA.md",
    "dev/WIKI/OWNER-DECISION-TREE.md",
    "dev/WIKI/SELECTOR-OWNER-CHEATSHEET.md",
    "dev/WIKI/MAP/diff-stability.md",
    "dev/WIKI/MAP/theme-css-risk-summary.json",
    "dev/WIKI/runtime-evidence-template.md",
    "dev/WIKI/runtime-evidence-storage.md",
    "dev/WIKI/RUNTIME/README.md",
    "dev/WIKI/RUNTIME/table.md",
    "dev/WIKI/RUNTIME/chrome.md",
    "dev/WIKI/RUNTIME/pdf.md",
    "dev/WIKI/RUNTIME/plugins.md",
    "dev/WIKI/TOKENS/usage-guide.md",
    "dev/WIKI/TOKENS/state-token-map.md",
    "dev/WIKI/PLUGINS/compatibility-matrix.md",
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
]

REQUIRED_TEXT = {
    ".github/copilot-instructions.md": [
        "consult `dev/WIKI` first",
        "numeric semver",
        "never use a leading `v` prefix",
    ],
    "dev/WIKI/README.md": [
        "OWNER-DECISION-TREE.md",
        "SELECTOR-OWNER-CHEATSHEET.md",
        "VISUAL-QA.md",
        "runtime-evidence-template.md",
        "runtime-evidence-storage.md",
        "TOKENS/",
        "PLUGINS/",
        "numeric semver tags only",
    ],
    "dev/WIKI/INDEX.md": [
        "OWNER-DECISION-TREE.md",
        "SELECTOR-OWNER-CHEATSHEET.md",
        "VISUAL-QA.md",
        "runtime-evidence-template.md",
        "SRC/validation-matrix.md",
        "TOKENS/usage-guide.md",
        "PLUGINS/compatibility-matrix.md",
        "RUNTIME/README.md",
        "RECIPES/README.md",
        "INCIDENTS/incident-template.md",
        "INCIDENTS/taxonomy.md",
        "dev/scripts/wiki_route.py",
        "dev/scripts/start_work.py",
        "dev/scripts/finish_work.py",
        "dev/scripts/validation_plan.py",
        "dev/scripts/new_runtime_evidence.py",
        "dev/scripts/work_summary.py",
        "dev/scripts/audit_mobile_owner.py",
        "dev/scripts/audit_wiki_route_coverage.py",
        "dev/scripts/audit_runtime_evidence_requirements.py",
        "PROMPTS/work-summary.md",
        "WORKFLOWS/validation-matrix.md",
    ],
    "dev/WIKI/audits.md": [
        "wiki_route.py --list",
        "wiki_route.py mobile",
        "audit_wiki_consistency.py",
    ],
    "dev/WIKI/MAP/diff-stability.md": [
        "sorted keys",
        "theme-css-risk-summary.json",
        "selector-key order",
        "fix the generator ordering",
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
        "SELECTOR-OWNER-CHEATSHEET.md",
        "If ownership is still unclear",
    ],
    "dev/WIKI/SELECTOR-OWNER-CHEATSHEET.md": [
        ".cm-table-widget",
        "Obsidian core",
        "OWNER-DECISION-TREE.md",
    ],
    "dev/WIKI/runtime-evidence-template.md": [
        "Required Evidence",
        "Matched rules",
        "If this template cannot be filled",
    ],
    "dev/WIKI/runtime-evidence-storage.md": [
        "dev/TEMP/runtime-evidence",
        "new_runtime_evidence.py",
        "Permanent Evidence",
        "Minimum Metadata",
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
        "src/chrome/32-overlay-popover-dataview.css",
        "Mermaid",
        "does not transfer ownership",
    ],
    "dev/WIKI/WORKFLOWS/validation-matrix.md": [
        "Change Type",
        "Full Release-Confidence Set",
        "wiki_route.py <surface>",
    ],
    "dev/WIKI/PROMPTS/work-summary.md": [
        "WIKI consulted",
        "Owner modules changed",
        "work_summary.py",
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
    ],
    "dev/WIKI/INCIDENTS/taxonomy.md": [
        "runtime-selected-state",
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
    build_src_map = read("dev/scripts/build_src_map.py")
    light_tokens = read("src/tokens/00-light-tokens.css")
    required_routes = ["table", "live-preview", "pdf", "chrome", "plugin", "mobile", "tokens", "docs", "release"]
    missing_routes = [route for route in required_routes if f'"{route}"' not in wiki_route]
    if missing_routes:
        fail("wiki_route.py missing routes: " + ", ".join(missing_routes))
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
    for script in ("dev/scripts/new_runtime_evidence.py", "dev/scripts/work_summary.py", "dev/scripts/audit_mobile_owner.py"):
        if not (ROOT / script).is_file():
            fail(f"missing helper script: {script}")
    for script in (
        "dev/scripts/start_work.py",
        "dev/scripts/finish_work.py",
        "dev/scripts/validation_plan.py",
        "dev/scripts/release_preflight.py",
        "dev/scripts/audit_wiki_route_coverage.py",
        "dev/scripts/audit_runtime_evidence_requirements.py",
    ):
        if not (ROOT / script).is_file():
            fail(f"missing process script: {script}")
    if "last-sync.json" not in sync_script:
        fail("sync_obsidian_theme.py must record dev/TEMP/last-sync.json")
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
        assert_index_has_no_legacy_routes()
        print("OK: WIKI consistency audit clean")
        return 0
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
