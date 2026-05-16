# v3 Style Settings Contract (extracted from v2.30.14)

이 문서는 `dev/scripts/extract_style_settings.py`가 자동 생성합니다.
v3-rewrite는 아래 모든 기능 옵션의 `id`/`type`/`default`/`title`을 그대로 유지해야 합니다.
사용자 vault에 저장된 기존 설정이 v3.0 설치 후에도 동일하게 적용됩니다.

- 스키마 이름: `Owen Graphite`
- 스키마 id: `owen-graphite-document`
- 전체 엔트리(heading 포함): **76**
- 기능 옵션 수(`class-toggle` / `variable-*` / `class-select`): **37**

## 기능 옵션 목록

| id | type | default | title |
| --- | --- | --- | --- |
| `ogd-body-size` | `variable-number-slider` | `15` | 본문 폰트 크기 |
| `ogd-line-height` | `variable-select` | `1.5` | 본문 줄간격 |
| `ogd-max-width` | `variable-select` | `420mm` | 본문 최대 폭 |
| `ogd-accent` | `variable-color` | `#4b5563` | 헤더 강조 색상 |
| `ogd-modern-tables` | `class-toggle` | `true` | 표 모던 스타일 강화 |
| `ogd-print-avoid-breaks` | `class-toggle` | `true` | PDF 블록 분할 방지 강화 |
| `ogd-report-mode` | `class-toggle` | `false` | 보고서 모드 (헤더 자동 넘버링 + 본문 들여쓰기 + 세리프) |
| `ogd-pdf-compact` | `class-toggle` | `false` | PDF Compact Report |
| `ogd-pdf-link-mode` | `class-select` | `ogd-pdf-links-inline` | PDF 링크 출력 방식 |
| `ogd-serif-body` | `class-toggle` | `false` | 본문 세리프 글꼴 |
| `ogd-indent-paragraph` | `class-toggle` | `false` | 첫 줄 들여쓰기 |
| `ogd-auto-number-headings` | `class-toggle` | `false` | 헤더 자동 넘버링 (1. 1.1 1.1.1) |
| `ogd-drop-cap` | `class-toggle` | `false` | 드롭 캡 (첫 문단 첫 글자 크게) |
| `ogd-spacing-preset` | `class-select` | `ogd-spacing-standard` | 간격 프리셋 |
| `ogd-accent-preset` | `class-select` | `ogd-accent-graphite` | 액센트 컬러 프리셋 |
| `ogd-code-theme` | `class-select` | `ogd-code-light` | 코드블록 테마 |
| `ogd-eye-care` | `class-toggle` | `false` | 시선 보호 모드 (베이지 배경) |
| `ogd-auto-dark` | `class-toggle` | `false` | OS 다크 모드 자동 추종 |
| `ogd-glass-intensity` | `class-select` | `ogd-glass-standard` | 데스크톱 Glass 강도 |
| `ogd-motion-intensity` | `class-select` | `ogd-motion-standard` | 데스크톱 Hover 움직임 |
| `ogd-cjk-boost` | `class-toggle` | `true` | 한글/CJK 폰트 +0.5px 자동 보정 |
| `ogd-first-page-header-enabled` | `class-toggle` | `true` | PDF 첫 페이지 Header 표시 |
| `ogd-first-page-header` | `variable-text` | `` | PDF 첫 페이지 우측 상단 문구 (본문) |
| `ogd-first-page-header-color` | `variable-color` | `#111827` | 첫 페이지 우측 본문 사이드바 색상 |
| `ogd-fp-right-label` | `variable-text` | `` | 첫 페이지 우측 상단 라벨 (소문자) |
| `ogd-first-page-header-left` | `variable-text` | `` | PDF 첫 페이지 좌측 상단 문구 (본문) |
| `ogd-first-page-header-left-color` | `variable-color` | `#0ea5e9` | 첫 페이지 좌측 본문 사이드바 색상 |
| `ogd-fp-left-label` | `variable-text` | `` | 첫 페이지 좌측 상단 라벨 (소문자) |
| `ogd-fp-label-color` | `variable-color` | `#6b7280` | 첫 페이지 좌·우 라벨 공통 색상 |
| `ogd-last-page-footer` | `class-toggle` | `false` | PDF 마지막 페이지 Footer 표시 |
| `ogd-last-page-footer-label` | `variable-text` | `` | PDF 마지막 페이지 Footer 라벨 |
| `ogd-last-page-footer-title` | `variable-text` | `` | PDF 마지막 페이지 Footer 제목 |
| `ogd-last-page-footer-body` | `variable-text` | `` | PDF 마지막 페이지 Footer 본문 |
| `ogd-last-page-footer-color` | `variable-color` | `#0ea5e9` | PDF 마지막 페이지 Footer 세로바 색상 |
| `ogd-last-page-footer-label-color` | `variable-color` | `#64748b` | PDF 마지막 페이지 Footer 라벨 색상 |
| `ogd-last-page-footer-title-color` | `variable-color` | `#0f172a` | PDF 마지막 페이지 Footer 제목 색상 |
| `ogd-last-page-footer-text-color` | `variable-color` | `#334155` | PDF 마지막 페이지 Footer 본문 색상 |

## 비기능 엔트리 (heading / info)

| id | type | title |
| --- | --- | --- |
| `ogd-settings-reading` | `heading` | 읽기와 본문 |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `ogd-settings-tables` | `heading` | 표와 코드 |
| `ogd-settings-report` | `heading` | 보고서와 PDF |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `ogd-settings-workspace` | `heading` | 워크스페이스와 접근성 |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `—` | `—` | — |
| `ogd-settings-first-page` | `heading` | PDF 첫 페이지 헤더 |
| `ogd-settings-last-page-footer` | `heading` | PDF 마지막 페이지 Footer |
