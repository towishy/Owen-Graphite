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
