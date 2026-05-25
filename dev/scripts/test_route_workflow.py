#!/usr/bin/env python3
"""Unit tests for WIKI route workflow helper scripts."""

from __future__ import annotations

import unittest

import audit_route_registry
import validation_plan
from route_registry import normalized_check, route_for


class RouteWorkflowTests(unittest.TestCase):
    def test_route_registry_is_clean(self) -> None:
        self.assertEqual([], audit_route_registry.audit())

    def test_placeholder_release_check_is_manual(self) -> None:
        release = route_for("release")
        model = normalized_check(release["checks"][0])
        self.assertEqual("dev/scripts/release_check.py", model["script"])
        self.assertFalse(model["safe"])
        self.assertTrue(model["requiresPlaceholder"])

    def test_command_to_args_normalizes_windows_paths(self) -> None:
        args = validation_plan.command_to_args(".\\.venv\\Scripts\\python.exe dev\\scripts\\audit_core_principles.py")
        self.assertIsNotNone(args)
        self.assertEqual("dev/scripts/audit_core_principles.py", args[1])

    def test_plan_deduplicates_surface_and_full_check(self) -> None:
        plan = validation_plan.build_plan(["chrome"], full_check=True)
        commands = [item["command"] for item in plan["commands"]]
        self.assertEqual(len(commands), len(set(commands)))
        self.assertIn(".\\.venv\\Scripts\\python.exe dev\\scripts\\audit_core_principles.py", commands)


if __name__ == "__main__":
    unittest.main()