# DEV: Sync Obsidian

Windows test vault path:

```powershell
.\.venv\Scripts\python.exe dev\scripts\sync_obsidian_theme.py --target "D:\Owen-WIKI\.obsidian\themes\Owen Graphite" --skip-bundle
```

After sync, compare repo `theme.css` with vault `theme.css` when debugging cache or path issues.
