# Owen Graphite — Future Feature Recommendations

This list collects previously advertised or previewed ideas that are not currently verified in DEV CSS, but still look compatible with Owen Graphite's liquid/glass direction and can likely be implemented with low theme risk.

## Recommended

### Status Bar Separator
- Source idea: v2.18 status bar separator.
- Why it fits: subtle chrome separation pairs well with the existing floating status bar glass.
- Risk: low if scoped to `.status-bar .status-bar-item + .status-bar-item::before` and kept decorative only.
- Suggested treatment: 1px vertical separator with low-opacity graphite/cyan tint, no layout shift, no left-rail metaphor.

### Modal Close Chrome
- Source idea: v2.18 modal close button polish.
- Why it fits: destructive/close affordance can use a quiet rose hover while preserving the current glass language.
- Risk: low if scoped to `.modal-close-button` and `:focus-visible` only.
- Suggested treatment: transparent base, rose-tinted hover, inset ring, accessible focus ring.

### Dataview Inline Field Chip
- Source idea: v2.16 Dataview inline field chip.
- Why it fits: key/value chip pairs can reuse tag pill and metadata pill styling.
- Risk: low to medium; depends on Dataview class stability.
- Suggested treatment: key as muted accent pill, value as mono glass pill, no heavy shadows inside text flow.

### Sync / Git Status Pill
- Source idea: v2.14 sync/git indicator polish.
- Why it fits: status indicators can reuse existing status bar segment glass and semantic colors.
- Risk: low to medium; plugin-specific selectors may vary.
- Suggested treatment: only style known status bar plugin items when class/aria labels are present; no broad status-bar overrides.

### Ribbon Active Pill
- Source idea: v2.15 ribbon active state.
- Why it fits: active ribbon icon can match the file explorer active surface without using a left rail.
- Risk: medium; ribbon active classes need to be verified in current Obsidian.
- Suggested treatment: full pill background, subtle inset ring, no transform by default.

## Defer Unless Needed

### Drag Preview Ghost
- Risk: medium to high because drag state can affect usability and hit testing.
- Revisit only with real Obsidian drag screenshots.

### Vault Switcher / Workspaces Modal Glass
- Risk: medium because modal classes may be version-specific.
- Revisit after confirming current Obsidian DOM selectors.

### Mobile Bottom Toolbar
- Risk: medium to high because mobile chrome and safe-area behavior are fragile.
- Revisit with mobile screenshots and touch target checks.

### CM6 Fold Gutter Polish
- Risk: medium because CM6 internals change and can affect editor usability.
- Revisit only with focused editor DOM tests.

### Reading Progress Bar
- Risk: medium because scroll-driven/progress UI can become noisy or unsupported across panes.
- Revisit if there is a clear user workflow for long reading sessions.

### Print TOC Utility
- Risk: low CSS-wise, but it is more of a document utility than liquid/glass chrome.
- Revisit in the report/PDF feature track rather than workspace chrome.
