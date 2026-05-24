# Owen Graphite WIKI

This wiki is the operational entry point for AI-assisted work on Owen Graphite.

`dev/WIKI/MAP` is the generated/provenance layer inside the wiki. The root wiki files are the curated workflow layer that tells an agent what to read, where to edit, what not to touch, and which gates must pass.

## Start Here

1. Read `CORE-PRINCIPLES.md`.
2. Read `STRUCTURE.md` when changing paths, generated artifacts, or docs layout.
3. Use `QUICK-ROUTING.md` to find the owner module.
4. Use `OWNER-DECISION-TREE.md` when ownership is ambiguous.
5. Open the relevant workflow under `WORKFLOWS/`.
6. Use `MAP/source-usage-map.md` to jump into generated source maps.
7. Use `DOCS/docs-map.md` when a task touches docs, samples, settings, visual baselines, or release process.
8. Use `runtime-evidence-template.md` before editing runtime state bugs.
9. Run the audits listed in the workflow before committing.

## Non-Negotiable

- Do not add late fixes because the owner is hard to find.
- Do not style Obsidian-owned markdown table widget geometry.
- Do not reintroduce `src/polish` or `!important`.
- Do not claim a runtime issue is fixed without runtime evidence.
- Do not release with a `v`-prefixed tag; Owen Graphite uses numeric semver tags only.
