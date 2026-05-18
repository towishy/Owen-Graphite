#!/usr/bin/env python3
"""Build a dist/theme-v3.css to src module line-range map.

The bundle includes `/* >>> src/... */` and `/* <<< src/... */` markers. This
script records those ranges so later browser provenance captured against the
bundled stylesheet can be mapped back to source owner modules.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "dist" / "theme-v3.css"
OUT = ROOT / "dev" / "MAP" / "effective-source-map.json"
MANIFEST = ROOT / "manifest.json"
START_RE = re.compile(r"/\* >>> (?P<module>src/.+?) \*/")
END_RE = re.compile(r"/\* <<< (?P<module>src/.+?) \*/")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def version() -> str:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))["version"]


def build_map() -> dict[str, object]:
    if not BUNDLE.is_file():
        raise FileNotFoundError("dist/theme-v3.css missing; run dev/scripts/bundle_v3.py")
    stack: list[tuple[str, int]] = []
    ranges: list[dict[str, object]] = []
    lines = BUNDLE.read_text(encoding="utf-8").splitlines()
    for line_number, line in enumerate(lines, start=1):
        start = START_RE.search(line)
        if start:
            stack.append((start.group("module"), line_number + 1))
            continue
        end = END_RE.search(line)
        if end:
            module = end.group("module")
            if not stack:
                raise AssertionError(f"unmatched bundle end marker at line {line_number}: {module}")
            start_module, start_line = stack.pop()
            if start_module != module:
                raise AssertionError(f"bundle marker mismatch: {start_module} ended by {module}")
            ranges.append(
                {
                    "module": module,
                    "bundleStartLine": start_line,
                    "bundleEndLine": line_number - 1,
                    "sourceStartLine": 1,
                    "sourceEndLine": max(1, line_number - start_line),
                }
            )
    if stack:
        raise AssertionError("unclosed bundle markers: " + ", ".join(module for module, _ in stack))
    return {
        "schema": "owen-graphite/effective-source-map/1",
        "version": version(),
        "bundle": BUNDLE.relative_to(ROOT).as_posix(),
        "bundleSha256": sha256(BUNDLE),
        "rangeCount": len(ranges),
        "ranges": ranges,
    }


def main() -> int:
    try:
        payload = build_map()
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"OK: wrote {OUT.relative_to(ROOT)} ({payload['rangeCount']} ranges)")
        return 0
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())