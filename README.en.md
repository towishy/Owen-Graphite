# Owen Graphite

Owen Graphite is an Obsidian theme for long-form technical writing, Korean and English knowledge bases, and PDF/report workflows. The v3 codebase is rebuilt as modular CSS under `src/`, with release audits for bundle freshness, Style Settings compatibility, docs/assets links, CSS budget, Live Preview editability, and PDF header/footer behavior.

## What It Is Good At

| Workflow | What Owen Graphite improves |
| --- | --- |
| Long Korean and English notes | Balanced CJK/Latin typography, calmer spacing, stable long tables and code blocks |
| Technical documentation | Clear callouts, embeds, tables, code blocks, and document-style reading surfaces |
| PDF reports | Automatic heading numbering, first-page header labels, final-page footer labels, and reduced page-break issues |
| Daily Obsidian workspaces | Polished tabs, file explorer, search panes, settings controls, popovers, and type badges |

## Install

1. Open Obsidian.
2. Go to `Settings` -> `Appearance` -> `Themes`.
3. Search for `Owen Graphite` and enable it.
4. Optional: install the Style Settings plugin to adjust PDF labels, typography, glass intensity, motion, and accessibility options.

Manual ZIP installs should use the release asset named `Owen-Graphite-3.1.66.zip`, not GitHub's auto-generated source archive.

## Documentation

| Topic | Link |
| --- | --- |
| Main README | [README.md](README.md) |
| Style Settings presets | [dev/WIKI/DOCS/v3/style-settings-presets.md](dev/WIKI/DOCS/v3/style-settings-presets.md) |
| Plugin compatibility | [dev/WIKI/DOCS/v3/plugin-compatibility.md](dev/WIKI/DOCS/v3/plugin-compatibility.md) |
| Release and validation plan | [dev/WIKI/DOCS/v3/release-plan.md](dev/WIKI/DOCS/v3/release-plan.md) |
| Visual comparison guide | [dev/WIKI/DOCS/v3/visual-comparison-guide.md](dev/WIKI/DOCS/v3/visual-comparison-guide.md) |

## Development

The source of truth is `src/`. Do not hand-edit `theme.css`; build it from the v3 source tree.

```powershell
python dev/scripts/bundle_v3.py
Copy-Item dist\theme-v3.css theme.css -Force
python dev/scripts/release_check.py
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full workflow.
