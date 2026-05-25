# DEV: Audits

Core commands:

```powershell
.\.venv\Scripts\python.exe dev\scripts\wiki_route.py --list
.\.venv\Scripts\python.exe dev\scripts\wiki_route.py table
.\.venv\Scripts\python.exe dev\scripts\wiki_route.py mobile
.\.venv\Scripts\python.exe dev\scripts\wiki_route.py settings
.\.venv\Scripts\python.exe dev\scripts\wiki_route.py settings --commands
.\.venv\Scripts\python.exe dev\scripts\start_work.py --surface chrome --name focus-polish
.\.venv\Scripts\python.exe dev\scripts\finish_work.py --check
.\.venv\Scripts\python.exe dev\scripts\finish_work.py --surface chrome --full-check
.\.venv\Scripts\python.exe dev\scripts\finish_work.py --full-check
.\.venv\Scripts\python.exe dev\scripts\validation_plan.py --surface chrome
.\.venv\Scripts\python.exe dev\scripts\validation_plan.py --surface chrome --surface settings
.\.venv\Scripts\python.exe dev\scripts\validation_plan.py --surface chrome --json
.\.venv\Scripts\python.exe dev\scripts\validation_plan.py --run-safe
.\.venv\Scripts\python.exe dev\scripts\validation_plan.py --full-check --run-safe
.\.venv\Scripts\python.exe dev\scripts\run_validation.py --preset core
.\.venv\Scripts\python.exe dev\scripts\run_validation.py --preset process
.\.venv\Scripts\python.exe dev\scripts\check_release_status.py --version <version>
```

Validation commands:

```powershell
.\.venv\Scripts\python.exe dev\scripts\build_source_usage_map.py --check
.\.venv\Scripts\python.exe dev\scripts\build_coverage_priority_plan.py --check
.\.venv\Scripts\python.exe dev\scripts\audit_core_principles.py
.\.venv\Scripts\python.exe dev\scripts\audit_wiki_consistency.py
.\.venv\Scripts\python.exe dev\scripts\audit_mobile_owner.py
.\.venv\Scripts\python.exe dev\scripts\audit_owner_risk_contracts.py
.\.venv\Scripts\python.exe dev\scripts\audit_route_registry.py
.\.venv\Scripts\python.exe dev\scripts\test_route_workflow.py
.\.venv\Scripts\python.exe dev\scripts\audit_wiki_route_coverage.py
.\.venv\Scripts\python.exe dev\scripts\build_route_registry_doc.py --check
.\.venv\Scripts\python.exe dev\scripts\audit_selector_owner_cheatsheet.py
.\.venv\Scripts\python.exe dev\scripts\audit_runtime_evidence_requirements.py
.\.venv\Scripts\python.exe dev\scripts\audit_direct_owner_guard.py
.\.venv\Scripts\python.exe dev\scripts\audit_v3_hit_routing.py
.\.venv\Scripts\python.exe dev\scripts\audit_lp_pdf_selector_ownership.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
.\.venv\Scripts\python.exe dev\scripts\run_validation.py --preset table
.\.venv\Scripts\python.exe dev\scripts\test_direct_owner_guard.py
```

Use runtime debug for selected/hover/focus issues that static audits cannot see.
Use `node dev\scripts\cdp_capture.mjs --status --require-vault Owen-WIKI --require-theme "Owen Graphite"` to confirm the approved Obsidian CDP port, vault, and theme before runtime captures.
