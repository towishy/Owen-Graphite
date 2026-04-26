# Screenshots

이 폴더에 다음 PNG 파일을 추가하세요. **Obsidian 공식 community-themes 등록 시 필수**.

| 파일 | 권장 크기 | 내용 |
|------|----------|------|
| `light.png` | 1280×720 (16:9) | Light 모드 일반 노트 (헤더 + 표 + callout 보임) |
| `dark.png` | 1280×720 | Dark 모드 동일 노트 |
| `report.png` | 1280×720 | 보고서 모드 (헤더 자동 넘버링 + 세리프 + 표지) |

## 캡처 가이드

### macOS
1. Obsidian에서 샘플 노트 열기 (예: 헤더 H1~H3 + 표 + callout 한 종류 + 코드블록 한 개)
2. 사이드바를 `⌘ ⌥ ←/→` 으로 모두 접어 본문에 집중
3. `⌘ ⇧ 4` → 영역 선택 캡처 또는 `⌘ ⇧ 5` → 창 캡처
4. 권장: 캡처 후 [ImageOptim](https://imageoptim.com/mac) 또는 `pngquant`로 압축

```bash
pngquant --quality=70-85 light.png --output light.png --force
```

### Windows
- 스니핑 도구 또는 `Win + Shift + S` → 영역 캡처

### 권장 비율
- **16:9** (1280×720, 1920×1080) — Obsidian 공식 권장
- 4:3, 21:9도 허용되지만 16:9가 가장 안전

## 샘플 노트 추천 구조

스크린샷이 다양한 기능을 보여주도록:

```markdown
# 보안 운영 가이드

> [!info] 이 문서의 목적
> 일일 운영 절차와 인시던트 대응 흐름을 정리합니다.

## 1. 일일 점검

### 1.1 알림 검토
- [x] Sentinel 인시던트 큐 확인
- [ ] Defender XDR 알림 분류

### 1.2 주요 지표

| 지표 | 임계 | 어제 | 추세 |
|------|-----:|-----:|:----:|
| MDE 알림 | 50 | 42 | ↘ |
| MDI 탐지 | 10 | 7 | → |

> [!warning] 주의
> SIEM 라이선스가 다음 주 만료됩니다.

```python
def alert_handler(incident):
    if incident.severity == "high":
        notify(incident)
```

`<kbd>⌘ K</kbd>` — 명령 팔레트 열기.
```

이런 노트로 캡처하면 헤더, callout, 표, 체크박스, kbd, 코드블록 모두 한 화면에 담깁니다.
