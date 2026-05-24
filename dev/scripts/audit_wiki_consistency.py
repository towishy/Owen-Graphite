#!/usr/bin/env python3
"""Audit consistency of Owen Graphite WIKI operating rules."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


REQUIRED_FILES = [
    "dev/WIKI/OWNER-DECISION-TREE.md",
    "dev/WIKI/runtime-evidence-template.md",
    "dev/WIKI/INCIDENTS/README.md",
    "dev/WIKI/INCIDENTS/incident-template.md",
    "dev/WIKI/SRC/validation-matrix.md",
    "dev/WIKI/WORKFLOWS/release.md",
]

REQUIRED_TEXT = {
    ".github/copilot-instructions.md": [
        "consult `dev/WIKI` first",
        "numeric semver",
        "never use a leading `v` prefix",
    ],
    "dev/WIKI/README.md": [
        "OWNER-DECISION-TREE.md",
        "runtime-evidence-template.md",
        "numeric semver tags only",
    ],
    "dev/WIKI/INDEX.md": [
        "OWNER-DECISION-TREE.md",
        "runtime-evidence-template.md",
        "SRC/validation-matrix.md",
        "INCIDENTS/incident-template.md",
    ],
    "dev/WIKI/WORKFLOWS/release.md": [
        "git tag <version>",
        "Never run `git tag v<version>`",
        "gh release view <version>",
    ],
    "dev/WIKI/OWNER-DECISION-TREE.md": [
        "runtime evidence",
        "Obsidian core",
        "If ownership is still unclear",
    ],
    "dev/WIKI/runtime-evidence-template.md": [
        "Required Evidence",
        "Matched rules",
        "If this template cannot be filled",
    ],
    "dev/WIKI/INCIDENTS/README.md": [
        "Existing Incidents",
        "Required Fields For New Incidents",
        "incident-template.md",
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
        assert_index_has_no_legacy_routes()
        print("OK: WIKI consistency audit clean")
        return 0
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
