# Owen Graphite WIKI

This wiki is the operational entry point for AI-assisted work on Owen Graphite.

`dev/WIKI/MAP` is the generated/provenance layer inside the wiki. The root wiki files are the curated workflow layer that tells an agent what to read, where to edit, what not to touch, and which gates must pass.

## Start Here

### By Task

| Task | First Route | Read Next |
| --- | --- | --- |
| Bug fix or visual change | `dev/scripts/wiki_route.py <surface>` | Relevant `WORKFLOWS/` page and `MAP/*-contract.md` |
| Runtime hover/focus/active issue | `runtime-evidence-template.md` | `runtime-evidence-schema.json`, `RUNTIME/` surface guide before editing CSS |
| New Style Settings option | `dev/scripts/wiki_route.py settings` | `MAP/settings-style-contract.md`, `RECIPES/style-settings-option.md` |
| Token or palette change | `dev/scripts/wiki_route.py tokens` | `MAP/shared-tokens-contract.md`, `TOKENS/usage-guide.md` |
| WIKI or process change | `WORKFLOWS/wiki-maintenance.md` | `audit_wiki_consistency.py`, `audit_owner_risk_contracts.py` |
| Release or Obsidian sync | `dev/scripts/wiki_route.py release` | `WORKFLOWS/release.md`, `sync-obsidian.md` |

### Standard Flow

1. Read `CORE-PRINCIPLES.md`.
2. Read `STRUCTURE.md` when changing paths, generated artifacts, or docs layout.
3. Use `QUICK-ROUTING.md` to find the owner module.
4. Use `OWNER-DECISION-TREE.md` when ownership is ambiguous.
5. Use `SELECTOR-OWNER-CHEATSHEET.md` when starting from matched selectors.
6. Open the relevant workflow under `WORKFLOWS/` or recipe under `RECIPES/`.
7. Use `MAP/source-usage-map.md` to jump into generated source maps.
8. Use `DOCS/docs-map.md` when a task touches docs, samples, settings, visual baselines, or release process.
9. Use `VISUAL-QA.md` for visual changes and `runtime-evidence-template.md` plus `runtime-evidence-storage.md` before editing runtime state bugs.
10. Use `TOKENS/`, `PLUGINS/`, and `MAP/settings-style-contract.md` when touching token, plugin, settings, or Style Settings behavior.
11. Run the audits listed in the workflow before committing.

## Non-Negotiable

- Owen can explicitly accept repository-specific visual/runtime risk. When that happens, record the risk in WIKI/evidence and update the relevant guard instead of silently bypassing it.
- Do not add late fixes because the owner is hard to find.
- Do not style Obsidian-owned markdown table widget geometry unless Owen explicitly accepts the risk and the WIKI/guard/evidence path is updated.
- Do not reintroduce `src/polish` or `!important`.
- Do not claim a runtime issue is fixed without runtime evidence.
- Do not release with a `v`-prefixed tag; Owen Graphite uses numeric semver tags only.
