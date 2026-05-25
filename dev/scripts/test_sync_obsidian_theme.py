#!/usr/bin/env python3
"""Unit tests for Obsidian sync helpers."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import sync_obsidian_theme


class SyncObsidianThemeTests(unittest.TestCase):
    def test_bundle_and_promote_isolates_sync_cli_args(self) -> None:
        calls: list[list[str] | None] = []

        class BundleModule:
            @staticmethod
            def main(argv: list[str] | None = None) -> int:
                calls.append(argv)
                return 0

        original_root = sync_obsidian_theme.ROOT
        original_load_module = sync_obsidian_theme.load_module
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dist = root / "dist" / "theme-v3.css"
            dist.parent.mkdir(parents=True)
            dist.write_text("body { color: red; }\n", encoding="utf-8")

            try:
                sync_obsidian_theme.ROOT = root
                sync_obsidian_theme.load_module = lambda _name, _path: BundleModule
                sync_obsidian_theme.bundle_and_promote()
            finally:
                sync_obsidian_theme.ROOT = original_root
                sync_obsidian_theme.load_module = original_load_module

            self.assertEqual([[]], calls)
            self.assertEqual(dist.read_text(encoding="utf-8"), (root / "theme.css").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()