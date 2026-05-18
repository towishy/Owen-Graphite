#!/usr/bin/env python3
"""Build direct-owner migration reports from provenance snapshots."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "dev" / "MAP" / "owner-registry.json"
MANIFEST = ROOT / "manifest.json"


def version() -> str:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))["version"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provenance-dir", type=Path, default=None)
    args = parser.parse_args()
    release = version()
    provenance_dir = args.provenance_dir or (ROOT / "dev" / "MAP" / "effective-baseline" / f"v{release}" / "provenance")
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    late_modules = {
        module
        for surface in registry.get("surfaces", [])
        for module in surface.get("allowedLateModules", [])
        if str(module).startswith("src/polish/")
    }
    if not late_modules:
        policy = json.loads((ROOT / "dev" / "MAP" / "late-layer-policy.json").read_text(encoding="utf-8"))
        late_modules = set(policy.get("protectedModules", []))
    out_dir = ROOT / "dev" / "MAP" / "effective-baseline" / f"v{release}" / "reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    counts: Counter[str] = Counter()
    by_module: dict[str, list[dict[str, object]]] = defaultdict(list)
    for path in sorted(provenance_dir.glob("*.json")) if provenance_dir.is_dir() else []:
        payload = json.loads(path.read_text(encoding="utf-8"))
        for target_id, target in payload.get("targets", {}).items():
            for rule in target.get("rules", []):
                source = rule.get("source") or {}
                module = source.get("module")
                if module not in late_modules:
                    continue
                properties = sorted({decl["name"] for decl in rule.get("declarations", []) if not str(decl.get("name", "")).startswith("--")})
                row = {"snapshot": path.name, "target": target_id, "module": module, "module_line": source.get("module_line"), "selector": rule.get("selector"), "properties": properties}
                rows.append(row)
                by_module[str(module)].append(row)
                counts[str(module)] += len(properties)
    markdown = [
        "# Direct Owner Migration Candidates",
        "",
        f"Version: `{release}`",
        "",
        "This report lists late-layer matched declarations found in provenance snapshots. Treat them as migration candidates, then confirm exact winners with computed diffs before deleting rules.",
        "",
        "## Summary",
        "",
    ]
    if counts:
        for module, count in counts.most_common():
            markdown.append(f"- `{module}`: {count} matched non-token declarations")
    else:
        markdown.append("- No late-layer matched declarations found in available provenance snapshots.")
    markdown.extend(["", "## Candidates", ""])
    for row in rows[:300]:
        selector = str(row["selector"]).replace("|", "\\|")
        markdown.append(
            f"- `{row['snapshot']}` `{row['target']}` -> `{row['module']}` "
            f"line {row['module_line'] or '?'}; properties `{', '.join(row['properties'])}`; selector `{selector}`"
        )
    if not rows:
        markdown.append("- No candidates in the available provenance snapshots.")
    (out_dir / "owner-migration-candidates.md").write_text("\n".join(markdown) + "\n", encoding="utf-8")
    (out_dir / "owner-migration-candidates.json").write_text(json.dumps({"schema": "owen-graphite/owner-migration-candidates/1", "version": release, "candidates": rows}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"OK: wrote owner migration report -> {out_dir.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())