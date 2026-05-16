# Changelog

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

