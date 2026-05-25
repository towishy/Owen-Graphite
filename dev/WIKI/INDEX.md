# WIKI Index

## Core

- `CORE-PRINCIPLES.md`: non-negotiable rules.
- `STRUCTURE.md`: canonical WIKI folders and removed legacy roots.
- `QUICK-ROUTING.md`: where to start by work area.
- `OWNER-DECISION-TREE.md`: fallback routing when ownership is ambiguous.
- `SELECTOR-OWNER-CHEATSHEET.md`: selector-to-owner quick map.
- `VISUAL-QA.md`: visual acceptance checklist.
- `runtime-evidence-template.md`: required runtime evidence shape.
- `runtime-evidence-schema.json`: required JSON fields for temporary runtime captures.
- `runtime-evidence-storage.md`: where runtime captures are kept.
- `runtime-evidence-example-selected-tab.md`: completed chrome selected-state example.
- `runtime-evidence-example-plugin-dom.md`: completed plugin DOM example.

## Workflows

- `WORKFLOWS/table.md`
- `WORKFLOWS/live-preview-cm6.md`
- `WORKFLOWS/pdf.md`
- `WORKFLOWS/chrome-ui.md`
- `WORKFLOWS/docs-assets.md`
- `WORKFLOWS/release.md`
- `WORKFLOWS/validation-matrix.md`
- `WORKFLOWS/wiki-maintenance.md`

## Generated MAP Bridge

- `MAP/source-usage-map.md`
- `MAP/coverage-priority-plan.md`
- `MAP/owner-registry.md`
- `MAP/route-registry.json`
- `MAP/route-registry.md`
- `MAP/risk-contracts.md`
- `MAP/selector-provenance.md`
- `MAP/reading-content-contract.md`
- `MAP/overlay-menu-search-contract.md`
- `MAP/mobile-narrow-layout-contract.md`
- `MAP/settings-style-contract.md`
- `MAP/shared-tokens-contract.md`

## Source Families

- `SRC/base.md`
- `SRC/surfaces.md`
- `SRC/features.md`
- `SRC/chrome.md`
- `SRC/plugins.md`
- `SRC/themes.md`
- `SRC/tokens.md`
- `SRC/validation-matrix.md`

## Tokens And Plugins

- `TOKENS/usage-guide.md`
- `TOKENS/state-token-map.md`
- `PLUGINS/compatibility-matrix.md`
- `PLUGINS/coverage-matrix.md`
- `PLUGINS/runtime-dom-notes.md`

## Runtime And Recipes

- `RUNTIME/README.md`
- `RUNTIME/table.md`
- `RUNTIME/chrome.md`
- `RUNTIME/pdf.md`
- `RUNTIME/plugins.md`
- `RECIPES/README.md`
- `RECIPES/reading-heading-spacing.md`
- `RECIPES/live-preview-spacing.md`
- `RECIPES/rendered-table-polish.md`
- `RECIPES/pdf-label-preset.md`
- `RECIPES/top-chrome-state.md`
- `RECIPES/style-settings-option.md`

## Operations

- `audits.md`
- `dev/scripts/wiki_route.py`: prints WIKI owner/workflow/check routing by surface.
- `dev/scripts/wiki_route.py settings`: routes settings UI and Style Settings work.
- `dev/scripts/wiki_route.py <surface> --commands`: prints copyable surface check commands.
- `dev/scripts/audit_route_registry.py`: validates route registry schema, links, and command references.
- `dev/scripts/build_route_registry_doc.py --check`: verifies generated route registry docs are fresh.
- `dev/scripts/validation_plan.py --surface <surface>`: plans route-aware checks before a diff exists.
- `dev/scripts/validation_plan.py --surface chrome --surface settings`: plans multi-surface checks with de-duplicated commands.
- `dev/scripts/finish_work.py --full-check`: runs release-confidence handoff validation.
- `runtime-debug.md`
- `build-release.md`
- `sync-obsidian.md`

## Docs Corpus

- `DOCS/README.md`
- `DOCS/docs-map.md`
- `DOCS/v3/`

## Incidents And Prompts

- `INCIDENTS/table-row-inflation.md`
- `INCIDENTS/direct-owner-violation.md`
- `INCIDENTS/README.md`
- `INCIDENTS/incident-template.md`
- `INCIDENTS/taxonomy.md`
- `PROMPTS/before-edit.md`
- `PROMPTS/review-core-principles.md`
- `PROMPTS/work-summary.md`

## Helper Scripts

- `dev/scripts/wiki_route.py`
- `dev/scripts/route_registry.py`
- `dev/scripts/audit_route_registry.py`
- `dev/scripts/build_route_registry_doc.py`
- `dev/scripts/start_work.py`
- `dev/scripts/finish_work.py`
- `dev/scripts/validation_plan.py`
- `dev/scripts/new_runtime_evidence.py`
- `dev/scripts/new_incident.py`
- `dev/scripts/promote_evidence.py`
- `dev/scripts/work_summary.py`
- `dev/scripts/build_coverage_priority_plan.py`
- `dev/scripts/audit_mobile_owner.py`
- `dev/scripts/audit_owner_risk_contracts.py`
- `dev/scripts/audit_wiki_route_coverage.py`
- `dev/scripts/audit_selector_owner_cheatsheet.py`
- `dev/scripts/audit_runtime_evidence_requirements.py`
