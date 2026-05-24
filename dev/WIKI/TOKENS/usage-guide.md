# Token Usage Guide

Use tokens before adding literal colors, shadows, spacing, or glass effects.

## Token Routes

| Need | Prefer | Avoid |
| --- | --- | --- |
| Text contrast | existing text/muted/accent tokens | one-off gray values |
| Glass surface | existing surface/rim/shadow tokens | opaque cards, heavy blur |
| Hover lift | existing shadow/elevation tokens | transform that shifts layout |
| Active state | shallow sky/rim token patterns | saturated fills |
| PDF labels | `ogd-pdf-*` tokens and preset variables | screen-only colors in print |
| Code syntax | `--ogd-code-*` tokens | unrelated accent colors |

## Rules

- Add a token only when multiple owners need the same value or the value is user-facing design intent.
- Do not create a token to hide a one-off repair.
- Do not bypass tokens with repeated literal colors.
- For dark-only behavior, route through `src/themes/50-dark.css` only when base ownership remains intact.

## Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
.\.venv\Scripts\python.exe dev\scripts\audit_style_settings_contract.py
```
