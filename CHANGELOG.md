# Changelog

## v3.1.47

- polish: 문서에 첨부/삽입되는 이미지에 1px 희미한 회색 외곽선을 추가해 흰 배경 스크린샷이 본문 배경에 묻히지 않도록 개선했습니다.
- polish: PDF Export 이미지와 figure 안의 이미지에도 동일한 1px 회색 외곽선과 `box-sizing: border-box`를 적용해 출력 폭을 안정화했습니다.
- docs: 이미지 외곽선 추천안 A/B/C/D를 비교하는 `docs/v3/research/image-border-samples.html` 샘플 fixture를 추가했습니다.

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
- docs: 전체 `src/` CSS 기준 Live Preview ↔ Export PDF 매핑 MAP을 `dev/MAP/live-preview-pdf-css-map/`에 추가했습니다.
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
