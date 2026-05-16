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
