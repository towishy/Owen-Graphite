# Changelog

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
