# v3 Style Settings Contract (extracted from v2.30.14)

이 문서는 v3 Style Settings 계약입니다.
아래 기능 옵션의 `id`/`type`/`default`/`title`은 사용자 vault 설정 호환성에 직접 영향을 줍니다.

- 스키마 이름: `Owen Graphite`
- 스키마 id: `owen-graphite-document`
- 전체 엔트리(heading 포함): **53**
- 기능 옵션 수(`class-toggle` / `variable-*` / `class-select`): **45**

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
| `ogd-pdf-visibility` | `class-toggle` | `false` | PDF 보고서 가시성 강화 |
| `ogd-pdf-screen-delivery` | `class-toggle` | `false` | PDF 고객 전달용 화면 가시성 |
| `ogd-pdf-font-size` | `class-select` | `ogd-pdf-font-standard` | PDF 글자 크기 |
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
| `ogd-pdf-header-enabled` | `class-toggle` | `false` | 첫 페이지 헤더 라벨 표시 |
| `ogd-pdf-footer-enabled` | `class-toggle` | `false` | 마지막 페이지 푸터 라벨 표시 |
| `ogd-pdf-label-layout` | `class-select` | `ogd-pdf-label-single` | PDF 라벨 구성 |
| `ogd-pdf-marginalia-preset` | `class-select` | `ogd-pdf-preset-custom` | 헤더/푸터 빠른 문구 |
| `ogd-pdf-marginalia-accent` | `variable-color` | `#475569` | 헤더/푸터 글자 색상 |
| `ogd-pdf-marginalia-style` | `class-select` | `ogd-pdf-label-bordered` | 헤더/푸터 라벨 스타일 |
| `ogd-pdf-marginalia-size` | `class-select` | `ogd-pdf-label-standard` | 헤더/푸터 라벨 크기 |
| `ogd-pdf-header-key-palette` | `class-select` | `ogd-pdf-header-key-graphite` | 헤더 Key 색상 |
| `ogd-pdf-header-value-palette` | `class-select` | `ogd-pdf-header-value-sky` | 헤더 Value 색상 |
| `ogd-pdf-header-text` | `variable-text` | `` | 첫 페이지 헤더 1번 Key 문구 |
| `ogd-pdf-header-value` | `variable-text` | `` | 첫 페이지 헤더 1번 Value 문구 |
| `ogd-pdf-header-dual-pair` | `class-toggle` | `false` | 첫 페이지 헤더 2번 Key/Value 표시 |
| `ogd-pdf-header2-key-palette` | `class-select` | `ogd-pdf-header2-key-graphite` | 헤더 2번 Key 색상 |
| `ogd-pdf-header2-value-palette` | `class-select` | `ogd-pdf-header2-value-sky` | 헤더 2번 Value 색상 |
| `ogd-pdf-header-text-2` | `variable-text` | `` | 첫 페이지 헤더 2번 Key 문구 |
| `ogd-pdf-header-value-2` | `variable-text` | `` | 첫 페이지 헤더 2번 Value 문구 |
| `ogd-pdf-header-position` | `class-select` | `ogd-pdf-header-top-right` | 첫 페이지 헤더 위치 |
| `ogd-pdf-footer-key-palette` | `class-select` | `ogd-pdf-footer-key-graphite` | 푸터 Key 색상 |
| `ogd-pdf-footer-value-palette` | `class-select` | `ogd-pdf-footer-value-sky` | 푸터 Value 색상 |
| `ogd-pdf-footer-text` | `variable-text` | `` | 마지막 페이지 푸터 Key 문구 |
| `ogd-pdf-footer-value` | `variable-text` | `` | 마지막 페이지 푸터 Value 문구 |

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
| `ogd-settings-pdf-marginalia` | `heading` | PDF 헤더/푸터 작은 라벨 |
| `ogd-pdf-settings-common` | `heading` | 공통 구성 |
| `ogd-pdf-settings-header` | `heading` | 헤더 설정 |
| `ogd-pdf-settings-footer` | `heading` | 푸터 설정 |
