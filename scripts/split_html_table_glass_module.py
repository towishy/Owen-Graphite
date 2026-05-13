"""Move the v2.30.9 HTML-table-in-Live-Preview liquid glass tokens out of
dev/10d-liquid-glass-core.css and into a dedicated module so 10d stays
under the 1500-line complexity budget enforced by scripts/validate_theme.py.

Cross-platform (mac + Windows) — pure Python, no shell heredocs.

Steps:
  1) Strip the previously appended v2.30.9 block from dev/10d-liquid-glass-core.css.
  2) Write the dedicated module dev/10e-html-table-live-preview-glass.css.
  3) Insert "10e-html-table-live-preview-glass.css" into dev/_order.txt
     immediately after "10d-liquid-glass-core.css".
  4) Add "dev/10e-html-table-live-preview-glass.css" to REQUIRED_FILES in
     scripts/validate_theme.py (idempotent).
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "dev" / "10d-liquid-glass-core.css"
NEW_MODULE = ROOT / "dev" / "10e-html-table-live-preview-glass.css"
ORDER = ROOT / "dev" / "_order.txt"
VALIDATOR = ROOT / "scripts" / "validate_theme.py"

V2309_HEADER = "v2.30.9 — HTML <table> in Live Preview liquid glass parity"
COMMENT_BLOCK_OPEN = "/* ====================================================================="
SHORT_V2309_COMMENT = "/* v2.30.9 — HTML <table> in Live Preview liquid glass parity"

ORDER_PREV = "10d-liquid-glass-core.css"
ORDER_NEW = "10e-html-table-live-preview-glass.css"

REQ_PREV = '    "dev/10d-liquid-glass-core.css",'
REQ_NEW = '    "dev/10e-html-table-live-preview-glass.css",'

NEW_MODULE_TEXT = """/* ============================================================
  v2.30.9 — HTML <table> in Live Preview liquid glass parity
  HTML-only; does NOT touch markdown table widgets.
  Mirrors the markdown-table-widget token blocks defined in
  dev/10d-liquid-glass-core.css. Selector intentionally excludes
  `.cm-callout` containers AND the markdown widget's inner
  `<table class="cm-table">`, so markdown tables never receive
  these declarations.

  Loaded after 10d-liquid-glass-core.css per dev/_order.txt so its
  late position keeps the cascade ordering identical to vanilla 10d.
   ============================================================ */
.markdown-source-view.mod-cm6 :is(.cm-html-embed, .cm-embed-block:not(.cm-callout)) table:not(.cm-table) { --ogd-table-surface: radial-gradient(circle at 42% 14%, rgba(255, 255, 255, 0.62), transparent 0 30%), linear-gradient(180deg, rgba(255, 255, 255, 0.82), rgba(248, 250, 252, 0.54)); --ogd-table-head-bg: radial-gradient(circle at 44% 12%, rgba(255, 255, 255, 0.70), transparent 0 30%), linear-gradient(180deg, rgba(248, 250, 252, 0.92), rgba(241, 245, 249, 0.66)); --ogd-table-border: rgba(203, 213, 225, 0.58); --ogd-table-cell-border: rgba(226, 232, 240, 0.84); --ogd-table-row-hover: rgba(240, 249, 255, 0.54); --ogd-table-row-even: rgba(248, 250, 252, 0.62); --ogd-table-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.88); background: var(--ogd-table-surface) !important; border-color: var(--ogd-table-border) !important; box-shadow: var(--ogd-table-shadow) !important; }
.markdown-source-view.mod-cm6 :is(.cm-html-embed, .cm-embed-block:not(.cm-callout)) table:not(.cm-table) th { background: var(--ogd-table-head-bg) !important; color: var(--ogd-text-slate, #334155) !important; border-color: var(--ogd-table-cell-border) !important; border-bottom-color: rgba(148, 163, 184, 0.58) !important; font-weight: 780 !important; }
.markdown-source-view.mod-cm6 :is(.cm-html-embed, .cm-embed-block:not(.cm-callout)) table:not(.cm-table) td { border-color: var(--ogd-table-cell-border) !important; color: var(--ogd-text-slate, #334155) !important; }
body.ogd-zebra-disabled-permanently .markdown-source-view.mod-cm6 :is(.cm-html-embed, .cm-embed-block:not(.cm-callout)) table:not(.cm-table) tbody tr:nth-child(even) td { background: var(--ogd-table-row-even) !important; }
.markdown-source-view.mod-cm6 :is(.cm-html-embed, .cm-embed-block:not(.cm-callout)) table:not(.cm-table) tbody tr:hover td { background: var(--ogd-table-row-hover) !important; }
:is(body.ogd-report-mode .markdown-source-view.mod-cm6, .markdown-source-view.mod-cm6.ogd-report-mode) :is(.cm-html-embed, .cm-embed-block:not(.cm-callout)) table:not(.cm-table) { --ogd-table-surface: linear-gradient(180deg, rgba(255, 255, 255, 0.98), rgba(255, 255, 255, 0.92)); --ogd-table-head-bg: linear-gradient(180deg, #f1f5f9, #e8eef6); --ogd-table-border: rgba(148, 163, 184, 0.72); --ogd-table-cell-border: rgba(203, 213, 225, 0.92); --ogd-table-row-hover: #f8fafc; --ogd-table-row-even: #fbfdff; --ogd-table-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.96); table-layout: auto !important; }
.theme-dark .markdown-source-view.mod-cm6 :is(.cm-html-embed, .cm-embed-block:not(.cm-callout)) table:not(.cm-table) { --ogd-table-surface: radial-gradient(circle at 42% 14%, rgba(255, 255, 255, 0.12), transparent 0 30%), linear-gradient(180deg, rgba(30, 41, 59, 0.68), rgba(15, 23, 42, 0.48)); --ogd-table-head-bg: radial-gradient(circle at 44% 12%, rgba(255, 255, 255, 0.13), transparent 0 30%), linear-gradient(180deg, rgba(51, 65, 85, 0.72), rgba(30, 41, 59, 0.58)); --ogd-table-border: rgba(203, 213, 225, 0.20); --ogd-table-cell-border: rgba(71, 85, 105, 0.56); --ogd-table-row-hover: rgba(51, 65, 85, 0.42); --ogd-table-row-even: rgba(15, 23, 42, 0.26); --ogd-table-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.08); }
.theme-dark :is(body.ogd-report-mode .markdown-source-view.mod-cm6, .markdown-source-view.mod-cm6.ogd-report-mode) :is(.cm-html-embed, .cm-embed-block:not(.cm-callout)) table:not(.cm-table), body.theme-dark.ogd-report-mode .markdown-source-view.mod-cm6 :is(.cm-html-embed, .cm-embed-block:not(.cm-callout)) table:not(.cm-table) { --ogd-table-surface: linear-gradient(180deg, rgba(30, 41, 59, 0.76), rgba(15, 23, 42, 0.62)); --ogd-table-head-bg: linear-gradient(180deg, rgba(51, 65, 85, 0.82), rgba(30, 41, 59, 0.74)); --ogd-table-border: rgba(203, 213, 225, 0.28); --ogd-table-cell-border: rgba(71, 85, 105, 0.72); --ogd-table-row-hover: rgba(51, 65, 85, 0.50); --ogd-table-row-even: rgba(15, 23, 42, 0.36); --ogd-table-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.10); }
body.theme-dark:not(.ogd-report-mode) .markdown-source-view.mod-cm6 :is(.cm-html-embed, .cm-embed-block:not(.cm-callout)) table:not(.cm-table) { --ogd-table-tint: rgba(14, 165, 233, 0.10); --ogd-table-surface: radial-gradient(circle at 44% 0%, rgba(255, 255, 255, 0.14), transparent 0 32%), linear-gradient(142deg, rgba(255, 255, 255, 0.10), transparent 34%), linear-gradient(180deg, rgba(30, 41, 59, 0.70), rgba(15, 23, 42, 0.54)), linear-gradient(135deg, var(--ogd-table-tint), transparent 66%); --ogd-table-head-bg: radial-gradient(circle at 44% 0%, rgba(255, 255, 255, 0.14), transparent 0 34%), linear-gradient(180deg, rgba(51, 65, 85, 0.72), rgba(30, 41, 59, 0.58)); --ogd-table-border: rgba(203, 213, 225, 0.20); --ogd-table-cell-border: rgba(71, 85, 105, 0.58); --ogd-table-row-hover: rgba(51, 65, 85, 0.44); --ogd-table-row-even: rgba(15, 23, 42, 0.28); --ogd-table-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.10); }
body.theme-dark:not(.ogd-report-mode) .markdown-source-view.mod-cm6 :is(.cm-html-embed, .cm-embed-block:not(.cm-callout)) table:not(.cm-table) th { border-bottom-color: rgba(148, 163, 184, 0.34) !important; color: var(--text-normal, #e5edf7) !important; }
body.theme-dark:not(.ogd-report-mode) .markdown-source-view.mod-cm6 :is(.cm-html-embed, .cm-embed-block:not(.cm-callout)) table:not(.cm-table) td { color: var(--text-normal, #e5edf7) !important; }
"""


def strip_v2309_from_core() -> tuple[bool, int]:
    text = CORE.read_text(encoding="utf-8")
    needle_at = text.find(V2309_HEADER)
    if needle_at == -1:
        return False, text.count("\n") + 1

    # Walk back to whichever comment opener is closer (long banner OR short comment).
    long_open = text.rfind(COMMENT_BLOCK_OPEN, 0, needle_at)
    short_open = text.rfind(SHORT_V2309_COMMENT, 0, needle_at + len(SHORT_V2309_COMMENT))
    candidates = [c for c in (long_open, short_open) if c != -1]
    if not candidates:
        return False, text.count("\n") + 1
    block_start = max(candidates)

    new_text = text[:block_start].rstrip() + "\n"
    CORE.write_text(new_text, encoding="utf-8", newline="\n")
    return True, new_text.count("\n") + 1


def write_new_module() -> int:
    NEW_MODULE.write_text(NEW_MODULE_TEXT, encoding="utf-8", newline="\n")
    return NEW_MODULE_TEXT.count("\n") + 1


def update_order() -> bool:
    lines = ORDER.read_text(encoding="utf-8").splitlines()
    if ORDER_NEW in lines:
        return False
    if ORDER_PREV not in lines:
        raise RuntimeError(f"{ORDER_PREV!r} not found in dev/_order.txt")
    insert_at = lines.index(ORDER_PREV) + 1
    lines.insert(insert_at, ORDER_NEW)
    ORDER.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return True


def update_validator() -> bool:
    text = VALIDATOR.read_text(encoding="utf-8")
    if REQ_NEW in text:
        return False
    if REQ_PREV not in text:
        raise RuntimeError(f"{REQ_PREV!r} not found in scripts/validate_theme.py")
    new_text = text.replace(REQ_PREV, REQ_PREV + "\n" + REQ_NEW, 1)
    VALIDATOR.write_text(new_text, encoding="utf-8", newline="\n")
    return True


def main() -> int:
    stripped, core_lines = strip_v2309_from_core()
    print(f"[1/4] {'stripped v2.30.9 block from' if stripped else 'no v2.30.9 block in'} 10d — line count {core_lines}")

    new_lines = write_new_module()
    print(f"[2/4] wrote {NEW_MODULE.relative_to(ROOT)} — {new_lines} lines")

    if update_order():
        print(f"[3/4] inserted {ORDER_NEW!r} into dev/_order.txt after {ORDER_PREV!r}")
    else:
        print(f"[3/4] dev/_order.txt already contains {ORDER_NEW!r}")

    if update_validator():
        print(f"[4/4] inserted {REQ_NEW.strip()!r} into REQUIRED_FILES in scripts/validate_theme.py")
    else:
        print("[4/4] scripts/validate_theme.py REQUIRED_FILES already contains the new module")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
