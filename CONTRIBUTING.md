# Contributing to Owen Graphite

이 저장소는 Obsidian용 보고서 지향 테마인 **Owen Graphite**를 관리합니다. 외부 기여를 환영합니다.

## 빠른 시작

```bash
git clone https://github.com/towishy/Owen-Graphite.git
cd Owen-Graphite
python3 -m venv .venv
source .venv/bin/activate
pip install -r scripts/requirements.txt 2>/dev/null || true
```

## 작업 흐름

### 1. 로컬 Obsidian 볼트에 즉시 반영

테마를 수정한 후 볼트에 동기화하여 실시간 확인합니다.

```bash
rsync -a --delete \
  --exclude='.git/' --exclude='.venv/' --exclude='dist/' --exclude='dev/temp/' --exclude='.DS_Store' \
  /path/to/Owen-Graphite/ \
  "/path/to/YourVault/.obsidian/themes/Owen Graphite/"
```

Obsidian → Settings → Appearance → 테마 새로고침으로 변경사항 확인.

### 2. 검증

커밋 전 반드시 검증 스크립트를 통과해야 합니다.

```bash
python3 scripts/validate_theme.py
```

수행되는 검사:
- `manifest.json` semver 형식
- `manifest.json` / `README.md` / `CHANGELOG.md` 버전 정합성
- Style Settings 옵션 카운트
- 스크린샷 PNG 치수
- Live Preview / Reading View 가드 룰 (편집성·레이아웃 보호)
- 색상 대비 (WCAG AA, 13쌍)
- 릴리즈 ZIP 자산 유효성

선택 visual regression:

```powershell
# Windows PowerShell
.\.venv\Scripts\python.exe -m pip install playwright
.\.venv\Scripts\python.exe -m playwright install chromium
.\.venv\Scripts\python.exe scripts\visual_regression.py
```

```bash
# macOS / Linux
.venv/bin/python -m pip install playwright
.venv/bin/python -m playwright install chromium
.venv/bin/python scripts/visual_regression.py
```

기본 캡처 출력은 `dev/temp/visual-regression/`에 저장되며 커밋하지 않습니다. README나 마켓에 쓰는 대표 이미지만 `screenshots/readme/` 같은 추적 경로로 승격합니다.

문서 정책:
- `docs/`는 로컬 작업 문서가 많아 기본 ignore 대상입니다.
- `scripts/validate_theme.py` 또는 release 안내가 요구하는 문서는 `git add -f`로 명시적으로 추적합니다.
- 추적되는 docs 파일을 추가할 때는 validator guard나 README/dev 문서의 책임 설명도 함께 맞춥니다.

추가 점검:
```bash
# 중괄호 균형 확인
python3 -c "s=open('theme.css').read(); print(s.count('{'), s.count('}'))"

# 볼트 동기화 확인
diff -qr --exclude=.git --exclude=.DS_Store \
  . "/path/to/YourVault/.obsidian/themes/Owen Graphite"
```

### 3. 빌드

```bash
python3 scripts/build_release.py
# → dist/Owen-Graphite-<version>.zip
```

### 4. 커밋 컨벤션

```
<type>: <subject>

<body>
```

Type:
- `feat:` 신규 기능
- `fix:` 버그 수정
- `style:` CSS 디자인 조정
- `docs:` 문서
- `refactor:` 리팩토링 (동작 변화 없음)
- `chore:` 빌드/스크립트/설정
- `Release vX.Y.Z —` 릴리즈 커밋

## 코드 스타일

### CSS 패치 블록 추가 규칙

기존 섹션을 직접 수정하기보다 **EOF 패치 블록**에 추가 오버라이드를 권장합니다 (회귀 위험 최소화).

```css
/* ============================================================================
 * vX.Y.Z — <기능명>
 * <간단 설명>
 * ========================================================================== */

.your-selector {
  property: value !important;
}

/* End of vX.Y.Z ... ======================================================== */
```

### Live Preview 가드

Live Preview (CM6) 편집성을 해치는 다음 규칙은 금지됩니다 (validate가 차단):
- `pointer-events: none` on `.cm-line`
- `user-select: none` on `.cm-content`
- 비대칭 `padding`으로 커서 좌표를 어긋나게 만드는 룰

### Style Settings 옵션 추가

`/* @settings ... */` YAML 블록에 그룹별로 추가하고 변수는 `--ogd-` 접두사를 사용합니다.

## 릴리즈 절차 (메인테이너)

릴리즈 전에는 같은 버전 태그가 이미 있는지 먼저 확인합니다.

```bash
git tag --list "vX.Y.Z"
gh release view vX.Y.Z --json tagName,name,isDraft,isPrerelease,publishedAt
```

```bash
# 1. manifest.json + README + CHANGELOG 버전 동기화
# 2. MAP + 검증 + 빌드
python3 scripts/analyze_theme_css.py
python3 scripts/validate_theme.py
python3 scripts/build_release.py

# 3. 커밋 + 태그 + 푸시
git add -A
git commit -m "Release vX.Y.Z — <subject>"
git tag -a vX.Y.Z -m "Owen Graphite vX.Y.Z"
git push origin main
git push origin vX.Y.Z

# 4. GitHub 릴리즈 (한글 노트는 반드시 --notes-file 사용!)
cat > /tmp/notes.md << 'EOF'
## Highlights
...
EOF
gh release create vX.Y.Z \
  dist/Owen-Graphite-X.Y.Z.zip theme.css manifest.json \
  --title "Owen Graphite vX.Y.Z" \
  --notes-file /tmp/notes.md
```

> **주의**: 한글이 포함된 릴리즈 노트는 shell 더블쿼트 안에서 `\u` 이스케이프가 풀리지 않으므로 반드시 파일로 작성 후 `--notes-file` 옵션을 사용합니다.

## 이슈 / PR

- 버그 신고: 재현 절차 + Obsidian 버전 + OS + 스크린샷
- 기능 제안: 사용 사례와 대안 검토 결과 포함
- PR: 위 검증을 모두 통과해야 머지 가능

## 라이선스

MIT — `LICENSE` 참조.
