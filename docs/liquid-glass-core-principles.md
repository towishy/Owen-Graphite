# Owen Liquid Glass Core Principles

> 기준 샘플: [docs/liquid-glass-hover-study-sample.html](liquid-glass-hover-study-sample.html)  
> 참고 영상: `H:\VSCode-개발관련\리퀴드글래스 구현 예.mp4`  
> 적용 목적: 단순한 파란 hover 효과가 아니라, Owen Editor처럼 흰 유리막이 기본이고 hover 때 빛·깊이·선명도가 살아나는 공통 디자인 언어를 만든다.

## 1. 기본 재질은 색이 아니라 반투명 흰 유리다

Liquid Glass의 기본값은 파랑 카드가 아니라 `white frosted surface`다. 색은 배경 전체를 칠하는 용도가 아니라 rim, shadow, icon state, 아주 약한 tint에만 들어간다.

- Base: 흰색 72~94% opacity의 vertical gradient
- Tint: sky/mint/warm 계열을 8~18% 수준으로 제한
- Border: slate/sky rim을 얇게 두고, hover 전에도 유리 경계가 보이게 유지
- Dark mode: 검은 유리가 아니라 slate glass에 faint blue rim을 섞는다

## 2. hover는 색 변경보다 물성 변화가 먼저다

Hover의 핵심은 `더 파랗게`가 아니라 `더 밝고, 더 떠 있고, 더 단단한 유리로 보이는 것`이다.

- 배경: white highlight가 증가한다
- Border: sky rim이 조금 더 선명해진다
- Shadow: 아래 방향 soft shadow가 커진다
- Motion: 1~2px lift만 사용한다
- Icon/text: normal은 graphite/gray, hover/active에서만 기능별 pastel tone으로 얕게 바뀐다

## 3. 한 버튼 안에는 세 레이어가 필요하다

1. Surface layer: 흰색 반투명 gradient
2. Reflection layer: 상단/우상단 radial white highlight
3. Depth layer: inset highlight + 아래 soft shadow

이 세 레이어가 같이 있어야 영상처럼 `플라스틱 버튼`이 아니라 `가벼운 유리 버튼`으로 보인다.

## 4. 색상 패턴은 pastel rim 방식으로 통일한다

기본 상태는 색상이 아니라 graphite/gray frosted glass다. 아이콘별 색상 차이는 평소에 드러내지 않고, hover/active 순간에만 얕게 올라와야 Owen Graphite의 차분한 문서 UI와 충돌하지 않는다.

아이콘/버튼은 hover 때 모두 같은 파랑을 쓰지 않는다. 기능군별로 sky, mint, warm, violet, rose, emerald tint를 아주 옅게 다르게 배정하되, resting state의 공통 surface는 회색 톤의 흰 유리막으로 유지한다.

- Resting neutral rim: `rgba(203, 213, 225, 0.44~0.74)`
- Hover primary rim: `rgba(96, 165, 250, 0.38~0.62)`
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

## 7. 금지 규칙

- 기본 상태를 진한 cyan/blue 카드처럼 만들지 않는다.
- hover 때 과한 scale, 큰 이동, 과한 glow를 쓰지 않는다.
- 모든 요소에 같은 파란색을 칠하지 않는다.
- shadow 없이 border/background만 바꾸지 않는다.
- dark mode에서 pure black glass를 쓰지 않는다.

## 8. CSS 구현 공식

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
  linear-gradient(180deg, rgba(255, 255, 255, 0.98), rgba(239, 246, 255, 0.74));
border-color: rgba(96, 165, 250, 0.42);
box-shadow:
  inset 0 1px 0 rgba(255, 255, 255, 0.98),
  inset 0 -1px 0 rgba(96, 165, 250, 0.10),
  inset 0 0 16px rgba(255, 255, 255, 0.34),
  0 12px 24px rgba(15, 23, 42, 0.16);
transform: translateY(-2px);
```

## 9. 샘플

- HTML 샘플: [docs/liquid-glass-hover-study-sample.html](liquid-glass-hover-study-sample.html)
- 이 샘플은 기본 상태, hover 상태, 확장된 secondary toolbar, tooltip, pointer shadow까지 한 번에 비교하도록 만들었다.
