# Owen Graphite Liquid Glass Token Map

## Reference Order

| 우선순위 | 기준 | 사용 범위 |
|----------|------|----------|
| 1 | [liquid-glass-hover-study-sample.html](liquid-glass-hover-study-sample.html) | resting white/gray glass, hover lift, neutral icon/rim behavior |
| 2 | [fixtures/liquid-glass-core-state-matrix.html](fixtures/liquid-glass-core-state-matrix.html) | active/focus/rim/halo/shadow state hierarchy |
| 3 | [liquid-glass-core-principles.md](liquid-glass-core-principles.md) | 금지 규칙, 의미색 예외, 구현 체크리스트 |

## CSS Token Mapping

| 상태 | 기준 토큰 | CSS 변수 | 적용 원칙 |
|------|-----------|----------|-----------|
| Resting surface | white frosted surface | `--ogd-lg-surface-bg`, `--ogd-lg-control-bg` | graphite/white glass를 기본으로 두고 의미색을 면 전체에 칠하지 않는다 |
| Resting edge | slate rim | `--ogd-lg-edge`, `--ogd-lg-border` | 기본 상태에서도 유리 경계가 읽혀야 한다 |
| Hover surface | brighter glass + lift shadow | `--ogd-lg-surface-bg-hover`, `--ogd-lg-shadow-hover` | hover는 색상보다 밝기, 깊이, 그림자 변화가 먼저다 |
| Active state | shallow mist sky | `--ogd-lg-mist-fill`, `--ogd-lg-mist-rim`, `--ogd-lg-shadow-active` | active는 얕은 sky tint와 rim에 제한한다 |
| Focus state | Frost Aqua rim + halo | `--ogd-lg-frost-rim`, `--ogd-lg-frost-halo`, `--ogd-lg-shadow-focus` | keyboard focus는 layout shift 없이 aqua rim과 soft halo로 표시한다 |
| Table wiki mode | airy glass table | `--ogd-table-surface`, `--ogd-table-head-bg`, `--ogd-table-row-hover` | 위키 노트 표는 가볍고 부드러운 glass surface를 유지한다 |
| Table report mode | crisp document table | `--ogd-table-border`, `--ogd-table-cell-border`, `--ogd-table-shadow` | 보고서/PDF 표는 선명한 rule과 정보 위계를 우선한다 |

## Frost Aqua Focus Sweep

| 영역 | 대표 selector | 기대 상태 |
|------|---------------|-----------|
| Ribbon/toolbar | `.clickable-icon`, `.view-action`, `.editingToolbarButton` | Frost Aqua rim, no size shift |
| Navigation | `.nav-file-title`, `.nav-folder-title`, `.tree-item-self` | row surface hover + focus halo |
| Tabs | `.workspace-tab-header`, `.workspace-tab-header-inner` | neutral tab body, aqua focus rim only on keyboard focus |
| Search/modal input | `.search-input-container`, `.document-search-container`, `.prompt-input`, `.modal input` | control glass 유지, focus halo 추가 |
| Settings | `.setting-item`, `.metadata-property` | row 전체가 흔들리지 않고 focus-within 표시 |

## Maintenance Notes

- 새 liquid glass chrome은 먼저 이 문서의 reference order와 token mapping에 맞춘다.
- 반복 chrome의 resting state에는 sky/rose/violet 등 의미색을 넣지 않는다.
- active/focus 색은 rim, halo, inset line, 작은 badge에만 제한한다.
- README 대표 SVG를 수정할 때는 실제 CSS token 계층과 색 번짐 정도가 맞는지 함께 확인한다.