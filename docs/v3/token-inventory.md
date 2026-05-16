# v3 Token Inventory

Current token inventory extracted from `src/**/*.css`.

- 총 토큰: **262**
- light(`:root`) default 정의: **65**
- dark(`.theme-dark`) default 정의: **175**

## 카테고리 분류

| category | tokens |
| --- | ---: |
| Liquid Glass surface | 54 |
| PDF header/footer marginalia | 22 |
| callout surface | 8 |
| feature-specific | 142 |
| line/border | 9 |
| radius | 5 |
| shadow | 1 |
| table surface | 13 |
| text color | 8 |

## 토큰 목록

| token | category | light default | dark default | uses | defs |
| --- | --- | --- | --- | ---: | ---: |
| `--ogd-09b-control-bg` | feature-specific | `—` | `var(--ogd-glass-control-bg, linear-gradient(180deg, rgba(51,65,85,0.55), rgba(30,41,59,0.30)))` | 5 | 3 |
| `--ogd-09b-control-border` | feature-specific | `—` | `rgba(148,163,184,0.22)` | 5 | 3 |
| `--ogd-09b-control-hover-bg` | feature-specific | `—` | `var(--ogd-glass-control-hover-bg, radial-gradient(circle at 76% 32%, rgba(148,163,184,0.14), tr…` | 5 | 3 |
| `--ogd-09b-control-hover-shadow` | feature-specific | `—` | `inset 0 1px 0 rgba(255,255,255,0.18), inset 0 -1px 0 rgba(203,213,225,0.08), 0 8px 20px rgba(0,…` | 5 | 3 |
| `--ogd-09b-control-shadow` | feature-specific | `—` | `inset 0 1px 0 rgba(255,255,255,0.06), inset 0 -1px 0 rgba(0,0,0,0.30)` | 5 | 3 |
| `--ogd-09b-floating-bg` | feature-specific | `—` | `var(--ogd-glass-toolbar-bg, linear-gradient(180deg, rgba(30,41,59,0.78), rgba(15,23,42,0.55)))` | 4 | 3 |
| `--ogd-09b-floating-border` | feature-specific | `—` | `rgba(203,213,225,0.18)` | 4 | 3 |
| `--ogd-09b-floating-shadow` | feature-specific | `—` | `inset 0 1px 0 rgba(255,255,255,0.08), inset 0 -1px 0 rgba(0,0,0,0.35), 0 14px 30px rgba(0,0,0,0…` | 4 | 3 |
| `--ogd-09b-toolbar-bg` | feature-specific | `—` | `var(--ogd-glass-toolbar-bg, linear-gradient(180deg, rgba(30,41,59,0.78), rgba(15,23,42,0.55)))` | 4 | 3 |
| `--ogd-09b-toolbar-border` | feature-specific | `—` | `rgba(203,213,225,0.18)` | 4 | 3 |
| `--ogd-09b-toolbar-shadow` | feature-specific | `—` | `inset 0 1px 0 rgba(255,255,255,0.08), inset 0 -1px 0 rgba(0,0,0,0.35), 0 6px 18px rgba(0,0,0,0.…` | 4 | 3 |
| `--ogd-accent` | feature-specific | `#4b5563` | `—` | 10 | 6 |
| `--ogd-blockquote-bg-1` | feature-specific | `—` | `#1f242b` | 3 | 2 |
| `--ogd-blockquote-bg-2` | feature-specific | `—` | `#252b34` | 3 | 2 |
| `--ogd-blockquote-bg-3` | feature-specific | `—` | `#2c333d` | 3 | 2 |
| `--ogd-body-size` | feature-specific | `15px` | `—` | 3 | 1 |
| `--ogd-border-none` | line/border | `0` | `—` | 31 | 1 |
| `--ogd-callout-accent` | callout surface | `—` | `#a5f3fc` | 34 | 31 |
| `--ogd-callout-bg` | callout surface | `—` | `radial-gradient(circle at 42% 0%, rgba(255, 255, 255, 0.14), transparent 0 34%), linear-gradien…` | 8 | 5 |
| `--ogd-callout-border` | callout surface | `—` | `rgba(203, 213, 225, 0.18)` | 46 | 35 |
| `--ogd-callout-icon-bg` | callout surface | `—` | `radial-gradient(circle at 42% 10%, rgba(255, 255, 255, 0.14), transparent 0 36%), linear-gradie…` | 8 | 5 |
| `--ogd-callout-icon-ring` | callout surface | `—` | `rgba(103, 232, 249, 0.11)` | 34 | 31 |
| `--ogd-callout-shadow` | callout surface | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.10)` | 8 | 4 |
| `--ogd-callout-shadow-focus` | callout surface | `—` | `0 0 0 4px rgba(103, 232, 249, 0.09), inset 0 1px 0 rgba(255, 255, 255, 0.12)` | 3 | 2 |
| `--ogd-callout-tint` | callout surface | `—` | `rgba(148, 163, 184, 0.08)` | 38 | 33 |
| `--ogd-codeblock-bg` | feature-specific | `—` | `radial-gradient(circle at 78% 16%, rgba(125, 211, 252, 0.14), transparent 0 38%), linear-gradie…` | 14 | 6 |
| `--ogd-codeblock-border` | feature-specific | `—` | `rgba(203, 213, 225, 0.68)` | 11 | 6 |
| `--ogd-codeblock-code-overflow-wrap` | feature-specific | `—` | `—` | 2 | 1 |
| `--ogd-codeblock-code-padding` | feature-specific | `—` | `2.9em 1.1em 1.05em` | 8 | 6 |
| `--ogd-codeblock-code-white-space` | feature-specific | `—` | `—` | 2 | 1 |
| `--ogd-codeblock-header-bg` | feature-specific | `—` | `rgba(248, 250, 252, 0.58)` | 9 | 6 |
| `--ogd-codeblock-header-border` | feature-specific | `—` | `rgba(148, 163, 184, 0.36)` | 15 | 6 |
| `--ogd-codeblock-header-font-size` | feature-specific | `—` | `—` | 2 | 1 |
| `--ogd-codeblock-header-padding` | feature-specific | `—` | `—` | 1 | 1 |
| `--ogd-codeblock-margin` | feature-specific | `—` | `—` | 3 | 1 |
| `--ogd-codeblock-radius` | feature-specific | `—` | `—` | 3 | 2 |
| `--ogd-codeblock-rim` | feature-specific | `—` | `rgba(255, 255, 255, 0.82)` | 4 | 2 |
| `--ogd-codeblock-shadow` | feature-specific | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.82), inset 0 -1px 0 rgba(15, 23, 42, 0.08), 0 12px 24px rgb…` | 7 | 4 |
| `--ogd-codeblock-wrapper-margin` | feature-specific | `—` | `—` | 3 | 1 |
| `--ogd-direct-parent-folder-halo-bg` | feature-specific | `—` | `—` | 3 | 2 |
| `--ogd-direct-parent-folder-halo-border` | feature-specific | `—` | `—` | 3 | 2 |
| `--ogd-direct-parent-folder-halo-shadow` | feature-specific | `—` | `—` | 3 | 2 |
| `--ogd-direct-parent-folder-icon` | feature-specific | `—` | `—` | 3 | 2 |
| `--ogd-direct-parent-folder-icon-opacity` | feature-specific | `—` | `—` | 3 | 2 |
| `--ogd-doc-caption-color` | feature-specific | `—` | `var(--ogd-text-soft, #94a3b8)` | 3 | 2 |
| `--ogd-doc-glass-bg` | feature-specific | `—` | `radial-gradient(circle at 74% 14%, rgba(255, 255, 255, 0.10), transparent 0 34%), linear-gradie…` | 7 | 2 |
| `--ogd-doc-glass-shadow` | feature-specific | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.10), inset 0 -1px 0 rgba(0, 0, 0, 0.24), 0 10px 24px rgba(0…` | 5 | 2 |
| `--ogd-doc-rim` | feature-specific | `—` | `rgba(51, 65, 85, 0.92)` | 4 | 2 |
| `--ogd-doc-rim-soft` | feature-specific | `—` | `rgba(51, 65, 85, 0.78)` | 3 | 2 |
| `--ogd-glass-bg` | Liquid Glass surface | `—` | `radial-gradient(circle at 76% 26%, rgba(148, 163, 184, 0.16), transparent 36%), radial-gradient…` | 22 | 18 |
| `--ogd-glass-bg-hover` | Liquid Glass surface | `—` | `radial-gradient(circle at 76% 24%, rgba(148, 163, 184, 0.19), transparent 35%), radial-gradient…` | 29 | 18 |
| `--ogd-glass-bg-strong` | Liquid Glass surface | `—` | `radial-gradient(circle at 74% 24%, rgba(148, 163, 184, 0.18), transparent 36%), radial-gradient…` | 28 | 18 |
| `--ogd-glass-border` | Liquid Glass surface | `—` | `rgba(203, 213, 225, 0.22)` | 23 | 10 |
| `--ogd-glass-border-hover` | Liquid Glass surface | `—` | `rgba(186, 230, 253, 0.30)` | 20 | 10 |
| `--ogd-glass-control-bg` | Liquid Glass surface | `linear-gradient(180deg, rgba(255,255,255,0.55), rgba(241,245,249,0.22))` | `radial-gradient(circle at 74% 26%, rgba(148,163,184,0.18), transparent 35%), linear-gradient(18…` | 20 | 7 |
| `--ogd-glass-control-hover-bg` | Liquid Glass surface | `radial-gradient(circle at 74% 24%, rgba(255,255,255,0.72), transparent 36%), linear-gradient(18…` | `radial-gradient(circle at 76% 24%, rgba(148,163,184,0.20), transparent 35%), radial-gradient(ci…` | 11 | 7 |
| `--ogd-glass-control-shadow` | Liquid Glass surface | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.12), inset 0 -1px 0 rgba(0, 0, 0, 0.30), inset 0 0 12px rgb…` | 24 | 8 |
| `--ogd-glass-filter` | Liquid Glass surface | `—` | `—` | 31 | 11 |
| `--ogd-glass-filter-control` | Liquid Glass surface | `—` | `—` | 77 | 11 |
| `--ogd-glass-filter-soft` | Liquid Glass surface | `—` | `—` | 57 | 11 |
| `--ogd-glass-shadow` | Liquid Glass surface | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.16), inset 0 -1px 0 rgba(0, 0, 0, 0.38), inset 0 0 22px rgb…` | 24 | 18 |
| `--ogd-glass-shadow-hover` | Liquid Glass surface | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.18), inset 0 -1px 0 rgba(0, 0, 0, 0.26), inset 0 0 20px rgb…` | 30 | 18 |
| `--ogd-glass-surface-bg` | Liquid Glass surface | `linear-gradient(180deg, rgba(255,255,255,0.88), rgba(241,245,249,0.50))` | `radial-gradient(circle at 76% 26%, rgba(148, 163, 184, 0.15), transparent 35%), radial-gradient…` | 13 | 7 |
| `--ogd-glass-toolbar-bg` | Liquid Glass surface | `linear-gradient(180deg, rgba(255,255,255,0.92), rgba(241,245,249,0.55))` | `radial-gradient(circle at 78% 24%, rgba(148, 163, 184, 0.16), transparent 35%), linear-gradient…` | 15 | 7 |
| `--ogd-glass-transition` | Liquid Glass surface | `—` | `—` | 4 | 1 |
| `--ogd-glass-transition-control` | Liquid Glass surface | `—` | `—` | 7 | 1 |
| `--ogd-graph-control-bg` | feature-specific | `—` | `radial-gradient(circle at 74% 35%, rgba(148, 163, 184, 0.14), transparent 34%), linear-gradient…` | 5 | 4 |
| `--ogd-graph-control-border` | feature-specific | `—` | `rgba(203, 213, 225, 0.14)` | 5 | 4 |
| `--ogd-graph-control-color` | feature-specific | `—` | `—` | 4 | 3 |
| `--ogd-graph-control-shadow` | feature-specific | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.10), 0 2px 7px rgba(0, 0, 0, 0.20)` | 5 | 4 |
| `--ogd-heading-border` | feature-specific | `—` | `rgba(203, 213, 225, 0.18)` | 7 | 3 |
| `--ogd-heading-border-soft` | feature-specific | `—` | `rgba(71, 85, 105, 0.62)` | 5 | 3 |
| `--ogd-heading-h1-bg` | feature-specific | `—` | `radial-gradient(circle at 78% 18%, rgba(125, 211, 252, 0.10), transparent 0 36%), linear-gradie…` | 5 | 3 |
| `--ogd-heading-h2-bg` | feature-specific | `—` | `linear-gradient(180deg, rgba(30, 41, 59, 0.60), rgba(15, 23, 42, 0.38))` | 4 | 3 |
| `--ogd-heading-rule` | feature-specific | `—` | `linear-gradient(90deg, rgba(103, 232, 249, 0.46), rgba(71, 85, 105, 0.62), transparent)` | 4 | 3 |
| `--ogd-heading-rule-soft` | feature-specific | `—` | `linear-gradient(90deg, rgba(203, 213, 225, 0.34), rgba(71, 85, 105, 0.16), transparent)` | 4 | 3 |
| `--ogd-heading-shadow` | feature-specific | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.12), inset 0 -1px 0 rgba(0, 0, 0, 0.24), 0 16px 34px rgba(0…` | 4 | 3 |
| `--ogd-hover-lift` | feature-specific | `translateY(-1px)` | `—` | 17 | 5 |
| `--ogd-hover-lift-strong` | feature-specific | `translateY(-2px)` | `—` | 5 | 4 |
| `--ogd-hover-lift-subtle` | feature-specific | `translateY(-0.5px)` | `—` | 6 | 5 |
| `--ogd-hover-shift` | feature-specific | `translateX(1px)` | `—` | 7 | 5 |
| `--ogd-html-table-axis-bg` | feature-specific | `—` | `linear-gradient(180deg, rgba(30, 41, 59, 0.76), rgba(15, 23, 42, 0.50))` | 6 | 4 |
| `--ogd-html-table-border` | feature-specific | `—` | `rgba(203, 213, 225, 0.26)` | 7 | 4 |
| `--ogd-html-table-caption-bg` | feature-specific | `—` | `radial-gradient(circle at 82% 18%, rgba(14, 165, 233, 0.18), transparent 0 36%), linear-gradien…` | 5 | 4 |
| `--ogd-html-table-cell-border` | feature-specific | `—` | `rgba(71, 85, 105, 0.68)` | 8 | 4 |
| `--ogd-html-table-head-bg` | feature-specific | `—` | `radial-gradient(circle at 42% 10%, rgba(255, 255, 255, 0.14), transparent 0 32%), linear-gradie…` | 6 | 4 |
| `--ogd-html-table-shadow` | feature-specific | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.11), inset 0 -1px 0 rgba(0, 0, 0, 0.22), 0 12px 30px rgba(0…` | 6 | 4 |
| `--ogd-html-table-surface` | feature-specific | `—` | `radial-gradient(circle at 78% 12%, rgba(255, 255, 255, 0.13), transparent 0 34%), linear-gradie…` | 6 | 4 |
| `--ogd-inline-code-bg` | feature-specific | `—` | `#2a2f37` | 3 | 2 |
| `--ogd-lg-border` | Liquid Glass surface | `—` | `rgba(203, 213, 225, 0.18)` | 14 | 3 |
| `--ogd-lg-border-hover` | Liquid Glass surface | `—` | `rgba(186, 230, 253, 0.30)` | 9 | 3 |
| `--ogd-lg-control-bg` | Liquid Glass surface | `—` | `radial-gradient(circle at 44% 12%, rgba(255, 255, 255, 0.12), transparent 0 28%), linear-gradie…` | 15 | 4 |
| `--ogd-lg-edge` | Liquid Glass surface | `—` | `rgba(255, 255, 255, 0.18)` | 29 | 3 |
| `--ogd-lg-edge-low` | Liquid Glass surface | `—` | `rgba(15, 23, 42, 0.64)` | 3 | 3 |
| `--ogd-lg-frost-halo` | Liquid Glass surface | `—` | `rgba(103, 232, 249, 0.10)` | 9 | 3 |
| `--ogd-lg-frost-outline` | Liquid Glass surface | `—` | `rgba(103, 232, 249, 0.18)` | 15 | 3 |
| `--ogd-lg-frost-rim` | Liquid Glass surface | `—` | `rgba(103, 232, 249, 0.42)` | 17 | 3 |
| `--ogd-lg-mist-fill` | Liquid Glass surface | `—` | `rgba(14, 116, 144, 0.20)` | 4 | 3 |
| `--ogd-lg-mist-glow` | Liquid Glass surface | `—` | `rgba(186, 230, 253, 0.10)` | 6 | 3 |
| `--ogd-lg-mist-line` | Liquid Glass surface | `—` | `rgba(125, 211, 252, 0.22)` | 6 | 3 |
| `--ogd-lg-mist-rim` | Liquid Glass surface | `—` | `—` | 5 | 1 |
| `--ogd-lg-mist-rim-dark` | Liquid Glass surface | `—` | `—` | 1 | 1 |
| `--ogd-lg-pane-header-shadow` | Liquid Glass surface | `—` | `inset 0 1px 0 var(--ogd-lg-edge), 0 7px 16px rgba(0, 0, 0, 0.24)` | 4 | 3 |
| `--ogd-lg-pane-shell-shadow` | Liquid Glass surface | `—` | `inset 0 1px 0 var(--ogd-lg-edge), 0 10px 26px rgba(0, 0, 0, 0.30)` | 4 | 3 |
| `--ogd-lg-refined-active-bg` | Liquid Glass surface | `—` | `radial-gradient(circle at 76% 18%, rgba(255, 255, 255, 0.16), transparent 0 36%), linear-gradie…` | 5 | 3 |
| `--ogd-lg-refined-border` | Liquid Glass surface | `—` | `rgba(203, 213, 225, 0.20)` | 8 | 3 |
| `--ogd-lg-refined-border-hover` | Liquid Glass surface | `—` | `rgba(186, 230, 253, 0.30)` | 4 | 3 |
| `--ogd-lg-refined-focus-shadow` | Liquid Glass surface | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.16), 0 16px 38px rgba(0, 0, 0, 0.40), 0 0 0 3px var(--ogd-l…` | 5 | 3 |
| `--ogd-lg-refined-hover-bg` | Liquid Glass surface | `—` | `radial-gradient(circle at 76% 18%, rgba(255, 255, 255, 0.17), transparent 0 36%), linear-gradie…` | 4 | 3 |
| `--ogd-lg-refined-rest-bg` | Liquid Glass surface | `—` | `radial-gradient(circle at 76% 18%, rgba(255, 255, 255, 0.13), transparent 0 36%), linear-gradie…` | 6 | 3 |
| `--ogd-lg-refined-shadow` | Liquid Glass surface | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.12), inset 0 -1px 0 rgba(0, 0, 0, 0.28), 0 10px 24px rgba(0…` | 6 | 3 |
| `--ogd-lg-refined-shadow-hover` | Liquid Glass surface | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.16), inset 0 -1px 0 rgba(0, 0, 0, 0.26), 0 18px 40px rgba(0…` | 6 | 3 |
| `--ogd-lg-row-active-bg` | Liquid Glass surface | `—` | `radial-gradient(circle at 42% 16%, rgba(255, 255, 255, 0.14), transparent 0 30%), linear-gradie…` | 4 | 3 |
| `--ogd-lg-row-active-shadow` | Liquid Glass surface | `—` | `0 20px 48px rgba(0, 0, 0, 0.44), 0 7px 20px rgba(0, 0, 0, 0.30), 0 0 0 1px rgba(125, 211, 252, …` | 4 | 3 |
| `--ogd-lg-shadow` | Liquid Glass surface | `—` | `0 18px 46px rgba(0, 0, 0, 0.46), 0 6px 18px rgba(0, 0, 0, 0.32), inset 0 1px 0 var(--ogd-lg-edg…` | 6 | 4 |
| `--ogd-lg-shadow-active` | Liquid Glass surface | `—` | `0 22px 54px rgba(0, 0, 0, 0.54), 0 0 0 3px var(--ogd-lg-mist-glow), inset 0 0 0 1px var(--ogd-l…` | 6 | 4 |
| `--ogd-lg-shadow-focus` | Liquid Glass surface | `—` | `0 18px 46px rgba(0, 0, 0, 0.46), 0 0 0 3px var(--ogd-lg-frost-halo), inset 0 1px 0 var(--ogd-lg…` | 16 | 4 |
| `--ogd-lg-shadow-hover` | Liquid Glass surface | `—` | `0 30px 72px rgba(0, 0, 0, 0.56), 0 12px 28px rgba(0, 0, 0, 0.38), inset 0 1px 0 var(--ogd-lg-ed…` | 7 | 4 |
| `--ogd-lg-surface-bg` | Liquid Glass surface | `—` | `radial-gradient(circle at 44% 12%, rgba(255, 255, 255, 0.14), transparent 0 28%), linear-gradie…` | 9 | 4 |
| `--ogd-lg-surface-bg-active` | Liquid Glass surface | `—` | `radial-gradient(circle at 44% 12%, rgba(255, 255, 255, 0.14), transparent 0 28%), linear-gradie…` | 9 | 4 |
| `--ogd-lg-surface-bg-hover` | Liquid Glass surface | `—` | `radial-gradient(circle at 44% 12%, rgba(255, 255, 255, 0.16), transparent 0 28%), linear-gradie…` | 13 | 4 |
| `--ogd-lg-tab-border` | Liquid Glass surface | `—` | `—` | 3 | 1 |
| `--ogd-lg-tab-border-hover` | Liquid Glass surface | `—` | `rgba(203, 213, 225, 0.18)` | 5 | 3 |
| `--ogd-lg-tab-focus-outline` | Liquid Glass surface | `—` | `var(--ogd-surface-transparent, transparent)` | 3 | 3 |
| `--ogd-lg-tab-shadow` | Liquid Glass surface | `—` | `0 16px 38px rgba(0, 0, 0, 0.42), 0 5px 14px rgba(0, 0, 0, 0.28), inset 0 1px 0 var(--ogd-lg-edg…` | 5 | 3 |
| `--ogd-lg-tab-shadow-hover` | Liquid Glass surface | `—` | `0 24px 54px rgba(0, 0, 0, 0.50), 0 8px 18px rgba(0, 0, 0, 0.32), inset 0 1px 0 var(--ogd-lg-edg…` | 5 | 3 |
| `--ogd-line-contrast` | line/border | `#374151` | `—` | 6 | 1 |
| `--ogd-line-dark` | line/border | `#334155` | `—` | 11 | 1 |
| `--ogd-line-faint` | line/border | `#94a3b8` | `—` | 2 | 1 |
| `--ogd-line-height` | line/border | `1.5` | `—` | 5 | 4 |
| `--ogd-line-ink` | line/border | `#111827` | `—` | 4 | 1 |
| `--ogd-line-muted` | line/border | `#475569` | `—` | 4 | 1 |
| `--ogd-line-soft` | line/border | `#e5e7eb` | `—` | 54 | 1 |
| `--ogd-line-strong` | line/border | `#cbd5e1` | `—` | 77 | 1 |
| `--ogd-list-marker-bg` | feature-specific | `—` | `radial-gradient(circle at 34% 26%, rgba(255, 255, 255, 0.28), rgba(255, 255, 255, 0.08) 44%, rg…` | 10 | 5 |
| `--ogd-list-marker-bg-active` | feature-specific | `—` | `radial-gradient(circle at 34% 26%, rgba(255, 255, 255, 0.32), rgba(255, 255, 255, 0.10) 44%, rg…` | 4 | 3 |
| `--ogd-list-marker-border` | feature-specific | `—` | `rgba(186, 230, 253, 0.32)` | 9 | 5 |
| `--ogd-list-marker-shadow` | feature-specific | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.12), inset 0 -1px 0 rgba(0, 0, 0, 0.30), 0 7px 16px rgba(0,…` | 10 | 5 |
| `--ogd-list-marker-shadow-active` | feature-specific | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.16), inset 0 -1px 0 rgba(0, 0, 0, 0.26), 0 12px 26px rgba(0…` | 4 | 3 |
| `--ogd-list-nested-marker` | feature-specific | `—` | `rgba(186, 230, 253, 0.28)` | 7 | 5 |
| `--ogd-list-task-border` | feature-specific | `—` | `rgba(203, 213, 225, 0.20)` | 4 | 3 |
| `--ogd-list-task-shadow` | feature-specific | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.12), 0 10px 24px rgba(0, 0, 0, 0.30)` | 4 | 3 |
| `--ogd-list-task-surface` | feature-specific | `—` | `radial-gradient(circle at 76% 18%, rgba(255, 255, 255, 0.13), transparent 0 36%), linear-gradie…` | 4 | 3 |
| `--ogd-lp-cell-focus-bg` | feature-specific | `—` | `linear-gradient(180deg, rgba(14, 116, 144, 0.20), rgba(15, 23, 42, 0.14))` | 3 | 2 |
| `--ogd-lp-code-bg` | feature-specific | `—` | `rgba(248, 250, 252, 0.84)` | 6 | 4 |
| `--ogd-lp-code-border` | feature-specific | `—` | `rgba(203, 213, 225, 0.68)` | 8 | 4 |
| `--ogd-lp-doc-glass-bg` | feature-specific | `—` | `radial-gradient(circle at 74% 14%, rgba(255, 255, 255, 0.10), transparent 0 34%), linear-gradie…` | 6 | 2 |
| `--ogd-lp-doc-glass-shadow` | feature-specific | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.10), inset 0 -1px 0 rgba(0, 0, 0, 0.24), 0 10px 24px rgba(0…` | 5 | 2 |
| `--ogd-lp-doc-rim` | feature-specific | `—` | `rgba(51, 65, 85, 0.92)` | 5 | 2 |
| `--ogd-lp-doc-rim-soft` | feature-specific | `—` | `rgba(51, 65, 85, 0.78)` | 3 | 2 |
| `--ogd-lp-focus-bg` | feature-specific | `—` | `linear-gradient(180deg, rgba(51, 65, 85, 0.34), rgba(14, 116, 144, 0.16))` | 2 | 2 |
| `--ogd-lp-focus-outline` | feature-specific | `—` | `rgba(103, 232, 249, 0.28)` | 2 | 2 |
| `--ogd-lp-focus-rim` | feature-specific | `—` | `rgba(103, 232, 249, 0.42)` | 3 | 2 |
| `--ogd-lp-focus-shadow` | feature-specific | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.10), 0 0 0 1px rgba(103, 232, 249, 0.08), 0 8px 18px rgba(0…` | 3 | 2 |
| `--ogd-macos-toggle-bg` | feature-specific | `—` | `linear-gradient(180deg, rgba(51, 65, 85, 0.78), rgba(15, 23, 42, 0.55))` | 4 | 3 |
| `--ogd-macos-toggle-border` | feature-specific | `—` | `1px solid rgba(203, 213, 225, 0.22)` | 4 | 3 |
| `--ogd-macos-toggle-color` | feature-specific | `—` | `var(--ogd-text-inverted, #f8fafc)` | 4 | 3 |
| `--ogd-macos-toggle-shadow` | feature-specific | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.12), inset 0 -1px 0 rgba(0, 0, 0, 0.28), 0 6px 16px rgba(0,…` | 4 | 3 |
| `--ogd-max-width` | feature-specific | `420mm` | `—` | 3 | 1 |
| `--ogd-overlay-selected-bg` | feature-specific | `—` | `rgba(51, 65, 85, 0.78)` | 3 | 2 |
| `--ogd-overlay-selected-line` | feature-specific | `—` | `var(--ogd-line-strong, #cbd5e1)` | 3 | 2 |
| `--ogd-overlay-selected-text` | feature-specific | `—` | `var(--ogd-surface-muted, #f8fafc)` | 3 | 2 |
| `--ogd-pdf-footer-font-size` | PDF header/footer marginalia | `8pt` | `—` | 3 | 2 |
| `--ogd-pdf-footer-max-width` | PDF header/footer marginalia | `90%` | `—` | 2 | 1 |
| `--ogd-pdf-footer-offset` | PDF header/footer marginalia | `-22mm` | `—` | 3 | 2 |
| `--ogd-pdf-footer-pad-x` | PDF header/footer marginalia | `14px` | `—` | 3 | 2 |
| `--ogd-pdf-footer-pad-y` | PDF header/footer marginalia | `5px` | `—` | 3 | 2 |
| `--ogd-pdf-footer-reserve` | PDF header/footer marginalia | `28mm` | `—` | 3 | 2 |
| `--ogd-pdf-footer-text` | PDF header/footer marginalia | `""` | `—` | 5 | 4 |
| `--ogd-pdf-header-font-size` | PDF header/footer marginalia | `7.5pt` | `—` | 3 | 2 |
| `--ogd-pdf-header-left` | PDF header/footer marginalia | `auto` | `—` | 3 | 2 |
| `--ogd-pdf-header-pad-x` | PDF header/footer marginalia | `10px` | `—` | 3 | 2 |
| `--ogd-pdf-header-pad-y` | PDF header/footer marginalia | `4px` | `—` | 3 | 2 |
| `--ogd-pdf-header-right` | PDF header/footer marginalia | `13mm` | `—` | 3 | 2 |
| `--ogd-pdf-header-text` | PDF header/footer marginalia | `""` | `—` | 5 | 4 |
| `--ogd-pdf-header-top` | PDF header/footer marginalia | `11mm` | `—` | 2 | 1 |
| `--ogd-pdf-header-transform` | PDF header/footer marginalia | `none` | `—` | 3 | 2 |
| `--ogd-pdf-label-letter-spacing` | PDF header/footer marginalia | `1.2px` | `—` | 4 | 2 |
| `--ogd-pdf-label-line-height` | PDF header/footer marginalia | `1.2` | `—` | 3 | 1 |
| `--ogd-pdf-label-radius` | PDF header/footer marginalia | `4px` | `—` | 3 | 1 |
| `--ogd-pdf-marginalia-accent` | PDF header/footer marginalia | `#279DF5` | `#38bdf8` | 6 | 2 |
| `--ogd-pdf-marginalia-bg` | PDF header/footer marginalia | `rgba(39, 157, 245, 0.06)` | `rgba(56, 189, 248, 0.16)` | 7 | 5 |
| `--ogd-pdf-marginalia-border` | PDF header/footer marginalia | `rgba(39, 157, 245, 0.22)` | `rgba(56, 189, 248, 0.38)` | 7 | 5 |
| `--ogd-pdf-marginalia-shadow` | PDF header/footer marginalia | `none` | `none` | 4 | 2 |
| `--ogd-plugin-dark-card-bg` | feature-specific | `—` | `radial-gradient(circle at 78% 18%, rgba(148, 163, 184, 0.12), transparent 34%), linear-gradient…` | 3 | 1 |
| `--ogd-plugin-dark-card-hover-shadow` | feature-specific | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.10), 0 8px 18px rgba(0, 0, 0, 0.34), 0 0 0 2px rgba(147, 19…` | 3 | 1 |
| `--ogd-plugin-dark-card-shadow` | feature-specific | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.08), 0 4px 12px rgba(0, 0, 0, 0.26)` | 3 | 1 |
| `--ogd-plugin-dark-surface-bg` | feature-specific | `—` | `radial-gradient(circle at 78% 18%, rgba(148, 163, 184, 0.11), transparent 34%), linear-gradient…` | 3 | 1 |
| `--ogd-plugin-dark-surface-border` | feature-specific | `—` | `rgba(203, 213, 225, 0.14)` | 3 | 1 |
| `--ogd-plugin-dark-surface-shadow` | feature-specific | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.08), 0 5px 14px rgba(0, 0, 0, 0.24)` | 3 | 1 |
| `--ogd-press-lift` | feature-specific | `translateY(0) scale(0.99)` | `—` | 7 | 5 |
| `--ogd-print-caption-text` | feature-specific | `—` | `#475569` | 2 | 1 |
| `--ogd-print-table-bg` | feature-specific | `—` | `rgba(255, 255, 255, 0.72)` | 5 | 1 |
| `--ogd-print-table-border` | feature-specific | `—` | `rgba(203, 213, 225, 0.40)` | 6 | 1 |
| `--ogd-print-table-cell-bg` | feature-specific | `—` | `rgba(255, 255, 255, 0.38)` | 3 | 1 |
| `--ogd-print-table-first-col-bg` | feature-specific | `—` | `rgba(248, 250, 252, 0.34)` | 3 | 1 |
| `--ogd-print-table-head-bg` | feature-specific | `—` | `rgba(248, 250, 252, 0.54)` | 4 | 1 |
| `--ogd-print-table-strong-border` | feature-specific | `—` | `rgba(148, 163, 184, 0.46)` | 2 | 1 |
| `--ogd-print-table-strong-text` | feature-specific | `—` | `#1f2937` | 3 | 1 |
| `--ogd-print-table-text` | feature-specific | `—` | `#334155` | 2 | 1 |
| `--ogd-print-table-zebra-bg` | feature-specific | `—` | `rgba(236, 254, 255, 0.16)` | 4 | 1 |
| `--ogd-radius-control` | radius | `7px` | `—` | 47 | 1 |
| `--ogd-radius-panel` | radius | `—` | `—` | 1 | 0 |
| `--ogd-radius-pill` | radius | `999px` | `—` | 49 | 1 |
| `--ogd-radius-pill-left` | radius | `var(--ogd-radius-pill, 999px) 0 0 var(--ogd-radius-pill, 999px)` | `—` | 2 | 1 |
| `--ogd-radius-top` | radius | `var(--radius-m, 6px) var(--radius-m, 6px) 0 0` | `—` | 4 | 1 |
| `--ogd-ribbon-icon-bg` | feature-specific | `—` | `radial-gradient(circle at 74% 24%, rgba(148, 163, 184, 0.16), transparent 36%), linear-gradient…` | 10 | 9 |
| `--ogd-ribbon-icon-border` | feature-specific | `—` | `rgba(203, 213, 225, 0.16)` | 10 | 9 |
| `--ogd-ribbon-icon-color` | feature-specific | `—` | `var(--ogd-line-strong, #cbd5e1)` | 7 | 6 |
| `--ogd-ribbon-icon-shadow` | feature-specific | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.11), inset 0 -1px 0 rgba(0, 0, 0, 0.28), inset 0 0 12px rgb…` | 10 | 9 |
| `--ogd-search-hl-bg` | feature-specific | `—` | `rgba(251, 191, 36, 0.22)` | 3 | 2 |
| `--ogd-search-hl-fg` | feature-specific | `—` | `#fde68a` | 3 | 2 |
| `--ogd-search-input-bg` | feature-specific | `—` | `linear-gradient(180deg, rgba(51, 65, 85, 0.82), rgba(15, 23, 42, 0.58))` | 7 | 5 |
| `--ogd-search-input-border` | feature-specific | `—` | `rgba(203, 213, 225, 0.18)` | 5 | 3 |
| `--ogd-search-input-control-bg` | feature-specific | `—` | `linear-gradient(180deg, rgba(51, 65, 85, 0.66), rgba(15, 23, 42, 0.46))` | 6 | 5 |
| `--ogd-search-input-control-border` | feature-specific | `—` | `rgba(203, 213, 225, 0.14)` | 4 | 3 |
| `--ogd-search-input-control-shadow` | feature-specific | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.08), 0 4px 12px -10px rgba(0, 0, 0, 0.42)` | 6 | 5 |
| `--ogd-search-input-shadow` | feature-specific | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.10), inset 0 -1px 0 rgba(255, 255, 255, 0.04), 0 10px 24px …` | 7 | 5 |
| `--ogd-shadow-none` | shadow | `none` | `—` | 46 | 1 |
| `--ogd-surface-base` | feature-specific | `#ffffff` | `—` | 34 | 1 |
| `--ogd-surface-dark` | feature-specific | `#111827` | `—` | 9 | 1 |
| `--ogd-surface-dark-muted` | feature-specific | `#374151` | `—` | 5 | 1 |
| `--ogd-surface-dark-subtle` | feature-specific | `#334155` | `—` | 5 | 1 |
| `--ogd-surface-muted` | feature-specific | `#f8fafc` | `—` | 24 | 1 |
| `--ogd-surface-subtle` | feature-specific | `#f3f4f6` | `—` | 33 | 1 |
| `--ogd-surface-transparent` | feature-specific | `transparent` | `—` | 117 | 1 |
| `--ogd-tab-glass-bg` | feature-specific | `—` | `linear-gradient(180deg, rgba(71, 85, 105, 0.84), rgba(15, 23, 42, 0.60))` | 9 | 8 |
| `--ogd-tab-glass-bg-hover` | feature-specific | `—` | `rgba(51, 65, 85, 0.34)` | 9 | 8 |
| `--ogd-tab-glass-border` | feature-specific | `—` | `var(--ogd-surface-transparent, transparent)` | 6 | 5 |
| `--ogd-tab-glass-border-bottom` | feature-specific | `—` | `var(--ogd-surface-transparent, transparent)` | 9 | 8 |
| `--ogd-tab-glass-border-hover` | feature-specific | `—` | `var(--ogd-surface-transparent, transparent)` | 6 | 5 |
| `--ogd-tab-glass-shadow` | feature-specific | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.13), inset 0 -1px 0 rgba(255, 255, 255, 0.05), 0 10px 24px …` | 10 | 8 |
| `--ogd-tab-glass-shadow-hover` | feature-specific | `—` | `none` | 9 | 8 |
| `--ogd-tab-header-bg` | feature-specific | `—` | `—` | 4 | 3 |
| `--ogd-tab-header-border-bottom` | feature-specific | `—` | `—` | 3 | 2 |
| `--ogd-tab-header-border-color` | feature-specific | `—` | `—` | 4 | 3 |
| `--ogd-tab-header-shadow` | feature-specific | `—` | `—` | 4 | 3 |
| `--ogd-table-bg` | table surface | `—` | `var(--ogd-print-table-bg)` | 4 | 3 |
| `--ogd-table-border` | table surface | `—` | `var(--ogd-print-table-border)` | 29 | 18 |
| `--ogd-table-cell-border` | table surface | `—` | `var(--ogd-print-table-border)` | 40 | 18 |
| `--ogd-table-font-size` | table surface | `—` | `—` | 13 | 10 |
| `--ogd-table-head-bg` | table surface | `—` | `var(--ogd-print-table-head-bg)` | 34 | 20 |
| `--ogd-table-line-height` | table surface | `—` | `—` | 14 | 10 |
| `--ogd-table-pad-x` | table surface | `—` | `—` | 13 | 10 |
| `--ogd-table-pad-y` | table surface | `—` | `—` | 13 | 10 |
| `--ogd-table-row-even` | table surface | `—` | `var(--ogd-print-table-zebra-bg)` | 23 | 17 |
| `--ogd-table-row-hover` | table surface | `—` | `rgba(8, 145, 178, 0.22)` | 23 | 16 |
| `--ogd-table-shadow` | table surface | `—` | `none` | 23 | 15 |
| `--ogd-table-surface` | table surface | `—` | `var(--ogd-print-table-bg)` | 26 | 17 |
| `--ogd-table-tint` | table surface | `—` | `rgba(14, 165, 233, 0.10)` | 8 | 4 |
| `--ogd-text-body` | text color | `#1a1a1a` | `—` | 1 | 1 |
| `--ogd-text-inverted` | text color | `#f8fafc` | `—` | 54 | 1 |
| `--ogd-text-muted` | text color | `#64748b` | `—` | 3 | 1 |
| `--ogd-text-secondary` | text color | `#374151` | `—` | 20 | 1 |
| `--ogd-text-slate` | text color | `#334155` | `—` | 70 | 1 |
| `--ogd-text-soft` | text color | `#94a3b8` | `—` | 31 | 1 |
| `--ogd-text-strong` | text color | `#111827` | `—` | 72 | 1 |
| `--ogd-text-subtle` | text color | `#475569` | `—` | 40 | 1 |
| `--ogd-title-rule-end` | feature-specific | `#0284c7` | `—` | 1 | 1 |
| `--ogd-title-rule-start` | feature-specific | `#0f766e` | `—` | 2 | 1 |
| `--ogd-topbar-icon-hover-bg` | feature-specific | `—` | `radial-gradient(circle at 76% 18%, rgba(255, 255, 255, 0.14), transparent 0 34%), linear-gradie…` | 5 | 3 |
| `--ogd-topbar-icon-hover-shadow` | feature-specific | `—` | `inset 0 1px 0 rgba(255, 255, 255, 0.12), 0 10px 20px rgba(0, 0, 0, 0.26)` | 5 | 3 |
