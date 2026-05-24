# Recipe: Coverage Plugin Runtime

## Route

- Owner: `src/plugins/*` for plugin-specific DOM; otherwise route through the core surface owner returned by `dev/scripts/wiki_route.py plugin`.
- Contract: `dev/WIKI/PLUGINS/runtime-dom-notes.md` and the surface contract for any shared table, chrome, or reading primitive.
- Read: `runtime-evidence-example-plugin-dom.md`, `RUNTIME/plugins.md`, and `PLUGINS/compatibility-matrix.md`.

## Steps

1. Choose one plugin bucket such as Dataview, Tasks, Canvas, Graph, Mermaid, or Bookmarks.
2. Capture real plugin DOM when available; if not, mark the fixture as an approximation.
3. Record plugin version, enabled state, DOM root selector, matched theme rule, owner, and fixture gap in `PLUGINS/runtime-dom-notes.md` or temporary evidence.
4. Confirm the rule does not transfer ownership of ordinary Markdown geometry to a plugin module.
5. Update `compatibility-matrix.md` when the route or support claim changes.

## Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_runtime_evidence_requirements.py --strict
.\.venv\Scripts\python.exe dev\scripts\audit_core_principles.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```