# Workflow: WIKI Maintenance

Use this when changing WIKI routing, owner registry, generated MAP bridges, runtime evidence guidance, helper scripts, or process gates.

## Owners

- Curated WIKI entry points: `dev/WIKI/README.md`, `dev/WIKI/INDEX.md`, `dev/WIKI/QUICK-ROUTING.md`.
- Owner routing: `dev/WIKI/MAP/owner-registry.json`, `dev/WIKI/MAP/route-registry.json`, `dev/WIKI/MAP/route-registry.md`, `dev/scripts/wiki_route.py`, `dev/scripts/validation_plan.py`, `dev/scripts/audit_route_registry.py`, `dev/scripts/audit_wiki_route_coverage.py`.
- Risk contracts: `dev/WIKI/MAP/*-contract.md`, `dev/scripts/audit_owner_risk_contracts.py`.
- Runtime evidence process: `dev/WIKI/runtime-evidence-*`, `dev/scripts/new_runtime_evidence.py`, `dev/scripts/audit_runtime_evidence_requirements.py`.

## Before Editing

- Run `dev/scripts/wiki_route.py docs --commands` and check whether docs-only validation is enough.
- If changing owner surfaces, update `owner-registry.json`, `route-registry.json`, route coverage, risk contracts, and regenerated source usage maps/route registry docs together.
- If adding a new WIKI page, link it from `INDEX.md` and the nearest entry point.
- If adding a new helper script, list it in `INDEX.md`, `audits.md` when relevant, and `audit_wiki_consistency.py` if it is a required process gate.
- If adding a process helper that shells out to GitHub or Git, keep pager-safe JSON output and add a dry-run mode before any push/tag behavior.
- If adding module-level runtime coverage, update `runtime-evidence-registry.json` and regenerate `MAP/coverage-priority-plan.md`.
- If adding an Owen risk-accepted exception, update `risk-accepted-registry.json`, source marker `id=`, runtime evidence, and the direct-owner guard together.
- Do not edit generated MAP outputs directly when a generator owns them.

## Required Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\build_source_usage_map.py --check
.\.venv\Scripts\python.exe dev\scripts\build_coverage_priority_plan.py --check
.\.venv\Scripts\python.exe dev\scripts\audit_wiki_consistency.py
.\.venv\Scripts\python.exe dev\scripts\audit_route_registry.py
.\.venv\Scripts\python.exe dev\scripts\test_route_workflow.py
.\.venv\Scripts\python.exe dev\scripts\audit_wiki_route_coverage.py
.\.venv\Scripts\python.exe dev\scripts\audit_owner_risk_contracts.py
.\.venv\Scripts\python.exe dev\scripts\build_route_registry_doc.py --check
.\.venv\Scripts\python.exe dev\scripts\audit_docs_assets.py
```

Run `dev/scripts/audit_core_principles.py` when the change touches owner registry, source maps, runtime evidence gates, pre-commit behavior, or release process rules.
