#!/usr/bin/env python3
"""Check GitHub Actions and GitHub Release state for a numeric Owen Graphite release."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")


def gh_json(args: list[str]) -> Any:
    env = os.environ.copy()
    env.setdefault("GH_PAGER", "cat")
    env.setdefault("PAGER", "cat")
    result = subprocess.run(["gh", *args], cwd=ROOT, text=True, capture_output=True, env=env, check=False)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or f"gh {' '.join(args)} failed")
    return json.loads(result.stdout or "null")


def latest_run_for(version: str, workflow: str) -> dict[str, Any] | None:
    runs = gh_json([
        "run",
        "list",
        "--workflow",
        workflow,
        "--limit",
        "20",
        "--json",
        "databaseId,status,conclusion,headBranch,displayTitle,url,createdAt",
    ])
    for run in runs:
        if str(run.get("headBranch")) == version:
            return dict(run)
    return None


def run_by_id(run_id: str) -> dict[str, Any]:
    return dict(gh_json(["run", "view", run_id, "--json", "databaseId,status,conclusion,headBranch,displayTitle,url,createdAt"]))


def release_for(version: str) -> dict[str, Any] | None:
    try:
        return dict(gh_json(["release", "view", version, "--json", "tagName,name,url,isDraft,isPrerelease"]))
    except RuntimeError:
        return None


def snapshot(version: str, workflow: str, run_id: str | None) -> dict[str, Any]:
    run = run_by_id(run_id) if run_id else latest_run_for(version, workflow)
    release = release_for(version)
    return {
        "schema": "owen-graphite/release-status/1",
        "checkedAt": datetime.now(timezone.utc).isoformat(),
        "version": version,
        "workflow": workflow,
        "run": run,
        "release": release,
        "ok": bool(run and run.get("status") == "completed" and run.get("conclusion") == "success" and release),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", required=True, help="Numeric semver release version, e.g. 3.1.61.")
    parser.add_argument("--workflow", default="Release", help="GitHub Actions workflow name.")
    parser.add_argument("--run-id", help="Specific GitHub Actions run id to inspect.")
    parser.add_argument("--wait", action="store_true", help="Wait until the workflow run completes or timeout is reached.")
    parser.add_argument("--timeout", type=int, default=900, help="Maximum seconds to wait with --wait.")
    parser.add_argument("--interval", type=int, default=10, help="Seconds between status checks with --wait.")
    parser.add_argument("--require-complete", action="store_true", help="Exit non-zero unless workflow succeeded and release exists.")
    parser.add_argument("--json", action="store_true", help="Print full JSON status.")
    args = parser.parse_args()

    if not SEMVER_RE.match(args.version):
        print("FAIL: version must be numeric semver without v prefix", file=sys.stderr)
        return 2

    deadline = time.monotonic() + args.timeout
    payload: dict[str, Any] = {}
    while True:
        try:
            payload = snapshot(args.version, args.workflow, args.run_id)
        except Exception as exc:
            print(f"FAIL: {exc}", file=sys.stderr)
            return 1
        run = payload.get("run") or {}
        if not args.wait or run.get("status") == "completed" or time.monotonic() >= deadline:
            break
        print(f"WAIT: {args.version} {run.get('status')} {run.get('url', '')}")
        time.sleep(max(1, args.interval))

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        run = payload.get("run") or {}
        release = payload.get("release") or {}
        print(f"Run: {run.get('status', 'missing')} / {run.get('conclusion', '')} {run.get('url', '')}")
        if release:
            print(f"Release: {release.get('name')} {release.get('url')}")
        else:
            print("Release: missing")
    if args.require_complete and not payload.get("ok"):
        print(f"FAIL: release {args.version} is not complete", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
