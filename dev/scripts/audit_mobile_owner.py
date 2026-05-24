#!/usr/bin/env python3
"""Audit positive `.is-mobile` selectors stay in mobile owner modules."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
ALLOWED = {
    "src/chrome/30-workspace.css",
    "src/plugins/61-live-preview-mobile-plugin.css",
}
POSITIVE_IS_MOBILE_RE = re.compile(r"(?<!not\()\.is-mobile\b")


def strip_comments(text: str) -> str:
    return re.sub(r"/\*.*?\*/", lambda match: "\n" * match.group(0).count("\n"), text, flags=re.S)


def main() -> int:
    offenders: list[str] = []
    for path in sorted(SRC.rglob("*.css")):
        rel = path.relative_to(ROOT).as_posix()
        if rel in ALLOWED:
            continue
        clean = strip_comments(path.read_text(encoding="utf-8"))
        for line_number, line in enumerate(clean.splitlines(), start=1):
            if POSITIVE_IS_MOBILE_RE.search(line):
                offenders.append(f"{rel}:{line_number}: {line.strip()[:140]}")
    if offenders:
        print("FAIL: positive .is-mobile selectors outside mobile owners:", file=sys.stderr)
        for offender in offenders[:60]:
            print(f"  - {offender}", file=sys.stderr)
        return 1
    print("OK: mobile owner audit clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())