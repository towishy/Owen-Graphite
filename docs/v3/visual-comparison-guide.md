# v3 Visual Comparison Guide

이 문서는 기본 Obsidian과 Owen Graphite의 차이를 같은 조건에서 캡처하기 위한 기준입니다. README나 릴리스 노트에 before/after 이미지를 추가할 때 이 기준을 사용합니다.

## 캡처 대상

| 비교면 | 기본 Obsidian | Owen Graphite | 확인 포인트 |
| --- | --- | --- | --- |
| 긴 기술 문서 | 같은 Markdown 샘플 Reading View | 같은 Markdown 샘플 Reading View | 제목 계층, 한글 문단 밀도, callout 리듬 |
| 긴 표 | 같은 표 fixture | 같은 표 fixture | sticky header, zebra, 긴 셀 wrapping, 다크 모드 대비 |
| 코드블럭 | 같은 fenced code fixture | 같은 fenced code fixture | 헤더, syntax 색상, Live Preview/PDF 패리티 |
| PDF 보고서 | 같은 문서 PDF export | 같은 문서 PDF export | 첫 페이지 헤더, 마지막 페이지 푸터, 페이지 분할 |
| 파일 탐색기 | 같은 vault tree | 같은 vault tree | 타입 배지, 긴 파일명 말줄임, hover/focus 안정성 |

## 촬영 규칙

- Light, Dark, Report 모드를 각각 분리해서 촬영합니다.
- 데스크톱은 1440px 이상, 모바일은 Obsidian 모바일 폭에 가까운 좁은 화면을 별도로 확인합니다.
- 같은 문서, 같은 zoom, 같은 Obsidian 버전, 같은 Style Settings 상태를 사용합니다.
- README에 넣는 이미지는 `screenshots/readme/`에 보관하고, 링크 추가 후 `python dev/scripts/audit_docs_assets.py`를 실행합니다.

## README 갤러리 기준

| 이미지 | 파일 위치 | 용도 |
| --- | --- | --- |
| Light mode | `screenshots/light.png` | 첫 인상과 본문 밀도 |
| Dark mode | `screenshots/dark.png` | 다크 대비와 chrome 안정성 |
| Report mode | `screenshots/report.png` | 보고서 모드와 PDF에 가까운 레이아웃 |
| 기능별 이미지 | `screenshots/readme/` | 최신 기능 3개 소개 |

## 남은 작업

- 기본 Obsidian before 이미지는 저장소에 포함하지 않습니다. 릴리스별로 필요한 경우 같은 fixture에서 새로 캡처합니다.
- 비교 이미지를 추가하면 [README.md](../../README.md)의 Visual Tour 또는 신기능 소개에 연결합니다.