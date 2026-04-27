#!/usr/bin/env python3
"""Cross-platform validation for the Owen Graphite Obsidian theme."""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import struct
import subprocess
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TARGETS = [
    Path(r"D:\JAELE\Obsidian\.obsidian\themes\Owen Graphite"),
    Path.home() / "Work" / "Obsidian" / ".obsidian" / "themes" / "Owen Graphite",
    Path.home() / "work" / "Obsidian" / ".obsidian" / "themes" / "Owen Graphite",
]

REQUIRED_FILES = [
    "theme.css",
    "manifest.json",
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
    "snippets/zz-obsidian-gray-force-override-v2.css",
    "docs/fixtures/table-report.md",
    "docs/fixtures/table-preview.html",
    "docs/fixtures/callout-report.md",
    "docs/fixtures/callout-preview.html",
    "docs/fixtures/live-preview-editing.md",
    "scripts/contrast_audit.py",
    "scripts/visual_regression.py",
    "screenshots/light.png",
    "screenshots/dark.png",
    "screenshots/report.png",
    "screenshots/table-sample.png",
]

PNG_SIZES = {
    "screenshots/light.png": (512, 288),
    "screenshots/dark.png": (512, 288),
    "screenshots/report.png": (512, 288),
    "screenshots/table-sample.png": (1946, 1988),
}

RELEASE_ASSETS = [
    "theme.css",
    "manifest.json",
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
    "screenshots/light.png",
    "screenshots/dark.png",
    "screenshots/report.png",
    "screenshots/table-sample.png",
    "snippets/zz-obsidian-gray-force-override-v2.css",
]

FORBIDDEN_LIVE_PREVIEW_RULES = {
    re.compile(r"(?:body\s+)?\.markdown-source-view\.mod-cm6\s+\.cm-line\s*\{[^}]*margin-(?:top|bottom)\s*:\s*(?:[1-9]|0\.[1-9]|[a-zA-Z_-])[^;}]*", re.S): "non-zero margin on CM6 .cm-line",
    re.compile(r"(?:body\s+)?\.markdown-source-view\.mod-cm6\s+\.cm-line\s*\{[^}]*line-height\s*:\s*(?:[0-9]|var\(|calc\(|normal\b)[^;}]+", re.S): "global line-height override on CM6 .cm-line",
    re.compile(r"(?:body\s+)?\.markdown-source-view\.mod-cm6\s+\.cm-content\s*\{[^}]*overflow-wrap\s*:\s*anywhere", re.S): "overflow-wrap:anywhere on CM6 .cm-content",
    re.compile(r"(?:body\s+)?\.markdown-source-view\.mod-cm6\s+\.cm-content\s*\{[^}]*word-break\s*:\s*keep-all", re.S): "word-break:keep-all on CM6 .cm-content",
    re.compile(r"(?:body\s+)?\.markdown-source-view\.mod-cm6\s+[^{}]*HyperMD-quote[^{}]*\{[^}]*background(?:-color)?\s*:\s*(?:#|rgb|hsl|var\(|linear-gradient)[^;}]+", re.S): "non-transparent Live Preview quote background",
    re.compile(r"(?:body\s+)?\.markdown-source-view\.mod-cm6\s+[^{}]*HyperMD-quote[^{}]*\{[^}]*border(?:-left|-inline-start)?\s*:\s*(?:[1-9]|0\.[1-9]|[a-zA-Z_-])[^;}]*", re.S): "decorative Live Preview quote border",
    re.compile(r"(?:body\s+)?\.markdown-source-view\.mod-cm6\s+[^{}]*HyperMD-header-[3-6][^{}]*\{[^}]*z-index\s*:\s*(?:-?\d+|var\()[^;}]+", re.S): "stacking z-index on Live Preview H3-H6",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def ok(message: str) -> None:
    print(f"OK: {message}")


def read_text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def required_files() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file() or (ROOT / path).stat().st_size == 0]
    if missing:
        fail(f"missing required files: {', '.join(missing)}")
    ok("required files present")


def manifest_and_versions() -> str:
    manifest = json.loads(read_text("manifest.json"))
    version = manifest.get("version", "")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        fail(f"manifest version must be semver, got {version!r}")
    if manifest.get("name") != "Owen Graphite":
        fail("manifest name mismatch")
    if not manifest.get("minAppVersion"):
        fail("manifest missing minAppVersion")
    ok(f"manifest.json version={version}")

    changelog = read_text("CHANGELOG.md")
    readme = read_text("README.md")
    changelog_match = re.search(r"^## \[(\d+\.\d+\.\d+)\]", changelog, flags=re.M)
    if not changelog_match:
        fail("CHANGELOG missing latest version header")
    if changelog_match.group(1) != version:
        fail(f"CHANGELOG latest header {changelog_match.group(1)} does not match manifest {version}")
    readme_match = re.search(r"\| \*\*버전\*\* \| `(\d+\.\d+\.\d+)`", readme)
    if not readme_match:
        fail("README missing top-level version row")
    if readme_match.group(1) != version:
        fail(f"README version {readme_match.group(1)} does not match manifest {version}")
    ok("version markers aligned")
    return version


def no_stale_legacy_markers() -> None:
    legacy_pattern = re.compile(r"v?1\.7\.6")
    stale_hits: list[str] = []
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT).as_posix()
        if path.is_dir() or rel.startswith(".git/") or rel == ".DS_Store":
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if legacy_pattern.search(content):
            stale_hits.append(rel)
    if stale_hits:
        fail(f"stale legacy marker found in: {', '.join(stale_hits)}")
    ok("no stale legacy markers")


def style_settings_count() -> None:
    theme = read_text("theme.css")
    readme = read_text("README.md")
    settings_match = re.search(r"/\* @settings(?P<body>.*?)\*/", theme, flags=re.S)
    if not settings_match:
        fail("theme.css missing Style Settings block")
    blocks = re.split(r"\n\s*-\s*\n", settings_match.group("body"))
    option_ids = []
    for block in blocks:
        id_match = re.search(r"^\s*id:\s*([a-zA-Z0-9_-]+)", block, flags=re.M)
        if not id_match or id_match.group(1) == "owen-graphite-document":
            continue
        type_match = re.search(r"^\s*type:\s*([a-zA-Z0-9_-]+)", block, flags=re.M)
        if type_match and type_match.group(1) == "heading":
            continue
        option_ids.append(id_match.group(1))
    option_count = len(set(option_ids))
    if option_count != 27:
        fail(f"expected 27 Style Settings options, got {option_count}")
    if "27개 옵션" not in readme or "27%20options" not in readme:
        fail("README missing 27 options text/badge")
    ok(f"Style Settings option count={option_count}")


def png_dimensions() -> None:
    for path, expected in PNG_SIZES.items():
        data = (ROOT / path).read_bytes()[:24]
        if not data.startswith(b"\x89PNG\r\n\x1a\n"):
            fail(f"{path} is not a PNG")
        width, height = struct.unpack(">II", data[16:24])
        if (width, height) != expected:
            fail(f"{path} expected {expected[0]}x{expected[1]}, got {width}x{height}")
    ok("screenshot PNG dimensions match expected sizes")


def release_workflow_assets() -> None:
    workflow = read_text(".github/workflows/release.yml")
    validate_workflow = read_text(".github/workflows/validate.yml")
    missing = [asset for asset in RELEASE_ASSETS if not re.search(rf"^\s+{re.escape(asset)}\s*$", workflow, flags=re.M)]
    if missing:
        fail(f"release workflow missing assets: {', '.join(missing)}")
    if "dist/Owen-Graphite-*.zip" not in workflow:
        fail("release workflow missing generated zip asset")
    if "python scripts/validate_theme.py --ci" not in workflow:
        fail("release workflow must run Python validator")
    if "python scripts/build_release.py" not in workflow:
        fail("release workflow must build release ZIP with Python")
    if validate_workflow.count("python scripts/validate_theme.py --ci") != 1:
        fail("validate workflow must call the Python validator exactly once")
    if any(token in validate_workflow for token in ["jq ", "ruby", "validate_theme.rb"]):
        fail("validate workflow should rely on Python validation only")
    ok("release workflow includes theme files and zip asset")


def python_only_scripts() -> None:
    ruby_scripts = sorted(path.relative_to(ROOT).as_posix() for path in (ROOT / "scripts").glob("*.rb"))
    if ruby_scripts:
        fail(f"Ruby scripts are not allowed: {', '.join(ruby_scripts)}")
    gitignore = read_text(".gitignore")
    required_ignores = ["dist/", ".venv/", "__pycache__/", "*.py[cod]"]
    missing = [item for item in required_ignores if item not in gitignore]
    if missing:
        fail(f".gitignore missing Python/release artifacts: {', '.join(missing)}")
    ok("scripts are Python-only and local artifacts are ignored")


def contrast_audit() -> None:
    script = ROOT / "scripts" / "contrast_audit.py"
    spec = importlib.util.spec_from_file_location("contrast_audit", script)
    if spec is None or spec.loader is None:
        fail("unable to load scripts/contrast_audit.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    failures = []
    for pair in module.PAIRS:
        ratio = module.contrast_ratio(pair.foreground, pair.background)
        if ratio < pair.minimum:
            failures.append(f"{pair.name} ({ratio:.2f}:1)")
    if failures:
        fail(f"contrast audit failed: {', '.join(failures)}")
    ok(f"contrast audit passed ({len(module.PAIRS)} pairs)")


def release_zip_if_present(version: str) -> None:
    zip_path = ROOT / "dist" / f"Owen-Graphite-{version}.zip"
    if not zip_path.exists():
        ok("release ZIP content check skipped")
        return
    expected = [f"Owen Graphite/{asset}" for asset in RELEASE_ASSETS]
    with zipfile.ZipFile(zip_path) as archive:
        names = archive.namelist()
    missing = [name for name in expected if name not in names]
    extra = [name for name in names if name not in expected]
    if missing:
        fail(f"release ZIP missing assets: {', '.join(missing)}")
    if extra:
        fail(f"release ZIP has unexpected assets: {', '.join(extra)}")
    ok("release ZIP contents match expected manual install package")


def live_preview_guards() -> None:
    css_sources = {
        "theme.css": read_text("theme.css"),
        "snippets/zz-obsidian-gray-force-override-v2.css": read_text("snippets/zz-obsidian-gray-force-override-v2.css"),
    }
    for path, content in css_sources.items():
        for pattern, description in FORBIDDEN_LIVE_PREVIEW_RULES.items():
            if pattern.search(content):
                fail(f"{path}: {description}")
    ok("Live Preview editability guards clean")


def diff_check() -> None:
    result = subprocess.run(["git", "diff", "--check"], cwd=ROOT, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        fail(f"git diff --check failed:\n{result.stdout}{result.stderr}")
    ok("git diff --check clean")


def target_sync_check(target: Path | None, ci: bool) -> None:
    if ci:
        ok("target vault sync check skipped")
        return
    candidates = [target] if target else DEFAULT_TARGETS
    existing = next((candidate for candidate in candidates if candidate and candidate.exists()), None)
    if not existing:
        ok("target vault sync check skipped")
        return
    for rel in RELEASE_ASSETS:
        source = (ROOT / rel).read_bytes()
        target_data = (existing / rel).read_bytes()
        if source != target_data:
            fail(f"target vault asset differs: {existing / rel}")
    ok("target vault release assets are synchronized")


def release_checklist(version: str, ci: bool) -> None:
    zip_path = ROOT / "dist" / f"Owen-Graphite-{version}.zip"
    print("\nRelease checklist")
    print(f"- version: {version}")
    print("- required files: present")
    print("- Style Settings: 27 functional options")
    print("- screenshots: dimensions verified")
    print(f"- release ZIP: {'present' if zip_path.exists() else 'not built yet'}")
    print("- target vault sync: skipped in CI" if ci else "- target vault sync: checked when target exists")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ci", action="store_true", help="Skip local vault synchronization checks.")
    parser.add_argument("--target", type=Path, help="Optional Obsidian theme folder to compare theme.css and manifest.json against.")
    args = parser.parse_args()

    required_files()
    version = manifest_and_versions()
    no_stale_legacy_markers()
    style_settings_count()
    png_dimensions()
    release_workflow_assets()
    python_only_scripts()
    contrast_audit()
    release_zip_if_present(version)
    live_preview_guards()
    diff_check()
    target_sync_check(args.target, args.ci)
    release_checklist(version, args.ci)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())