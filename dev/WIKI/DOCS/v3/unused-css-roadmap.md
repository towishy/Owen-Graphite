# v3 Unused CSS Roadmap

unused CSS 정리는 단순 no-match 제거가 아니라 coverage 확장 작업입니다. 현재 리포트는 [dev/WIKI/MAP/unused-css-candidates.md](../../MAP/unused-css-candidates.md)가 진본입니다.

## 현재 상태

| 분류 | 의미 | 처리 |
| --- | --- | --- |
| `candidate` | 낮은 위험의 no-match selector | 현재 0개. 발견 시 소유 모듈에서 제거 검토 |
| `reserved` | runtime, state, plugin, print, Style Settings 등 정적 fixture만으로 증명 불가 | coverage 보강 전 삭제 금지 |
| `invalid-query` | 브라우저 query 한계 또는 pseudo-element 경로 | 삭제 근거로 사용 금지 |

## 제거 조건

| Bucket | 제거 전 필요한 근거 |
| --- | --- |
| `state-interaction` | hover/focus/active 상태를 실제 DOM 또는 Playwright fixture로 확인 |
| `obsidian-chrome-runtime` | Obsidian app chrome에서 pane, tab, modal, menu, tooltip 경로 확인 |
| `plugin-runtime` | Dataview, Tasks, Canvas, Graph, Bookmarks 같은 실제 플러그인 DOM 확인 |
| `print-pdf-context` | PDF export 또는 print fixture에서 header/footer와 page-break 확인 |
| `document-content-fixture-gap` | 자연스러운 Markdown 샘플로 selector가 의미 있는지 확인 |
| `style-setting-class` | Style Settings 계약에서 해당 body class가 제거된 경우에만 검토 |
| `live-preview-runtime` | CodeMirror/Live Preview가 생성하는 runtime class 확인 |

## 다음 coverage 우선순위

1. `state-interaction`: `dev/WIKI/RECIPES/coverage-state-interaction.md`.
2. `plugin-runtime`: `dev/WIKI/RECIPES/coverage-plugin-runtime.md`.
3. `print-pdf-context`: `dev/WIKI/RECIPES/coverage-print-pdf-context.md`.
4. `document-content-fixture-gap`: `dev/WIKI/RECIPES/coverage-document-content-fixture.md`.

## 작업 절차

```powershell
python dev/scripts/build_unused_css_report.py
python dev/scripts/release_check.py
```

리포트에서 `candidate`가 새로 생긴 경우에만 소유 모듈에서 작은 단위로 제거합니다. 제거 후에는 번들 freshness와 docs/assets가 아니라 CSS budget, hit-routing, PDF, visual fixture를 함께 확인합니다.