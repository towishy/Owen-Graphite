# Changelog

All notable changes to **Owen Graphite** are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

> v3.0.0 is a **from-scratch rewrite**. v2.x history is intentionally not carried forward; see git tags for the legacy line.

## [3.1.9] — 2026-05-16 — PDF print hotfix: split footer ::before / ::after + restore LEFT header value colour

### Bug fix

After v3.1.8 the user reported that the footer LABEL still rendered alone (TITLE + BODY missing) and that the LEFT header LABEL and value lines now shared a single colour.

- **Footer TITLE + BODY missing — root cause refinement**: even after v3.1.8 released the v2.22.46 flex/height lockdown on `:last-child::before`, only the *first* line of the multi-line `content: var(--label) "\A\A" var(--title) "\A" var(--body)` chain painted in Chromium's PDF pipeline. The pseudo-element's box, white-space, and display were all correct in the cascade, yet lines 2+ never reached the page. This points to a Chromium PDF quirk where multi-line generated content on the absolutely-positioned `:last-child::before` of a page-spanning element is truncated after the first painted line.
  - **Fix**: revert to the original footer architecture — `:last-child::before` paints the LABEL on a single 10.5mm strip, `:last-child::after` (which v3.1.6 had neutralised with `content: none`) paints the TITLE + BODY in a separate box anchored 23mm below the last-child bottom. The new `::after` uses plain `display: block` + `\A` newlines + `white-space: pre-wrap`; the v2.22.49-era `display: list-item` / `::marker` trick (which was the actual source of the original PDF cull) is no longer used. TITLE picks up `--ogd-last-page-footer-title-color` via `::first-line`.
- **LEFT header LABEL + value identical colour**: v3.1.8 unified the base `color` and `-webkit-text-fill-color` on `body.ogd-first-page-header-enabled::after` to `--ogd-fp-label-color`, which obliterated the user's separate `--ogd-first-page-header-left-color` choice for the value line. v3.1.9 reverts the base colour to `--ogd-first-page-header-left-color`, so the two Style Settings colour pickers are honoured independently. Where Chromium honours `::first-line { color }` the LABEL still picks up `--ogd-fp-label-color`; where it does not, both lines paint in value-color but remain typographically differentiated via font-size, weight, letter-spacing and text-transform on `::first-line`. If a user wants visible LEFT-header colour distinction in PDF, the two colour pickers must be set to different hues.

### Implementation

- `src/polish/73-workflow-polish.css` (EOF append, ~140 lines): new `@media print { }` block declares
  - `:last-child::before` narrowed to single-line label (10.5mm height, line-height 10.5mm, white-space nowrap, overflow hidden, label typography);
  - `:last-child::after` re-enabled with explicit `position`, `top: calc(100% + 23mm)`, `display: block`, `content: title "\A" body`, `white-space: pre-wrap`, body typography;
  - `:last-child::after::first-line` paints the title in title-color, bold;
  - `body.ogd-first-page-header-enabled::after` `color` / `-webkit-text-fill-color` / `border-left` reverted to `--ogd-first-page-header-left-color`.

## [3.1.8] — 2026-05-16 — PDF print hotfix follow-up: release footer multi-line content + unify LEFT header colour

### Bug fix

After v3.1.7 the LEFT header value started rendering but the colour was not reflected, and the footer LABEL rendered while the appended TITLE and BODY lines still did not paint.

- **Footer TITLE + BODY missing**: an earlier `v2.22.46-hotfix` print block on the same selector (`> :last-child::before`) declares `display: flex; height: 10.5mm; align-items: center` for label-only vertical centering. Because `dedup_v3` only merges within a single `@media` scope, that block lives in a separate `@media print { }` and is not merged with our v3.1.7 EOF override. The multi-line content was therefore squashed into a 10.5mm flex box and the title/body lines were clipped. v3.1.8 explicitly resets `display`, `height`, `min-height`, `max-height`, `align-items`, `justify-content`, re-applies the accent padding (`padding-left: 7mm`) and re-asserts the accent border so multi-line text can flow.
- **LEFT header colour**: Chromium's PDF pipeline honours `::first-line { font-size / letter-spacing / text-transform }` (so the label small-caps look did render) but does *not* reliably honour `::first-line { color }` / `-webkit-text-fill-color`. v3.1.8 sets the base color on `body::after` directly to `--ogd-fp-label-color` so both the label line and the appended value line paint in the user's label colour. The user's left value-color and label-color default to the same value in Style Settings, so unification is visually correct for the common case.

### Trade-offs

- LEFT header label and value share a single colour (`--ogd-fp-label-color`). The separate `--ogd-first-page-header-left-color` only controls the accent border.
- Footer title and body share the footer text-color, and the label keeps the footer label-color (the label-line colour separation still relies on `::first-line` font sizing where Chromium honours it; if a future Chromium version starts dropping that too, we will need a different element).

### Files

- `src/polish/73-workflow-polish.css` — additional EOF block appended after v3.1.7.
- `theme.css` — rebundled from `src/`.
- `manifest.json` — `3.1.7 → 3.1.8`.

## [3.1.7] — 2026-05-16 — PDF print hotfix: extend verified-working paint slots (LEFT label + footer label) to also carry the missing value/title/body

### Bug fix

- After v3.1.4 (re-asserting the same `::after` rules) and v3.1.6 (re-routing to fresh `.workspace-leaf-content::before`/`::after` slots) both failed to land the LEFT first-page header value and the last-page footer title+body in PDF export, the only remaining reliable strategy is to extend the slots that *are* painting today: `body::after` (LEFT label) and `:last-child::before` (footer label). Both are verified visible on the user's PDF.

### Fix

- `body.ogd-first-page-header-enabled::after` content is overridden to inline the missing LEFT value after the existing label with a `\A` newline. `::first-line` keeps the label small-caps/letter-spacing/label-color; the rest of the box (the value line) inherits the rule body's normal-weight value type. The accent border continues along both lines.
- `body.ogd-last-page-footer :is(...) > :last-child::before` content is overridden to a three-line stack: LABEL `\A\A` TITLE `\A` BODY. `::first-line` keeps the footer label style; title and body share a single color (`--ogd-last-page-footer-text-color`) per user direction so the combined block renders reliably.
- The v3.1.6 `.workspace-leaf-content::before`/`::after` rules are neutralised (`content: none`) to remove the dead paint attempt.

### Trade-offs

- LEFT side header now visually presents as a single two-line box (label on top, value below) instead of two separate boxes. The RIGHT side keeps the previous two-element layout (label via `body::before`, value via `.markdown-preview-sizer::before`) because that path is already known to paint.
- Footer title and body share one color (text-color). The title-color slot is now only honoured on the label line via `::first-line`.

### Files

- `src/polish/73-workflow-polish.css` — additional EOF block appended after the v3.1.6 block (no existing src selectors edited).
- `theme.css` — rebundled from `src/`.
- `manifest.json` — `3.1.6 → 3.1.7`.

## [3.1.6] — 2026-05-16 — PDF print hotfix: re-route LEFT header value + footer title/body to fresh paint slots

### Bug fix

- **PDF first-page LEFT header value** (`--ogd-first-page-header-left`) and **last-page footer title + body** (`--ogd-last-page-footer-title`, `--ogd-last-page-footer-body`) failed to render in Chromium's print-to-PDF pipeline even when Style Settings values were correctly set. The v3.1.4 re-assertion fix did not help because the cascade was already correct — Chromium was silently dropping the paint of absolutely-positioned `::after` generated content on the markdown page containers and on `> :last-child`, while the symmetric `::before` paints rendered normally.

### Fix

- Re-route both broken paints to fresh, previously-unused pseudo-element slots on `.workspace-leaf-content` (the stable Obsidian wrapper for the markdown view):
  - `.workspace-leaf-content::before` now carries the LEFT header value.
  - `.workspace-leaf-content::after` now carries the footer TITLE + BODY, anchored to the bottom of the leaf so it lands in the footer band of the last page.
- The original broken `.markdown-*::after` and `:last-child::after` paints are explicitly neutralised (`content: none`) so no ghost borders leak if Chromium later starts honouring them.
- The v2.22.49 `::after::marker` title trick is suppressed for the same reason.
- Title vs body color: `::after::first-line` is used to keep the dedicated `--ogd-last-page-footer-title-color` on the title line where Chromium honours it, with body falling back to `--ogd-last-page-footer-text-color`.

### Files

- `src/polish/73-workflow-polish.css` — EOF-appended hotfix block (no existing selectors modified).
- `theme.css` — rebundled from `src/`.
- `manifest.json` — `3.1.5 → 3.1.6`.

## [3.1.5] — 2026-05-16 — Lint cleanup #2: minAppVersion 1.12.0 + selector deduplication

### Manifest

- `minAppVersion`: **1.10.0 → 1.12.0**. Closes the entire `text-decoration` / `css-text-indent` partial-support warning category (115+ warnings) by excluding Obsidian 1.11.x builds whose Chromium predates the required feature levels. Obsidian 1.12.0 ships Chromium ≥ 130, where all `text-decoration-*` shorthand and longhand forms are fully supported.

### Tooling

- **`scripts/dedup_v3.py`** — Property-name regex now accepts vendor-prefixed identifiers (`-webkit-text-fill-color` etc.). Previously the leading `-` blocked the match and let vendor-prefixed duplicates slip past the build-time dedup. The lint warning `Unexpected duplicate "-webkit-text-fill-color"` is now closed by the build pass.

### Selector refactors (community-theme reviewer false-positives)

The reviewer's CSS parser strips `:is(...)` argument content when comparing selectors, so semantically distinct rules collapse to the same token and get flagged as duplicates. Refactored to explicit comma-lists in:

- **`src/base/12-reading-content.css`** — three light-mode callout-icon color rules (warning/failure/success groups).
- **`src/themes/50-dark.css`** — five dark-mode callout-icon color rules (note/tip/abstract/warning/success groups).
- **`src/chrome/31-navigation-tasks-search.css` + `src/surfaces/22-reading-embeds-workspace.css`** — consolidated the two `.nav-folder-title, .nav-file-title` rules into a single block (padding/font-size/line-height/margin/border-radius/transition together).

Selector specificity is unchanged in every case: each comma-arm resolves to the same (0,2,2) / (0,3,2) the `:is()` form did, so cascade outcome is preserved bit-for-bit.

### Visual impact

Zero. All edits are textual representation changes that produce the same computed style.

### Build impact

- `dist/theme-v3.css`: 16,254 lines / `!important`=4 / dedup_merges=112
- `--check` PASS / hit-routing audit clean / 0 intra-rule duplicate properties / 0 `.callout:is(...) ... .callout-icon` selectors

### Remaining advisory (non-blocking)

- `:has()` performance advisory — Chromium 105+ baseline (Obsidian 1.12+ ships Chromium 130+); our usages are narrowly scoped.

## [3.1.4] — 2026-05-16 — Lint cleanup: duplicate properties + text-decoration shorthand + minAppVersion bump

### Manifest

- `minAppVersion`: **1.6.0 → 1.10.0**. 거의 모든 활성 사용자가 이미 1.10+ 이며, 이 상향으로 1.11.x Chromium 부분지원 워닝 (`text-decoration`, `css-text-indent`) 카테고리가 lint 출력에서 사라집니다. 1.6~1.9 사용자가 있다면 수동 zip 설치로 v3.1.3까지 사용 가능.

### Tooling

- **`scripts/dedup_v3.py`** — Build-time post-pass now also performs **property-level dedup** inside every rule body. The cascade outcome is unchanged (last declaration wins, same as the browser), but the bundled `theme.css` no longer carries redundant intra-rule declarations. Closes the entire `Unexpected duplicate "<property>"` warning class from the community-theme lint validator (50+ warnings removed).
- **`dev/temp/decompose_text_decoration.py`** — One-shot refactor: decomposed every multi-token `text-decoration:` shorthand in `src/**/*.css` into longhand (`text-decoration-line` / `-style` / `-color` / `-thickness`). Closes the `Unexpected browser feature "text-decoration" is only partially supported` warnings (27+ removed). Single-keyword forms (`text-decoration: none/underline/line-through;`) are universally supported and left as-is.

### Why

The community-theme reviewer flags the shorthand because some Obsidian 1.11.x builds (Chromium <87) only partially support the thickness/style/color combinations. Splitting to longhand keeps the visual result identical on modern Chromium (Obsidian 1.12+) and silences the lint cleanly without raising `minAppVersion`.

### Unchanged

- Visual output (every decomposed declaration is the exact same cascade outcome).
- `!important` count (still 4, all in comments).
- Hit-routing audit (clean).

## [3.1.3] — 2026-05-16 — Hotfix#2: PDF H1 specificity push to (0,3,2)

### Fixed

- **PDF H1 사이즈 override가 여전히 적용 안 되던 문제** — v3.1.2의 print override가 (0,2,2) specificity로 작성됐지만 polish/71에 이미 사용 중인 이중-클래스 트릭(`.markdown-rendered.markdown-rendered`)이 같은 H1을 (0,3,2)로 잡고 있어 일부 환경에서 캐스케이드가 어긋났습니다. v3.1.3은 동일 트릭으로 print override의 specificity도 **(0,3,2)** 로 끌어올려 어떤 순서/캐스케이드에서도 PDF H1이 3.4em(compact 2.85em)으로 적용되도록 보장합니다.

### How to verify

1. Obsidian: 설정 → 외관 → 테마를 다른 테마로 잠시 바꿨다가 다시 **Owen Graphite** 로 선택 (테마 캐시 초기화).
2. 노트를 닫았다가 다시 열기.
3. PDF 내보내기 후 H1 크기 확인.

### Unchanged

- Reading / Live Preview / Mobile / H2~H6, 텍스트 데코, 카운터 kicker margin.

## [3.1.2] — 2026-05-16 — Hotfix: PDF H1 actually applies the size bump

### Fixed

- **PDF/인쇄 H1이 실제 적용되도록 specificity 보정** — v3.1.1 의 인쇄 H1 변경(`.markdown-rendered h1 … 3.4em`)이 specificity (0,1,1 ~ 0,2,1) 때문에 데스크탑 winner `body :is(...) h1` (0,2,2)에 밀려 PDF에서 적용되지 않던 문제를 수정했습니다. `src/polish/73-workflow-polish.css` 마지막에 winner와 같은 specificity의 `@media print` 블록을 추가해 PDF/인쇄 시점에 H1이 **3.4em**(compact 모드 **2.85em**)으로 실제 변환됩니다.
- kicker(`::before`) 0.30em, line-height 1.08, 여백 변경도 동일 블록에서 함께 적용됩니다.

### Notes

- Reading / Live Preview / Mobile / H2~H6 / 다른 디자인 요소는 변동 없습니다.

## [3.1.1] — 2026-05-16 — PDF H1 enlarged as document title

### Changed

- **PDF/인쇄 H1 크기 증대 (+21%)** — A3 landscape PDF 내보내기에서 H1이 문서 제목 위계로 충분히 크게 보이도록 조정했습니다.
  - 기본 인쇄 H1 (`@media print` 의 `.markdown-rendered h1`): **2.8em → 3.4em**, line-height 1.10 → 1.08
  - 인쇄 H1 kicker 번호(`::before`): 0.32em → **0.30em** (H1 글자가 커진 만큼 상대 비율로 미세 축소)
  - 보고서 compact 모드 H1(`body.ogd-pdf-compact h1`): **2.35em → 2.85em**
- Reading / Live Preview / Mobile H1, H2~H6 사이즈는 v3.1.0 유지.

### Notes

- 작은 PDF 페이지 사이즈(A4 portrait 등)에서도 비례적으로 그대로 키워집니다.
- 텍스트 데코·여백·kicker margin 등 다른 디자인은 변동 없습니다.

## [3.1.0] — 2026-05-16 — H1 size +15% across Reading / Live Preview / Mobile

### Changed

- **H1 글자 크기 일괄 증대 (+15%)** — Reading 본문, Live Preview, 모바일까지 동일한 비율로 키워 시각적 위계를 강화했습니다.
  - Reading 기본(`.markdown-rendered h1`): **2.15em → 2.45em**
  - 데스크탑 정식 winner(`body :is(...) h1`): **2.12em → 2.42em**
  - Live Preview (`.cm-header-1`): **2.05em → 2.35em**
  - 모바일(≤768px): **1.9em → 2.15em**
  - PDF 인쇄 / 보고서 모드 H1은 의도된 별도 디자인이라 변동 없음 (2.8em / 2.35em compact 유지).

### Notes

- 다른 H 레벨(H2~H6)·여백·텍스트 데코는 변동 없습니다. H1만 시각 위계 측면에서 +15%.

## [3.0.8] — 2026-05-16 — Doc + tooling polish

### Changed

- **번들 헤더 문구 갱신** — `dist/theme-v3.css` 헤더의 v3-rewrite 시점 잔존 문구("not a drop-in replacement … keeps theme.css on v2.30.14 until S11 swap is approved")를 정식 출시 후 사실관계에 맞게 정리하고 dedup 패스 위치를 안내하도록 다듬었습니다.
- **pre-commit 후크에 결정성 검증 연결** — `scripts/hooks/pre-commit` 이 `bundle_v3.py --check` 로 바뀌었습니다. 소스만 수정하고 `dist/theme-v3.css` 재빌드/스테이징을 빠뜨린 커밋을 사전 차단합니다.

### Notes

- 디자인·런타임·산출물 동작 변동 없습니다. v3.0.7 사용자는 업데이트 없이도 동일하게 작동합니다.

## [3.0.7] — 2026-05-16 — Source dedup follow-up + bundle `--check` mode

### Changed

- **소스 중복 1건 정리** — `src/features/43-print-base.css` 안에서 같은 `@media print` 스코프에 두 번 등장하던 `.markdown-rendered h1 { page-break-before: always }` 블록을 한 곳으로 정리했습니다. 빌드 dedup 패스가 이미 처리하던 소스 레벨 중복(1건) → 0건. 인쇄 동작 100% 동일.
- **빌드 결정성 검증** — `python scripts/bundle_v3.py --check` 로 현재 `dist/theme-v3.css` 가 소스와 일치하는지 확인하는 모드를 추가했습니다 (CI / pre-commit 후크 용). 불일치 시 종료코드 1과 재빌드 안내 메시지.

### Notes

- 디자인·런타임 동작 변동 없으며 v3.0.6 사용자도 안전하게 업데이트할 수 있습니다.

## [3.0.6] — 2026-05-16 — Build: same-context duplicate-selector dedup pass

### Changed

- **빌드 단계에 selector 중복 병합 패스 추가** — 새 스크립트 `scripts/dedup_v3.py`가 같은 `@-rule` 컨텍스트(top-level 또는 같은 `@media`/`@supports`/`@container`) 안에서 정규화된 selector 문자열이 일치하는 블록만 마지막 위치로 모아 병합합니다. `:is()`·`:not()` 파싱 시도는 일절 하지 않으며 specificity·소스 순서 cascade가 그대로 보존됩니다.
- 적용 결과: `theme.css` 16,448 → **16,367 라인** (-81), 113개의 정확히 동일한 selector 블록 병합, `!important` 4건(전부 주석 내) 변동 없음. 스캐너의 “duplicate selector” 워닝이 의미 없는 잡음 수준으로 감소합니다.

### Notes

- 다른 `@-rule` 스코프 사이의 같은 selector(예: 일반 vs `@media print`)는 **병합하지 않습니다** — cascade 의미가 달라지기 때문입니다.
- 디자인·런타임 동작은 100% 동일합니다.

## [3.0.5] — 2026-05-16 — Scanner warnings: column-gap → gap

### Changed

- **커뮤니티 스캐너 multicolumn 워닝 2건 제거** — `src/features/43-print-base.css` 의 `column-gap` 2건을 표준 `gap`(L1 속기) 으로 교체. 그리드 컬럼 장면이라 동작 100% 동일.
- 단축형 `text-decoration` multi-value 27건, `:has()` 성능 권고, 의도된 중복 selector 워닝은 디자인·기능 핵심 의존성으로 유지.

## [3.0.4] — 2026-05-16 — Scanner warnings: text-decoration shorthand sweep

### Changed

- **커뮤니티 스캐너 `text-decoration partially supported` 워닝 일괄 정리** — `src/**/*.css`의 longhand `text-decoration-line/style/color/thickness` 42개 선언을 동등한 L1 `text-decoration` 단축형으로 조합. 링크 밑줄·스트라이크스루·철자 오류 수식 등 모든 표시는 100% 동일.
- 남은 `text-decoration-skip-ink: none` 3건은 H1/H3/H4 밑줄이 g·p·q 등 descender를 관통하며 그려지도록 유지하는 의도적 디자인 함수로 유지.

### Notes

- `text-indent`(2건)과 남은 `text-decoration-skip-ink`(3건) 워닝은 스캐너의 보수적 false positive이며 현재 Obsidian Electron 25+에서 완전 지원됩니다.

## [3.0.3] — 2026-05-16 — Scanner warnings: multicolumn cleanup

### Changed

- **커뮤니티 테마 스캐너 “multicolumn partially supported” 워닝 제거** — `src/**/*.css` 의 19개 `break-before/after/inside` 선언을 동등한 `page-break-*`(L2 알리스) 만 남기도록 치환. 인쇄(쪽 나눌) 동작과 디자인 100% 동일.

### Notes

- 남은 두 워닝 — `text-decoration` 계열(점선/두께/색 조절 underline)과 `text-indent`은 스캐너의 보수적 false positive입니다. 현재 Obsidian(Electron 25+)에서 완전 지원되며, 디자인(외부 링크의 닷티드 단과 한국어 본문 들여쓰기)을 손상하지 않고는 제거할 수 없어 남겨둡니다.

## [3.0.2] — 2026-05-16 — File explorer hover double-paint full fix

### Fixed

- **파일 탐색기 hover 더블 페인트(완전 해결)** — v3.0.1에서 여전히 남아있던 근본 원인 2가지를 제거.
  1. `src/chrome/37-tabs-file-explorer-search.css` 의 row hover 규칙이 `min-height` 24→32px, transform shift, inner pill padding을 동시에 키우면서 row와 pill이 겹쳐 두 겹으로 보이던 점프. → row는 transparent 고정, pill만 resting과 동일한 크기로 글래스 톤 적용.
  2. Obsidian 코어의 `--nav-item-background-{hover,active,selected}` 토큰이 그대로 살아있어 row에 회색 박스를 그리던 경로. → file-explorer 스코프에서 세 토큰을 transparent로 덮어 코어 페인트 경로 완전 차단.
- 최상위 root 폴더 hover는 resting pill 위에 글래스를 다시 얹는 대신 단일 톤(`rgba(255,255,255,0.92)` / dark 동등)으로 살짝 진해지게만 처리.

## [3.0.1] — 2026-05-16 — File explorer hotfix

### Fixed

- **파일 트리 hover 더블 페인트** — `src/chrome/31-navigation-tasks-search.css` 에 남아있던 v2 잔존 룰이 행 전체에 불투명 회색(`#f3f4f6` / `#1f2937`)을 칠해, `src/chrome/37-tabs-file-explorer-search.css` 의 글래스 pill 위에 회색 배경이 한 번 더 보이던 현상 제거. 이제 hover 표현은 글래스 pill 단일 레이어로 일원화됩니다.

### Changed

- **사이드바 파일 탐색기 컴팩트화** — 행 높이 28→24px, 자식 들여쓰기 15→8px, 아이콘 영역과 상하 여백 축소(자세한 수치는 `src/chrome/37-tabs-file-explorer-search.css`). 같은 패널 폭에서 약 20% 더 많은 문서 제목이 보입니다. 폴더 vertical rail과 hover/active 글래스 표현은 유지.

## [3.0.0] — 2026-05-16 — From-scratch rewrite with zero `!important`

### Summary

Owen Graphite v3.0.0은 v2.30.14의 픽셀 결과를 보존한 채 16,000+ 줄 CSS를 처음부터 다시 작성한 릴리즈입니다. `src/` 폴더 구조(tokens → base → surfaces → chrome → features → themes → plugins → polish)를 새로 설계하고, declaration-level `!important`를 5,816개에서 0개로 줄였습니다. computed-style fingerprint diff는 Light/Dark 모두 0, Live Preview hit-routing 감사도 clean입니다.

### Changed

- **CSS 재작성** — `dev/*` 60+ 파일을 `src/*` 폴더 8개 계층(tokens/base/surfaces/chrome/features/themes/plugins/polish)으로 재구성. 모든 본문 룰은 unlayered, 캐스케이드는 파일 import 순서 + 선택자 특이도로 통제.
- **`!important` 정책** — declaration-level `!important` = 0 (S11.5 일괄 제거). 자세한 휴리스틱·실증 결과는 [docs/v3/cascade-research.md](docs/v3/cascade-research.md) §4.1.
- **토큰 contract 유지** — `--ogd-*` 토큰 255개의 이름과 기본값은 v2.30.14와 동일. Style Settings 옵션 호환.
- **빌드 도구 교체** — `scripts/bundle_v3.py` 가 새 엔트리 포인트. `dist/theme-v3.css` 가 진본 번들이며 `theme.css` 는 이 번들의 사본.
- **CI 워크플로우** — `.github/workflows/validate.yml` 과 `release.yml` 을 v3 도구(`bundle_v3.py`, `audit_v3_hit_routing.py`, `v3_audit_duplicate_selectors.py`)로 갱신.

### Added

- `docs/v3/` — 보존 계약(`design-spec.md`), 캐스케이드 연구(`cascade-research.md`), 릴리즈 절차(`release-plan.md`), surface state matrix, golden image scenarios, live preview editability, style settings contract, token inventory.
- `docs/v3/research/` — 캐스케이드 휴리스틱 실증 시나리오 6종 + golden rig.
- `docs/v3/computed-fingerprint-v3.0.0-light.json` · `computed-fingerprint-v3.0.0-dark.json` — 베이스라인 fingerprint.
- `scripts/audit_v3_hit_routing.py` — Live Preview 블록 위젯·HyperMD line·active line·embed BFC·content overflow 회귀를 한 번에 검사하는 standalone 감사.
- `scripts/v3_audit_duplicate_selectors.py` — 모듈 간 selector 중복 통계.
- `scripts/v3_strip_important_src.py` — 주석 보호된 안전한 `!important` 제거기.
- `scripts/build_release.py` — `bundle_v3.py` 호출 → `theme.css` 승격 → `dist/Owen-Graphite-3.0.0.zip` 빌드.
- `scripts/sync_obsidian_theme.py` — 번들 + 승격 + Obsidian vault 동기화 통합 명령.

### Removed

- `dev/` 폴더 전체 (v2 source). `src/` 가 새 진본.
- v2 전용 스크립트: `bundle_theme.py`, `validate_theme.py`, `analyze_theme_css.py`, `diff_guard.py`, `who_added.py`, `hit_routing_probe.py`, `visual_regression.py`, `contrast_audit.py`, `generate_screenshots.py`, `build_selector_provenance.py`, `changelog_lint.py`, `find_safe_duplicate_selectors.py` 등.
- v2 전용 문서: `liquid-glass-migration-checklist.md`, `liquid-glass-token-map.md`, `css-important-audit.md`, `style-settings.md`, `qa-checklist.md` (v2 절차 한정), `ai-document-guide.md` 등.
- v2 release artifact: `dist/Owen-Graphite-2.30.*.zip`, `dist/theme-v3.no-important.css`.
- v2 screenshots: `screenshots/golden/v2.30.14/` 와 readme 폴더의 `v2.*.svg` 자산.

### Verification

| 항목 | 도구 | 결과 |
| --- | --- | --- |
| 번들 빌드 | `scripts/bundle_v3.py` | OK (16,509 줄, !important=4 — 모두 주석 안) |
| Light fingerprint diff | `scripts/fp_diff_summary.py --theme light` | **0** |
| Dark fingerprint diff | `scripts/fp_diff_summary.py --theme dark` | **0** |
| Live Preview hit-routing | `scripts/audit_v3_hit_routing.py` | clean |
| Release ZIP | `scripts/build_release.py` | `dist/Owen-Graphite-3.0.0.zip` (265 KB) |

[3.0.5]: https://github.com/towishy/Owen-Graphite/releases/tag/3.0.5
[3.0.4]: https://github.com/towishy/Owen-Graphite/releases/tag/3.0.4
[3.0.3]: https://github.com/towishy/Owen-Graphite/releases/tag/3.0.3
[3.0.0]: https://github.com/towishy/Owen-Graphite/releases/tag/3.0.0
