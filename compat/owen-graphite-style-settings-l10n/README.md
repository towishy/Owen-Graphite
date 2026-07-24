# Owen Graphite Style Settings Language

Locale compatibility companion for Owen Graphite and Style Settings 1.0.9.

## Why a companion

Style Settings 1.0.9 resolves `title.<Obsidian locale>` only from Obsidian's
application locale. It cannot use a locale stored by an individual CSS schema.
This companion observes the stable `ogd-language-auto` / `ogd-language-ko` /
`ogd-language-en` body class applied by Style Settings and translates only rendered Owen Graphite rows
identified by their existing `data-id`. It does not read, rewrite, migrate, or
delete `obsidian-style-settings/data.json`.

Automatic is the default: Korean Obsidian locales use Korean, while every other
locale uses English. Users can explicitly override the result from the Language
control under the Interface section.

## Provenance and license

- Compatibility target: `mgmeyers/obsidian-style-settings` 1.0.9
- Upstream source: https://github.com/mgmeyers/obsidian-style-settings/tree/1.0.9
- Upstream manifest: https://raw.githubusercontent.com/mgmeyers/obsidian-style-settings/1.0.9/manifest.json
- Upstream package metadata declares MIT. This independently written companion
  is also MIT-licensed, does not include the upstream bundle, and does not
  modify the installed upstream plugin. No GPL-covered source is incorporated;
  source, build, tests, and install logic are all included here for auditability.

The plugin is built from the checked-in CSS schema and `src/en.json`:

```powershell
python build.py
python test.py
python install.py --obsidian-config C:\path\to\vault\.obsidian
```

The build emits deterministic `main.js`, `core.js`, and
`catalog.generated.json` artifacts. Installation preserves the upstream Style
Settings settings file byte-for-byte and adds this plugin ID to
`community-plugins.json` only when absent. If the installed Owen Graphite theme
is newer than the repository manifest, the installer preserves that manifest
and CSS, creates a hash-named backup, and injects only the locale selector schema
entry. Re-running the installer does not duplicate the entry.