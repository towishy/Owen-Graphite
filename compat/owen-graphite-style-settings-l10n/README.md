# Owen Graphite Companion

Runtime companion for Owen Graphite and Style Settings 1.0.9.

Obsidian 1.12 can render its interface in Korean while leaving the legacy
`localStorage.language` key empty. Style Settings 1.0.9 reads that key once and
falls back to English, so native `title.ko` and `description.ko` metadata are not
selected. This companion localizes only Owen Graphite rows using the restored
Automatic/Korean/English setting and Obsidian's runtime locale.

Owen Graphite and native preferences dropdowns use an accessible custom list while retaining their
native select values and input/change events. The list supports pointer and
keyboard selection, typeahead, disabled options, and light-dismiss.

Native settings groups without headings receive the existing localized page
label and navigation icon. Native rows, descriptions, links, values, and event
handlers are retained. Owen plugins keep ownership of their own headings and
dropdowns. The observer follows the native modal's owner document because
Obsidian 1.14 settings popouts do not emit workspace `window-open` events.
Menus, event listeners, generated headings, and owned ARIA attributes are
removed or restored on unload; closed documents are released.

On desktop, the companion also structures Obsidian's plain-text
`title + blank line + metadata` tooltips. This lets the theme keep wrapped
titles bold and position metadata from the real title height.

The companion does not modify, migrate, or delete Style Settings `data.json`.

```powershell
python build.py
python test.py
python install.py --obsidian-config C:\path\to\vault\.obsidian
```

Localization remains limited to Owen Graphite Style Settings. The shared
preferences enhancements do not translate third-party settings or alter their
stored values. Tooltip structure remains limited to the title/metadata
blank-line separator.

For optional real-runtime regression checks, use a disposable vault containing
the Owen plugins, Style Settings, and this companion. The runner installs its
legacy settings fixture only after verifying the explicitly selected vault:

```powershell
node ..\..\dev\scripts\test_settings_runtime.cjs C:\path\to\playwright-core http://127.0.0.1:9222 C:\test-vault C:\test-evidence
```
