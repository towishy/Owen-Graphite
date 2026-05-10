# Owen Graphite — Obsidian Theme

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
| **버전** | `2.22.120` |
| **기본 릴리즈** | `v2.22.120` |
| **롤백 베이스라인** | `v2.22.120` |
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

README에는 **v2.22.20 이상** 주요 변경만 간략히 요약합니다. 전체 이력은 [CHANGELOG.md](CHANGELOG.md)에서 확인할 수 있습니다.

| 버전 | 핵심 변경 |
|------|----------|
| **v2.22.120** | PDF table header 색감 추가 보정: Chromium print에서 header 배경이 Live Preview보다 진한 회청색으로 보이던 문제를 줄이기 위해 PDF fallback을 더 밝은 Frosted Ledger 표면/헤더/경계선 토큰으로 조정 |
| **v2.22.119** | PDF table parity 보정: A Frosted Ledger 적용 후 PDF 표 글자가 Live Preview보다 작고 진하게 보이던 문제를 수정. PDF table font/padding/line-height와 header/body slate 색상, frosted tint를 Live Preview 기준으로 재조정 |
| **v2.22.118** | Markdown table 기본 디자인을 승인된 A Frosted Ledger 방향으로 전환. Reading View, Live Preview CM6 table widget, PDF export가 같은 frosted surface/header/grid/hover 토큰을 공유하도록 보정 |
| **v2.22.117** | callout 내부 체크리스트 보정: 중첩 task-list 카드 프레임을 제거해 하단 잔여선과 checkbox 잘림을 줄이고, Live Preview callout task line에서 `- [ ]` 원문 marker가 과하게 드러나는 상태를 정리 |
| **v2.22.116** | callout 바로 뒤 Markdown 수평선이 PDF뿐 아니라 Reading View/Live Preview에서도 잔여 회색 라인처럼 보이던 문제 수정. 일반 `hr`는 유지하고, `.callout + hr` 및 Live Preview의 callout widget 직후 `.HyperMD-hr`만 숨김 |
| **v2.22.115** | PDF Compact Report에서 callout 바로 뒤 Markdown 수평선이 잔여 회색 라인처럼 보이던 문제 수정. 일반 `hr`는 유지하되 `.callout + hr`만 PDF에서 숨김 |
| **v2.22.114** | PDF export 세부 보정: 긴 코드블럭이 페이지에서 분할될 때 배경/토큰 색이 어긋나지 않도록 print code surface와 token palette를 고정하고 `box-decoration-break`를 적용. 중첩 code wrapper의 회색 림 제거 범위를 확대하고, PDF 테이블 글자 크기를 본문에 더 가깝게 상향 |
| **v2.22.113** | PDF export 추가 보정: `language-text`/`language-kusto` 코드블럭 라벨을 `TEXT`/`KUSTO`로 정리하고, PDF 테이블이 Live Preview의 report sheet 계열과 맞도록 gradient header, outer rim, cell border, row tone을 재조정. risk-table 마지막 열의 과한 per-cell rounded box도 print에서 평탄화 |
| **v2.22.112** | 코드블럭 디자인 cascade 보정: late overlay/print 규칙 때문에 `LANGUAGE-POWERSHELL` 같은 raw class label이 노출되고 회색 wrapper 띠가 생기던 문제를 마지막 CSS 레이어에서 수정. Reading View/PDF 모두 readable language label, Candidate C header/rim/gradient, 투명 wrapper 유지 |
| **v2.22.111** | PDF export 코드블럭이 화면용 Candidate C와 다른 Candidate D fallback으로 보이던 문제 수정. `@media print`에서도 frosted glass gradient, rim shadow, header divider, 코드 본문 padding을 C 스타일에 맞춰 적용하되 Chromium print가 `backdrop-filter`를 평탄화해도 gradient/rim으로 디자인 정체성이 유지되도록 보강 |
| **v2.22.110** | 코드블럭 디자인을 승인된 Candidate C(Frosted Glass + Rim)로 갱신: Reading View fenced code block에 glass surface/rim/header row/copy button/token 색상 적용, print/PDF는 Candidate D 기반의 조용한 outline fallback 적용. `.HyperMD-codeblock*`도 hit-routing 가드에 추가하고 기존 Live Preview codeblock begin/end 수직 margin/padding 제거 |
| **v2.22.109** | 회귀 방지 인프라 전면 구축: `live_preview_hit_routing_audit`에 active-line/embed BFC/pointer-events 카테고리 추가, `scripts/diff_guard.py` + `scripts/hooks/pre-commit` (패치 단위 감사), `scripts/build_selector_provenance.py` + `scripts/who_added.py` (셀렉터 도입 이력), `scripts/changelog_lint.py` (버전/셀렉터 토큰 강제), `dev/MAP/cm6-hit-routing-contract.md` 원칙 문서, `dev/test-samples/click-to-edit-regression.md` 시나리오 샘플, `scripts/hit_routing_probe.py` stub. CSS 모듈 상단에 FORBIDDEN 고지 주석 추가 |
| **v2.22.108** | Live Preview hit-routing 재발 방지 가드 추가: `scripts/validate_theme.py`에 CM6 block widget(`.cm-callout`/`.cm-table-widget`/`.cm-embed-block.cm-callout`) 수직 margin과 HyperMD-* `.cm-line` 수직 margin/padding 감지 패턴 추가. 가드가 즉시 잡은 `ogd-spacing-relaxed` preset의 callout/table widget margin 및 HyperMD-callout cm-line 수직 padding 제거 |
| **v2.22.107** | Live Preview callout 위 단락 클릭 라우팅 수정: v2.22.83 Report Notice callout이 `.cm-callout` widget에 적용하던 `margin: 1em 0 1.15em` 제거. v2.22.106 표 widget과 동일한 hitbox bleeding 패턴 |
| **v2.22.106** | Live Preview 표 위 단락 클릭 잔존 문제 해결: `.cm-embed-block`의 `overflow-x:auto + max-width` BFC 강제 룰 제거, `.cm-table-widget`의 `margin: 0.4em 0` 제거. 표 위 hit-routing이 vanilla로 환원 |
| **v2.22.105** | Live Preview 표 위 단락 클릭 라우팅 root cause 수정: `.HyperMD-table-row`(표 source `.cm-line`)에 `margin: 0.4em 0` 적용하던 구문을 제거. 그 margin이 cm-line hitbox를 위로 확장해 위 단락 클릭을 가로채던 문제 해결 |
| **v2.22.104** | Live Preview active 라인 glass focus visual 제거. outline+shadow+background 페인트가 인접 라인 클릭 hit-testing을 가리던 문제 해결. table cell focus는 유지 |
| **v2.22.103** | Live Preview 빈 줄 강제 압축(0.45em) 제거. native CM6 line-height(약 1.5em)로 환원해 마우스 클릭 hit-target 확보. 화살표키는 되면서 마우스 클릭은 안 되던 증상 해결 |
| **v2.22.102** | Live Preview EOF pointer-events isolation block 제거. `.cm-line *` 강제 override가 active 라인의 list marker/widget hit 라우팅을 가로채고 다른 줄 선택을 막던 문제 해결. native CM6 동작으로 환원 |
| **v2.22.101** | Live Preview 헤더 클릭 라우팅 root cause 수정: heading `.cm-line`의 padding-top/bottom을 0으로 환원해 hitbox를 시각 텍스트와 일치시킴 (vanilla parity) |
| **v2.22.100** | 헤더 인접 빈 줄 hitbox를 0.45em로 통일해 헤더-빈줄-헤더 클릭 라우팅 침범을 줄이고, Live Preview EOF isolation을 native pointer 경로 단일 가드로 단순화 |
| **v2.22.99** | Live Preview v2.22.84~98 실험 체인을 물리 제거하고, 비활성 rendered span 클릭을 CM6 line box로 넘기는 native edit isolation 적용 |
| **v2.22.98** | v2.22.97 복구 블록이 실패 블록보다 앞에 삽입된 cascade 오류를 수정하고, Live Preview v2.22.76 row model 복구를 실제 EOF 최종 승자로 재적용 |
| **v2.22.97** | Live Preview 편집성 관계 맵을 추가하고 v2.22.84~96 실험층으로 오염된 빈 줄/헤더/포인터 이벤트 관계를 v2.22.76 row model로 최종 복원 |
| **v2.22.96** | Live Preview 헤더 `.cm-line`의 margin/padding 기반 spacing을 제거하고 CM6 native row hit-test를 복원해 인접 헤더·문단 선택/편집 불가 문제 보정 |
| **v2.22.95** | Live Preview CSS 맵을 추가하고 헤더 하단 spacing을 padding에서 margin으로 이동해 active heading hitbox가 아래 문단 선택·편집을 가로막는 문제 보정 |
| **v2.22.94** | Live Preview 텍스트 span click-through 실험을 마지막 cascade에서 제거하고 헤더 line box를 기본 크기로 복원해 헤더 아래 문단 편집 진입 문제 보정 |
| **v2.22.93** | Live Preview 렌더 span hit-test 정책을 정리해 일반 헤더/문단 텍스트 클릭은 CodeMirror 줄 컨테이너가 받고 링크·위젯만 직접 클릭 가능하도록 보정 |
| **v2.22.92** | Live Preview 헤더와 바로 아래 문단 사이의 안전 간격을 복원해 active heading hitbox가 다음 줄 선택·편집을 막는 현상 보정 |
| **v2.22.91** | Live Preview 헤더 인접 빈 줄의 hitbox를 접고 텍스트 span 선택 동작을 기본값으로 복원해 빈 줄 클릭 후 아래 헤더/문단 편집 불가 현상 보정 |
| **v2.22.90** | Live Preview 빈 줄 Aqua focus 박스를 고 specificity로 제거하고 heading/문단 렌더 span 클릭이 CodeMirror 편집 진입을 막지 않도록 보정 |
| **v2.22.89** | Rendered/Live Preview 텍스트 선택·클릭 경로를 기본 동작으로 되돌리고 heading 장식 pseudo-element가 선택을 가로채지 않도록 보정 |
| **v2.22.88** | Live Preview active-line Aqua 박스가 일반 heading/paragraph 선택·편집을 방해할 수 있어 active-line 장식을 제거하고 기본 hit-test를 복구 |
| **v2.22.87** | Live Preview의 렌더된 일반 문단/목록 span이 클릭을 가로채 편집 진입을 막는 문제를 보정 |
| **v2.22.86** | Live Preview에서 활성 heading 아래 문단이 클릭/편집되지 않는 hit-test 겹침 문제를 보정 |
| **v2.22.85** | PDF Export에서도 B. Report Notice callout이 유지되도록 print cascade의 예전 좌측 stripe 규칙을 덮음 |
| **v2.22.84** | Live Preview 빈 줄 active focus 박스와 마우스 선택 불안정성을 보정해 편집 화면 선택성을 복구 |
| **v2.22.83** | Live Preview 편집 DOM에도 B. Report Notice callout 스타일을 적용해 기존 문서 편집 화면의 좌측 stripe 잔상을 제거 |
| **v2.22.82** | 기본 callout을 승인된 B. Report Notice 디자인으로 변경해 전체 테두리, paper surface, 원형 아이콘 배지 중심으로 정리 |
| **v2.22.81** | 기본 Markdown table을 승인된 B. Report Sheet 디자인으로 변경해 헤더 대비와 grid 가시성을 강화 |
| **v2.22.80** | PDF 링크 출력 방식을 Inline URL / Clean Reading / Reference First로 분리하고 figure caption 인쇄 스타일을 추가 |
| **v2.22.79** | PDF Compact Report 토글을 추가해 제목·본문·callout·표·참고 문헌의 인쇄 간격을 압축하고 정보 밀도를 높임 |
| **v2.22.78** | PDF Export 첫 페이지에 YAML frontmatter/properties 원문이 출력되는 문제를 인쇄 전용으로 숨김 |
| **v2.22.77** | PDF Export 코드블럭의 과도한 회색 외곽 박스와 화면용 배지를 제거하고 인쇄용 여백·줄바꿈을 정리 |
| **v2.22.76** | Live Preview 편집 중인 라인·Markdown 표 셀 focus·긴 inline token wrapping을 조용한 Frost Aqua 상태로 보강 |
| **v2.22.75** | 메뉴·사이드 pane·검색 제안·상단 아이콘·탭을 단순한 컨테이너형 Liquid Glass로 정리하고, 기본 상태의 복잡한 외곽 효과를 줄임 |
| **v2.22.74** | PDF 페이지 경계 가이드 기능(`ogd-pdf-page-guides`, `ogd-pdf-width-preview`, `ogd-pdf-risk-hints`, `ogd-page-size`) 전면 제거 — Live Preview와 실제 PDF 페이지 나뉘의 구조적 불일치로 혼선만 주던 풌 정리 |
| **v2.22.55** | callout 박스·아이콘·제목 정렬 흔들림과 긴 inline code overflow 보정 |
| **v2.22.51** | PDF 마지막 페이지 footer 본문이 넓은 페이지 폭을 충분히 쓰지 못하던 문제 수정 |
| **v2.22.50** | 문서 본문 샘플 강화와 `ogd-spacing-relaxed` Live Preview 패리티 보강 |
| **v2.22.49** | PDF 마지막 페이지 footer 제목 색상이 설정값과 다르게 출력되던 문제 수정 |
| **v2.22.48** | Style Settings Pickr swatch가 같은 섹션의 마지막 색상으로 초기화되어 보이던 문제 수정 |
| **v2.22.47** | Style Settings color picker swatch가 회색으로 고정되어 보이던 문제 수정 |
| **v2.22.46** | PDF 마지막 페이지 footer 라벨 문구를 가로 유지하고 라벨 칸 세로 중앙 정렬 |
| **v2.22.45** | PDF 마지막 페이지 footer NOTICE 아래 가로 라인 제거 |
| **v2.22.44** | PDF 마지막 페이지 footer 라벨·제목·본문 색상 설정 초기화처럼 보이던 문제 수정 |
| **v2.22.43** | PDF 마지막 페이지 footer의 세로 notice bar 복원과 회색 배경 번짐 방지 유지 |
| **v2.22.42** | PDF 마지막 페이지 footer의 회색 배경 번짐 hotfix와 좌측 세로 accent 제거 |
| **v2.22.41** | PDF 마지막 페이지 H3 헤더형 confidential footer와 Style Settings 옵션 추가 |
| **v2.22.40** | Live Preview 표 헤더 인라인 편집 높이 팽창 hotfix |
| **v2.22.39** | Mermaid 진단용 control fixture의 DOM-only 상태 명확화 |
| **v2.22.38** | Mermaid Live Preview control DOM 표시 fix와 진단 샘플 추가 |
| **v2.22.37** | fixture 추적 정책, 릴리즈 guard, side pane QA matrix 보강 |
| **v2.22.36** | 사이드 pane glass parity와 회귀 fixture 보강 |
| **v2.22.35** | 백링크 설명 카드와 오른쪽 pane glass surface 정렬 |
| **v2.22.34** | 우상단 view header action 버튼 glass surface 정렬 |
| **v2.22.33** | toolbar/plugin token 정리와 community theme search fixture guard 추가 |
| **v2.22.32** | 커뮤니티 테마 탐색 검색창 focus 하이라이트 완화 |
| **v2.22.31** | README 대표 이미지, 표 모드 분리, Frost Aqua focus 정리 |
| **v2.22.30** | 탭 rim과 active file row focus hotfix |
| **v2.22.29** | core state matrix 기반 liquid glass 토큰 적용 |
| **v2.22.28** | CSS guard, QA, fixture 검증 체계 강화 |
| **v2.22.27** | Live Preview editable table 샘플 hotfix |
| **v2.22.26** | core glass sample 반영과 active/selected rim 정리 |
| **v2.22.25** | MAP info 축소 및 overlay/search/graph 안정화 |
| **v2.22.24** | ribbon/toggle/tab/focus/graph control 소유권 정리 |
| **v2.22.23** | file explorer hierarchy와 compatibility warning 정리 |
| **v2.22.22** | README knowledge work stack 이미지 교체 |
| **v2.22.21** | active path, ribbon/graph, backlink row liquid glass baseline |
| **v2.22.20** | 상태바, modal close, Dataview chip, sync/git pill polish |

> 전체 릴리즈 노트 → [CHANGELOG.md](CHANGELOG.md)

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
