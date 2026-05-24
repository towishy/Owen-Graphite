# Plugin Runtime DOM Notes

Use this to record plugin DOM facts that static fixtures cannot prove.

## Capture Template

| Field | Value |
| --- | --- |
| Plugin / Surface |  |
| Obsidian version |  |
| Plugin version |  |
| Runtime state |  |
| DOM root selector |  |
| Matched theme rule |  |
| Source owner |  |
| Fixture gap |  |

## Evidence Rules

- Prefer real plugin DOM for plugin compatibility changes.
- If real DOM is unavailable, mark the fixture as an approximation.
- Do not remove reserved selectors from unused CSS reports solely because fixtures do not match plugin DOM.
- Update `compatibility-matrix.md` when a plugin route changes.
