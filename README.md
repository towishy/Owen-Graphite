<!-- markdownlint-disable MD022 MD032 MD033 MD040 MD041 -->

[![GitHub release](https://img.shields.io/github/v/release/towishy/Owen-Graphite?style=flat-square)](https://github.com/towishy/Owen-Graphite/releases/latest)
[![License](https://img.shields.io/github/license/towishy/Owen-Graphite?style=flat-square)](LICENSE)
[![Obsidian](https://img.shields.io/badge/Obsidian-Compatible-7c3aed?style=flat-square&logo=obsidian)](https://obsidian.md)
[![!important](https://img.shields.io/badge/!important-0-0d9488?style=flat-square)](dev/WIKI/DOCS/v3/cascade-research.md)

[English README](README.en.md) · [Style Settings presets](dev/WIKI/DOCS/v3/style-settings-presets.md) · [Compatibility matrix](dev/WIKI/DOCS/v3/plugin-compatibility.md)

# Owen Graphite — Obsidian Theme

**Owen Graphite v3.1.64** — 한국어 기술 문서·보고서·위키 작성을 위한 Obsidian 테마. 17,000+ 줄 CSS를 src/ 폴더에 처음부터 다시 작성한 v3 코드베이스의 최신 안정 릴리즈입니다.

**English summary** — Owen Graphite is an Obsidian theme for technical documentation, knowledge bases, and report writing. It focuses on readable Korean and English notes, stable long tables and code blocks, polished workspace chrome, Live Preview / PDF export parity, and report-friendly layouts for recurring documentation work.

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
| Bundle freshness | `theme.css` must match `dist/theme-v3.css` | [release plan](dev/WIKI/DOCS/v3/release-plan.md) |
| Zero-important cascade | declaration-level `!important` policy is enforced | [cascade research](dev/WIKI/DOCS/v3/cascade-research.md) |
| Style Settings contract | option ids/defaults are audited against the contract | [contract](dev/WIKI/DOCS/v3/style-settings-contract.md) |
| Docs/assets links | local Markdown links and README images are audited | [contributing](CONTRIBUTING.md) |
| Live Preview/PDF parity | LP hit-routing, PDF header/footer, and visual fixture checks are scripted | [release plan](dev/WIKI/DOCS/v3/release-plan.md) |

## Visual Tour

| Surface | Preview |
| --- | --- |
| Light mode | ![Light Mode](screenshots/light.png) |
| Dark mode | ![Dark Mode](screenshots/dark.png) |
| Top tabs and floating toolbar | ![상단 탭과 플로팅 툴바](screenshots/readme/top-tabs-liquid-glass.svg) |
| Writing surface and floating toolbar | ![문서 작성 화면과 플로팅 툴바](screenshots/readme/workspace-writing-surface.jpg) |
| Style Settings report controls | ![Style Settings 보고서 옵션](screenshots/readme/style-settings-report-options.jpg) |
| PDF customer delivery visibility | ![PDF 고객 전달용 화면 가시성 설정](screenshots/readme/pdf-customer-delivery-feature.png) |
| Owen Editor toolbar controls | ![Owen Editor 툴바 설정](screenshots/readme/owen-editor-toolbar-settings.jpg) |
| File explorer type badges | ![파일 탐색기 확장자 배지](screenshots/readme/file-explorer-type-badges.svg) |

비교 스크린샷을 새로 캡처할 때는 [visual comparison guide](dev/WIKI/DOCS/v3/visual-comparison-guide.md)를 기준으로 기본 Obsidian과 Owen Graphite를 같은 문서·같은 뷰포트에서 촬영합니다.

## English Overview

Owen Graphite is designed for people who write long-form notes, technical documents, knowledge-base pages, and printable reports in Obsidian. It keeps dense Markdown content readable, makes workspace chrome quieter, and preserves a consistent visual language across editing, reading, and PDF export.

### Features

| Area | What it improves |
| --- | --- |
| Korean and English notes | Balanced typography for CJK and Latin text, with stable spacing for long documents |
| Technical writing | Clear code blocks, long tables, callouts, embeds, and document-style layouts |
| Workspace navigation | Polished tabs, file explorer, search panels, sidebars, and type badges for common file formats |
| PDF workflows | Print-friendly surfaces, PDF header options, and reduced page-break issues |
| Maintenance | Modular v3 CSS source, release audits, and zero-important cascade policy |

### Installation

1. Open Obsidian and go to `Settings` → `Appearance` → `Themes`.
2. Search for `Owen Graphite` in the community theme browser.
3. Install and enable the theme.
4. Optional: install the Style Settings plugin to adjust PDF header fields, typography, and workspace polish options.

| 핵심 사용처 | 바로 얻는 효과 |
| --- | --- |
| 한국어 위키·기술 문서 | CJK 가독성, 긴 표·코드·callout 안정화 |
| A3/PDF 보고서 | 표지·자동 넘버링·페이지 분할 완화 |
| 반복 작성 워크스페이스 | 탭·사이드바·검색·설정 UI의 얕은 liquid-glass polish |

---

## 1. 테마 소개 / Theme Profile

| 항목 | 내용 |
| --- | --- |
| **버전** | `3.1.64` |
| **베이스라인 / 롤백 기준** | `v3.1.64` |
| **모드 지원** | ✅ Light / Dark |
| **플랫폼** | ✅ Desktop & Mobile |
| **디자인 정책** | Liquid Glass core · 토큰 우선 · zero-important cascade |

<details>
<summary>📷 Light / Dark 모드 스크린샷</summary>

![Light Mode](screenshots/light.png)
![Dark Mode](screenshots/dark.png)

</details>

---

## 2. 신기능 소개 / Latest Highlights

> [ 정보 ]
> [Style Settings 플러그인](https://community.obsidian.md/plugins/obsidian-style-settings)을 설치하면, 신기능 관련 옵션과 설정을 진행할 수 있습니다.

Recent updates are listed here so English-speaking users and reviewers can quickly see what changed in the latest stable releases.

### v3.1.56 — Style Settings Import / Export Glass Polish

Style Settings의 `Import`, `Export`, `Copy to clipboard`, `Download`, `Import from file` 링크 문자열을 Owen Graphite의 설정 화면 톤에 맞는 작은 glass pill 버튼으로 정리했습니다. Export/Import 모달 안에서도 같은 버튼 언어를 적용해 링크 텍스트가 설정 화면에서 따로 떠 보이지 않도록 맞췄습니다.

This release polishes the Style Settings import/export links into compact glass pill controls, including the export and import modals, so plugin utility actions align with the rest of the Owen Graphite settings surface.

| 구분 | 개선 내용 |
| --- | --- |
| Style Settings | Import/Export 계열 링크를 glass pill 버튼 톤으로 정리 |
| Modal | Copy, Download, Import from file 액션도 같은 시각 언어로 통일 |
| CI | main Validate workflow에 Playwright/requirements 설치 단계를 추가해 release check 실행 환경을 맞춤 |
| 검증 | CSS budget, bundle freshness, release ZIP 검증 통과 |

### v3.1.55 — PDF 고객 전달용 화면 가시성 / Customer Delivery PDF Visibility

고객에게 PDF 파일로 전달하는 문서를 위해 `PDF 고객 전달용 화면 가시성` 옵션을 추가했습니다. 인쇄물보다 메일, Teams, 브라우저 미리보기에서 바로 읽히는 화면 PDF를 기준으로 제목 위계, 본문·표 크기, callout 역할 구분, 헤더/푸터 라벨 톤을 조정합니다.

This release adds a customer-delivery PDF visibility option for screen-first PDFs shared through mail, Teams, and browser previews. It strengthens heading hierarchy, body/table readability, callout role separation, and PDF label tone without replacing the existing print-stability presets.

![PDF 고객 전달용 화면 가시성 설정](screenshots/readme/pdf-customer-delivery-feature.png)

| 구분 | 개선 내용 |
| --- | --- |
| Style Settings | `PDF 고객 전달용 화면 가시성` 토글을 보고서와 PDF 그룹에 추가 |
| 화면 PDF | 고객이 확대 없이 읽기 쉽도록 본문·표·callout 크기와 대비를 조정 |
| 라벨 톤 | 작성자·검토자·상태 라벨은 유지하되 본문보다 낮은 보조 정보 위계로 정리 |
| 검증 | Style Settings contract, PDF header/footer contract, release build 검증 통과 |

### v3.1.54 — File Explorer Actions & Transparent Top Chrome

파일 탐색기 상단 5개 액션 버튼을 Owen Graphite 전용 아이콘과 liquid-glass 표면으로 맞추고, hover/focus 시 teal/cyan 림과 살짝 떠오르는 리프트를 추가했습니다. 문서 상단 root view header는 더 투명한 cyan-tint glass로 낮췄고, 활성 탭 뒤에 보이던 둥근 backline/connector 레이어를 숨겼습니다.

| 구분 | 개선 내용 |
| --- | --- |
| 파일 탐색기 액션 | 새 노트, 새 폴더, 정렬, compact, fold 계열 5개 버튼에 전용 마스크 아이콘 적용 |
| 상단 chrome | root view header의 흰 배경, 하이라이트, 그림자를 낮춰 더 투명한 glass 톤으로 조정 |
| 활성 탭 | 뒤쪽 rounded connector와 확산 그림자를 제거해 탭 뒤 라인이 드러나지 않도록 정리 |
| 검증 | release check, CSS budget, LP/PDF selector ownership, Live Preview hit-routing 검증 통과 |

### v3.1.53 — Live Preview Codeblock Header Editability

Live Preview 코드블럭 헤더의 `TEXT`, `SHELL` 같은 언어 라벨이 클릭 후에도 사라지지 않도록 정리했습니다. 헤더 오른쪽에는 향후 copy icon 같은 액션을 넣을 수 있는 슬롯 토큰을 예약했고, 언어 라벨은 해당 영역과 겹치지 않도록 폭을 제한했습니다.

| 구분 | 개선 내용 |
| --- | --- |
| 헤더 라벨 | `.code-block-flair` 표시를 복원해 기존 `TEXT`/`SHELL` 라벨 가시성 유지 |
| 편집성 | 클릭 라우팅을 막지 않도록 `pointer-events` 경로를 유지하고 실제 fence 토큰 active 표시 보강 |
| 액션 슬롯 | 오른쪽 액션 영역 토큰을 예약해 향후 copy icon 버튼과 라벨 충돌 방지 |
| 검증 | Live Preview hit-routing, LP/PDF selector ownership, CSS budget 검증 통과 |

### v3.1.52 — Workspace Chrome Connected Glass

상단 활성 탭, 하단 문서 프레임, vault switcher를 같은 sky-rim liquid glass 언어로 맞췄습니다. 활성 탭은 문서 표면과 이어지는 bridge를 갖고, 비활성 탭은 별도 pill처럼 분리되며, 하단 문서 제목과 `Owen-WIKI` vault switcher는 활성 파일 pill 계열의 frosted glass 표면으로 정리했습니다.

This release aligns the active workspace tab, bottom document frame, and vault switcher with one connected sky-rim liquid-glass language. Active tabs now read as attached to the document surface, while inactive tabs stay separated and quiet.

![Workspace Chrome Connected Glass](screenshots/readme/workspace-chrome-connected-glass.svg)

| 구분 | 개선 내용 |
| --- | --- |
| 활성 탭 | 문서 표면과 이어지는 bridge, 중앙 정렬 제목, 낮춘 top shadow로 attached tab 느낌 강화 |
| 비활성 탭 | 제목 중앙 정렬과 낮은 graphite edge로 활성 탭 뒤에 겹치지 않는 독립 pill 유지 |
| 하단 프레임 | 문서 제목·상태칩·외부 그림자를 같은 frosted glass 계층으로 정리 |
| Vault switcher | `Owen-WIKI` 박스를 활성 파일 pill 계열 sky rim glass로 통일 |

### v3.1.51 — 상단 탭 Liquid Glass / Top Tab Liquid Glass

상단 workspace tab을 첨부 화면 기준의 붙은 탭 형태로 다듬었습니다. 활성 탭은 위·좌·우 rim이 같은 sky 톤으로 이어지고, 비활성 탭은 분리선 대신 보일듯 말듯한 graphite outline으로 경계를 남깁니다. 플로팅 툴바와 같은 frosted glass 톤 안에서 탭 상태가 더 조용하고 명확하게 읽히도록 정리했습니다.

This release refines the top workspace tabs into an attached liquid-glass shape. The active tab uses one consistent sky rim across the top and sides, while inactive tabs keep a barely visible graphite outline instead of hard divider lines.

![상단 탭과 플로팅 툴바](screenshots/readme/top-tabs-liquid-glass.svg)

| 구분 | 개선 내용 |
| --- | --- |
| 활성 탭 | sky rim을 위/좌/우 동일 톤으로 맞추고 두 겹처럼 보이던 top highlight 제거 |
| 비활성 탭 | 매우 낮은 alpha의 graphite outline으로 경계를 보일듯 말듯하게 유지 |
| 분리선 | Obsidian 기본 tab separator와 pseudo-element 라인을 숨겨 `&#124;`처럼 보이는 선 제거 |
| 문서 자산 | 첨부 화면 구도의 README 신기능 이미지를 `screenshots/readme/`에 추가 |

### v3.1.50 — README 화면 투어 / README Visual Tour Refresh

README 상단 Visual Tour에 실제 작업 화면과 설정 화면 스크린샷을 보강했습니다. 문서 작성 surface, 플로팅 툴바, Style Settings의 보고서 옵션, Owen Editor 툴바 설정을 첫 화면에서 바로 확인할 수 있습니다.

This release expands the README Visual Tour with real workspace screenshots for the writing surface, floating toolbar, report-oriented Style Settings controls, and Owen Editor toolbar options.

![문서 작성 화면과 플로팅 툴바](screenshots/readme/workspace-writing-surface.jpg)

| 구분 | 개선 내용 |
| --- | --- |
| 작업 화면 | 문서 표면, floating glass toolbar, 사이드바 톤을 한 화면에서 확인 |
| 설정 화면 | Style Settings의 본문/보고서 옵션과 Owen Editor 툴바 설정 이미지 추가 |
| 문서 자산 | 새 JPG 3장을 `screenshots/readme/` 인벤토리에 등록 |

이전 신기능 소개는 [dev/WIKI/DOCS/v3/feature-history.md](dev/WIKI/DOCS/v3/feature-history.md)에 보관합니다.

---

## 3. 테마 설치 / Installation Details

### 옵션 A — Obsidian 커뮤니티 마켓 (승인 후) / Community Theme Browser

1. 설정 → **외관 → 테마 관리**
2. 검색: `Owen Graphite`
3. 설치 → 사용

### 옵션 B — ZIP 수동 설치 / Manual ZIP Install

[Releases 페이지](https://github.com/towishy/Owen-Graphite/releases/latest)에서 **`Owen-Graphite-3.1.64.zip`** 을 받아 압축 해제합니다.

| 플랫폼 | 대상 경로 |
| --- | --- |
| Windows | `<YourVault>\.obsidian\themes\Owen Graphite\` |
| macOS / Linux | `<YourVault>/.obsidian/themes/Owen Graphite/` |

설치 후 Obsidian → 설정 → **외관 → 테마** → `Owen Graphite` 선택.

> ⚠️ Release Assets에는 GitHub 자동 생성 `Source code (zip)`도 함께 표시됩니다. 반드시 `Owen-Graphite-3.1.64.zip` 을 받으세요.

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

자세한 기여 가이드는 [CONTRIBUTING.md](CONTRIBUTING.md), 변경 이력은 [CHANGELOG.md](CHANGELOG.md), 보존·검증 계약은 [dev/WIKI/DOCS/v3/design-spec.md](dev/WIKI/DOCS/v3/design-spec.md) 참조.

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
