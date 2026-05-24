# SRC Validation Matrix

Use this after choosing an owner with `QUICK-ROUTING.md` or `OWNER-DECISION-TREE.md`.

| Source Family | Typical Owners | Minimum Checks | Extra Evidence |
| --- | --- | --- | --- |
| `src/tokens/` | `00-light-tokens.css`, `01-dark-tokens.css` | `release_check.py --skip-bundle`, Style Settings contract when setting-facing | Light/Dark visual comparison for broad token changes |
| `src/themes/` | dark and accessibility theme modules | `release_check.py --skip-bundle`, CSS budget | Light/Dark screenshot or computed fingerprint for visible changes |
| `src/base/` | workspace base, reading typography, Live Preview geometry | source usage map, core principles gate, hit-routing audit | Runtime evidence for CM6, selected/focused/active states |
| `src/surfaces/` | rendered tables/code/callouts/embeds/canvas/graph | direct owner guard, LP/PDF selector ownership, release check | Visual fixture for table/code/callout changes |
| `src/chrome/` | tabs, ribbon, explorer, search, overlays, settings | release check, core gate, docs/assets when screenshots change | Screenshot/runtime evidence for hover/focus/active states |
| `src/features/40-style-settings.css` | Style Settings metadata | Style Settings contract, docs/assets | Update `DOCS/v3/style-settings-contract.*` together |
| `src/features/41-feature-presets.css` | presets and PDF marginalia | PDF header/footer contract, release check | PDF/export check for label layout |
| `src/features/42-report-print-polish.css` | report/PDF table/code/callout closure | PDF header/footer contract, LP/PDF selector ownership | Print fixture or visual quality fixture |
| `src/features/43-print-base.css` | base print page behavior | release check, PDF header/footer contract | PDF page-break/header/footer smoke check |
| `src/plugins/` | plugin-specific compatibility | release check, docs/assets when support docs change | Real plugin DOM or fixture evidence |

## Universal Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\build_source_usage_map.py --check
.\.venv\Scripts\python.exe dev\scripts\audit_core_principles.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```

## Runtime Rule

If the change depends on selected, hovered, focused, active, plugin-generated, or inline styles, fill `runtime-evidence-template.md` before editing source.
