# Risk Contract: Reading Content

Applies to `reading-typography` and `reading-callouts-lists` owner surfaces.

## Owners

- Typography, headings, paragraphs, links, and list rhythm: `src/base/12-reading-content.css`.
- Callouts, callout internals, blockquotes, and rendered task/list surfaces: `src/surfaces/21-reading-callouts-lists.css`.
- `src/surfaces/23-liquid-glass-core.css` may support validated glass closure, but it is not the owner for new reading behavior.

## Boundaries

- Do not route Reading View fixes through late visual modules when the selector belongs to the reading owner.
- Do not mix rendered reading tables with Live Preview markdown table widget geometry.
- Do not change list or callout spacing without checking nested callouts, task lists, and blockquotes.

## Evidence

- Use a natural document fixture for long paragraphs, nested lists, callouts, embeds, and code/table neighbors.
- For hover, focus, selected, collapsed, or plugin-injected states, capture runtime evidence before editing.

## Checks

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_core_principles.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```