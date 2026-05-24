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

## Evidence Source

- Temporary evidence file:
- Runtime evidence schema:
- Capture tool:
- Approximation or real runtime DOM:

## Owner Decision

- Owner edit:
- No CSS fix:
- WIKI/MAP update:

## Forbidden Fix

- 

## Regression Check

- Runtime state to recheck:
- Fixture or visual scenario:
- Audit command:

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
