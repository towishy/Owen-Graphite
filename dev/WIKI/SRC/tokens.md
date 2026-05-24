# SRC: Tokens

- `src/tokens/00-light-tokens.css`: light and shared token defaults.
- `src/tokens/01-dark-tokens.css`: dark token overrides.

Tokens define design intent. Avoid hardcoding repeated values when a token exists.

Minimum checks: `SRC/validation-matrix.md`, `release_check.py --skip-bundle`, and Style Settings/PDF audits when a token drives settings or print output.
