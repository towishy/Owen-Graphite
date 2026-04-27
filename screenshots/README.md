# Screenshots

Owen Graphite 테마의 마켓플레이스 등록용 스크린샷.

| 파일 | 크기 | 모드 | 내용 |
|------|------|------|------|
| `light.png` | 512×288 (16:9) | Light | v1.8.42 기준: Liquid-glass ribbon·toggle hover·nav active·breadcrumb·editing toolbar·search options·floating UI·callout·table |
| `dark.png`  | 512×288 (16:9) | Dark | 동일 레이아웃 다크 모드, slate gradient + cyan accent |
| `report.png`| 512×288 (16:9) | Report | 보고서 모드 (자동 넘버링 + Side Bar 헤더 + serif 본문) |
| `snippet-design-8-improvements-preview.png` | 3096×3586 | Concept | Gray override snippet 8개 구조 개선 preview |
| `table-sample.png` | — | Concept | 보고서형 테이블 클래스 디자인 샘플 |

> 모든 스크린샷은 익명 샘플 콘텐츠로 제작되어 개인·고객사 식별 정보가 포함되지 않습니다.

## 재생성 방법

v1.8.42 기준 mock-up 이미지는 Pillow로 직접 렌더링합니다. 한글은 Windows 기본 설치 Malgun Gothic 사용.

```bash
python -m pip install pillow
python scripts/generate_screenshots.py
```

스크립트는 1280×720 원본을 렌더링하고 LANCZOS로 512×288에 다운스케일합니다.

### 이전 SVG 기반 렌더러 (deprecated)

원본 SVG는 별도 작업 폴더에 보관되어 있으며, `cairosvg`로 PNG 변환합니다.

```bash
python3 -m pip install cairosvg
for n in light dark report; do
  python3 -c "
import cairosvg
cairosvg.svg2png(
    url=f'owen-graphite-screenshot-{n}.svg'.replace('{n}', '$n'),
    write_to=f'screenshots/{n}.png'.replace('{n}', '$n'),
    output_width=512, output_height=288)
"
done
```

또는 macOS에서 librsvg 사용:

```bash
brew install librsvg
rsvg-convert -w 512 -h 288 owen-graphite-screenshot-light.svg -o screenshots/light.png
```

### 압축 (선택)

```bash
brew install pngquant
pngquant --quality=70-85 screenshots/*.png --ext .png --force
```

## 직접 캡처하고 싶다면

### macOS
1. Obsidian 사이드바 모두 접기 (`⌘ ⌥ ←/→`)
2. `⌘ ⇧ 5` → 창 캡처 → 1280×720 비율로 자르기

### Windows
- `Win + Shift + S` → 영역 캡처

### 권장 비율
- **16:9** (512×288 lightweight preview, 1280×720 full preview)
