# Owen Graphite Companion

Localization bridge for Owen Graphite and Style Settings 1.0.9.

Obsidian 1.12 can render its interface in Korean while leaving the legacy
`localStorage.language` key empty. Style Settings 1.0.9 reads that key once and
falls back to English, so native `title.ko` and `description.ko` metadata are not
selected. This companion localizes only Owen Graphite rows using the restored
Automatic/Korean/English setting and Obsidian's runtime locale.

The companion does not modify, migrate, or delete Style Settings `data.json`.

```powershell
python build.py
python test.py
python install.py --obsidian-config C:\path\to\vault\.obsidian
```

The runtime observer is limited to Owen Graphite setting rows and does not add
unrelated editor or theme behavior.
