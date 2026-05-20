#!/usr/bin/env python3
"""Run the standard Owen Graphite v3 release validation sequence."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PYTHON = sys.executable


def run_step(label: str, command: list[str]) -> None:
    print(f"\n== {label} ==")
    subprocess.run(command, cwd=ROOT, check=True)


def assert_theme_fresh() -> None:
    theme = (ROOT / "theme.css").read_text(encoding="utf-8")
    bundle = (ROOT / "dist" / "theme-v3.css").read_text(encoding="utf-8")
    if theme != bundle:
        raise AssertionError("theme.css is stale vs dist/theme-v3.css; promote the fresh bundle before commit")
    print("OK: theme.css matches dist/theme-v3.css")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tag", help="Optional release tag to compare with manifest version; leading v is ignored.")
    parser.add_argument("--skip-bundle", action="store_true", help="Skip bundle rebuild but still check existing bundle freshness.")
    parser.add_argument("--include-zip", action="store_true", help="Build and audit the manual install ZIP.")
    parser.add_argument("--include-visual", action="store_true", help="Run the static visual quality fixture audit.")
    args = parser.parse_args()

    metadata_command = [PYTHON, "dev/scripts/audit_release_metadata.py"]
    if args.tag:
        metadata_command.extend(["--tag", args.tag])

    steps: list[tuple[str, list[str]]] = []
    if not args.skip_bundle:
        steps.append(("Bundle v3 CSS", [PYTHON, "dev/scripts/bundle_v3.py"]))

    steps.append(("Check bundle freshness", [PYTHON, "dev/scripts/bundle_v3.py", "--check"]))

    steps.extend(
        [
            ("Release metadata", metadata_command),
            ("Style Settings contract", [PYTHON, "dev/scripts/audit_style_settings_contract.py"]),
            ("Docs and assets", [PYTHON, "dev/scripts/audit_docs_assets.py"]),
            ("CSS compatibility budget", [PYTHON, "dev/scripts/audit_css_compat_budget.py"]),
            ("LP/PDF selector ownership", [PYTHON, "dev/scripts/audit_lp_pdf_selector_ownership.py"]),
            ("Live Preview hit routing", [PYTHON, "dev/scripts/audit_v3_hit_routing.py"]),
            ("PDF header/footer contract", [PYTHON, "dev/scripts/audit_pdf_header_footer.py"]),
            ("Duplicate selector threshold", [PYTHON, "dev/scripts/v3_audit_duplicate_selectors.py", "--threshold", "10"]),
        ]
    )

    if args.include_visual:
        steps.append(("Visual quality static fixture", [PYTHON, "dev/scripts/audit_visual_quality_fixture.py", "--static-only"]))

    if args.include_zip:
        steps.extend(
            [
                ("Build manual install ZIP", [PYTHON, "dev/scripts/build_release.py"]),
                ("Audit manual install ZIP", [PYTHON, "dev/scripts/audit_release_zip.py"]),
            ]
        )

    try:
        for label, command in steps:
            run_step(label, command)
            if label == "Check bundle freshness":
                assert_theme_fresh()
        print("\nOK: release validation sequence completed")
        return 0
    except Exception as exc:
        print(f"\nFAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())