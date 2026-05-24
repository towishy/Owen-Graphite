#!/usr/bin/env python3
"""Print WIKI routing guidance for Owen Graphite work surfaces."""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

ROUTES: dict[str, dict[str, list[str] | str]] = {
    "table": {
        "owner": "Rendered: src/surfaces/20-reading-tables-code.css; LP HTML: src/base/13-live-preview.css + src/surfaces/24-html-table-live-preview-glass.css; LP markdown widget: Obsidian core",
        "read": ["dev/WIKI/WORKFLOWS/table.md", "dev/WIKI/RUNTIME/table.md", "dev/WIKI/SELECTOR-OWNER-CHEATSHEET.md"],
        "contracts": ["dev/WIKI/MAP/cm6-hit-routing-contract.md", "dev/WIKI/MAP/live-preview-pdf-css-map/parity-guidelines.md"],
        "checks": ["dev/scripts/audit_direct_owner_guard.py", "dev/scripts/audit_v3_hit_routing.py", "dev/scripts/audit_lp_pdf_selector_ownership.py"],
    },
    "live-preview": {
        "owner": "src/base/13-live-preview.css",
        "read": ["dev/WIKI/WORKFLOWS/live-preview-cm6.md", "dev/WIKI/RUNTIME/table.md", "dev/WIKI/runtime-evidence-template.md"],
        "contracts": ["dev/WIKI/MAP/cm6-hit-routing-contract.md"],
        "checks": ["dev/scripts/audit_v3_hit_routing.py", "dev/scripts/audit_core_principles.py"],
    },
    "pdf": {
        "owner": "src/features/41-feature-presets.css, src/features/42-report-print-polish.css, or src/features/43-print-base.css by surface",
        "read": ["dev/WIKI/WORKFLOWS/pdf.md", "dev/WIKI/RUNTIME/pdf.md", "dev/WIKI/RECIPES/pdf-label-preset.md"],
        "contracts": ["dev/WIKI/MAP/pdf-header-footer-contract.md"],
        "checks": ["dev/scripts/audit_pdf_header_footer.py", "dev/scripts/release_check.py --skip-bundle"],
    },
    "chrome": {
        "owner": "src/chrome/* according to dev/WIKI/SRC/chrome.md",
        "read": ["dev/WIKI/WORKFLOWS/chrome-ui.md", "dev/WIKI/RUNTIME/chrome.md", "dev/WIKI/SELECTOR-OWNER-CHEATSHEET.md"],
        "contracts": ["dev/WIKI/MAP/top-chrome-icon-background-contract.md when top chrome is involved"],
        "checks": ["dev/scripts/audit_core_principles.py", "dev/scripts/release_check.py --skip-bundle"],
    },
    "plugin": {
        "owner": "src/plugins/* for plugin-specific DOM; Dataview tables/inline fields currently route to src/chrome/32-overlay-popover-dataview.css; core document geometry stays with core owners",
        "read": ["dev/WIKI/PLUGINS/compatibility-matrix.md", "dev/WIKI/PLUGINS/runtime-dom-notes.md", "dev/WIKI/RUNTIME/plugins.md"],
        "contracts": ["dev/WIKI/SELECTOR-OWNER-CHEATSHEET.md"],
        "checks": ["dev/scripts/audit_core_principles.py", "dev/scripts/release_check.py --skip-bundle"],
    },
    "mobile": {
        "owner": "src/chrome/30-workspace.css for general mobile layout; src/plugins/61-live-preview-mobile-plugin.css for plugin/mobile embeds",
        "read": ["dev/WIKI/WORKFLOWS/chrome-ui.md", "dev/WIKI/RUNTIME/chrome.md", "dev/WIKI/VISUAL-QA.md"],
        "contracts": ["dev/WIKI/SRC/validation-matrix.md"],
        "checks": ["dev/scripts/audit_core_principles.py", "dev/scripts/release_check.py --skip-bundle"],
    },
    "tokens": {
        "owner": "src/tokens/00-light-tokens.css and src/tokens/01-dark-tokens.css",
        "read": ["dev/WIKI/TOKENS/usage-guide.md", "dev/WIKI/TOKENS/state-token-map.md", "dev/WIKI/VISUAL-QA.md"],
        "contracts": ["dev/WIKI/SRC/validation-matrix.md"],
        "checks": ["dev/scripts/audit_style_settings_contract.py when setting-facing", "dev/scripts/release_check.py --skip-bundle"],
    },
    "docs": {
        "owner": "dev/WIKI/DOCS/*, README files, screenshots/readme/* by publication target",
        "read": ["dev/WIKI/WORKFLOWS/docs-assets.md", "dev/WIKI/DOCS/docs-map.md", "dev/WIKI/VISUAL-QA.md"],
        "contracts": ["dev/WIKI/STRUCTURE.md"],
        "checks": ["dev/scripts/audit_docs_assets.py", "dev/scripts/audit_readme_svg_layout.py"],
    },
    "release": {
        "owner": "manifest.json, CHANGELOG.md, README.md, dev/WIKI/DOCS/v3/release-plan.md, dev/scripts/build_release.py",
        "read": ["dev/WIKI/WORKFLOWS/release.md", "dev/WIKI/DOCS/v3/release-plan.md"],
        "contracts": ["numeric semver tag only; no leading v prefix"],
        "checks": ["dev/scripts/release_check.py --tag <version>", "dev/scripts/audit_release_zip.py"],
    },
}

COMMON_READ = [
    "dev/WIKI/README.md",
    "dev/WIKI/CORE-PRINCIPLES.md",
    "dev/WIKI/QUICK-ROUTING.md",
]


def existing(path: str) -> str:
    rel = path.split()[0]
    if rel.startswith("dev/") or rel.startswith("README"):
        return "OK" if (ROOT / rel).exists() else "MISSING"
    return "INFO"


def print_route(surface: str, route: dict[str, list[str] | str]) -> None:
    print(f"# WIKI route: {surface}")
    print(f"Owner: {route['owner']}")
    print("\nRead first:")
    for item in COMMON_READ + list(route["read"]):
        print(f"- [{existing(item)}] {item}")
    print("\nContracts / boundaries:")
    for item in route["contracts"]:
        print(f"- {item}")
    print("\nChecks:")
    for item in route["checks"]:
        print(f"- .\\.venv\\Scripts\\python.exe {item}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("surface", nargs="?", choices=sorted(ROUTES), help="Work surface to route.")
    parser.add_argument("--list", action="store_true", help="List available surfaces.")
    args = parser.parse_args()

    if args.list or not args.surface:
        print("Available surfaces:")
        for key in sorted(ROUTES):
            print(f"- {key}")
        return 0 if args.list else 1

    print_route(args.surface, ROUTES[args.surface])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())