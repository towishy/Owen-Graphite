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

### Print / PDF (17)

| id | 내용 | 조건 |
| --- | --- | --- |
| `print-default-light` | 기본 PDF 출력 | `@media print` |
| `print-report-mode` | report-mode PDF | `ogd-report-mode=on`, print |
| `print-compact` | compact PDF | `ogd-pdf-compact=on`, print |
| `print-last-page-footer` | 마지막 페이지 footer | `ogd-pdf-footer-enabled=on`, print |
| `print-pdf-header-short` | 짧은 첫 페이지 헤더 라벨 | `ogd-pdf-header-enabled=on`, custom text |
| `print-pdf-header-long` | 긴 첫 페이지 헤더 라벨 말줄임 | `ogd-pdf-header-enabled=on`, long custom text |
| `print-pdf-footer-long` | 긴 마지막 페이지 푸터 라벨 말줄임 | `ogd-pdf-footer-enabled=on`, long custom text |
| `print-pdf-both-labels` | 헤더와 푸터 동시 출력 | header/footer on |
| `print-pdf-table-end` | 표로 끝나는 문서의 푸터 reserve | footer on, table as final block |
| `print-pdf-code-end` | 코드블록으로 끝나는 문서의 푸터 reserve | footer on, code block as final block |
| `print-pdf-list-end` | 리스트로 끝나는 문서의 푸터 reserve | footer on, list as final block |
| `print-pdf-presets` | 빠른 문구 프리셋 출력 | each marginalia preset |
| `print-pdf-segmented-labels` | Key/Value 2세그먼트 헤더/푸터 | `ogd-pdf-label-segmented`, badge style, header/footer palette split |
| `print-live-preview-pdf-parity` | Live Preview/Reading/PDF 공통 callout + 긴 셀 fixture | `docs/v3/research/live-preview-pdf-parity-fixture.html`, `ogd-pdf-visibility`, `ogd-pdf-font-comfortable` |
| `print-image-body-quality` | PDF 이미지/figure/caption + 본문 조판 fixture | `docs/v3/research/pdf-image-body-quality-fixture.html`, `ogd-figure-*`, `ogd-pdf-visibility`, `ogd-pdf-font-comfortable` |
| `print-code-font-clarity` | Live Preview/Reading/PDF 코드 폰트와 syntax 색상 fixture | `docs/v3/research/code-font-clarity-fixture.html`, `ogd-code-*`, `cm-*`, `token.*` |
| `print-table-callout-parity` | LP markdown table widget/HTML embed/Reading/PDF 표와 콜아웃 fixture | `docs/v3/research/table-callout-parity-fixture.html`, `cm-table-widget`, `cm-html-embed`, `ogd-pdf-visibility`, `ogd-pdf-font-comfortable` |

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
| Print / PDF | 17 |
| **합계** | **79** |

## v3 결과 검증 스크립트 (최신 v3.1.36 기준)

v3는 기존 66 시나리오 대신 **computed-style fingerprint** 방식으로 시각 보존을 검증했습니다 (최초 v3.0.0 릴리즈 시점에 0 diff 달성, 이후 v3.0.x → v3.1.x 체인은 디자인 표면을 건드리지 않음). PDF marginalia는 v3.1.x에서 추가된 취약 출력 표면이므로 위 8개 시나리오를 별도 수동/자동 후보로 유지합니다.

- 캡처: dev/scripts/capture_computed_fingerprint.py --build v3 --theme {light,dark}
- diff: dev/scripts/fp_diff_summary.py [--theme dark]
- 하네스: docs/v3/research/golden-rig/obsidian-harness.html
- Live Preview/PDF 품질 fixture: docs/v3/research/live-preview-pdf-parity-fixture.html
- PDF 이미지/본문 품질 fixture: docs/v3/research/pdf-image-body-quality-fixture.html
- 코드 폰트/PDF 품질 fixture: docs/v3/research/code-font-clarity-fixture.html
- 표/콜아웃 LP-PDF 품질 fixture: docs/v3/research/table-callout-parity-fixture.html
- 로컬 렌더 smoke check: dev/scripts/audit_visual_quality_fixture.py
- computed-style parity check: dev/scripts/audit_lp_pdf_computed_styles.py
- 베이스라인: docs/v3/computed-fingerprint-v3.0.0-{light,dark}.json (v3 최초 캡처 원본 — 파일명 그대로 유지)
- 결과: 모두 0 diff

실제 PNG 스크린샷은 screenshots/README.md 참고. 이 문서의 66 시나리오 목록은 향후 자동 시각 회귀 스위트를 도입할 때의 설계 문서로 남겨둡니다.
