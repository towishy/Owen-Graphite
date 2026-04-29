# Owen Graphite — Style Settings 옵션 풀 레퍼런스

[Style Settings 플러그인](https://github.com/mgmeyers/obsidian-style-settings)을 설치하면 사이드바에서 33개 옵션을 토글로 즉시 적용할 수 있습니다. 본 문서는 README의 분류 표를 보강하는 풀 레퍼런스입니다.

> 베이스라인: **v2.13.0**

---

## 📑 타이포 (5종)

| 항목 | 종류 | 기본값 | 설명 |
|------|------|--------|------|
| 본문 폰트 크기 | 슬라이더 | 15px | 13–18px |
| 본문 줄간격 | 셀렉트 | 1.5 | 1.35 / 1.45 / 1.5 / 1.6 / 1.7 |
| 본문 최대 폭 | 셀렉트 | 420mm | 210 / 297 / 360 / 420mm / 100% |
| 본문 세리프 글꼴 | 토글 | OFF | Noto Serif KR |
| 한글/CJK +0.5px 보정 | 토글 | ON | 가독성 |

---

## 📊 표 (3종)

| 항목 | 종류 | 기본값 | 설명 |
|------|------|--------|------|
| 표 zebra 줄무늬 | 토글 | ON | 짝수 행 옅은 배경 |
| 표 모던 스타일 강화 | 토글 | ON | 헤더/첫 컬럼/hover/PDF border 강화 |
| 표 sticky header | 토글 | ON | accent underline + blur (v2.12.0+) |

---

## 📝 보고서 (7종)

| 항목 | 종류 | 기본값 | 설명 |
|------|------|--------|------|
| **보고서 모드** | 토글 | OFF | 표지+넘버링+들여쓰기+세리프 한 번에 |
| 첫 줄 들여쓰기 | 토글 | OFF | 1em |
| 헤더 자동 넘버링 | 토글 | OFF | 1. / 1.1 / 1.1.1 |
| 드롭 캡 | 토글 | OFF | 첫 문단 첫 글자 크게 |
| 간격 프리셋 | 셀렉트 | 표준 | 컴팩트 / 표준 / 여유 |
| 헤더 강조 색상 | 색상 | `#4b5563` | 자유 색상 |
| 시선 보호 모드 | 토글 | OFF | 베이지 배경 |

---

## 🖨️ PDF (9종)

| 항목 | 종류 | 기본값 | 설명 |
|------|------|--------|------|
| PDF 페이지 크기 | 셀렉트 | A3 가로 | A4 세로 / A4 가로 / A3 가로 |
| PDF 블록 분할 방지 강화 | 토글 | ON | callout/표/Mermaid/코드/이미지 분할 완화 |
| **PDF 첫 페이지 우측 본문** | 텍스트 | (빈 값) | 예: `회사명`, `2026 Q2 보고서` |
| **PDF 첫 페이지 우측 라벨** | 텍스트 | (빈 값) | 예: `PREPARED BY`, `AUTHOR` |
| **PDF 첫 페이지 우측 사이드바 색** | 색상 | `#111827` | 우측 수직 막대 색 |
| **PDF 첫 페이지 좌측 본문** | 텍스트 | (빈 값) | 예: `Q2 Security Review` |
| **PDF 첫 페이지 좌측 라벨** | 텍스트 | (빈 값) | 예: `CONFIDENTIAL` |
| **PDF 첫 페이지 좌측 사이드바 색** | 색상 | `#0ea5e9` | 좌측 수직 막대 색 |
| **PDF 첫 페이지 라벨 색** | 색상 | `#6b7280` | 좌/우 라벨 공통 색 |

---

## 🎨 컬러 (9종)

| 항목 | 종류 | 기본값 | 설명 |
|------|------|--------|------|
| 액센트 컬러 프리셋 | 셀렉트 | Graphite | Graphite / Blue / Teal / Violet / Amber |
| 코드블록 테마 | 셀렉트 | Light | Light / Solarized / Nord / Dracula |
| OS 다크 모드 자동 추종 | 토글 | OFF | 시스템 설정 따라감 |
| Glass 강도 (`--og-glass-blur`) | 셀렉트 | 12px | Off / Reduced(8) / Subtle(10) / Standard(12) / Strong(16) / Max(20) |
| (그 외 액센트 변종 / 다크 톤 / Settings 행 hover / Editing Toolbar 등 5종) | — | — | 플러그인 UI 참조 |

---

## 사용자 클래스 (수동 부여)

Style Settings 옵션과 별개로, 노트 안에서 직접 부여하는 유틸리티 클래스 모음입니다.

| 클래스 | 위치 | 효과 |
|--------|------|------|
| `.ogd-blur` | inline element | 텍스트 blur, hover 시 해제 |
| `.ogd-cover` | h1 | 표지 페이지 강제 |
| `.cover-page` | YAML cssclasses 또는 div wrapper | 세로 중앙 정렬된 레포트 표지 + 자동 페이지 분할 |
| `.cover-meta` | div inside `.cover-page` | 표지 하단 메타(날짜/버전) 모노스페이스 |
| `.cover-rule` | div inside `.cover-page` | 제목 아래 80×3px accent 룰 |
| `.ogd-mini-toc` | YAML cssclasses 또는 div wrapper | Reading view 우측 sticky mini TOC, 모바일 자동 인라인 |
| `.ogd-print-toc` | div wrapper | **(v2.13.0+)** A3 PDF 자동 목차 페이지 (cover 다음, dotted leader) |
| `sticky-first-col` | `<table>` | 첫 컬럼 sticky scroll |
| `.num` | th/td | 숫자 우측정렬 + tabular-nums |
| `wide-table` | `<table>` | 열이 많은 표의 폰트/간격 압축 |
| `compact-table` | `<table>` | 로그/체크리스트용 조밀한 표 |
| `numeric-table` | `<table>` | 숫자 중심 표 우측 정렬 |
| `comparison-table` | `<table>` | 비교표 첫 컬럼/헤더 강조 |
| `risk-table` | `<table>` | 위험도/상태 badge 스타일 (`.risk-high`, `.risk-medium`, `.risk-low`, `.risk-ok`) |
| `matrix-table` | `<table>` | 매트릭스형 표 중앙 정렬 |
| `print-fit-table` | `<table>` | PDF 출력 시 폰트/패딩 축소 |
| `wrap-table` | `<table>` | 긴 URL/식별자 줄바꿈 강화 |
| `nowrap-code-table` | `<table>` | 긴 코드 토큰을 한 줄 ellipsis로 표시 |
| `scroll-token-table` | `<table>` | 코드 토큰 셀 폭을 보존해 행 높이 급증 완화 |
| `scroll-table` | `<table>` | 화면에서는 표 자체를 가로 스크롤 |

> Dataview 표는 v2.13.0부터 자동으로 sticky header + zebra + tabular-nums 가 적용됩니다 (`.block-language-dataview table`).

---

## Callout 종류

| 데이터-콜아웃 | 색상 | 용도 |
|--------------|------|------|
| `conclusion` | 그레이 | 최종 요약·판단 |
| `recommendation` | 그린 | 권장 조치 |
| `risk` | 앰버 | 위험·주의 |
| `action` | 시안 | 다음 작업 |
| `decision` | 그레이 | 결정 사항 |
| `note` / `info` | 블루 | 일반 정보 |
| `tip` / `hint` / `important` | 시안 | 팁, 중요 |
| `abstract` / `summary` / `tldr` | 보라 | 요약 |
| `example` | 앰버 | 예시 |
| `quote` / `cite` | 그레이 (italic) | 인용 (v2.11+ no-left-line) |
| `question` / `help` / `faq` | 옐로 | 질문 |
| `warning` / `danger` / `error` / `bug` | 오렌지 | 경고 |
| `success` / `check` / `done` | 그린 | 완료 |
| `secret` / `hidden` | 그레이 + blur | 가려진 내용 |

---

## 관련 문서
- [README.md](../README.md) — 테마 소개 / 설치 / 신기능
- [CHANGELOG.md](../CHANGELOG.md) — 전체 릴리즈 노트
- [docs/fixtures/](fixtures/) — 디자인 미리보기 HTML
