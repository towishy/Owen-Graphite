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
| **차별점** | A3 인쇄 + 헤더 자동 넘벍링 + 표지 + **PDF 첫 페이지 모던 헤더 (Side Bar + Two-line)** + **데스크톱 Liquid-glass chrome presets** + **Workspace Surfaces (Graph view·Canvas·Folder cues·Mini TOC·Cover page)** + **Polish Pack (callout stripe·code label·dark parity)** + Style Settings 27종 + Live Preview/Reading parity |
| **Light & Dark** | ✅ 양쪽 모두 모든 위젯 패리티 보장 |
| **모바일** | ✅ Desktop & Mobile |
| **버전** | `2.0.5` (Obsidian 1.6.0+) |

---

## 📦 설치

### 옵션 A — Obsidian 커뮤니티 마켓 (승인 후)

1. 설정 → **외관 → 테마 관리**
2. 검색: `Owen Graphite`
3. 설치 → 사용

### 옵션 B — Git으로 수동 설치 / 업데이트

Obsidian vault 안의 `.obsidian/themes/Owen Graphite/` 폴더에 테마 저장소를 설치합니다. Git으로 설치하면 이후 같은 명령으로 빠르게 업데이트할 수 있습니다.

Git이 없다면 먼저 설치하세요.

| 플랫폼 | Git 설치 명령 |
|------|------|
| Windows | `winget install --id Git.Git -e --source winget` |
| macOS | `brew install git` |
| Ubuntu / Debian | `sudo apt update && sudo apt install git` |
| Fedora | `sudo dnf install git` |

#### Windows

PowerShell에서 vault 루트 경로를 기준으로 실행합니다. 아래 명령은 테마를 반드시 `.obsidian\themes\Owen Graphite` 아래에 설치하며, 이미 Git으로 설치된 경우에는 새로 clone하지 않고 업데이트합니다.

```powershell
$ErrorActionPreference = "Stop"

cd "D:\Path\To\YourVault"
New-Item -ItemType Directory -Force ".obsidian\themes" | Out-Null
$ThemeDir = ".obsidian\themes\Owen Graphite"
$Repo = "https://github.com/towishy/Owen-Graphite.git"

function Invoke-GitQuiet {
    param([string[]]$GitArgs)
    & git @GitArgs *> $null
    if ($LASTEXITCODE -ne 0) { throw "git command failed" }
}

try {
    if (Test-Path "$ThemeDir\.git") {
        Invoke-GitQuiet @("-C", $ThemeDir, "fetch", "--quiet", "origin", "main")
        Invoke-GitQuiet @("-C", $ThemeDir, "reset", "--quiet", "--hard", "origin/main")
    } elseif (Test-Path $ThemeDir) {
        throw "Owen Graphite folder already exists but is not a Git clone."
    } else {
        Invoke-GitQuiet @("clone", "--quiet", $Repo, $ThemeDir)
    }
    Write-Host "OK: Owen Graphite installed or updated."
} catch {
    Write-Host "FAILED: Owen Graphite was not installed or updated. Check Git, network, vault path, or an existing non-Git theme folder."
    exit 1
}
```

#### macOS / Linux

터미널에서 vault 루트 경로를 기준으로 실행합니다. 이미 Git으로 설치된 경우에는 새로 clone하지 않고 업데이트합니다.

```bash
set -e
trap 'echo "FAILED: Owen Graphite was not installed or updated. Check Git, network, vault path, or an existing non-Git theme folder."' ERR

cd "/path/to/YourVault"
mkdir -p ".obsidian/themes"
THEME_DIR=".obsidian/themes/Owen Graphite"
REPO="https://github.com/towishy/Owen-Graphite.git"

if [ -d "$THEME_DIR/.git" ]; then
    git -C "$THEME_DIR" fetch --quiet origin main >/dev/null 2>&1
    git -C "$THEME_DIR" reset --quiet --hard origin/main >/dev/null 2>&1
elif [ -e "$THEME_DIR" ]; then
    false
else
    git clone --quiet "$REPO" "$THEME_DIR" >/dev/null 2>&1
fi

trap - ERR
echo "OK: Owen Graphite installed or updated."
```

### 옵션 C — ZIP으로 수동 설치

[Releases 페이지](https://github.com/towishy/Owen-Graphite/releases/latest)에서 `Owen-Graphite-<version>.zip`을 다운로드한 뒤 압축을 해제합니다. ZIP 안의 최상위 폴더 이름은 반드시 `Owen Graphite`여야 합니다. 압축 해제 도구가 다른 이름의 폴더를 만들었다면 폴더명을 `Owen Graphite`로 바꾼 뒤 플랫폼별 테마 대상 경로에 배치합니다.

> **⚠️ ZIP 파일 선택 주의**
> Release Assets 목록에는 GitHub가 자동 생성하는 `Source code (zip)`과 테마 배포용 `Owen-Graphite-<version>.zip`이 함께 표시됩니다.
> **반드시 `Owen-Graphite-<version>.zip`을 다운로드하세요.** `Source code (zip)`은 빌드 전 소스 코드이므로 테마로 사용할 수 없습니다.
>
> ![ZIP 다운로드 안내 — Assets에서 Owen-Graphite-x.x.x.zip 선택](screenshots/readme/zip-download-guide.svg)

| 플랫폼 | 테마 대상 경로 |
|------|------|
| Windows | `<YourVault>\.obsidian\themes\Owen Graphite\` |
| macOS / Linux | `<YourVault>/.obsidian/themes/Owen Graphite/` |

이미 같은 이름의 폴더가 있다면 Obsidian을 종료한 뒤 기존 `Owen Graphite` 폴더를 교체하거나, 백업 이름으로 바꾼 다음 새 폴더를 배치하세요.

> **v1.8.64+ 업데이트:** 기존 별도 CSS snippet (`zz-obsidian-gray-force-override-v2.css`) 기능은 모두 본 테마에 흡수되어 빌트인으로 제공됩니다. 더 이상 별도 snippet 설치는 필요하지 않습니다.

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

#### Style Settings 구획 (한글 / English)

| 한글 구획 | English section | 주요 옵션 |
|----------|-----------------|-----------|
| 읽기와 본문 | Reading & Body | font size, line height, max width, accent |
| 표와 코드 | Tables & Code | zebra, modern table style, PDF block-break guard |
| 보고서와 PDF | Report & PDF | report mode, serif body, indent, auto numbering, drop cap, spacing preset, page size |
| 워크스페이스와 접근성 | Workspace & A11y | accent preset, code block theme, sepia, OS dark, glass intensity, CJK font tune |
| PDF 첫 페이지 헤더 | PDF Cover Header | left/right body & sidebar color, label color |

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

## 🧩 Gray Report Tone — 빌트인 (v1.8.64+)

과거 별도 CSS snippet (`zz-obsidian-gray-force-override-v2.css`)으로 제공하던 **엄격한 회색 보고서 톤** 기능은 v1.8.64부터 테마에 완전 흡수되어 별도 설치 없이 기본 동작합니다.

### 흡수된 주요 기능

| 영역 | 내용 |
|------|------|
| Graphite-first | 헤더, blockquote, callout, 코드 색상을 회색 중심으로 고정 |
| 보고서 구조 | H1/H2/H3, TOC, 캡션, diagram frame, footnote, task list 통일 톤 |
| 표/PDF 안정성 | 비교표·매트릭스·고객 보고서 표가 화면과 PDF에서 균일하게 보이도록 보강 |
| 링크 구분 | 외부 URL은 Muted Gray 점선 밑줄로 내부 링크와 분리 |
| Live Preview 안전성 | Reading View 장식을 CM6 편집 라인에 과도하게 강제하지 않음 |

> 과거에 snippet을 설치하셨던 사용자는 `<YourVault>/.obsidian/snippets/zz-obsidian-gray-force-override-v2.css`를 제거하고 Obsidian 설정 → 외관 → CSS snippets에서 비활성화하세요. 동일한 효과가 테마에서 자동 적용됩니다.

---

## 🖥️ Workspace Surfaces Pack — 빌트인 (v2.0.0+)

v2.0.0부터 노트 본문 외 **워크스페이스 상의 주요 면**(Graph view, Canvas, File explorer, 출력물)을 통일된 디자인 언어로 정리합니다.

| 영역 | 상세 |
|------|------|
| **Graph view** | 노드 레이블 폰트 통일, hover 시 accent stroke, 원형 그룹 컬러 input pill |
| **Canvas** | 카드 다층 shadow, focus 외곽선, color group 6개 변수화, edge hover 강조 |
| **File explorer 폴더 컬러 큐** | `raw/` `wiki/` `outputs/` `reports/` `presentations/` `Clippings/` `Attachments/` `Templates/` `archive/` `drafts/` 10개 패턴에 3px 좌측 틴트 |
| **Reading view mini TOC** | `.ogd-mini-toc` 클래스 적용 시 우측 sticky TOC, 모바일에서 자동 인라인화, 프린트에서 숨김 |
| **Print 표지 페이지** | YAML에 `cssclasses: [cover-page]` 또는 `<div class="cover-page">` 래핑 시 세로 중앙 정렬 표지 + 자동 페이지 분할, `.cover-meta` `.cover-rule` 하위 스타일 제공 |

> 모든 기능은 **opt-in** 또는 **경로 자동 감지** 방식으로 동작하며, 기존 노트·테마 동작에 영향을 주지 않습니다.

---

## 🎛️ Polish Pack — 빌트인 (v1.8.66+)

v1.8.66부터 일상 사용 경험을 고르게 다듬은 **Polish Pack**이 기본 포함됩니다.

| 영역 | 상세 |
|------|------|
| **Dark Mode parity** | blockquote 3단계 톤, H1 kicker, inline code, search highlight가 다크 모드에서도 동등한 읽힌성 유지 |
| **Mobile (≤768px)** | H1 축소, callout/아이콘 재배치, 탭 햄들 폰트 축소로 모바일·태블릿 애플 대응 |
| **Tab 대비** | 활성 탭 상단 2px accent + bold, 비활성 탭 opacity 0.78 → hover시 1.0 |
| **Callout 컬러바** | 13개 타입별 좌측 4px 컬러 스트라이프 (note/info/tip/success/warning/danger/example/quote/abstract/todo/question/bug 등) |
| **코드 언어 라벨** | 코드블록 우상단 12개 언어 표시 (TS/JS/PY/SH/CSS/HTML/JSON/YAML/MD/RS/GO/SQL) |
| **Inline code** | 연한 회색 배경 + 레드 텍스트로 본문과 명확한 구분 |
| **방문 링크** | 외부 링크가 방문 후 보라색으로 전환되어 수신 이력 파악 용이 |
| **헤딩 앵커** | H2/H3/H4 hover 시 좌측에 `#` 앵커 표시 (PDF 출력시는 숨김) |
| **Status bar** | 모노스페이스 11px 통일로 글자수·라인수 가독성 향상 |
| **Search 강조** | 검색 매치 amber 배경 + 외곽선으로 명확한 식별 |
| **Frontmatter** | YAML·Properties 패널 모노스페이스 + 연한 명도 차등화 |

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
| `.ogd-cover` | h1 | 표지 페이지 강제 || `.cover-page` | YAML cssclasses 또는 div wrapper | **(v2.0.0+)** 세로로 중앙 정렬된 레포트 표지 + 자동 페이지 분할 |
| `.cover-meta` | div inside `.cover-page` | **(v2.0.0+)** 표지 하단 메타(날짜/버전) 모노스페이스 |
| `.cover-rule` | div inside `.cover-page` | **(v2.0.0+)** 제목 아래 80×3px accent 룰 |
| `.ogd-mini-toc` | YAML cssclasses 또는 div wrapper | **(v2.0.0+)** Reading view 우측 sticky mini TOC, 모바일 자동 인라인 || `sticky-first-col` | `<table>` | 첫 컬럼 sticky scroll |
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
├── theme.css                # 테마 본체 (~9,900줄, snippet 흠수)
├── manifest.json            # Obsidian 테마 메타데이터
├── README.md                # 빠른 사용법과 설정 요약
├── CHANGELOG.md             # 전체 릴리즈 노트
├── CONTRIBUTING.md          # (v1.9.0+) 외부 기여 가이드
├── LICENSE                  # MIT
├── .github/workflows/       # validate / release CI
├── docs/fixtures/           # 검증·디자인 preview fixture
├── screenshots/             # README/마켓플레이스 이미지
├── scripts/                 # 로컬 검증 스크립트 (Python)
└── src/                     # (v2.0.0+) 장기 모듈화 로드맵 문서
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

생성물은 `dist/Owen-Graphite-<version>.zip`에 저장되며, 수동 설치용 필수 파일을 `Owen Graphite/` 폴더 구조로 묶습니다.

---

## 📝 변경 이력

전체 이력은 [CHANGELOG.md](CHANGELOG.md) 참고.
- **v2.0.0** — Workspace Surfaces Pack: Graph view·Canvas 스타일, File explorer 폴더 컬러 큐(10개 패턴), Reading view mini TOC, Print 표지 페이지 유틸리티. 파괴적 변경 없음.
- **v1.9.0** — Maintainability Pass: CONTRIBUTING.md 신규, theme.css BOF Section Index, CI brace balance 검사. 디자인 변경 없음.
- **v1.8.66** — Polish Pack: Dark Mode parity, Mobile 반응형, Tab 대비, Callout 컬러바, 코드 언어 라벨, Inline code 톤, Heading anchor, Status bar mono, Search HL, Frontmatter.
- **v1.8.65** — Windows Live Preview `>` 마커 그리프 이슈 수정, 모노스페이스 폰트 폴백 강화, PDF thead 반복 출력 및 줄간격 미세조정.- **v1.8.64** — H1 스타일을 편집 장세·챕터 번호 키커 (Sample B)로 재디자인, blockquote는 세로바 대신 연한 배경+이탈릭으로 시각화, 인라인 제목 기본 비활성화, 별도 CSS snippet을 테마에 완전 흡수
- **v1.8.62** — Windows/macOS/Linux Git 설치 명령에서 Git 출력 잡음을 숨기고 성공 시 OK 메시지만 표시하도록 정리
- **v1.8.61** — Windows 신규 설치의 Reading View/Live Preview readable 컬럼 중앙 배치 회귀를 더 넓은 Obsidian DOM 선택자로 보강
- **v1.8.60** — Windows 신규 설치에서 readable 본문 컬럼 앞에 큰 공백이 생기던 정렬 회귀 수정, 설치 예시 경로와 ZIP 폴더명 안내 정리
- **v1.8.59** — 신규 Obsidian 설치에서 Live Preview 본문 영역이 내용 폭으로 수축해 빈 영역 클릭이 먹지 않던 회귀 수정, Windows/macOS/Linux Git 설치·업데이트 및 ZIP 수동 설치 안내 정리
- **v1.8.58** — 신규 Obsidian 설치에서 Reading View 문단이 한 글자 폭으로 접히는 회귀 수정, Windows 수동 설치 명령을 `.obsidian\themes` 경로 기준으로 정리
- **v1.8.57** — 수동 설치 + 스니핏 미적용 환경의 Live Preview 본문 폭 수축 가능성을 1차 보강
- **v1.8.56** — 검색 focus, command palette/list popup, tooltip/popover, empty state, focus-visible 상태를 Graphite 톤으로 정리
- **v1.8.55** — 작성 화면 노이즈를 줄이도록 lead 문단, 상태 badge, 구분선, 사이드바 위계, 링크 문법, H2-표 간격을 정리
- **v1.8.54** — 실제 Obsidian 적용 화면 기준으로 표, 편집 spellcheck 밑줄, 제목 rhythm, 선택 파일 상태를 정리
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

이슈, 기능 제안, PR을 환영합니다. 외부 기여자는 [CONTRIBUTING.md](CONTRIBUTING.md)의 개발 환경·검증·릴리즈 절차를 먼저 확인해 주세요.

- 이슈: [GitHub Issues](https://github.com/towishy/Owen-Graphite/issues)
- 토론: [Discussions](https://github.com/towishy/Owen-Graphite/discussions)
- 기여 가이드: [CONTRIBUTING.md](CONTRIBUTING.md)
- 모듈화 로드맵: [src/README.md](src/README.md)

---

## 📜 라이선스

[MIT License](LICENSE) © 2026 Owen ([@towishy](https://github.com/towishy))

---

## 🙏 크레딧

- 글꼴: Pretendard (Kil Hyung-jin), Noto Sans/Serif KR (Google), JetBrains Mono (JetBrains), D2Coding (Naver)
- 영감: Obsidian Minimal, Things, AnuPpuccin
- 빌드 환경: Obsidian 1.6.x / macOS · Windows · Linux
