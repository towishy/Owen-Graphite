# Prompt: Work Summary

Use this before final response, commit, or PR text.

Generate a draft with:

```powershell
.\.venv\Scripts\python.exe dev\scripts\work_summary.py
```

The script reads `dev/TEMP/last-sync.json` and `dev/TEMP/runtime-evidence/*.json` when present.
It also emits a changelog candidate line based on the changed files.

Run the finish helper when wrapping up a task:

```powershell
.\.venv\Scripts\python.exe dev\scripts\finish_work.py --check
```

To sync Obsidian as part of wrap-up:

```powershell
.\.venv\Scripts\python.exe dev\scripts\finish_work.py --check --sync --target "D:\Owen-WIKI\.obsidian\themes\Owen Graphite"
```

## Required Summary Fields

| Field | Value |
| --- | --- |
| WIKI consulted |  |
| Owner modules changed |  |
| Runtime evidence required | yes / no |
| Runtime evidence captured | path or n/a |
| Generated artifacts refreshed | yes / no |
| Audits passed |  |
| Obsidian synced | yes / no / n/a |
| Release/tag impact | numeric tag only / n/a |

## Rules

- If runtime evidence was required but not captured, say why and do not claim runtime correctness.
- If Obsidian sync failed, include the failure and workaround status.
- If generated MAP files changed, mention whether the generator was run once after source edits.
- If release metadata changed, confirm numeric semver only and no leading `v` prefix.
