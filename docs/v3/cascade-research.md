# 캐스케이드 전략 검증 — Obsidian core 대 v3 theme

**작성일**: S3.1 직후 (피벗 사후 검증).
**상태**: 확정. 실증적 근거 확보.
**관련 결정**: design-spec.md "캐스케이드 전략 — 파일 순서 + 선택자 특이도".

## 1. 사실 (직접 확인)

`C:\Program Files\Obsidian\resources\obsidian.asar`을 `@electron/asar`로 추출하여 `app.css`(600 KB, 20,018줄)를 검사:

| 항목 | 개수 | 위치 요약 |
|---|---|---|
| `@layer` 선언 | **0** | 없음 |
| `!important` | **66** | print(`@media print`) 3060~3120, `forced-colors` 1145~1170, scrollbar 숨김, pdf popover, 일부 chrome utility |

**결론**: Obsidian core CSS는 **unlayered**이며, **!important 사용량이 극히 적다(66)**. 5,816개 !important를 쓰는 v2.30.14는 core와 싸우는 것이 아니라 **자기 자신과 싸우고 있다**.

검증 스크립트: `scripts/probe_cascade_behavior.py`.

## 2. CSS Cascading Level 5 — 정확한 규칙

> Sort order (later items decide first when prior items are tied):
> 1. **Origin and importance**
> 2. **Context** (encapsulation)
> 3. Element-attached styles
> 4. **Layers** (within same origin and importance)
> 5. **Specificity**
> 6. Order of appearance

**핵심**: 레이어 비교는 **특이도보다 앞**에서 이루어진다. 같은 origin/importance 내에서:

- unlayered ⟶ implicit "outermost" layer로 취급되며, **모든 named layer를 이긴다**.
- 따라서 theme이 `@layer` 안에 있고 core가 unlayered면, **특이도가 아무리 높아도 core가 이긴다**.
- 단 `!important`는 layer 순서를 **역전**시킨다(중요도 우선).

## 3. 실증 — Playwright 행동 시험

`scripts/probe_cascade_behavior.py`가 6개 시나리오를 측정한다. core를 흉내낸 fake CSS는 unlayered로, theme은 각 시나리오마다 다르게 구성한다.

| # | 시나리오 | font-size 결과 | color 결과 | 승자 |
|---|---|---|---|---|
| 1 | theme **unlayered**, 같은 특이도(`p` vs core의 `.cm-line p`) | 12px | rgb(136,136,136) | core |
| 2 | theme **layered**, 같은 특이도 | 12px | rgb(136,136,136) | core |
| 3 | theme **layered + !important** | 20px | rgb(255,0,0) | **theme** |
| 4 | theme **layered, 더 높은 특이도** | 12px | rgb(136,136,136) | **core** ← 결정적 |
| 5 | theme **unlayered**, 같은 특이도, 뒤에 선언 | 20px | rgb(255,0,0) | **theme** |
| 6 | theme **unlayered, 더 높은 특이도** | 20px | rgb(255,0,0) | **theme** |

**시나리오 4가 피벗을 강제하는 근거**: theme이 `body.theme-light .x` 같은 더 높은 특이도를 가져도, `@layer` 안에 있으면 unlayered core의 더 낮은 특이도 룰에 패배한다. 이 상태에서 theme이 이기는 길은 `!important`뿐이며, 그러면 layer를 도입한 의미(낮은 우선순위에서 시작해 점진적으로 강화)가 사라진다.

## 4. v3 캐스케이드 결정 — 확정

1. **v3 theme은 unlayered**. `src/entry.css`의 `@import`는 plain import, `layer(name)` 어노테이션 없음.
2. **우선순위 도구는 특이도 + 파일 순서**. 시나리오 5·6이 보장.
3. **`!important`는 다음 두 경우에만 허용**:
   - core 본인이 `!important`를 사용한 66개 위치 중 하나와 직접 충돌.
   - Style Settings 토글이 사용자 의도를 즉시 표현해야 할 때.
4. v2.30.14의 5,816 `!important` 중 대부분은 **자기 자신과 싸우는 잔재**다. S11에서 다음 휴리스틱으로 정리한다:
   - `!important` 룰을 임시 제거 → 시각적 변화 없음 → 영구 제거.
   - 변화 발생 → 어떤 다른 룰과 싸웠는지 추적 → 그 룰의 특이도를 조정해 자연스럽게 정렬.
   - core나 Style Settings와 직접 충돌 시 유지.
5. **수치 목표**: v3 최종 `!important` ≤ 100 (core의 66 + Style Settings 토글 여유분).

## 4.1 S11.5 — 휴리스틱 실증 결과 (목표 ≤100 → 실측 0)

S11.5에서 §4의 휴리스틱을 자동화하여 일괄 적용했다.

**자동화 절차** (`scripts/v3_strip_important.py`, `scripts/v3_strip_important_src.py`):

1. **번들 sanity 테스트**: `dist/theme-v3.css`에서 모든 `!important` 5,821개를 정규식으로 제거 → 임시 번들 생성.
2. **fingerprint 측정**: 55 element × 51 property × {light, dark} = 5,610 cell.
3. **충돌 셀만 추적**: baseline과 다른 cell만 §4-2의 "원인 추적" 대상이 된다.

**결과**:

| 측정 | 값 |
| --- | ---: |
| 제거 대상 `!important` | 5,821 |
| fingerprint 셀 미스매치 (light) | 8 |
| fingerprint 셀 미스매치 (dark) | 1 |
| 유일 충돌 element | `a.external-link` 1개 |

**원인**: `src/base/12` (teal resting state, 특이도 0,3,1) 과 `src/polish/70` (slate baseline, 특이도 0,2,1) 이 같은 selector에서 충돌. polish/70의 `!important`만이 슬레이트 색을 강제했고, 그것이 v2.30.14 baseline. 즉 base/12의 teal 룰은 _죽은 코드_였다.

**해결**: base/12 resting 색을 slate로 정렬(hover는 teal 유지). 특이도 충돌 해소 → polish/70의 `!important` 불필요.

**일괄 제거 후 재측정**:

| 측정 | 값 |
| --- | ---: |
| `src/`의 declaration-level `!important` | **0** |
| `dist/theme-v3.css`의 declaration-level `!important` | **0** (주석 내 토큰 4건 보존) |
| fingerprint 미스매치 (light/dark) | **0 / 0** |
| 번들 라인 수 | 16,509 |
| hit-routing audit | clean |
| v2 invariants | pass |

**결론**: §4-5의 수치 목표 ≤100을 갱신한다. 새 목표 = **0 (declaration level)**. 주석 내 인용은 보존하여 역사적 맥락 유지. 자세한 절차는 `/memories/repo/v3-important-strategy.md` 참조.

**참고**: harness는 resting 상태 55개 element만 다룬다. hover/focus, plugin widget, dataview, canvas/graph 상태는 사용자 vault 검증으로 확인했다 (2026-05-16, 사용자 confirm).

## 5. 다음 단계 검증 — 매 단계 회귀

각 Sx 단계 종료 시 다음을 측정한다:

- `dist/theme-v3.css` 내 `!important` 개수.
- `docs/v3/computed-fingerprint-v2.30.14-v3-{light,dark}.json` 미스매치 추이.
- 로컬 Obsidian 볼트에서 실제 노트로 spot-check.

## 6. 재현 절차

```powershell
# 1. obsidian.asar 추출 (재확인용)
mkdir $env:TEMP\obsidian-asar-extract -Force | Out-Null
cd $env:TEMP\obsidian-asar-extract
& 'C:\Program Files\nodejs\npx.cmd' --yes @electron/asar extract `
  'C:\Program Files\Obsidian\resources\obsidian.asar' .

# 2. core CSS에서 @layer, !important 카운트
$css = Get-Content .\app.css -Raw
([regex]::Matches($css, '@layer')).Count       # → 0
([regex]::Matches($css, '!important')).Count   # → 66

# 3. 캐스케이드 행동 실증
cd h:\owen-graphite
.\.venv\Scripts\python.exe scripts\probe_cascade_behavior.py
```
