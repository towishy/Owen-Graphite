# MAP Diff Stability

Generated MAP artifacts are useful only when their diffs are reviewable. Keep generator output deterministic.

## Current Rules

- JSON output uses sorted keys.
- `theme-css-risk-summary.json` is the stable review surface for ordinary changes.
- Selector provenance entries are written in sorted selector-key order.
- Cross-file selector line references are sorted by module and line.
- Markdown/HTML reports remain generated from the same payload and should not be hand-edited.

## When Diffs Are Large

1. Confirm the source CSS change really changed selector counts or labels.
2. Re-run `dev/scripts/build_src_map.py` and `dev/scripts/build_source_usage_map.py` once.
3. Do not manually edit generated MAP files to quiet the diff.
4. If a small source change causes unstable ordering, fix the generator ordering rather than the generated artifact.

## Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\build_src_map.py
.\.venv\Scripts\python.exe dev\scripts\build_source_usage_map.py --check
.\.venv\Scripts\python.exe dev\scripts\audit_wiki_consistency.py
```