# v3 Surface State Matrix

Owen Graphite의 모든 Liquid Glass surface가 가질 수 있는 상태와 각 상태의 토큰 매핑을 정의합니다. v3-rewrite는 이 표대로 토큰을 선언하고 사용해야 합니다.

원본 디자인 의도는 `docs/liquid-glass-core-principles.md`와 `dev/MAP/top-chrome-icon-background-contract.md`에 있습니다. 이 문서는 그 의도를 **v3 토큰 매핑 표**로 압축합니다.

## 공통 디자인 원칙 (사용자 요청)

- **Resting state**: 흰색/회색 frosted glass (white/gray frost)
- **Hover state**: 약간 밝아지고 들어 올려짐(lift), 더 큰 부드러운 그림자, **얕은 파스텔 톤만** 살짝
- **Active state**: 단 하나의 sky pastel — 명확한 sky tint + glass border
- **Disabled state**: 채도·alpha 50% 감소, 그림자 제거
- **금지**: 좌측 vertical accent line/rail 사용 금지
- **요구**: 1px graphite rim + top white shine + wide soft shadow + internal reflection layer

## 상태별 토큰 명세

### Rest (기본)

| 토큰 | 책임 | 권장 값 (light) | 권장 값 (dark) |
| --- | --- | --- | --- |
| `--ogd-glass-rest-surface` | 표면 그라데이션 | `linear-gradient(180deg, #ffffff 0%, #f8fafc 100%)` | `linear-gradient(180deg, rgba(30,41,59,0.78) 0%, rgba(15,23,42,0.62) 100%)` |
| `--ogd-glass-rest-rim` | 1px 외곽선 | `rgba(214, 220, 229, 0.82)` | `rgba(148, 163, 184, 0.22)` |
| `--ogd-glass-rest-shine` | 상단 흰 광선 | `inset 0 1px 0 rgba(255, 255, 255, 0.86)` | `inset 0 1px 0 rgba(255, 255, 255, 0.08)` |
| `--ogd-glass-rest-shadow` | 외곽 그림자 | `0 10px 28px rgba(15, 23, 42, 0.06)` | `0 12px 30px rgba(0, 0, 0, 0.32)` |
| `--ogd-glass-rest-filter` | backdrop filter | `blur(12px) saturate(152%) contrast(103%)` | `blur(12px) saturate(140%) contrast(101%) brightness(1.02)` |

### Hover (마우스 hover)

| 토큰 | 책임 | 권장 값 (light) | 권장 값 (dark) |
| --- | --- | --- | --- |
| `--ogd-glass-hover-surface` | 더 밝은 그라데이션 | `linear-gradient(180deg, #ffffff 0%, #f1f5f9 100%)` | `linear-gradient(180deg, rgba(51,65,85,0.82) 0%, rgba(30,41,59,0.66) 100%)` |
| `--ogd-glass-hover-rim` | rim은 동일 또는 살짝 진하게 | `rgba(203, 213, 225, 0.92)` | `rgba(148, 163, 184, 0.30)` |
| `--ogd-glass-hover-shine` | shine은 그대로 | (rest 동일) | (rest 동일) |
| `--ogd-glass-hover-shadow` | 더 큰 부드러운 그림자 | `0 18px 40px rgba(15, 23, 42, 0.10)` | `0 18px 44px rgba(0, 0, 0, 0.40)` |
| `--ogd-glass-hover-pastel` | hover 시 살짝 들어가는 파스텔 alpha | sky / mint / warm / violet / rose / emerald 중 하나, alpha < 0.10 | 동일, alpha < 0.14 |

### Active (단 하나의 sky pastel)

활성 상태는 **테마 전체에서 동시에 하나만** 존재합니다(예: 현재 활성 탭, 현재 활성 폴더, 현재 활성 콜아웃). 색은 **sky pastel 한 종**.

| 토큰 | 책임 | 권장 값 (light) | 권장 값 (dark) |
| --- | --- | --- | --- |
| `--ogd-glass-active-tint` | sky tint 배경 | `rgba(186, 230, 253, 0.32)` | `rgba(56, 189, 248, 0.18)` |
| `--ogd-glass-active-rim` | 명확한 sky border | `rgba(125, 211, 252, 0.62)` | `rgba(125, 211, 252, 0.50)` |
| `--ogd-glass-active-shine` | shine 강화 | `inset 0 1px 0 rgba(255, 255, 255, 0.96)` | `inset 0 1px 0 rgba(255, 255, 255, 0.14)` |
| `--ogd-glass-active-shadow` | 그림자 살짝 더 큼 | `0 18px 40px rgba(56, 189, 248, 0.12)` | `0 18px 44px rgba(56, 189, 248, 0.22)` |
| `--ogd-glass-active-text` | 텍스트 색 강화 | `#0c4a6e` | `#e0f2fe` |

### Disabled

| 토큰 | 책임 | 권장 값 (light) | 권장 값 (dark) |
| --- | --- | --- | --- |
| `--ogd-glass-disabled-surface` | alpha 50% | `linear-gradient(180deg, rgba(255,255,255,0.5), rgba(248,250,252,0.4))` | `linear-gradient(180deg, rgba(30,41,59,0.40), rgba(15,23,42,0.30))` |
| `--ogd-glass-disabled-rim` | rim alpha 50% | `rgba(214, 220, 229, 0.40)` | `rgba(148, 163, 184, 0.12)` |
| `--ogd-glass-disabled-shadow` | 그림자 제거 | `none` | `none` |
| `--ogd-glass-disabled-text` | 텍스트 채도 감소 | `#94a3b8` | `#475569` |

## Surface 카테고리별 적용

위 토큰을 다음 surface 종류에 어떻게 매핑할지:

| Surface | rest | hover | active | disabled |
| --- | --- | --- | --- | --- |
| **카드 (workspace tab, file explorer item)** | glass-rest 전체 | glass-hover | active 또는 그냥 hover | disabled |
| **버튼 (toolbar button, view header action)** | glass-rest | glass-hover + pastel alpha 0.06 | active(눌린 상태일 때) | disabled |
| **콜아웃** | callout-bg (별도 token) | (콜아웃은 hover 변화 거의 없음) | active(현재 caret 위치) | — |
| **메뉴 항목 (overlay)** | rest | hover + 약간 짙은 surface | (메뉴는 active 없음, focused만) | disabled |
| **표 셀** | rest 또는 zebra | hover row | — | — |
| **코드 블록** | codeblock-bg (별도) | (hover 없음) | — | — |
| **링크 카드 (embed)** | rest | hover + lift | — | — |

## Active 상태의 단일성 강제

"단 하나의 sky pastel" 원칙을 보장하기 위해, v3에서는 다음 셀렉터에만 active surface 토큰을 적용합니다.

- `.workspace-tab-header.is-active`
- `.nav-folder-title.is-active`
- `.nav-file-title.is-active`
- `.suggestion-item.is-selected`
- `.tree-item-self.is-active`
- `.cm-active.cm-line` (현재 캐럿 라인)
- (콜아웃 안의) `.cm-callout:has(.cm-active.cm-line)` — `:has()` 가드는 `@supports selector(:has(*))`로 감쌈

다른 곳에서 active surface 토큰을 쓰는 것은 PR 리뷰 단계에서 차단.

## 회귀 검증

S1의 골든 이미지 매트릭스가 각 surface × 각 상태를 모두 캡처합니다(예상 16~24 시나리오). v3-rewrite의 각 step은 그 슬라이스만큼 통과해야 합니다.
