# Changelog

All notable changes to **Owen Graphite** are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

> v3.0.0 is a **from-scratch rewrite**. v2.x history is intentionally not carried forward; see git tags for the legacy line.

## [3.0.4] — 2026-05-16 — Scanner warnings: text-decoration shorthand sweep

### Changed

- **커뮤니티 스캐너 `text-decoration partially supported` 워닝 일괄 정리** — `src/**/*.css`의 longhand `text-decoration-line/style/color/thickness` 42개 선언을 동등한 L1 `text-decoration` 단축형으로 조합. 링크 밑줄·스트라이크스루·철자 오류 수식 등 모든 표시는 100% 동일.
- 남은 `text-decoration-skip-ink: none` 3건은 H1/H3/H4 밑줄이 g·p·q 등 descender를 관통하며 그려지도록 유지하는 의도적 디자인 함수로 유지.

### Notes

- `text-indent`(2건)과 남은 `text-decoration-skip-ink`(3건) 워닝은 스캐너의 보수적 false positive이며 현재 Obsidian Electron 25+에서 완전 지원됩니다.

## [3.0.3] — 2026-05-16 — Scanner warnings: multicolumn cleanup

### Changed

- **커뮤니티 테마 스캐너 “multicolumn partially supported” 워닝 제거** — `src/**/*.css` 의 19개 `break-before/after/inside` 선언을 동등한 `page-break-*`(L2 알리스) 만 남기도록 치환. 인쇄(쪽 나눌) 동작과 디자인 100% 동일.

### Notes

- 남은 두 워닝 — `text-decoration` 계열(점선/두께/색 조절 underline)과 `text-indent`은 스캐너의 보수적 false positive입니다. 현재 Obsidian(Electron 25+)에서 완전 지원되며, 디자인(외부 링크의 닷티드 단과 한국어 본문 들여쓰기)을 손상하지 않고는 제거할 수 없어 남겨둡니다.

## [3.0.2] — 2026-05-16 — File explorer hover double-paint full fix

### Fixed

- **파일 탐색기 hover 더블 페인트(완전 해결)** — v3.0.1에서 여전히 남아있던 근본 원인 2가지를 제거.
  1. `src/chrome/37-tabs-file-explorer-search.css` 의 row hover 규칙이 `min-height` 24→32px, transform shift, inner pill padding을 동시에 키우면서 row와 pill이 겹쳐 두 겹으로 보이던 점프. → row는 transparent 고정, pill만 resting과 동일한 크기로 글래스 톤 적용.
  2. Obsidian 코어의 `--nav-item-background-{hover,active,selected}` 토큰이 그대로 살아있어 row에 회색 박스를 그리던 경로. → file-explorer 스코프에서 세 토큰을 transparent로 덮어 코어 페인트 경로 완전 차단.
- 최상위 root 폴더 hover는 resting pill 위에 글래스를 다시 얹는 대신 단일 톤(`rgba(255,255,255,0.92)` / dark 동등)으로 살짝 진해지게만 처리.

## [3.0.1] — 2026-05-16 — File explorer hotfix

### Fixed

- **파일 트리 hover 더블 페인트** — `src/chrome/31-navigation-tasks-search.css` 에 남아있던 v2 잔존 룰이 행 전체에 불투명 회색(`#f3f4f6` / `#1f2937`)을 칠해, `src/chrome/37-tabs-file-explorer-search.css` 의 글래스 pill 위에 회색 배경이 한 번 더 보이던 현상 제거. 이제 hover 표현은 글래스 pill 단일 레이어로 일원화됩니다.

### Changed

- **사이드바 파일 탐색기 컴팩트화** — 행 높이 28→24px, 자식 들여쓰기 15→8px, 아이콘 영역과 상하 여백 축소(자세한 수치는 `src/chrome/37-tabs-file-explorer-search.css`). 같은 패널 폭에서 약 20% 더 많은 문서 제목이 보입니다. 폴더 vertical rail과 hover/active 글래스 표현은 유지.

## [3.0.0] — 2026-05-16 — From-scratch rewrite with zero `!important`

### Summary

Owen Graphite v3.0.0은 v2.30.14의 픽셀 결과를 보존한 채 16,000+ 줄 CSS를 처음부터 다시 작성한 릴리즈입니다. `src/` 폴더 구조(tokens → base → surfaces → chrome → features → themes → plugins → polish)를 새로 설계하고, declaration-level `!important`를 5,816개에서 0개로 줄였습니다. computed-style fingerprint diff는 Light/Dark 모두 0, Live Preview hit-routing 감사도 clean입니다.

### Changed

- **CSS 재작성** — `dev/*` 60+ 파일을 `src/*` 폴더 8개 계층(tokens/base/surfaces/chrome/features/themes/plugins/polish)으로 재구성. 모든 본문 룰은 unlayered, 캐스케이드는 파일 import 순서 + 선택자 특이도로 통제.
- **`!important` 정책** — declaration-level `!important` = 0 (S11.5 일괄 제거). 자세한 휴리스틱·실증 결과는 [docs/v3/cascade-research.md](docs/v3/cascade-research.md) §4.1.
- **토큰 contract 유지** — `--ogd-*` 토큰 255개의 이름과 기본값은 v2.30.14와 동일. Style Settings 옵션 호환.
- **빌드 도구 교체** — `scripts/bundle_v3.py` 가 새 엔트리 포인트. `dist/theme-v3.css` 가 진본 번들이며 `theme.css` 는 이 번들의 사본.
- **CI 워크플로우** — `.github/workflows/validate.yml` 과 `release.yml` 을 v3 도구(`bundle_v3.py`, `audit_v3_hit_routing.py`, `v3_audit_duplicate_selectors.py`)로 갱신.

### Added

- `docs/v3/` — 보존 계약(`design-spec.md`), 캐스케이드 연구(`cascade-research.md`), 릴리즈 절차(`release-plan.md`), surface state matrix, golden image scenarios, live preview editability, style settings contract, token inventory.
- `docs/v3/research/` — 캐스케이드 휴리스틱 실증 시나리오 6종 + golden rig.
- `docs/v3/computed-fingerprint-v3.0.0-light.json` · `computed-fingerprint-v3.0.0-dark.json` — 베이스라인 fingerprint.
- `scripts/audit_v3_hit_routing.py` — Live Preview 블록 위젯·HyperMD line·active line·embed BFC·content overflow 회귀를 한 번에 검사하는 standalone 감사.
- `scripts/v3_audit_duplicate_selectors.py` — 모듈 간 selector 중복 통계.
- `scripts/v3_strip_important_src.py` — 주석 보호된 안전한 `!important` 제거기.
- `scripts/build_release.py` — `bundle_v3.py` 호출 → `theme.css` 승격 → `dist/Owen-Graphite-3.0.0.zip` 빌드.
- `scripts/sync_obsidian_theme.py` — 번들 + 승격 + Obsidian vault 동기화 통합 명령.

### Removed

- `dev/` 폴더 전체 (v2 source). `src/` 가 새 진본.
- v2 전용 스크립트: `bundle_theme.py`, `validate_theme.py`, `analyze_theme_css.py`, `diff_guard.py`, `who_added.py`, `hit_routing_probe.py`, `visual_regression.py`, `contrast_audit.py`, `generate_screenshots.py`, `build_selector_provenance.py`, `changelog_lint.py`, `find_safe_duplicate_selectors.py` 등.
- v2 전용 문서: `liquid-glass-migration-checklist.md`, `liquid-glass-token-map.md`, `css-important-audit.md`, `style-settings.md`, `qa-checklist.md` (v2 절차 한정), `ai-document-guide.md` 등.
- v2 release artifact: `dist/Owen-Graphite-2.30.*.zip`, `dist/theme-v3.no-important.css`.
- v2 screenshots: `screenshots/golden/v2.30.14/` 와 readme 폴더의 `v2.*.svg` 자산.

### Verification

| 항목 | 도구 | 결과 |
| --- | --- | --- |
| 번들 빌드 | `scripts/bundle_v3.py` | OK (16,509 줄, !important=4 — 모두 주석 안) |
| Light fingerprint diff | `scripts/fp_diff_summary.py --theme light` | **0** |
| Dark fingerprint diff | `scripts/fp_diff_summary.py --theme dark` | **0** |
| Live Preview hit-routing | `scripts/audit_v3_hit_routing.py` | clean |
| Release ZIP | `scripts/build_release.py` | `dist/Owen-Graphite-3.0.0.zip` (265 KB) |

[3.0.4]: https://github.com/towishy/Owen-Graphite/releases/tag/3.0.4
[3.0.3]: https://github.com/towishy/Owen-Graphite/releases/tag/3.0.3
[3.0.0]: https://github.com/towishy/Owen-Graphite/releases/tag/3.0.0
