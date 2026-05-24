# Runtime Evidence Storage

Use this when runtime evidence is needed but should not become a permanent incident yet.

## Temporary Evidence

Store temporary captures under:

```text
dev/TEMP/runtime-evidence/<yyyy-mm-dd>-<surface>-<short-name>.json
```

Use this for exploratory DOM chains, computed styles, matched rules, screenshots notes, and plugin DOM probes.

## Permanent Evidence

Promote evidence into `dev/WIKI/INCIDENTS/` only when one of these is true:

- the same mistake could recur;
- a runtime state changes owner or contract guidance;
- a workaround or forbidden approach must be remembered;
- the issue affects release, PDF, Live Preview hit routing, or plugin compatibility.

## Minimum Metadata

Each evidence note should include:

- surface and owner candidate;
- Obsidian version and OS when known;
- runtime state;
- DOM chain or selector root;
- matched theme rule and source module;
- decision: owner edit, no CSS fix, or WIKI/MAP update.

Temporary files in `dev/TEMP/runtime-evidence/` are local working artifacts and should not be required for release packaging.
