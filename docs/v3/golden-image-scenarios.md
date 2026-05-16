# v3 Golden Image Scenarios

S1에서 캡처할 골든 이미지 시나리오 목록입니다. v3-rewrite는 각 시나리오에서 v2.30.14 baseline과 픽셀 단위로 일치해야 합니다.

## 캡처 조건

- 도구: Playwright Chromium, viewport `1440 × 900`, `device_scale_factor=2` (2x retina)
- 폰트 렌더링: subpixel antialiasing 비활성 (`-webkit-font-smoothing: antialiased`)
- 캡처 위치: `screenshots/golden/v2.30.14/<scenario-id>.png`
- 비교 도구: pixelmatch + Playwright `toMatchSnapshot()`, diff threshold 1%
- 캡처 시점: v3-rewrite 브랜치 시작 직전(v2.30.14 baseline) 빌드에서 1회

## 카테고리별 시나리오 (60+)

### Reading View (12)

| id | 내용 | 옵션 |
| --- | --- | --- |
| `reading-light-default` | 기본 마크다운 문서 | light, Style Settings 기본 |
| `reading-dark-default` | 기본 마크다운 문서 | dark |
| `reading-light-report-mode` | 보고서 모드 | light, `ogd-report-mode=on` |
| `reading-dark-report-mode` | 보고서 모드 | dark, `ogd-report-mode=on` |
| `reading-headings-h1-h6` | H1~H6 샘플 | light |
| `reading-headings-h1-h6-dark` | H1~H6 샘플 | dark |
| `reading-paragraph-rhythm` | 단락·인용·구분선 | light |
| `reading-blockquote-stack` | 중첩 인용 | light |
| `reading-list-mixed` | bullet + numbered + checkbox | light |
| `reading-list-mixed-dark` | bullet + numbered + checkbox | dark |
| `reading-link-citation` | 일반 링크 + 인용 링크 | light |
| `reading-image-embed` | 이미지 임베드 | light |

### Live Preview (8)

| id | 내용 | 옵션 |
| --- | --- | --- |
| `lp-light-default` | 기본 편집 화면 | light |
| `lp-dark-default` | 기본 편집 화면 | dark |
| `lp-callout-inside` | 콜아웃 내부 편집 | light |
| `lp-callout-inside-dark` | 콜아웃 내부 편집 | dark |
| `lp-table-widget` | 표 위젯 편집 | light |
| `lp-codeblock-edit` | 코드블록 편집 | light |
| `lp-active-line` | 현재 캐럿 라인 강조 | light |
| `lp-html-table-embed` | HTML 테이블 임베드 | light |

### Surfaces (16)

| id | surface × state | 비고 |
| --- | --- | --- |
| `surface-tab-rest` | workspace tab rest | light |
| `surface-tab-hover` | workspace tab hover | light |
| `surface-tab-active` | workspace tab active (sky pastel) | light |
| `surface-tab-rest-dark` | workspace tab rest | dark |
| `surface-tab-active-dark` | workspace tab active | dark |
| `surface-nav-folder-active` | active folder marker | light |
| `surface-nav-file-active` | active file marker | light |
| `surface-button-rest` | toolbar button rest | light |
| `surface-button-hover` | toolbar button hover | light |
| `surface-callout-note` | note 콜아웃 (5종 중 대표) | light |
| `surface-callout-warning` | warning 콜아웃 | light |
| `surface-callout-info-dark` | info 콜아웃 | dark |
| `surface-code-block-light` | 코드블록 | light |
| `surface-code-block-dark` | 코드블록 | dark |
| `surface-link-card` | 링크 카드 (embed) | light |
| `surface-link-card-dark` | 링크 카드 | dark |

### Tables (8)

| id | 내용 | 옵션 |
| --- | --- | --- |
| `table-markdown-widget` | 일반 markdown table widget | light |
| `table-markdown-widget-dark` | 같은 표 | dark |
| `table-html-utility-class` | `.risk-table`/`.numeric-table` 유틸리티 클래스 | light |
| `table-html-utility-dark` | 동일 유틸리티 클래스 | dark |
| `table-zebra-disabled` | `ogd-zebra-disabled-permanently=on` | light |
| `table-modern-strong` | `ogd-modern-tables=on` 강조 | light |
| `table-pdf-mode` | report-mode 표 | light |
| `table-pdf-mode-dark` | report-mode 표 | dark |

### Chrome (8)

| id | 내용 | 옵션 |
| --- | --- | --- |
| `chrome-ribbon-light` | 좌측 ribbon | light |
| `chrome-ribbon-dark` | 좌측 ribbon | dark |
| `chrome-tab-strip-light` | 상단 tab strip | light |
| `chrome-tab-strip-dark` | 상단 tab strip | dark |
| `chrome-status-bar-light` | 하단 status bar | light |
| `chrome-file-explorer-light` | 파일 탐색기 | light |
| `chrome-file-explorer-dark` | 파일 탐색기 | dark |
| `chrome-settings-panel-light` | 설정 패널 | light |

### Overlays (6)

| id | 내용 | 옵션 |
| --- | --- | --- |
| `overlay-menu-light` | 컨텍스트 메뉴 | light |
| `overlay-menu-dark` | 컨텍스트 메뉴 | dark |
| `overlay-tooltip-light` | tooltip | light |
| `overlay-popover-light` | 호버 카드 (block ref preview) | light |
| `overlay-popover-dark` | 호버 카드 | dark |
| `overlay-suggestion-light` | autocomplete suggestion | light |

### Accessibility (4)

| id | 내용 | 조건 |
| --- | --- | --- |
| `a11y-prefers-contrast-more` | high contrast | `prefers-contrast: more` |
| `a11y-prefers-reduced-motion` | reduced motion (정적 캡처) | `prefers-reduced-motion: reduce` |
| `a11y-forced-colors-light` | Windows High Contrast | `forced-colors: active` |
| `a11y-forced-colors-dark` | Windows High Contrast Dark | `forced-colors: active`, dark |

### Print / PDF (4)

| id | 내용 | 조건 |
| --- | --- | --- |
| `print-default-light` | 기본 PDF 출력 | `@media print` |
| `print-report-mode` | report-mode PDF | `ogd-report-mode=on`, print |
| `print-compact` | compact PDF | `ogd-pdf-compact=on`, print |
| `print-last-page-footer` | 마지막 페이지 footer | `ogd-last-page-footer=on`, print |

## 총 시나리오 수

| 카테고리 | 수 |
| --- | ---: |
| Reading View | 12 |
| Live Preview | 8 |
| Surfaces | 16 |
| Tables | 8 |
| Chrome | 8 |
| Overlays | 6 |
| Accessibility | 4 |
| Print / PDF | 4 |
| **합계** | **66** |

## 캡처 스크립트 (S1 작업)

- 신규: `scripts/capture_golden_images.py`
  - Playwright 기반
  - 입력: `docs/v3/golden-image-scenarios.md` (이 문서)의 표 파싱 + `dev/test-samples/` 안의 fixture 파일 매핑
  - 출력: `screenshots/golden/v2.30.14/<id>.png`
  - 옵션: `--check` 모드 — 기존 이미지와 새 캡처를 pixelmatch 비교, diff > 1% 시 실패
- baseline 캡처: v2.30.14 빌드 1회
- v3-rewrite 진행 중에는 동일 스크립트 `--check` 모드로 회귀 감지

## 시나리오별 fixture 매핑 (S1에서 결정)

각 시나리오는 `dev/test-samples/` 안의 어느 마크다운 파일을 어떻게 렌더링할지 결정해야 합니다. 현재 `dev/test-samples/`에는 다음 카테고리의 fixture가 이미 존재합니다.

- `callout-recommendation-samples.html`
- `document-status-chips-samples.html`
- `h1-h4-recommended-heading-sample.html`
- `liquid-glass-core-state-matrix.html`
- 기타 markdown sample

S1 단계에서 각 시나리오 ↔ fixture를 1:1 매핑하는 표를 만들고 누락된 시나리오는 신규 fixture를 작성합니다.

## 비고

- 픽셀 100% 보존이 어려운 시나리오(예: `backdrop-filter`가 다른 GPU에서 미세 차이)는 **사용자가 명시적으로 허용한 시나리오 목록**에 추가하고 diff threshold를 별도 설정.
- 골든 이미지는 git에 커밋합니다 (PNG, 약 30~50KB × 66 = 2~3MB 정도 예상). LFS는 사용하지 않습니다.
