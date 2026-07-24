# Owen Graphite Agent Instructions

이 저장소는 Obsidian용 Owen Graphite liquid-glass theme 프로젝트다.

## Knowledge Source

VS Code에서는 이 프로젝트와 `C:\OWEN\github\wiki`를 멀티 루트 워크스페이스로 함께 연다.

Owen Graphite, Obsidian 문서, SVG, PDF, UI 디자인 관련 작업은 wiki를 먼저 참조한다.

```powershell
Push-Location C:\OWEN\github\wiki
.\.venv\Scripts\python.exe scripts\wiki-query.py "Owen Graphite Liquid Glass Obsidian" --limit 7 --json
Pop-Location
```

## UI Direction

UI 작업 전 sibling workspace folder `wiki`의 `wiki/concepts/ui-design-system-knowledge.md`를 우선 참조한다.

기본 조합:

- Extend-UI / shadcn component structure
- Owen Graphite Liquid Glass visual surface
- Reicon for richer icon options
- Border Beam only for focused emphasis
- Boneyard only for data-heavy app skeleton loading

이 저장소에서는 Owen Graphite 자체가 canonical visual system이다. 외부 UI 리소스는 theme identity를 보완할 때만 참고한다.

## Local Rules

- `!important` 남발 금지. cascade/token-first 원칙을 우선한다.
- Live Preview, Reading View, PDF export parity를 고려한다.
- Obsidian DOM/computed style 확인이 필요한 변경은 CDP remote debugging으로 실제 selector를 검증한다.
- README용 이미지와 SVG는 한글 안전 폰트, overflow 검증, 다크모드 대응을 확인한다.
- release 관련 변경은 README, CHANGELOG, visual evidence를 함께 확인한다.

## Localization Contract

- Owen Graphite와 호환 companion의 사용자 노출 UI 기본 언어는 영어(`en`)다.
- Style Settings 기능을 추가하거나 변경할 때 section title, setting label, description, option label, 검색·가져오기·내보내기 chrome의 영어와 한국어(`ko`)를 같은 변경에서 함께 구현한다.
- setting ID, CSS variable/class, default value namespace, 저장된 machine value는 번역하지 않는다.
- 기본 preference는 `ogd-language-auto`다. Obsidian locale이 `ko` 계열이면 한국어, 그 외에는 영어를 사용하며, 기존 `ogd-language-en`/`ogd-language-ko` 저장값은 명시적 override로 우선한다.
- 영어/한국어 catalog completeness, option coverage, 영어 fallback, 자동 locale 해석, override 우선순위, 기존 저장값 호환성을 자동 검사에 포함한다.
- 테마 schema와 locale companion을 함께 빌드·검증하고 실제 Obsidian에서 두 언어 전환과 overflow를 확인한 뒤 릴리스한다.
