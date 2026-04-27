# Owen Graphite - Obsidian Theme

Owen WIKI, Owen Graphite, Owen Editor는 LLM 기반 지식 정리부터 Obsidian 보고서 작성, Markdown 편집 UI까지 이어지는 Owen의 지식 작업 스택입니다.

![Owen GitHub Repository Picks](screenshots/readme/github-repo-promo-sample-readme.png)

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/towishy/Owen-Graphite?style=flat-square)](https://github.com/towishy/Owen-Graphite/releases/latest)
[![GitHub License](https://img.shields.io/github/license/towishy/Owen-Graphite?style=flat-square)](LICENSE)
[![Obsidian Downloads](https://img.shields.io/badge/Obsidian-Compatible-7c3aed?style=flat-square&logo=obsidian)](https://obsidian.md)
[![Style Settings](https://img.shields.io/badge/Style%20Settings-27%20options-0d9488?style=flat-square)](#style-settings-전체-옵션-목록)

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
| **차별점** | A3 인쇄 + 헤더 자동 넘버링 + 표지 + **PDF 첫 페이지 모던 헤더 (Side Bar + Two-line)** + **데스크톱 Liquid-glass chrome presets** + Style Settings 27종 + Live Preview/Reading parity |
| **Light & Dark** | ✅ 양쪽 모두 모든 위젯 패리티 보장 |
| **모바일** | ✅ Desktop & Mobile |
| **버전** | `1.8.53` (Obsidian 1.6.0+) |

---

## 📦 설치

### 옵션 A — Obsidian 커뮤니티 마켓 (승인 후)

1. 설정 → **외관 → 테마 관리**
2. 검색: `Owen Graphite`
3. 설치 → 사용

### 옵션 B — 수동 설치

Obsidian vault 안의 `.obsidian/themes/Owen Graphite/` 폴더에 테마 파일을 배치합니다.

#### Windows

PowerShell에서 vault 경로를 기준으로 실행합니다.

```powershell
cd "D:\Path\To\YourVault\.obsidian\themes"
git clone https://github.com/towishy/Owen-Graphite.git "Owen Graphite"
```

예: vault가 `D:\JAELE\WIKI`라면 대상 경로는 `D:\JAELE\WIKI\.obsidian\themes\Owen Graphite\`입니다.

#### macOS / Linux

```bash
cd <YourVault>/.obsidian/themes
git clone https://github.com/towishy/Owen-Graphite.git "Owen Graphite"
```

예: vault가 `/Users/owen/Work/WIKI`라면 대상 경로는 `/Users/owen/Work/WIKI/.obsidian/themes/Owen Graphite/`입니다.

#### Releases 파일로 설치

[Releases 페이지](https://github.com/towishy/Owen-Graphite/releases/latest)에서 `theme.css`, `manifest.json`, `README.md`, `CHANGELOG.md`, `LICENSE`, `screenshots/`를 다운로드한 뒤 아래 위치에 배치합니다.

| 플랫폼 | 테마 대상 경로 |
|------|------|
| Windows | `<YourVault>\.obsidian\themes\Owen Graphite\` |
| macOS / Linux | `<YourVault>/.obsidian/themes/Owen Graphite/` |

선택 CSS snippet을 함께 쓰는 경우 `snippets/zz-obsidian-gray-force-override-v2.css`를 아래 위치에 배치한 뒤 Obsidian 설정 → 외관 → CSS snippets에서 활성화하세요.

| 플랫폼 | snippet 대상 경로 |
|------|------|
| Windows | `<YourVault>\.obsidian\snippets\` |
| macOS / Linux | `<YourVault>/.obsidian/snippets/` |

이후 Obsidian → 설정 → **외관 → 테마** → `Owen Graphite` 선택.

> Obsidian 테마 관리 화면에서 README나 스크린샷이 비어 보이면 테마 폴더에 `README.md`와 `screenshots/`가 같이 들어 있는지 확인한 뒤, **업데이트 확인** 또는 Obsidian 재시작을 실행하세요.

### 옵션 C — Style Settings 통합 (권장)

[Style Settings](https://github.com/mgmeyers/obsidian-style-settings) 플러그인 설치 시
사이드바에서 27개 옵션으로 즉시 모드 전환 가능.
주요 사용 흐름은 아래 [빠른 사용법](#-빠른-사용법)과 [고급 설정 요약](#-고급-설정-요약)을 참고하세요.

---

## 🚀 빠른 사용법

1. Obsidian → 설정 → 외관 → 테마에서 **Owen Graphite**를 선택합니다.
2. [Style Settings](https://github.com/mgmeyers/obsidian-style-settings) 플러그인을 설치하면 27개 옵션을 UI에서 조정할 수 있습니다.
3. 보고서 PDF가 필요하면 **보고서 모드**를 켜고, PDF Export에서 `A3` / `가로` / `15mm` 여백을 선택합니다.
4. 첫 페이지 헤더가 필요하면 Style Settings에서 좌·우 라벨/본문/사이드바 색을 채웁니다. 비워둔 쪽은 출력되지 않습니다.

## 🔧 고급 설정 요약

| 영역 | 대표 옵션 | 용도 |
|------|-----------|------|
| 문서 밀도 | 본문 폰트 크기, 줄간격, 최대 폭, 간격 프리셋 | 화면/인쇄 가독성 조정 |
| 보고서 출력 | 보고서 모드, A3 페이지, 세리프 본문, 첫 줄 들여쓰기, 자동 넘버링 | PDF 보고서 레이아웃 구성 |
| 색상/표현 | 액센트 컬러, 코드블록 테마, 시선 보호 모드, OS 다크 모드, Glass 강도 | 개인 작업 환경 튜닝 |
| PDF 첫 페이지 | 좌·우 라벨/본문/사이드바 색, 라벨 색 | 표지 상단 메타 정보 출력 |
| 안정성 | 표 zebra, 표 모던 스타일, PDF 블록 분할 방지 | 긴 표·callout·이미지 출력 안정화 |

Style Settings UI는 `읽기와 본문`, `표와 코드`, `보고서와 PDF`, `워크스페이스와 접근성`, `PDF 첫 페이지 헤더` 구획으로 나뉘어 긴 옵션 목록을 빠르게 훑을 수 있습니다. 실제 조정 가능한 옵션 수는 기존과 동일한 27개입니다.

Style Settings 없이도 테마는 정상 동작하지만 모든 값이 기본값으로 고정됩니다. PDF 헤더, 보고서 모드, 액센트 컬러 변경을 자주 쓴다면 플러그인 사용을 권장합니다.

### 추천 프리셋 조합

| 사용 흐름 | 권장 설정 | 보조 클래스/패턴 |
|----------|-----------|------------------|
| 매일 작성 | 표준 간격, Graphite accent, Subtle 또는 Standard glass | 기본 Markdown + 일반 callout |
| 긴 보고서/PDF | 보고서 모드, PDF 블록 분할 방지, A3 가로 preview | `wide-table print-fit-table`, 보고서형 callout |
| 눈 피로 감소 | 줄간격 1.6 또는 1.7, 시선 보호 모드, Reduced glass | 외부 링크/출처 목록은 `.ogd-reference-list` |
| 기술 감사 보고서 | 표 모던 스타일, 코드블록 Light/Nord, 자동 넘버링 | `comparison-table nowrap-code-table`, `risk-table` |
| 저성능 환경 | Glass Off 또는 Reduced, 애니메이션 최소화 | 큰 Mermaid/표는 fixture로 사전 확인 |

### Glass 강도 프리셋

| 프리셋 | 권장 상황 |
|------|-----------|
| Off | glass 효과 없이 가장 단순한 UI가 필요할 때 |
| Reduced | 배터리·저성능 환경에서 blur 부담을 줄이고 싶을 때 |
| Subtle | 업무용으로 차분한 glass 느낌만 남기고 싶을 때 |
| Standard | 기본 추천값 |
| Strong | glass 표면과 그림자를 더 뚜렷하게 보고 싶을 때 |

`prefers-reduced-motion` 환경에서는 hover lift와 blur filter가 자동으로 억제됩니다. 고대비/forced-colors 환경에서는 glass border와 focus outline을 더 명확하게 유지합니다.

---

## 🧩 선택 CSS snippet — Gray Report Force Override

릴리즈 자산에 포함된 `snippets/zz-obsidian-gray-force-override-v2.css`는 Owen Graphite를 기반으로 **더 엄격한 회색 보고서 톤**을 강제하고 싶을 때 쓰는 선택 snippet입니다. 테마 본체보다 강한 우선순위로 적용되므로, 팀 보고서나 고객 제출 문서처럼 화면·PDF·공유 환경에서 색상 편차를 줄이고 싶을 때 적합합니다.

### 디자인 의도

| 초점 | 내용 |
|------|------|
| Graphite-first | 헤더, blockquote, callout, 코드 색상을 회색 중심으로 고정 |
| 보고서 구조 | H1/H2/H3, TOC, 캡션, diagram frame, footnote, task list를 같은 톤으로 정리 |
| 표/PDF 안정성 | 비교표·매트릭스·고객 보고서 표가 화면과 PDF에서 균일하게 보이도록 보강 |
| 링크 구분 | 외부 URL은 Muted Gray 점선 밑줄로 내부 링크와 분리 |
| Live Preview 안전성 | Reading View 장식을 CM6 편집 라인에 과도하게 강제하지 않음 |

![Gray override snippet 8개 구조 개선 preview](screenshots/snippet-design-8-improvements-preview.png)

### 적용 방법

1. 릴리즈에서 `zz-obsidian-gray-force-override-v2.css`를 다운로드합니다.
2. `<YourVault>/.obsidian/snippets/`에 배치합니다.
3. Obsidian → 설정 → 외관 → **CSS snippets**에서 `zz-obsidian-gray-force-override-v2`를 활성화합니다.

> 이 snippet은 선택 사항입니다. Owen Graphite 기본 테마만으로도 정상 동작하며, snippet은 더 단단한 회색 보고서 톤이 필요할 때 추가로 켜는 보강 레이어입니다.

---

## 🎨 주요 특징

| 영역 | 특징 |
|------|------|
| 시각 디자인 | Graphite 기반 팔레트, 5종 액센트, heading rhythm, 표/코드/callout 톤 통일 |
| Live Preview | Reading View와 위키링크·태그·코드·callout·표 스타일을 최대한 맞추되 클릭 편집성과 커서 좌표 안정성을 우선 |
| 보고서 출력 | A3 가로, 헤더/푸터, 자동 넘버링, 표지 페이지, 세리프 본문, PDF page-break 보강 |
| PDF 첫 페이지 | 좌·우 라벨/본문 2줄 구조, 3px side bar, 빈 값 자동 생략 |
| 콘텐츠 강조 | `<kbd>`, `secret` blur, Mermaid frame, 이미지 hover, footnote/popover 톤 정리 |
| 참고 출처 | `.ogd-reference-list` 선택 패턴으로 링크 밀집 구간을 출처/문서/설명 구조로 정리 |
| 워크스페이스 | 사이드바, 탭, 검색, Properties, Bases, Canvas, Graph, Backlink, Tag pane 톤 통일 |
| 접근성 | `:focus-visible`, high contrast, reduced motion, CJK 가독성 보정, OS dark mode 옵션 |

Live Preview 클릭 회귀 확인용 문서는 [docs/fixtures/live-preview-editing.md](docs/fixtures/live-preview-editing.md)에 있습니다.

### 참고 출처 정리 패턴

링크가 많은 참고 출처 섹션은 선택적으로 HTML list에 `.ogd-reference-list`를 붙여 더 빠르게 스캔할 수 있습니다. 일반 Markdown 목록 스타일은 바꾸지 않습니다.

```html
<p class="ogd-reference-summary">링크 밀집 구간만 출처명, 문서명, 설명으로 분리합니다.</p>
<ol class="ogd-reference-list">
    <li>
        <span class="ogd-reference-source">Microsoft</span>
        <div class="ogd-reference-main">
            <a class="ogd-reference-title" href="https://learn.microsoft.com/">Microsoft Purview service description</a>
            <span class="ogd-reference-meta">Purview 기능별 라이선스 기준</span>
        </div>
    </li>
</ol>
```

### 보고서형 callout 팔레트 (v1.8.0+)

```markdown
> [!conclusion] 권장 결론
> 최종 판단이나 제안 텍스트를 강조합니다.

> [!recommendation] 권장 조치
> 실행 가능한 권장안을 정리합니다.

> [!risk] 주의
> 정책 충돌, 우회 가능성, 운영 위험을 표시합니다.

> [!action] 다음 단계
> 담당자나 후속 작업을 나열합니다.

> [!decision] 결정 사항
> 회의 또는 설계 결정의 확정 내용을 기록합니다.
```

Callout 회귀 확인용 fixture는 [docs/fixtures/callout-report.md](docs/fixtures/callout-report.md)와 [docs/fixtures/callout-preview.html](docs/fixtures/callout-preview.html)에 있습니다.

### Detail Preview

| 초점 | 확인 위치 | 확인 내용 |
|------|-----------|-----------|
| 파일 탐색기 active/chevron | [screenshots/light.png](screenshots/light.png), [screenshots/dark.png](screenshots/dark.png) | 접기 아이콘, active 파일, hover 톤 |
| 보고서형 callout | [docs/fixtures/callout-preview.html](docs/fixtures/callout-preview.html) | conclusion/recommendation/risk/action/decision 톤 |
| 긴 식별자 표 | [docs/fixtures/table-preview.html](docs/fixtures/table-preview.html) | `nowrap-code-table`, `scroll-token-table`, `scroll-table` 조합 |

### 워크스페이스 폴리시
- 사이드바 폴더 path-based 색상
- 활성 파일 4px accent bar, 활성 탭 상단 액센트 보더
- File Explorer hover/active 상태 강화, active folder hierarchy 강조
- 탭 아이콘 타입별 색상 (md/canvas/pdf/image)
- 검색/제안 결과 카드 hover

### 작업 상태 체크박스 (v1.8.2+)

```markdown
- [ ] 대기
- [x] 완료
- [/] 진행 중
- [>] 위임/전달
- [!] 중요/위험
- [?] 확인 필요
- [-] 취소/제외
- [*] 핵심/즐겨찾기
```

### 플러그인 통합 (라이트/다크 모두)
- **Dataview** 표 → 본 테마 표 스타일 통일
- **Properties** (Obsidian 1.4+) — 박스 + grid layout
- **Bases** (Obsidian 1.7+) — 카드 + 표 보더
- **Excalidraw**, **Kanban**, **Calendar**
- Command Palette / Modal / Menu / Hover Preview overlay 톤 통일
- Settings / Style Settings controls — input, dropdown, toggle, slider, color picker 톤 통일
- Canvas / Graph / Backlink / Tag pane — 지식 그래프 탐색 UI 톤 통일

| 플러그인/영역 | 지원 수준 | 비고 |
|--------------|-----------|------|
| Dataview | Styled | 표, hover, zebra, numeric tone 통일 |
| Properties / Bases | Styled | 카드/표/입력면 Graphite 톤 적용 |
| Canvas / Graph | Styled | 노드, edge, control surface 톤 정리 |
| Backlinks / Outgoing / Search / Tag pane | Styled | 결과 match, count badge, tag chip 정리 |
| Excalidraw / Kanban / Calendar | Basic tone aligned | 주요 surface와 border 톤만 보정 |
| Editing Toolbar | Styled | top bar, icon button, submenu glass 톤 |
| 알 수 없는 third-party view | Not modified | Obsidian 기본 변수 상속에 의존 |

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
| 표 모던 스타일 강화 | 토글 | ON | 헤더/첫 컬럼/hover/PDF border 강화 |
| PDF 블록 분할 방지 강화 | 토글 | ON | callout/표/Mermaid/코드/이미지 분할 완화 |
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

```html
<span class="ogd-blur">민감한 정보</span>
```

### 보고서형 테이블 클래스

Markdown 표 바로 아래에 HTML 표를 쓰거나, Dataview/HTML 출력에서 class를 줄 수 있을 때 다음 클래스를 사용합니다.

![Table design samples](screenshots/table-sample.png)

전체 미리보기 HTML은 [docs/fixtures/table-preview.html](docs/fixtures/table-preview.html), PDF/모바일 회귀 확인용 Markdown 샘플은 [docs/fixtures/table-report.md](docs/fixtures/table-report.md)에 있습니다.

```html
<table class="wide-table print-fit-table comparison-table nowrap-code-table">
    <thead>
        <tr><th>항목</th><th>정책</th><th class="num">점수</th></tr>
    </thead>
    <tbody>
        <tr><td>Baseline</td><td>장문 정책 설명</td><td class="num">95.2%</td></tr>
    </tbody>
</table>
<p class="table-note">출처: 내부 검토 샘플</p>
```

- `wide-table print-fit-table`: 열이 많은 A3/PDF 표
- `numeric-table`: 수치·금액·점수 중심 표
- `comparison-table`: 제품/정책/옵션 비교표
- `risk-table`: `High`, `Medium`, `Low`, `OK`, `Fail` 같은 상태값 강조
- `wrap-table`: 긴 URL, 정책명, 리소스 ID 줄바꿈
- `nowrap-code-table` / `scroll-token-table`: 정책 ID처럼 줄바꿈보다 스캔성이 중요한 긴 코드 토큰
- `scroll-table`: 화면 검토에서는 가로 스크롤을 허용하고 PDF에서는 기존 print-fit 규칙과 함께 사용

권장 조합은 `comparison-table nowrap-code-table`(정책 비교), `wide-table scroll-table scroll-token-table`(화면 검토용 넓은 표), `wide-table print-fit-table wrap-table`(PDF 제출용 넓은 표)입니다.

---

## 💬 Callout 종류

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
├── theme.css          # 테마 본체
├── manifest.json      # Obsidian 테마 메타데이터
├── README.md          # 빠른 사용법과 설정 요약
├── CHANGELOG.md       # 전체 릴리즈 노트
├── snippets/          # 선택 CSS snippet
├── docs/fixtures/     # 검증·디자인 preview fixture
├── screenshots/       # README/마켓플레이스 이미지
└── scripts/           # 로컬 검증 스크립트
```

### 로컬 검증

```bash
python scripts/validate_theme.py
```

Windows/macOS 양쪽에서 같은 검증 경로를 쓰기 위해 모든 로컬 검증과 릴리즈 자동화는 Python 스크립트로만 관리합니다. 검증기는 필수 파일, 버전 정합성, Style Settings 카운트, 스크린샷 크기, contrast audit, 릴리즈 ZIP 내용, Live Preview 안전 selector, `git diff --check`, 선택적 vault sync를 확인하고 마지막에 release checklist를 출력합니다.

### 색상 대비 감사

```bash
python scripts/contrast_audit.py
```

주요 light/dark 텍스트, 링크, 표, callout, 검색 하이라이트 색상 조합의 WCAG AA 기본 대비를 확인합니다.

### 시각 회귀 확인

실제 Obsidian DOM과 가장 가까운 HTML fixture는 [docs/fixtures](docs/fixtures)에 모아 둡니다. 브라우저 또는 Playwright 같은 캡처 도구로 `table-preview.html`, `callout-preview.html`, `search-input-glass-preview.html`, `tab-glass-preview.html`을 캡처해 light/dark/report 변경 전후를 비교하면 CSS cascade 회귀를 빠르게 확인할 수 있습니다.

```bash
python -m pip install playwright
python -m playwright install chromium
python scripts/visual_regression.py
```

캡처 결과는 `screenshots/fixture-regression/` 아래에 생성됩니다. 이 폴더는 비교용 로컬 산출물로 사용하고 릴리즈 asset에는 포함하지 않습니다.

### 릴리즈 ZIP 생성

```bash
python scripts/build_release.py
```

생성물은 `dist/Owen-Graphite-<version>.zip`에 저장되며, 수동 설치용 필수 파일과 선택 snippet을 `Owen Graphite/` 폴더 구조로 묶습니다.

---

## 📝 변경 이력

전체 이력은 [CHANGELOG.md](CHANGELOG.md) 참고.

- **v1.8.53** — 릴리즈 ZIP과 GitHub Release asset에 README 참조 스크린샷을 모두 포함하도록 패키징 보강
- **v1.8.52** — 파일 탐색기 폴더/문서 아이콘을 Thin Outline Icons로 정리, 선택 문서 glass 효과에서 outline grow와 heavy filled icon 제거, vault tree 시안 fixture/스크린샷 추가
- **v1.8.51** — callout fixture, contrast audit, release checklist, 추천 프리셋/플러그인 지원표/시각 회귀 문서, CSS 섹션 인덱스와 토큰 alias 추가
- **v1.8.50** — Style Settings 구획 헤더, 현대적인 파일 탐색기 접기 chevron, 본문 좌측 여백 보강, 긴 코드 토큰용 표 유틸리티, 보고서형 callout 아이콘/톤 정리
- **v1.8.49** — 참고 출처 링크 밀집 구간을 출처/문서/설명 구조로 정리하는 `.ogd-reference-list` 패턴 추가
- **v1.8.45** — 기존 Ruby 검증 스크립트 제거, Python-only 검증/릴리즈 자동화로 정리, Python 로컬 산출물 ignore 추가
- **v1.8.44** — Python 기반 검증기/릴리즈 ZIP 생성기 추가, GitHub Actions 검증·릴리즈 워크플로 Python 단일화, 수동 설치용 ZIP asset 자동 생성
- **v1.8.43** — Style Settings Glass 강도 프리셋(Off/Reduced/Subtle/Standard/Strong), 저성능용 Reduced glass, 컨트롤/Properties/Editing Toolbar glass polish, 스크린샷 갱신
- **v1.8.42** — Floating UI와 Settings 컨트롤 전반에 liquid-glass 확장, 토글 glass track/thumb, 선택 suggestion 상태 세밀화, Settings 행 hover 외곽 박스 복구
- **v1.8.41** — Editing Toolbar 좌측 간격 보정, 프레임 조절바 hover 표시 방식, workspace divider/파일 탐색기 스크롤바 라인 정리
- **v1.8.40** — 검색 옵션 suggestion popover hover/click 상태에 liquid-glass + 그림자 효과 적용
- **v1.8.39** — Settings 모달 liquid-glass hover 적용 (좌측 nav + 우측 설정 행, light/dark 패리티)
- **v1.8.38** — macOS 사이드바 토글 버튼 hover 시 liquid-glass 표면 적용 (본얰 상태는 native subtle 유지)
- **v1.8.37** — macOS 사이드바 토글 버튼이 타이틀바 안에서 36×36 프레임으로 떠 보이던 회귀 수정
- **v1.8.36** — 데스크톱 chrome 전역 liquid-glass: ribbon·사이드바 토글·탭 list·nav hover·active file·Editing Toolbar·resize handle·context menu·tooltip·breadcrumb (mobile parity 유지)
- **v1.8.19** — PDF 보고서 간격, 표 가독성, 상태 badge, action/summary callout, 반복 table header 안정화 및 10개 개선 preview 추가
- **v1.8.18** — PDF export 첫 H1/H2 title rule 출력 안정화, 첫 페이지 헤더-제목 사이 옷은 구분선 추가

이전 버전의 세부 변경은 [CHANGELOG.md](CHANGELOG.md)에만 유지해 README를 짧게 관리합니다.

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
