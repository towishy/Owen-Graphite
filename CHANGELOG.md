# Changelog

## v3.1.34

- fix: community.obsidian.md 제출 포털 CSS 검증기 `Unexpected }` (theme.css:2230) 에러 해소. `src/surfaces/22-reading-embeds-workspace.css` 파일 상단의 짝 없는 `padding-left: 1.35em; }` 블록(메칭되는 여는 셌렉터 없이 고아 선언 + 닫음 괄호)을 제거. 브라우저는 관대하게 무시해 시각 영향은 0이고, 새 검증기만 정확히 잘아내던 쟠복적 소스 버그입니다.

## v3.1.33

- fix: PDF Header/Footer 라벨을 @media print 안으로 격리. Live Preview/Reading View에서 노출되던 회귀 수정.

## v3.1.32

- feat: PDF Header/Footer 입력 기능 추가.

