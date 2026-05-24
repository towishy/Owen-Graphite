#!/usr/bin/env python3
"""Audit local Markdown links and image assets used by project docs."""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[2]
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
README_IMAGE_RE = re.compile(r"!\[[^\]]*\]\((screenshots/[^)]+)\)|<img\s+[^>]*src=\"(screenshots/[^\"]+)\"")
SKIP_SCHEMES = {"http", "https", "mailto", "tel", "obsidian"}
DOC_GLOBS = ("README.md", "README.en.md", "CHANGELOG.md", "CONTRIBUTING.md", "screenshots/README.md", "dev/WIKI/**/*.md", "docs/**/*.md")
ASSET_LISTS = (
    ("dev/scripts/build_release.py", "DEFAULT_FILES"),
    ("dev/scripts/sync_obsidian_theme.py", "RELEASE_ASSETS"),
    ("dev/scripts/audit_release_zip.py", "REQUIRED_FILES"),
)


def iter_markdown_files() -> list[Path]:
    files: list[Path] = []
    for pattern in DOC_GLOBS:
        for path in ROOT.glob(pattern):
            if path.is_file() and path not in files:
                files.append(path)
    return sorted(files)


def clean_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        target = target[1:target.index(">")]
    elif " " in target:
        # Strip optional markdown title: [x](path "title"). Paths in this repo use percent-encoding for spaces.
        target = target.split()[0]
    return target.strip()


def is_local_file_target(target: str) -> bool:
    if not target or target.startswith("#"):
        return False
    parsed = urlparse(target)
    if parsed.scheme in SKIP_SCHEMES:
        return False
    return True


def resolve_target(source: Path, target: str) -> Path | None:
    target = clean_target(target)
    if not is_local_file_target(target):
        return None
    path_part = unquote(target.split("#", 1)[0])
    if not path_part:
        return None
    return (source.parent / path_part).resolve()


def read_constant_string_sequence(path: Path, name: str) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8-sig"), filename=str(path))
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(isinstance(target, ast.Name) and target.id == name for target in node.targets):
            continue
        if not isinstance(node.value, (ast.List, ast.Tuple)):
            raise AssertionError(f"{path.relative_to(ROOT)}:{name} is not a list/tuple")
        values: set[str] = set()
        for item in node.value.elts:
            if not isinstance(item, ast.Constant) or not isinstance(item.value, str):
                raise AssertionError(f"{path.relative_to(ROOT)}:{name} contains a non-string item")
            values.add(item.value)
        return values
    raise AssertionError(f"{path.relative_to(ROOT)} is missing {name}")


def read_github_release_assets() -> set[str]:
    path = ROOT / ".github" / "workflows" / "release.yml"
    assets: set[str] = set()
    in_files = False
    files_indent = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped == "files: |":
            in_files = True
            files_indent = len(line) - len(line.lstrip())
            continue
        if not in_files:
            continue
        indent = len(line) - len(line.lstrip())
        if stripped and indent <= files_indent:
            break
        if stripped and not any(char in stripped for char in "*${}"):
            assets.add(stripped)
    return assets


def readme_image_targets() -> set[str]:
    readme = ROOT / "README.md"
    targets: set[str] = set()
    for match in README_IMAGE_RE.finditer(readme.read_text(encoding="utf-8")):
        raw = match.group(1) or match.group(2)
        target = clean_target(raw).split("#", 1)[0]
        targets.add(unquote(target))
    return targets


def audit_readme_images_are_release_assets() -> None:
    targets = readme_image_targets()
    if not targets:
        raise AssertionError("README.md does not reference any local screenshots assets")

    containers: list[tuple[str, set[str]]] = []
    for script_rel, variable in ASSET_LISTS:
        containers.append((f"{script_rel}:{variable}", read_constant_string_sequence(ROOT / script_rel, variable)))
    containers.append((".github/workflows/release.yml:files", read_github_release_assets()))

    missing: list[str] = []
    for label, assets in containers:
        for target in sorted(targets):
            if target not in assets:
                missing.append(f"{label} missing README image asset: {target}")
    if missing:
        raise AssertionError("README image assets are not fully packaged/synced:\n" + "\n".join(missing))


def main() -> int:
    try:
        missing: list[str] = []
        for source in iter_markdown_files():
            text = source.read_text(encoding="utf-8")
            for match in LINK_RE.finditer(text):
                target_path = resolve_target(source, match.group(1))
                if target_path is None:
                    continue
                try:
                    target_path.relative_to(ROOT)
                except ValueError:
                    missing.append(f"{source.relative_to(ROOT)} -> outside repo: {match.group(1)}")
                    continue
                if not target_path.exists():
                    missing.append(f"{source.relative_to(ROOT)} -> missing: {match.group(1)}")

        if missing:
            raise AssertionError("broken local docs links:\n" + "\n".join(missing[:40]))

        audit_readme_images_are_release_assets()

        print(f"OK: docs/assets local links resolved ({len(iter_markdown_files())} markdown files)")
        return 0
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
