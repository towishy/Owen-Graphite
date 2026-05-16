# v3 Token Inventory (extracted from v2.30.14)

이 문서는 `scripts/extract_token_inventory.py`가 자동 생성합니다.
v3-rewrite는 아래 모든 토큰 이름을 동일하게 선언하고, light/dark default 값이 일치해야 합니다.

- 총 토큰: **255**
- light(`:root`) default 정의: **57**
- dark(`.theme-dark`) default 정의: **177**

## 카테고리 분류

| prefix | 추정 책임 |
| --- | --- |
| `--ogd-glass-*` | Liquid Glass surface (rest/hover/active/disabled) |
| `--ogd-table-*` | 표 surface tokens |
| `--ogd-callout-*` | callout surface tokens |
| `--ogd-text-*` | 텍스트 색 토큰 |
| `--ogd-line-*`, `--ogd-border-*` | 분리선·테두리 |
| `--ogd-radius-*` | radius scale |
| `--ogd-shadow-*` | shadow scale |
| `--ogd-last-page-footer-*` | PDF 마지막 페이지 footer |
| 기타 `--ogd-*` | feature-specific |

## 토큰 목록 (light default | dark default | 사용 횟수 | 정의 위치 수)

| token | light default | dark default | uses | defs |
| --- | --- | --- | ---: | ---: |
| `--ogd-09b-control-bg` | `—` | `var(--ogd-glass-control-bg, linear-gradient(180deg, rgba(51,65,85,0.55), rgba…` | 4 | 2 |
| `--ogd-09b-control-border` | `—` | `rgba(148,163,184,0.22)` | 4 | 2 |
| `--ogd-09b-control-hover-bg` | `—` | `var(--ogd-glass-control-hover-bg, radial-gradient(circle at 76% 32%, rgba(148…` | 4 | 2 |
| `--ogd-09b-control-hover-shadow` | `—` | `inset 0 1px 0 rgba(255,255,255,0.18), inset 0 -1px 0 rgba(203,213,225,0.08), …` | 4 | 2 |
| `--ogd-09b-control-shadow` | `—` | `inset 0 1px 0 rgba(255,255,255,0.06), inset 0 -1px 0 rgba(0,0,0,0.30)` | 4 | 2 |
| `--ogd-09b-floating-bg` | `—` | `var(--ogd-glass-toolbar-bg, linear-gradient(180deg, rgba(30,41,59,0.78), rgba…` | 3 | 2 |
| `--ogd-09b-floating-border` | `—` | `rgba(203,213,225,0.18)` | 3 | 2 |
| `--ogd-09b-floating-shadow` | `—` | `inset 0 1px 0 rgba(255,255,255,0.08), inset 0 -1px 0 rgba(0,0,0,0.35), 0 14px…` | 3 | 2 |
| `--ogd-09b-toolbar-bg` | `—` | `var(--ogd-glass-toolbar-bg, linear-gradient(180deg, rgba(30,41,59,0.78), rgba…` | 3 | 2 |
| `--ogd-09b-toolbar-border` | `—` | `rgba(203,213,225,0.18)` | 3 | 2 |
| `--ogd-09b-toolbar-shadow` | `—` | `inset 0 1px 0 rgba(255,255,255,0.08), inset 0 -1px 0 rgba(0,0,0,0.35), 0 6px …` | 3 | 2 |
| `--ogd-accent` | `#4b5563` | `—` | 9 | 6 |
| `--ogd-blockquote-bg-1` | `—` | `#1f242b` | 2 | 1 |
| `--ogd-blockquote-bg-2` | `—` | `#252b34` | 2 | 1 |
| `--ogd-blockquote-bg-3` | `—` | `#2c333d` | 2 | 1 |
| `--ogd-body-size` | `15px` | `—` | 3 | 1 |
| `--ogd-border-none` | `0` | `—` | 32 | 1 |
| `--ogd-callout-accent` | `—` | `#99f6e4` | 34 | 31 |
| `--ogd-callout-bg` | `—` | `radial-gradient(circle at 42% 0%, rgba(255, 255, 255, 0.14), transparent 0 34…` | 8 | 5 |
| `--ogd-callout-border` | `—` | `rgba(203, 213, 225, 0.18)` | 46 | 35 |
| `--ogd-callout-icon-bg` | `—` | `radial-gradient(circle at 42% 10%, rgba(255, 255, 255, 0.14), transparent 0 3…` | 8 | 5 |
| `--ogd-callout-icon-ring` | `—` | `rgba(45, 212, 191, 0.12)` | 34 | 31 |
| `--ogd-callout-shadow` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.10)` | 8 | 4 |
| `--ogd-callout-shadow-focus` | `—` | `0 0 0 4px rgba(103, 232, 249, 0.09), inset 0 1px 0 rgba(255, 255, 255, 0.12)` | 3 | 2 |
| `--ogd-callout-tint` | `—` | `rgba(148, 163, 184, 0.08)` | 38 | 33 |
| `--ogd-codeblock-bg` | `—` | `radial-gradient(circle at 78% 16%, rgba(125, 211, 252, 0.14), transparent 0 3…` | 14 | 6 |
| `--ogd-codeblock-border` | `—` | `rgba(203, 213, 225, 0.68)` | 11 | 6 |
| `--ogd-codeblock-code-overflow-wrap` | `—` | `—` | 2 | 1 |
| `--ogd-codeblock-code-padding` | `—` | `2.9em 1.1em 1.05em` | 8 | 6 |
| `--ogd-codeblock-code-white-space` | `—` | `—` | 2 | 1 |
| `--ogd-codeblock-header-` | `—` | `—` | 1 | 0 |
| `--ogd-codeblock-header-bg` | `—` | `rgba(248, 250, 252, 0.58)` | 9 | 6 |
| `--ogd-codeblock-header-border` | `—` | `rgba(148, 163, 184, 0.36)` | 15 | 6 |
| `--ogd-codeblock-header-font-size` | `—` | `—` | 2 | 1 |
| `--ogd-codeblock-header-padding` | `—` | `—` | 1 | 1 |
| `--ogd-codeblock-margin` | `—` | `—` | 3 | 1 |
| `--ogd-codeblock-radius` | `—` | `—` | 3 | 2 |
| `--ogd-codeblock-rim` | `—` | `rgba(255, 255, 255, 0.82)` | 4 | 2 |
| `--ogd-codeblock-shadow` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.82), inset 0 -1px 0 rgba(15, 23, 42, 0.08…` | 7 | 4 |
| `--ogd-codeblock-wrapper-margin` | `—` | `—` | 3 | 1 |
| `--ogd-direct-parent-folder-halo-bg` | `—` | `radial-gradient(circle at 68% 22%, rgba(255, 255, 255, 0.14), transparent 38%…` | 3 | 2 |
| `--ogd-direct-parent-folder-halo-border` | `—` | `rgba(186, 230, 253, 0.30)` | 3 | 2 |
| `--ogd-direct-parent-folder-halo-shadow` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.12), inset 0 -1px 0 rgba(0, 0, 0, 0.24), …` | 3 | 2 |
| `--ogd-direct-parent-folder-icon` | `—` | `#cbd5e1` | 3 | 2 |
| `--ogd-direct-parent-folder-icon-opacity` | `—` | `0.68` | 3 | 2 |
| `--ogd-doc-caption-color` | `—` | `var(--ogd-text-soft, #94a3b8)` | 3 | 2 |
| `--ogd-doc-glass-bg` | `—` | `radial-gradient(circle at 74% 14%, rgba(255, 255, 255, 0.10), transparent 0 3…` | 7 | 2 |
| `--ogd-doc-glass-shadow` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.10), inset 0 -1px 0 rgba(0, 0, 0, 0.24), …` | 5 | 2 |
| `--ogd-doc-rim` | `—` | `rgba(51, 65, 85, 0.92)` | 4 | 2 |
| `--ogd-doc-rim-soft` | `—` | `rgba(51, 65, 85, 0.78)` | 3 | 2 |
| `--ogd-first-page-header` | `""` | `—` | 2 | 1 |
| `--ogd-first-page-header-color` | `#111827` | `—` | 3 | 1 |
| `--ogd-first-page-header-left` | `""` | `—` | 2 | 1 |
| `--ogd-first-page-header-left-color` | `#0ea5e9` | `—` | 3 | 1 |
| `--ogd-fp-label-color` | `#6b7280` | `—` | 3 | 1 |
| `--ogd-fp-left-label` | `""` | `—` | 2 | 1 |
| `--ogd-fp-right-label` | `""` | `—` | 2 | 1 |
| `--ogd-glass-bg` | `—` | `radial-gradient(circle at 76% 26%, rgba(148, 163, 184, 0.16), transparent 36%…` | 18 | 14 |
| `--ogd-glass-bg-hover` | `—` | `radial-gradient(circle at 76% 24%, rgba(148, 163, 184, 0.19), transparent 35%…` | 27 | 14 |
| `--ogd-glass-bg-strong` | `—` | `radial-gradient(circle at 74% 24%, rgba(148, 163, 184, 0.18), transparent 36%…` | 24 | 14 |
| `--ogd-glass-border` | `—` | `rgba(203, 213, 225, 0.22)` | 21 | 8 |
| `--ogd-glass-border-hover` | `—` | `rgba(186, 230, 253, 0.30)` | 20 | 8 |
| `--ogd-glass-control-bg` | `linear-gradient(180deg, rgba(255,255,255,0.55), rgba(241,245,249,0.22))` | `radial-gradient(circle at 74% 26%, rgba(148,163,184,0.18), transparent 35%), …` | 18 | 6 |
| `--ogd-glass-control-hover-bg` | `radial-gradient(circle at 74% 24%, rgba(255,255,255,0.72), transparent 36%), …` | `radial-gradient(circle at 76% 24%, rgba(148,163,184,0.20), transparent 35%), …` | 9 | 6 |
| `--ogd-glass-control-shadow` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.12), inset 0 -1px 0 rgba(0, 0, 0, 0.30), …` | 23 | 7 |
| `--ogd-glass-filter` | `—` | `—` | 31 | 11 |
| `--ogd-glass-filter-control` | `—` | `—` | 77 | 11 |
| `--ogd-glass-filter-soft` | `—` | `—` | 59 | 11 |
| `--ogd-glass-shadow` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.16), inset 0 -1px 0 rgba(0, 0, 0, 0.38), …` | 20 | 14 |
| `--ogd-glass-shadow-hover` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.18), inset 0 -1px 0 rgba(0, 0, 0, 0.26), …` | 28 | 14 |
| `--ogd-glass-surface-bg` | `linear-gradient(180deg, rgba(255,255,255,0.88), rgba(241,245,249,0.50))` | `radial-gradient(circle at 76% 26%, rgba(148, 163, 184, 0.15), transparent 35%…` | 12 | 6 |
| `--ogd-glass-toolbar-bg` | `linear-gradient(180deg, rgba(255,255,255,0.92), rgba(241,245,249,0.55))` | `radial-gradient(circle at 78% 24%, rgba(148, 163, 184, 0.16), transparent 35%…` | 12 | 6 |
| `--ogd-glass-transition` | `—` | `—` | 4 | 1 |
| `--ogd-glass-transition-control` | `—` | `—` | 7 | 1 |
| `--ogd-graph-control-bg` | `—` | `radial-gradient(circle at 74% 35%, rgba(148, 163, 184, 0.14), transparent 34%…` | 5 | 4 |
| `--ogd-graph-control-border` | `—` | `rgba(203, 213, 225, 0.14)` | 5 | 4 |
| `--ogd-graph-control-color` | `—` | `var(--ogd-text-inverted, #f8fafc)` | 4 | 3 |
| `--ogd-graph-control-shadow` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.10), 0 2px 7px rgba(0, 0, 0, 0.20)` | 5 | 4 |
| `--ogd-heading-border` | `—` | `rgba(203, 213, 225, 0.18)` | 7 | 3 |
| `--ogd-heading-border-soft` | `—` | `rgba(71, 85, 105, 0.62)` | 5 | 3 |
| `--ogd-heading-h1-bg` | `—` | `radial-gradient(circle at 78% 18%, rgba(125, 211, 252, 0.10), transparent 0 3…` | 5 | 3 |
| `--ogd-heading-h2-bg` | `—` | `linear-gradient(180deg, rgba(30, 41, 59, 0.60), rgba(15, 23, 42, 0.38))` | 4 | 3 |
| `--ogd-heading-rule` | `—` | `linear-gradient(90deg, rgba(103, 232, 249, 0.46), rgba(71, 85, 105, 0.62), tr…` | 4 | 3 |
| `--ogd-heading-rule-soft` | `—` | `linear-gradient(90deg, rgba(203, 213, 225, 0.34), rgba(71, 85, 105, 0.16), tr…` | 4 | 3 |
| `--ogd-heading-shadow` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.12), inset 0 -1px 0 rgba(0, 0, 0, 0.24), …` | 4 | 3 |
| `--ogd-hover-lift` | `translateY(-1px)` | `—` | 19 | 5 |
| `--ogd-hover-lift-strong` | `translateY(-2px)` | `—` | 5 | 4 |
| `--ogd-hover-lift-subtle` | `translateY(-0.5px)` | `—` | 6 | 5 |
| `--ogd-hover-shift` | `translateX(1px)` | `—` | 7 | 5 |
| `--ogd-html-table-axis-bg` | `—` | `linear-gradient(180deg, rgba(30, 41, 59, 0.76), rgba(15, 23, 42, 0.50))` | 6 | 4 |
| `--ogd-html-table-border` | `—` | `rgba(203, 213, 225, 0.26)` | 7 | 4 |
| `--ogd-html-table-caption-bg` | `—` | `radial-gradient(circle at 82% 18%, rgba(14, 165, 233, 0.18), transparent 0 36…` | 5 | 4 |
| `--ogd-html-table-cell-border` | `—` | `rgba(71, 85, 105, 0.68)` | 8 | 4 |
| `--ogd-html-table-head-bg` | `—` | `radial-gradient(circle at 42% 10%, rgba(255, 255, 255, 0.14), transparent 0 3…` | 6 | 4 |
| `--ogd-html-table-shadow` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.11), inset 0 -1px 0 rgba(0, 0, 0, 0.22), …` | 6 | 4 |
| `--ogd-html-table-surface` | `—` | `radial-gradient(circle at 78% 12%, rgba(255, 255, 255, 0.13), transparent 0 3…` | 6 | 4 |
| `--ogd-inline-code-bg` | `—` | `#2a2f37` | 2 | 1 |
| `--ogd-last-page-footer-body` | `""` | `—` | 3 | 1 |
| `--ogd-last-page-footer-color` | `#0ea5e9` | `—` | 6 | 1 |
| `--ogd-last-page-footer-label` | `""` | `—` | 2 | 1 |
| `--ogd-last-page-footer-label-color` | `#64748b` | `—` | 4 | 1 |
| `--ogd-last-page-footer-text-color` | `#334155` | `—` | 6 | 1 |
| `--ogd-last-page-footer-title` | `""` | `—` | 3 | 1 |
| `--ogd-last-page-footer-title-color` | `#0f172a` | `—` | 7 | 1 |
| `--ogd-lg-border` | `—` | `rgba(203, 213, 225, 0.18)` | 13 | 2 |
| `--ogd-lg-border-hover` | `—` | `rgba(186, 230, 253, 0.30)` | 8 | 2 |
| `--ogd-lg-control-bg` | `—` | `radial-gradient(circle at 44% 12%, rgba(255, 255, 255, 0.12), transparent 0 2…` | 14 | 3 |
| `--ogd-lg-edge` | `—` | `rgba(255, 255, 255, 0.18)` | 20 | 2 |
| `--ogd-lg-edge-low` | `—` | `rgba(15, 23, 42, 0.64)` | 2 | 2 |
| `--ogd-lg-frost-halo` | `—` | `rgba(103, 232, 249, 0.10)` | 6 | 2 |
| `--ogd-lg-frost-outline` | `—` | `rgba(103, 232, 249, 0.18)` | 14 | 2 |
| `--ogd-lg-frost-rim` | `—` | `rgba(103, 232, 249, 0.42)` | 16 | 2 |
| `--ogd-lg-mist-fill` | `—` | `rgba(14, 116, 144, 0.20)` | 3 | 2 |
| `--ogd-lg-mist-glow` | `—` | `rgba(186, 230, 253, 0.10)` | 4 | 2 |
| `--ogd-lg-mist-line` | `—` | `rgba(125, 211, 252, 0.22)` | 4 | 2 |
| `--ogd-lg-mist-rim` | `—` | `—` | 5 | 1 |
| `--ogd-lg-mist-rim-dark` | `—` | `—` | 1 | 1 |
| `--ogd-lg-pane-header-shadow` | `—` | `inset 0 1px 0 var(--ogd-lg-edge), 0 7px 16px rgba(0, 0, 0, 0.24)` | 3 | 2 |
| `--ogd-lg-pane-shell-shadow` | `—` | `inset 0 1px 0 var(--ogd-lg-edge), 0 10px 26px rgba(0, 0, 0, 0.30)` | 3 | 2 |
| `--ogd-lg-refined-active-bg` | `—` | `radial-gradient(circle at 76% 18%, rgba(255, 255, 255, 0.16), transparent 0 3…` | 4 | 2 |
| `--ogd-lg-refined-border` | `—` | `rgba(203, 213, 225, 0.20)` | 7 | 2 |
| `--ogd-lg-refined-border-hover` | `—` | `rgba(186, 230, 253, 0.30)` | 3 | 2 |
| `--ogd-lg-refined-focus-shadow` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.16), 0 16px 38px rgba(0, 0, 0, 0.40), 0 0…` | 4 | 2 |
| `--ogd-lg-refined-hover-bg` | `—` | `radial-gradient(circle at 76% 18%, rgba(255, 255, 255, 0.17), transparent 0 3…` | 3 | 2 |
| `--ogd-lg-refined-rest-bg` | `—` | `radial-gradient(circle at 76% 18%, rgba(255, 255, 255, 0.13), transparent 0 3…` | 5 | 2 |
| `--ogd-lg-refined-shadow` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.12), inset 0 -1px 0 rgba(0, 0, 0, 0.28), …` | 5 | 2 |
| `--ogd-lg-refined-shadow-hover` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.16), inset 0 -1px 0 rgba(0, 0, 0, 0.26), …` | 5 | 2 |
| `--ogd-lg-row-active-bg` | `—` | `radial-gradient(circle at 42% 16%, rgba(255, 255, 255, 0.14), transparent 0 3…` | 3 | 2 |
| `--ogd-lg-row-active-shadow` | `—` | `0 20px 48px rgba(0, 0, 0, 0.44), 0 7px 20px rgba(0, 0, 0, 0.30), 0 0 0 1px rg…` | 3 | 2 |
| `--ogd-lg-shadow` | `—` | `0 18px 46px rgba(0, 0, 0, 0.46), 0 6px 18px rgba(0, 0, 0, 0.32), inset 0 1px …` | 5 | 3 |
| `--ogd-lg-shadow-active` | `—` | `0 22px 54px rgba(0, 0, 0, 0.54), 0 0 0 3px var(--ogd-lg-mist-glow), inset 0 0…` | 5 | 3 |
| `--ogd-lg-shadow-focus` | `—` | `0 18px 46px rgba(0, 0, 0, 0.46), 0 0 0 3px var(--ogd-lg-frost-halo), inset 0 …` | 15 | 3 |
| `--ogd-lg-shadow-hover` | `—` | `0 30px 72px rgba(0, 0, 0, 0.56), 0 12px 28px rgba(0, 0, 0, 0.38), inset 0 1px…` | 6 | 3 |
| `--ogd-lg-surface-bg` | `—` | `radial-gradient(circle at 44% 12%, rgba(255, 255, 255, 0.14), transparent 0 2…` | 8 | 3 |
| `--ogd-lg-surface-bg-active` | `—` | `radial-gradient(circle at 44% 12%, rgba(255, 255, 255, 0.14), transparent 0 2…` | 8 | 3 |
| `--ogd-lg-surface-bg-hover` | `—` | `radial-gradient(circle at 44% 12%, rgba(255, 255, 255, 0.16), transparent 0 2…` | 12 | 3 |
| `--ogd-lg-tab-border` | `—` | `—` | 3 | 1 |
| `--ogd-lg-tab-border-hover` | `—` | `rgba(203, 213, 225, 0.18)` | 4 | 2 |
| `--ogd-lg-tab-focus-outline` | `—` | `var(--ogd-surface-transparent, transparent)` | 2 | 2 |
| `--ogd-lg-tab-shadow` | `—` | `0 16px 38px rgba(0, 0, 0, 0.42), 0 5px 14px rgba(0, 0, 0, 0.28), inset 0 1px …` | 4 | 2 |
| `--ogd-lg-tab-shadow-hover` | `—` | `0 24px 54px rgba(0, 0, 0, 0.50), 0 8px 18px rgba(0, 0, 0, 0.32), inset 0 1px …` | 4 | 2 |
| `--ogd-line-contrast` | `#374151` | `—` | 6 | 1 |
| `--ogd-line-dark` | `#334155` | `—` | 11 | 1 |
| `--ogd-line-faint` | `#94a3b8` | `—` | 2 | 1 |
| `--ogd-line-height` | `1.5` | `—` | 5 | 4 |
| `--ogd-line-ink` | `#111827` | `—` | 4 | 1 |
| `--ogd-line-muted` | `#475569` | `—` | 4 | 1 |
| `--ogd-line-soft` | `#e5e7eb` | `—` | 54 | 1 |
| `--ogd-line-strong` | `#cbd5e1` | `—` | 77 | 1 |
| `--ogd-list-marker-bg` | `—` | `radial-gradient(circle at 34% 26%, rgba(255, 255, 255, 0.28), rgba(255, 255, …` | 10 | 5 |
| `--ogd-list-marker-bg-active` | `—` | `radial-gradient(circle at 34% 26%, rgba(255, 255, 255, 0.32), rgba(255, 255, …` | 4 | 3 |
| `--ogd-list-marker-border` | `—` | `rgba(186, 230, 253, 0.32)` | 9 | 5 |
| `--ogd-list-marker-shadow` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.12), inset 0 -1px 0 rgba(0, 0, 0, 0.30), …` | 10 | 5 |
| `--ogd-list-marker-shadow-active` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.16), inset 0 -1px 0 rgba(0, 0, 0, 0.26), …` | 4 | 3 |
| `--ogd-list-nested-marker` | `—` | `rgba(186, 230, 253, 0.28)` | 7 | 5 |
| `--ogd-list-task-border` | `—` | `rgba(203, 213, 225, 0.20)` | 4 | 3 |
| `--ogd-list-task-shadow` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.12), 0 10px 24px rgba(0, 0, 0, 0.30)` | 4 | 3 |
| `--ogd-list-task-surface` | `—` | `radial-gradient(circle at 76% 18%, rgba(255, 255, 255, 0.13), transparent 0 3…` | 4 | 3 |
| `--ogd-lp-cell-focus-bg` | `—` | `linear-gradient(180deg, rgba(14, 116, 144, 0.20), rgba(15, 23, 42, 0.14))` | 3 | 2 |
| `--ogd-lp-code-bg` | `—` | `rgba(248, 250, 252, 0.84)` | 6 | 4 |
| `--ogd-lp-code-border` | `—` | `rgba(203, 213, 225, 0.68)` | 8 | 4 |
| `--ogd-lp-doc-glass-bg` | `—` | `radial-gradient(circle at 74% 14%, rgba(255, 255, 255, 0.10), transparent 0 3…` | 6 | 2 |
| `--ogd-lp-doc-glass-shadow` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.10), inset 0 -1px 0 rgba(0, 0, 0, 0.24), …` | 5 | 2 |
| `--ogd-lp-doc-rim` | `—` | `rgba(51, 65, 85, 0.92)` | 5 | 2 |
| `--ogd-lp-doc-rim-soft` | `—` | `rgba(51, 65, 85, 0.78)` | 3 | 2 |
| `--ogd-lp-focus-bg` | `—` | `linear-gradient(180deg, rgba(51, 65, 85, 0.34), rgba(14, 116, 144, 0.16))` | 2 | 2 |
| `--ogd-lp-focus-outline` | `—` | `rgba(103, 232, 249, 0.28)` | 2 | 2 |
| `--ogd-lp-focus-rim` | `—` | `rgba(103, 232, 249, 0.42)` | 3 | 2 |
| `--ogd-lp-focus-shadow` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.10), 0 0 0 1px rgba(103, 232, 249, 0.08),…` | 3 | 2 |
| `--ogd-macos-toggle-bg` | `—` | `linear-gradient(180deg, rgba(51, 65, 85, 0.78), rgba(15, 23, 42, 0.55))` | 4 | 3 |
| `--ogd-macos-toggle-border` | `—` | `1px solid rgba(203, 213, 225, 0.22)` | 4 | 3 |
| `--ogd-macos-toggle-color` | `—` | `var(--ogd-text-inverted, #f8fafc)` | 4 | 3 |
| `--ogd-macos-toggle-shadow` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.12), inset 0 -1px 0 rgba(0, 0, 0, 0.28), …` | 4 | 3 |
| `--ogd-max-width` | `420mm` | `—` | 3 | 1 |
| `--ogd-overlay-selected-bg` | `—` | `rgba(51, 65, 85, 0.78)` | 3 | 2 |
| `--ogd-overlay-selected-line` | `—` | `var(--ogd-line-strong, #cbd5e1)` | 3 | 2 |
| `--ogd-overlay-selected-text` | `—` | `var(--ogd-surface-muted, #f8fafc)` | 3 | 2 |
| `--ogd-plugin-dark-card-bg` | `—` | `radial-gradient(circle at 78% 18%, rgba(148, 163, 184, 0.12), transparent 34%…` | 3 | 1 |
| `--ogd-plugin-dark-card-hover-shadow` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.10), 0 8px 18px rgba(0, 0, 0, 0.34), 0 0 …` | 3 | 1 |
| `--ogd-plugin-dark-card-shadow` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.08), 0 4px 12px rgba(0, 0, 0, 0.26)` | 3 | 1 |
| `--ogd-plugin-dark-surface-bg` | `—` | `radial-gradient(circle at 78% 18%, rgba(148, 163, 184, 0.11), transparent 34%…` | 3 | 1 |
| `--ogd-plugin-dark-surface-border` | `—` | `rgba(203, 213, 225, 0.14)` | 3 | 1 |
| `--ogd-plugin-dark-surface-shadow` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.08), 0 5px 14px rgba(0, 0, 0, 0.24)` | 3 | 1 |
| `--ogd-press-lift` | `translateY(0) scale(0.99)` | `—` | 7 | 5 |
| `--ogd-print-caption-text` | `—` | `#475569` | 2 | 1 |
| `--ogd-print-table-bg` | `—` | `rgba(255, 255, 255, 0.72)` | 5 | 1 |
| `--ogd-print-table-border` | `—` | `rgba(203, 213, 225, 0.40)` | 6 | 1 |
| `--ogd-print-table-cell-bg` | `—` | `rgba(255, 255, 255, 0.38)` | 3 | 1 |
| `--ogd-print-table-first-col-bg` | `—` | `rgba(248, 250, 252, 0.34)` | 3 | 1 |
| `--ogd-print-table-head-bg` | `—` | `rgba(248, 250, 252, 0.54)` | 4 | 1 |
| `--ogd-print-table-strong-border` | `—` | `rgba(148, 163, 184, 0.46)` | 2 | 1 |
| `--ogd-print-table-strong-text` | `—` | `#1f2937` | 3 | 1 |
| `--ogd-print-table-text` | `—` | `#334155` | 2 | 1 |
| `--ogd-print-table-zebra-bg` | `—` | `rgba(236, 254, 255, 0.16)` | 4 | 1 |
| `--ogd-radius-control` | `7px` | `—` | 47 | 1 |
| `--ogd-radius-panel` | `—` | `—` | 1 | 0 |
| `--ogd-radius-pill` | `999px` | `—` | 49 | 1 |
| `--ogd-radius-pill-left` | `var(--ogd-radius-pill, 999px) 0 0 var(--ogd-radius-pill, 999px)` | `—` | 2 | 1 |
| `--ogd-radius-top` | `var(--radius-m, 6px) var(--radius-m, 6px) 0 0` | `—` | 4 | 1 |
| `--ogd-ribbon-icon-bg` | `—` | `radial-gradient(circle at 74% 24%, rgba(148, 163, 184, 0.16), transparent 36%…` | 10 | 9 |
| `--ogd-ribbon-icon-border` | `—` | `rgba(203, 213, 225, 0.16)` | 10 | 9 |
| `--ogd-ribbon-icon-color` | `—` | `var(--ogd-line-strong, #cbd5e1)` | 7 | 6 |
| `--ogd-ribbon-icon-shadow` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.11), inset 0 -1px 0 rgba(0, 0, 0, 0.28), …` | 10 | 9 |
| `--ogd-search-hl-bg` | `—` | `rgba(251, 191, 36, 0.22)` | 2 | 1 |
| `--ogd-search-hl-fg` | `—` | `#fde68a` | 2 | 1 |
| `--ogd-search-input-bg` | `—` | `linear-gradient(180deg, rgba(51, 65, 85, 0.82), rgba(15, 23, 42, 0.58))` | 7 | 5 |
| `--ogd-search-input-border` | `—` | `rgba(203, 213, 225, 0.18)` | 5 | 3 |
| `--ogd-search-input-control-bg` | `—` | `linear-gradient(180deg, rgba(51, 65, 85, 0.66), rgba(15, 23, 42, 0.46))` | 6 | 5 |
| `--ogd-search-input-control-border` | `—` | `rgba(203, 213, 225, 0.14)` | 4 | 3 |
| `--ogd-search-input-control-shadow` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.08), 0 4px 12px -10px rgba(0, 0, 0, 0.42)` | 6 | 5 |
| `--ogd-search-input-shadow` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.10), inset 0 -1px 0 rgba(255, 255, 255, 0…` | 7 | 5 |
| `--ogd-shadow-none` | `none` | `—` | 46 | 1 |
| `--ogd-surface-base` | `#ffffff` | `—` | 34 | 1 |
| `--ogd-surface-dark` | `#111827` | `—` | 9 | 1 |
| `--ogd-surface-dark-muted` | `#374151` | `—` | 5 | 1 |
| `--ogd-surface-dark-subtle` | `#334155` | `—` | 5 | 1 |
| `--ogd-surface-muted` | `#f8fafc` | `—` | 24 | 1 |
| `--ogd-surface-subtle` | `#f3f4f6` | `—` | 34 | 1 |
| `--ogd-surface-transparent` | `transparent` | `—` | 113 | 1 |
| `--ogd-tab-glass-bg` | `—` | `linear-gradient(180deg, rgba(71, 85, 105, 0.84), rgba(15, 23, 42, 0.60))` | 7 | 6 |
| `--ogd-tab-glass-bg-hover` | `—` | `rgba(51, 65, 85, 0.34)` | 7 | 6 |
| `--ogd-tab-glass-border` | `—` | `var(--ogd-surface-transparent, transparent)` | 5 | 4 |
| `--ogd-tab-glass-border-bottom` | `—` | `var(--ogd-surface-transparent, transparent)` | 7 | 6 |
| `--ogd-tab-glass-border-hover` | `—` | `var(--ogd-surface-transparent, transparent)` | 5 | 4 |
| `--ogd-tab-glass-shadow` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.13), inset 0 -1px 0 rgba(255, 255, 255, 0…` | 8 | 6 |
| `--ogd-tab-glass-shadow-hover` | `—` | `none` | 7 | 6 |
| `--ogd-tab-header-bg` | `—` | `—` | 4 | 3 |
| `--ogd-tab-header-border-bottom` | `—` | `—` | 3 | 2 |
| `--ogd-tab-header-border-color` | `—` | `—` | 4 | 3 |
| `--ogd-tab-header-shadow` | `—` | `—` | 4 | 3 |
| `--ogd-table-bg` | `—` | `radial-gradient(circle at 78% 12%, rgba(125, 211, 252, 0.10), transparent 0 3…` | 4 | 3 |
| `--ogd-table-border` | `—` | `rgba(71, 85, 105, 0.86)` | 29 | 18 |
| `--ogd-table-cell-border` | `—` | `rgba(51, 65, 85, 0.88)` | 42 | 18 |
| `--ogd-table-font-size` | `—` | `—` | 13 | 10 |
| `--ogd-table-head-bg` | `—` | `linear-gradient(180deg, rgba(51, 65, 85, 0.78), rgba(30, 41, 59, 0.70))` | 34 | 20 |
| `--ogd-table-line-height` | `—` | `—` | 14 | 10 |
| `--ogd-table-pad-x` | `—` | `—` | 13 | 10 |
| `--ogd-table-pad-y` | `—` | `—` | 13 | 10 |
| `--ogd-table-row-even` | `—` | `rgba(30, 41, 59, 0.44)` | 23 | 17 |
| `--ogd-table-row-hover` | `—` | `rgba(8, 145, 178, 0.22)` | 23 | 16 |
| `--ogd-table-shadow` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.10), inset 0 -1px 0 rgba(0, 0, 0, 0.28)` | 24 | 15 |
| `--ogd-table-surface` | `—` | `var(--ogd-print-table-bg)` | 27 | 17 |
| `--ogd-table-tint` | `—` | `rgba(14, 165, 233, 0.10)` | 8 | 4 |
| `--ogd-text-body` | `#1a1a1a` | `—` | 1 | 1 |
| `--ogd-text-inverted` | `#f8fafc` | `—` | 54 | 1 |
| `--ogd-text-muted` | `#64748b` | `—` | 3 | 1 |
| `--ogd-text-secondary` | `#374151` | `—` | 20 | 1 |
| `--ogd-text-slate` | `#334155` | `—` | 69 | 1 |
| `--ogd-text-soft` | `#94a3b8` | `—` | 30 | 1 |
| `--ogd-text-strong` | `#111827` | `—` | 73 | 1 |
| `--ogd-text-subtle` | `#475569` | `—` | 40 | 1 |
| `--ogd-title-rule-end` | `#0284c7` | `—` | 1 | 1 |
| `--ogd-title-rule-start` | `#0f766e` | `—` | 2 | 1 |
| `--ogd-topbar-icon-hover-bg` | `—` | `radial-gradient(circle at 76% 18%, rgba(255, 255, 255, 0.14), transparent 0 3…` | 4 | 2 |
| `--ogd-topbar-icon-hover-shadow` | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.12), 0 10px 20px rgba(0, 0, 0, 0.26)` | 4 | 2 |
