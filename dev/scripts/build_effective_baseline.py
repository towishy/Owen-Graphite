#!/usr/bin/env python3
"""Write immutable metadata for the current effective baseline release."""

from __future__ import annotations

import hashlib
import json
import os
import platform
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "manifest.json"
ENTRY = ROOT / "src" / "entry.css"
STYLE_CONTRACT = ROOT / "docs" / "v3" / "style-settings-contract.json"
IMPORT_RE = re.compile(r"@import\s+url\(\s*['\"]?([^'\")]+)['\"]?\s*\)\s*;", re.I)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def version() -> str:
    return read_json(MANIFEST)["version"]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_value(args: list[str]) -> str | None:
    try:
        result = subprocess.run(["git", *args], cwd=ROOT, text=True, capture_output=True, check=False)
    except OSError:
        return None
    if result.returncode != 0:
        return None
    return result.stdout.strip() or None


def import_order() -> list[dict[str, object]]:
    modules: list[dict[str, object]] = []
    for line_number, line in enumerate(ENTRY.read_text(encoding="utf-8").splitlines(), start=1):
        match = IMPORT_RE.search(line)
        if not match or line.strip().startswith("/*"):
            continue
        module_path = (ENTRY.parent / match.group(1)).resolve()
        modules.append(
            {
                "index": len(modules) + 1,
                "entryLine": line_number,
                "module": module_path.relative_to(ROOT).as_posix(),
                "sha256": sha256(module_path),
                "lineCount": module_path.read_text(encoding="utf-8").count("\n") + 1,
            }
        )
    return modules


def optional_file_hash(env_name: str) -> dict[str, object] | None:
    value = os.environ.get(env_name)
    if not value:
        return None
    path = Path(value)
    if not path.is_file():
        return {"path": value, "exists": False}
    return {"path": str(path), "exists": True, "sha256": sha256(path), "bytes": path.stat().st_size}


def main() -> int:
    try:
        release_version = version()
        out_dir = ROOT / "dev" / "MAP" / "effective-baseline" / f"v{release_version}"
        out_dir.mkdir(parents=True, exist_ok=True)
        contract = read_json(STYLE_CONTRACT)
        bundle_paths = [ROOT / "theme.css", ROOT / "dist" / "theme-v3.css"]
        payload: dict[str, object] = {
            "schema": "owen-graphite/effective-baseline-metadata/1",
            "version": release_version,
            "git": {
                "branch": git_value(["branch", "--show-current"]),
                "commit": git_value(["rev-parse", "HEAD"]),
            },
            "environment": {
                "platform": platform.platform(),
                "python": sys.version.split()[0],
                "obsidianVersion": os.environ.get("OBSIDIAN_VERSION"),
                "styleSettingsVersion": os.environ.get("STYLE_SETTINGS_VERSION"),
                "obsidianAppCss": optional_file_hash("OBSIDIAN_APP_CSS"),
            },
            "bundles": [
                {
                    "path": path.relative_to(ROOT).as_posix(),
                    "sha256": sha256(path),
                    "bytes": path.stat().st_size,
                    "lineCount": path.read_text(encoding="utf-8").count("\n") + 1,
                }
                for path in bundle_paths
                if path.is_file()
            ],
            "importOrder": import_order(),
            "styleSettings": {
                "contract": STYLE_CONTRACT.relative_to(ROOT).as_posix(),
                "totalEntries": contract.get("total_entries"),
                "functionalOptions": contract.get("functional_options"),
                "contractSha256": sha256(STYLE_CONTRACT),
            },
            "linkedArtifacts": {
                "ownerRegistry": "dev/MAP/owner-registry.json",
                "effectiveSourceMap": "dev/MAP/effective-source-map.json",
            },
        }
        path = out_dir / "baseline-metadata.json"
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"OK: wrote {path.relative_to(ROOT)}")
        return 0
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
