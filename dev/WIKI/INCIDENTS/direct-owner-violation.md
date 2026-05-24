# Incident: Direct Owner Violation

## Symptom

A fix is added later in the cascade instead of correcting the owner module.

## Wrong Approach

- Add another override.
- Treat allowed-late modules as broad owners.
- Rely on memory instead of the process gate.

## Correct Process

1. Use `QUICK-ROUTING.md` to identify the owner.
2. Remove or merge the follow-up rule.
3. Update source usage map if ownership changed.
4. Run `audit_core_principles.py`.
