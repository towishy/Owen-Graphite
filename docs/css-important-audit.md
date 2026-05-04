# Owen Graphite CSS Important Audit

## Current Inventory

| 항목 | 값 |
|------|----|
| Theme size | 약 10,600 lines |
| `!important` count | 약 3,461 |
| Audit 기준 | `scripts/validate_theme.py`의 CSS complexity inventory |

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