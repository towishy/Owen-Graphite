---
title: Liquid Glass Table and Focus Smoke Sample
date: 2026-05-04
tags:
  - liquid-glass
  - qa
  - table
  - focus
cssclasses:
  - ogd-modern-tables
  - ogd-print-avoid-breaks
---

# Liquid Glass Table and Focus Smoke Sample

이 문서는 Owen Graphite의 위키형 표, 보고서형 표, Frost Aqua focus 상태를 한 번에 확인하기 위한 QA 샘플이다.

## Wiki Table Baseline

일반 위키 노트에서는 Markdown table을 유지한다. 표면은 가벼운 glass surface, 행 hover는 얕은 sky tint 기준이다.

| 항목 | 상태 | 메모 |
|------|------|------|
| 문서 구조 | 진행 | 링크와 본문 흐름 유지 |
| 표 표현 | 점검 | 부드러운 rim과 낮은 shadow |
| 포커스 | 확인 | keyboard focus 시 halo 확인 |

## Report Table Baseline

보고서/PDF 문서에서는 `ogd-report-mode`를 적용하고 rule과 contrast를 우선 확인한다.

```yaml
cssclasses:
  - ogd-report-mode
  - ogd-modern-tables
  - ogd-print-avoid-breaks
```

| 구분 | 수치 | 판단 |
|------|-----:|------|
| 위험 | 3 | 관리 |
| 완료 | 92% | 유지 |
| 검토 | 1 | 보류 |

## Frost Aqua Focus Sweep

아래 항목을 Tab 키로 순회하면서 layout shift 없이 aqua rim과 soft halo가 표시되는지 확인한다.

- Ribbon/toolbar: `.clickable-icon`, `.view-action`, `.editingToolbarButton`
- Navigation: `.nav-file-title`, `.nav-folder-title`, `.tree-item-self`
- Tabs: `.workspace-tab-header`, `.workspace-tab-header-inner`
- Search/modal: `.search-input-container`, `.document-search-container`, `.prompt-input`, `.modal input`
- Settings: `.setting-item`, `.metadata-property`

## Regression Notes

- resting state는 white/gray frosted glass여야 한다.
- active/focus 색은 rim, halo, inset line에만 제한한다.
- table row와 outer shell 사이에는 여유 마진이 있어야 한다.
- 좌측 세로 line/rail로 선택 상태를 만들지 않는다.