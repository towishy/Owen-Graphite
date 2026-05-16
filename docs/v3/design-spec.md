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
| C1 | 시각 (Liquid Glass + 일반 surface) | `scripts/capture_computed_fingerprint.py` + `scripts/fp_diff_summary.py` | computed-style fingerprint diff = 0 (Light / Dark) |
| C2 | 색 대비 (WCAG) | 수동 샘플 + Style Settings 토글 매트릭스 | 30+ 쌍 모두 AA 이상 (베이스라인 v2.30.14와 동일) |
| C3 | Style Settings 동작 | 토글 매트릭스 캡처 | 37개 옵션 × ON/OFF = 74 cell 동일 |
| C4 | Live Preview 편집성 | `scripts/audit_v3_hit_routing.py` | violations = 0 |
| C5 | PDF 출력 | print 시나리오 PDF 비교 | 페이지 수·레이아웃·footer 동일 |

각 계약의 매트릭스는 별도 문서에 상세화됩니다 (아래 "참조 문서" 표 참고).

## 아키텍처 결정

### 캐스케이드 전략 — 파일 순서 + 선택자 특이도

v3는 `@layer`를 본문 룰에 사용하지 **않습니다**. CSS Cascade Layers 스펙상 unlayered styles가 layered styles를 항상 이기는데, Obsidian core CSS(`app.css`)가 unlayered이기 때문입니다. theme 룰을 `@layer` 안에 두면 core에 패배하여 `!important`로만 되돌릴 수 있고, 이는 v3의 목표(!important 감축)와 모순됩니다.

**이 결정은 사후 실증 검증을 거쳤습니다.** `obsidian.asar`에서 추출한 `app.css`(600 KB)를 직접 검사한 결과 `@layer` 0개, `!important` 66개(대부분 print/forced-colors 영역). 또한 Playwright 캐스케이드 시험(`scripts/probe_cascade_behavior.py`)에서 theme이 더 높은 특이도를 가져도 `@layer` 안에 들어가면 unlayered core에 패배함을 확인했습니다. 전체 근거는 `docs/v3/cascade-research.md` 참고.

따라서 v3 본문 룰은 **unlayered** 상태로 유지합니다. 캐스케이드 도구는 다음 셋입니다:

1. **`@import` 파일 순서** — 같은 특이도에서 뒤에 import 된 파일이 승리. tokens → base → surfaces → chrome → features → dark → a11y 순서가 의미를 가집니다.
2. **선택자 특이도** — `body.theme-light`, `.theme-light :is(...)` 같은 고특이도 prefix가 Obsidian core를 이깁니다. 이것은 v2.30.14가 이미 사용하던 패턴이며 v3에서도 유지합니다.
3. **잔여 `!important`** — Obsidian core 자체가 `!important`를 거는 곳에서만 허용. 감축은 S11 polish 단계의 별도 책임입니다.

`src/` 폴더 구조 (`tokens/`, `base/`, `surfaces/`, `chrome/`, `features/`, `themes/`, `plugins/`)는 가독성·선택자 provenance 감사를 위한 **조직적 약속**일 뿐이며, 캐스케이드 의미를 갖지 않습니다.

```css
/* src/entry.css */
@import url("./tokens/00-light-tokens.css");
@import url("./tokens/01-dark-tokens.css");
@import url("./base/10-base-workspace.css");
/* ... */
```

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

- v3는 v2.30.14의 5,816개를 한 번에 0으로 떨어뜨리려 하지 않습니다. S3~S10에선 dev/*를 src/*로 옮기는 "정확성 유지" 작업을 우선합니다.
- S11(polish)에서 다음을 수행합니다:
  1. 선택자 특이도가 이미 충분히 높은데 `!important`가 붙은 룰 → 제거
  2. 같은 토큰을 여러 모듈에서 재정의하는 중복 룰 → 단일 source-of-truth 모듈로 통합
  3. Obsidian core 자체가 `!important`를 거는 위치에 대한 `!important` → 인라인 주석에 "defeats core <selector>" 명시 후 유지
- 목표는 "두 자릿수"가 아니라 "필요한 곳에만 명시적 주석으로 남는 모든 `!important`"입니다. 결과 수치는 측정 후 보고합니다.

**S11.5 결과 (2026-05-16)**: `src/` declaration-level `!important` = **0**. 자세한 실증·휴리스틱·일괄 제거 절차는 [cascade-research.md §4.1](cascade-research.md#41-s115--휴리스틱-실증-결과-목표-100--실측-0) 참조. 위 정책 1번은 자동화 절차로 100% 달성, 2번은 S11.7에서 별도 검토, 3번은 0개라서 N/A.

## 참조 문서 (S0 산출물)

| 문서 | 책임 |
| --- | --- |
| [token-inventory.md](token-inventory.md) | v2.30.14 토큰 이름·기본값 contract (255 tokens) |
| [style-settings-contract.md](style-settings-contract.md) | Style Settings 37개 옵션 이름·동작 표 |
| [surface-state-matrix.md](surface-state-matrix.md) | Liquid Glass rest/hover/active/disabled 정의표 |
| [live-preview-editability.md](live-preview-editability.md) | hit-routing 보존 contract |
| [golden-image-scenarios.md](golden-image-scenarios.md) | 66 시각 회귀 시나리오 목록 |

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
| 2026-05-16 (S3) | `@layer` 폐기, 파일 순서+특이도 채택 | unlayered Obsidian core가 layered theme을 이기는 CSS spec 한계 발견. `!important`로만 되돌릴 수 있어 v3 목표와 모순됨. |
| 2026-05-16 (S3) | dev/* → src/* 단계적 이관, !important 감축은 S11에 일임 | 정확성(fingerprint diff=0)을 먼저 보장한 뒤 polish 단계에서 감축하는 strangler 패턴. |

## 참고

- [release-plan.md](release-plan.md) — v3.0.0 릴리즈 기록·투체인·절차
- [cascade-research.md](cascade-research.md) — unlayered 캐스케이드 실증·S11.5 `!important` 일괄 제거 결과
- [surface-state-matrix.md](surface-state-matrix.md) — Liquid Glass rest/hover/active/disabled 정의
- [live-preview-editability.md](live-preview-editability.md) — hit-routing 계약 (v3 구현: `scripts/audit_v3_hit_routing.py`)
