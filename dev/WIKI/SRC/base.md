# SRC: Base

- `src/base/10-base-workspace.css`: base workspace and app-wide reading/source primitives.
- `src/base/12-reading-content.css`: Reading View typography, headings, paragraphs, links.
- `src/base/13-live-preview.css`: CM6 geometry, Live Preview source lines, hit routing, HTML table embed primitives.

Risk: broad `.cm-content`, `.cm-line`, or `.HyperMD-*` selectors can affect nested runtime editors.
