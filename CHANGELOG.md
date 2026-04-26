# Changelog

All notable changes to **Owen Graphite Document** are recorded here.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and
this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.4.9] — 2026-04-26

### Fixed
- v1.4.8에서도 첫 페이지 헤더가 Times 계열 serif 폰트로 떨어지던 문제 수정
  - 원인: `font-weight: 600`이 Pretendard SemiBold를 찾지 못해 fallback 발생
  - 수정: `Pretendard Variable` 우선 + `font-weight: 500` (Medium, Variable 폰트가 다 지원) + `-apple-system`/`BlinkMacSystemFont` 스택 추가
  - `font-style/size/weight` 모두 `!important`로 인쇄 머지 룰 완전 제어

## [1.4.8] — 2026-04-26

### Fixed
- v1.4.7에서 `var(--font-text-theme)`가 PDF export 의 인쇄 컨테이너에서 상속되지 않아 머리말 폰트가 system 폰트로 표시되던 문제 수정
  - `font-family`에 Pretendard 스택을 명시적으로 삽입 + `!important`로 우선순위 고정

## [1.4.7] — 2026-04-26

### Changed
- PDF 첫 페이지 우상단 문구가 본문 폰트(Pretendard 등)를 따르도록 `font-family: var(--font-text-theme)` 명시

## [1.4.6] — 2026-04-26

### Fixed
- v1.4.5에서도 PDF 첫 페이지 헤더가 보이지 않던 문제 수정
  - `top: -10mm`이 페이지 마진 영역 밖으로 잘린 것으로 판단
  - `body`, `.print`, `.markdown-preview-view`, `.markdown-rendered` 모두에 `::before` 바인딩하여 Obsidian PDF DOM 변이에 대응
  - `top: 0; right: 0`으로 인쇄 가능 영역 안의 우상단 배치
  - `var(...)`에 fallback `""` 및 `#b91c1c` 명시로 변수 미설정 시 안전 동작
  - `pointer-events: none`으로 에디터 상호작용 방해 방지

## [1.4.5] — 2026-04-26

### Fixed
- PDF 첫 페이지 우측 상단 문구가 PDF에 표시되지 않던 문제 수정
  - 원인: Chromium PDF 엔진은 `@page` 마진 박스(`@top-right` 등) 내부에서 CSS 변수(`var()`)를 해석하지 못함
  - 해결: `@page :first { @top-right }` 방식 대신 `.markdown-preview-view::before` + `position: absolute`로 실제 DOM 요소에 배치
  - 이후 페이지는 새 페이지 박스라 자연스럽게 미표시

## [1.4.4] — 2026-04-26

### Added
- PDF 첫 페이지 우측 상단 머리말 — Style Settings 사용자 입력형
  - `ogd-first-page-header` (variable-text): 표시할 문구 (예: "내부 전용", "Confidential"). 비우면 표시 안 함
  - `ogd-first-page-header-color` (variable-color, 기본 `#b91c1c` 빨강): 문구 색상
  - `@page :first { @top-right { content: var(--ogd-first-page-header) } }` 적용
  - 2페이지부터는 표시되지 않으며, 기존 상단 중앙 H1 제목 / 우하단 페이지 번호는 그대로 유지

## [1.4.3] — 2026-04-26

### Removed
- PDF/인쇄 출력 시 좌하단에 표시되던 "Owen Graphite Document" 푸터 텍스트 제거
  - `@page { @bottom-left { content: "Owen Graphite Document" } }` 블록 삭제
  - 우하단 페이지 번호(`N / N`)와 상단 문서 제목은 유지

## [1.4.2] — 2026-04-26

### Fixed
- 도구모음에 사이드바·이다·탭이 클릭될 때 본문 영역에 검은 outline이 뜨는 문제 해결
  - `:focus-visible` 적용 범위를 **인터랙티브 요소**(button/a/input/role=button 등)로 한정
  - `.workspace-leaf`, `.view-content`, `.markdown-source-view`, `.markdown-reading-view`, `.cm-editor`, `.cm-scroller` 등 콘테이너에서 명시적으로 outline 제거
  - 접근성 G3 조항은 유지 — 실제 조작 대상인 링크·버튼·입력만 강한 포커스 링 유지

## [1.4.1] — 2026-04-26

### Fixed
- Blockquote / callout / CM6 quote: 좌측 보더와 본문 텍스트가 겹치는 문제 해결
  - blockquote padding-left 16 → 22px (보더 3 → 4px)
  - callout padding-left 12 → 18px
  - CM6 HyperMD-quote padding-left 20 → 24px (보더 3 → 4px)
- 모든 보더 요소에 `box-sizing: border-box` 명시

## [1.4.0] — 2026-04-26

### Added — 33-point comprehensive upgrade

**A. Typography**
- Drop cap (toggle)
- First-line indent (toggle)
- Serif body mode (Noto Serif KR, toggle)
- Auto heading numbering (1. / 1.1 / 1.1.1, toggle)
- Hanging punctuation
- Tabular numerals on tables

**B. Content emphasis**
- `<kbd>` Mac key cap styling
- `> [!secret]` blur callout (hover to reveal)
- Footnote ref highlight on hover
- Hover popover unified shadow / padding
- Image zoom-in cursor + brightness hover
- Mermaid card container

**C. Report features**
- Cover page (report mode)
- TOC dot leader
- Print header / footer (title + page number)
- Per-chapter page counter
- A4 portrait / A4 landscape / A3 landscape options
- Frontmatter metadata grid block

**D. UI polish**
- Sidebar folder color coding by path
- Active file 4px accent bar
- Tab icon coloring by file type
- Status bar segment dividers
- Command palette card hover
- Graph view node colors
- Dataview table unified with theme tables

**E. Plugin integration**
- Excalidraw host / svg
- Kanban lane / card / item
- Calendar active day
- Properties panel (Obsidian 1.4+)
- Bases card / table (Obsidian 1.7+)

**F. Style Settings presets**
- Report Mode bundle toggle
- Spacing presets (Compact / Standard / Relaxed)
- Accent colors (Graphite / Blue / Teal / Violet / Amber)
- Code themes (Light / Solarized / Nord / Dracula)
- Eye-care beige background mode
- OS dark-mode auto follow

**G. Accessibility / i18n**
- `prefers-contrast: high`
- `prefers-reduced-motion`
- Strong `:focus-visible` outline + glow
- CJK font +0.5px auto boost
- OS dark-mode auto follow

### Changed
- Style Settings: 5 → 16 items
- README.md: comprehensive 229-line documentation

## [1.3.1] — 2026-04-26

### Added — Live Preview ↔ Reading View 12-point parity
- CM6 header per-level line-height + `cm-header-N` font-size/weight
- Codeblock middle lines: left/right borders for full box look
- Wikilink chip background in CM6
- Tag pill shape (begin/end split radius)
- Inline code box + dimmed backticks
- `cm-strong` weight, `cm-em` italic, `cm-strikethrough`
- Checkbox alignment in CM6
- Callout widget radius/padding sharing
- Table widget border + hover + dim pipes
- List markers accent color + indent guide
- Frontmatter box (rounded first/last lines)
- Dark mode parity for all 12 items

## [1.3.0] — 2026-04-26

### Added — 13-category comprehensive improvement
- Style Settings header (`/* @settings */`)
- Full dark mode variable set + dark variants for callout/table/code/tag/link/checkbox/highlight
- H4–H6 styling
- All callout types: note/info/tip/abstract/example/quote/question/warning/success
- Table enhancements: tabular-nums, hover row, sticky-first-col, zebra toggle, `.num` right-align
- Code: language badge (top-right), diff line tinting, copy button contrast, KO/EN inline baseline fix
- Lists: ol marker color, nested indent guide, custom checkbox (✓), strikethrough completed
- Tag chip styling (pill, border, hover)
- Footnotes / Frontmatter box
- Image shadow + figure caption, iframe 16:9, pdf-embed border
- Live Preview formatting markers dim (`#cbd5e1`)
- Workspace polish: active tab top accent border, search highlight, `:focus-visible` outline
- Print enhancements: H1 page break, heading break-after avoid, external link URL display, UI chrome hidden
- Korean font fallback chain + `word-break: keep-all` + `overflow-wrap: anywhere`

## [1.2.0] — 2026-04-26

### Fixed
- Live Preview blank line height — `.cm-line:empty` and `.cm-line:has(br:only-child)` height 0.45em
- Bridge to compact PDF spacing now also applies in Source mode

## [1.1.0] — 2026-04-26

### Changed — PDF compact spacing
- Body line-height 1.68 → 1.5
- Paragraph margin-bottom 0.72em → 0.45em
- H1/H2/H3 margin-top 1.8/1.55/1.1em → 1.0/0.95/0.7em
- Tables, blockquote, callout, pre all 30–50% reduced

## [1.0.0] — Initial release

### Added
- Basic graphite light theme based on `outputs/drafts/옵시디언설정`
- Light mode with graphite accent
- Initial header / paragraph / table / code / blockquote styling
- A3 landscape print support

---

[1.4.2]: https://github.com/towishy/Owen-Graphite/releases/tag/1.4.2
[1.4.1]: https://github.com/towishy/Owen-Graphite/releases/tag/1.4.1
[1.4.0]: https://github.com/towishy/Owen-Graphite/releases/tag/1.4.0
[1.3.1]: https://github.com/towishy/Owen-Graphite/releases/tag/1.3.1
[1.3.0]: https://github.com/towishy/Owen-Graphite/releases/tag/1.3.0
[1.2.0]: https://github.com/towishy/Owen-Graphite/releases/tag/1.2.0
[1.1.0]: https://github.com/towishy/Owen-Graphite/releases/tag/1.1.0
[1.0.0]: https://github.com/towishy/Owen-Graphite/releases/tag/1.0.0
