# `@layer` Migration Roadmap

Owen Graphite의 5,819개 `!important`를 장기적으로 줄이기 위한 캐스케이드 레이어 도입 계획입니다. 본 문서는 **계획서**이며, 실 마이그레이션은 별도 메이저 버전(예: v3.0)에서 단계적으로 진행합니다.

## 문제 정의

| 항목 | 현재 |
| --- | ---: |
| 전체 `!important` | 5,819 |
| 영향 모듈 수 | 29 |
| 대표 owner | `08-report-print-polish.css` (516), `10-a11y-regression-hotfixes.css` (498), `10b-late-reading-nav-polish.css` (339), `10d-liquid-glass-core.css` (342) |
| 직접 원인 | Obsidian core CSS를 이기기 위한 우선순위 명시 + Style Settings 토글 + 다크/프린트/a11y override가 한 cascading layer를 공유 |

## 목표 레이어 구조

```css
@layer obsidian, owen-base, owen-glass, owen-features, owen-darkmode, owen-print, owen-a11y, owen-hotfix;
```

| 레이어 | 책임 | 현재 모듈 |
| --- | --- | --- |
| `obsidian` | Obsidian core가 정의한 변수와 reset (선언만 하고 비워둠 — 실제 core는 이 레이어 밖이지만 우선순위 계산 기준점) | (없음) |
| `owen-base` | 토큰 정의, 기본 reading/Live Preview 룰 | `00`, `01`, `02`, `03`, `03a`, `03b`, `03c`, `05` |
| `owen-glass` | Liquid Glass 코어 토큰 | `10d` |
| `owen-features` | Style Settings 토글, feature preset | `00`, `06`, `06`의 일부 |
| `owen-darkmode` | dark theme override | `04` |
| `owen-print` | 프린트/리포트 polish | `04-print-base.css`, `08`, `06`의 `@media print` 블록 |
| `owen-a11y` | accessibility motion/contrast | `10`, `10a` |
| `owen-hotfix` | 안정화 전 hotfix (장기적으로 비어가야 함) | `10b`, `10c`, `10e`, `10f` |

레이어 안에서 선언된 규칙은 **선언 순서와 무관하게 레이어 우선순위로 이깁니다**. `!important` 없이도 다크/프린트/a11y가 base를 이길 수 있습니다.

## 단계별 마이그레이션 계획

### Phase 0 — 가드 구축 (소요 1 패치)
- `@layer` 선언 부재 시 회귀 발생을 잡기 위해 `scripts/visual_regression.py`에 다음 추가:
  - Liquid Glass surface (rest / hover / active)
  - dark + light × report-mode × Live Preview 매트릭스 16샷
  - `prefers-contrast: more` 가상 매트릭스 4샷
- `scripts/contrast_audit.py`의 13쌍 ↗ 25쌍으로 확장.
- 변경 사항 없음. 회귀 안전망만 마련.

### Phase 1 — 레이어 선언 도입 (1 패치, 시각 변화 0)
- `dev/00-settings.css` 최상단에 `@layer obsidian, owen-base, owen-glass, owen-features, owen-darkmode, owen-print, owen-a11y, owen-hotfix;` 추가.
- 모든 기존 규칙은 **레이어 밖**(unlayered)에 남음 → unlayered 규칙은 모든 `@layer`보다 우선이므로 **시각 변화 0**.
- 회귀 테스트가 모두 통과해야 다음 단계.

### Phase 2 — `owen-base` 이전 (3~5 패치, low risk)
- 모듈 단위로 `@layer owen-base { … }`로 감쌈.
- 한 패치당 1~2 모듈씩.
- 각 패치마다:
  1. 해당 모듈을 layer 안으로 이동.
  2. 그 모듈 안의 `!important` 가운데 "Obsidian core를 이기기 위한 것"만 제거.
  3. 회귀 테스트 + Style Settings 모든 옵션 토글 확인.
  4. 다크/프린트/a11y 모듈은 아직 unlayered → 그대로 이김.
- 예상 `!important` 감소: 모듈당 약 30~80건.

### Phase 3 — `owen-glass` 이전 (1 패치)
- `dev/10d-liquid-glass-core.css`를 `@layer owen-glass { … }`로 감쌈.
- Liquid Glass 토큰은 base보다 늦고 dark/print보다 일찍 이겨야 하므로 레이어 순서가 정확해야 함.
- Hover study fixture, mobile glass fixture로 회귀 확인.

### Phase 4 — `owen-features` 이전 (2~3 패치)
- Style Settings 토글(`body.ogd-*`)을 활용한 feature preset 모듈.
- 토큰만 갈아끼는 형태가 많아서 가장 안전한 이전 대상.

### Phase 5 — `owen-darkmode` + `owen-print` 이전 (2 패치)
- dark/print는 base보다 늦게 이겨야 하므로 레이어 우선순위 활용.
- 한 모듈을 옮길 때 base 모듈도 이미 layer 안에 있어야 함.

### Phase 6 — `owen-a11y` 이전 (1 패치)
- `prefers-contrast: more`, `prefers-reduced-motion` 가드 모듈.
- 모든 다른 layer를 이겨야 하므로 거의 마지막 layer.

### Phase 7 — `owen-hotfix` 소진 (다수 패치, 장기)
- 기존 `dev/10b`, `dev/10c`, `dev/10e`, `dev/10f`의 규칙을 원 owner 모듈로 되돌림.
- 옮길 수 없는 진짜 hotfix만 `owen-hotfix` layer에 남김.
- 최종적으로 `owen-hotfix` layer 행 수 < 200을 목표.

## 위험 매트릭스

| 단계 | 위험 | 완화책 |
| --- | --- | --- |
| Phase 1 | layer 선언 자체가 일부 구형 모바일 WebView에서 미지원 | `minAppVersion: 1.6.0` 가정 + Phase 0 회귀 매트릭스가 모바일 포함 |
| Phase 2 | unlayered → layered 이동 시 specificity 계산이 달라 보일 수 있음 | layer 안에서도 selector specificity는 동일하게 작동. layer 우선순위가 추가될 뿐 |
| Phase 3 | Liquid Glass가 dark mode 위로 떠 보이면 안 됨 | layer 순서 `owen-glass < owen-darkmode`로 명시 |
| Phase 5 | `@media print` 규칙은 layer 안에 들어가도 동작하지만, `@page` rule은 layer 밖 | print rule은 `@layer owen-print { @media print { … } }` 구조로 감쌈 |
| Phase 7 | 안정화된 hotfix를 원 owner로 되돌릴 때 잠재 회귀 | 모듈 단위로 한 패치당 < 100줄 이동, visual regression 통과 의무화 |

## 예상 결과

| 항목 | v2.30.13 | v3.0 목표 |
| --- | ---: | ---: |
| 전체 `!important` | 5,819 | < 1,500 |
| 모듈 수 | 29 | 동일 (책임만 명확해짐) |
| `dev/10-*` (hotfix layer) 총 라인 | 약 3,700 | < 800 |
| 빌드 크기 (theme.css) | 약 800KB | < 600KB |

## 권고

- **단기**: 본 로드맵은 계획서로만 유지. v2.30.x 패치 사이클에서는 기존 `!important` 청소만 점진적으로 진행.
- **중기**: Obsidian core가 `@layer`를 정식으로 도입(또는 사용)하는 시점이 오면 Phase 1 즉시 진행.
- **장기**: v3.0 메이저 버전 도입과 함께 Phase 2~7 진행. 메이저 버전에서는 minAppVersion을 그 시점의 안정 버전으로 올려 모바일 호환 가드를 단순화.

## 참고

- [community-scanner-acknowledgments.md](community-scanner-acknowledgments.md) — 현재 경고의 의도성 정리
- `docs/css-important-audit.md` — 기존 `!important` 청소 진행 기록
- `dev/MAP/css-stabilization-checklist.md` — 안정화 체크리스트
- MDN: [`@layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/@layer)
