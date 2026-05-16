# Contributing to Owen Graphite v3

Owen Graphite v3 (현재 안정 릴리즈 v3.1.5)은 처음부터 다시 작성된 코드베이스입니다. 본 문서는 v3 기여자가 따라야 할 워크플로우와 검증 절차를 정리합니다.

## 0. 사전 준비

- Python 3.10+ (`.venv\Scripts\python.exe` 권장; Windows 기준)
- Obsidian 1.6.0+
- (선택) Style Settings 플러그인 — 옵션 토글 확인용

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt   # Playwright 등 fingerprint 캡처용
python -m playwright install chromium
```

## 1. 폴더 구조

진본 CSS는 모두 `src/` 아래에 있습니다.

```
src/
  tokens/      # 색, 타이포, 간격, 그림자, glass surface 토큰
  base/        # reset, 타이포, reading view, live preview 기본
  surfaces/    # callout, table, code, list, embed, canvas, graph
  chrome/      # workspace, nav, overlay, settings
  features/    # style settings, report, pdf/print, dark
  themes/      # dark, a11y
  plugins/     # dataview, tasks, 기타 호환
  polish/      # 최종 조정 + glass polish
```

번들 결과는 `dist/theme-v3.css`, 진본 사본은 루트 `theme.css`.

## 2. 작업 흐름

1. **분기**: `git checkout -b feature/<name>` (베이스: `main`)
2. **편집**: `src/` 안에서만 수정. `theme.css` 는 직접 편집하지 않습니다.
3. **번들**: `python dev/scripts/bundle_v3.py`
4. **승격**: `Copy-Item dist\theme-v3.css theme.css -Force` (또는 macOS/Linux `cp`)
5. **감사**:
   - `python dev/scripts/audit_v3_hit_routing.py` — Live Preview 회귀 차단
   - `python dev/scripts/v3_audit_duplicate_selectors.py` — 중복 selector 통계 (정보용)
6. **시각 회귀 (선택)**:
   - `python dev/scripts/capture_computed_fingerprint.py --build v3 --theme light`
   - `python dev/scripts/capture_computed_fingerprint.py --build v3 --theme dark`
   - `python dev/scripts/fp_diff_summary.py [--theme dark]` — 베이스라인과 0 diff 유지
7. **commit/PR**: 메시지에 영향 받는 `src/` 모듈을 명시. fingerprint diff가 0이 아닌 경우 PR 본문에 사유 첨부.

## 3. 보존 계약 (Preservation Contract)

v3는 v2.30.14의 픽셀 결과를 **보존**합니다. 모든 변경은 다음을 통과해야 합니다.

| 계약 | 도구 | 통과 기준 |
| --- | --- | --- |
| C1 시각 | `dev/scripts/capture_computed_fingerprint.py` + `fp_diff_summary.py` | Light/Dark diff = 0 |
| C2 Live Preview 편집성 | `dev/scripts/audit_v3_hit_routing.py` | violations = 0 |
| C3 Style Settings 옵션 | 수동 토글 매트릭스 | 37 옵션 × ON/OFF 동일 |
| C4 PDF 출력 | `@media print` 시나리오 수동 비교 | 페이지 수·레이아웃·footer 동일 |

상세 계약은 [docs/v3/design-spec.md](docs/v3/design-spec.md) 참고.

## 4. `!important` 정책

declaration-level `!important` = **0**. 새 `!important`를 추가하려면:

1. 해당 룰의 선택자 특이도가 Obsidian core를 이기는지 확인 (대부분 충분합니다)
2. 그래도 필요하다면 PR 본문에 "defeats core <selector>" 형태로 사유 명시
3. CSS 주석에 동일한 사유 인라인 명시

자동 제거 도구 `dev/scripts/v3_strip_important_src.py` 는 주석 안의 `!important` 토큰은 건드리지 않습니다.

## 5. 디자인 가이드라인 (Liquid Glass core)

- **Resting state**: 흰색/회색 frosted glass, 좌측 vertical rail 금지
- **Hover**: 살짝 밝아지고 들어올림, wide soft downward shadow, 얕은 pastel 톤
- **Active**: 선택 문서/탭 같은 명확한 상태에만 sky tint + glass border 적용
- **반복 chrome**: 의미색 대신 밝기·그림자로만 반응
- **샘플 자산**: 새 기능 추가 시 README의 해당 섹션에 liquid-glass 샘플 이미지(SVG/PNG) 동봉

자세한 원칙은 [docs/v3/surface-state-matrix.md](docs/v3/surface-state-matrix.md).

## 6. Pre-commit hook (선택)

```bash
ln -sf ../../dev/scripts/hooks/pre-commit .git/hooks/pre-commit
chmod +x dev/scripts/hooks/pre-commit
```

Windows에서는 hook 내용을 `.git/hooks/pre-commit.ps1` 로 직접 옮기거나, WSL/Git Bash 환경에서 실행하세요. Hook은 번들 + hit-routing 감사를 강제합니다.

## 7. Release 절차

`docs/v3/release-plan.md` 의 R0~R6 단계 참조.

요약:

1. `manifest.json` 의 `version` 갱신
2. `CHANGELOG.md` 에 새 섹션 추가
3. `python dev/scripts/build_release.py` → `dist/Owen-Graphite-<version>.zip`
4. `git tag <version>` + `git push origin <version>` (CI가 GitHub Release 생성)
