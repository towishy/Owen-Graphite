#!/usr/bin/env python3
"""Render the Live Preview / PDF parity fixture when a local browser exists."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "docs" / "v3" / "research" / "live-preview-pdf-parity-fixture.html"
THEME = ROOT / "theme.css"
OUT_DIR = ROOT / "dev" / "temp" / "visual-quality"
SCREENSHOT = OUT_DIR / "live-preview-pdf-parity.png"
PDF = OUT_DIR / "live-preview-pdf-parity.pdf"

REQUIRED_MARKERS = (
    'data-ogd-fixture="live-preview-pdf-parity"',
    'data-check="lp-callout-summary"',
    'data-check="reading-callout-summary"',
    'data-check="pdf-callout-summary"',
    'class="ogd-html-table wrap-table print-fit-table"',
    'class="ogd-token-wrap"',
    'ogd-pdf-visibility',
    'ogd-pdf-font-comfortable',
)

BROWSER_NAMES = (
    "msedge",
    "msedge.exe",
    "microsoft-edge",
    "microsoft-edge-stable",
    "google-chrome",
    "google-chrome-stable",
    "chrome",
    "chrome.exe",
    "chromium",
    "chromium-browser",
)


def windows_browser_candidates() -> list[Path]:
    candidates: list[Path] = []
    for env_name in ("ProgramFiles", "ProgramFiles(x86)", "LocalAppData"):
        base = os.environ.get(env_name)
        if not base:
            continue
        root = Path(base)
        candidates.extend(
            (
                root / "Microsoft" / "Edge" / "Application" / "msedge.exe",
                root / "Google" / "Chrome" / "Application" / "chrome.exe",
            )
        )
    return candidates


def find_browser() -> str | None:
    for name in BROWSER_NAMES:
        found = shutil.which(name)
        if found:
            return found
    for candidate in windows_browser_candidates():
        if candidate.exists():
            return str(candidate)
    return None


def validate_fixture_contract() -> None:
    if not FIXTURE.exists():
        raise FileNotFoundError(f"missing fixture: {FIXTURE}")
    if not THEME.exists():
        raise FileNotFoundError(f"missing theme: {THEME}")

    html = FIXTURE.read_text(encoding="utf-8")
    missing = [marker for marker in REQUIRED_MARKERS if marker not in html]
    if missing:
        raise AssertionError("fixture is missing required markers: " + ", ".join(missing))


def run_browser(browser: str, args: list[str]) -> subprocess.CompletedProcess[str]:
    command = [browser, "--headless=new", "--disable-gpu", "--no-first-run", *args]
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    if result.returncode == 0:
        return result

    legacy_command = [browser, "--headless", "--disable-gpu", "--no-first-run", *args]
    return subprocess.run(legacy_command, cwd=ROOT, text=True, capture_output=True, check=False)


def assert_output(path: Path, min_size: int) -> None:
    if not path.exists():
        raise AssertionError(f"browser did not create {path}")
    size = path.stat().st_size
    if size < min_size:
        raise AssertionError(f"{path} is unexpectedly small: {size} bytes")


def render(browser: str) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    fixture_uri = FIXTURE.as_uri()

    screenshot_result = run_browser(
        browser,
        [
            "--window-size=1440,1100",
            f"--screenshot={SCREENSHOT}",
            fixture_uri,
        ],
    )
    if screenshot_result.returncode != 0:
        raise RuntimeError(screenshot_result.stderr.strip() or "screenshot render failed")
    assert_output(SCREENSHOT, 20_000)

    pdf_result = run_browser(
        browser,
        [
            "--run-all-compositor-stages-before-draw",
            f"--print-to-pdf={PDF}",
            "--print-to-pdf-no-header",
            fixture_uri,
        ],
    )
    if pdf_result.returncode != 0:
        raise RuntimeError(pdf_result.stderr.strip() or "PDF render failed")
    assert_output(PDF, 10_000)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--static-only", action="store_true", help="validate fixture markers without launching a browser")
    parser.add_argument("--require-browser", action="store_true", help="fail when Chrome/Edge/Chromium is not available")
    args = parser.parse_args()

    try:
        validate_fixture_contract()
        if args.static_only:
            print("OK: visual quality fixture contract")
            return 0

        browser = find_browser()
        if not browser:
            message = "SKIP: Chrome/Edge/Chromium not found; fixture contract passed"
            print(message)
            return 2 if args.require_browser else 0

        render(browser)
        print(f"OK: rendered {SCREENSHOT.relative_to(ROOT)}")
        print(f"OK: rendered {PDF.relative_to(ROOT)}")
        return 0
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
