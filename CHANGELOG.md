# Changelog

All notable changes to **Owen Graphite** are recorded here.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and
this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.4] — 2026-04-29 — Live Preview cm-embed-block table fix

### Fixed
- **Live Preview 표 셀이 늘어나는 현상 실제 원인 차단** — v2.0.2/v2.0.3은 `.cm-table-widget` / `.HyperMD-table-row` 만 노렸으나, 현재 Obsidian(1.6.x+) Live Preview는 커서가 표 밖에 있을 때 표를 `.cm-embed-block > <table>` 정적 블록으로 렌더링함. 실제 세이브되는 표에 대해 `td > p` margin 0, `td/th/tr` height auto + min-height 0, 컬러 block 자체 min-height 0 적용.

## [2.0.3] — 2026-04-29 — Table inflate hardening

### Fixed
- **표 셀 inflate 잔존 케이스 완전 차단** — v2.0.2에서도 다음 조건에서 셀이 높이로 부풀는 현상이 남아 있었음을 보완:
  - (a) `cm-table-widget` 컨테이너 자체·중첩 자식이 inner cm-content로부터 min-height를 세승하는 경우 → 레벨 불문 `min-height: 0`.
  - (b) Reading view에서 Obsidian이 셀 텍스트를 `<p>`로 래핑해 상하 1em margin을 추가하는 경우 → `td > p` margin 0.
  - (c) 고정 height가 명시된 셀 → `height: auto`, `vertical-align: top` 명시.
  - (d) Live Preview의 빈 trailing `cm-line` → `display: none`.
- Reading view + Live Preview 양쪽에서 동일하게 적용.

## [2.0.2] — 2026-04-29 — Bugfix + README 종합 정리

### Fixed
- **Live Preview 표 셀 편집시 행이 화면 높이로 늘어나는 버그 수정** — `.cm-content { min-height: calc(100vh - 220px) }` 베이스 룰이 표 셀 안 중첩 CodeMirror 에디터에도 적용되어 셀이 화면 전체로 부풀던 현상을 수정. `.cm-table-widget` / `table.cm-table` / `.HyperMD-table-row` 안쪽의 `cm-content`·`cm-line`·`cm-scroller`에 `min-height: 0` `height: auto` 적용.

### Documentation
- **한 줄 요약 차별점** — Workspace Surfaces / Polish Pack 단서 추가.
- **사용자 클래스 표 확장** — `.cover-page` `.cover-meta` `.cover-rule` `.ogd-mini-toc` v2.0.0 옵인 클래스 도쇄.
- **파일 구조 광명** — `CONTRIBUTING.md`, `LICENSE`, `.github/workflows/`, `src/` 신규 항목 표시 및 theme.css 라인 그급 명시.
- **변경 이력 최신화** — v1.8.65 / v1.8.66 / v1.9.0 / v2.0.0 요약 추가.
- **기여 섹션** — CONTRIBUTING.md / src/README.md 참조 링크 추가.

## [2.0.1] — 2026-04-29 — README 종합 정리

v2.0.0 시점의 기능·파일 구조·사용자 클래스를 README에 종합 반영하는 문서 패치.

### Documentation
- **한 줄 요약 차별점** — Workspace Surfaces / Polish Pack 단서 추가.
- **사용자 클래스 표 확장** — `.cover-page` `.cover-meta` `.cover-rule` `.ogd-mini-toc` v2.0.0 옵인 클래스 도쇄.
- **파일 구조 광멵** — `CONTRIBUTING.md`, `LICENSE`, `.github/workflows/`, `src/` 신규 항목 표시 및 theme.css 라인 그기 명시.
- **변경 이력 최신화** — v1.8.65 / v1.8.66 / v1.9.0 / v2.0.0 요약 추가.
- **기여 섹션** — CONTRIBUTING.md / src/README.md 참조 링크 추가.

### Notes
- CSS 변경 없음. v2.0.0 완전 동일.

## [2.0.0] — 2026-04-29 — Workspace Surfaces Pack

노트 본문 외 주요 워크스페이스 면을 통일된 디자인 언어로 정리하고, 향후 모듈 분할 계획을 `src/` 디렉터리에 문서화한 메이저 릴리즈.

### Added
- **Graph view 스타일** — 노드 레이블 폰트 통일(11px / 500 weight), hover 시 accent stroke, 그룹 컬러 input 원형 pill.
- **Canvas 컴포넌트** — 카드 다층 shadow, focus 외곽선, edge hover 강조, 6개 color group 변수화.
- **File explorer 폴더 컬러 큐** — 온톨로지 경로 패턴(`raw/`, `wiki/`, `outputs/`, `reports/`, `presentations/`, `Clippings/`, `Attachments/`, `Templates/`, `archive/`, `drafts/`)에 3px 좌측 틴트.
- **Reading view mini TOC** — `.ogd-mini-toc` 옵인 클래스. 우측 sticky TOC, 모바일 자동 인라인, 프린트에서 숨김, `:target` hover 강조.
- **Print 표지 페이지** — `cover-page` 옵인 클래스. 세로로 중앙 정렬, H1 확대, `.cover-meta`·`.cover-rule` 서브클래스, 출력 시 자동 페이지 분할.
- **`src/README.md`** — v2.1.0 이후 도입할 모듈 분할 구조, 빌드 파이프라인, 마이그레이션 원칙 정리.

### Notes
- **파괴적 변경 없음** (v1.x 사용자 안전). 새 기능은 전부 opt-in(에 대한 클래스 적용) 또는 경로 자동 감지 방식. v2.0.0 bump는 새 면적의 수(workspace surfaces)와 모듈화 로드맵 공식화를 반영.
- `theme.css` 실제 모듈 분할은 v2.1.0 부터 단계적으로 진행 예정 (`src/README.md` 참조).

## [1.9.0] — 2026-04-29 — Maintainability Pass

구조·문서·자동화를 정비한 마이너 릴리즈. CSS 동작은 v1.8.66과 동일하고 제로 회귀입니다.

### Added
- **`CONTRIBUTING.md`** — 로컬 개발 환경 세팅, rsync·validate·build 워크플로우, CSS 패치 블록 추가 규칙, 릴리즈 절차(한글 노트는 `--notes-file` 필수) 등 외부 기여자 가이드.
- **README Style Settings i18n 매핑표** — 한글 구획 명을 English 대응 명과 함께 표기(외국 사용자 접근성).
- **theme.css BOF Section Index** — 구제적인 라인 범위 추가, 몇 달간 누적된 패치 블록(v1.8.42 ~ v1.8.66) 인벤토리 및 기여자 주의사항 명시.

### Changed
- **CI 강화 (`.github/workflows/validate.yml`)** — brace balance 검사와 `manifest.json` JSON 파싱을 PR 단계에서 자동 검증.
- **theme.css 헤더** — 라이선스(MIT)·저자·레포 명시, 섬션 레이아웃 명확화.

### Notes
- 새 기능/디자인 변경 없음. 온전히 유지 보수 릴리즈(`minor` bump는 CONTRIBUTING/CI/Index 신규 파일·세그먼트 추가를 알리기 위함).
- 향후 v2.0.0에서 theme.css 실제 모듈 분할(섬션별 파일)을 검토 예정. 현재는 회귀 위험 최소화 우선.

## [1.8.66] — 2026-04-29 — Polish Pack

### Added
- **Dark Mode parity** — blockquote 3단계 톤, H1 kicker 색상, inline code, search highlight의 다크 모드 전용 변수 추가로 명도 대비 귬형.
- **Mobile 반응형** (`@media (max-width: 768px)`) — H1 2.8em → 1.9em, kicker letter-spacing 완화, callout padding·아이콘 축소, 탭 타이틀 폰트 조정.
- **Tab 구분 강화** — 활성 탭 상단 2px accent bar + 600 weight, 비활성 탭 opacity 0.78에서 hover 시 1.0으로 복귀.
- **Callout 타입별 좌측 컬러바** — note/info/tip/success/warning/danger/example/quote/abstract/todo/question/bug 13개 타입에 4px 수직 스트라이프.
- **코드 블록 언어 라벨** — 코드블록 우상단에 언어 배지(TS/JS/PY/SH/CSS/HTML/JSON/YAML/MD/RS/GO/SQL).
- **헤딩 앵커** — H2/H3/H4 hover 시 좌측 `#` 앵커 표시(인쇄시 숨김).
- **Status bar 모노스페이스 통일** — 11px JetBrains Mono 적용.
- **Search highlight 강화** — amber 배경 + box-shadow 외곽선, 다크 모드 `#5b4a14` 대응.
- **Frontmatter 가독성** — YAML 코드블록과 Properties 패널 모노스페이스 + 키 weight 600.

### Changed
- **Inline code** 연한 회색 배경(`#f3f4f6`) + `#b91c1c` 텍스트로 본문과 더 명확하게 구분.
- **방문 링크** `:visited` 색상을 보라색 계열(`#7c3aed` / dark `#c4b5fd`)로 전환.

## [1.8.65] — 2026-04-29

### Fixed
- **Windows Live Preview에서 `>` 인용 마커가 돌출되는 »·› 글리프로 렌더링되는 폰트 폴백 이슈 수정** — `cm-formatting-quote`를 완전 숨김 처리하고 연한 배경 틴트로 인용 구분.
- PDF에서 긴 표가 여러 페이지에 걸칠 때 헤더가 매 페이지 상단에 반복 출력되도록 `thead`에 `display: table-header-group` 적용.
- Windows Chromium에서 H1 chapter break가 매번 적용되도록 `-webkit-column-break-before` fallback 추가.

### Changed
- 모노스페이스 폰트 폴백 보강 — `Cascadia Mono`, `Consolas`, `Courier New` 추가로 Windows 기본 설치 환경에서도 키커·코드 블록이 동일하게 렌더링.
- Nested blockquote 단계별 톤 차등화 (1단계 `#f8fafc` → 2단계 `#f1f5f9` → 3단계 `#e2e8f0`).
- PDF 줄간격 미세조정 (본문 1.5 → 1.55, 표 1.4 → 1.45).
- PDF Footnote 섹션 스타일 보강 (상단 구분선 + 폰트 축소).

### Removed
- `docs/fixtures/h1-style-samples.html` 디버그용 임시 파일 제거.

## [1.8.64] — 2026-04-29

### Added
- H1 헤딩에 자동 챕터 번호 키커(Sample B 에디토리얼 스타일) 적용 — `01`, `02` 형식의 모노스페이스 키커 + 큰 굵은 제목, Reading view·Live Preview·PDF 모두 동일.
- Blockquote 인용문 시각화 방식 개선 — 세로 바 대신 연한 회색 배경(`#f8fafc`) + 둥근 모서리 + 이탤릭 글꼴 조합. PDF 출력에서도 동일하게 적용.
- 인라인 제목(inline title) 기본 비활성화 — 파일명은 탭 헤더에서 표시.

### Changed
- 기존 별도 CSS 스니핏(`zz-obsidian-gray-force-override-v2.css`) 기능을 테마에 완전 흡수하여 빌트인으로 제공. 별도 스니핏 설치 불필요.
- PDF 출력 시 H1 폰트 크기를 `2.15em → 2.8em`으로 강화하여 H2와의 시각적 위계 명확화.
- 다크 모드 blockquote 배경을 `#1f2937`로 정리하여 라이트 모드와 대칭.

### Removed
- `snippets/zz-obsidian-gray-force-override-v2.css` 파일 제거 (기능은 테마로 이전).
- README의 별도 snippet 설치 안내 섹션 제거, 빌트인 흡수 안내로 교체.
- `build_release.py`/`validate_theme.py` 스크립트의 snippet 참조 제거.

### Fixed
- PDF에서 H1 아래 그라데이션 라인이 중복 출력되던 v1.8.19 패치 잔존 규칙 정리.
- 키커 자간이 너무 넓어 "0 1"로 분리되어 보이던 문제 수정 (`letter-spacing 4px → 2px`, fallback 폰트에 Consolas/Cascadia Mono 추가).

## [1.8.63] — 2026-04-28

### Added
- ZIP 수동 설치 섹션에 올바른 asset 파일 선택 안내 및 SVG 가이드 이미지 추가 (Source code zip ≠ Owen-Graphite zip).

## [1.8.62] — 2026-04-28

### Changed
- Updated Windows, macOS, and Linux Git install commands to suppress raw Git output and print a clear OK message only after a successful install or update.

## [1.8.61] — 2026-04-28

### Fixed
- Broadened readable-line-width overrides across Reading View and Live Preview wrappers so fresh Windows installs no longer center the Markdown column with a large leading blank area.

## [1.8.60] — 2026-04-28

### Fixed
- Fixed an oversized leading blank area before the readable Markdown column on fresh Windows installs by anchoring the readable column to the pane's left edge.

### Changed
- Removed redundant vault path examples from the Windows and macOS/Linux manual install sections.
- Clarified that the manual ZIP install folder must be named `Owen Graphite`.

## [1.8.59] — 2026-04-28

### Fixed
- Fixed a fresh-install Live Preview regression where the CodeMirror editing surface could shrink to the text glyph width, leaving the rest of the writing area unresponsive to clicks.

### Changed
- Updated the manual install docs with platform-specific Git install commands, Git-based install/update commands for Windows/macOS/Linux, and a separate ZIP install path.

## [1.8.58] — 2026-04-28

### Fixed
- Fixed a fresh-install Reading View regression where preview paragraph blocks could shrink to a one-character-wide column in Korean notes.

### Changed
- Updated the Windows manual install command so it creates `.obsidian\themes` from the vault root and clones directly into `.obsidian\themes\Owen Graphite`.

## [1.8.57] — 2026-04-28

### Fixed
- Fixed a Live Preview layout regression where manually installed themes without the optional force-override snippet could collapse Korean editing lines into a one-character-wide column.

## [1.8.56] — 2026-04-28

### Changed
- Refined search input focus states with a calmer Graphite ring across search panes, modals, and prompt inputs.
- Polished command palette, suggestion, and menu selected rows so overlay lists feel consistent with the document selection language.
- Unified tooltip and hover popover surfaces with lower-contrast borders, softer shadows, and tighter document-preview rhythm.
- Improved empty states and keyboard `:focus-visible` indicators for quieter screens that still remain navigable.

## [1.8.55] — 2026-04-28

### Added
- Added `.ogd-status-ok`, `.ogd-status-no`, and `.ogd-status-warn` inline status badges for OS-independent report status markers.

### Changed
- Refined the first lead paragraph after H1, horizontal rules, internal/external link grammar, and H2-to-table spacing for calmer writing screens.
- Reduced top-level file explorer weight while keeping the active path legible in deep report vaults.

## [1.8.54] — 2026-04-28

### Changed
- Refined default Markdown table surfaces with a calmer graphite header, softer internal grid, quieter hover state, and clearer first-column emphasis.
- Improved document rhythm around title/section headings and their following lead paragraphs for real Obsidian report editing screens.
- Softened selected file explorer glass contrast so the active document stays clear without pulling focus from the report body.
- Reduced spellcheck and grammar underline noise in Live Preview while preserving the editor signal.

## [1.8.53] — 2026-04-28

### Fixed
- Release ZIP and GitHub Release assets now include every screenshot referenced by the README, including the README promo image and recent preview fixtures.

## [1.8.52] — 2026-04-28

### Added
- Vault tree design, icon treatment, selected-document icon effect, and color comparison preview fixtures with generated sample screenshots.

### Changed
- File explorer folder and document pseudo-icons now use the lighter Thin Outline Icons treatment for a calmer Graphite tree.
- Active file selection keeps the glass surface and shadow while removing the outline-grow ring, scale lift, and heavy filled icon treatment.

## [1.8.51] — 2026-04-27

### Added
- Callout report and HTML preview fixtures for semantic report callout regression checks.
- `scripts/contrast_audit.py` for key light/dark foreground and background contrast pairs.
- Optional `scripts/visual_regression.py` Playwright capture helper for HTML fixture screenshots.
- Validator contrast audit integration plus a final release checklist summary.
- README guidance for Style Settings presets, plugin support levels, table utility combinations, detail preview links, and optional visual regression workflow.

### Changed
- `theme.css` now starts with a compact section index and exposes shared Graphite surface/line/text token aliases for future maintenance.

## [1.8.50] — 2026-04-27

### Added
- Style Settings section headings for reading, table/code, report/PDF, workspace/accessibility, and first-page header controls while keeping the same 27 functional options.
- `nowrap-code-table`, `scroll-token-table`, and `scroll-table` table helper classes for long policy IDs, URLs, and resource names that should not make rows excessively tall.

### Changed
- File explorer disclosure arrows now use a softer modern chevron treatment with hover feedback in light and dark modes.
- Reading and Live Preview content gains slightly more left breathing room so report blocks do not sit too close to the sidebar.
- Report callouts (`conclusion`, `recommendation`, `risk`, `action`, `decision`) now share a calmer semantic outline language and updated Lucide icon mapping.

## [1.8.49] — 2026-04-27

### Added
- Optional `.ogd-reference-list` pattern for reference-heavy sections, separating source badges, document titles, metadata, and notes for faster scanning in reports.
- `.ogd-reference-summary`, `.ogd-reference-source`, `.ogd-reference-main`, `.ogd-reference-title`, `.ogd-reference-meta`, and `.ogd-reference-note` helper classes with light/dark and mobile handling.
- Reference-list polish preview fixture comparing the current bullet list style with the recommended structured reference layout.

### Changed
- README now documents the reference-list pattern and keeps it opt-in so ordinary Markdown lists remain unchanged.

## [1.8.48] — 2026-04-27

### Added
- Search pane input glass treatment for desktop, including the search field, Aa button, and filter controls with reduced-motion, high-contrast, forced-colors, and glass-intensity handling.
- Preview fixtures for search input glass and external-link dotted underline color comparisons.

### Changed
- External links now use a calmer Muted Gray dotted underline instead of the previous teal treatment, reducing visual noise in reference-heavy documents.
- Active file explorer items no longer show the decorative document watermark inside the selected glass pill.
- Release packaging now includes README screenshot assets so manual installs and theme detail views can render README images correctly.

## [1.8.47] — 2026-04-27

### Added
- Workspace tab glass treatment for desktop chrome, scoped to the inner tab surface to avoid Obsidian tab-frame divider conflicts.
- A tab glass preview fixture for comparing conservative, balanced, and strong tab styling variants before applying them to the main theme.

### Changed
- Active workspace tabs now use a line-free focused glass surface with subtle diffuse shadow, stronger text emphasis, square corners, and wider tab spacing.
- Default Obsidian tab separator pseudo-lines are neutralized so inactive-tab dividers and active-tab internal vertical lines do not show through the glass surface.
- Reduced-motion, high-contrast, forced-colors, dark mode, and glass-intensity presets remain aligned with the new tab styling.

## [1.8.46] — 2026-04-27

### Added
- Accessibility hardening for the latest glass UI layer: reduced-motion users now get no hover lift, no glass blur filters, and near-zero transition timing across toolbar, settings, status bar, popover, suggestion, metadata, and canvas controls.
- High-contrast and forced-colors handling for glass borders, focus outlines, selected suggestions, modals, notices, toggles, and status bar segments.
- Python validator checks for Python-only scripts, ignored local Python/build artifacts, single-source validation workflow usage, release workflow Python calls, and generated release ZIP contents when present.

### Changed
- Validation workflow now delegates to `python scripts/validate_theme.py --ci` as the single source of truth instead of duplicating manifest/theme checks in shell steps.
- README documents Glass intensity presets and accessibility behavior more explicitly.

## [1.8.45] — 2026-04-27

### Removed
- Removed the legacy Ruby validator (`scripts/validate_theme.rb`). Theme validation and release automation are now Python-only.

### Changed
- README now describes Python as the single validation path for both Windows and macOS.
- `.gitignore` now excludes local Python virtual environments and bytecode caches.

## [1.8.44] — 2026-04-27

### Added
- Cross-platform Python validator (`scripts/validate_theme.py`) for required files, manifest/README/CHANGELOG version alignment, Style Settings option count, screenshot dimensions, release workflow assets, Live Preview editability guards, `git diff --check`, and optional active-vault sync checks.
- Python release ZIP builder (`scripts/build_release.py`) that packages manual install assets into `dist/Owen-Graphite-<version>.zip`.

### Changed
- GitHub Actions validation and release workflows now use Python instead of Ruby, improving Windows/macOS parity and reducing local setup friction.
- Release workflow now validates the package and attaches the generated manual-install ZIP alongside individual theme assets.
- README local validation instructions now prefer Python and document the release ZIP build command.

## [1.8.43] — 2026-04-27

### Added
- Style Settings glass intensity preset: Off, Reduced, Subtle, Standard, and Strong for desktop liquid-glass chrome.
- Reduced glass mode disables blur while keeping restrained surface contrast and light shadows for low-power or battery-focused environments.
- Additional control polish for color pickers, disabled controls, CTA/warning/destructive pressed states, command palette focus rings, and Properties value focus rows.

### Changed
- Glass surfaces now share preset-driven filter variables so prompts, modals, hover popovers, settings controls, Canvas controls, status bar segments, and Editing Toolbar plugin surfaces can scale together.
- Print output explicitly neutralizes glass variables to keep report/PDF rendering isolated from desktop UI effects.
- Marketplace screenshots were regenerated to show v1.8.43 command palette, glass toggles, and the new preset language.

## [1.8.42] — 2026-04-27

### Added
- Floating UI glass expansion for command palette, modal/prompt surfaces, hover popovers, notices, Properties/frontmatter panels, Canvas controls, and status bar hover segments.
- Settings controls now share the desktop glass treatment across toggles, inputs, dropdowns, sliders, color pickers, and button-adjacent focus/hover states.
- Toggle switches receive a glass track/thumb treatment with light/dark parity and distinct enabled/disabled surfaces.

### Changed
- Settings row hover glass now covers the full outer row box again, using an outline-based border treatment to avoid shrinking the hover surface.
- Command palette and suggestion selected states are now more distinct from plain hover states, improving keyboard navigation clarity.
- Nested plugin settings rows, including Style Settings-style layouts, use a lighter glass hover so deeply nested controls remain readable.
- Status bar glass hover is more restrained to keep the footer calm while still matching the broader chrome language.

## [1.8.41] — 2026-04-27

### Changed
- Editing Toolbar plugin top bar now offsets from the left splitter using the plugin's own toolbar offset variable, so the full toolbar surface no longer hugs the sidebar frame.
- Workspace resize handles are hidden by default but remain usable: hovering/focusing the split edge reveals a subtle handle while preserving drag resizing.
- Workspace frame/divider cleanup now neutralizes persistent split-pane frame lines through Obsidian divider and tab outline variables.
- File explorer and side dock scrollbar cleanup hides the sidebar thumb line across nested scroll containers.

## [1.8.40] — 2026-04-27

### Added
- 검색 옵션 suggestion popover(`.suggestion-container`, search suggest variants)에 desktop liquid-glass surface 적용.
- 검색 옵션 항목 hover/click/selected 상태에 반투명 유리창 효과, blur, drop shadow, subtle lift 적용.
- Light/Dark 테마 패리티 보장.

## [1.8.39] — 2026-04-27

### Added
- Settings 모달에 liquid-glass hover 적용: 좌측 nav 항목(`.vertical-tab-nav-item`)과 우측 설정 행(`.setting-item`) 모두 hover 시 슬레이트 gradient + blur + 서틀 lift 적용. Active nav 항목은 sky-tint로 구분.
- Light/Dark 테마 패리티 보장.

## [1.8.38] — 2026-04-27

### Changed
- macOS: 사이드바 토글 버튼 hover 시 다른 chrome과 동일한 liquid-glass 표면(연한 슬레이트 gradient + blur + 서틀 lift) 적용. 본얰 상태는 여전히 Obsidian 기본 subtle을 유지해 타이틀바 안에서 떠 보이지 않음.

## [1.8.37] — 2026-04-27

### Fixed
- macOS: 좌/우 사이드바 토글 버튼이 v1.8.21–22 글래스 트리트먼트로 인해 타이틀바 안에서 두꺼운 36×36 프레임 버튼처럼 떠 보이던 문제 수정. `body.mod-macos`에서만 토글 버튼을 Obsidian 기본 subtle 스타일로 되돌리고, 좌측 ribbon 아이콘의 글래스 효과는 그대로 유지.

## [1.8.36] — 2026-04-27

### Added
- Liquid-glass surface across desktop chrome:
  - Ribbon · sidebar toggle · workspace tab list · nav file/folder hover · active file (v1.8.20–v1.8.23)
  - Editing Toolbar plugin: bar · icon buttons · submenu popovers (v1.8.24, v1.8.32, v1.8.33)
  - Resize handle, context menu (`.menu`), tooltip, breadcrumb hover (v1.8.27, v1.8.31, v1.8.34, v1.8.35, v1.8.36)
- All glass blocks scoped to `@media (min-width: 701px)` + `body:not(.is-mobile)` to keep mobile parity stable.
- Light/Dark theme pairs for every glass surface (slate gradient + sky accent on hover).

### Changed
- Sidebar `outputs` / `raw/obsidian/outputs` folder labels are now bold near-black (`#111827` light / `#f9fafb` dark) for stronger hierarchy (D1).
- Resize handle muted by default, brightens on hover with sky tint.
- Editing Toolbar shifted right (padding-left 72px) so it no longer hugs the left sidebar edge.
- `mod-root` view-header / tab-header borders softened to `rgba(100,116,139,0.22)` (light) / `rgba(203,213,225,0.18)` (dark) to remove sharp dark hairlines.

### Fixed
- v1.8.24 block was missing its closing `}` for the `@media` wrapper, which silently nested all subsequent v1.8.25b–v1.8.36 rules. Brace balance restored to 862/862.
- Removed duplicate v1.8.34 `.menu` glass block.

## [1.8.19] — 2026-04-26

### Added
- PDF 디자인 10개 개선 전/후를 비교하는 HTML fixture와 PNG preview 이미지 추가
- Border식 작업 영역 프레임, 반투명 유리 리본 아이콘, 활성 문서, 활성 탭 chrome 샘플 fixture와 preview 이미지 추가

### Changed
- macOS/Windows Obsidian 데스크톱 클라이언트에서 작업 영역 chrome이 반투명 유리 톤으로 보이도록 최종 override 추가
- PDF export에서 제목 직후 문단, H2/H3/H4 다음 표, 긴 표 셀, 첫 컬럼, `hr` 구분선의 간격과 가독성을 보강
- PDF용 `ogd-status-badge`, `ogd-executive-summary`, `ogd-action-summary` 스타일을 추가해 emoji 상태값과 반복 액션 문장을 badge/callout 형태로 정리할 수 있도록 보강
- 긴 표가 페이지를 넘어갈 때 `thead` 반복과 행 분할 회피가 더 안정적으로 동작하도록 print table cascade 보강
- 문서 원문에 별도 class를 추가하지 않아도 첫 Executive Summary 표의 상태 컬럼과 표 뒤 bold-leading 액션 문단이 더 명확히 보이도록 자동 print selector 보강

## [1.8.18] — 2026-04-26

### Changed
- PDF export에서 첫 H1/H2 제목 라인이 제목 길이에 맞는 Teal-to-Sky rule로 안정적으로 출력되도록 print cascade 보강
- PDF 첫 페이지 헤더와 첫 제목 사이에 매우 옅은 구분선을 추가해 상단 영역을 더 정돈
- README의 Gray override 섹션에서 report title spacing preview 이미지 노출 제거

## [1.8.17] — 2026-04-26

### Added
- 보고서 제목 라인 간격과 컬러를 확인하는 HTML fixture와 PNG preview 이미지 추가

### Changed
- 기본 테마와 Gray override snippet의 H1 제목 스타일을 제목 길이에 맞는 Teal-to-Sky 하단 라인으로 정리
- PDF 첫 페이지의 첫 H1은 헤더와 제목, 제목 라인과 본문 사이 여백을 더 넓게 조정

## [1.8.16] — 2026-04-26

### Added
- 외부 링크 점선 밑줄 색상 후보를 비교하는 HTML fixture와 PNG preview 이미지 추가

### Changed
- 기본 테마와 Gray override snippet의 외부 링크를 Muted Teal 점선 밑줄 스타일로 정리해 내부 링크와 구분

## [1.8.15] — 2026-04-26

### Added
- Gray override snippet에 TOC, 이미지/첨부 캡션, Mermaid/SVG diagram frame, footnote, task list, definition list, 검색 하이라이트, PDF heading rhythm 스타일 추가
- 8개 추가 디자인 개선안을 시각화하는 HTML fixture와 PNG preview 이미지 추가

### Changed
- README의 Gray Report Force Override 설명에 8개 개선 preview 이미지를 연결하고 기능 설명을 확장

## [1.8.14] — 2026-04-26

### Added
- Gray override CSS snippet 디자인 개선안을 시각화하는 HTML fixture와 PNG preview 이미지 추가
- Gray override snippet에 `hr`, link, `mark`, `kbd`, table caption / numeric cell / first-column 강조 스타일 추가
- Gray override snippet에 print/PDF page-break 보강과 dark mode report fallback 스타일 추가

### Changed
- Gray override snippet의 callout을 compact density와 semantic outline icon badge 중심으로 정리
- Gray override snippet의 table, blockquote, inline code, Live Preview codeblock 톤을 보고서형 문서에 맞게 완화

## [1.8.13] — 2026-04-26

### Added
- Live Preview heading / paragraph / wrapped blockquote / callout / table adjacency 편집 hitbox 회귀 확인용 fixture 문서 추가
- `validate_theme.rb`에 CM6 Live Preview 편집성을 깨뜨리기 쉬운 selector guard 추가

### Changed
- 기본 callout 팔레트를 의미별 `lucide-*` 아이콘과 원형 outline 배지 중심으로 정리
- README에 Live Preview 편집성 원칙과 회귀 fixture / selector guard 검증 항목을 문서화

## [1.8.12] — 2026-04-26

### Changed
- `note` / `info` callout의 파란 채움 사각 아이콘을 slate 계열 원형 outline `lucide-info` 배지로 변경
- Gray override CSS snippet에서도 동일한 info/note callout 아이콘 톤을 적용해 보고서형 문서 스타일과 일관되게 정리

## [1.8.11] — 2026-04-26

### Fixed
- Live Preview에서 blockquote 문장이 화면상 여러 줄로 접힐 때 두 번째 시각 줄 클릭이 편집으로 진입하지 못하던 문제를 수정
- CM6 편집 영역의 강제 word-break / overflow-wrap / line-height 조정을 분리해 CodeMirror 커서 좌표와 시각적 줄바꿈이 어긋나지 않도록 정리
- Gray override CSS snippet의 Live Preview heading / blockquote 레이어와 간격을 조정해 제목 아래 문장 클릭 안정성 개선

## [1.8.10] — 2026-04-26

### Fixed
- Live Preview에서 펼쳐진 H3-H6 섹션 제목 클릭이 아래 콘텐츠 위젯과 겹쳐 편집으로 진입하지 못하던 문제를 수정
- Gray override CSS snippet이 Reading View용 heading block 스타일을 Live Preview 편집 라인에 강제 적용하지 않도록 selector 분리

## [1.8.9] — 2026-04-26

### Changed
- Live Preview에서 H3/H4 제목의 클릭 편집 영역이 시각적 제목 위치와 어긋나지 않도록 헤더 라인 패딩을 정리

## [1.8.8] — 2026-04-26

### Added
- **Release asset guard** — release workflow가 `README.md`, `CHANGELOG.md`, `theme.css`, `manifest.json`, `LICENSE`를 모두 첨부하는지 로컬/CI 검증에 포함
- **Marketplace README guidance** — Obsidian 테마 화면에서 README가 비어 보일 때 확인할 설치/업데이트 절차를 README에 추가

### Changed
- 수동 설치 안내를 현재 릴리즈 자산 구성에 맞게 갱신

## [1.8.7] — 2026-04-26

### Added
- **Table output polish** — wide/compact/numeric/comparison/risk/matrix/print-fit/wrap table 클래스로 보고서형 표 출력 제어 강화
- **PDF table stability** — 긴 셀, 코드 셀, 행 분할, 표 설명/출처 문구가 PDF에서 더 안정적으로 보이도록 보강
- **Mobile table affordance** — 모바일에서 넓은 표가 가로 스크롤 가능하다는 시각 힌트와 overflow 안전장치 추가
- **Table fixture document** — 주요 표 클래스와 PDF 회귀 확인용 Markdown fixture 추가

### Changed
- README에 테이블 클래스 사용법과 보고서 표 출력 가이드를 추가

## [1.8.6] — 2026-04-26

### Added
- **Parity cleanup** — Live Preview callout/table/embed spacing and Source mode chips를 Reading View 톤에 더 가깝게 보강
- **Mobile stability** — narrow viewport sidebar/search/tag panes, long filenames, wide embeds overflow를 안정화
- **Knowledge panes polish** — Outline / Bookmarks / Bases / embedded media / status bar를 v1.8.5 탐색 UI 톤으로 확장
- **Validation script** — manifest, changelog, required files, screenshots, legacy release marker, local vault sync 상태를 한 번에 확인하는 Ruby 검증 스크립트 추가

### Changed
- README / screenshots 문서의 옵션 수, 파일 구조, 스크린샷 크기, 버전 표기를 실제 v1.8.6 상태에 맞게 정리

## [1.8.5] — 2026-04-26

### Added
- **Canvas polish** — canvas node, selected/focused state, edge, controls를 문서 카드 톤으로 정리
- **Graph View tonal alignment** — dense graph에서도 node, line, highlight, label이 차분하게 보이도록 라이트/다크 색상 보강
- **Backlink / Outgoing / Search / Tag pane 정리** — 링크 탐색 패널의 hover, match, count badge, tag chip 스타일을 Graphite 톤으로 통일

## [1.8.4] — 2026-04-26

### Added
- **Settings / Style Settings polish** — setting item spacing, heading/description tone, control layout을 Graphite 문서 톤으로 정리
- **Form controls parity** — text input, dropdown, textarea, button, toggle, slider, color picker를 라이트/다크 모드에서 일관되게 조정
- **Focus state 정리** — 설정 화면 컨트롤의 focus ring과 hover feedback을 접근성 유지 범위에서 차분하게 통일

## [1.8.3] — 2026-04-26

### Added
- **Command Palette / Modal / Menu polish** — overlay surface, prompt input, selected suggestion, menu hover를 Graphite 톤으로 통일
- **Hover Preview / Popover 개선** — wiki hover preview를 가벼운 문서 카드처럼 보이도록 border, shadow, padding, heading color 정리
- **Dataview 표 parity 보강** — 일반 표와 동일한 rounded border, header, zebra, hover, 다크 모드 톤으로 정렬

## [1.8.2] — 2026-04-26

### Added
- **Sidebar / File Explorer 현대화** — 파일·폴더 hover, active file, active folder, depth path 가독성을 graphite 톤으로 강화
- **특수 체크박스 상태 강화** — `[/]`, `[>]`, `[!]`, `[?]`, `[-]`, `[*]` 상태에 의미별 배경·보더·문자 마커 적용
- **Search / Highlight 가독성 개선** — `==highlight==`, 검색 결과, suggestion highlight, flash target을 라이트/다크 모두 더 선명하게 조정

## [1.8.1] — 2026-04-26

### Added
- **Properties / Frontmatter 카드형 정리** — 메타데이터 영역의 배경, 좌측 바, row divider, key/value 색상을 보고서 톤으로 정리
- **모바일 table / Mermaid / Dataview overflow 안정화** — 넓은 구조물이 모바일 화면을 밀어내지 않고 가로 스크롤되도록 조정
- **README callout 팔레트 사용법 추가** — `[!conclusion]`, `[!recommendation]`, `[!risk]`, `[!action]`, `[!decision]` 예시 문서화

## [1.8.0] — 2026-04-26

### Added
- **PDF 출력 안정화 강화** — callout, blockquote, table, code block, mermaid, embed, image의 페이지 중간 분할을 완화하고 H2–H4가 다음 본문과 떨어져 출력되는 현상 완화
- **보고서형 callout 팔레트 확장** — `[!recommendation]`, `[!risk]`, `[!action]`, `[!decision]` 추가
- **표 모던 스타일 강화** — 헤더 배경, 첫 컬럼 강조, zebra, hover, rounded border, PDF 친화 border 톤 개선
- **Style Settings 옵션 2종 추가** — `표 모던 스타일 강화`, `PDF 블록 분할 방지 강화`

### Notes
- 기존 `[!conclusion]` Soft Sky 스타일은 유지
- 표/print 개선은 기본 적용되며, Style Settings가 있으면 명시적으로 제어 가능

## [1.7.10] — 2026-04-26

### Added
- **커스텀 callout `[!conclusion]`** — Soft Sky 팔레트로 권장 결론/제안 강조
  - 라이트: bg `#f0f9ff` / border-left `#0ea5e9` / text `#0c4a6e`
  - 다크: bg `#082f49` / border-left `#38bdf8` / text `#e0f2fe`
  - 사용법: `> [!conclusion] 권장 결론`

## [1.7.9] — 2026-04-26

### Changed
- **단락/리스트 다음에 오는 헤더 간격 확대** — 본문 이후 헤더는 간격을 크게, 연속 헤더는 그대로 유지 (sibling 셀렉터)
  - H2: 2.2em / H3: 1.8em / H4: 1.5em / H5·H6: 1.2em
  - 본문 마지막 문장과 소절 헤더 간 경계 가독성 향상

## [1.7.8] — 2026-04-26

### Changed
- **H4 스타일 통일** — v1.7.7에서 H3에 적용한 패턴을 H4(`#### 4.1`)에도 적용: 좌측 3px 액센트 바 제거 → 하단 1px 연한 회색 underline

## [1.7.7] — 2026-04-26

### Changed
- **H3 스타일 변경** — 좌측 5px 액센트 바 제거 → 하단 1px 연한 회색 underline (`rgba(0,0,0,0.08)` / 다크 `rgba(255,255,255,0.10)`)
  - "4.1 라우팅 충돌" 같은 시큐셨널 소절 표시 시 좌측 바가 시각적 잡음을 주던 문제 해소
  - H1은 기존 좌측 액센트 바 유지 (대제목 강조)

## [1.7.5] — 2026-04-26

### Fixed
- **Mermaid 노드 하단 흰색 잨여림 제거** — v1.7.3의 `overflow: visible`가 텍스트를 rect 밖으로 밀어내며 흰 빈 영역이 생성되던 현상 해소
  - `overflow: hidden` 복원 → 라벨이 rect 내부에만 머무름
  - 교체책: 폰트 11px (기존 12px)로 축소 → 멀티라인 라벨도 대부분 맞음
  - flex 수직 중앙 정렬로 그래도 잘리지 않도록 배치
- **v1.7.3 + v1.7.4 블록 통합** — 중복 셀렉터 제거

### Author Note
- 극단적으로 긴 라벨은 여전히 컷트될 수 있으므로 **소스에 `<br/>` 명시적 줄바꿈** 권장 (memory 가이드 참조)

## [1.7.4] — 2026-04-26

### Fixed
- **Mermaid 노드 내부 배경 색 불일치 해소** — `<rect>` fill과 `foreignObject`/`nodeLabel` 내부 디비 배경이 달라 노드 안에 색상 이음이 보이던 현상을 수정. 라벨 측 배경을 전부 transparent로 고정 → rect fill이 유일 색상 소스
- **Edge label 배경**은 컨테이너 카드 색과 동일하게 `--background-primary`로 고정 (엣지와 겹치는 자리에서 잠식의 랜드마크 제거)

## [1.7.3] — 2026-04-26

### Fixed
- **Mermaid 노드 라벨 잘림 완화** — 박스 안 멀티라인 텍스트(`<br/>`)가 잘리는 현상을 완화:
  - 노드 서점 12px / 엣지 라벨 11px / 클러스터 제목 12.5px 하향 조정
  - line-height 1.25, `word-break: keep-all`, `overflow-wrap: break-word`
  - `foreignObject overflow: visible` → 하단 잘릴하더라도 표시 유지
  - flex 수직 중앙 정렬로 파단단 레이아웃 근접도한 동작
- **권장: 장문 라벨은 mermaid 소스에 `<br/>`로 명시적 줄바꿈 넣기** (Mermaid 자체 측정 한계 회피)

## [1.7.2] — 2026-04-26

### Changed
- **PDF 푸터 간소화** — 좌측 "Owen Graphite" 제거, 우측 접두어 "p. " 제거 → `"1 / 19"` 형식만 유지

## [1.7.1] — 2026-04-26

### Fixed
- **PDF 첫 페이지 헤더 값(VALUE) 미표시 문제 해소** — v1.6.0에서 `.markdown-preview-sizer` 단일 컨테이너로 줄인 바인딩을 4개 컨테이너(`sizer`/`view`/`section`/`rendered`)로 복원. 다일과 플랫폼별 PDF 렌더 DOM 차이에 대한 동시 대응.

## [1.7.0] — 2026-04-26

### Added
- **#1 액티브 탭 인디케이터** — `.workspace-tab-header.is-active::before` 2px 액센트 바
- **#3 모바일 분기** — `.is-mobile` 헤더 패딩, 본문 폰트 16px, PDF 헤더 자동 숨김
- **#5 PDF 푸터 페이지 번호** — `@page @bottom-left/right` 페이지 카운터
- **#6 Graph view 톤 일치** — 라이트/다크 line·text·fill 변수 정합
- **#7 검색 결과 하이라이트 강화** — 황색 배경 + 라운드 보더
- **#8 임베드 노트 좌측 액센트** — 3px 액센트 + secondary bg + title 강조
- **#9 커스텀 체크박스 8종** — `x`, `/`, `-`, `>`, `<`, `?`, `!`, `*` 컬러 매핑 (Minimal 호환)
- **#10 태그 칩 호버 피드백** — translateY -1px + shadow + accent bg
- **#11 통일 `:focus-visible`** — WCAG 2.4.7 준수 2px outline (모든 인터랙티브 요소)
- **#12 `prefers-contrast: more`** — 고대비 모드 자동 분기 (border 강도, 링크 underline)

### Notes
- 모든 변경은 **추가 전용**(additive). 기존 셀렉터 미수정 → 회귀 위험 최소화
- `@layer` 리팩토링 및 Callout 시각 통일은 v2.0에서 진행

## [1.6.1] — 2026-04-26

### Added
- **Editing Toolbar 플러그인 좌측 여백 8px** — 사이드바 분리선과 툴바 사이 시각적 간격 확보
  - 셀렉터: `.editingToolbarModalBar { margin-left: 8px }`

## [1.6.0] — 2026-04-26

### Changed
- **테마 이름 `Owen Graphite Document` → `Owen Graphite`**
  - `manifest.json#name`, `appearance.json#cssTheme`, 종속 텍스트 일괄 교체
  - Style Settings ID(`owen-graphite-document`)와 CSS 변수(`--ogd-*`)는 기존 사용자 설정 보존을 위해 그대로 유지

### Fixed
- **PDF 첫 페이지 헤더 값 부착 컨테이너 5→01개로 정리** — v1.4.5–1.5.1 누적 방어 코드 제거
  - `.markdown-preview-sizer::before/::after`만 유지 (가장 안정적)
  - PDF DOM 이중 렌더링 위험 차단 + ~30줄 감축
- **무효 CSS 문법 제거** — `body.ogd-page-* @media print { @page { size: ... } }` 불당 중첩 제거
  - `@page { size: ... }`는 body class로 조건화 불가 (Chromium 제약). README에 명시.
  - Style Settings `PDF 페이지 크기` 옵션은 "Preview 폭 힌트"로 설명 명확화 (실제 PDF 크기는 Obsidian Export 다이얼로그에서 설정)
- **오타 수정**: "삼이드바" → "사이드바" (theme.css 주석 · Style Settings 설명 · CHANGELOG 다수 위치)

### Added
- **Mermaid 다크 모드 텍스트 가독성 수정**
  - SVG `<text>`, `.nodeLabel`, `.edgeLabel`이 검은색마 남아 다이어그램이 안 보이던 문제 해결
  - cluster rect 배경도 다크 펠리트에 맞게 보정
- **Reading view 내부 링크 chip 스타일** (Live Preview와 패리티)
  - `[[위키링크]]`가 Reading view에서도 연한 파란색 chip으로 표시
  - hover 시 더 진한 배경 + 밑줄
  - unresolved 링크는 호박 조 + 점선 밑줄
  - 다크 모드 패리티 동시 적용
- **코드 언어 배지 × 복사 버튼 중첩 해소**
  - 배지를 `right: 48px`로 이동, hover 시에만 표시
  - 평소 코드블록은 멀끔하게 유지

## [1.5.1] — 2026-04-26

### Fixed
- v1.5.0의 사이드바가 본문 줄에만 짧게 그려지던 문제 수정 — 샘플 이미지는 라벨+본문을 모두 덮는 김이의 상하 막대로 표현
  - 본문 재원소에 `padding-top: 16px` + `top: 0`으로 이동 → 사이드바 길이가 라벨 영역까지 확장
  - 라벨의 left/right offset을 13px로 조정해 사이드바와 겹치지 않게 안쪽 배치
  - 라벨 top도 2px로 미세 조정해 사이드바 상단과 정렬

## [1.5.0] — 2026-04-26

### Added
- **PDF 첫 페이지 헤더 모던 디자인 (Design ② Side Bar + Two-line)**
  - 좌·우 각각 **라벨(소문자, 상단) + 본문(하단) 2줄 구조** + **3px 수직 사이드바**
  - 신규 Style Settings 옵션 3개:
    - `ogd-fp-right-label` (variable-text): 우측 라벨 (예: "PREPARED BY")
    - `ogd-fp-left-label` (variable-text): 좌측 라벨 (예: "CONFIDENTIAL")
    - `ogd-fp-label-color` (variable-color, 기본 `#6b7280`): 좌·우 라벨 공통 색상
  - 기존 옵션 재활용 (하위 호환):
    - `ogd-first-page-header` → 우측 본문
    - `ogd-first-page-header-color` → 우측 사이드바 색상 (기본 `#111827` Dark)
    - `ogd-first-page-header-left` → 좌측 본문
    - `ogd-first-page-header-left-color` → 좌측 사이드바 색상 (기본 `#0ea5e9` Sky)
  - 라벨은 8pt SemiBold + uppercase + 1.8px letter-spacing, 본문은 10.5pt Medium
  - 라벨·본문 모두 비워두면 표시 안 함 (하위 호환)
  - 라벨은 `body::before/::after`, 본문은 `.markdown-preview-sizer ::before/::after` 등 여러 컨테이너에 분리하여 서로 이중 렌더링 아닌 단일 위치에 배치

## [1.4.12] — 2026-04-26

### Added
- PDF 첫 페이지 **좌측 상단** 머리말 추가 — Style Settings 사용자 입력형
  - `ogd-first-page-header-left` (variable-text): 좌측에 표시할 문구 (예: "2026 Q2", "프로젝트 코드")
  - `ogd-first-page-header-left-color` (variable-color, 기본 `#6b7280` 그레이): 문구 색상
  - `::after` 의사요소로 좌측 배치, 기존 우측 `::before`와 독립적으로 제어
  - 둘 다 비워두면 표시 안 함

## [1.4.11] — 2026-04-26

### Changed
- 첫 페이지 헤더 폰트 스택을 본문 스택과 완전 일치 (Pretendard 1순위)
  - macOS에서 Pretendard가 설치되어있으면 본문과 동일한 Pretendard로 표시
  - Windows에서도 동일한 스택 적용 (Pretendard → Apple SD Gothic Neo → Noto Sans KR → Segoe UI → Malgun Gothic → sans-serif)
  - weight 400 (Regular)로 유지 — 모든 OS에서 안전 + `font-synthesis: weight style`로 필요 시 합성

## [1.4.10] — 2026-04-26

### Fixed
- v1.4.9에서도 Times serif로 fallback되던 문제 최종 수정
  - 폰트 스택 1순위를 **`-apple-system`** + **`BlinkMacSystemFont`**로 변경 (macOS의 SF Pro 강제 적용 시스템 폰트는 절대 serif fallback 안 됨)
  - `font-weight: 400` (Regular)로 낮춰 weight 매칭 실패 제거
  - `font-synthesis: weight style` 명시로 합성 허용
  - `.markdown-preview-sizer::before`, `.markdown-preview-section > div:first-child::before` 추가로 Obsidian 실제 print 컨테이너에 직접 부착
  - 모든 속성에 `!important` 추가하여 print 룰 완전 제어

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
- PDF/인쇄 출력 시 좌하단에 표시되던 "Owen Graphite" 푸터 텍스트 제거
  - `@page { @bottom-left { content: "Owen Graphite" } }` 블록 삭제
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
