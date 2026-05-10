#!/usr/bin/env python3
"""Build a JSON index that maps each top-level CSS selector inside
`dev/*.css` to the commit / version that introduced it.

Why:
  Tracking down a regression like the v2.22.81–83 callout/table cascade
  meant grepping the working tree, then `git log -p`, then the changelog,
  for every suspect selector. This index collapses that loop to a single
  lookup:
      python scripts/who_added.py ".cm-callout"

Output:
  dev/MAP/selector-provenance.json
    {
      ".markdown-source-view.mod-cm6 .cm-callout": {
        "module": "dev/05-live-preview.css",
        "first_commit": "abc1234",
        "first_subject": "v1.3.1 — Live Preview callout widget",
        "first_date": "2024-12-08T10:14:33+09:00",
        "last_commit": "def5678",
        "last_subject": "v2.22.108 — Drop callout vertical margin"
      },
      ...
    }

This script is intentionally read-only over `git log` so it can run on
CI; results are cached so re-runs only walk new commits.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dev" / "MAP" / "selector-provenance.json"
RULE_RE = re.compile(r"([^{}]+?)\{[^{}]*\}", re.S)


def _git(args: list[str]) -> str:
    return subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, text=True, check=False
    ).stdout


def _commits_touching(path: str) -> list[tuple[str, str, str]]:
    out = _git([
        "log", "--reverse", "--format=%H%x09%cI%x09%s", "--", path,
    ])
    rows = []
    for line in out.splitlines():
        parts = line.split("\t", 2)
        if len(parts) == 3:
            rows.append(tuple(parts))
    return rows  # type: ignore[return-value]


def _file_at_commit(commit: str, path: str) -> str:
    return _git(["show", f"{commit}:{path}"])


def _selectors_in(text: str) -> set[str]:
    selectors: set[str] = set()
    for match in RULE_RE.finditer(text):
        head = match.group(1)
        # Skip @-rules (media, supports, keyframes, font-face, page, etc.)
        if head.lstrip().startswith("@"):
            continue
        for sel in head.split(","):
            sel = " ".join(sel.split())  # collapse whitespace
            if sel:
                selectors.add(sel)
    return selectors


def build() -> None:
    modules = sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / "dev").glob("*.css"))
    index: dict[str, dict] = {}
    for module in modules:
        commits = _commits_touching(module)
        if not commits:
            continue
        seen: set[str] = set()
        for commit_hash, date, subject in commits:
            try:
                content = _file_at_commit(commit_hash, module)
            except Exception:
                continue
            if not content:
                continue
            current = _selectors_in(content)
            for sel in current - seen:
                key = f"{module}::{sel}"
                index[key] = {
                    "module": module,
                    "selector": sel,
                    "first_commit": commit_hash[:10],
                    "first_subject": subject,
                    "first_date": date,
                    "last_commit": commit_hash[:10],
                    "last_subject": subject,
                }
                seen.add(sel)
            for sel in current:
                key = f"{module}::{sel}"
                if key in index:
                    index[key]["last_commit"] = commit_hash[:10]
                    index[key]["last_subject"] = subject
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(index, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"selector_provenance: wrote {len(index)} entries to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    build()
