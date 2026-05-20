# v3 Release Notes Workflow

릴리스 노트의 진본은 [CHANGELOG.md](../../CHANGELOG.md)의 최신 `## vX.Y.Z` 섹션입니다. GitHub Release 본문, 커뮤니티 제출 설명, README 최신 기능 소개는 이 섹션을 기준으로 작성합니다.

## 자동 생성

```powershell
python dev/scripts/build_release_notes.py
python dev/scripts/build_release_notes.py --output dist/release-notes-v<version>.md
```

스크립트는 `manifest.json`의 version과 CHANGELOG 최신 섹션이 일치하는지 확인하고, 최신 섹션만 추출해 Markdown release note로 출력합니다.

## 작성 기준

| 섹션 | 포함 내용 |
| --- | --- |
| Highlights | 사용자 체감 기능, 문서 개선, 검증 강화 |
| Validation | release check, ZIP audit, Style Settings contract, docs/assets audit |
| Install note | 수동 설치 시 `Owen-Graphite-<version>.zip` 사용 안내 |

## README와의 관계

- README의 최신 기능 소개는 3개만 유지합니다.
- 오래된 기능은 [feature-history.md](feature-history.md)로 이동합니다.
- 릴리스 노트는 changelog 기반이고, README는 사용자 진입용 설명입니다. 같은 내용을 중복하더라도 README는 더 짧게 유지합니다.