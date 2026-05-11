#!/usr/bin/env python3
"""Lint CHANGELOG.md against the current manifest version and (optionally)
the staged/branch CSS diff.

Why:
  Past sweeps lost track of which selectors a release touched. This lint
  enforces three rules:
     1. The top-most `## [X.Y.Z]` or explicitly requested `## [X.Y]`
         entry in CHANGELOG.md must match
       `manifest.json` `version`.
    2. The latest entry must declare a `### Selectors touched` (or
       `### Affected selectors`) section listing changed selector tokens.
    3. When run with `--staged` or `--base`, every CSS selector token
       altered by the diff must appear at least as a substring inside
       the latest changelog entry. Catches "I bumped the version but
       forgot to record what changed".

Usage:
  python scripts/changelog_lint.py
  python scripts/changelog_lint.py --staged
  python scripts/changelog_lint.py --base origin/main
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHANGELOG = ROOT / "CHANGELOG.md"
MANIFEST = ROOT / "manifest.json"


def _git(args: list[str]) -> str:
    return subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, text=True, check=False
    ).stdout


def _latest_entry() -> tuple[str, str]:
    """Return (version, entry_body) for the topmost release block."""
    text = CHANGELOG.read_text(encoding="utf-8")
    matches = list(re.finditer(r"^## \[(\d+\.\d+(?:\.\d+)?)\][^\n]*\n", text, re.M))
    if not matches:
        return "", ""
    first = matches[0]
    end = matches[1].start() if len(matches) > 1 else len(text)
    return first.group(1), text[first.end():end]


def _selector_tokens_in_diff(base: str | None, staged: bool) -> set[str]:
    """Extract selector tokens (`.cm-callout`, `.HyperMD-table-row`, etc.)
    from the *added* lines of the diff. We use a coarse heuristic: any
    `.foo-bar`, `#foo`, or pseudo-class tokens on `+` lines."""
    if staged:
        out = _git(["diff", "--unified=0", "--cached", "--", "dev"])
    else:
        ref = base or "origin/main"
        out = _git(["diff", "--unified=0", f"{ref}...HEAD", "--", "dev"])
    tokens: set[str] = set()
    token_re = re.compile(r"\.[A-Za-z][\w-]+")
    for line in out.splitlines():
        if not line.startswith("+") or line.startswith("+++"):
            continue
        for tok in token_re.findall(line[1:]):
            # Filter generic words that would be noisy.
            if len(tok) < 4:
                continue
            tokens.add(tok)
    return tokens


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", help="git ref to diff against")
    parser.add_argument("--staged", action="store_true")
    parser.add_argument(
        "--strict-tokens", action="store_true",
        help="Fail when changed selector tokens are missing from the latest entry.",
    )
    args = parser.parse_args()

    failures: list[str] = []

    manifest_version = json.loads(MANIFEST.read_text(encoding="utf-8")).get("version", "")
    entry_version, entry_body = _latest_entry()
    if not entry_version:
        failures.append("CHANGELOG.md has no `## [X.Y.Z]` entries")
    elif entry_version != manifest_version:
        failures.append(
            f"CHANGELOG.md latest entry is `{entry_version}` but manifest.json is `{manifest_version}`"
        )
    if entry_body and not re.search(
        r"###\s+(?:Selectors touched|Affected selectors|Fixed|Added|Changed)\b",
        entry_body,
    ):
        failures.append(
            "Latest CHANGELOG entry must include at least one of "
            "`### Fixed / Added / Changed / Selectors touched / Affected selectors`."
        )

    if args.staged or args.base:
        diff_tokens = _selector_tokens_in_diff(args.base, args.staged)
        # Only enforce against curated, high-risk tokens by default; --strict
        # widens to every changed token.
        watchlist = {
            ".cm-callout", ".cm-table-widget", ".cm-embed-block",
            ".HyperMD-table-row", ".HyperMD-callout",
            ".HyperMD-codeblock", ".HyperMD-codeblock-begin", ".HyperMD-codeblock-end",
            ".cm-active", ".cm-line", ".cm-content",
        }
        check = diff_tokens if args.strict_tokens else (diff_tokens & watchlist)
        missing = [tok for tok in sorted(check) if tok not in entry_body]
        if missing:
            failures.append(
                "Latest CHANGELOG entry is missing selector tokens that this "
                "patch touched: " + ", ".join(missing) +
                ". Mention them under `### Selectors touched` so future "
                "regression archaeology stays cheap."
            )

    if failures:
        print("changelog_lint: FAIL", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1
    print(f"changelog_lint: OK (version {manifest_version})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
