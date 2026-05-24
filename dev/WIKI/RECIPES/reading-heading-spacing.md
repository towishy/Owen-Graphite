# Recipe: Reading Heading Spacing

## Route

- Owner: `src/base/12-reading-content.css`.
- Read: `SRC/base.md`, `VISUAL-QA.md`.
- Avoid: fixing Reading typography from late visual modules.

## Steps

1. Identify heading level and view: Reading, Live Preview, PDF.
2. Check whether the issue is typography rhythm or runtime hitbox.
3. Edit the owner module only.
4. If Live Preview or PDF also changes, follow those recipes separately.

## Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_core_principles.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```
