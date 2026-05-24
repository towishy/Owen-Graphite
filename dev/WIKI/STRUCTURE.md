# WIKI Structure

`dev/WIKI` is the single operational knowledge root for Owen Graphite.

## Canonical Folders

| Path | Role |
| --- | --- |
| `dev/WIKI/MAP/` | Generated maps, owner registry, risk contracts, provenance artifacts. |
| `dev/WIKI/DOCS/` | Documentation corpus routing and absorbed v3 docs/research fixtures. |
| `dev/WIKI/SRC/` | Curated source-family routing notes. |
| `dev/WIKI/WORKFLOWS/` | Task-specific edit and validation workflows. |
| `dev/WIKI/effective-baseline/` | Effective baseline snapshots and Style Settings matrices. |
| `dev/WIKI/runtime-debug-snippets/` | Runtime evidence snippets used before CSS fixes. |

## Removed Legacy Roots

These paths must not be recreated:

- `dev/LLM-WIKI/`
- `dev/MAP/`
- `dev/effective-baseline/`
- `dev/WIKI/DEV/`
- `docs/v3/`

Use `dev/scripts/audit_core_principles.py` to enforce the structure.