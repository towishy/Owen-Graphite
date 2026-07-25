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
디자인/프론트엔드 작업을 시작하기 전 `C:\OWEN\github\wiki\lib\ui-foundation`의 `README.md`, `DESIGN.md`, `tokens/`, `src/` 컴포넌트 계약을 읽고 현재 프로젝트에 맞게 적용한다.

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

- Owen Graphite Style Settings의 사용자 노출 metadata 기본 언어는 영어(`en`)다.
- Style Settings 기능을 추가하거나 변경할 때 section title, setting label, description의 영어 기본값과 한국어(`title.ko`/`description.ko`)를 같은 변경에서 함께 구현한다.
- Style Settings가 locale별 option label을 지원하지 않으므로 언어별 표기가 필요한 option label은 간결한 영어/한국어 병기로 제공한다.
- setting ID, CSS variable/class, default value namespace, 저장된 machine value는 번역하지 않는다.
- `ogd-style-settings-language`는 Obsidian locale 자동 추종과 한국어/English 명시 선택을 제공한다. Style Settings 1.0.9의 legacy locale 키가 비어 native metadata 선택이 실패하면 `compat/owen-graphite-style-settings-l10n` bridge만 Owen Graphite 행을 현지화한다.
- localization bridge는 Style Settings `data.json`이나 setting ID, CSS class, default, machine value를 수정하지 않는다.
- 영어/한국어 metadata completeness, option coverage, 영어 fallback과 기존 저장값 호환성을 자동 검사에 포함한다.
- 테마 schema를 빌드·검증하고 실제 Obsidian에서 영어/한국어 locale과 overflow를 확인한 뒤 릴리스한다.
