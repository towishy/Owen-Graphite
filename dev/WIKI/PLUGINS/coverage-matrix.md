# Plugin Coverage Matrix

Use this table to decide whether plugin support is backed by real DOM, an approximation, or only a documented fixture gap.

| Plugin / Surface | Real DOM Captured | Fixture Exists | Owner Confirmed | Visual Checked | Unused CSS Bucket Covered | Evidence Route |
| --- | --- | --- | --- | --- | --- | --- |
| Dataview table | partial | yes | yes | partial | plugin-runtime | `runtime-evidence-example-plugin-dom.md`, `PLUGINS/runtime-dom-notes.md`, `DOCS/v3/research/coverage-priority-fixture.html` |
| Tasks | no | yes | partial | no | plugin-runtime / document-content-fixture-gap | fixture covers task DOM; capture real task plugin DOM before compatibility claims |
| Canvas | yes | yes | yes | partial | plugin-runtime | 2026-05-25 CDP captured real node/control/card menu button/edge path states; zoom/drag behavior remains visual QA rather than selector removal evidence |
| Graph | partial | yes | yes | partial | plugin-runtime | 2026-05-25 CDP captured real graph controls/button hover including dark mode; graph canvas color classes still need visual/runtime capture before selector removal |
| Mermaid | partial | yes | partial | partial | plugin-runtime / document-content-fixture-gap | fixture covers rendered SVG output; confirm real Mermaid plugin output before compatibility claims |
| Bookmarks | no | partial | partial | no | obsidian-chrome-runtime | route through chrome/list owner and capture active/hover state |
| Outline | no | partial | partial | no | obsidian-chrome-runtime | route through chrome/list owner and capture indentation/active state |
| Backlinks / Outgoing links | yes | yes | yes | partial | state-interaction / plugin-runtime | 2026-05-25 CDP captured real pane row resting/hover states for `src/plugins/60-canvas-graph-link-panes.css` |
| Search | yes | yes | yes | partial | state-interaction / obsidian-chrome-runtime | 2026-05-25 CDP captured real Global Search result title/match rows; search input focus remains chrome/search owner evidence |

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