# Risk Contract: Mobile Narrow Layout

Applies to mobile and narrow-width workspace/content overflow stability.

## Owners

- General mobile workspace layout: `src/chrome/30-workspace.css`.
- Plugin/mobile embeds and Live Preview mobile behavior: `src/plugins/61-live-preview-mobile-plugin.css`.

## Boundaries

- Do not solve mobile overflow by globally shrinking desktop typography or table geometry.
- Keep mobile-specific selectors scoped to `body.is-mobile`, media queries, or the owner module's established narrow-width boundary.
- Plugin/mobile embed fixes need plugin DOM evidence or a recorded fixture gap.

## Evidence

- Check left/right pane, file explorer, editor, rendered reading content, and at least one overlay at narrow width.
- For plugin surfaces, record whether the DOM came from a real plugin or an approximation.

## Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_mobile_owner.py
.\.venv\Scripts\python.exe dev\scripts\audit_core_principles.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```