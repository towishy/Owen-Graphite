# Plugin Coverage Matrix

Use this table to decide whether plugin support is backed by real DOM, an approximation, or only a documented fixture gap.

| Plugin / Surface | Real DOM Captured | Fixture Exists | Owner Confirmed | Visual Checked | Unused CSS Bucket Covered | Evidence Route |
| --- | --- | --- | --- | --- | --- | --- |
| Dataview table | partial | yes | yes | partial | plugin-runtime | `runtime-evidence-example-plugin-dom.md`, `PLUGINS/runtime-dom-notes.md` |
| Tasks | no | partial | partial | no | plugin-runtime / document-content-fixture-gap | capture real task plugin DOM before compatibility claims |
| Canvas | partial | no | yes | partial | plugin-runtime | `src/plugins/60-canvas-graph-link-panes.css` runtime capture needed for selected/dragged states |
| Graph | no | no | yes | no | plugin-runtime | capture graph controls and dark-mode background before selector removal |
| Mermaid | partial | partial | partial | partial | plugin-runtime / document-content-fixture-gap | capture rendered SVG/image output, not source markdown |
| Bookmarks | no | partial | partial | no | obsidian-chrome-runtime | route through chrome/list owner and capture active/hover state |
| Outline | no | partial | partial | no | obsidian-chrome-runtime | route through chrome/list owner and capture indentation/active state |
| Search | partial | yes | yes | partial | state-interaction / obsidian-chrome-runtime | route through chrome/search owner and capture focus/highlight state |

## Update Rules

- Mark `Real DOM Captured` as `yes` only when an Obsidian runtime capture exists or is promoted into an incident.
- Mark `Fixture Exists` as `yes` only when a maintained fixture exercises the plugin-like DOM path.
- Mark `Owner Confirmed` as `yes` only after matched theme rules map to an owner module or a documented fixture gap.
- Do not use this matrix as deletion evidence by itself; it points to the evidence still needed.

## Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_runtime_evidence_requirements.py --strict
.\.venv\Scripts\python.exe dev\scripts\audit_docs_assets.py
```