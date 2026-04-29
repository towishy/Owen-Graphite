# Changelog

All notable changes to **Owen Graphite** are recorded here.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and
this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.22.12] — 2026-04-30 — Windows forced chrome rollback

### Fixed
- v2.22.11에서도 Windows 세로 리본바 첫 번째 아이콘이 비정상으로 보이던 문제를 막기 위해 리본 크기 강제 가드를 비활성화.
- Windows titlebar를 검은색으로 고정하던 v2.22.9 레이어를 비활성화해 Obsidian 기본 titlebar/tabbar 동작으로 되돌림.

### Changed
- 실제 Windows DOM 확인 전까지 non-macOS titlebar/tabbar/ribbon 구조 강제 복원 selector를 추가하지 않음.

## [2.22.11] — 2026-04-30 — Windows ribbon guard after tabbar rescue rollback

### Fixed
- v2.22.10에서 Windows 세로 리본바 첫 번째 아이콘이 세로로 늘어지던 문제 수정.
- 리본 아이콘까지 잡아 늘리던 broad `[role="tab"]` tabbar rescue 블록을 비활성화하고, Windows/non-macOS 리본 버튼·SVG 크기를 32px/18px로 복원.

### Preserved
- v2.22.9의 Windows dark titlebar 색상 복원 유지.
- macOS Glass chrome 유지.

## [2.22.10] — 2026-04-30 — Windows dark-mode tabbar structural rescue

### Fixed
- Windows dark theme에서 titlebar 색상은 적용되지만 탭이 계속 보이지 않는 문제에 대응.
- non-macOS desktop 한정으로 `.workspace-tabs`, `.workspace-tab-header-container`, `.workspace-tab-container`, tab header descendant 전체의 flex 슬롯·높이·가시성·텍스트 색상을 강하게 복구.

### Preserved
- macOS Glass chrome 유지.
- 좌측 라인 영구 밴 정책 위반 없음.

## [2.22.9] — 2026-04-30 — Windows dark titlebar + tabbar visibility reset

### Fixed
- Windows Obsidian에서 v2.22.8 이후에도 탭이 보이지 않고, titlebar가 예전의 진한 회색 대신 연한 회색으로 보이던 문제에 대응.
- Windows/Electron body class 차이를 고려해 `body:not(.mod-macos):not(.is-mobile)` 범위에서 titlebar/tabbar를 진한 회색 chrome으로 복원하고, tab header/title/button의 표시·크기·색상을 강제 복구.

### Preserved
- macOS Glass chrome 유지.
- 좌측 라인 영구 밴 정책 위반 없음.

## [2.22.8] — 2026-04-30 — Windows default titlebar/tabbar rollback

### Fixed
- Windows Obsidian titlebar 왼쪽에 아래로 내려오는 회색 라인이 보이고, v2.22.7에서도 탭이 보이지 않던 문제에 대응.
- 실패한 v2.22.0~v2.22.7 Windows/Linux chrome 강제 패치 묶음을 비활성화해 Windows가 Obsidian 기본 titlebar/tabbar 레이아웃을 다시 사용하도록 롤백.

### Preserved
- macOS Glass chrome 유지.
- 좌측 라인 영구 밴 정책 위반 없음.

## [2.22.7] — 2026-04-30 — Windows tabbar layout slot restoration

### Fixed
- v2.22.6에서도 Windows Obsidian 상단 탭이 보이지 않는 문제에 대응해, Windows/Linux 한정으로 `.workspace-tabs` flex column, `.workspace-tab-header-container` auto header row, `.workspace-tab-container` flexible body 레이아웃 슬롯을 명시 복원.
- 탭 헤더/탭 제목/새 탭 버튼/탭 목록 버튼/titlebar 버튼의 최소 크기와 flex 슬롯을 복구해 탭바가 0px 또는 화면 밖으로 접히지 않도록 보강.

### Preserved
- macOS Glass chrome 유지.
- 좌측 라인 영구 밴 정책 위반 없음.

## [2.22.6] — 2026-04-30 — Windows default chrome restoration

### Fixed
- Windows Obsidian에서 Owen Graphite 적용 시 상단 탭/버튼이 사라지고 왼쪽 Obsidian 아이콘만 보이던 문제의 root fix 적용.
- EOF 복원 패치로 Windows/Linux에서 v2.22.0~v2.22.5의 솔리드 chrome 덮어쓰기를 무력화하고, v1.8.66에서 확인된 공통 데스크톱 탭 스타일을 다시 적용.
- macOS Glass chrome은 그대로 유지하면서 Windows/Linux 탭/버튼은 `opacity`, `visibility`, text/icon color를 명시적으로 복원.

### Preserved
- macOS Glass chrome 유지.
- 좌측 라인 영구 밴 정책 위반 없음.

## [2.22.5] — 2026-04-30 — Windows chrome rollback + conservative visibility only

### Fixed
- v2.22.3/v2.22.4의 광범위한 `display:flex` / workspace layout 강제 패치를 제거해, Windows 상단 chrome 레이아웃을 Obsidian 기본 구조에 다시 맡김.
- 실제 Windows DOM 확인 전까지 구조 변경을 중단하고, Windows/Linux 한정으로 색상 토큰, `opacity`, `visibility`, text/icon color만 보수적으로 보강.

### Preserved
- macOS Glass chrome 유지.
- 좌측 라인 영구 밴 정책 위반 없음.

## [2.22.4] — 2026-04-30 — Windows workspace-tabs layout correction

### Fixed
- v2.22.3 적용 후 Windows 상단에서 왼쪽 Obsidian 아이콘만 보이고 탭/버튼이 계속 보이지 않는 문제를 보정.
- 원인 후보: v2.22.3의 넓은 `display:flex` 복구가 `.workspace-tabs`를 기본 column 레이아웃이 아닌 row 흐름으로 만들 수 있어, 탭바/본문 레이아웃이 깨지는 케이스.
- Windows/non-macOS 한정으로 `.workspace-tabs`는 `flex-direction: column`, `.workspace-tab-header-container`는 auto header, `.workspace-tab-container`는 flex body로 되돌림.

### Preserved
- macOS는 `body.mod-macos` 제외로 기존 Glass chrome 유지.
- 좌측 라인 영구 밴 정책 위반 없음.

## [2.22.3] — 2026-04-30 — Windows viewport-independent tabbar rescue

### Fixed
- Windows Obsidian에서 기본 테마는 탭/버튼이 보이나 Owen Graphite로 전환하면 즉시 사라지는 문제를 추가 보강.
- 기존 v2.22.0~2.22.2 복구가 모두 `@media (min-width: 701px)` / `:not(.is-mobile)` 조건 안에 있어 적용되지 않을 수 있는 케이스를 제거하고, non-macOS tabbar 영역에 조건 없는 최소 표시 복구 적용.
- 탭바 컨테이너, 탭, 탭 내부 텍스트/아이콘/닫기 버튼, 새 탭/탭 목록 버튼, titlebar 버튼의 `display`, `visibility`, `opacity`, `color`, `background`, `filter`를 강제 복구.

### Preserved
- macOS는 `body.mod-macos` 제외로 기존 Glass chrome 유지.
- 좌측 라인 영구 밴 정책 위반 없음.

## [2.22.2] — 2026-04-30 — Windows emergency tab/button visibility fallback

### Fixed
- v2.22.1 적용 후에도 일부 Windows Obsidian 환경에서 탭/버튼이 보이지 않던 문제에 대응하는 emergency fallback 추가.
- Windows/non-macOS 한정으로 Obsidian native tab/titlebar/icon 변수(`--tab-*`, `--titlebar-*`, `--icon-color*`)를 솔리드 값으로 강제 환원.
- `.workspace-tab-header`뿐 아니라 `[role="tab"]`, 탭바 내부 `button`, `.clickable-icon`, 새 탭 버튼, 탭 목록 버튼, 닫기 버튼, SVG 아이콘까지 visibility/opacity/color를 강제 보강.

### Preserved
- macOS는 `body.mod-macos` 제외로 기존 Glass chrome 유지.
- 좌측 라인 영구 밴 정책 위반 없음.

## [2.22.1] — 2026-04-30 — Windows/Linux chrome hardening

### Fixed
- v2.22.0 적용 후에도 Windows Obsidian에서 탭/버튼이 계속 흐리거나 보이지 않을 수 있던 문제 보강.
- 탭 내부 surface뿐 아니라 `.workspace-tab-header` parent surface까지 솔리드 배경/보더/그림자를 적용해 실제 Windows DOM 차이에 대응.
- 탭바 버튼 전체(`.workspace-tab-header-tab-list`, `.workspace-tab-header-new-tab`, `.clickable-icon.mod-new-tab`), 좌/우 사이드바 토글, 탭 닫기 버튼, titlebar 버튼 색상/opacity를 Windows/non-macOS 한정으로 강제 보강.

### Preserved
- macOS는 `body.mod-macos` 제외로 기존 Glass 탭/버튼 룩 유지.
- 좌측 라인 영구 밴 정책 위반 없음.

## [2.22.0] — 2026-04-30 — Windows/Linux chrome visibility hotfix (samples-first approved)

### Fixed
- **윈도/리눅스 Obsidian에서 탭 + 좌/우 사이드바 토글 버튼이 거의 안 보이던 문제** 수정. 원인: macOS 기준 Glass(반투명 그라디언트 + `backdrop-filter: blur`)로 chrome 분리감을 만들었으나, 윈도/리눅스 Electron에서 `backdrop-filter`가 fallback되면 거의 순백 그라디언트가 동일 톤 컨테이너에 묻혀 형체 소실.

### Added
- `body.mod-windows` / `body:not(.mod-macos):not(.is-mobile)` 한정 솔리드 chrome 토큰 세트 도입(`--ogd-win-titlebar-*`, `--ogd-win-tabbar-*`, `--ogd-win-tab-*`, `--ogd-win-toggle-*`).
  - **타이틀바**: 본문보다 진한 톤(라이트 `#e2e8f0` / 다크 `#0f1419`) + 1px 보더.
  - **탭바**: 타이틀바보다 약간 밝은 톤(라이트 `#eef2f7` / 다크 `#1c2128`) — 3단 hierarchy.
  - **활성 탭**: 솔리드(라이트 `#ffffff` / 다크 `#2c333d`) + 1px 보더 + soft shadow (카드처럼 들림).
  - **비활성 탭**: 옅은 솔리드 배경 + 1px 보더 + opacity 0.78 → 0.95 완화.
  - **사이드바 토글 (좌/우)**: 솔리드 배경 + 진한 보더 + 그림자, hover 시 톤 변경.
- **blur fallback 가드** (`@supports not (backdrop-filter)`): 모든 OS의 backdrop-filter 미지원 환경에서도 동일한 솔리드 톤으로 chrome 가시성 보장.

### Preserved
- macOS Glass 정체성 100% 유지 (기본값 = 현재 룩, 변경 없음).
- 좌측 라인 영구 밴 정책 / Glass+Shadow 코어 정책 위배 없음. 윈도/리눅스는 OS가 backdrop-filter를 일관 지원하지 않는 환경 특성상 "솔리드 + 그림자"로 표현(정책 § 적용 범위 예외 절차에 따른 핫픽스).

### Workflow
- 샘플-우선 정책 준수: [`docs/fixtures/v2.22-windows-chrome-preview.html`](docs/fixtures/v2.22-windows-chrome-preview.html) 사용자 승인 후 적용.
- EOF 추가 패치: 기존 셀렉터 수정 없음.

## [2.21.0] — 2026-04-29 — Canvas, Inputs & Modals (8 items, samples-first approved)

### Added
1. **Canvas group / frame (A1)** — `.canvas-frame` 점선 보더 + 옅은 카테고리 fill (라이트 teal / 다크 mint) + floating chip 라벨 (좌측 라인 X).
2. **Canvas minimap (A2)** — `.canvas-minimap` floating glass card + brand viewport 박스.
3. **Slider / range (D1)** — `input[type="range"]` 글래스 thumb (4px halo) + 그라디언트 fill track + active scale + focus-visible 6px ring.
4. **Dropdown select (D2)** — `.dropdown`, `select.dropdown` chrome + focus-visible 2px inset ring.
5. **Number stepper (D3)** — `input[type="number"]` 글래스 + mono tabular-nums + WebKit spinner hover opacity.
6. **Notice action button (C1)** — `.notice .notice-action` 글래스 mini button + hover lift, `.mod-cta`는 brand fill.
7. **Release notes / Help modal row (C2)** — `.release-notes-modal .release-notes-item` row glass hover + 버전 mono pill.
8. **Code block copy button + success pulse (E2)** — `pre > button.copy-code-button` opacity 0→1 (hover 노출) + 글래스 chip + `.copied` green pulse 600ms (reduce-motion 호환).

### Workflow
- 샘플-우선 정책 준수: [`docs/fixtures/v2.21-preview.html`](docs/fixtures/v2.21-preview.html) 사용자 승인 후 적용.
- 좌측 라인 ban / Glass+Shadow core 정책 100% 준수 (full outline / inset ring / opacity 강조만 사용).

## [2.20.1] — 2026-04-29 — Hotfix: search-input double-ring

### Fixed
- **F1 Search input 이중 ring 제거** — v2.20.0 `.search-input-container` 글래스 pill과 내부 `<input>`의 기존 focus ring(v1.8.56 잔재)이 동시 노출되어 이중 halo 박스가 나타나는 사고 수정. wrapper는 inset ring만, 내부 input은 모든 chrome(border/outline/box-shadow) 완전 제거.
- Style Settings 검색창 아이콘 오버랩 해소 (wrapper padding 0으로 되돌림).

## [2.20.0] — 2026-04-29 — Inputs & System Surfaces (5 items, samples-first approved)

### Added
1. **Toggle switch glass (F3)** — `.checkbox-container` 글래스 track + floating thumb (떠 있는 그림자), `is-enabled`는 accent fill + ring (좌측 라인 X).
2. **Search input + filter chips (F1)** — `.search-input-container` glass pill + `:focus-within` 3px brand ring + active toggle pill 통일.
3. **Community plugins / themes cards (E4)** — `.community-item` 글래스 카드 + hover lift + `mod-installed` green pill.
4. **Pane title count badges (D2)** — outline/backlinks/outgoing/tag 카운트를 mono pill로 통일 (brand/teal/amber 카테고리별 색).
5. **Drop snap target hint (G1)** — `.is-drop-target`, `.is-drop-target-before/after` 전체 둘레 dashed outline + 얙은 brand fill (좌측 라인 패턴 완전 제거).

### Workflow
- 샘플-우선 정책 준수: [`docs/fixtures/v2.20-preview.html`](docs/fixtures/v2.20-preview.html) 사용자 승인 후 적용.
- v2.19.0 D2 토큰(`--og-accent-pill-*`, `--og-glass-bg-strong`) 적극 재사용.

## [2.19.0] — 2026-04-29 — Editor Depth, System Cleanup & Glass Surface Sweep (10 items, samples-first approved)

### Added
1. **Task checkbox custom glyphs (B4)** — Tasks/Projects 컨벤션 7종(`[ ]` `[x]` `[/]` `[?]` `[!]` `[>]` `[-]`) 색별 매핑: 완료=green, 진행=accent split, 질문=amber, 중요=rose, 액션=purple, 취소=mute strikethrough.
2. **Heading anchor copy hint (B5)** — H1–H6 hover 시 커틀 아이콘 `⎘` fade-in (v2.14 `#` 해시태그 결합). reduce-motion 안전망.
3. **Templater suggestion glass (C1)** — `.suggestion-container.mod-templater`, `.menu.templater-menu` 반투명 + blur(14) + lift shadow (커맨드 팔레트 패턴 재사용).
4. **Nested tag pill hierarchy (C5)** — `a.tag[href*="/"]` 세그먼트 그라디언트 + word-break 안정화.
5. **Token migration Phase 1 (D2)** — `--og-accent-pill-{bg,fg,border}` `--og-glass-bg-strong` 신규 토큰 도입 (사용자 override 용이).
6. **PDF viewer chrome (A1)** — `.pdf-toolbar`, `.pdf-sidebar`, `.pdf-thumbnail-view` 글래스 카드 + lift shadow + 8px inset margin. 활성 페이지 accent ring (좌측 라인 X).
7. **Audio / Video player chrome (A2)** — `.video-embed`, `.media-embed`, `audio` chrome wrapper 반투명 + blur(12) + soft shadow.
8. **Canvas node cards glass (B1)** — `.canvas-node` 반투명 fill + blur(8) + 2단 shadow, hover lift / `.is-focused` ring (좌측 라인 X). `.canvas-edge-label` pill 통일.
9. **Floating glass status bar (D1)** — `.app-container .status-bar` 자체를 floating glass bar로 (8px inset margin), word count는 accent pill.
10. **Date / Color picker popover (C3)** — `.flatpickr-calendar`, `.daterangepicker`, color picker 글래스 카드 통일. today=14% / selected=full accent + lift shadow.

### Workflow
- 샘플-우선 정책 준수: [`docs/fixtures/v2.19-preview.html`](docs/fixtures/v2.19-preview.html) 사용자 승인 후 적용.
- 좌측 라인 영구 밴 + Glass+Shadow 3종세트 정책 전역 준수.

## [2.18.0] — 2026-04-29 — All-A Surface Sweep (5 items, samples-first approved)

### Added
1. **Workspace split divider polish (A1)** — `.workspace-leaf-resize-handle` hover 시 1px→2px brand fade + glow + col/row-resize cursor (전체 라인, 좌측 전용 X).
2. **Drag preview ghost glass (A2)** — `.is-being-dragged` (tab/nav-file/folder/tree-item) opacity 0.85 + rotate(1deg) scale(1.02) + lift shadow + blur(10).
3. **Vault switcher / Workspaces 모달 (A3)** — `.modal.mod-vault-switcher`, `.modal.mod-workspaces`, `.workspaces-modal` glass card + row hover lift + active pill.
4. **Status bar separator (A4)** — `.status-bar-item + .status-bar-item::before` 1px×12px 수직 separator + item hover tint (구분용 세퍼레이터 · 강조 용도 아님 → 좌측 라인 정책 예외).
5. **Modal close (×) chrome (A5)** — `.modal-close-button` mute → hover 시 rose tint + inset ring (destructive 액션 구분) + focus-visible brand ring.

### Workflow
- 샘플-우선 정책 준수: [`docs/fixtures/v2.18-preview.html`](docs/fixtures/v2.18-preview.html) 사용자 승인 ("A로 진행") 후 적용.
- D1 토큰(`--og-glass-border/-shadow-lift`, `--og-accent-bg-*`) 적극 재사용으로 일관성 확보.

## [2.17.0] — 2026-04-29 — Surface Gaps & Tokenization (5 items, samples-first approved)

### Added
1. **Scrollbar polish (A4)** — WebKit `::-webkit-scrollbar` 8px overlay glass thumb → hover 12px 확장 + brand 색 전환, Firefox `scrollbar-color` fallback 포함 (workspace/cm-scroller/leaf/modal/menu 일괄).
2. **Empty state 일러스트 (A1)** — `.empty-state::before` 72×72 그라디언트 glass square + `.empty-state-action` brand pill button.
3. **Wiki-link unresolved 톤 (B5)** — `a.internal-link.is-unresolved` muted color + dashed underline + `?` superscript, hover 시 rose 톤으로 전환 (CM6 포함).
4. **Calendar 플러그인 today/active (C4)** — `data-type="calendar"` .day 원형 fill: today=14% · active/is-selected=24% + 1px inset ring, 좌측 라인 X.
5. **CSS 읽수 토큰화 v2 (D1)** — `--og-accent-bg-{hover,active,strong}` · `--og-accent-border-soft/ring` · `--og-{teal,rose,amber,green}-bg-soft/border-soft` · `--og-glass-{border,shadow-md,shadow-lift}` 전역 토큰 도입 (하위 호환 유지).

### Workflow
- 샘플-우선 정책 준수: [`docs/fixtures/v2.17-preview.html`](docs/fixtures/v2.17-preview.html) 사용자 승인 후 적용.
- 릴리즈 철학: chrome 눠라진 표면(scrollbar/empty state/calendar) 메우고, 향후 패치 재사용을 위한 토큰 레이어 확립.

## [2.16.0] — 2026-04-29 — Interaction & A11y Deep Polish (5 items, samples-first approved)

### Added
1. **Bookmarks 패널 chrome (A4)** — `.workspace-leaf-content[data-type="bookmarks"]` 항목 hover lift + active pill + `.tree-item-flair` count pill (teal). 좌측 라인 X.
2. **CM6 fold gutter polish (B1)** — `.cm-gutter.cm-foldGutter .cm-gutterElement` mute → brand on hover + smooth color/transform transition.
3. **Dataview inline field chip (C1)** — `.dataview.inline-field-key/-value` 로 key=accent pill + value=mono pill 2단 chip 통일 (Properties · tag pill 계열 일관성).
4. **`prefers-reduced-motion` 전면 안전망 (D1)** — progress bar / sync pulse / ribbon / menu / bookmarks / fold gutter / hover lift · 전역 `animation-duration: 0.001ms` cap.
5. **`prefers-contrast: more` 대응 (D5)** — chrome border 0.28→0.62 · `--text-muted` solid 톤 · focus-visible ring 0.28→0.55 · modal/popover 그림자 강화.

### Workflow
- 샘플-우선 정책 준수: [`docs/fixtures/v2.16-preview.html`](docs/fixtures/v2.16-preview.html) (RM/HC 토글 포함).
- 사용자 "D로 진행 계속" 명시로 일괄 적용 · 서밋/릴리즈.

## [2.15.0] — 2026-04-29 — Surfaces & A11y Polish (5 items, samples-first approved)

### Added
1. **Context menu glass (A1)** — `.menu` blur(12) + lift shadow + `.menu-item.selected/.is-active/.mod-active` 를 brand 14% bg pill (좌측 라인 X), separator 톤 통일.
2. **Ribbon active pill (A4)** — `.workspace-ribbon .side-dock-ribbon-action.is-active/.mod-active` 좌측 라인 잔재 제거 → full pill bg + 1px inset ring + soft shadow.
3. **Mermaid block chrome (B3)** — `.block-language-mermaid` 글래스 카드 + 우상단 "MERMAID" badge (code/embed 패턴 일관성).
4. **Tasks 플러그인 chrome (C1)** — `task-due/scheduled/start` 자동 pill (amber) · `task-overdue` rose · `task-done` green · 완료 항목 strikethrough + 0.55 opacity.
5. **Focus-visible ring 통일 (D2)** — input/textarea/select/button/a/clickable-icon/tab-header/nav-title/suggestion/menu-item/ribbon `:focus-visible` 3px brand ring 표준화 (라이트 28% / 다크 36%).

### Workflow
- 샘플-우선 정책 준수: [`docs/fixtures/v2.15-preview.html`](docs/fixtures/v2.15-preview.html).
- 사용자 "모두 진행 + 서밋/릴리즈" 명시로 일괄 적용.

## [2.14.0] — 2026-04-29 — Chrome & Indicator Polish (5 items, samples-first approved)

### Added
1. **Sync / Cloud 인디케이터 Polish** — Status bar `plugin-obsidian-sync` / `plugin-git` / aria-label 매칭 항목을 glass pill + 상태색 4단계 (ok/busy/warn/err), busy는 `og-sync-pulse` 애니메이션.
2. **Settings 모달 검색 결과 강조** — `.modal.mod-settings .setting-item` 를 row glass + hover lift, `mark` / `search-result-file-matched-text` 를 underline-gradient HL.
3. **Heading anchor `#` hover 인터랙션** — H1–H6 좌측 fade-in `#` (`::before`), `@media print` 에서 비활성.
4. **Hover popover favicon + 도메인 breadcrumb** — `.popover.hover-popover .external-link-popover-header` 헤더 chrome 추가 (그라디언트 favicon + accent 도메인 + crumb).
5. **Frontmatter Properties 인라인 편집 polish** — `.metadata-container input` 에 focus glass ring (3px), `.multi-select-pill` 을 v2.13 chip 디자인 (teal 그라디언트 + dot)으로 통일.

### Workflow
- 샘플-우선 정책 준수: [`docs/fixtures/v2.14-preview.html`](docs/fixtures/v2.14-preview.html).
- 리드미 스크린샷: `screenshots/readme/v2.14-preview-{light,dark}.png` (Playwright 캡처).

## [2.13.0] — 2026-04-29 — Reading Polish & Surfaces (9 items, samples-first approved)

### Added
1. **Search 결과 패널 Polish** — `.search-result-file-match` 를 row glass + hover lift, match HL을 underline-gradient 로 강조.
2. **Graph view legend / control glass** — `.graph-controls` 우상단 글래스 카드(blur·border·shadow), local graph 동일 적용.
3. **Mobile bottom toolbar 재정비** — `.mobile-toolbar` 를 floating glass card 로, `safe-area-inset-bottom` 보강.
4. **Print TOC 유틸리티** — `.ogd-print-toc` (A3 PDF cover-page 다음 자동 목차 페이지 + 점선 leader + accent 카운터).
5. **Footnote 패널 Polish** — `.footnotes` 글래스 카드 + `FOOTNOTES` 소제목 + 번호 알약(pill), `sup.footnote-ref` 도 동일 pill.
6. **Inline tag pill v2** — 본문 `a.tag` / CM6 `.cm-hashtag` 를 tag-pane 알약 디자인으로 통일 (teal 그라디언트 + border).
7. **Callout 다크 패리티 재감사** — note/warning/danger/success 다크 배경·border·텍스트 톤 보강 (v2.11 quote no-left-line 이후 일부 대비 약화 해소).
8. **Dataview 표 자동 매핑** — `.block-language-dataview table` 에 wide-table·sticky header·zebra·tabular-nums 자동 적용 (`@media print` 에서 sticky 비활성).
9. **docs/style-settings.md 신설** — 33개 옵션 풀 레퍼런스 문서 (README 분류 표 보강, 죽은 링크 해소).

### Workflow
- 샘플-우선 정책 준수: [`docs/fixtures/v2.13-preview.html`](docs/fixtures/v2.13-preview.html).
- 리드미 스크린샷: `screenshots/readme/v2.13-preview-{light,dark}.png` (Playwright 캡처).
- 베이스라인 정책 갱신: README는 v2.13.0 기준, 이전 마일스톤 마커는 CHANGELOG 로 위임.

## [2.12.0] — 2026-04-29 — Panels & Code Polish (6 items, samples-first approved)

### Added
1. **Tab bar 활성 탭 underline** — 그라디언트 underline + soft shadow (좌측 라인 X, outer ring X).
2. **Backlinks / Outgoing card lift** — 우측 패널 링크 항목을 padded glass row + hover lift.
3. **테이블 zebra + sticky header** — 짝수행 미세 톤 + accent 밑줄 sticky header.
4. **Code block line numbers** (opt-in) — `pre.line-numbers` 에 CSS counter 기반 좌측 행 번호 + 1px divider.
5. **Embed 노트 카드 Polish** — `.markdown-embed` 글래스 카드 + 우상단 "EMBED" badge.
6. **Glass 강도 변수** — `--og-glass-blur` CSS 변수 도입 (Style Settings으로 사용자가 8/12/16/20px override 가능).

### Workflow
- 샘플-우선 정책 준수: [`docs/fixtures/v2.12-preview.html`](docs/fixtures/v2.12-preview.html).
- 리드미 스크린샷: `screenshots/readme/v2.12-preview-{light,dark}.png`.

## [2.11.0] — 2026-04-29 — Reading & Properties Polish (5 items, samples-first approved)

### Added (#2 Tab glow skipped per user)
1. **Properties 패널 Glass** — `.metadata-container` 카드형 glass + tabular-nums (다크 대응).
2. **본문 강조 종류별 차등** — strong/em/mark/del 톤·굵기·배경 분리 (CM6 클래스 포함).
3. **인용문 좌측 라인 대체** — 4px bar 제거 → 배경 tint + radius 8px + 코너 글리프(“) (no-left-line 정책 일관성).
4. **Reading view 진행률 인디케이터** — scroll-driven animation 기반 sticky 2px 그라디언트 바 (`@supports (animation-timeline: scroll())`, fallback safe).
5. **Code block 언어 라벨 + copy 일체화** — 우상단 chrome 모듈로 통합 (data-lang ::before + .copy-code-button glass).

### Workflow
- 샘플-우선 정책 준수: [`docs/fixtures/v2.11-preview.html`](docs/fixtures/v2.11-preview.html) 사용자 승인 후 적용.
- 리드미 스크린샷: `screenshots/readme/v2.11-preview-{light,dark}.png`.

## [2.10.0] — 2026-04-29 — 12 Improvements Pack (samples-first approved)

### Added (12종 개선 · 좌측 라인 영구 밴 + Glass+Shadow 코어 정책 준수)
1. **Quick Switcher / Command Palette Glass** — `.prompt` 에 backdrop-blur(14px) + floating multi-shadow.
2. **Notice / Toast** — 좌측 라인 없이 info/success/warning/error 카테고리 tint + 둘레 1px border + blur(10px).
3. **Note Hover Popover Glass** — `.popover.hover-popover` 에 backdrop-blur(14px) + floating shadow + radius 10px.
4. **Outline 레벨별 위계 강화** — H1 700/0.96em → H2 600/0.90em → H3 500/0.84em → H4+ 400/0.80em.
5. **Tag pane 카운트 알약** — `.tree-item-flair` / `.tag-pane-tag-count` 틸 론 + 1px border + tabular-nums.
6. **폴더 노트 수 카운트** — `.nav-folder-title[data-count]::after` (JS 플러그인 또는 Dataview로 속성 주입).
7. **본문 색상 swatch (opt-in)** — `code.og-color` + `--swatch` CSS 변수로 ::before 동그라미.
8. **각주 dotted hover hint** — `sup.footnote-link` 에 dotted underline + cursor:help.
9. **Diff 코드블록 색상** — `language-diff` 의 +/-/@@ 줄 그린/레드/블루 톤.
10. **Selection 색조 통일** — Reading view + CM6 에디터 동일 블루 톤 (라이트 22% / 다크 30%).
11. **링크 hover ↗ 인디케이터** — 내부=블루, 외부=틸.
12. **Status bar 단어수/읽기시간** — `tabular-nums` + letter-spacing + 강조 톤.

### Workflow
- 샘플-우선 정책 준수: 코드 적용 전 [`docs/fixtures/v2.10-improvements-preview.html`](docs/fixtures/v2.10-improvements-preview.html) 으로 사용자 승인 후 적용.
- 리드미 스크린샷 추가: `screenshots/readme/v2.10-improvements-{light,dark}.png`.

## [2.9.8] — 2026-04-29 — Hotfix: outline active+hover 이중 박스 제거

### Fixed
- **Outline / Bookmarks / Backlink / Recent / Tag / Outgoing-link active 항목 위 hover 시 이중 박스** — 외곽 연보라(#eef2ff) + 내부 흰색 글래스 pill 동시 표시 문제 해제.
- 원인: v1.8.16+ file explorer 글래스 hover 룰(`tree-item-self:hover .tree-item-inner { background: glass; backdrop-filter: blur }`)이 좌우 패널의 tree-item-self 에도 매칭.
- 조치: 우측 패널 6종(outline/bookmarks/backlink/recent/tag/outgoing-link)의 tree-item-inner 내부 글래스 효과 무력화, hover 는 단순 background 틴트만.
- file explorer 글래스 hover 효과는 영향 없이 보존.

## [2.9.7] — 2026-04-29 — Hotfix: Outline active 회색 외곽 박스 제거 (기존 #eef2ff 에 위임)

### Fixed
- **Outline / Bookmarks / Backlink / Recent / Tag / Outgoing-link active 항목 회색 외곽 박스 제거.** v2.9.6에서 추가한 `background: rgba(37,99,235,0.10) + outline: 1px solid` 가 기존 v2.7.x 룰(`background: #eef2ff`)과 중첩되어 외곡 회색 박스 표시.
- 좌측 라인 무력화는 유지, 배경은 기존 연보라 틴트에 위임 — 외곽 박스·외곽 shadow 모두 제거.

### Policy (매모리 등록)
- **신규 디자인 기능은 코드 적용 전 반드시 샘플 이미지를 보여주고 사용자 확인 후 진행** — 코어 디자인 원칙으로 영구 등록. 버그 핫픽스·기존 정책 적용 등은 예외.

## [2.9.6] — 2026-04-29 — Hotfix: 회색 외곽 박스 제거 (기존 글래스에 광아올 추가 제거)

### Fixed
- **File explorer active 항목 우측 회색 박스 제거.** 원인: v1.8.16+ 디자인은 `.nav-file-title.is-active` 자체는 빈 컨테이너로 두고 내부 `.nav-file-title-content` 에 글래스 효과를 적용하는 구조. v2.9.2~v2.9.5에서 외부 컨테이너에 background+shadow+outline을 추가하는 실수로 글래스 위에 회색 박스가 한 겹 더 얹혀 보였음.
- file/folder explorer 는 외부 컨테이너에 `border/box-shadow` 제거, **좌측 라인 무력화만 유지**. 기존 글래스 효과가 그대로 살아남.
- outline/bookmarks/backlink/recent/tag 는 자체 글래스가 없으므로 **경량 패턴** (background tint + outline) 으로 적용. 외곢 shadow 없음 — 좁은 패널에서 잔상 방지.

## [2.9.5] — 2026-04-29 — Hotfix: Outline active 우측 잘림 + dashed 좌측 가이드 제거

### Fixed
- **Outline / Bookmarks / Tag / Backlink active 항목 우측 잘림** — v2.9.2~2.9.4의 1px `border` 가 좁은 패널 폭에서 overflow clip을 유발. `border` → `outline: 1px solid; outline-offset: -1px` 으로 교체 (레이아웃 영향 X).
- **Outline / Backlink 패널 좌측 dashed 가이드 라인** (`tree-item-children { border-left: 1px dashed }`) 제거 — 좌측 라인 영구 금지 정책 적용.
- **Outline / Backlink tree-item-self base 2px transparent border-left + hover accent** 무력화 — hover 강조도 background 틴트로 변경.

## [2.9.4] — 2026-04-29 — Step 3: Backlink / Recent / Tag / Outgoing-link active 좌측 라인 제거

### Changed (chrome 좌측 라인 점진 적용 · 3단계)
- **Backlink / Recent files / Tag pane / Outgoing-link** 패널의 active 항목 좌측 세로 라인 제거 + Glass+Shadow 적용.
- v2.9.2/v2.9.3과 동일 패턴.
- Settings nav / suggestion / notice / modal / popover 등은 **다음 단계**에서 처리.

## [2.9.3] — 2026-04-29 — Step 2: Outline / Bookmarks active 좌측 라인 제거

### Changed (chrome 좌측 라인 점진 적용 · 2단계)
- **Outline 패널** (`.outline .tree-item-self.is-active`) 좌측 세로 라인 제거 + Glass+Shadow 적용.
- **Bookmarks 패널** (`.bookmarks-view .tree-item-self.is-active`) 동일 적용.
- v2.9.2와 동일 패턴: 반투명 틴트 + `backdrop-filter: blur(8px)` + 다층 box-shadow + 둘레 1px border + radius 6px.
- Backlink / recent / tag / settings nav / notice / modal 등은 **다음 단계**에서 처리 (점진 적용 유지).

## [2.9.2] — 2026-04-29 — Step 1: File explorer active 좌측 라인 제거 (Glass+Shadow)

### Changed (chrome 좌측 라인 점진 적용 · 1단계)
- **File explorer active 항목** (`.nav-file-title.is-active`, `.nav-folder-title.is-active`) — 기존 좌측 세로 라인(`box-shadow: inset 3px 0 0`, `::before` stripe) 제거.
- 강조는 코어 디자인 원칙("Glass + Shadow") 그대로:
  - 반투명 틴트 `rgba(37,99,235,0.10)`
  - `backdrop-filter: blur(8px) saturate(1.1)`
  - 다층 box-shadow (외곽 soft + inset highlight)
  - 둘레 1px border `rgba(37,99,235,0.18)`
- Outline / bookmarks / backlink / recent / tag / settings nav / notice / modal 등 **나머지 chrome은 이번 단계에서 건드리지 않음** (v2.9.0 사고 방지 위해 점진 처리).

## [2.9.1] — 2026-04-29 — Hotfix: revert v2.9.0 chrome overhaul

### Fixed
- **워크스페이스 레이아웃 깨짐 긴급 복구.** v2.9.0의 광범위한 `!important` chrome 룰 + `backdrop-filter` 적용이 사이드바/탭/툴바 레이아웃을 깨뜨려 EOF v2.9.0 패치 블록 전체 제거.
- v2.7.0–v2.8.0 동작으로 복원. Style Settings UI / 옵션 33개 / 검증기 통과 그대로 유지.

### Notes
- 영구 디자인 정책(메인 = Glass + Shadow, chrome 좌측 세로 라인 영구 금지)은 보존. 다음 패치부터 셀렉터 단위로 *최소 범위*에서 점진 적용 예정.
- v2.9.0 추가 기능(Tag pane, Mobile drawer, Calendar, Search 토글 등)도 동일하게 점진 재도입 예정.

## [2.9.0] — 2026-04-29 — Left-line Permanent Ban + Glass/Shadow + Panels/Mobile + Navigation + Authoring Pack

### Design Policy (PERMANENT)
- **메인 디자인 언어 = "투명유리창(Glass) + 그림자(Shadow)"** — chrome 컴포넌트는 반투명 배경 + `backdrop-filter: blur` + 다층 그림자로 통일. 평면 단색 fill 금지.
- **좌측 세로 라인 강조 톤 영구 밴** — file explorer / outline / bookmarks / tag / backlink / recent / sidebar / tab / modal / suggestion / settings nav / notice / drop indicator / folder color 등 **모든 chrome 영역**에서 active/hover/drop 강조용 좌측 세로 라인(border-left, box-shadow inset Npx 0 0, ::before 좌측 stripe) 사용 금지. 강조는 background 틴트 + font-weight + 둘레 border / outline 만으로 표현.
- **예외**: callout / quote / embed / markdown-embed 본문 시맨틱 좌측 stripe (문서 콘텐츠 정체성 표현이며 active 강조가 아님 → 유지).

### Removed
- **Notice/Toast 좌측 4px 컬러 라인** 제거 (mod-info/success/warning/error 전체 background 틴트 + border 색).
- **File explorer / Outline / Bookmarks / Backlinks / Recent / Tag / Outgoing-link 패널의 active 좌측 라인** 일괄 무력화 (background 틴트 + bold + 라운드).
- **Settings 좌측 nav active 좌측 라인 / Suggestion 메뉴 좌측 라인 / Tab drop indicator 좌측 inset / Workspace split divider hover 좌측 라인 / Folder color code 좌측 라인 / Properties drag handle 좌측 라인** 모두 제거.

### Enforced (Glass + Shadow)
- Modal / Suggestion / Hover popover / Notice 모두 `rgba()` 반투명 배경 + `backdrop-filter: blur(...)` + 다층 그림자 적용 (라이트/다크 통합).
- Mobile drawer / 헤더 / 툴바도 동일 정책 — 16px blur + 24px 외곽 그림자.

### Added (A: Panels/Mobile)
- **Tag pane** — 트리 항목 라운드 + hover 틸 배경, 태그 카운트 알약, 계층 padding 가이드(좌측 라인 없음).
- **모바일 드로어** — 좌/우 드로어 라운드 + 그림자, 헤더/툴바 backdrop blur, 버튼 active 틴트.
- **Calendar 플러그인** — 일 셀 라운드, 오늘 outline+굵게, 주말 빨강, 노트 dot 틸.
- **Pinned 탭 lock 아이콘** 좌측 이모지 + **split divider hit area** 증해 (시각 두께 유지).

### Added (B: Navigation)
- **Search 옵션 토글** (정규식/대소문자/단어경계) active 시 블루 틴트.
- **Quick switcher / Command palette** 그룹 헤더 uppercase + tracking + 구분선, fuzzy match 강조.
- **Outline 패널** 계층 padding 가이드 + active 항목 background 틴트 강조(좌측 라인 없음).
- **링크 hover 인디케이터** (↗) — 내부링크 블루, 외부링크 틸.

### Added (C: Authoring precision)
- **Code block diff 하이라이트** — `language-diff`에서 +/-/coord 줄 그린/레드/블루 틴트.
- **Inline Dataview/Templater 결과** — 옷 틸 배경 + 틸 컬러.
- **본문 색상 코드 옷 컬러 인디케이터** (opt-in `ogd-color-swatch`) — `<code class="og-color" data-color="#hex">` 안에 동그라미 swatch.
- **Selection highlight** 블루 톤 (Reading view + CM6 에디터).
- **Spell check underline** 톴다운 (빨강 dotted 알파 낮춤).
- **Footnote ref** 점선 밑줄 + cursor:help 으로 hover 가능성 힌트 (기존 popover는 v2.7.0 팬업 상속).
- **Status bar word count / reading time** 아이템 tabular-nums + 톤 궁기 강조.

### Changed
- Style Settings 옵션 수: 32 → **33** (`ogd-color-swatch` 추가).
- 디자인 정책 메모 갱신 — "메뉴/탭/nav active + Notice" 좌측 세로 라인 금지로 범위 확대.

### Print/PDF
- 링크 hover 인디케이터, footnote dotted 밑줄 print 제거.

### Notes
- 모든 변경 EOF 패치 (Notice 라인 제거는 v2.7.0 블록 내 수정). 다크 모드 패리티 전 항목 포함.

## [2.8.0] — 2026-04-29 — Settings + Notice/Embed + Plugins + Editor Pack

### Added
- **Settings input/select/slider/checkbox/color picker/button** 일괄 통일 — 라운드, 포컬스 링, 토글 스위치 블루/다크 변형, mod-cta/mod-warning 버튼 컬러.
- **Notice stack + auto-dismiss progress** — 슬라이드 인 애니메이션, 하단 프로그레스 바 (5s), hover 시 일시정지.
- **Embed (트랜스클루전) 호버 액션** — 우상단 "원본 열기" 링크 버튼, hover 시 표시.
- **Audio/Video 임베드 플레이어** — audio 돌알 라운드, video 라운드 + 그림자, 컨트롤 패널 톤 통일.
- **PDF viewer 임베드** — 툴바 배경 통일, 버튼 hover background, container 배경 통일.
- **Excalidraw 플러그인** — 캔버스 배경 톤, ToolIcon 라운드 + hover.
- **Kanban 플러그인** — lane 배경/라운드, lane title uppercase + tracking, item 카드 그림자 + hover lift.
- **Tasks 플러그인** — 쿼리 결과 본구 카드 배경/국경. v2.4.0 체크박스 6종 상태와 자연 연동.
- **Unresolved (미해결) 링크** — dashed underline + 빨강 톤 (일견 식별성 ↑).
- **Vim mode caret + status indicator** — 블록 caret 블루/아웃라인, visual mode 옥펀 선택, status bar VIM 컬러 칩.
- **Properties drag handle** — hover 시 좌측 3px 그레이 핸들 (메뉴 active 강조 아닌 드래그 시각화 용도 — 정책 예외 허용).

### Changed
- `scripts/validate_theme.py` YAML lint 강화 — description 외에도 `title`/`default` 값의 YAML-special 접두 검증, 검사 문자 확장 (` * & ! | > % @ ? : - #).

### Print/PDF
- markdown-embed-link / pdf-toolbar / notice progress 는 print 시 숨김.
- unresolved 링크는 print 시 dashed 제거 + 기본 색상.

### Notes
- 옵션 수 32개 유지 (CSS-only 패치).
- 모든 변경 EOF 패치. 기존 셀렉터 영향 없음.
- 다크 모드 패리티 전 항목 포함.
- 메뉴/탭/nav active 좌측 세로 라인 금지 정책 (v2.6.1) 준수.

## [2.7.0] — 2026-04-29 — Sidebar/Panel + Authoring UX + Interaction Pack

### Added
- **Bookmark / Recent files / File recovery 패널** — 트리 아이템 라운드/hover background, 북마크 별표 옵션 온레지, 최근 파일 시계 그레이. 좌측 세로 라인 없음 (정책 준수).
- **Right sidebar 패널 헤더** — 백링크/아웃라인/아웃고잉링크 패널 타이틀 uppercase + tracking, count chip 알약 디자인.
- **Status bar 위젯** — 아이템 hover background, 아이템 사이 1px 구분자, 라운드 코너.
- **확장 태그 pill 카테고리** (opt-in `ogd-extended-tag-pills`, 기본 on) — #meeting/#review/#wip/#archive/#weekly/#monthly/#draft/#published 8종 추가 카테고리 색.
- **Slash command / Editor autocomplete 팬업** — 라운드/그림자 강화, 선택 항목 background 강조 (좌측 라인 금지 정책 준수), 단축키 kbd 알약.
- **Frontmatter 추가 타입** — `priority` (빨강), `status` (draft/review/done/archived 색), `progress` (틸), `version` (틸) 아이콘/값 컴러.
- **Drag indicator** — 파일/폴더 drop zone에 dashed 블루 outline + 옥펀, 탭 drop 시 inset border + 좌/우 placeholder.
- **Notice / Toast** — 라운드/그림자, mod-info/success/warning/error 별 좌측 4px 컬러 액센트.
- **Hover preview popover** — 라운드/그림자 강화, 임베드 타이틀 굵게 + 단축 구분선.

### Changed
- Style Settings 옵션 수: 31 → **32** (`ogd-extended-tag-pills` 추가).
- 베이스라인 선언: v2.2.0 → **v2.6.2** (UX Pack 누적분 + Settings YAML hotfix 검증).

### Print/PDF
- status-bar / notice-container / hover-popover / suggestion-container 는 print 시 숨김.

### Notes
- 모든 변경은 EOF 추가 패치 형태. 기존 셀렉터 영향 없음.
- 다크 모드 패리티 전 항목 포함.
- 메뉴/탭/nav active 좌측 세로 라인 금지 정책 (v2.6.1) 준수.

## [2.6.2] — 2026-04-29 — Fix Style Settings YAML parse error

### Fixed
- **Style Settings 파싱 에러** (`YAMLException: bad indentation of a mapping entry`) — v2.6.0에서 추가한 `ogd-folder-color-code`, `ogd-inline-code-categories` 옵션의 `description:` 값이 백틱(\`)으로 시작해 js-yaml 파서가 mapping entry로 오인식. 해당 두 description을 이중따옴표로 감싸 복구. 이 에러로 인해 전체 Style Settings UI가 렌더 실패 → PDF 헤더 설정 등 모든 옵션 UI 불가 상태였음.

### Added
- **YAML lint guard** in `scripts/validate_theme.py` — `@settings` 블록의 description 값이 YAML-special 문자(\` \* & ! | > % @)로 시작하면 검증 실패로 조기 차단.

### Notes
- 옵션 수 31개 유지. CSS 세렉터는 변경 없음.

## [2.6.1] — 2026-04-29 — Drop Settings nav left-accent

### Removed
- **Settings 좌측 nav active 항목의 좌측 세로 블루 라인** (`box-shadow: inset 2px 0 0 #2563eb`) 제거. 강조는 background + font-weight로만 처리.

### Policy
- **메뉴/탭/nav active 상태에 좌측 세로 액센트 라인 사용 금지** (사용자 정책, 2026-04-29). callout stripe / folder color code / search guide 등 의도된 디자인 언어는 유지.

### Notes
- 옵션 수 31개 유지. CSS 단일 행 삭제만.

## [2.6.0] — 2026-04-29 — Workspace + Search/Modal + Polish Pack

### Added
- **Tab close 버튼 / unsaved 인디케이터** — close 버튼 hover 시 빨강 배경, 미저장 탭에 노란 점 마커, hover 시 close 아이콘으로 전환. pinned 탭은 틸 컬러 강조.
- **File Explorer 폴더 컬러 코드** (opt-in, `ogd-folder-color-code`) — top-level 폴더 이름(`00-/01-/.../Inbox/Projects/Areas/Resources/Archive/Daily/Templates`)에 좌측 액센트 컬러 자동 적용. PARA 친화.
- **Workspace split divider** — 패널 resize handle hover 시 블루 액센트 + 두께 강조.
- **Search 결과 polish** — 결과 카드 라운드/hover 그림자, 파일명 굵게, 매치 키워드 옐로우 highlight 강화, sub-match 좌측 가이드 라인.
- **Modal / Settings 패널 통일** — modal 라운드/그림자 강화, Settings 좌측 nav를 본문 톤과 통일 (uppercase 그룹 라벨, active 항목 좌측 블루 액센트).
- **Inline code 카테고리** (opt-in, `ogd-inline-code-categories`) — `<code class="og-key|og-cmd|og-path|og-env">` 또는 `data-prefix="..."` 속성으로 카테고리 색 분기 (틸/블루/오렌지/퍼플).
- **Mermaid 다크모드 패리티** — ML 8색 팔레트 노드를 다크에서 약간 톤다운, edge label 다크 배경 + 가독성, cluster 점선 다크 톤, marker arrow 색 통일.
- **Print/PDF 마감** — 코드블록 `pre-wrap` + `break-word` 강제, callout 인쇄 시 배경 제거 + 1px 보더, 표 row break 방지, 폴더 컬러 코드/인라인 코드 카테고리는 인쇄 시 톤다운.

### Changed
- Style Settings 옵션 수: 29 → **31** (`ogd-folder-color-code`, `ogd-inline-code-categories` 추가).
- 검증 스크립트 옵션 카운트 31 기준으로 갱신.

### Notes
- 모든 변경은 v2.2.0 베이스라인을 보존하는 EOF 추가 패치 형태. 기존 셀렉터 영향 없음.
- 다크 모드 패리티 전 항목 포함. 신규 opt-in 옵션은 기본값 off로 회귀 위험 0.

## [2.5.0] — 2026-04-29 — Pro Pack (Canvas + Graph + Code label + Sticky table + Math + Caption + Anchor + dl)

### Added
- **Canvas polish** — 노드 카드에 그래파이트 톤 라운드/그림자, focus 시 블루 액센트, 엣지는 텍스트 톤(`#94a3b8`)으로 통일, edge label 알약 캡슐, 그리드 배경 점선화. 다크 모드 패리티.
- **Graph view** 색 팔레트 — `color-fill / color-line / color-text / color-circle / color-tag / color-focused / color-arrow` 등 그래파이트 변수에 매핑. 첨부·미해결 노드는 톤다운, focus는 블루, 태그는 틸. 다크 모드 패리티.
- **Code block 언어 라벨** — Reading view 코드블록 우상단에 언어 클래스 기반 알약 라벨, hover 시 Obsidian 기본 copy 버튼 노출 강화.
- **Table sticky header** (opt-in) — Style Settings `표 헤더 행 고정 (sticky)` 토글 (`.ogd-table-sticky-header`). Reading view + Dataview 표 모두 적용. PDF/print에서는 자동 비활성.
- **Math (KaTeX) 블록** — `$$ … $$` 블록에 좌측 액센트 + 옅은 배경 + 가로 스크롤 허용. 다크 모드 패리티.
- **Image caption** — 이미지 직후의 italic 단독 라인을 자동으로 가운데 정렬 캡션화 (CSS-only, `:has()` 사용).
- **Heading anchor** — h1~h6 hover 시 우측에 `¶` 마커 표시 (PDF에서는 비활성).
- **Definition list** (`<dl>`) — term/definition 그리드 레이아웃, term 굵게/우측 정렬, 옅은 배경 카드.

### Changed
- Style Settings 옵션 수: 28 → **29** (`ogd-table-sticky-header` 추가).
- 검증 스크립트(`scripts/validate_theme.py`)를 29개 기준으로 갱신.

### Notes
- 모든 변경은 v2.2.0 베이스라인을 보존하는 EOF 추가 패치 형태. 기존 셀렉터 영향 없음.
- 다크 모드 패리티 전 항목 포함. Print/PDF에서는 sticky·anchor·코드 라벨 비활성으로 인쇄 호환성 유지.

## [2.4.0] — 2026-04-29 — Status bar + Footnote + Checkbox states

### Added
- **Status bar / Title bar** — 상태표시줄 그라디언트 바닥, 아이템 구분자, hover 하이라이트. titlebar·탭 컨테이너 배경 통일.
- **Footnote (각주)** — 본문 `sup.footnote-link a`를 돔근 배지로 변경, 하단 `section.footnotes`에 `Footnotes` 라벨 + 점선 구분자, backref 톤다운.
- **Checkbox 6종 상태** — `data-task` 속성 기반:
  - `[x]` done (상도) · `[/]` in-progress (반 판 블루) · `[!]` important (빨강 느낌표)
  - `[?]` question (보라 물음표) · `[-]` cancelled (회색 이선) · `[>]` forwarded (주황 꿩쇠)

### Notes
- 다크 모드 패리티 전 항목 포함.
- 베이스라인 v2.2.0 유지; 추가 패치만.
- Style Settings 옵션 수: 28 (변동 없음).

## [2.3.1] — 2026-04-29 — View header title emphasis

### Changed
- **뷰 헤더 문서 제목** (`.view-header-title`, breadcrumb 마지막 항목) 굵게 + 약간 크게 표시해 현재 문서 인식성 강화.
- breadcrumb 상위 경로는 톤다운(`#94a3b8`)으로 조정.

## [2.3.0] — 2026-04-29 — Properties + Quote + Dataview

### Added
- **Properties (frontmatter) panel** — 카드 형태 컬러, 키 레이블 톤다운, 값 비워있으면 흐릿게, 타입별 아이콘 색 (`tag/date/status/author/url`), `multi-select-pill`은 메인 tag pill과 동일한 로드 형태.
- **Quote (`>`) 블록** — callout과 구분되는 4px 좌측 액센트 + 좀 이테릭 + 좀 `“` 장식. Live Preview에서도 포맷 마커만 흐릿게 표시.
- **Dataview 표 polish** — 헤더 uppercase + 정렬 마커 삼각형, zebra striping, hover 했라이트, 둘레테두리/메세지 일관. `block-language-dataview ul.dataview` 자식 트리에 좌측 가이드 라인.

### Notes
- 다크 모드 패리티 전 항목 포함.
- 베이스라인(v2.2.0) 유지; 기존 선택자에 영향 없는 추가 패치.
- Style Settings 옵션 수: 28 (변동 없음).

## [2.2.0] — 2026-04-29 — UX Pack + new baseline

### Added
- **Tag pill** — Reading view의 `a.tag`도 론드된 핀 형태로 통일. `#project / #todo / #idea / #done / #blocked / #urgent / #question / #reference` 카테고리별 테마 색 자동 적용 (href 기반).
- **Embedded note (트랜스클루전)** — `.markdown-embed`에 좌측 3px 액센트 + 도장 색 바탕 + 상단 `EMBED` 라벨로 원본 자료와 시각적 구분.
- **Backlinks / Outline panel polish** — hover시 좌측 액센트 바, 자식 트리에 dashed indent guide, Outline 글꼴 0.88em / heading-1·2 굵기 구분.
- **Command palette / Switcher** — 랜더링 그림자, 선택 항목 강조 배경, 단축키 `kbd` 모노스페이스 + 테두리 처리로 읽기 쉬움.
- **Mermaid ML 8색 팔레트** — 명시적 `classDef` 없는 노드는 Owen 표준 그레이 prep 색, edge label 가독성 강화, cluster는 점선 테두리.

### Baseline
- **다크 모드 패리티** 전 항목 포함.
- v2.0.5 hard reset + v2.1.0 opt-out toggle 유지.
- 새 베이스라인: **v2.2.0**.

## [2.1.0] — 2026-04-29 — Table cell height opt-out

### Added
- **Style Settings: "표 셀 행 높이 자동 stretch (legacy)"** — v2.0.5 hard reset을 원하는 사용자가 v2.0.4 이전 동작(셀이 행 내 제일 큰 셀 높이로 늘어나는 관습)으로 돌아갈 수 있도록 opt-in toggle 추가. 기본값: off (v2.0.5 동작 유지).
  - body class: `.ogd-table-cell-stretch`
  - Style Settings 옵션 수: 27 → **28**

### Changed
- README/validate 스크립트에서 옵션 카운트 27 → 28 갱신.

### Notes
- 테마 버전 추적: v2.0.5 baseline + 1 opt-in toggle.
- v3.0.0에서는 `theme.css` 모듈 분할(`src/*.css`)로 이동 예정. 현재는 회귀 위험 최소화 우선.

## [2.0.6] — 2026-04-29 — Baseline declaration

### Documentation
- **v2.0.5를 정식 안정 베이스라인으로 선언** — v1.8.42 이후 누적된 Live Preview 표 셀 inflate 단에 v2.0.5 hard reset으로 완전 해소. v2.0.5 상태를 이후 작업의 기준점으로 삼음.
- `theme.css` BOF 헤더에 `Baseline (verified stable)` 마커 추가.
- `README.md`에 `baseline since v2.0.5` 표기.

### Notes
- CSS 동작 변경 없음. 순수 문서·메타 패치.
- 향후 v2.1.0부터는 v2.0.5 기반으로 `src/` 모듈 분할과 추가 기능 진행.

## [2.0.5] — 2026-04-29 — Hard reset for table-cell-wrapper

### Fixed
- **Live Preview 표 셀 inflate 완전 차단 (최종)** — v2.0.4 이후에도 `td > div.table-cell-wrapper > div.cm-editor > div.cm-scroller > div.cm-content > div.cm-active.cm-line` 경로의 cm-active.cm-line이 ~80px로 렌더링되는 케이스가 남아 있었음. 셀 내부 모든 계층(`td *`)에 강제 min-height 0, height auto, padding/margin 0 적용.
- `.table-cell-wrapper`, `.cm-active.cm-line`, `.cm-editor`, `.cm-scroller`, `.cm-content`, `.cm-line` 명시 레이어에 개별 reset.
- `.cm-embed-block.cm-table-widget` 컨테이너 + `table/thead/tbody/tr`에도 height auto.

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
