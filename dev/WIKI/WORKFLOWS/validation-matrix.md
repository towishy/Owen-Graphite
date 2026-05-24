# Workflow: Validation Matrix

Use this to choose validation depth without guessing.

| Change Type | Always Run | Also Run When Relevant |
| --- | --- | --- |
| Any source CSS | `build_source_usage_map.py --check`, `audit_core_principles.py`, `release_check.py --skip-bundle` | owner-specific audits below |
| Live Preview / CM6 | universal checks | `audit_v3_hit_routing.py`, runtime evidence |
| Tables / code / callouts | universal checks | `audit_direct_owner_guard.py`, `audit_lp_pdf_selector_ownership.py`, visual fixture |
| Chrome hover/focus/active | universal checks | runtime evidence, screenshot review |
| Tokens / design language | universal checks | `audit_style_settings_contract.py` when setting-facing, Light/Dark review |
| PDF / print | universal checks | `audit_pdf_header_footer.py`, visual quality fixture |
| Plugin DOM | universal checks | real plugin DOM evidence or recorded fixture gap |
| Docs / screenshots | `audit_docs_assets.py`, `audit_readme_svg_layout.py` | release check when README/release assets change |
| Release | `release_check.py --tag <version>`, `build_release.py`, `audit_release_zip.py` | GitHub workflow and release view |

## Full Release-Confidence Set

```powershell
.\.venv\Scripts\python.exe dev\scripts\build_source_usage_map.py --check
.\.venv\Scripts\python.exe dev\scripts\audit_wiki_consistency.py
.\.venv\Scripts\python.exe dev\scripts\audit_core_principles.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```

Use `dev/scripts/wiki_route.py <surface>` before choosing owner-specific checks.

Use `dev/scripts/validation_plan.py` to recommend checks from the current git diff.

Use `dev/scripts/validation_plan.py --run-safe` to execute recommended checks that do not require placeholders.

`--run-safe` never builds release ZIPs, publishes, or syncs Obsidian; use explicit release/sync commands for those.

The pre-commit hook uses the same diff-aware validation path and then escalates to full release validation when source, release, screenshot, or generated MAP files are staged.
