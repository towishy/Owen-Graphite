# Owen Graphite CSS Important Audit

## Current Inventory

| 항목 | 값 |
| --- | --- |
| Theme size | 14,782 lines |
| `!important` count | 5,050 |
| Audit 기준 | `scripts/validate_theme.py`의 CSS complexity inventory |

## First Pass Counts

| 모듈 | lines | `!important` | 1차 판정 |
| --- | ---: | ---: | --- |
| `dev/08-report-print-polish.css` | 1,426 | 516 | PDF/report output polish가 여전히 밀집된 주요 점검 지점 |
| `dev/10-a11y-regression-hotfixes.css` | 1,393 | 498 | callout liquid glass owner 포함, 안정화된 hotfix를 원 owner로 되돌릴 후보 |
| `dev/10b-late-reading-nav-polish.css` | 848 | 339 | late reading/nav override 중복 후보 |
| `dev/10d-liquid-glass-core.css` | 1,364 | 342 | 최신 liquid glass token owner, 제거보다 기준 고정 우선 |
| `dev/09b-editing-menu-tooltip-glass.css` | 800 | 296 | editing menu/tooltip/toolbar surface 중복 후보 |
| `dev/06-feature-presets.css` | 913 | 262 | feature preset/report utility 책임 분리 후보 |
| `dev/07-plugin-workspace.css` | 708 | 205 | plugin row/card state 공통화 후보 |

## v2.22.33 Cleanup Result

| 항목 | 이전 | 이후 | 메모 |
| --- | ---: | ---: | --- |
| 전체 `!important` | 3,466 | 3,456 | `09b` toolbar/submenu control rest/hover 값을 shared token으로 접음 |
| `dev/09b-editing-menu-tooltip-glass.css` lines | 842 | 820 | selector target은 유지하고 light/dark 중복 선언만 축소 |
| `dev/09b-editing-menu-tooltip-glass.css` `!important` | 312 | 302 | context menu row state는 실제 DOM 확인 전 유지 |
| Visual QA fixture | - | 추가 | community theme browser search calm focus smoke fixture 추가 |

## v2.22.34 Header Action Hotfix Note

| 항목 | 값 | 메모 |
| --- | ---: | --- |
| 전체 `!important` | 3,477 | 우상단 view header action glass surface 보정 후 수치 |
| `dev/10d-liquid-glass-core.css` | 440 lines / 113 `!important` | late core owner에 scoped header action treatment 추가 |
| MAP risk | medium=0, low=0, info=79 | width/height 구조 고정은 제거하고 surface state만 유지 |

## v2.22.128 Inventory Refresh

| 항목 | 값 | 메모 |
| --- | ---: | --- |
| 전체 `!important` | 5,050 | PDF/list/table/callout parity 안정화 이후 현재 validator 기준 |
| `dev/08-report-print-polish.css` | 1,426 lines / 516 `!important` | legacy report callout rail 축소 후에도 PDF table/code/callout 밀집 구간 |
| `dev/10-a11y-regression-hotfixes.css` | 1,393 lines / 498 `!important` | Liquid Glass callout 최종 owner 포함, 장기 hotfix owner 축소 후보 |
| `dev/09b-editing-menu-tooltip-glass.css` | 800 lines / 296 `!important` | toolbar/submenu surface token compaction 적용 후 남은 menu/tooltip 후보 |

## Highest Priority Modules

| 우선순위 | 모듈 | 현재 성격 | 정리 방향 |
| --- | --- | --- | --- |
| 1 | `dev/08-report-print-polish.css` | PDF/report output polish와 print fallback 밀집 | PDF table/code/callout/header-footer 책임 구간별 압축 또는 분리 검토 |
| 2 | `dev/10-a11y-regression-hotfixes.css` | 최종 회귀 hotfix owner | 안정화된 규칙은 원 owner 모듈로 되돌리고 마지막 방어만 유지 |
| 3 | `dev/09b-editing-menu-tooltip-glass.css` | editing menu, tooltip, toolbar glass override 밀집 | 중복 hover/focus shadow를 shared token으로 접기 |
| 4 | `dev/10d-liquid-glass-core.css` | 최신 liquid glass state override | token mapping 기준을 유지하고 새 selector는 한 묶음씩 검토 |

## Rules For Cleanup

- `!important`를 한 번에 제거하지 않는다. 한 selector group씩 실제 Obsidian 화면에서 확인한다.
- core chrome 구조 속성은 validator guard를 먼저 통과해야 한다.
- shadow/rim/focus 값은 [liquid-glass-token-map.md](liquid-glass-token-map.md)의 token mapping을 우선한다.
- 삭제보다 ownership 축소가 먼저다. 같은 상태를 여러 모듈에서 칠하면 가장 늦은 모듈에만 남긴다.

## Candidate Work Items

| 작업 | 기대 효과 | 검증 |
| --- | --- | --- |
| PDF/report polish 구간별 inventory 작성 | `08` 예산 초과 위험 사전 차단 | `Validate Theme`, PDF/report sample 확인 |
| A11y hotfix owner 재분류 | late hotfix cascade 의존도 축소 | `Validate Theme`, Live Preview/table smoke |
| Editing toolbar hover/focus selector 묶음 조사 | `09b` 중복 override 축소 | `Validate Theme`, toolbar visual smoke |
| Feature preset table/report selector 재분류 | `06`의 report/table 책임 분리 | PDF/report sample 확인 |
| Plugin workspace row state 공통화 | `07`의 row hover/focus 중복 감소 | search/backlinks/graph sample 확인 |
| Liquid glass focus selector matrix 유지 | 새 focus 대상 누락 방지 | token map + validator guard |

## 09b First Cleanup Slice

| selector group | 현재 상태 | 다음 조사 |
| --- | --- | --- |
| `#editingToolbarModalBar :is(.clickable-icon, button, .editingToolbarButton)` | base/hover/dark hover가 `--ogd-glass-control-*` token을 반복 사용 | light/dark 공통 declaration을 token owner로 접을 수 있는지 확인 |
| `.editing-toolbar :is(.editing-toolbar-button, button, .clickable-icon):hover` | hover background/shadow가 modal bar hover와 유사 | hover shadow를 shared control shadow 변수로 합칠 후보 |
| `.editing-toolbar-modal`, `.editing-toolbar-popover`, `[class*="cMenuToolbar"]` | floating toolbar surface와 button state가 반복 | surface owner와 control owner를 분리해 중복 선언 축소 후보 |
| `.menu .menu-item:hover` | menu row 안정성을 위해 `!important`가 집중 | row height/hit target이 유지되는지 확인 전 제거 금지 |

## Do Not Start With

- `dev/10d-liquid-glass-core.css`의 최신 focus/table override를 먼저 제거하지 않는다.
- Obsidian 실제 DOM 확인 없이 `.workspace-tab-*`, `.titlebar-*`, `.workspace-ribbon` 관련 `!important`를 제거하지 않는다.
- validator가 보호하는 focus selector는 공통 token으로 접기 전까지 유지한다.
