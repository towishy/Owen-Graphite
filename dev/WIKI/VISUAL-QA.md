# Visual QA

Use this when a change affects visible theme output. The goal is to keep Owen Graphite quiet, utilitarian, and liquid-glass consistent without adding late repair layers.

## Required View Matrix

| Surface | Minimum View | Extra State |
| --- | --- | --- |
| Reading View | Light and Dark long-form note | table, callout, code, image, embed |
| Live Preview | Light and Dark source editing | active line, selection, nested widget |
| PDF / Print | report mode and ordinary print | header/footer, page break, long table |
| Chrome | desktop wide viewport | hover, focus, active, split panes |
| Mobile / Narrow | narrow viewport or mobile class | side panes, file explorer, overflow |
| Plugin | real or fixture DOM | Dataview, Tasks, Canvas, Graph, Mermaid |

## Liquid Glass Acceptance

| State | Expected | Avoid |
| --- | --- | --- |
| Resting | white/gray frosted glass, subtle rim, restrained shadow | saturated hue, heavy glow, left rail |
| Hover | slightly brighter, lifted, wider soft downward shadow | layout shift, strong color fill |
| Active | clear but shallow sky tint or stronger rim | opaque card, disconnected tab backline |
| Focus | accessible ring that fits the surface | aggressive cyan wall, text overlap |
| Print | quiet document surface with readable hierarchy | screen-only chrome leaking into PDF |

## Text And Layout Rules

- Text must stay inside its container at desktop and mobile widths.
- Buttons and compact controls need stable dimensions.
- Do not put cards inside cards.
- Do not add left vertical accent rails.
- Use icons for tool actions when an icon exists.
- Match type scale to context: no hero-scale text inside compact panels.

## Evidence

For runtime states, fill `runtime-evidence-template.md`. For static visual claims, record the fixture, viewport, theme mode, and files touched.

After implementing any design or visible CSS change, verify the live Obsidian app through CDP before handoff:

```powershell
node dev\scripts\cdp_capture.mjs --status --require-theme "Owen Graphite"
```

Then inspect or capture the changed surface through CDP. For hover/focus/active states, save a fragment under `dev/TEMP/runtime-evidence/fragments/` and reference it from a runtime evidence note when the fix depends on that state. Static fixture rendering is supplemental; it does not replace the CDP live-app check for design changes.

## Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_docs_assets.py
.\.venv\Scripts\python.exe dev\scripts\audit_readme_svg_layout.py
.\.venv\Scripts\python.exe dev\scripts\audit_visual_quality_fixture.py --static-only
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
node dev\scripts\cdp_capture.mjs --status --require-theme "Owen Graphite"
```
