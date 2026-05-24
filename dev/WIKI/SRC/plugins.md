# SRC: Plugins

- `src/plugins/60-canvas-graph-link-panes.css`: Canvas, graph, links, panes.
- `src/plugins/61-live-preview-mobile-plugin.css`: Live Preview/mobile/plugin compatibility and Mermaid support.

Plugin CSS should not become the owner for core document geometry.

Minimum checks: `SRC/validation-matrix.md`, `release_check.py --skip-bundle`, plus real plugin DOM or fixture evidence for runtime plugin selectors.
