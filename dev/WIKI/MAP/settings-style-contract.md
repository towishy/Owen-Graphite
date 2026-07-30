# Risk Contract: Settings And Style Settings

Applies to Obsidian settings controls and Style Settings metadata.

## Owners

- Obsidian settings panes, setting rows, toggles, sliders, dropdowns, and settings search presentation: `src/chrome/33-settings-controls.css`.
- Style Settings metadata, ids, defaults, options, and user-facing compatibility: `src/features/40-style-settings.css` and `dev/WIKI/DOCS/v3/style-settings-contract.json`.
- Owen Graphite row localization when Style Settings cannot resolve the Obsidian locale, plus transient desktop title/metadata tooltip structure: `compat/owen-graphite-style-settings-l10n`.

## Boundaries

- Do not put setting control presentation in overlay or workspace chrome owners unless the selector belongs to those surfaces.
- A setting option is not complete until CSS metadata, the contract JSON, and docs agree.
- `ogd-style-settings-language` must preserve `ogd-language-auto`, `ogd-language-ko`, and `ogd-language-en`; automatic mode follows the Obsidian runtime locale.
- The companion may translate only Owen Graphite rows and Style Settings chrome. It may structure transient desktop `.tooltip` text only when Obsidian provides a title/metadata blank-line separator; it must preserve the text and ignore one-line tooltips. It must not modify Style Settings `data.json`, setting ids, defaults, generated body classes, or machine option values.
- Use tokens for repeated setting UI colors, spacing, and focus states instead of local literals.
- Scope Obsidian core settings cards through the active native `data-setting-id` and direct `.vertical-tab-content > .setting-group` boundary. Do not target translated section-title text.
- Core groups without a native heading receive card geometry only. Do not synthesize locale-dependent labels or icon headers from CSS.
- Section-specific core icons may use group position only inside a named core tab because Obsidian does not expose semantic group ids. Re-capture all core tabs after an Obsidian update changes group count or order.

## Evidence

- For settings UI changes, capture the setting pane state and any focused/hovered control involved.
- For core card changes, record group/card counts, heading icon geometry, horizontal overflow, and row overlap for `about`, `editor`, `file`, `appearance`, `hotkeys`, `keychain`, `plugins`, and `community-plugins`.
- For Style Settings changes, record the setting id, default, option values, and generated body class.
- 2026-07-25 CDP evidence on Obsidian 1.12.7: `navigator.language` and `moment.locale()` were `ko`, while `localStorage.language` was `null`; Style Settings 1.0.9 therefore rendered English despite valid `title.ko` metadata.

## Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_style_settings_contract.py
.\.venv\Scripts\python.exe compat\owen-graphite-style-settings-l10n\test.py
.\.venv\Scripts\python.exe dev\scripts\audit_core_principles.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```
