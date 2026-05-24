# Incident: <short-name>

## Trigger

- Surface:
- Runtime state:
- User-visible symptom:

## Wrong Approach To Avoid

- 

## Evidence Required

- DOM/runtime evidence:
- Matched rules:
- Owner mapping:

## Correct Owner Route

- Owner module:
- Workflow:
- Risk contract:

## Required Gates

```powershell
.\.venv\Scripts\python.exe dev\scripts\build_source_usage_map.py --check
.\.venv\Scripts\python.exe dev\scripts\audit_core_principles.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```

## WIKI/MAP Follow-Up

- 
