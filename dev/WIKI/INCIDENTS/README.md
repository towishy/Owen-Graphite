# Incident Index

Use incidents to preserve failure patterns, wrong approaches, correct owner routes, and gates. Add an incident whenever a bug required investigation beyond a straightforward owner edit.

## Existing Incidents

| Incident | Surface | Read When | Correct Route |
| --- | --- | --- | --- |
| `table-row-inflation.md` | Live Preview markdown table widget | Table cell selection, row height, nested editors | Runtime evidence, Obsidian core boundary, owner guard |
| `direct-owner-violation.md` | CSS ownership/cascade | Late fixes, overlay repairs, speculative patches | Identify owner, remove repair layer, update WIKI/MAP |

## Required Fields For New Incidents

- Trigger and runtime state.
- Affected owner surface.
- Wrong approach to avoid.
- Evidence that would have prevented the mistake.
- Correct owner route.
- Required audits and runtime checks.
- Follow-up WIKI/MAP updates.

Use `incident-template.md` for new entries.

Use `taxonomy.md` to decide which class of incident applies.

Create a new incident scaffold with:

```powershell
.\.venv\Scripts\python.exe dev\scripts\new_incident.py --type runtime-selected-state --name table-row-height --surface table --state selected
```
