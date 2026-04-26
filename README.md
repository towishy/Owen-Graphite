# Owen Graphite - Obsidian Theme

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/towishy/Owen-Graphite?style=flat-square)](https://github.com/towishy/Owen-Graphite/releases/latest)
[![GitHub License](https://img.shields.io/github/license/towishy/Owen-Graphite?style=flat-square)](LICENSE)
[![Obsidian Downloads](https://img.shields.io/badge/Obsidian-Compatible-7c3aed?style=flat-square&logo=obsidian)](https://obsidian.md)
[![Style Settings](https://img.shields.io/badge/Style%20Settings-19%20options-0d9488?style=flat-square)](#style-settings-항목)

> **Obsidian 보고서 지향 라이트/다크 테마.**
> 그래파이트(graphite) 기반의 차분한 색감, **A3 인쇄 친화 레이아웃**,
> **Live Preview ↔ Reading View 시각 동기**, **한국어 보고서 작성 최적화**.

![Light Mode](screenshots/light.png)

<details>
<summary>📷 Dark Mode / Report Mode 스크린샷</summary>

![Dark Mode](screenshots/dark.png)
![Report Mode (auto-numbering + serif body + cover page)](screenshots/report.png)

</details>

---

## ✨ 한 줄 요약

| 분야 | 내용 |
|------|------|
| **타깃** | 보고서·기술 문서·위키 작성자 (특히 한국어) |
| **차별점** | A3 인쇄 + 헤더 자동 넘버링 + 표지 + **PDF 첫 페이지 모던 헤더 (Side Bar + Two-line)** + Style Settings 19종 + Live Preview/Reading parity |
| **Light & Dark** | ✅ 양쪽 모두 모든 위젯 패리티 보장 |
| **모바일** | ✅ Desktop & Mobile |
| **버전** | `1.7.6` (Obsidian 1.6.0+) |

---

## 📦 설치

### 옵션 A — Obsidian 커뮤니티 마켓 (승인 후)

1. 설정 → **외관 → 테마 관리**
2. 검색: `Owen Graphite`
3. 설치 → 사용

### 옵션 B — 수동 설치

```bash
cd <YourVault>/.obsidian/themes
git clone https://github.com/towishy/Owen-Graphite.git "Owen Graphite"
```

또는 [Releases 페이지](https://github.com/towishy/Owen-Graphite/releases/latest)에서
`theme.css`, `manifest.json`만 다운로드 → `<YourVault>/.obsidian/themes/Owen Graphite/`에 배치.

이후 Obsidian → 설정 → **외관 → 테마** → `Owen Graphite` 선택.

### 옵션 C — Style Settings 통합 (권장)

[Style Settings](https://github.com/mgmeyers/obsidian-style-settings) 플러그인 설치 시
사이드바에서 19개 옵션으로 즉시 모드 전환 가능.
자세한 설정 방법은 아래 [⚙️ Style Settings 플러그인 설정](#%EF%B8%8F-style-settings-%ED%94%8C%EB%9F%AC%EA%B7%B8%EC%9D%B8-%EC%84%A4%EC%A0%95) 섹션을 참고하세요.

---

## ⚙️ Style Settings 플러그인 설정

> **이 테마의 모든 커스터마이징(보고서 모드, A3 페이지 크기, 액센트 컬러, PDF 첫 페이지 헤더 등)은 [Style Settings](https://github.com/mgmeyers/obsidian-style-settings) 플러그인을 통해 제어합니다.** 플러그인이 없어도 테마 자체는 동작하지만, **PDF 첫 페이지 헤더 / 보고서 모드 / 액센트 컬러 변경 등 핵심 기능을 사용하려면 반드시 설치해야 합니다.**

### 1단계 — Style Settings 플러그인 설치

1. Obsidian → **설정 → 커뮤니티 플러그인 → 탐색**
2. 검색: `Style Settings`
3. **설치 → 활성화**

### 2단계 — 테마 옵션 패널 열기

1. 좌측 사이드바 하단 **톱니바퀴 아이콘** 또는 명령 팔레트(`⌘ P`) → `Style Settings: Show style settings view` 실행
2. 좌측 트리에서 **`Owen Graphite`** 펼치기
3. 카테고리별로 토글·슬라이더·텍스트 입력·색상 선택기를 통해 즉시 적용

### 3단계 — PDF 첫 페이지 헤더 설정 (Design ② Side Bar + Two-line)

PDF로 내보낼 때 **첫 페이지 좌·우 상단**에 회사 정보·기밀 등급·작성자·프로젝트 코드 등을 표시할 수 있습니다.
모든 항목은 **비워두면 표시되지 않으므로**, 필요한 쪽만 채우면 됩니다.

#### 우측 (`PREPARED BY` 영역, 기본 색상 `#111827` Dark)

| Style Settings 항목명 | 입력 예시 | 설명 |
|----------------------|----------|------|
| **PDF 첫 페이지 우측 라벨** | `PREPARED BY`, `AUTHOR`, `작성자` | 상단 작은 대문자 라벨 (7.5pt SemiBold) |
| **PDF 첫 페이지 우측 본문** | `Security Architecture Team`, `홍길동 · CSA` | 하단 큰 글씨 본문 (10.5pt Medium) |
| **PDF 첫 페이지 우측 사이드바 색** | `#111827` (기본) / `#bc8cff` 등 | 우측 3px 수직 막대 색 |

#### 좌측 (`CONFIDENTIAL` 영역, 기본 색상 `#0ea5e9` Sky)

| Style Settings 항목명 | 입력 예시 | 설명 |
|----------------------|----------|------|
| **PDF 첫 페이지 좌측 라벨** | `CONFIDENTIAL`, `INTERNAL`, `프로젝트 코드` | 상단 작은 대문자 라벨 |
| **PDF 첫 페이지 좌측 본문** | `Q2 Security Review · 분기 보고서` | 하단 본문 |
| **PDF 첫 페이지 좌측 사이드바 색** | `#0ea5e9` (기본) / `#dc2626` 등 | 좌측 3px 수직 막대 색 |

#### 공통

| 항목 | 기본값 | 설명 |
|------|-------|------|
| **PDF 첫 페이지 라벨 색** | `#6b7280` | 좌·우 라벨 글자 공통 색상 |

#### 입력 예시 (보고서 표지)

```
좌측 라벨:    CONFIDENTIAL
좌측 본문:    Q2 Security Review · 분기 보고서
좌측 막대 색: #0ea5e9 (Sky)

우측 라벨:    PREPARED BY
우측 본문:    Security Architecture Team
우측 막대 색: #111827 (Dark)

라벨 색:      #6b7280 (Gray)
```

→ PDF로 내보내면 첫 페이지 상단에 다음과 같이 표시됩니다:

```
│ CONFIDENTIAL                              PREPARED BY │
│ Q2 Security Review · 분기 보고서  Security Architecture Team │
└─ Sky 막대                                Dark 막대 ─┘
```

> 💡 **팁:** 라벨만 채우고 본문을 비우거나, 본문만 채우고 라벨을 비울 수도 있습니다. 한 쪽(좌 또는 우)을 통째로 비우면 해당 쪽 사이드바·라벨·본문 모두 렌더링되지 않습니다.

### 4단계 — 보고서 모드 토글 (선택)

표지 페이지 + 헤더 자동 넘버링 + 들여쓰기 + 세리프 본문을 **한 번에** 적용:

1. Style Settings 패널 → `Owen Graphite` → **보고서 모드** 토글 ON
2. PDF 내보내기 시 자동으로:
   - 첫 H1 → 화면 중앙 큰 표지로 변환
   - H2/H3/H4 → `1.` / `1.1` / `1.1.1` 자동 넘버링
   - 본문 → Noto Serif KR 세리프
   - 모든 문단 첫 줄 들여쓰기

### 5단계 — A3 가로 페이지 크기 설정

1. Style Settings → **PDF 페이지 크기** → `A3 가로` 선택 (기본값)
2. Obsidian → **PDF로 내보내기** → 페이지 크기 `A3` / 방향 `가로` / 여백 `15mm`

### Style Settings 없이 사용하면?

- 테마는 정상 동작하지만 **모든 옵션이 기본값으로 고정**됩니다.
- PDF 첫 페이지 헤더는 **빈 값**으로 처리되어 표시되지 않습니다.
- 보고서 모드·액센트 컬러·코드블록 테마 등을 변경하려면 `theme.css`를 직접 수정해야 합니다.
- **결론: 플러그인 설치를 강력 권장합니다.**

---

## 🎨 주요 특징

### 시각 디자인
- **그래파이트 액센트**: 차분한 회색 + 5종 액센트 컬러 프리셋 (Graphite/Blue/Teal/Violet/Amber)
- **헤더 3단계 강조**: H1 좌측 5px 보더 + 그라디언트, H2 하단 220px 액센트 바, H3 좌측 보더
- **세련된 callout**: note·info·tip·abstract·example·quote·question·warning·success 9종
- **표 강화**: tabular-nums, hover 행, sticky 첫 컬럼, zebra 토글, `.num` 우측정렬

### Live Preview ↔ Reading View 동등 (v1.3.1)
- CM6 헤더 라인별 line-height + 폰트 명시 (1.45 generic 덮어쓰기 해소)
- 코드블록 박스 외곽선 (begin / middle / end 모두 좌우 보더)
- 위키링크 / 태그 / 인라인 코드 chip이 Source 모드에서도 동일한 모양
- Strong / em / strikethrough / 체크박스 정렬 보정
- Callout / 표 widget 변수 공유, frontmatter 박스 round border

### 보고서 출력 (v1.4.0)
- **A3 가로 기본** + Header(제목) / Footer(페이지 번호) 자동 삽입
- **헤더 자동 넘버링**: H2 = `1.`, H3 = `1.1`, H4 = `1.1.1`
- **드롭 캡 / 첫 줄 들여쓰기 / 세리프 본문** — 한국 보고서 스타일
- **표지 페이지**: 첫 H1을 화면 중앙 큰 글씨로 변환 (보고서 모드)
- **외부 링크 URL 자동 표시**, 표/이미지/callout `page-break-inside: avoid`

### PDF 첫 페이지 모던 헤더 (v1.5.0+)
- **Design ② Side Bar + Two-line** — 좌/우 각각 **라벨(소문자, 상단) + 본문(하단) 2줄 구조** + **3px 수직 사이드바**
- 상단 레이블: 7.5pt SemiBold uppercase + 1.8px letter-spacing
- 하단 본문: 10.5pt Medium, 본문 폰트 스택과 동일 (Pretendard 우선, macOS/Windows 패리티)
- 좌측은 `Sky #0ea5e9`, 우측은 `Dark #111827` 기본 (Style Settings에서 변경 가능)
- 라벨 또는 본문을 비워두면 해당 쪽 렌더링 생략

### 콘텐츠 강조
- `<kbd>` Mac 키 캡 스타일
- `> [!secret]` blur 처리, hover 시 해제
- Mermaid 카드형 컨테이너 (배경 + 둥근 모서리 + 그림자)
- 이미지 zoom-in 커서 + brightness hover
- Footnote ref 하이라이트, hover popover 그림자/패딩 통일

### 워크스페이스 폴리시
- 사이드바 폴더 path-based 색상
- 활성 파일 4px accent bar, 활성 탭 상단 액센트 보더
- 탭 아이콘 타입별 색상 (md/canvas/pdf/image)
- 검색/제안 결과 카드 hover

### 플러그인 통합 (라이트/다크 모두)
- **Dataview** 표 → 본 테마 표 스타일 통일
- **Properties** (Obsidian 1.4+) — 박스 + grid layout
- **Bases** (Obsidian 1.7+) — 카드 + 표 보더
- **Excalidraw**, **Kanban**, **Calendar**

### 접근성
- `:focus-visible` 두꺼운 outline + glow
- `prefers-contrast: high` — 보더·하이라이트 강화
- `prefers-reduced-motion` — 트랜지션 제거
- CJK 자동 +0.5px 보정 (한글 가독성)
- OS 다크 모드 자동 추종 옵션

---

## 📋 Style Settings 전체 옵션 목록

플러그인 설치 후 사이드바에서 토글로 즉시 적용:

| 항목 | 종류 | 기본값 | 설명 |
|------|------|--------|------|
| 본문 폰트 크기 | 슬라이더 | 15px | 13–18px |
| 본문 줄간격 | 셀렉트 | 1.5 | 1.35 / 1.45 / 1.5 / 1.6 / 1.7 |
| 본문 최대 폭 | 셀렉트 | 420mm | 210/297/360/420mm / 100% |
| 헤더 강조 색상 | 색상 | `#4b5563` | 자유 색상 |
| 표 zebra 줄무늬 | 토글 | ON | 짝수 행 옅은 배경 |
| **보고서 모드** | 토글 | OFF | 표지+넘버링+들여쓰기+세리프 한 번에 |
| 본문 세리프 글꼴 | 토글 | OFF | Noto Serif KR |
| 첫 줄 들여쓰기 | 토글 | OFF | 1em |
| 헤더 자동 넘버링 | 토글 | OFF | 1. / 1.1 / 1.1.1 |
| 드롭 캡 | 토글 | OFF | 첫 문단 첫 글자 크게 |
| 간격 프리셋 | 셀렉트 | 표준 | 컴팩트 / 표준 / 여유 |
| PDF 페이지 크기 | 셀렉트 | A3 가로 | A4 세로 / A4 가로 / A3 가로 |
| 액센트 컬러 프리셋 | 셀렉트 | Graphite | Graphite / Blue / Teal / Violet / Amber |
| 코드블록 테마 | 셀렉트 | Light | Light / Solarized / Nord / Dracula |
| 시선 보호 모드 | 토글 | OFF | 베이지 배경 |
| OS 다크 모드 자동 추종 | 토글 | OFF | 시스템 설정 따라감 |
| 한글/CJK +0.5px 보정 | 토글 | ON | 가독성 |
| **PDF 첫 페이지 우측 본문** | 텍스트 | (빈 값) | 예: `회사명`, `2026 Q2 보고서` |
| **PDF 첫 페이지 우측 라벨** | 텍스트 | (빈 값) | 예: `PREPARED BY`, `AUTHOR` |
| **PDF 첫 페이지 우측 사이드바 색** | 색상 | `#111827` | 우측 수직 막대 색 |
| **PDF 첫 페이지 좌측 본문** | 텍스트 | (빈 값) | 예: `Q2 Security Review` |
| **PDF 첫 페이지 좌측 라벨** | 텍스트 | (빈 값) | 예: `CONFIDENTIAL` |
| **PDF 첫 페이지 좌측 사이드바 색** | 색상 | `#0ea5e9` | 좌측 수직 막대 색 |
| **PDF 첫 페이지 라벨 색** | 색상 | `#6b7280` | 좌/우 라벨 공통 색 |

---

## 🏷️ 사용자 클래스 (수동 부여)

| 클래스 | 위치 | 효과 |
|--------|------|------|
| `.ogd-blur` | inline element | 텍스트 blur, hover 시 해제 |
| `.ogd-cover` | h1 | 표지 페이지 강제 |
| `sticky-first-col` | `<table>` | 첫 컬럼 sticky scroll |
| `.num` | th/td | 숫자 우측정렬 + tabular-nums |

```html
<span class="ogd-blur">민감한 정보</span>
```

---

## 💬 Callout 종류

| 데이터-콜아웃 | 색상 | 용도 |
|--------------|------|------|
| `note` / `info` | 블루 | 일반 정보 |
| `tip` / `hint` / `important` | 시안 | 팁, 중요 |
| `abstract` / `summary` / `tldr` | 보라 | 요약 |
| `example` | 앰버 | 예시 |
| `quote` / `cite` | 그레이 (italic) | 인용 |
| `question` / `help` / `faq` | 옐로 | 질문 |
| `warning` / `danger` / `error` / `bug` | 오렌지 | 경고 |
| `success` / `check` / `done` | 그린 | 완료 |
| `secret` / `hidden` | 그레이 + blur | 가려진 내용 |

---

## 🖨️ A3 인쇄 가이드

### Obsidian PDF Export
1. **보고서 모드 ON** (선택)
2. 메뉴 → **PDF로 내보내기**
3. 페이지 크기: **A3** / 방향: **가로** / 여백: 15mm
4. 모든 callout/표/이미지가 페이지 경계에서 자동 분할 회피

### 인쇄 시 자동 적용
- H1마다 새 페이지 시작
- 외부 링크 옆에 URL 자동 표시
- UI 영역(사이드바·탭·상태바·copy 버튼) 자동 숨김
- 색상 정확 출력 (`-webkit-print-color-adjust: exact`)

---

## 🅰️ 권장 폰트

미리 설치하면 더 깔끔합니다 (없어도 fallback 적용):

- **Pretendard** / **Pretendard Variable** — 본문 (sans)
- **Noto Sans KR** / **Apple SD Gothic Neo** — fallback
- **Noto Serif KR** / **나눔명조** — 보고서 모드 (serif)
- **JetBrains Mono** / **D2Coding** — 코드 (mono)

---

## 📁 파일 구조

```
Owen Graphite/
├── theme.css         # ~2,560줄, 모든 스타일
├── manifest.json     # 버전·메타
├── README.md         # 이 파일
├── CHANGELOG.md      # 버전별 변경 이력
├── LICENSE           # MIT
└── screenshots/
    ├── light.png     # 1280×720
    ├── dark.png
    └── report.png
```

---

## 📝 변경 이력

전체 이력은 [CHANGELOG.md](CHANGELOG.md) 참고.

- **v1.7.0** — UX·접근성·인쇄 종합 개선 (액티브 탭, 모바일 분기, PDF 푸터, 그래프 톤, 검색 강조, 임베드 액센트, 8종 체크박스, 태그 호버, `:focus-visible` 통일, `prefers-contrast`)
- **v1.6.1** — Editing Toolbar 좌측 여백 8px
- **v1.6.0** — 테마 이름 변경 (`Owen Graphite Document` → `Owen Graphite`), PDF 헤더 컨테이너 정리
- **v1.5.1** — Side Bar가 라벨+본문 양쪽을 모두 덮도록 확장 (Design ② 완성)
- **v1.5.0** — PDF 첫 페이지 모던 헤더 (Side Bar + Two-line, 좌·우 라벨 + 본문)
- **v1.4.7–1.4.12** — 첫 페이지 헤더 폰트 안정화 및 좌측 헤더 추가
- **v1.4.5–1.4.6** — PDF 첫 페이지 헤더 렌더링 수정 (Chromium @page var() 회피)
- **v1.4.1** — Blockquote/callout 좌측 보더 텍스트 겹침 수정
- **v1.4.0** — 33-point 종합 업그레이드 (보고서 모드, A4 옵션, 액센트 5종, 코드 4종, 접근성)
- **v1.3.1** — Live Preview ↔ Reading View 12-point parity
- **v1.3.0** — 13개 카테고리 종합 개선
- **v1.2.0** — Live Preview 빈 줄 압축
- **v1.1.0** — PDF 컴팩트 spacing
- **v1.0.0** — 초기 그래파이트 라이트 테마

---

## 🤝 기여

이슈, 기능 제안, PR을 환영합니다:
- 이슈: [GitHub Issues](https://github.com/towishy/Owen-Graphite/issues)
- 토론: [Discussions](https://github.com/towishy/Owen-Graphite/discussions)

---

## 📜 라이선스

[MIT License](LICENSE) © 2026 Owen ([@towishy](https://github.com/towishy))

---

## 🙏 크레딧

- 글꼴: Pretendard (Kil Hyung-jin), Noto Sans/Serif KR (Google), JetBrains Mono (JetBrains), D2Coding (Naver)
- 영감: Obsidian Minimal, Things, AnuPpuccin
- 빌드 환경: Obsidian 1.6.x / macOS · Windows · Linux
