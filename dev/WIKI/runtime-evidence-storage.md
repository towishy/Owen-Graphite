# Runtime Evidence Storage

Use this when runtime evidence is needed but should not become a permanent incident yet.

## Temporary Evidence

Store temporary captures under:

```text
dev/TEMP/runtime-evidence/<yyyy-mm-dd>-<surface>-<short-name>.json
```

Use this for exploratory DOM chains, computed styles, matched rules, screenshots notes, and plugin DOM probes.

Create a scaffold with:

```powershell
.\.venv\Scripts\python.exe dev\scripts\new_runtime_evidence.py --surface table --name selected-cell-height --state selected
```

Capture real Obsidian DOM/computed fragments through CDP with:

```powershell
node dev\scripts\cdp_capture.mjs --selector ".workspace" --scenario resting --out dev\TEMP\runtime-evidence\fragments\workspace.json
```

Use these examples as the expected level of detail:

```text
dev/WIKI/runtime-evidence-example-selected-tab.md
dev/WIKI/runtime-evidence-example-plugin-dom.md
```

Use strict mode when runtime correctness is part of the claim:

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_runtime_evidence_requirements.py --strict
```

Strict mode is required when the diff touches Live Preview CM6 routing, `.cm-*`, `.HyperMD-*`, `.cm-table-widget`, chrome hover/focus/active states, or plugin runtime selectors such as Mermaid, Dataview, Canvas, and Graph.

When a temporary capture proves module-level coverage for unused/reserved selector planning, record the status in `dev/WIKI/runtime-evidence-registry.json`. `dev/scripts/build_coverage_priority_plan.py` reads that registry so P0/P1 rows show whether runtime evidence is captured, partial, unavailable, or still needed.

When Owen accepts a known repository risk, record the exception in `dev/WIKI/risk-accepted-registry.json` and reference the registry id from the source marker.

Use `dev/scripts/cdp_capture.mjs --status` before capture runs when you need to confirm that Obsidian is reachable through the approved CDP port.

Promote temporary evidence into a permanent incident with:

```powershell
.\.venv\Scripts\python.exe dev\scripts\promote_evidence.py --incident table-row-height --evidence dev/TEMP/runtime-evidence/<file>.json
```

## Permanent Evidence

Promote evidence into `dev/WIKI/INCIDENTS/` only when one of these is true:

- the same mistake could recur;
- a runtime state changes owner or contract guidance;
- a workaround or forbidden approach must be remembered;
- the issue affects release, PDF, Live Preview hit routing, or plugin compatibility.

## Minimum Metadata

Each evidence note should include:

- schema fields from `dev/WIKI/runtime-evidence-schema.json`;
- surface and owner candidate;
- Obsidian version and OS when known;
- runtime state;
- DOM chain or selector root;
- matched theme rule and source module;
- decision: owner edit, no CSS fix, or WIKI/MAP update.

Temporary files in `dev/TEMP/runtime-evidence/` are local working artifacts and should not be required for release packaging.
