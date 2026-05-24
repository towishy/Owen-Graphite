# SRC: Features

- `src/features/40-style-settings.css`: Style Settings metadata.
- `src/features/41-feature-presets.css`: presets and PDF marginalia owner.
- `src/features/42-report-print-polish.css`: report/PDF output and allowed table/code/callout print closures.
- `src/features/43-print-base.css`: base print page and generic PDF rules.

PDF header/footer ownership belongs to `41-feature-presets.css`.

Minimum checks: `SRC/validation-matrix.md`, `audit_style_settings_contract.py` for settings, `audit_pdf_header_footer.py` for PDF, `release_check.py --skip-bundle`.
