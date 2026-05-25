# PDF Font Size Matrix

Use this when changing `ogd-pdf-font-size`, PDF visibility presets, or customer-delivery PDF readability.

CSS print sizing uses `pt`, while Live Preview uses `px`. For Owen Graphite planning, use:

```text
1pt = 1.333px
12pt = 16px
12.4pt = 16.5px
```

## Policy

- Live Preview body size is the readability reference.
- PDF body text may add up to about `+1px` visual compensation because exported PDFs often read smaller in viewers and browser previews.
- Table, callout, and code sizes should track `--ogd-pdf-surface-text-font-size` unless a print-specific contract says otherwise.
- Heading hierarchy should not be scaled by PDF body presets unless explicitly requested.

## Current Presets

| Preset / Context | CSS token | Size | Approx px | Line height | Notes |
| --- | --- | ---: | ---: | ---: | --- |
| PDF visibility | `--ogd-pdf-surface-text-font-size` | `12pt` | `16px` | `1.45` | Default readable PDF surface size. |
| PDF customer delivery | `--ogd-pdf-surface-text-font-size` | `12.4pt` | `16.5px` | `1.48` | Screen-share/customer review preset. |
| Header label default | `--ogd-pdf-header-font-size` | `7.4pt` | `9.9px` | inherited | Compact marginalia label. |
| Footer label default | `--ogd-pdf-footer-font-size` | `7.6pt` | `10.1px` | inherited | Compact marginalia label. |
| Customer header label | `--ogd-pdf-header-font-size` | `8.8pt` | `11.7px` | inherited | Used by customer-delivery preset. |
| Customer footer label | `--ogd-pdf-footer-font-size` | `9pt` | `12px` | inherited | Used by customer-delivery preset. |

## Validation

Run:

```powershell
.\.venv\Scripts\python.exe dev\scripts\audit_pdf_header_footer.py
.\.venv\Scripts\python.exe dev\scripts\release_check.py --skip-bundle
```
