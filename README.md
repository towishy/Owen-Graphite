<!-- markdownlint-disable MD022 MD032 MD033 MD040 MD041 -->

![Owen Kit](screenshots/readme/owen-kit.png)

[![GitHub release](https://img.shields.io/github/v/release/towishy/Owen-Graphite?style=flat-square)](https://github.com/towishy/Owen-Graphite/releases/latest)
[![License](https://img.shields.io/github/license/towishy/Owen-Graphite?style=flat-square)](LICENSE)
[![Obsidian](https://img.shields.io/badge/Obsidian-Compatible-7c3aed?style=flat-square&logo=obsidian)](https://obsidian.md)
[![!important](https://img.shields.io/badge/!important-0-0d9488?style=flat-square)](dev/WIKI/DOCS/v3/cascade-research.md)

[Style Settings presets](dev/WIKI/DOCS/v3/style-settings-presets.md) · [Compatibility matrix](dev/WIKI/DOCS/v3/plugin-compatibility.md) · [Changelog](CHANGELOG.md)

# Owen Graphite — Obsidian Theme

**Owen Graphite v3.1.88** is a liquid-glass Obsidian theme for technical documentation, knowledge bases, and report-ready notes, giving Korean/English typography, long tables, code blocks, workspace chrome, Style Settings controls, and PDF export layouts one calm graphite surface across Live Preview, Reading View, and print.

## Why Owen Graphite?

| Workflow | What you feel immediately |
| --- | --- |
| Long technical notes | CJK/Latin paragraphs, headings, code, and dense tables keep a stable rhythm without feeling cramped. |
| Live Preview writing | Editing, Reading View, and rendered widgets share the same quiet surfaces for tables, code blocks, callouts, and embeds. |
| Report and PDF handoff | Header/footer labels, page numbering, screen-first PDF readability, and page-break guards support recurring report delivery. |
| Daily workspace navigation | Tabs, file explorer hierarchy, search, settings, popovers, and type badges use a restrained graphite liquid-glass language. |

## Design And Function Snapshot

| Surface | Design signal | Function signal |
| --- | --- | --- |
| Workspace chrome | Frosted white/graphite panels, shallow rims, and soft lift states | Active files, parent folders, tabs, and vault controls stay scannable in large vaults. |
| Writing surface | Calm document panes with balanced body, code, table, and callout density | Long Korean/English technical pages remain readable through editing and review. |
| Settings and presets | Compact glass controls instead of loud colored panels | Style Settings exposes PDF, typography, spacing, chrome, and accessibility options without visual clutter. |
| PDF export | Report labels, customer-delivery presets, and print-safe spacing | Notes can become screen-shared PDFs or formal report output with less manual cleanup. |

## Release Confidence

| Guard | Current status | Evidence |
| --- | --- | --- |
| Bundle freshness | `theme.css` must match `dist/theme-v3.css` | [release plan](dev/WIKI/DOCS/v3/release-plan.md) |
| Zero-important cascade | declaration-level `!important` policy is enforced | [cascade research](dev/WIKI/DOCS/v3/cascade-research.md) |
| Style Settings contract | option ids/defaults are audited against the contract | [contract](dev/WIKI/DOCS/v3/style-settings-contract.md) |
| Docs/assets links | local Markdown links and README images are audited | [contributing](CONTRIBUTING.md) |
| Live Preview/PDF parity | LP hit-routing, PDF header/footer, and visual fixture checks are scripted | [release plan](dev/WIKI/DOCS/v3/release-plan.md) |

## Visual Tour

| Surface | Preview |
| --- | --- |
| Light mode | ![Light Mode](screenshots/light.png) |
| Dark mode | ![Dark Mode](screenshots/dark.png) |
| Top tabs and floating toolbar | ![Top tabs and floating toolbar](screenshots/readme/top-tabs-liquid-glass.svg) |
| Writing surface and floating toolbar | ![Writing surface and floating toolbar](screenshots/readme/workspace-writing-surface.jpg) |
| Style Settings report controls | ![Style Settings report controls](screenshots/readme/style-settings-report-options.jpg) |
| PDF customer delivery visibility | ![PDF customer delivery visibility controls](screenshots/readme/pdf-customer-delivery-feature.png) |
| Owen Editor toolbar controls | ![Owen Editor toolbar controls](screenshots/readme/owen-editor-toolbar-settings.jpg) |
| File explorer type badges | ![File explorer type badges](screenshots/readme/file-explorer-type-badges.svg) |

New comparison screenshots should follow the [visual comparison guide](dev/WIKI/DOCS/v3/visual-comparison-guide.md) so default Obsidian and Owen Graphite are captured with the same note, viewport, and state.

---

## 1. Theme Profile

| Item | Value |
| --- | --- |
| **Version** | `3.1.88` |
| **Baseline / rollback target** | `v3.1.88` |
| **Mode support** | Light / Dark |
| **Platform** | Desktop & Mobile |
| **Design policy** | Liquid Glass core · token-first surfaces · zero-important cascade |

<details>
<summary>Light / Dark mode screenshots</summary>

![Light Mode](screenshots/light.png)
![Dark Mode](screenshots/dark.png)

</details>

---

## 2. Latest Highlights

Install the [Style Settings plugin](https://community.obsidian.md/plugins/obsidian-style-settings) to unlock the report, typography, spacing, PDF, and workspace polish controls referenced below.

### v3.1.88 — Active Tab Bridge Hotfix

This release restores the missing connection between the active tab and document surface by overriding the Obsidian core clipping and hidden pseudo-element state with a measured 5px bridge.

| Area | What changed |
| --- | --- |
| Active tab | The tab surface now continues through the 3.5px header boundary gap instead of stopping above it. |
| Cascade repair | The active tab owner explicitly restores visible overflow, full pseudo width, and opacity. |
| Visual restraint | The failed 19px decorative cap and shadow are replaced by a flat 5px continuation. |
| Runtime evidence | Obsidian 1.12.7 CDP confirmed a source-only `252px × 5px` bridge with `opacity: 1`. |

### v3.1.87 — Connected Workspace And Neutral Focus

This release connects the active tab to the document surface, frames the current file's parent folder, removes cyan focus halos from daily controls, and wires the existing A4/A3 paper choices to print geometry.

| Area | What changed |
| --- | --- |
| Workspace continuity | The active tab uses a 19px glass continuation so the tab and document read as one surface. |
| File explorer | The current document's direct parent folder gains a compact heading band and neutral glass frame. |
| Focus and controls | Settings, search, navigation, editing tools, and document chrome use quiet slate focus and hover states. |
| PDF paper size | A4/A3 portrait and landscape choices now select named Chromium print pages. |

### v3.1.86 — UI Foundation Workbench Alignment

This release aligns Owen Graphite and Owen Editor around a quieter UI Foundation contract: 4px spacing, 44px targets, consistent motion, clear keyboard focus, opaque repeated work surfaces, and liquid glass at the outer boundary.

| Area | What changed |
| --- | --- |
| Owen Editor integration | Floating tools share the Graphite boundary surface while palette controls keep plugin-owned opaque workbench styling. |
| Accessibility | Focus rings, mobile targets, reduced-transparency surfaces, and narrow top-tab geometry use shared tokens. |
| Style Settings | Sections open with clearer defaults and the document-width selector uses task-oriented labels. |
| Release guard | Runtime light/dark/focus/narrow checks, owner contracts, source maps, and release audits were refreshed. |

Older feature notes are kept in [dev/WIKI/DOCS/v3/feature-history.md](dev/WIKI/DOCS/v3/feature-history.md).

---

## 3. Installation Details

### Option A — Obsidian Community Theme Browser

1. Open `Settings` → `Appearance` → `Manage` under Themes.
2. Search for `Owen Graphite`.
3. Install and enable the theme.

### Option B — Manual ZIP Install

Download **`Owen-Graphite-3.1.88.zip`** from the [latest release](https://github.com/towishy/Owen-Graphite/releases/latest), then extract it into your vault theme folder.

| Platform | Target path |
| --- | --- |
| Windows | `<YourVault>\.obsidian\themes\Owen Graphite\` |
| macOS / Linux | `<YourVault>/.obsidian/themes/Owen Graphite/` |

After extraction, open Obsidian and select `Owen Graphite` from `Settings` → `Appearance` → `Themes`.

> Release assets also include GitHub's generated `Source code (zip)`. Use `Owen-Graphite-3.1.88.zip` for the installable theme package.

### Option C — Git Install Or Update

Clone into `.obsidian/themes/Owen Graphite/`. Running the same command again updates the theme.

#### Windows (PowerShell)

```powershell
$ErrorActionPreference = "Stop"
$Vault = "D:\Path\To\YourVault"            # replace with your vault path
$Repo = "https://github.com/towishy/Owen-Graphite.git"
$ThemesDir = Join-Path $Vault ".obsidian\themes"
$ThemeDir = Join-Path $ThemesDir "Owen Graphite"

New-Item -ItemType Directory -Force -Path $ThemesDir | Out-Null

if (Test-Path -LiteralPath (Join-Path $ThemeDir ".git")) {
  git -C "$ThemeDir" fetch --quiet origin main
  git -C "$ThemeDir" reset --quiet --hard origin/main
  git -C "$ThemeDir" clean -qfd
  Write-Host "OK: Owen Graphite updated."
} elseif (Test-Path -LiteralPath $ThemeDir) {
  $Backup = "${ThemeDir}.backup-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
  Move-Item -LiteralPath $ThemeDir -Destination $Backup
  git clone --quiet $Repo "$ThemeDir"
  Write-Host "OK: Owen Graphite reinstalled. Backup: $Backup"
} else {
  git clone --quiet $Repo "$ThemeDir"
  Write-Host "OK: Owen Graphite installed."
}
```

#### macOS / Linux (bash)

```bash
set -e
VAULT="/path/to/YourVault"                  # replace with your vault path
REPO="https://github.com/towishy/Owen-Graphite.git"
THEME_DIR="$VAULT/.obsidian/themes/Owen Graphite"
mkdir -p "$VAULT/.obsidian/themes"

if [ -d "$THEME_DIR/.git" ]; then
  git -C "$THEME_DIR" fetch --quiet origin main
  git -C "$THEME_DIR" reset --quiet --hard origin/main
  git -C "$THEME_DIR" clean -qfd
  echo "OK: Owen Graphite updated."
elif [ -e "$THEME_DIR" ]; then
  BACKUP="$THEME_DIR.backup-$(date +%Y%m%d-%H%M%S)"
  mv "$THEME_DIR" "$BACKUP"
  git clone --quiet "$REPO" "$THEME_DIR"
  echo "OK: Owen Graphite reinstalled. Backup: $BACKUP"
else
  git clone --quiet "$REPO" "$THEME_DIR"
  echo "OK: Owen Graphite installed."
fi
```

---

## 4. Developer Workflow

The v3 source lives in `src/` and is split into tokens, base, surfaces, chrome, features, themes, and plugins. Build and audit work should use the v3 tools in `dev/scripts/`.

| Task | Command |
| --- | --- |
| Build bundle | `python dev/scripts/bundle_v3.py` → `dist/theme-v3.css` |
| Refresh `theme.css` | `Copy-Item dist/theme-v3.css theme.css -Force` on Windows, or the equivalent copy command on macOS/Linux |
| Live Preview hit-routing audit | `python dev/scripts/audit_v3_hit_routing.py` |
| Duplicate selector audit | `python dev/scripts/v3_audit_duplicate_selectors.py` |
| Unused CSS candidate report | `python dev/scripts/build_unused_css_report.py` |
| Computed-style fingerprint capture | `python dev/scripts/capture_computed_fingerprint.py --build v3 --theme {light,dark}` |
| fingerprint diff | `python dev/scripts/fp_diff_summary.py [--theme dark]` |
| Release ZIP | `python dev/scripts/build_release.py` |
| Obsidian vault sync | `python dev/scripts/sync_obsidian_theme.py` |

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution details, [CHANGELOG.md](CHANGELOG.md) for release history, and [dev/WIKI/DOCS/v3/design-spec.md](dev/WIKI/DOCS/v3/design-spec.md) for the design and validation contract.

---

## 5. Support

<p align="center">
  <a href="https://github.com/sponsors/towishy">
    <img src="screenshots/readme/sponsor-coffee.svg" alt="Support Owen Graphite with a coffee" width="560">
  </a>
</p>

Owen Graphite is free and open source. If it helps your report, wiki, or documentation workflow, you can support maintenance through [GitHub Sponsors](https://github.com/sponsors/towishy).

---

## 6. License

MIT — [LICENSE](LICENSE)
