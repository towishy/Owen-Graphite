# Owen Graphite — Obsidian Theme

<!-- markdownlint-disable MD022 MD032 MD033 MD040 MD060 -->

Owen WIKI, Owen Graphite, Owen Editor는 LLM 기반 지식 정리부터 Obsidian 보고서 작성, Markdown 편집 UI까지 이어지는 Owen의 지식 작업 스택입니다.

![Owen Markdown 지식 작업 스택](screenshots/readme/owen-knowledge-work-stack.svg?v=2.22.37)

![Owen AI 문서 제작 병합 모델](screenshots/readme/owen-ai-document-stack.svg)

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/towishy/Owen-Graphite?style=flat-square)](https://github.com/towishy/Owen-Graphite/releases/latest)
[![GitHub License](https://img.shields.io/github/license/towishy/Owen-Graphite?style=flat-square)](LICENSE)
[![Obsidian Downloads](https://img.shields.io/badge/Obsidian-Compatible-7c3aed?style=flat-square&logo=obsidian)](https://obsidian.md)
[![Style Settings](https://img.shields.io/badge/Style%20Settings-38%20options-0d9488?style=flat-square)](#2-테마-기능-요약)

---

## 1. 테마 소개

**Owen Graphite**는 그래파이트(graphite) 톤의 라이트/다크 Obsidian 테마입니다. 한국어 보고서·기술 문서·위키 작성에 최적화되어 있으며, A3 인쇄 친화 레이아웃과 Live Preview ↔ Reading View 시각 동기화를 핵심 가치로 삼습니다.

| 분야 | 내용 |
|------|------|
| **타깃** | 보고서·기술 문서·위키 작성자 (특히 한국어) |
| **버전** | `2.22.131` |
| **기본 릴리즈** | `v2.22.131` |
| **롤백 베이스라인** | `v2.22.131` |
| **모드 지원** | ✅ Light / Dark / Report — 모든 위젯 패리티 보장 |
| **플랫폼** | ✅ Desktop & Mobile |
| **디자인 정책** | Glass+Shadow 코어 · 샘플-우선 워크플로우 |

![Owen Graphite Liquid Glass Overview](screenshots/readme/v2.22.31-liquid-glass-overview.svg)

<details>
<summary>📷 Light / Dark / Report 모드 스크린샷</summary>

![Light Mode](screenshots/light.png)
![Dark Mode](screenshots/dark.png)
![Report Mode (auto-numbering + serif body + cover page)](screenshots/report.png)

</details>

---

## 2. 테마 기능 요약

| 분류 | 주요 기능 | 요약 |
|------|----------|------|
| **디자인 코어** | Graphite 톤 · Liquid-glass chrome | 차분한 graphite 기반에 ribbon·사이드바·탭·툴바·command palette·tooltip glass surface 적용 |
| **상태 표현** | Frosted Ledger tables · Report Notice callouts | 기본 Markdown 표와 callout을 선명한 문서형 스타일로 정리하고 focus 상태는 aqua rim + soft halo로 표시 |
| **워크스페이스** | Workspace Surfaces Pack · Polish Pack | Graph view·Canvas·Folder cues·Mini TOC·Cover page·Dark parity·Mobile·Tab·Search HL 정리 |
| **보고서·인쇄** | A3 PDF Export · 자동 넘버링 | A3 가로/15mm 여백, 첫 페이지 헤더, H1 페이지 분할 |
| **분할 안정성** | 자동 분할 회피 | callout·표·Mermaid·코드·이미지가 PDF에서 중간 분할되지 않도록 보정 |
| **커스터마이징** | Style Settings 38종 · 사용자 클래스 | 폰트·간격·컬러·보고서 모드·PDF Compact Report·PDF 링크 출력 토글과 `.ogd-blur`·`.ogd-cover`·테이블/callout 유틸리티 제공 |
| **접근성·환경** | 시선 보호 · OS 다크 모드 · CJK 보정 | 시선 보호 모드, OS 다크 모드 자동 추종, CJK +0.5px 자동 보정 지원 |
| **Style Settings 분류** | 타이포 · 표 · 보고서 · PDF · 컬러/모션 | Style Settings 플러그인에서 전체 옵션을 사이드바 UI로 조정 |

---

## 3. 테마 설치 방법

### 옵션 A — Obsidian 커뮤니티 마켓 (승인 후)

1. 설정 → **외관 → 테마 관리**
2. 검색: `Owen Graphite`
3. 설치 → 사용

### 옵션 B — ZIP 수동 설치

[Releases 페이지](https://github.com/towishy/Owen-Graphite/releases/latest)에서 **`Owen-Graphite-<version>.zip`** 을 다운로드해 압축 해제합니다.

> **⚠️ 주의** Release Assets에는 GitHub 자동 생성 `Source code (zip)`도 함께 표시됩니다. 반드시 `Owen-Graphite-<version>.zip` 을 받으세요.

| 플랫폼 | 테마 대상 경로 |
| --- | --- |
| Windows | `<YourVault>\.obsidian\themes\Owen Graphite\` |
| macOS / Linux | `<YourVault>/.obsidian/themes/Owen Graphite/` |

설치 후 Obsidian → 설정 → **외관 → 테마** → `Owen Graphite` 선택.

<details>
<summary>옵션 C — Git 수동 설치 / 업데이트</summary>

#### Git 수동 설치 / 업데이트

Obsidian vault의 `.obsidian/themes/Owen Graphite/` 경로에 클론합니다. **같은 명령을 다시 실행하면 자동으로 업데이트**됩니다. 이미 클론된 폴더는 `fetch → reset --hard origin/main → clean` 순서로 최신 릴리스 상태를 맞춥니다.

| 플랫폼 | Git 설치 | 설치 / 업데이트 명령 |
| --- | --- | --- |
| Windows | `winget install --id Git.Git -e --source winget` | PowerShell 스크립트 (아래) |
| macOS | `brew install git` | bash 스크립트 (아래) |
| Linux | `sudo apt install git` (또는 `dnf install git`) | macOS와 동일 |

#### Windows (PowerShell)

```powershell
$ErrorActionPreference = "Stop"
$Vault = "D:\Path\To\YourVault"    # vault 경로로 교체
$Repo = "https://github.com/towishy/Owen-Graphite.git"
$ThemesDir = Join-Path $Vault ".obsidian\themes"
$ThemeDir = Join-Path $ThemesDir "Owen Graphite"

New-Item -ItemType Directory -Force -Path $ThemesDir | Out-Null

if (Test-Path -LiteralPath (Join-Path $ThemeDir ".git")) {
  git -C "$ThemeDir" fetch --quiet origin main
  git -C "$ThemeDir" reset --quiet --hard origin/main
  git -C "$ThemeDir" clean -qfd
  Write-Host "OK: Owen Graphite updated."
} elseif (Test-Path -LiteralPath $ThemeDir) {
  $Backup = "${ThemeDir}.backup-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
  Move-Item -LiteralPath $ThemeDir -Destination $Backup
  git clone --quiet $Repo "$ThemeDir"
  Write-Host "OK: Owen Graphite reinstalled. Backup: $Backup"
} else {
  git clone --quiet $Repo "$ThemeDir"
  Write-Host "OK: Owen Graphite installed."
}
```

#### macOS / Linux (bash)

최신 버전의 macOS에서는 git이 기본 포함되어 있으며, 아래 스크립트는 **설치 / 업데이트 / 손상된 폴더 복구**를 모두 처리합니다.

```bash
set -e
VAULT="/path/to/YourVault"          # ← vault 경로로 교체
REPO="https://github.com/towishy/Owen-Graphite.git"
THEME_DIR="$VAULT/.obsidian/themes/Owen Graphite"

mkdir -p "$VAULT/.obsidian/themes"

if [ -d "$THEME_DIR/.git" ]; then
  # 이미 설치됨 → 최신화 (rebase 대신 hard reset 으로 충돌 회피)
  git -C "$THEME_DIR" fetch --quiet origin main
  git -C "$THEME_DIR" reset --quiet --hard origin/main
  git -C "$THEME_DIR" clean -qfd
  echo "OK: Owen Graphite updated to $(git -C "$THEME_DIR" describe --tags --abbrev=0 2>/dev/null || echo 'main HEAD')."
elif [ -e "$THEME_DIR" ]; then
  # 폴더는 있으나 git 저장소가 아님 (수동 ZIP 설치 등) → 백업 후 재클론
  BACKUP="$THEME_DIR.backup-$(date +%Y%m%d-%H%M%S)"
  echo "WARN: 기존 비-Git 폴더 발견 → $BACKUP 으로 백업 후 재설치"
  mv "$THEME_DIR" "$BACKUP"
  git clone --quiet "$REPO" "$THEME_DIR"
  echo "OK: Owen Graphite 재설치 완료 (이전 폴더는 $BACKUP 에 보관)."
else
  git clone --quiet "$REPO" "$THEME_DIR"
  echo "OK: Owen Graphite 설치 완료."
fi
```

**한 줄 버전** (이미 vault 경로에서 실행 중일 때):

```bash
THEME_DIR=".obsidian/themes/Owen Graphite"; REPO="https://github.com/towishy/Owen-Graphite.git"; mkdir -p "$(dirname "$THEME_DIR")"; if [ -d "$THEME_DIR/.git" ]; then git -C "$THEME_DIR" fetch -q origin main && git -C "$THEME_DIR" reset -q --hard origin/main && git -C "$THEME_DIR" clean -qfd; else if [ -e "$THEME_DIR" ]; then mv "$THEME_DIR" "$THEME_DIR.backup-$(date +%Y%m%d-%H%M%S)"; fi; git clone -q "$REPO" "$THEME_DIR"; fi && echo "OK"
```

> [Style Settings](https://github.com/mgmeyers/obsidian-style-settings) 플러그인을 함께 설치하면 38개 옵션을 사이드바 UI에서 토글하고, PDF Compact Report, PDF 링크 출력 방식, PDF Header/Footer 문구 및 색상도 입력창에서 바로 설정할 수 있습니다. Header/Footer 텍스트 기본값은 비워져 있으므로 필요한 문구만 직접 입력해 사용합니다.

</details>

---

## 4. 테마 신기능

### ✨ v2.22.41 — PDF 마지막 페이지 Footer

PDF export 마지막 페이지에 H3 헤더형 confidential footer를 추가했습니다. Style Settings에서 첫 페이지 Header와 마지막 페이지 Footer의 PDF 출력 여부, 라벨/제목/본문 문구, 각 색상 옵션을 조정할 수 있습니다.

![Style Settings PDF Header Footer 설정 화면](screenshots/readme/v2.22.41-style-settings-pdf-controls.svg)

### ✨ v2.22.31 — README Liquid Glass Overview

README 대표 이미지와 실제 테마 CSS를 같은 liquid glass 기준으로 맞추고, 표와 focus 상태의 최신 시각 기준을 정리했습니다.

![Owen Graphite Liquid Glass Overview](screenshots/readme/v2.22.31-liquid-glass-overview.svg)

| # | 항목 | 내용 |
|---|------|------|
| 1 | README 대표 이미지 | 실제 작업공간 chrome, 위키형 표, 보고서형 표, Frost Aqua focus를 한 장에 요약 |
| 2 | Table mode split | 위키형 표는 airy glass surface, 보고서형 표는 PDF 친화 contrast/rule 중심으로 분리 |
| 3 | Frost Aqua focus | ribbon, nav, tab, search/modal, settings focus를 aqua rim + soft halo로 통일 |
| 4 | QA guard | README SVG, liquid glass token map, table/focus smoke sample을 validator로 보호 |

---

## 5. Change Log

README에는 **최근 10개 릴리즈**만 간략히 요약합니다. 전체 변경 이력과 상세 검증 내역은 [CHANGELOG.md](CHANGELOG.md)에서 확인할 수 있습니다.

| 버전 | 핵심 변경 |
|------|----------|
| **v2.22.131** | H1-H4 recommended heading hierarchy: H1/H2는 neutral Liquid Glass surface와 aqua ledger rule을 사용하고, H3/H4는 짧은 graphite rule로 정리. PDF export는 blur/shadow 없이 print-safe rule 중심으로 평탄화하며 `ogd-no-h1-number`로 H1 number kicker를 끌 수 있음 |
| **v2.22.130** | Mermaid control MAP stabilization: Live Preview Mermaid 컨트롤에서 공용 `.clickable-icon` 구조 보정을 분리해 CSS MAP의 high/low finding을 0으로 낮추고, 버튼의 glass hover/focus 장식은 유지 |
| **v2.22.129** | Quiet table and callout outer shadows: Markdown table과 callout의 외곽 drop-shadow를 제거하고, 내부 텍스트·grid line·row fill·semantic color·inset shine은 유지해 표면을 더 차분하게 정리 |
| **v2.22.128** | PDF and table Liquid Glass parity: 기본 Markdown table은 Reading View/Live Preview에서 frosted surface, rim, header shine, 얕은 row tint를 공유하고, PDF export의 callout/table도 print-safe Liquid Glass tint와 semantic color를 유지하도록 보정 |
| **v2.22.127** | PDF table color parity: PDF export에서 table surface, rim line, caption을 low-alpha print-safe sRGB tint로 매핑해 화면과 더 가까운 투명하고 연한 표 인상을 유지하면서 callout semantic color는 보존 |
| **v2.22.126** | Native ordered-list counter restore: 이전 glass marker용 custom counter가 native list numbering과 `start` 처리에 간섭하지 않도록 ordered list counter를 브라우저/Obsidian 기본값으로 되돌리고, 하이라이트로 깨진 문단 fallback의 과한 들여쓰기를 제거 |
| **v2.22.125** | PDF checklist flattening: PDF Export에서 체크리스트가 회색 행/카드처럼 깨져 보이지 않도록 task-list surface와 row border를 print에서 평탄화하고 native checkbox flow를 복원 |
| **v2.22.124** | Highlighted list alignment guard: 리스트 항목 내부 하이라이트가 gutter/본문 정렬을 흔들지 않도록 `mark`/CM6 highlight span을 inline flow로 고정하고 PDF fallback도 같은 방향으로 보정 |
| **v2.22.123** | Native accent list markers: PDF에서 긴 inline code가 깨지지 않도록 custom chip/grid list marker를 끄고, `::marker` 색상·굵기 중심의 안정적인 A안으로 전환 |
| **v2.22.122** | List marker parity hotfix: Live Preview의 CodeMirror list marker span에도 glass marker를 직접 적용하고, PDF export의 page-break 구간에서 native marker 색으로 되돌아가는 현상을 줄이기 위해 print grid fallback을 추가 |
| **v2.22.121** | Liquid list marker redesign: ordered list는 glass number chip, unordered list는 pearl marker, task list는 상태별 compact glass checkbox로 정리. PDF export에서도 print-safe fallback을 적용해 Live Preview와 최대한 비슷한 리스트 인상을 유지 |
| **v2.22.120** | PDF table header 색감 추가 보정: Chromium print에서 header 배경이 Live Preview보다 진한 회청색으로 보이던 문제를 줄이기 위해 PDF fallback을 더 밝은 Frosted Ledger 표면/헤더/경계선 토큰으로 조정 |
| **v2.22.118** | Markdown table 기본 디자인을 승인된 A Frosted Ledger 방향으로 전환. Reading View, Live Preview CM6 table widget, PDF export가 같은 frosted surface/header/grid/hover 토큰을 공유하도록 보정 |
| **v2.22.117** | callout 내부 체크리스트 보정: 중첩 task-list 카드 프레임을 제거해 하단 잔여선과 checkbox 잘림을 줄이고, Live Preview callout task line에서 `- [ ]` 원문 marker가 과하게 드러나는 상태를 정리 |
| **v2.22.116** | callout 바로 뒤 Markdown 수평선이 PDF뿐 아니라 Reading View/Live Preview에서도 잔여 회색 라인처럼 보이던 문제 수정. 일반 `hr`는 유지하고, `.callout + hr` 및 Live Preview의 callout widget 직후 `.HyperMD-hr`만 숨김 |
| **v2.22.115** | PDF Compact Report에서 callout 바로 뒤 Markdown 수평선이 잔여 회색 라인처럼 보이던 문제 수정. 일반 `hr`는 유지하되 `.callout + hr`만 PDF에서 숨김 |
| **v2.22.114** | PDF export 세부 보정: 긴 코드블럭이 페이지에서 분할될 때 배경/토큰 색이 어긋나지 않도록 print code surface와 token palette를 고정하고 `box-decoration-break`를 적용. 중첩 code wrapper의 회색 림 제거 범위를 확대하고, PDF 테이블 글자 크기를 본문에 더 가깝게 상향 |
| **v2.22.113** | PDF export 추가 보정: `language-text`/`language-kusto` 코드블럭 라벨을 `TEXT`/`KUSTO`로 정리하고, PDF 테이블이 Live Preview의 report sheet 계열과 맞도록 gradient header, outer rim, cell border, row tone을 재조정. risk-table 마지막 열의 과한 per-cell rounded box도 print에서 평탄화 |
| **v2.22.112** | 코드블럭 디자인 cascade 보정: late overlay/print 규칙 때문에 `LANGUAGE-POWERSHELL` 같은 raw class label이 노출되고 회색 wrapper 띠가 생기던 문제를 마지막 CSS 레이어에서 수정. Reading View/PDF 모두 readable language label, Candidate C header/rim/gradient, 투명 wrapper 유지 |
| **v2.22.111** | PDF export 코드블럭이 화면용 Candidate C와 다른 Candidate D fallback으로 보이던 문제 수정. `@media print`에서도 frosted glass gradient, rim shadow, header divider, 코드 본문 padding을 C 스타일에 맞춰 적용하되 Chromium print가 `backdrop-filter`를 평탄화해도 gradient/rim으로 디자인 정체성이 유지되도록 보강 |

> 전체 릴리즈 노트와 상세 변경 내역 → [CHANGELOG.md](CHANGELOG.md)

---

## 6. 기타

### 🤝 기여
- 이슈: [GitHub Issues](https://github.com/towishy/Owen-Graphite/issues)
- 토론: [Discussions](https://github.com/towishy/Owen-Graphite/discussions)
- 기여 가이드: [CONTRIBUTING.md](CONTRIBUTING.md)
- 개발 모듈 워크플로우: [dev/README.md](dev/README.md)

### 📁 파일 구조

```
Owen Graphite/
├── theme.css         # 테마 본체 (~10,600줄)
├── manifest.json     # Obsidian 테마 메타데이터
├── README.md         # 본 문서
├── CHANGELOG.md      # 전체 릴리즈 노트
├── CONTRIBUTING.md   # 기여 가이드
├── LICENSE           # MIT
├── dev/test-samples/ # 개발/검증용 샘플 문서
├── docs/             # 디자인 기준, QA, 토큰 매핑 문서
├── dev/MAP/          # dev CSS 기준 theme.css risk map 산출물
├── dev/temp/         # 임시 요청 산출물 보관소 (내용물은 커밋 제외)
├── screenshots/      # README/마켓 이미지
└── scripts/          # Python 검증/릴리즈 스크립트
```

### 🅰️ 권장 폰트
- **Pretendard** / **Noto Sans KR** — 본문 (sans)
- **Noto Serif KR** / **나눔명조** — 보고서 모드 (serif)
- **JetBrains Mono** / **D2Coding** — 코드 (mono)

### 📜 라이선스
[MIT License](LICENSE) © 2026 Owen ([@towishy](https://github.com/towishy))

### 🙏 크레딧
- 글꼴: Pretendard (Kil Hyung-jin), Noto Sans/Serif KR (Google), JetBrains Mono (JetBrains), D2Coding (Naver)
- 영감: Obsidian Minimal, Things, AnuPpuccin
- 빌드: Obsidian 1.6.x / macOS · Windows · Linux
