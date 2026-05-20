# Owen Graphite — Obsidian Theme

<!-- markdownlint-disable MD022 MD032 MD033 MD040 -->

**Owen Graphite v3.1.48** — 한국어 기술 문서·보고서·위키 작성을 위한 Obsidian 테마. 17,000+ 줄 CSS를 src/ 폴더에 처음부터 다시 작성한 v3 코드베이스의 최신 안정 릴리즈입니다.

**English summary** — Owen Graphite is an Obsidian theme for technical documentation, knowledge bases, and report writing. It focuses on readable Korean and English notes, stable long tables and code blocks, polished workspace chrome, Live Preview / PDF export parity, and report-friendly layouts for recurring documentation work.

[![GitHub release](https://img.shields.io/github/v/release/towishy/Owen-Graphite?style=flat-square)](https://github.com/towishy/Owen-Graphite/releases/latest)
[![License](https://img.shields.io/github/license/towishy/Owen-Graphite?style=flat-square)](LICENSE)
[![Obsidian](https://img.shields.io/badge/Obsidian-Compatible-7c3aed?style=flat-square&logo=obsidian)](https://obsidian.md)
[![!important](https://img.shields.io/badge/!important-0-0d9488?style=flat-square)](docs/v3/cascade-research.md)

[English README](README.en.md) · [Style Settings presets](docs/v3/style-settings-presets.md) · [Compatibility matrix](docs/plugin-compatibility.md)

## Why Owen Graphite?

| 작업 흐름 | 바로 좋아지는 지점 |
| --- | --- |
| 긴 한글·영문 기술 문서 | CJK/Latin 혼합 문단, 제목, 코드, 표의 밀도와 리듬을 안정화 |
| Live Preview 중심 작성 | 편집 화면과 Reading View의 표·코드·callout 표면 차이를 줄임 |
| PDF 보고서 제출 | 첫 페이지 헤더, 마지막 페이지 푸터, 자동 넘버링, 페이지 분할 완화 지원 |
| 반복 작성 워크스페이스 | 탭, 탐색기, 검색, 설정, 팝오버를 조용한 liquid-glass 톤으로 정리 |

## Release Confidence

| Guard | Current status | Evidence |
| --- | --- | --- |
| Bundle freshness | `theme.css` must match `dist/theme-v3.css` | [release plan](docs/v3/release-plan.md) |
| Zero-important cascade | declaration-level `!important` policy is enforced | [cascade research](docs/v3/cascade-research.md) |
| Style Settings contract | option ids/defaults are audited against the contract | [contract](docs/v3/style-settings-contract.md) |
| Docs/assets links | local Markdown links and README images are audited | [contributing](CONTRIBUTING.md) |
| Live Preview/PDF parity | LP hit-routing, PDF header/footer, and visual fixture checks are scripted | [release plan](docs/v3/release-plan.md) |

## Visual Tour

| Surface | Preview |
| --- | --- |
| Light mode | ![Light Mode](screenshots/light.png) |
| Dark mode | ![Dark Mode](screenshots/dark.png) |
| Report mode | ![Report Mode](screenshots/report.png) |
| File explorer type badges | ![파일 탐색기 확장자 배지](screenshots/readme/file-explorer-type-badges.svg) |

비교 스크린샷을 새로 캡처할 때는 [visual comparison guide](docs/v3/visual-comparison-guide.md)를 기준으로 기본 Obsidian과 Owen Graphite를 같은 문서·같은 뷰포트에서 촬영합니다.

## English Overview

Owen Graphite is designed for people who write long-form notes, technical documents, knowledge-base pages, and printable reports in Obsidian. It keeps dense Markdown content readable, makes workspace chrome quieter, and preserves a consistent visual language across editing, reading, and PDF export.

### Features

| Area | What it improves |
| --- | --- |
| Korean and English notes | Balanced typography for CJK and Latin text, with stable spacing for long documents |
| Technical writing | Clear code blocks, long tables, callouts, embeds, and document-style layouts |
| Workspace navigation | Polished tabs, file explorer, search panels, sidebars, and type badges for common file formats |
| Report workflows | Report mode, print-friendly surfaces, PDF header options, and reduced page-break issues |
| Maintenance | Modular v3 CSS source, release audits, and zero-important cascade policy |

### Installation

1. Open Obsidian and go to `Settings` → `Appearance` → `Themes`.
2. Search for `Owen Graphite` in the community theme browser.
3. Install and enable the theme.
4. Optional: install the Style Settings plugin to adjust report mode, PDF header fields, and workspace polish options.

| 핵심 사용처 | 바로 얻는 효과 |
| --- | --- |
| 한국어 위키·기술 문서 | CJK 가독성, 긴 표·코드·callout 안정화 |
| A3/PDF 보고서 | 표지·자동 넘버링·페이지 분할 완화 |
| 반복 작성 워크스페이스 | 탭·사이드바·검색·설정 UI의 얕은 liquid-glass polish |

---

## 1. 테마 소개 / Theme Profile

| 항목 | 내용 |
| --- | --- |
| **버전** | `3.1.48` |
| **베이스라인 / 롤백 기준** | `v3.1.48` |
| **모드 지원** | ✅ Light / Dark / Report |
| **플랫폼** | ✅ Desktop & Mobile |
| **디자인 정책** | Liquid Glass core · 토큰 우선 · zero-important cascade |

<details>
<summary>📷 Light / Dark / Report 모드 스크린샷</summary>

![Light Mode](screenshots/light.png)
![Dark Mode](screenshots/dark.png)
![Report Mode (auto-numbering + serif body + cover page)](screenshots/report.png)

</details>

---

## 2. 신기능 소개 / Latest Highlights

> [ 정보 ]
> [Style Settings 플러그인](https://community.obsidian.md/plugins/obsidian-style-settings)을 설치하면, 신기능 관련 옵션과 설정을 진행할 수 있습니다.

Recent updates are listed here so English-speaking users and reviewers can quickly see what changed in the latest stable releases.

### v3.1.44 — 파일 탐색기 확장자 배지 / File Explorer Type Badges

파일 탐색기의 오른쪽 확장자 텍스트를 숨기고, 앞쪽 문서 아이콘 자리에 `MD`, `HTML`, `SVG`, `PDF`, `CFG` 같은 타입 배지를 표시합니다. 오른쪽 배지가 차지하던 폭을 파일명 표시 영역으로 돌려 긴 문서 제목이 더 늦게 말줄임되며, 문서·이미지·코드·설정·오피스·미디어·Obsidian 특화 파일을 한눈에 구분할 수 있습니다.

This update hides the right-side extension label and replaces the leading document icon with compact type badges such as `MD`, `HTML`, `SVG`, `PDF`, and `CFG`. The file name receives more horizontal space, so long document titles stay readable for longer in the file explorer.

![파일 탐색기 확장자 배지](screenshots/readme/file-explorer-type-badges.svg)

| 구분 | 개선 내용 |
| --- | --- |
| 제목 표시 | 파일 row가 사용 가능한 폭을 끝까지 쓰도록 조정 |
| 확장자 표시 | 오른쪽 `HTML` 같은 확장자 배지를 숨기고 앞쪽 타입 배지로 통합 |
| 대응 범위 | Markdown, HTML/SVG/PDF, 코드, 설정, 오피스, 이미지, 오디오/비디오, Obsidian canvas/excalidraw |
| 가독성 | 타입 배지와 파일명 사이 간격을 확보해 목록 스캔성을 개선 |

### v3.1.39 — PDF 헤더 Key/Value 2쌍 / Two PDF Header Key-Value Pairs

PDF 첫 페이지 헤더에 Key/Value 쌍을 두 개까지 출력할 수 있습니다. 1번과 2번 쌍은 설정 UI의 순서 그대로 `1번 Key → 1번 Value → 2번 Key → 2번 Value`로 배치되며, 네 segment의 높이를 같은 기준으로 맞췄습니다. 2번 key/value도 별도 색상 팔레트를 사용해 문서 작성자, 부서, 보안 등급, 검토 상태를 한 줄에서 구분할 수 있습니다.

![PDF 헤더 Key/Value 2쌍](screenshots/readme/pdf-dual-key-value-header.png)

| 설정 영역 | 개선 내용 |
| --- | --- |
| 라벨 구성 | `Key/Value 1쌍`과 `Key/Value 2쌍`을 직접 선택 |
| 헤더 1번 | Key/Value 문구와 색상 팔레트 유지 |
| 헤더 2번 | Key/Value 문구와 독립 색상 팔레트 추가 |
| PDF 안정성 | Obsidian export wrapper 구조와 무관하게 2쌍 출력 |

### v3.1.38 — 코드블럭 Live Preview / PDF 패리티 / Code Block Live Preview and PDF Parity

Live Preview, Reading View, PDF Export의 코드블럭 헤더·폰트·syntax 색상을 같은 토큰 기준으로 맞췄습니다. Obsidian Live Preview의 source line, rendered code widget, PDF export의 Prism `.token.*`/CodeMirror `.cm-*` 경로를 모두 검증 fixture에 포함해 앞으로 코드블럭 개선 시 누락되는 경로를 줄였습니다.

![코드블럭 Live Preview / PDF 패리티](screenshots/readme/code-font-clarity.png)

| 검증 영역 | 개선 내용 |
| --- | --- |
| Live Preview | 코드 fence 헤더를 한 줄 라벨로 정리하고 rendered widget 경로까지 동일한 codeblock surface 적용 |
| PDF Export | `.token.*`와 `.cm-*` syntax class를 같은 `--ogd-code-*` 색상·폰트 토큰으로 매핑 |
| 유지보수 | `dev/MAP/live-preview-pdf-css-map/`에 selector 매핑, cascade ownership, parity guideline 추가 |

이전 신기능 소개는 [docs/v3/feature-history.md](docs/v3/feature-history.md)에 보관합니다.

---

## 3. 테마 설치 / Installation Details

### 옵션 A — Obsidian 커뮤니티 마켓 (승인 후) / Community Theme Browser

1. 설정 → **외관 → 테마 관리**
2. 검색: `Owen Graphite`
3. 설치 → 사용

### 옵션 B — ZIP 수동 설치 / Manual ZIP Install

[Releases 페이지](https://github.com/towishy/Owen-Graphite/releases/latest)에서 **`Owen-Graphite-3.1.48.zip`** 을 받아 압축 해제합니다.

| 플랫폼 | 대상 경로 |
| --- | --- |
| Windows | `<YourVault>\.obsidian\themes\Owen Graphite\` |
| macOS / Linux | `<YourVault>/.obsidian/themes/Owen Graphite/` |

설치 후 Obsidian → 설정 → **외관 → 테마** → `Owen Graphite` 선택.

> ⚠️ Release Assets에는 GitHub 자동 생성 `Source code (zip)`도 함께 표시됩니다. 반드시 `Owen-Graphite-3.1.48.zip` 을 받으세요.

### 옵션 C — Git 수동 설치 / 업데이트 / Git Install or Update

`.obsidian/themes/Owen Graphite/` 경로에 클론합니다. **같은 명령을 다시 실행하면 자동 업데이트**됩니다.

#### Windows (PowerShell)

```powershell
$ErrorActionPreference = "Stop"
$Vault = "D:\Path\To\YourVault"            # vault 경로로 교체
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

```bash
set -e
VAULT="/path/to/YourVault"                  # vault 경로로 교체
REPO="https://github.com/towishy/Owen-Graphite.git"
THEME_DIR="$VAULT/.obsidian/themes/Owen Graphite"
mkdir -p "$VAULT/.obsidian/themes"

if [ -d "$THEME_DIR/.git" ]; then
  git -C "$THEME_DIR" fetch --quiet origin main
  git -C "$THEME_DIR" reset --quiet --hard origin/main
  git -C "$THEME_DIR" clean -qfd
  echo "OK: Owen Graphite updated."
elif [ -e "$THEME_DIR" ]; then
  BACKUP="$THEME_DIR.backup-$(date +%Y%m%d-%H%M%S)"
  mv "$THEME_DIR" "$BACKUP"
  git clone --quiet "$REPO" "$THEME_DIR"
  echo "OK: Owen Graphite reinstalled. Backup: $BACKUP"
else
  git clone --quiet "$REPO" "$THEME_DIR"
  echo "OK: Owen Graphite installed."
fi
```

---

## 4. 개발자 워크플로우

v3 소스는 `src/` 폴더에 토큰 → base → surfaces → chrome → features → themes → plugins → polish 순서로 분리되어 있습니다. 빌드/감사는 `dev/scripts/` 의 v3 도구만 사용합니다.

| 작업 | 명령 |
| --- | --- |
| 번들 빌드 | `python dev/scripts/bundle_v3.py` → `dist/theme-v3.css` |
| `theme.css` 갱신 | `Copy-Item dist/theme-v3.css theme.css -Force` (Windows) 또는 동등 명령 |
| Live Preview hit-routing 감사 | `python dev/scripts/audit_v3_hit_routing.py` |
| 중복 selector 감사(참고용) | `python dev/scripts/v3_audit_duplicate_selectors.py` |
| unused CSS 후보 리포트 | `python dev/scripts/build_unused_css_report.py` |
| computed-style fingerprint 캡처 | `python dev/scripts/capture_computed_fingerprint.py --build v3 --theme {light,dark}` |
| fingerprint diff | `python dev/scripts/fp_diff_summary.py [--theme dark]` |
| Release ZIP | `python dev/scripts/build_release.py` |
| Obsidian vault 동기화 | `python dev/scripts/sync_obsidian_theme.py` |

자세한 기여 가이드는 [CONTRIBUTING.md](CONTRIBUTING.md), 변경 이력은 [CHANGELOG.md](CHANGELOG.md), 보존·검증 계약은 [docs/v3/design-spec.md](docs/v3/design-spec.md) 참조.

---

## 5. 후원

<p align="center">
  <a href="https://github.com/sponsors/towishy">
    <img src="screenshots/readme/sponsor-coffee.svg" alt="커피 한 잔으로 Owen Graphite 응원하기" width="560">
  </a>
</p>

Owen Graphite는 무료/오픈소스입니다. 한국어 보고서·위키 작성 환경 유지에 도움이 되셨다면 [GitHub Sponsors](https://github.com/sponsors/towishy)에서 커피 한 잔으로 응원해 주세요.

---

## 6. 라이선스

MIT — [LICENSE](LICENSE)
