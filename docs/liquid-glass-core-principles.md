# Owen Liquid Glass Core Principles

> 기준 샘플: [docs/liquid-glass-hover-study-sample.html](liquid-glass-hover-study-sample.html)  
> 참고 영상: 로컬 Liquid Glass hover reference video  
> 적용 목적: 단순한 파란 hover 효과가 아니라, Owen Editor처럼 흰 유리막이 기본이고 hover 때 빛·깊이·선명도가 살아나는 공통 디자인 언어를 만든다. 반복 UI chrome은 graphite/slate glass를 기본으로 하며, 색상은 의미가 있을 때만 제한적으로 사용한다.

## 1. 기본 재질은 색이 아니라 반투명 흰 유리다

Liquid Glass의 기본값은 파랑 카드가 아니라 `white frosted surface`다. 반복되는 버튼, 행, 닫기 아이콘, 패널 chrome은 graphite/slate 계열 유리막을 기본으로 한다. 색은 배경 전체를 칠하는 용도가 아니라 의미 있는 상태의 rim, icon state, 아주 약한 tint에만 들어간다.

- Base: 흰색 72~94% opacity의 vertical gradient
- Tint: 반복 chrome에서는 slate 중심으로 유지하고, 의미색은 4~12% 수준의 얕은 rim/tint로 제한
- Border: slate rim을 기본으로 두고, hover 전에도 유리 경계가 보이게 유지
- Dark mode: 검은 유리가 아니라 slate glass에 neutral rim을 섞는다

## 2. hover는 색 변경보다 물성 변화가 먼저다

Hover의 핵심은 `더 파랗게`가 아니라 `더 밝고, 더 떠 있고, 더 단단한 유리로 보이는 것`이다.

- 배경: white highlight가 증가한다
- Border: slate rim이 조금 더 선명해진다
- Shadow: 아래 방향 soft shadow가 커진다
- Motion: 1~2px lift만 사용한다
- Icon/text: normal은 graphite/gray, hover/active도 반복 chrome에서는 graphite/slate를 유지한다. 링크, callout, task, warning, destructive button처럼 의미가 있는 경우에만 기능별 pastel tone을 얕게 허용한다

## 3. 한 버튼 안에는 세 레이어가 필요하다

1. Surface layer: 흰색 반투명 gradient
2. Reflection layer: 상단/우상단 radial white highlight
3. Depth layer: inset highlight + 아래 soft shadow

이 세 레이어가 같이 있어야 영상처럼 `플라스틱 버튼`이 아니라 `가벼운 유리 버튼`으로 보인다.

## 3-1. Liquid Glass 구현 체크리스트

새 Liquid Glass 표면을 만들거나 기존 표면을 강화할 때는 다음 원칙을 우선 적용한다.

- 패널 rim은 기본 상태에서도 유리 경계가 읽히도록 선명하게 둔다.
- 상단 shine 곡선은 DOM/CSS 제약이 허용되는 요소에 추가한다.
- 카드 shadow는 작고 진한 그림자보다 넓고 부드러운 하강 그림자로 만든다.
- 내부 glass 반사 레이어를 radial highlight 또는 inset shine으로 추가한다.
- active 카드는 sky tint와 glass border를 resting/hover보다 더 또렷하게 둔다.
- 좌측 세로 라인/rail은 사용하지 않는다. 계층, 선택, 강조는 border, halo, icon, chip, surface state로 표현한다.

## 4. 색상 패턴은 pastel rim 방식으로 통일한다

기본 상태는 색상이 아니라 graphite/gray frosted glass다. 아이콘별 색상 차이는 평소에 드러내지 않고, hover/active 순간에도 반복 chrome에서는 최대한 slate 계열로 남겨야 Owen Graphite의 차분한 문서 UI와 충돌하지 않는다.

아이콘/버튼은 hover 때 모두 같은 파랑을 쓰지 않는다. 단순 열기/닫기/전환/선택/탐색 같은 반복 chrome은 graphite/slate glass로 통일한다. 기능군별 sky, mint, warm, violet, rose, emerald tint는 의미가 있는 상태에만 아주 옅게 배정하고, resting state의 공통 surface는 회색 톤의 흰 유리막으로 유지한다.

- Resting neutral rim: `rgba(203, 213, 225, 0.44~0.74)`
- Hover neutral rim: `rgba(100, 116, 139, 0.28~0.42)` light, `rgba(203, 213, 225, 0.18~0.28)` dark
- Semantic sky rim: `rgba(96, 165, 250, 0.24~0.42)` only for links/search/task-like meaning
- Mint accent: `rgba(153, 246, 228, 0.30~0.42)`
- Warm accent: `rgba(253, 230, 138, 0.34~0.46)`
- Violet accent: `rgba(196, 181, 253, 0.34~0.52)`
- Rose accent: `rgba(254, 205, 211, 0.34~0.54)`
- Emerald accent: `rgba(167, 243, 208, 0.34~0.54)`
- Surface white: `rgba(255, 255, 255, 0.72~0.98)`

## 5. 그림자는 hover의 가장 중요한 신호다

영상의 hover는 outline보다 shadow 변화가 더 크게 느껴진다. 따라서 hover shadow는 작고 진한 그림자보다 넓고 부드러운 그림자가 맞다.

- Resting shadow: `0 4px 10px rgba(15, 23, 42, 0.08~0.12)`
- Hover shadow: `0 12px 24px rgba(15, 23, 42, 0.14~0.18)`
- Floating toolbar/container: `0 18px 38px rgba(15, 23, 42, 0.14~0.18)`

## 6. 적용 우선순위

1. Floating controls: ribbon, graph controls, toolbar buttons, popovers
2. Repeated interactive rows: backlinks/outgoing/search rows
3. Active selected state: current tool, current file path, selected action
4. Dense document surfaces: 너무 강한 hover lift를 피하고 rim/brightness 중심으로 적용

## 7. 의미색 예외

다음은 색상 사용을 허용한다. 단, 면을 강하게 채우는 대신 얕은 rim, icon color, underline, small badge, semantic callout tone에 제한한다.

- 링크, unresolved link, code syntax, search highlight
- callout type, task marker, graph data color처럼 정보 자체를 색으로 구분하는 요소
- 실제 warning/destructive/CTA 버튼처럼 사용자가 행동의 성격을 즉시 알아야 하는 요소
- 리포트/프린트 전용 상태 배지처럼 문서 의미를 표시하는 요소

단순 닫기 버튼, 선택 행, 탐색 항목, 일반 toolbar icon, modal suggestion row는 destructive/warning 색을 쓰지 않는다.

## 8. 금지 규칙

- 기본 상태를 진한 cyan/blue 카드처럼 만들지 않는다.
- hover 때 과한 scale, 큰 이동, 과한 glow를 쓰지 않는다.
- 모든 요소에 같은 파란색을 칠하지 않는다.
- 단순 닫기/선택/탐색 chrome에 red/rose 같은 destructive 색을 쓰지 않는다.
- shadow 없이 border/background만 바꾸지 않는다.
- dark mode에서 pure black glass를 쓰지 않는다.

## 9. CSS 구현 공식

```css
/* resting */
background:
  radial-gradient(circle at 74% 24%, rgba(255, 255, 255, 0.70), transparent 36%),
  linear-gradient(180deg, rgba(255, 255, 255, 0.92), rgba(248, 250, 252, 0.62));
border: 1px solid rgba(203, 213, 225, 0.58);
box-shadow:
  inset 0 1px 0 rgba(255, 255, 255, 0.96),
  inset 0 -1px 0 rgba(15, 23, 42, 0.06),
  0 4px 10px rgba(15, 23, 42, 0.10);
backdrop-filter: blur(14px) saturate(155%);
```

```css
/* hover */
background:
  radial-gradient(circle at 74% 24%, rgba(255, 255, 255, 0.82), transparent 36%),
  linear-gradient(180deg, rgba(255, 255, 255, 0.98), rgba(248, 250, 252, 0.74));
border-color: rgba(100, 116, 139, 0.36);
box-shadow:
  inset 0 1px 0 rgba(255, 255, 255, 0.98),
  inset 0 -1px 0 rgba(15, 23, 42, 0.08),
  inset 0 0 16px rgba(255, 255, 255, 0.34),
  0 12px 24px rgba(15, 23, 42, 0.16);
transform: translateY(-2px);
```

## 10. 샘플

- HTML 샘플: [docs/liquid-glass-hover-study-sample.html](liquid-glass-hover-study-sample.html)
- 이 샘플은 기본 상태, hover 상태, 확장된 secondary toolbar, tooltip, pointer shadow까지 한 번에 비교하도록 만들었다.
