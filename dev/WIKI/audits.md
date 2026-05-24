# DEV: Audits

Core commands:

```powershell
.\.venv\Scripts\python.exe dev\scripts\wiki_route.py --list
.\.venv\Scripts\python.exe dev\scripts\wiki_route.py table
.\.venv\Scripts\python.exe dev\scripts\wiki_route.py mobile
```

Validation commands:

```powershell
.\.venv\Scripts\python.exe dev\scripts\build_source_usage_map.py --check
.\.venv\Scripts\python.exe dev\scripts\audit_core_principles.py
.\.venv\Scripts\python.exe dev\scripts\audit_wiki_consistency.py
.\.venv\Scripts\python.exe dev\scripts\audit_direct_owner_guard.py
.\.venv\Scripts\python.exe dev\scripts\audit_v3_hit_routing.py
.\.venv\Scripts\python.exe dev\scripts\audit_lp_pdf_selector_ownership.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```

Use runtime debug for selected/hover/focus issues that static audits cannot see.
