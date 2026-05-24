# DEV: Sync Obsidian

Windows test vault path:

```powershell
.\.venv\Scripts\python.exe dev\scripts\sync_obsidian_theme.py --target "D:\Owen-WIKI\.obsidian\themes\Owen Graphite" --skip-bundle
```

After sync, compare repo `theme.css` with vault `theme.css` when debugging cache or path issues.

`sync_obsidian_theme.py` uses `copy2` first and falls back to chunk-copy with SHA-256 verification when Windows reports large-file `WinError 483` device hardware failures.

Successful sync writes `dev/TEMP/last-sync.json` with target, timestamp, asset hashes, and byte counts.
