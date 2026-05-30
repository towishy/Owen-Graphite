# Changelog

## v3.1.70

- fix: Settings > Appearance > Manage community-theme search에서 선택된 `Owen Graphite` 카드가 어두운 graphite 배경과 near-black 텍스트로 겹쳐 보이던 상태를 밝은 frosted glass 선택 카드로 정리했습니다.
- docs: README 첫 화면을 영어 단일 소개로 재구성하고, v3.1.70 기준으로 디자인/기능 신호와 최신 하이라이트가 바로 보이도록 갱신했습니다.
- guard: README 영어 `Version`/`Baseline` 행을 release metadata audit가 인식하도록 보강하고, CDP 런타임 확인, source usage map, core principles, release check, runtime evidence strict 검증을 통과했습니다.

## v3.1.69

- polish: 파일 탐색기 active 하위 폴더 진입 전 여백을 살짝 늘려 상위 폴더와 active 문서박스 사이의 계층 리듬을 더 안정화했습니다.
- polish: active 하위 폴더 내부 파일명 글자 크기와 확장자 배지 폭을 미세 조정해 긴 파일명이 조금 더 읽히도록 했습니다.
- polish: 파일 탐색기 목록 하단에 얕은 fade/inner edge를 추가해 vault switcher 위쪽 여백이 목록 끝으로 읽히도록 정리했습니다.
- guard: CDP 런타임 확인, source usage map, core principles, release check, Obsidian theme sync 검증을 통과했습니다.

## v3.1.68

- fix: 파일 탐색기 active 하위 폴더 ancestor에 남던 Obsidian virtual list inline `min-height` spacer를 제거해 하단 빈 스크롤 영역이 보이지 않도록 수정했습니다.
- polish: active 하위 폴더의 흰 문서박스와 문서 리스트는 유지하면서 부모 folder children box만 레이아웃에서 빠지도록 selector를 좁혔습니다.
- guard: CDP 런타임 확인, source usage map, core principles, release check, Obsidian theme sync 검증을 통과했습니다.

## v3.1.67

- polish: active 하위 폴더 문서 목록을 더 선명한 흰 유리면으로 정리하고, header/body 경계와 첫 문서 pill 사이 여백을 안정화했습니다.
- polish: active 하위 폴더 내부 문서 pill의 제목 표시 폭을 넓히고 그림자를 낮춰 선택 상태가 덜 무겁게 보이도록 다듬었습니다.
- fix: 깊은 하위 폴더에서 문서 pill이 박스 경계에 붙어 보이던 계층별 margin을 보정하고, 긴 하위 폴더명 ellipsis/중앙정렬을 안정화했습니다.
- guard: light/dark CDP 런타임 확인, source usage map, core principles, release check, Obsidian theme sync 검증을 통과했습니다.

## v3.1.66

- polish: 파일 탐색기에서 선택 문서를 포함한 하위 폴더 하나만 코드블록형 outer/header band로 보이도록 계층 표현을 좁혔습니다.
- polish: active 하위 폴더 헤더의 폴더 아이콘/이름을 중앙 정렬하고, hover pill이 헤더 라인과 겹치지 않도록 제거했습니다.
- fix: active 하위 폴더 내부 문서 배지와 문서 제목이 겹치던 간격을 CDP computed style 기준으로 보정했습니다.
- guard: CDP 런타임 확인, source usage map, core principles, release check, Obsidian theme sync 검증을 통과했습니다.

## v3.1.65

- compat: 커뮤니티 테마 최소 지원 버전을 Obsidian `1.5.8`로 낮추고 문서/이슈 템플릿의 기준 버전도 맞췄습니다.
- a11y: light/dark 핵심 보조 텍스트와 code comment 팔레트 대비를 WCAG AA 기준에 맞게 보강했습니다.
- fix: bundled `theme.css` 중간에 섞이던 UTF-8 BOM을 제거해 커뮤니티 스캐너의 unknown type selector 경고를 정리했습니다.
- polish: 파일 탐색기 최상위 폴더 기본 외곽선을 조금 진하게 해 폴더 간 구분을 더 쉽게 보이게 했습니다.
- guard: source usage map, core principles, release check, Obsidian theme sync 검증을 통과했습니다.

## v3.1.64

- polish: 왼쪽 파일 탐색기 문서 트리의 hover/active/parent folder 위계를 더 조용하게 정리하고, 선택 문서 외곽선과 sibling 문서 대비를 보강했습니다.
- polish: 파일 탐색기 확장자 배지가 기본 상태에서는 회색으로 쉬고, hover/active 상태에서 MD/MDX 문서도 푸른 glass 배지로 명확히 올라오도록 수정했습니다.
- fix: MD/MDX 확장자 전용 회색 배지 변수가 hover 색상 변수를 덮던 cascade를 owner CSS 안에서 바로잡았습니다.
- guard: bundle freshness, source usage map, core principles, release check, runtime evidence strict 검증과 Obsidian test vault sync를 통과했습니다.

## v3.1.63

- feat: Style Settings에 `PDF 고객 전달 권장 프리셋`(`ogd-pdf-client-delivery`)을 추가해 고객 공유용 PDF 가시성 조합을 한 번에 적용할 수 있게 했습니다.
- polish: 새 프리셋에서 화면 전달용 본문·표·callout 톤을 재사용하고, 긴 URL은 본문 뒤에 붙이지 않도록 reference-first 출력 흐름을 기본화했습니다.
- docs: 고객 전달용 PDF 샘플 fixture를 추가하고 Style Settings 프리셋 문서와 계약을 갱신했습니다.
- guard: Style Settings contract, PDF header/footer contract, docs/assets, source usage map, core principles, release check, Obsidian sync 검증을 통과했습니다.

## v3.1.62

- polish: 커뮤니티 테마 검색 입력 focus 시 보이던 cyan rim/halo를 CDP로 원인 확인 후 shadow-only 상태로 낮췄습니다.
- polish: Chrome/settings 상태 표현의 shadow, lift, selected/focus 깊이를 더 차분한 liquid-glass 위계로 맞췄습니다.
- process: 디자인/visible CSS 변경 후 Obsidian CDP remote debugging 상태 확인과 live DOM/computed 확인을 WIKI 및 validation plan에 필수 handoff 단계로 반영했습니다.
- guard: CDP status, runtime evidence strict check, visual fixture render, release check, Obsidian sync 검증을 통과했습니다.

## v3.1.61

- process: Owen risk-accepted 예외를 `risk-accepted-registry.json` 기반으로 구조화하고 source marker `id`/evidence와 연결했습니다.
- guard: direct-owner guard가 risk registry의 module, selector, allowed property, evidence를 검증하도록 강화하고 legacy 단일 marker bypass를 제거했습니다.
- tooling: CDP runtime evidence helper에 `--status` 모드를 추가해 승인된 Obsidian 원격 디버깅 포트와 vault/version metadata를 빠르게 확인할 수 있게 했습니다.
- docs: WIKI core principles, table workflow, runtime evidence storage, audits, consistency check를 새 risk registry/CDP status 흐름에 맞췄습니다.
- guard: release check, table validation, WIKI consistency, CDP status smoke 검증을 통과했습니다.

## v3.1.60

- polish: PDF 기본 본문/표/callout/code 기준 글자 크기를 12pt(약 16px)로 올리고, 고객 전달용 PDF는 12.4pt(약 16.5px)로 조정했습니다.
- fix: callout 타입별 왼쪽 accent rail을 제거하고 전체 border/아이콘 중심의 liquid-glass 톤으로 복구했습니다.
- process: Owen risk-accepted 예외 경로를 WIKI와 guard에 반영하고 Markdown table widget을 HTML table 가시성에 맞췄습니다.
- guard: source usage map, runtime evidence, direct owner, hit routing, LP/PDF ownership, release check 검증을 통과했습니다.

## v3.1.59

- polish: Live Preview HTML table의 셀 여백과 line-height를 넓혀 긴 한국어 표의 가독성을 개선했습니다.
- polish: Owen risk-accepted 예외로 Live Preview Markdown table widget의 글자 크기와 셀 여백을 HTML table 가시성에 맞췄습니다.
- fix: Canvas card menu와 edge hover selector를 Obsidian 1.12 runtime DOM(`.canvas-card-menu-button`, `.canvas-edges path`)에 맞게 보강했습니다.
- process: CDP runtime evidence registry와 coverage priority plan을 연결하고 Dataview/Canvas/Graph/Search real DOM evidence를 기록했습니다.
- polish: Settings 섹션 heading의 좌측 vertical rail을 제거하고 Owen Graphite liquid-glass 원칙에 맞는 작은 frosted badge로 정리했습니다.
- docs: chrome/settings/overlay/mobile 상태를 한 화면에서 확인하는 `chrome-ui-state-fixture.html` visual QA fixture를 추가했습니다.
- process: WIKI route registry command를 `script`/`args`/`safe` 구조로 바꾸고 JSON validation plan, last-validation summary, route workflow unit test를 추가했습니다.
- guard: source usage map, visual fixture contract/render, Style Settings contract, core principles, release check, Obsidian sync 검증을 통과했습니다.

## v3.1.58

- fix: callout 타입별 왼쪽 accent rail을 제거하고 전체 border/아이콘 중심의 liquid-glass 톤으로 복구했습니다.
- process: 작업 시작/종료 helper, diff-aware validation, runtime evidence strict mode, incident/evidence helper를 WIKI workflow에 연결했습니다.
- guard: selector owner cheatsheet, WIKI route coverage, mobile owner guard, WIKI schema consistency 검증을 core/release gate에 보강했습니다.
- sync: Obsidian theme sync에 chunk-copy fallback, verify-only, last-sync 기록을 추가했습니다.
- guard: release preflight, source usage map freshness, core principles gate, release check, Obsidian sync 검증을 통과했습니다.

## v3.1.57

- docs: `dev/MAP`, `dev/effective-baseline`, `docs/v3` 운영 자료를 `dev/WIKI` 아래로 흡수해 WIKI를 단일 작업 진입점으로 정리했습니다.
- process: 모든 코드 작성, 기능 개선, 수정, 정리 작업 전에 `dev/WIKI`를 먼저 참조하도록 Copilot 지침, WIKI core/prompt, CONTRIBUTING, core gate를 보강했습니다.
- guard: WIKI 필수 파일과 legacy 경로 재생성 금지, 새 DOCS/fixture 경로, Style Settings 계약 경로를 release check에 연결했습니다.
- guard: source usage map freshness, core principles gate, docs/assets, Style Settings contract, release check를 통과했습니다.

## v3.1.56

- polish: Style Settings의 `Import`, `Export`, `Copy to clipboard`, `Download`, `Import from file` 링크 문자열을 Owen Graphite glass pill 버튼 톤으로 정리했습니다.
- polish: Style Settings export/import 모달 안의 유틸리티 액션도 설정 화면과 같은 버튼 언어로 맞췄습니다.
- ci: main Validate workflow에 requirements와 Playwright Chromium 설치 단계를 추가해 release check 실행 환경을 릴리즈 workflow와 맞췄습니다.
- guard: CSS budget, bundle freshness, release build, release ZIP 검증을 통과했습니다.

## v3.1.55

- feat: 고객 전달용 화면 PDF를 위한 `PDF 고객 전달용 화면 가시성` Style Settings 토글을 추가했습니다.
- polish: 새 PDF preset에서 제목 위계, 본문·표 글자 크기, callout 역할 구분, 헤더/푸터 라벨 톤을 화면 공유용으로 조정했습니다.
- docs: README 신기능 소개와 Visual Tour에 PDF 고객 전달용 화면 가시성 이미지를 추가했습니다.
- guard: Style Settings contract, PDF header/footer contract, release build, release ZIP 검증을 통과했습니다.

## v3.1.54

- polish: 파일 탐색기 상단 5개 액션 버튼에 Owen Graphite 전용 마스크 아이콘, liquid-glass 표면, hover/focus 리프트 효과를 적용했습니다.
- polish: 문서 상단 root view header의 흰 배경을 더 투명한 cyan-tint glass로 낮추고, 실제 소유 규칙의 하이라이트와 그림자를 함께 줄였습니다.
- fix: 활성 workspace tab 뒤에 보이던 둥근 backline/connector 레이어와 확산 그림자를 정리해 탭 뒤쪽 라인이 드러나지 않도록 했습니다.
- guard: release check, CSS budget, LP/PDF selector ownership, Live Preview hit-routing, PDF header/footer 검증을 통과했습니다.

## v3.1.53

- fix: Live Preview 코드블럭 헤더 라벨이 클릭 후 사라지지 않도록 `.code-block-flair` 표시를 복원하고, 클릭 라우팅은 유지했습니다.
- polish: 코드블럭 헤더 오른쪽 액션 슬롯 토큰을 예약해 향후 copy icon 같은 DOM 액션이 라벨과 겹치지 않도록 정리했습니다.
- guard: Live Preview hit-routing, LP/PDF selector ownership, CSS budget, PDF header/footer 릴리스 검증을 통과했습니다.

## v3.1.52

- polish: 활성 workspace tab과 문서 표면이 이어지는 connected glass 처리, 비활성 탭 제목 중앙 정렬, 빈 탭 영역 하단 hairline을 정리했습니다.
- polish: 하단 문서 프레임과 vault switcher에 활성 파일 pill 계열의 sky rim / frosted glass surface를 적용하고, 상태칩·문서 제목 위계를 조정했습니다.
- fix: Windows 타이틀바 버튼 영역을 침범하지 않도록 탭 라인 구현을 background 기반으로 정리하고, Owen Editor top/bottom 툴바 위치와 문서 시작/끝 여백을 분기했습니다.
- docs: README 최신 신기능 소개와 전용 SVG 이미지를 v3.1.52 기준으로 갱신했습니다.

## v3.1.51

- polish: 상단 workspace tab을 첨부 이미지 기준의 attached liquid-glass 형태로 정리하고, 활성 탭의 sky rim을 위/좌/우 동일 톤으로 맞췄습니다.
- polish: 비활성 탭에도 보일듯 말듯한 외곽선을 추가해 탭 경계가 사라지지 않도록 하면서, Obsidian 기본 separator 라인은 계속 숨깁니다.
- docs: 새 상단 탭/플로팅 툴바 신기능 이미지를 README 신기능 소개와 스크린샷 인벤토리에 등록했습니다.

## v3.1.50

- docs: README Visual Tour에 문서 작성 화면, Style Settings 보고서 옵션, Owen Editor 툴바 설정 스크린샷을 추가했습니다.
- docs: 새 README 스크린샷 3장을 `screenshots/readme/`에 등록하고 스크린샷 인벤토리를 갱신했습니다.
- release: 문서/스크린샷 자산 링크 검증을 통과한 README 갤러리 갱신 릴리즈입니다.

## v3.1.49

- polish: Style Settings 그룹 제목과 Obsidian 설정 본문 섹션 제목에 추천안 D의 liquid header bar와 좌측 gradient rail을 적용했습니다.
- polish: 단축키/검색 입력창의 강한 파란 focus rim을 추천안 B Liquid Aqua rim으로 낮춰 settings chrome의 glass 톤과 맞췄습니다.
- docs: 설정 그룹 제목과 검색 focus rim 추천안 preview를 추가하고, README 신기능 이미지와 소개를 v3.1.49 기준으로 갱신했습니다.

## v3.1.48

- polish: 이미지 외곽선 추천안 D를 적용해 1px 회색 rim에 내부 liquid-glass highlight와 절제된 그림자를 더했습니다.
- fix: Live Preview 첨부 이미지 경로(`.internal-embed`, `.image-embed`, `.media-embed`, `.cm-embed-block`)에도 동일한 이미지 외곽선 효과가 적용되도록 selector 범위를 확장했습니다.
- docs: liquid rim, soft shadow, restrained shadow 후보를 비교하는 `dev/WIKI/DOCS/v3/research/image-border-effect-preview.html` 및 PNG 샘플을 추가했습니다.

## v3.1.47

- polish: 문서에 첨부/삽입되는 이미지에 1px 희미한 회색 외곽선을 추가해 흰 배경 스크린샷이 본문 배경에 묻히지 않도록 개선했습니다.
- polish: PDF Export 이미지와 figure 안의 이미지에도 동일한 1px 회색 외곽선과 `box-sizing: border-box`를 적용해 출력 폭을 안정화했습니다.
- docs: 이미지 외곽선 추천안 A/B/C/D를 비교하는 `dev/WIKI/DOCS/v3/research/image-border-samples.html` 샘플 fixture를 추가했습니다.

## v3.1.46

- docs: README 첫 화면에 사용 시나리오, release confidence, visual tour를 추가해 테마의 강점과 검증 상태를 더 빠르게 파악할 수 있도록 정리했습니다.
- docs: 영어 README, Style Settings 프리셋, 시각 비교 가이드, unused CSS 로드맵, 릴리스 노트 workflow 문서를 추가했습니다.
- guard: `release_check.py`로 로컬/CI/release 검증 흐름을 단일 진입점으로 묶고, CHANGELOG 기반 release note 생성 스크립트를 추가했습니다.
- repo: GitHub Issue 템플릿을 추가해 버그, 시각 회귀, 기능 요청에 필요한 재현 정보를 표준화했습니다.

## v3.1.45

- docs: Obsidian community review가 요구하는 영어 테마 설명을 README 상단에 추가했습니다.
- docs: README 파일 탐색기 확장자 배지 SVG를 한글 안전 폰트, 단일 배경, liquid-glass 화살표, 텍스트 overflow 검증 기준으로 정리했습니다.
- docs: README 요약, 검증 상태, 시각 갤러리, Style Settings 프리셋, 호환성/unused CSS/릴리스 노트 문서를 연결했습니다.
- guard: 로컬 릴리스 점검을 묶는 `dev/scripts/release_check.py`와 changelog 기반 릴리스 노트 생성 스크립트를 추가했습니다.

## v3.1.44

- feat: 파일 탐색기에서 오른쪽 확장자 배지를 숨기고 앞쪽 타입 배지로 통합해 긴 문서 제목 표시 폭을 넓혔습니다.
- feat: Markdown, HTML/SVG/PDF, 코드, 설정, 오피스, 이미지, 오디오/비디오, Obsidian canvas/excalidraw 등 주요 확장자 타입 배지를 추가했습니다.
- docs: README 신기능 소개와 전용 SVG 이미지를 추가하고 설치 ZIP 안내를 새 버전 기준으로 갱신했습니다.

## v3.1.43

- release: Obsidian community scanner refresh를 위해 v3.1.43 패치 릴리즈를 발행합니다.
- guard: direct-owner CSS baseline, effective/provenance MAP, unused CSS candidate report를 main에 고정해 커뮤니티 스캔 전 검증 근거를 보강했습니다.
- docs: release metadata와 설치 ZIP 안내를 새 버전 기준으로 갱신했습니다.

## v3.1.42

- polish: Live Preview H1 글자 크기를 두 배로 키워 편집 화면에서도 문서 제목 계층이 더 강하게 보이도록 조정했습니다.
- fix: Windows 테스트 vault `H:\Owen-WIKI`를 Obsidian sync 기본 후보에 추가해 로컬 확인 흐름에서 최신 테마가 바로 반영되도록 했습니다.

## v3.1.41

- polish: Live Preview H1 글자 크기를 키워 문서 제목 계층이 더 선명하게 보이도록 조정했습니다.
- polish: PDF Export H1 박스에 흰색/회색 liquid-glass surface, 연한 회색 rim, 내부 반사와 부드러운 그림자를 적용했습니다.
- fix: H1 텍스트 아래 cyan underline을 제거해 PDF 제목 박스가 더 차분한 frosted glass 톤으로 보이도록 정리했습니다.

## v3.1.40

- fix: PDF Export에서 첫 H1로 렌더링되는 문서 제목을 숨기고, 본문 첫 H1은 이전 크기와 리듬으로 유지합니다.
- polish: PDF Header/Footer 라벨이 켜진 상태에서 첫 본문 H1이 상단 배지와 겹치지 않도록 여백을 보강했습니다.
- guard: LP/PDF computed-style audit가 문서 제목 숨김과 본문 H1 표시/크기 유지 조건을 함께 검증하도록 확장했습니다.

## v3.1.39

- feat: PDF 첫 페이지 헤더에 Key/Value 2쌍 출력을 추가하고, 1번 → 2번 순서와 동일 segment 높이를 보장했습니다.
- feat: 헤더 2번 key/value 전용 색상 팔레트를 Style Settings에 추가했습니다.
- guard: computed-style audit가 2쌍 헤더의 출력 순서, 높이 일치, 독립 색상 적용을 검증하도록 보강했습니다.

## v3.1.38

- feat: Live Preview와 PDF Export 코드블럭의 헤더, 폰트, syntax 색상 패리티를 정리했습니다.
- docs: 전체 `src/` CSS 기준 Live Preview ↔ Export PDF 매핑 MAP을 `dev/WIKI/MAP/live-preview-pdf-css-map/`에 추가했습니다.
- guard: 코드 clarity fixture를 확장해 Live Preview source line, rendered widget, PDF `.token.*`/`.cm-*` syntax class 경로를 함께 검증합니다.

## v3.1.37

- feat: Live Preview / Reading / PDF Export 품질 패리티 fixture와 로컬 visual smoke 검증 스크립트를 추가했습니다.
- polish: PDF callout의 glass rim, icon chip, 페이지 분할 안정성을 보강하고 긴 셀·긴 코드 토큰 wrapping을 안정화했습니다.
- guard: CI/pre-commit/release/sync 검증 흐름을 fresh bundle, `theme.css` freshness, helper script 실패 전파 기준으로 강화했습니다.

## v3.1.36

- feat: PDF Key/Value 라벨 색상을 헤더/푸터별, key/value별로 독립 선택할 수 있도록 Style Settings UI를 재구성했습니다.
- polish: PDF 라벨 UI를 활성화 → 라벨 구성 → 공통 구성 → 헤더 설정 → 푸터 설정 순서로 그룹화하고, 라벨 글자 굵기/크기와 segment 폭을 조정해 긴 key 문구가 잘리지 않도록 개선했습니다.
- docs: README에 PDF Key/Value 라벨 신기능과 전용 스크린샷을 추가했습니다.

## v3.1.35

- feat: PDF Header/Footer 라벨에 Key/Value 2-segment 모드를 추가. Style Settings에서 단일 라벨과 2-segment 구성을 선택하고, 헤더/푸터 value 입력값과 Graphite/Sky/Mint/Violet/Teal 팔레트를 설정할 수 있습니다.
- polish: 붙은 배지 스타일을 추가하고 header/footer segment 간격, 글자 크기, 여백을 조정해 PDF 출력에서 정보 위계를 더 또렷하게 표시합니다.
- guard: PDF marginalia MAP 계약과 감사 스크립트를 확장하고 fixture/validation 문서 및 token inventory를 갱신했습니다.

## v3.1.34

- fix: community.obsidian.md 제출 포털 CSS 검증기 `Unexpected }` (theme.css:2230) 에러 해소. `src/surfaces/22-reading-embeds-workspace.css` 파일 상단의 짝 없는 `padding-left: 1.35em; }` 블록(메칭되는 여는 셌렉터 없이 고아 선언 + 닫음 괄호)을 제거. 브라우저는 관대하게 무시해 시각 영향은 0이고, 새 검증기만 정확히 잘아내던 쟠복적 소스 버그입니다.

## v3.1.33

- fix: PDF Header/Footer 라벨을 @media print 안으로 격리. Live Preview/Reading View에서 노출되던 회귀 수정.

## v3.1.32

- feat: PDF Header/Footer 입력 기능 추가.
