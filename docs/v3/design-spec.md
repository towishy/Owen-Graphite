# Owen Graphite v3.0 Design Spec

이 문서는 Owen Graphite v3.0 **from-scratch 재작성**의 단일 진실 공급원(single source of truth)입니다. v3-rewrite 브랜치에서 작성되는 모든 CSS는 이 문서의 **보존 계약**을 통과해야 합니다.

## 목표

- 디자인 100% 보존, 기능 100% 보존
- CSS 첫 줄부터 새로 작성
- Obsidian 커뮤니티 스캐너 경고 **0**
- 코드량 약 16,000줄 → 6,000~8,000줄 목표
- `!important` 5,816 → 두 자릿수 이하 목표

## 보존 계약 (Preservation Contract)

다음 5가지가 모두 통과해야 "v2.30.14와 동일하다"로 판정합니다. 각 계약은 자동 검증 도구를 가집니다.

| # | 계약 | 검증 도구 | 통과 기준 |
| --- | --- | --- | --- |
| C1 | 시각 (Liquid Glass + 일반 surface) | `scripts/visual_regression.py` (확장) | 60+ 시나리오, 픽셀 diff < 1% |
| C2 | 색 대비 (WCAG) | `scripts/contrast_audit.py` (확장) | 30+ 쌍 모두 AA 이상 |
| C3 | Style Settings 동작 | 토글 매트릭스 캡처 | 37개 옵션 × ON/OFF = 74 cell 동일 |
| C4 | Live Preview 편집성 | `scripts/hit_routing_probe.py` | 클릭 좌표 → 동일 contenteditable 도달 |
| C5 | PDF 출력 | print 시나리오 PDF 비교 | 페이지 수·레이아웃·footer 동일 |

각 계약의 매트릭스는 별도 문서에 상세화됩니다 (아래 "참조 문서" 표 참고).

## 아키텍처 결정

### 캐스케이드 레이어

```css
@layer reset, tokens, base, surfaces, chrome, features, plugins, dark, a11y, hotfix;
```

- `reset` — Obsidian core를 부드럽게 다듬는 reset
- `tokens` — `--ogd-*` custom property 정의 (light default)
- `base` — Reading View / Live Preview 베이스 타이포·간격
- `surfaces` — callout / table / code / list / embed
- `chrome` — workspace / nav / overlay / settings
- `features` — Style Settings 토글, report-mode, PDF print
- `plugins` — Dataview / Tasks / Canvas / Outline 등
- `dark` — `.theme-dark` override
- `a11y` — `prefers-contrast: more`, `prefers-reduced-motion`, `forced-colors`
- `hotfix` — 정말 옮길 수 없는 최후의 hotfix (v3에서는 비어 있어야 함)

### 폴더 구조

```
src/
  entry.css                  # @layer 선언 + @import 순서
  tokens/
    01-colors.css            # 색 스케일 (slate, sky, neutral)
    02-typography.css        # font, size, line-height
    03-spacing.css           # spacing, radius
    04-motion.css            # easing, duration
    05-glass.css             # Liquid Glass surface tokens (rest/hover/active/disabled)
  base/
    10-reset.css
    11-typography.css
    12-reading-view.css
    13-live-preview.css
  surfaces/
    20-callout.css
    21-table.css
    22-code-block.css
    23-list.css
    24-embed.css
    25-canvas-graph.css
  chrome/
    30-workspace.css
    31-nav.css
    32-overlay.css
    33-settings.css
  features/
    40-style-settings.css
    41-report-mode.css
    42-pdf-print.css
  themes/
    50-dark.css
    51-a11y.css
  plugins/
    60-dataview.css
    61-tasks.css
    ...
```

### 토큰 우선 설계

모든 색·간격·그림자·필터는 `var(--ogd-*)` 토큰을 통과합니다. 색 한 개를 바꾸려면 `tokens/01-colors.css`의 한 줄만 수정.

**토큰 이름 contract**: v2.30.14의 255개 토큰 이름을 그대로 유지합니다 (Style Settings 마이그레이션을 위해). 신규 토큰 추가는 OK, 기존 이름 변경은 금지.

기존 토큰 인벤토리: [token-inventory.md](token-inventory.md) (255 tokens, scripts/extract_token_inventory.py로 자동 생성)

### `!important` 정책

- `tokens` ~ `plugins` 레이어: `!important` **금지** (예외는 PR 리뷰)
- `dark`, `a11y` 레이어: `!important` **금지** (layer 우선순위로 해결)
- `hotfix` 레이어: 명시적 주석 + PR 리뷰 통과 시에만 허용

Obsidian core CSS가 `!important`를 거는 곳을 이기기 위한 경우에만 예외. 그 경우에도 CSS comment에 **어떤 core selector를 이기는지** 명시해야 함.

## 참조 문서 (S0 산출물)

| 문서 | 책임 |
| --- | --- |
| [token-inventory.md](token-inventory.md) | v2.30.14 토큰 이름·기본값 contract |
| `surface-state-matrix.md` (TODO) | Liquid Glass rest/hover/active/disabled 정의표 |
| `style-settings-contract.md` (TODO) | Style Settings 37개 옵션 이름·동작 표 |
| `live-preview-editability.md` (TODO) | hit-routing 보존 contract |
| `golden-image-scenarios.md` (TODO) | 60+ 시각 회귀 시나리오 목록 |

## 진행 단계 (Phase / Step)

| Step | 산출물 | 위험 |
| --- | --- | --- |
| **S0** | 디자인 스펙 + 토큰 인벤토리 (현재 진행) | 낮음 (읽기만) |
| **S1** | 골든 이미지 60+ 세트 = v2.30.14의 정답지 | 낮음 (현재 빌드로 캡처) |
| **S2** | `src/entry.css` + 토큰 모듈 + v3-alpha manifest | 낮음 |
| **S3** | base + reading-view | 중간 |
| **S4** | live-preview + editability probe 통과 | **높음** |
| **S5** | surfaces (callout/table/code/list/embed) | 중간 |
| **S6** | chrome (workspace/nav/overlay/settings) | 중간 |
| **S7** | features (Style Settings 37개) | 중간 |
| **S8** | dark + a11y | 중간 |
| **S9** | PDF print | 중간 |
| **S10** | plugins (선택적) | 낮음 |
| **S11** | 스캐너 0 warning 확인 + v3.0.0 릴리스 | 낮음 |

각 Step은 다음 조건을 모두 만족해야 다음 Step으로 진입:

1. 해당 Step이 담당하는 보존 계약(C1~C5) 통과
2. 로컬 Obsidian에서 사용자 육안 검증 완료
3. v3-rewrite 브랜치에 commit (커밋 메시지에 "step Sx" prefix)

## 검증 전략

### 기준점

- baseline 빌드: v2.30.14 (commit `94e5fbe`, tag `2.30.14`)
- baseline theme.css: `theme.css` (v3-rewrite 브랜치 시작 시점)
- 모든 골든 이미지는 baseline 빌드에서 캡처

### 로컬 Obsidian 검증

- 검증 vault: `H:\Obsidian` (Owen Graphite 테마 설치 위치)
- 검증 방식:
  1. v3-rewrite 브랜치에서 빌드 후 `robocopy /MIR`로 vault에 동기화
  2. Obsidian에서 **Ctrl+R** (또는 Reload App)로 테마 새로 로드
  3. 미리 정의된 검증 시나리오 (S1에서 정의) 순회
- 회귀 발견 시: v3-rewrite 작업 중단, baseline으로 즉시 되돌리기, 원인 분석

### 브랜치 전략

- `main`: v2.30.x 안정 라인. 커뮤니티 릴리스. 비상 hotfix만 적용.
- `v3-rewrite`: from-scratch 작업 브랜치. **로컬 검증 완료 전까지 main으로 머지 금지.**
- `v3-rewrite`가 완성되면 `main`에 머지하되, manifest version을 `3.0.0`으로 점프.

## 비목표 (Non-Goals)

다음은 v3.0의 목표가 **아닙니다**:

- 새로운 디자인 도입 (디자인 변경은 v3.1+)
- 새로운 기능 추가 (기능 추가는 v3.1+)
- Style Settings 옵션 통합·정리 (v3.0은 37개 이름·동작 동일 유지)
- minAppVersion 변경 (1.6 유지)
- 새로운 플러그인 지원 추가

이 비목표 가운데 어느 것이라도 필요해지면 v3.0 출시 후 별도 마이너 버전에서 다룹니다.

## 의사결정 로그

| 일자 | 결정 | 근거 |
| --- | --- | --- |
| 2026-05-16 | v3.0 from-scratch 진행 결정 | 사용자 요청 ("기능과 디자인을 유지할수있다면 첫줄부터 새로 짜도 좋을정도") |
| 2026-05-16 | v3-rewrite 별도 브랜치 사용 | 사용자 요청 ("일단 별도 브랜치로 해서 작업하고, 로컬 옵시디언에서 검증") |
| 2026-05-16 | 골든 이미지 픽셀 100% 기준 | 가장 안전. 미세 차이는 v3.0 출시 후 별도 검토 |
| 2026-05-16 | Style Settings 37개 이름·동작 동일 | 사용자 vault 설정 그대로 작동 보장 |
| 2026-05-16 | minAppVersion 1.6 유지 | 현재 사용자 분포 보호 |

## 참고

- [layer-migration-roadmap.md](layer-migration-roadmap.md) — 점진적 layer 도입 대안 (v3 from-scratch 채택으로 비활성화)
- [community-scanner-acknowledgments.md](community-scanner-acknowledgments.md) — v2.30 스캐너 경고 책임 매트릭스
- `dev/MAP/cm6-hit-routing-contract.md` — Live Preview hit-routing 계약 (S4의 기준)
- `dev/MAP/css-stabilization-checklist.md` — 안정화 체크리스트
