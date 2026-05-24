# Risk Contract: Shared Tokens

Applies to shared `--ogd-*` design intent and theme tokens consumed by multiple surfaces.

## Owners

- Light tokens: `src/tokens/00-light-tokens.css`.
- Dark tokens: `src/tokens/01-dark-tokens.css`.
- Dark-only adaptations may route through `src/themes/50-dark.css` only when base ownership remains intact.

## Boundaries

- Add a token only when multiple owners need the value or the value is user-facing design intent.
- Do not create a token to hide a one-off repair.
- Do not change shared tokens without checking both light and dark mode consumers.

## Evidence

- Identify at least two consumers before adding a new shared token.
- For visual token changes, review light/dark and any PDF/report consumer that depends on the token.

## Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_style_settings_contract.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```