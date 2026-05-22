# Owen Graphite Feature History

README의 신기능 소개에는 최신 3개 기능만 유지합니다. 그보다 오래된 신기능 소개는 이 문서로 옮겨 보관합니다.

## v3.1.44 — 파일 탐색기 확장자 배지 / File Explorer Type Badges

파일 탐색기의 오른쪽 확장자 텍스트를 숨기고, 앞쪽 문서 아이콘 자리에 `MD`, `HTML`, `SVG`, `PDF`, `CFG` 같은 타입 배지를 표시합니다. 오른쪽 배지가 차지하던 폭을 파일명 표시 영역으로 돌려 긴 문서 제목이 더 늦게 말줄임되며, 문서·이미지·코드·설정·오피스·미디어·Obsidian 특화 파일을 한눈에 구분할 수 있습니다.

This update hides the right-side extension label and replaces the leading document icon with compact type badges such as `MD`, `HTML`, `SVG`, `PDF`, and `CFG`. The file name receives more horizontal space, so long document titles stay readable for longer in the file explorer.

![파일 탐색기 확장자 배지](../../screenshots/readme/file-explorer-type-badges.svg)

| 구분 | 개선 내용 |
| --- | --- |
| 제목 표시 | 파일 row가 사용 가능한 폭을 끝까지 쓰도록 조정 |
| 확장자 표시 | 오른쪽 `HTML` 같은 확장자 배지를 숨기고 앞쪽 타입 배지로 통합 |
| 대응 범위 | Markdown, HTML/SVG/PDF, 코드, 설정, 오피스, 이미지, 오디오/비디오, Obsidian canvas/excalidraw |
| 가독성 | 타입 배지와 파일명 사이 간격을 확보해 목록 스캔성을 개선 |

## v3.1.38 — 코드블럭 Live Preview / PDF 패리티

Live Preview, Reading View, PDF Export의 코드블럭 헤더·폰트·syntax 색상을 같은 토큰 기준으로 맞췄습니다. Obsidian Live Preview의 source line, rendered code widget, PDF export의 Prism `.token.*`/CodeMirror `.cm-*` 경로를 모두 검증 fixture에 포함해 앞으로 코드블럭 개선 시 누락되는 경로를 줄였습니다.

![코드블럭 Live Preview / PDF 패리티](../../screenshots/readme/code-font-clarity.png)

| 검증 영역 | 개선 내용 |
| --- | --- |
| Live Preview | 코드 fence 헤더를 한 줄 라벨로 정리하고 rendered widget 경로까지 동일한 codeblock surface 적용 |
| PDF Export | `.token.*`와 `.cm-*` syntax class를 같은 `--ogd-code-*` 색상·폰트 토큰으로 매핑 |
| 유지보수 | `dev/MAP/live-preview-pdf-css-map/`에 selector 매핑, cascade ownership, parity guideline 추가 |

## v3.1.37 — Live Preview / PDF 품질 패리티

Live Preview, Reading View, PDF Export에서 callout과 긴 표 셀이 같은 품질 기준으로 보이도록 검증 fixture와 출력 안정화 guard를 추가했습니다. PDF callout은 흰색/회색 frosted surface, 얇은 rim, icon chip 중심으로 정리하고 긴 코드 토큰은 표 디자인을 유지한 채 셀 안에서 줄바꿈됩니다.

![Live Preview / PDF 품질 패리티](../../screenshots/readme/pdf-live-preview-parity.png)

| 검증 영역 | 개선 내용 |
| --- | --- |
| Live Preview / Reading | callout rim, icon chip, 얕은 glass surface 기준 정렬 |
| PDF Export | callout 제목/본문 분리 완화, 긴 셀·코드 토큰 wrapping 안정화 |
| 릴리즈 검증 | fresh bundle, `theme.css` freshness, visual smoke fixture 추가 |

## v3.1.36 — PDF Key/Value 헤더와 푸터 라벨

PDF 출력 전용 헤더와 푸터 라벨을 단일 문구 또는 Key/Value 1쌍 배지로 표시할 수 있습니다. Style Settings에서 헤더와 푸터를 각각 켜고, key/value 문구와 색상을 독립적으로 지정해 작성자, 기밀 등급, 문서 상태를 본문 흐름 밖에 작게 배치합니다.

![PDF Key/Value 헤더와 푸터 라벨](../../screenshots/readme/pdf-key-value-labels.png)

| 설정 영역 | 가능한 조정 |
| --- | --- |
| 헤더 설정 | Key 색상, Value 색상, Key 문구, Value 문구, 위치 |
| 푸터 설정 | Key 색상, Value 색상, Key 문구, Value 문구 |
| 공통 구성 | 단일/Key-Value 구성, 라벨 스타일, 라벨 크기, 빠른 문구 |