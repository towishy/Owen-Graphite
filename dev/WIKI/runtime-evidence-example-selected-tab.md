# Runtime Evidence Example: Selected Tab

Use this as a completed example for chrome selected, active, hovered, or focused state bugs. Values are illustrative; capture fresh values for real fixes.

## Capture Header

| Field | Value |
| --- | --- |
| Issue | Active tab rim looks detached from adjacent tab background |
| Surface | Chrome |
| Runtime state | selected |
| Obsidian version | 1.12.x |
| OS | Windows |
| Theme version | current working tree |
| Vault/theme path | `C:\OWEN\Drive\Obsidian\.obsidian\themes\Owen Graphite` |
| Repro note | Open two markdown tabs, select the second tab, inspect `.workspace-tab-header.is-active`. |

## Required Evidence

1. DOM chain: `.workspace-tabs > .workspace-tab-header-container > .workspace-tab-header.is-active > .workspace-tab-header-inner`.
2. Bounding rect chain: active header and inner rect keep the same height before and after selection.
3. Computed geometry: `display`, `position`, `height`, `padding`, `line-height`, `overflow`, and `transform` show no layout shift.
4. Matched rules: selected tab rim/background comes from `src/chrome/37-tabs-file-explorer-search.css`; top chrome icon/ribbon rules do not own this state.
5. Inline style check: no inline height, transform, or box-shadow controls the selected state.
6. Owner mapping: tabs/file explorer owner, plus `dev/WIKI/MAP/top-chrome-icon-background-contract.md` when icon background is involved.
7. Screenshot/state note: selected tab is visibly active and adjacent inactive tab remains same height.

## Decision

| Question | Answer |
| --- | --- |
| Is a theme rule responsible? | Yes, selected tab visual rules. |
| If yes, which source owner? | `src/chrome/37-tabs-file-explorer-search.css`. |
| Is an inline/core rule responsible? | No inline geometry owner observed. |
| Is CSS allowed by a risk contract? | Yes, chrome owner plus top chrome contract if icon background changes. |
| Which workflow applies? | `WORKFLOWS/chrome-ui.md`. |
| Which audit proves the change? | `audit_core_principles.py`, `release_check.py --skip-bundle`, plus runtime recheck. |