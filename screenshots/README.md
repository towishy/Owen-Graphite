# Screenshots

Owen Graphite v3.1.71 마켓플레이스 등록용 스크린샷.

| 파일 | 모드 | 용도 |
| --- | --- | --- |
| `light.png` | Light | README 대표 이미지 (실제 Obsidian 화면) |
| `dark.png` | Dark | README 다크 모드 이미지 |
| `thumbnail.png` | — | 커뮤니티 카탈로그 썸네일 |
| `readme/workspace-chrome-connected-glass.svg` | Workspace chrome | README 연결형 탭·하단 프레임·vault switcher 신기능 이미지 |
| `readme/top-tabs-liquid-glass.svg` | Workspace chrome | README 상단 탭 liquid-glass 신기능 이미지 |
| `readme/owen-knowledge-work-stack.svg` | — | Owen 지식 작업 스택 다이어그램 |
| `readme/owen-ai-document-stack.svg` | — | Owen AI 문서 제작 다이어그램 |
| `readme/pdf-key-value-labels.png` | PDF | README PDF Key/Value 라벨 기능 이미지 |
| `readme/pdf-dual-key-value-header.png` | PDF | README PDF 헤더 Key/Value 2쌍 기능 이미지 |
| `readme/pdf-customer-delivery-feature.png` | Settings / PDF | README PDF 고객 전달용 화면 가시성 신기능 이미지 |
| `readme/pdf-live-preview-parity.png` | PDF | README Live Preview / PDF 품질 패리티 이미지 |
| `readme/code-font-clarity.png` | Live Preview / PDF | README 코드블럭 폰트·색상 패리티 이미지 |
| `readme/file-explorer-type-badges.svg` | File Explorer | README 파일 탐색기 확장자 배지 기능 이미지 |
| `readme/search-focus-rim-liquid-aqua.png` | Settings / Search | README 검색 focus rim 기능 이미지 |
| `readme/sponsor-coffee.svg` | — | 후원 배너 |

> 모든 스크린샷은 익명 샘플 콘텐츠로 제작되어 개인·고객사 식별 정보를 포함하지 않습니다.

## 캡처 가이드

### macOS

1. Obsidian 사이드바 모두 접기 (`⌘ ⌥ ←/→`)
2. `⌘ ⇧ 5` → 창 캡처 → 1280×720 비율로 자르기

### Windows

- `Win + Shift + S` → 영역 캡처

### 권장 크기

- README 대표 이미지는 실제 화면 비율을 유지한 **512px 폭**을 권장합니다.
- 압축은 `pngquant --quality=70-85 screenshots/*.png --ext .png --force`.

## v3 디자인 언어

새 스크린샷을 만들 때는 Owen Graphite Liquid Glass 원칙을 따릅니다.

- Resting state: 흰색/회색 frosted glass, 좌측 vertical rail 금지
- Hover: 살짝 밝아지고 들어올림, wide soft downward shadow, 얕은 pastel 톤
- Active: 선택 문서/탭 등 명확한 상태에만 sky tint + glass border

자세한 원칙은 [../dev/WIKI/DOCS/v3/surface-state-matrix.md](../dev/WIKI/DOCS/v3/surface-state-matrix.md).
