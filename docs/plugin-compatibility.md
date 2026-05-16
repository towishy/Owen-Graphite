# Owen Graphite — Plugin Compatibility

Owen Graphite는 기본 Obsidian UI와 자주 쓰는 작성 플러그인을 함께 쓰는 상황을 기준으로 점검합니다. 이 표는 완전한 지원 보증이라기보다 릴리즈 전 smoke matrix입니다.

| 플러그인/영역 | 현재 기준 | 점검 포인트 |
| --- | --- | --- |
| Style Settings | 지원 | 37개 옵션 표시, 토글/셀렉트/컬러 입력이 overflow 없이 표시 |
| Dataview | 지원 | 테이블 sticky header, zebra, 숫자 정렬, 다크 모드 대비 |
| Tasks | 지원 | 체크박스, 완료/진행/주의 task marker, callout 내부 task spacing |
| Canvas | 지원 | 카드/edge/toolbar가 workspace glass 톤과 충돌하지 않음 |
| Graph view | 지원 | 다크/라이트 배경 대비, pane chrome과 graph control 분리 |
| Search | 지원 | 검색 결과 제목, match highlight, hover/focus row contrast |
| Bookmarks | 지원 | row height 안정성, hover 시 layout shift 없음 |
| Outline | 지원 | active/hover row가 left rail 없이 식별 가능 |

## 릴리즈 전 확인

- Light/Dark 양쪽에서 위 영역을 한 번씩 연다.
- hover/focus가 행 높이를 바꾸지 않는지 본다.
- 다크 모드에서 muted text와 border가 배경에 묻히지 않는지 확인한다.
- Dataview/Tasks 결과가 긴 텍스트를 포함할 때 본문 column을 밀어내지 않는지 확인한다.
