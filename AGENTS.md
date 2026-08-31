# Owen Graphite Agent Instructions

이 저장소는 Obsidian용 Owen Graphite liquid-glass theme 프로젝트다.

## Knowledge Source

VS Code에서는 이 프로젝트와 `C:\OWEN\github\wiki`를 멀티 루트 워크스페이스로 함께 연다.

- `C:\OWEN\github\wiki`를 디자인·지식 참고 루트로 상시 취급한다.
- UI/UX, 접근성, 반응형 또는 컴포넌트 작업 전 `lib/ui-foundation/`, `lib/ui-lab/src/`, 관련 `lib/ui-foundation/REFERENCE-STUDY-*.md`를 작업 용어로 검색하고 해당 소스를 확인한다.
- 사용자가 명시적으로 요청하지 않으면 `C:\OWEN\github\wiki`의 파일은 읽기 전용으로 유지한다.
- `C:\OWEN\github\wiki`에 접근할 수 없으면 추측으로 대체하지 않고, 검증하지 못한 사실을 완료 보고에 명시한다.

Owen Graphite, Obsidian 문서, SVG, PDF, UI 디자인 관련 작업은 wiki를 먼저 참조한다.

```powershell
Push-Location C:\OWEN\github\wiki
.\.venv\Scripts\python.exe scripts\wiki-query.py "Owen Graphite Liquid Glass Obsidian" --limit 7 --json
Pop-Location
```

<!-- ui-portal-usage:start -->
## Owen UI Portal 사용

- UI/UX, frontend, component, 접근성, 반응형 또는 시각 자산 작업을 계획하거나 편집하기 전 companion WIKI의 UI Portal을 task-specific 자산 선택의 기본 라우터로 사용한다.
- WIKI 루트는 멀티루트 workspace의 `wiki`, sibling `../wiki`, 현재 플랫폼의 알려진 WIKI 경로 순서로 찾으며 하나의 절대 경로만 가정하지 않는다.
- 구현용 선택은 WIKI 루트에서 `node scripts/ui-portal/query-assets.mjs brief "<한 문장의 output job>" --limit 5`를 실행하고 Task Profile, Context Pack, exact Asset ID, `ownerPath`/`ownerApi`, maturity와 validation을 확인한다. broad Registry를 모델 컨텍스트에 넣거나 Asset ID를 추측하지 않는다.
- 시각 검토는 WIKI의 `process: UI Portal Controller`를 실행·재사용하고 VS Code 내장 브라우저에서 `/uiportal query="<작업>"` 또는 `http://127.0.0.1:4172/portal/`을 연다.
- Portal은 라우팅·증거 surface이고 Foundation의 `DESIGN.md`와 owning source가 최종 계약이다. WIKI는 명시적 요청이 없으면 읽기 전용으로 유지하며, 접근할 수 없으면 미검증 범위를 보고한다.
<!-- ui-portal-usage:end -->

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

<!-- ui-foundation-design-guide:start -->
## UI Foundation Lab 디자인 가이드

- 모든 UI 설계·구현 전에 [UI-FOUNDATION-DESIGN-GUIDE.md](UI-FOUNDATION-DESIGN-GUIDE.md)를 먼저 읽는다.
- UI Foundation Lab 왼쪽 패널의 26개 UI를 모두 `Priority 1` 디자인 후보로 취급한다.
- `Priority 1` 안에서는 Clear glass search, controls, workflow를 가장 먼저 검토한다.
- 나머지 Lab specimen을 검토한 뒤에만 앱 전용 신규 디자인이나 외부 reference를 고려한다.
- 이 프로젝트의 기존 제품 제약과 더 엄격한 접근성·runtime 규칙은 그대로 유지한다.
<!-- ui-foundation-design-guide:end -->
