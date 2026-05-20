#!/usr/bin/env python3
"""Build GitHub release notes from the latest CHANGELOG section."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def manifest_version() -> str:
    data = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    return str(data["version"])


def latest_changelog_section() -> tuple[str, str]:
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    match = re.search(r"^## v(\d+\.\d+\.\d+)\s*$", changelog, re.MULTILINE)
    if not match:
        raise AssertionError("CHANGELOG.md has no latest release heading like '## vX.Y.Z'")
    start = match.end()
    next_match = re.search(r"^## v\d+\.\d+\.\d+\s*$", changelog[start:], re.MULTILINE)
    end = start + next_match.start() if next_match else len(changelog)
    return match.group(1), changelog[start:end].strip()


def build_notes(version: str, body: str) -> str:
    return f"""# Owen Graphite v{version}

## Highlights

{body}

## Validation

- `python dev/scripts/release_check.py --tag v{version}`
- `python dev/scripts/build_release.py`
- `python dev/scripts/audit_release_zip.py`

## Install Note

For manual installs, download `Owen-Graphite-{version}.zip` from the release assets. Do not use GitHub's auto-generated source archive as the theme install package.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", help="Optional path for the generated release note. Defaults to stdout.")
    args = parser.parse_args()

    try:
        version = manifest_version()
        changelog_version, body = latest_changelog_section()
        if changelog_version != version:
            raise AssertionError(f"CHANGELOG latest v{changelog_version} does not match manifest {version}")
        notes = build_notes(version, body)
        if args.output:
            output = (ROOT / args.output).resolve()
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(notes, encoding="utf-8")
            print(f"OK: wrote {output.relative_to(ROOT)}")
        else:
            print(notes)
        return 0
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())