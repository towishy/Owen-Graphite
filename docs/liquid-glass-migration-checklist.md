# Liquid Glass Core Migration Checklist

> 기준 문서: [liquid-glass-core-principles.md](liquid-glass-core-principles.md)  
> 기준 샘플: [liquid-glass-hover-study-sample.html](liquid-glass-hover-study-sample.html)

이 문서는 기존 Owen Graphite CSS를 새 코어 원칙에 맞춰 하나씩 리뷰하고 적용하기 위한 작업 목록입니다.

## 코어 원칙 요약

- Resting: white/gray frosted glass, graphite/gray icon and rim.
- Hover/Active: only then add shallow per-control pastel tone.
- 색은 면 전체를 칠하지 않고 icon, rim, inset, very shallow shadow에 얹는다.
- Hover는 색 변경보다 brightness, lift, depth shadow 변화가 먼저다.
- 한 번에 전역 치환하지 않고, 시각 범위가 좁은 selector부터 적용한다.

## 이미 기준에 가까운 영역

| 상태 | 파일 | 이유 |
|---|---|---|
| 유지 | [dev/09a-nav-ribbon-glass.css](../dev/09a-nav-ribbon-glass.css) | Ribbon glass icon은 resting gray glass와 hover lift/rim 구조가 이미 기준에 가깝다. |
| 유지 | [dev/09c-floating-ui-glass-system.css](../dev/09c-floating-ui-glass-system.css) | 공통 `--ogd-glass-*` 토큰 소유자. 다만 일부 hover token의 색 배경은 추후 얕게 조정할 수 있다. |
| 유지 | [dev/09d-tabs-file-explorer-search.css](../dev/09d-tabs-file-explorer-search.css) | Tab/file explorer/search surface는 대부분 white/gray glass 중심이다. |
| 유지 | [dev/07d-canvas-graph-link-panes.css](../dev/07d-canvas-graph-link-panes.css) | v2.22.21 graph controls/backlink rows는 이미 새 샘플 원칙에 맞춰 조정된 편이다. |

## 리뷰/적용 후보

| 우선순위 | 상태 | 파일 | 대상 | 리뷰 포인트 | 권장 적용 |
|---|---|---|---|---|---|
| 1 | 적용 | [dev/07-plugin-workspace.css](../dev/07-plugin-workspace.css), [dev/05-live-preview.css](../dev/05-live-preview.css), [dev/10b-late-reading-nav-polish.css](../dev/10b-late-reading-nav-polish.css) | Internal-link chip | Reading view 배경은 `07-plugin`, CM6 Live Preview는 `05-live-preview`, 최종 텍스트 색은 `10b`가 소유 | Resting neutral gray chip, hover-only shallow sky rim/text 적용 |
| 2 | 검토 완료 | [dev/10b-late-reading-nav-polish.css](../dev/10b-late-reading-nav-polish.css) | Late reading internal/external link polish | 최근 override가 실제 최종 적용 owner임을 확인 | 내부 링크 최종 텍스트 색을 resting graphite, hover sky로 조정 |
| 3 | 적용 | [dev/07d-canvas-graph-link-panes.css](../dev/07d-canvas-graph-link-panes.css) | Canvas selected node, graph node/line highlight | `#6366f1` indigo가 강하게 보이던 상태 | Canvas selected/edge/graph highlight를 pastel violet/sky rim·stroke 중심으로 완화 |
| 4 | 적용 | [dev/07c-settings-controls.css](../dev/07c-settings-controls.css), [dev/02-base-workspace.css](../dev/02-base-workspace.css) | Warning/destructive buttons | warning/destructive가 resting부터 peach/orange 면을 가졌던 상태 | Resting은 white/gray glass + graphite text, hover/focus에서만 shallow warm/rose rim 적용 |
| 5 | 적용 | [dev/07a-navigation-tasks-search.css](../dev/07a-navigation-tasks-search.css), [dev/07d-canvas-graph-link-panes.css](../dev/07d-canvas-graph-link-panes.css), [dev/10c-overlay-layout-polish.css](../dev/10c-overlay-layout-polish.css) | Task/search active rows | `#eef2ff`, `#6366f1` 계열 active tint와 search match warm 면색이 강했던 상태 | Active는 의미상 색 허용, 배경 면색은 낮추고 rim/left inset/search highlight 중심으로 조정 |
| 6 | 적용 | [dev/07b-overlay-popover-dataview.css](../dev/07b-overlay-popover-dataview.css) | Dataview inline field chip | key chip이 resting부터 sky/cyan surface를 가졌던 상태 | Resting neutral key/value chip, hover/focus에서만 shallow sky rim/text 적용 |
| 7 | 적용 | [dev/06-feature-presets.css](../dev/06-feature-presets.css), [dev/07-plugin-workspace.css](../dev/07-plugin-workspace.css), [dev/07e-live-preview-mobile-plugin.css](../dev/07e-live-preview-mobile-plugin.css) | Kanban/Bases/plugin cards | dark mode flat solid cards와 plugin card glass 부재 | Kanban/Bases/properties 카드 rest를 neutral glass로 낮추고 hover에서만 shallow sky rim/lift 적용 |
| 8 | 적용 | [dev/01-tokens.css](../dev/01-tokens.css), [dev/09c-floating-ui-glass-system.css](../dev/09c-floating-ui-glass-system.css) | 공통 hover token | 일부 hover token이 sky/warm tint를 면색으로 많이 포함했던 상태 | 공통 hover/selected/strong glass token을 neutral glass 중심으로 낮추고 shallow sky rim/inset만 유지 |

## 진행 방식

1. 한 번에 한 우선순위만 리뷰한다.
2. 해당 selector의 실제 최종 owner 파일을 먼저 확인한다.
3. Light/dark/rest/hover/active를 모두 같이 정리한다.
4. `theme.css` bundle, local vault sync, `Validate Theme`를 통과시킨다.
5. README 기능 설명이 바뀌는 경우에만 README와 sample image를 추가한다.

## 1차 추천

첫 적용은 내부 링크 chip부터 진행했습니다. 범위가 작고, 문서 본문에서 자주 보이며, resting gray glass와 hover-only tone 원칙을 체감하기 좋습니다.

내부 링크는 [dev/07-plugin-workspace.css](../dev/07-plugin-workspace.css), [dev/10b-late-reading-nav-polish.css](../dev/10b-late-reading-nav-polish.css), [dev/05-live-preview.css](../dev/05-live-preview.css)에 중복 selector가 있으므로 세 파일을 함께 조정했습니다.