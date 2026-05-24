# Plugin Coverage Matrix

Use this table to decide whether plugin support is backed by real DOM, an approximation, or only a documented fixture gap.

| Plugin / Surface | Real DOM Captured | Fixture Exists | Owner Confirmed | Visual Checked | Unused CSS Bucket Covered | Evidence Route |
| --- | --- | --- | --- | --- | --- | --- |
| Dataview table | partial | yes | yes | partial | plugin-runtime | `runtime-evidence-example-plugin-dom.md`, `PLUGINS/runtime-dom-notes.md`, `DOCS/v3/research/coverage-priority-fixture.html` |
| Tasks | no | yes | partial | no | plugin-runtime / document-content-fixture-gap | fixture covers task DOM; capture real task plugin DOM before compatibility claims |
| Canvas | partial | yes | yes | partial | plugin-runtime | fixture covers selected node/control state; real zoom/drag runtime capture still needed |
| Graph | no | yes | yes | no | plugin-runtime | fixture covers controls/canvas shell; capture real graph colors and dark-mode background before selector removal |
| Mermaid | partial | yes | partial | partial | plugin-runtime / document-content-fixture-gap | fixture covers rendered SVG output; confirm real Mermaid plugin output before compatibility claims |
| Bookmarks | no | partial | partial | no | obsidian-chrome-runtime | route through chrome/list owner and capture active/hover state |
| Outline | no | partial | partial | no | obsidian-chrome-runtime | route through chrome/list owner and capture indentation/active state |
| Search | partial | yes | yes | partial | state-interaction / obsidian-chrome-runtime | fixture covers selected suggestion/highlight; route through chrome/search owner and capture focus state |

## Update Rules

- Mark `Real DOM Captured` as `yes` only when an Obsidian runtime capture exists or is promoted into an incident.
- Mark `Fixture Exists` as `yes` only when a maintained fixture exercises the plugin-like DOM path.
- Mark `Owner Confirmed` as `yes` only after matched theme rules map to an owner module or a documented fixture gap.
- Do not use this matrix as deletion evidence by itself; it points to the evidence still needed.
- `DOCS/v3/research/coverage-priority-fixture.html` is fixture coverage, not real plugin DOM evidence.

## Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_runtime_evidence_requirements.py --strict
.\.venv\Scripts\python.exe dev\scripts\audit_docs_assets.py
```