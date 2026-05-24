# v3 Live Preview Editability Contract

이 문서는 v3-rewrite가 Live Preview(CodeMirror 6, `.markdown-source-view.mod-cm6`)에서 **클릭→편집 라우팅**을 보존하기 위해 반드시 지켜야 하는 CSS 규칙의 요약이며, `dev/scripts/audit_v3_hit_routing.py`가 자동으로 강제합니다.

## 왜 이게 중요한가

Live Preview는 마우스 클릭을 CM6 라인/위젯으로 라우팅할 때 **plain CSS box geometry**를 사용합니다. 잘못된 요소에 vertical box가 생기면 인접 단락까지 hit target이 확장되어 사용자가 정확히 클릭한 위치가 아닌 위젯 내부로 캐럿이 들어갑니다. 결과는 "줄을 더블클릭해야 편집된다"는 사용자 보고입니다.

v2.22.99~108 사이에 같은 원인으로 7번 패치가 나갔습니다. v3-rewrite는 이 모든 hotfix를 **CSS 단계가 아닌 contract 단계에서** 회피해야 합니다.

## 금지 카테고리 (Hard ERROR)

다음은 절대 위반하면 안 됩니다. `dev/scripts/audit_v3_hit_routing.py`가 강제합니다.

### F1. 블록 위젯의 vertical margin

다음 selector를 **직접 타깃**으로 하는 규칙은 non-zero `margin`, `margin-top`, `margin-bottom`, `margin-block*`을 선언하면 안 됩니다.

- `.cm-callout`
- `.cm-table-widget`
- `.cm-embed-block.cm-callout`

블록 사이의 수직 리듬은 **CM6가 자동 삽입하는 빈 `.cm-line`**이 담당합니다. 수평 margin/padding은 OK.

### F2. HyperMD `.cm-line` vertical box

위와 같은 규칙 + padding 까지 금지됩니다.

- `.HyperMD-table-row`
- `.HyperMD-callout`
- `.HyperMD-codeblock`, `.HyperMD-codeblock-begin`, `.HyperMD-codeblock-end`

### F3. `.cm-line` 자체의 vertical margin

`.cm-line`에 직접 `margin-*`을 거는 것은 금지. 라인 간 간격은 `line-height` 토큰으로만 조절.

### F4. `transform: translate(...)` 가 vertical 성분을 갖는 경우

블록 위젯에 `transform: translate(0, -2px)` 같은 미세 보정 금지. 클릭 hit-box는 transform 이전 좌표로 계산되어 라우팅이 어긋남.

### F5. `pointer-events: none` 누락된 overlay layer

장식 목적의 overlay(::before/::after)에 `pointer-events: none`이 빠지면 클릭을 가로챔. v3에서 추가하는 모든 장식 overlay는 자동으로 `pointer-events: none`이어야 함.

## 권장 카테고리 (Soft 권고)

### S1. 블록 위젯 안쪽 정렬은 `padding`으로

`.cm-callout > .callout-title { padding-block: ... }`는 OK. `.cm-callout { padding-block: ... }`도 OK (블록 위젯 자체에 거는 padding은 hit-box 안쪽에 머무름).

### S2. 위젯 사이 시각적 간격은 `.cm-line` line-height로

블록 위젯 사이를 더 떨어뜨리고 싶다면 빈 `.cm-line`의 `line-height`(또는 `min-height`)를 늘리는 방향으로. 위젯 자체에 margin을 거는 방향은 금지.

### S3. 위젯 호버 효과는 `transform: scale()` 또는 `box-shadow`로

`transform: scale(1.005)`는 OK(중심이 동일하므로 hit-box 중심 변화 없음). `transform: translateY(...)`는 금지(F4).

## v3-rewrite 작업 시 점검 항목

v3 작업자가 새 CSS를 작성할 때 다음을 확인해야 합니다.

| 항목 | 검사 방법 |
| --- | --- |
| 블록 위젯에 vertical margin 없음 | `grep -E '\.cm-(callout\|table-widget\|embed-block).*\{[^}]*margin' src/` |
| HyperMD line에 vertical box 없음 | `grep -E '\.HyperMD-.*\{[^}]*(margin\|padding)-(top\|bottom\|block)' src/` |
| Overlay layer에 `pointer-events: none` | `grep -B 3 '::before\|::after' src/` 검토 |
| vertical transform 없음 | `grep -E 'transform:\s*translate(Y)?\([^,)]+,\s*-?[0-9]' src/` |

이 4개 자동 검사가 `dev/scripts/audit_v3_hit_routing.py`의 `live_preview_hit_routing_audit`에 이미 구현되어 있어, v3 작업도 동일 검증을 통과해야 합니다.

## 검증 도구

### C4 보존 계약 (Live Preview hit-routing)

- `dev/scripts/audit_v3_hit_routing.py` (v3) — `dist/theme-v3.css` 번들을 파싱해서 위 금지 카테고리를 자동 검사. CI와 pre-commit hook에서 모두 실행.
- (선택) 수동 세션: light/dark × report-mode on/off 조합으로 콜아웃·표·코드블록 위/아래 단락에서 클릭→caret 위치 육안 확인.

### 회귀 매트릭스

| 시나리오 | 기대 동작 |
| --- | --- |
| 콜아웃 위 단락 끝을 클릭 | 단락 끝 caret |
| 콜아웃 아래 단락 시작을 클릭 | 단락 시작 caret |
| 표 위젯 위 단락 끝을 클릭 | 단락 끝 caret |
| 표 위젯 아래 단락 시작을 클릭 | 단락 시작 caret |
| 코드블록 안 특정 줄 클릭 | 그 줄 caret |
| 콜아웃 내부 특정 줄 클릭 | 그 줄 caret |
| 임베드 블록 아래 빈 줄 클릭 | 빈 줄 caret |

각 시나리오는 light/dark, report-mode on/off 4조합으로 검증됩니다.

## 비고

- v2.30.x에서 누적된 hit-routing hotfix는 모두 위 금지 카테고리를 **사후 보정**한 결과입니다. v3-rewrite는 이를 **사전 회피**하므로 hotfix 자체가 발생하지 않아야 합니다.
- 만약 v3에서 새로운 hit-routing 회귀가 발생한다면, 그것은 위 contract가 불완전하다는 증거이므로 **본 문서와 `dev/scripts/audit_v3_hit_routing.py` 명세를 동시에 업데이트**해야 합니다.
