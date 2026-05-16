# Community Scanner Acknowledgments

이 문서는 Obsidian 커뮤니티 테마 스캐너가 `Owen Graphite`에 대해 출력하는 경고 가운데 **의도적으로 유지되는 항목**을 한 페이지로 정리합니다. 각 경고가 왜 디자인·기능을 깨지 않고는 제거할 수 없는지, 어떤 모듈이 책임자(owner)인지 명시합니다.

스캐너 경고는 **블로커가 아니라 정보성**입니다. 아래 항목들은 모두 Owen Graphite의 캐스케이드 아키텍처상 필요한 것이며, 실제 렌더 결과에는 부정적 영향이 없습니다.

## 1. `Multiple !important rules detected` — **유지**

| 항목 | 값 |
| --- | ---: |
| 빌드 기준 `!important` | 5,819 (v2.30.13) |
| 주요 owner | `dev/08-report-print-polish.css`, `dev/10-a11y-regression-hotfixes.css`, `dev/10b-late-reading-nav-polish.css`, `dev/10d-liquid-glass-core.css`, `dev/09b-editing-menu-tooltip-glass.css` |

### 왜 필요한가
- Obsidian core CSS는 Owen Graphite 모듈보다 늦게 로드되는 일이 많고, 일부 Style Settings 옵션(`body.ogd-*` 토글)은 core variables 위에 다시 얹혀야 합니다.
- `@layer` 같은 캐스케이드 레이어 메커니즘 없이 우선순위를 명시적으로 표현하는 유일한 방법이 `!important`입니다.
- Liquid Glass 토큰, dark mode override, `prefers-contrast: more`, `@media print`, Style Settings 미러 토큰이 모두 한 cascading layer에 있기 때문에, 한 곳에서 `!important`를 빼면 다른 모듈이 의도와 다른 시점에 이깁니다.

### 어떻게 줄이고 있는가
- `docs/css-important-audit.md`에 모듈별 우선순위가 정리되어 있으며, 안정화된 hotfix를 원 owner 모듈로 되돌리는 작업이 지속적으로 진행됩니다.
- 패치 사이클당 평균 10~50건이 자연 감소합니다(예: v2.22.33 `09b` toolbar token 축소 등).

### 완전 제거 방법
- 장기 로드맵은 [layer-migration-roadmap.md](layer-migration-roadmap.md) 참조. `@layer obsidian, owen-base, owen-glass, owen-hotfix;` 도입 후 단계적 마이그레이션이 유일한 정공법입니다.

## 2. `Unexpected duplicate selector` — **대부분 유지**

| 카테고리 | 처리 |
| --- | --- |
| 같은 모듈, 같은 selector, 같은 body, 같은 at-rule context | **자동 청소 대상** — `scripts/find_safe_duplicate_selectors.py`로 추출하여 패치 단위로 제거 |
| 다른 모듈에 같은 selector가 등장 (light → dark → a11y → print → hotfix) | **유지** — 의도된 책임 분리. 다크/프린트/hotfix의 cascading override가 동작해야 함 |
| 같은 모듈, 같은 selector, **다른 body** | **유지** — 후속 패치에서 의도적으로 specificity 또는 위치를 활용한 override |

### 책임자 매트릭스 (대표 selector 예시)

| selector | 1차 owner | 2차 (dark) | 3차 (print/report) | 4차 (a11y/hotfix) |
| --- | --- | --- | --- | --- |
| `.markdown-rendered table` | `dev/03a-reading-tables-code.css` | `dev/04-dark-mode.css` | `dev/08-report-print-polish.css`, `dev/06-feature-presets.css` (@media print) | `dev/10-a11y-regression-hotfixes.css` |
| `.callout` | `dev/03b-reading-callouts-lists.css` | `dev/04-dark-mode.css` | `dev/08-report-print-polish.css` | `dev/10-a11y-regression-hotfixes.css`, `dev/10d-liquid-glass-core.css` |
| `.workspace-tab-header` | `dev/02-base-workspace.css` | `dev/04-dark-mode.css` | — | `dev/09d-tabs-file-explorer-search.css`, `dev/10d-liquid-glass-core.css` |
| `.cm-callout` | `dev/05-live-preview.css` | `dev/04-dark-mode.css` | `dev/08-report-print-polish.css` | `dev/10-a11y-regression-hotfixes.css` |
| `body.ogd-report-mode .metadata-container` | `dev/06-feature-presets.css` | — | `dev/08-report-print-polish.css` | — |

위 4단 구조 가운데 한 단계라도 통합하면 다른 단계가 우선권을 잃으며 시각적 회귀가 발생합니다.

### v2.30.13 cleanup 결과

`scripts/find_safe_duplicate_selectors.py`로 탐지된 **진짜 무해한 중복 4건**을 v2.30.13 패치에서 제거했습니다.

| 모듈 | 위치(이전) | 비고 |
| --- | --- | --- |
| `dev/06-feature-presets.css` | `@media print` 내 `body.ogd-last-page-footer ... :last-child::after::first-line` 두 번째 사본 | 같은 `@media print` 블록 내 byte-identical 중복. ::marker 기반 isolation hotfix는 그대로 유지 |
| `dev/10e-html-table-live-preview-glass.css` | v2.30.9 블록의 `body.ogd-zebra-disabled-permanently ... tbody tr:nth-child(even) td` | v2.30.16 블록이 owner로 남음 |
| `dev/10e-html-table-live-preview-glass.css` | v2.30.9 블록의 `body.theme-dark:not(.ogd-report-mode) ... table { --ogd-table-* tokens }` | v2.30.16 블록이 owner로 남음 |
| `dev/10e-html-table-live-preview-glass.css` | v2.30.18 블록의 dark report-mode `thead th { border-bottom-color: rgba(148, 163, 184, 0.34) !important }` | v2.30.20 블록이 owner로 남음 |

각 제거는 다음 세 조건을 모두 만족하는 경우에만 수행했습니다.
1. 같은 모듈 내에 동일 selector + 동일 body + 동일 at-rule context의 사본이 존재.
2. 두 사본 사이에 같은 property를 다른 값으로 재정의하는 규칙이 없음(cascade 결과 동일).
3. 두 사본을 한 줄로 합쳐도 specificity 합산 결과가 변하지 않음.

## 3. `Avoid :has(...)` — **유지 (Obsidian 1.6+ 전제)**

### 왜 필요한가
- 활성 폴더/탭/링크 마커, 콜아웃 내부 코드블록 처리, Live Preview 위젯의 부모 인식, "현재 라인을 포함한 콜아웃 강조" 등에서 `:has()`는 **CSS 단독으로 부모-자식 상태를 추론하는 유일한 수단**입니다.
- 대안은 JavaScript로 부모에 boolean class를 추가하는 것뿐인데, Owen Graphite는 CSS-only 테마라 적용 불가합니다.

### 호환성
- Obsidian 데스크톱 1.6+(Chromium ≥ 110)는 `:has()`를 완전 지원합니다.
- iOS Safari 15 이하는 부분 지원이지만, Obsidian iOS는 WKWebView 기반으로 OS 16 이상에서만 동작하며 OS 16부터 완전 지원.
- 따라서 실사용 환경에서는 false positive입니다.

### 명시 위치
- `manifest.json`의 `minAppVersion: 1.6.0`이 baseline을 명시합니다.

## 4. Partial support: `text-decoration` / `multicolumn` / `css-text-indent`

| 속성 | caniuse 비고 | Obsidian 영향 |
| --- | --- | --- |
| `text-decoration` shorthand | IE/구형 Safari 부분 지원 | 데스크톱/iOS/Android 모두 정상 |
| `column-*` / multicolumn | 구형 Edge 부분 지원 | 비대상 |
| `text-indent` 추가 옵션 | iOS Safari 일부 키워드 부분 지원 | 사용된 옵션은 모두 호환 범위 |

### 처리
- Obsidian core가 위 속성을 사용하지 않는 환경(레거시 모바일 등)에서 Owen Graphite의 시각 효과가 약간 다르게 보일 수 있으나, 가독성 자체에는 영향이 없습니다.
- 기능 회귀가 발생하면 해당 layer만 `@supports`로 가드합니다(현재 발견된 사례 없음).

## 요약

| 카테고리 | 건수 (v2.30.13) | 권고 |
| --- | ---: | --- |
| `!important` | 5,819 | 유지, 장기 layer 마이그레이션 |
| Duplicate selector (의도) | 다수 | 유지 |
| Duplicate selector (의도하지 않음) | 0 | v2.30.13에서 4건 정리 완료 |
| `:has()` | 다수 | 유지 (Obsidian 1.6+ 가정) |
| Partial support 속성 | 소수 | 유지 (실사용 환경 영향 없음) |

스캐너 결과에서 위 카테고리에 해당하지 않는 **새로운** 경고가 나타나면 별도로 검토 후 이 문서를 갱신합니다.
