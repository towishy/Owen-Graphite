# Source MAP Stabilization Checklist

## Gates

- Finding `critical = 0`: no orphan braces, unclosed blocks, or unterminated comments.
- Finding `high` must not increase unless a release note explains the Obsidian core conflict.
- CM6 hit-routing sensitive findings must be reviewed against `dev/MAP/cm6-hit-routing-contract.md`.
- Top chrome/icon changes must be reviewed against `dev/MAP/top-chrome-icon-background-contract.md`.
- PDF header/footer sensitive findings must be reviewed against `dev/MAP/pdf-header-footer-contract.md`.

## Current Finding Baseline

- critical=0
- high=0
- medium=468
- low=75
- info=0

## Current Module Baseline

- critical=0
- high=17
- medium=5
- low=3
- info=1

## Regenerate

```powershell
.\.venv\Scripts\python.exe dev\scripts\build_src_map.py
```
