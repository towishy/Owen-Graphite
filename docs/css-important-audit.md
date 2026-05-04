# Owen Graphite CSS Important Audit

## Current Inventory

| 항목 | 값 |
|------|----|
| Theme size | 약 10,600 lines |
| `!important` count | 약 3,461 |
| Audit 기준 | `scripts/validate_theme.py`의 CSS complexity inventory |

## First Pass Counts

| 모듈 | `!important` | 1차 판정 |
|------|-------------:|----------|
| `dev/09b-editing-menu-tooltip-glass.css` | 312 | editing menu/tooltip focus와 hover shadow 중복 후보 |
| `dev/07-plugin-workspace.css` | 204 | plugin row/card state 공통화 후보 |
| `dev/06-feature-presets.css` | 170 | report/table preset 책임 분리 후보 |
| `dev/10d-liquid-glass-core.css` | 92 | 최신 liquid glass token owner, 제거보다 기준 고정 우선 |

## Highest Priority Modules

| 우선순위 | 모듈 | 현재 성격 | 정리 방향 |
|----------|------|-----------|-----------|
| 1 | `dev/09b-editing-menu-tooltip-glass.css` | editing menu, tooltip, toolbar glass override 밀집 | 중복 hover/focus shadow를 shared token으로 접기 |
| 2 | `dev/06-feature-presets.css` | feature preset, report utility, print-related override 혼재 | preset별 selector ownership를 문서화하고 반복 declaration 축소 |
| 3 | `dev/07-plugin-workspace.css` | plugin/workspace surface override 다수 | plugin DOM별 책임 범위를 분리하고 late override 의존도 축소 |
| 4 | `dev/10d-liquid-glass-core.css` | 최신 liquid glass state override | token mapping 기준을 유지하고 새 selector는 한 묶음씩 검토 |

## Rules For Cleanup

- `!important`를 한 번에 제거하지 않는다. 한 selector group씩 실제 Obsidian 화면에서 확인한다.
- core chrome 구조 속성은 validator guard를 먼저 통과해야 한다.
- shadow/rim/focus 값은 [liquid-glass-token-map.md](liquid-glass-token-map.md)의 token mapping을 우선한다.
- 삭제보다 ownership 축소가 먼저다. 같은 상태를 여러 모듈에서 칠하면 가장 늦은 모듈에만 남긴다.

## Candidate Work Items

| 작업 | 기대 효과 | 검증 |
|------|-----------|------|
| Editing toolbar hover/focus selector 묶음 조사 | `09b` 중복 override 축소 | `Validate Theme`, toolbar visual smoke |
| Feature preset table/report selector 재분류 | `06`의 report/table 책임 분리 | PDF/report sample 확인 |
| Plugin workspace row state 공통화 | `07`의 row hover/focus 중복 감소 | search/backlinks/graph sample 확인 |
| Liquid glass focus selector matrix 유지 | 새 focus 대상 누락 방지 | token map + validator guard |

## 09b First Cleanup Slice

| selector group | 현재 상태 | 다음 조사 |
|----------------|-----------|-----------|
| `#editingToolbarModalBar :is(.clickable-icon, button, .editingToolbarButton)` | base/hover/dark hover가 `--ogd-glass-control-*` token을 반복 사용 | light/dark 공통 declaration을 token owner로 접을 수 있는지 확인 |
| `.editing-toolbar :is(.editing-toolbar-button, button, .clickable-icon):hover` | hover background/shadow가 modal bar hover와 유사 | hover shadow를 shared control shadow 변수로 합칠 후보 |
| `.editing-toolbar-modal`, `.editing-toolbar-popover`, `[class*="cMenuToolbar"]` | floating toolbar surface와 button state가 반복 | surface owner와 control owner를 분리해 중복 선언 축소 후보 |
| `.menu .menu-item:hover` | menu row 안정성을 위해 `!important`가 집중 | row height/hit target이 유지되는지 확인 전 제거 금지 |

## Do Not Start With

- `dev/10d-liquid-glass-core.css`의 최신 focus/table override를 먼저 제거하지 않는다.
- Obsidian 실제 DOM 확인 없이 `.workspace-tab-*`, `.titlebar-*`, `.workspace-ribbon` 관련 `!important`를 제거하지 않는다.
- validator가 보호하는 focus selector는 공통 token으로 접기 전까지 유지한다.