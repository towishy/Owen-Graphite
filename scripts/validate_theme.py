#!/usr/bin/env python3
"""Cross-platform validation for the Owen Graphite Obsidian theme."""

from __future__ import annotations

import argparse
import json
import re
import struct
import subprocess
import sys
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
    "docs/fixtures/live-preview-editing.md",
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
    if f"## [{version}]" not in changelog:
        fail(f"CHANGELOG missing {version} header")
    if f"`{version}`" not in readme and f"v{version}" not in readme:
        fail(f"README missing {version} version")
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
    ids = re.findall(r"^\s*id:\s*([a-zA-Z0-9_-]+)", theme, flags=re.M)
    option_count = len({setting_id for setting_id in ids if setting_id != "owen-graphite-document"})
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
    missing = [asset for asset in RELEASE_ASSETS if not re.search(rf"^\s+{re.escape(asset)}\s*$", workflow, flags=re.M)]
    if missing:
        fail(f"release workflow missing assets: {', '.join(missing)}")
    if "dist/Owen-Graphite-*.zip" not in workflow:
        fail("release workflow missing generated zip asset")
    ok("release workflow includes theme files and zip asset")


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
    for rel in ["theme.css", "manifest.json"]:
        source = (ROOT / rel).read_bytes()
        target_data = (existing / rel).read_bytes()
        if source != target_data:
            fail(f"target vault theme differs: {existing / rel}")
    ok("target vault theme.css and manifest.json are synchronized")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ci", action="store_true", help="Skip local vault synchronization checks.")
    parser.add_argument("--target", type=Path, help="Optional Obsidian theme folder to compare theme.css and manifest.json against.")
    args = parser.parse_args()

    required_files()
    manifest_and_versions()
    no_stale_legacy_markers()
    style_settings_count()
    png_dimensions()
    release_workflow_assets()
    live_preview_guards()
    diff_check()
    target_sync_check(args.target, args.ci)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())