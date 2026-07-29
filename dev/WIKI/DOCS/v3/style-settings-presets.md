# v3 Style Settings Presets

이 문서는 Style Settings 플러그인을 설치한 사용자가 목적별로 빠르게 시작할 수 있도록 권장 조합을 정리합니다. 실제 option id와 기본값은 [style-settings-contract.md](style-settings-contract.md)가 진본입니다.

## 빠른 선택

| 목적 | 켜거나 고를 옵션 | 추천 상황 |
| --- | --- | --- |
| 기술 문서 기본형 | `ogd-modern-tables`, `ogd-cjk-boost`, `ogd-code-light`, `ogd-spacing-standard` | README, 위키, API 노트처럼 표와 코드가 많은 문서 |
| 보고서/PDF 제출 | `ogd-auto-number-headings`, `ogd-print-avoid-breaks`, `ogd-pdf-header-enabled`, `ogd-pdf-footer-enabled` | A4/A3 PDF, 검토본, 내부 보고서 |
| 장시간 읽기 | `ogd-eye-care`, `ogd-serif-body`, `ogd-spacing-relaxed`, `ogd-motion-subtle` | 긴 리서치 노트, 독서 기록, 다크 모드 피로도 완화 |
| 넓은 위키 화면 | `ogd-max-width`, `ogd-modern-tables`, `ogd-glass-subtle` | 큰 모니터에서 여러 pane을 열고 쓰는 vault |
| 발표/검토용 강조 | `ogd-pdf-font-large`, `ogd-pdf-readability`, `ogd-accent-preset` | 화면 공유, 리뷰 PDF, 시니어 리뷰용 출력 |
| 고객 전달용 PDF | `ogd-pdf-font-comfortable`, `ogd-pdf-links-reference`, `ogd-print-avoid-breaks`, `ogd-modern-tables` | 메일, Teams, 브라우저 미리보기에서 바로 읽히는 외부 공유 PDF |

## 보고서/PDF 프리셋

| 그룹 | 권장값 |
| --- | --- |
| 문서 구조 | `ogd-auto-number-headings`: on, `ogd-indent-paragraph`: 필요 시 on, `ogd-serif-body`: 필요 시 on |
| 페이지 분할 | `ogd-print-avoid-breaks`: on |
| 첫 페이지 헤더 | `ogd-pdf-header-enabled`: on, `ogd-pdf-label-layout`: `ogd-pdf-label-segmented` 또는 `ogd-pdf-label-segmented-dual` |
| 두 번째 Key/Value | `ogd-pdf-header-dual-pair`: 보안 등급, 검토 상태, 부서 정보를 함께 넣을 때 on |
| 마지막 페이지 푸터 | `ogd-pdf-footer-enabled`: 제출일, 작성자, 문서 상태가 필요할 때 on |

## 고객 전달용 PDF 조합

| 그룹 | 권장값 |
| --- | --- |
| 본문 크기 | `ogd-pdf-font-size`: `ogd-pdf-font-comfortable` 또는 `ogd-pdf-font-large` |
| 페이지 분할 | `ogd-print-avoid-breaks`: on |
| 표 | `ogd-modern-tables`: on, 표가 넓으면 Markdown table에 `print-fit-table` 또는 `wrap-table` class 사용 |
| 링크 | `ogd-pdf-link-mode`: `ogd-pdf-links-reference`, 명시적인 `ogd-reference-list` 중심으로 정리 |
| 헤더/푸터 | 필요 시 `ogd-pdf-header-enabled`, `ogd-pdf-footer-enabled`, `ogd-pdf-label-badge`를 함께 사용 |

## 위키/기술 문서 프리셋

| 그룹 | 권장값 |
| --- | --- |
| 본문 | `ogd-body-size`: 기본값, `ogd-line-height`: `1.5`, `ogd-cjk-boost`: on |
| 표 | `ogd-modern-tables`: on, zebra는 기본 유지 |
| 코드 | `ogd-code-theme`: light/dark 모드와 맞춰 선택 |
| 워크스페이스 | `ogd-glass-intensity`: standard, `ogd-motion-intensity`: standard 또는 subtle |

## 장시간 읽기 프리셋

| 그룹 | 권장값 |
| --- | --- |
| 배경 | `ogd-eye-care`: on |
| 본문 | `ogd-serif-body`: 취향에 따라 on, `ogd-spacing-preset`: relaxed |
| 움직임 | `ogd-motion-intensity`: subtle |
| 강조색 | `ogd-accent-preset`: graphite 또는 muted 계열 |

## 검증 메모

- 설정 id, title, default를 바꾸면 [style-settings-contract.md](style-settings-contract.md)와 [style-settings-contract.json](style-settings-contract.json)을 함께 갱신합니다.
- 변경 후 `python dev/scripts/audit_style_settings_contract.py`를 실행합니다.
- PDF 관련 옵션을 바꾸면 `python dev/scripts/audit_pdf_header_footer.py`도 함께 실행합니다.