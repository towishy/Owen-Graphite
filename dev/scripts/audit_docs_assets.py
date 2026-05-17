#!/usr/bin/env python3
"""Audit local Markdown links and image assets used by project docs."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[2]
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
SKIP_SCHEMES = {"http", "https", "mailto", "tel", "obsidian"}
DOC_GLOBS = ("README.md", "CHANGELOG.md", "CONTRIBUTING.md", "screenshots/README.md", "docs/**/*.md")


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

        print(f"OK: docs/assets local links resolved ({len(iter_markdown_files())} markdown files)")
        return 0
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
