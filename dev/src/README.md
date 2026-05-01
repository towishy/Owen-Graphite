# `dev/src/` - Superseded Modularization Plan

> **Status**: Superseded by the active `dev/` CSS module workflow.

The theme now uses `dev/` as the development source folder. Edit the CSS modules in `dev/`, then run `python scripts/bundle_theme.py` to regenerate the Obsidian entrypoint `theme.css`.

The notes below are retained as historical planning context only.

`theme.css`는 v1.x 동안 누적된 패치 블록을 포함해 약 9,900줄에 달했습니다. v2.0.0에서는 안정성을 우선해 단일 파일을 유지하되, **다음 마이너 릴리즈(v2.1.0+)부터 모듈 분할 빌드 도입을 예정**했습니다.

## 제안 구조

```
dev/src/
  00-meta.css           # @settings YAML metadata
  01-tokens.css         # CSS variables, Graphite palette
  02-typography.css     # headings, links, lists, body
  03-callouts.css       # callout types + color stripes
  04-code.css           # inline code, code blocks, language labels
  05-tables.css         # table base, modern, comparison/risk patterns
  06-blockquote.css     # nested tonal steps
  07-workspace.css      # tabs, sidebars, status bar, command palette
  08-graph-canvas.css   # graph view, canvas
  09-explorer.css       # file explorer, folder color cues
  10-search.css         # search highlight, switcher
  11-frontmatter.css    # YAML, properties panel
  12-pdf-print.css      # @media print rules, cover page, page headers
  13-mobile.css         # @media (max-width: 768px)
  14-a11y-glass.css     # accessibility, glass intensity, reduced motion
  patches/
    v1.8.42-glass.css
    v1.8.43-glass.css
    v1.8.46-a11y.css
    v1.8.47-tab.css
    v1.8.65-blockquote.css
    v1.8.65-pdf.css
    v1.8.66-polish.css
    v1.8.68-inline-title.css
    v2.0.0-surfaces.css
```

## 빌드 방식 (제안)

`scripts/bundle_theme.py` (신규):
1. `dev/src/*.css`를 정렬된 순서로 concat
2. `dev/src/patches/*.css`를 버전 순으로 append
3. 결과를 `theme.css`로 출력
4. brace balance + validate 자동 실행

## 마이그레이션 원칙

- 기존 `theme.css`의 동작과 **셀렉터·우선순위가 100% 동일**해야 함
- 분할 후 첫 PR에서 visual regression 스크린샷 픽셀 단위 비교 필수
- 분할은 한 번에 진행하지 않고 섹션별 점진 추출 (각 섹션마다 별도 PR)
- 모든 PR은 `python3 scripts/validate_theme.py` 통과 + brace balance 동일

## 왜 v2.0.0에 즉시 분할하지 않았는가

1. **회귀 위험**: 9,900줄을 한 번에 14개 파일로 쪼개면 작은 누락도 시각적 회귀로 이어짐
2. **CSS Cascade 의존**: 일부 `!important` 패치는 선언 순서에 의존 — 분할 시 검증 도구 필요
3. **사용자 영향 0**: Obsidian은 단일 `theme.css`만 로드하므로 분할은 빌드 단계 개선이지 사용자 가치 즉시 증가는 아님
4. **v1.9.0 Section Index 우선**: 현재는 `theme.css` BOF 섹션 인덱스로 탐색성 충분히 개선됨

## 진행 시점

- **v2.1.0**: `dev/src/00-meta.css`, `dev/src/01-tokens.css`만 추출하여 빌드 파이프라인 검증
- **v2.2.0**: typography / callout / code / table 추출
- **v2.3.0**: workspace / pdf / mobile / a11y 추출 — 분할 완료
