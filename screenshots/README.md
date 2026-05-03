# Screenshots

Owen Graphite 테마의 마켓플레이스 등록용 스크린샷.

| 파일 | 크기 | 모드 | 내용 |
| --- | --- | --- | --- |
| `light.png` | 512×438 | Light | 실제 Obsidian 적용 화면을 축소한 README 대표 이미지 |
| `dark.png` | 512×438 | Dark | 동일 캡처를 기반으로 가공한 다크 모드 대표 이미지 |
| `report.png` | 512×438 | Report | 동일 캡처를 기반으로 가공한 보고서/인쇄 톤 대표 이미지 |
| `snippet-design-8-improvements-preview.png` | 3096×3586 | Concept | Gray override snippet 8개 구조 개선 preview |
| `table-sample.png` | — | Concept | 보고서형 테이블 클래스 디자인 샘플 |

> 모든 스크린샷은 익명 샘플 콘텐츠로 제작되어 개인·고객사 식별 정보가 포함되지 않습니다.

## 재생성 방법

`light.png`는 실제 Obsidian 적용 화면 캡처를 축소해 만듭니다. 원본 캡처가 `dev/temp/light-screenshot.png`에 있으면 그 파일을 사용하고, 없으면 기존 `screenshots/light.png`를 기준으로 `dark.png`와 `report.png`를 다시 가공합니다.

```bash
python -m pip install pillow
python scripts/generate_screenshots.py
```

스크립트는 원본 비율을 유지하면서 가로 512px로 다운스케일합니다.

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

### 권장 크기

- README 대표 이미지는 실제 적용 화면 비율을 유지한 **512px 폭**을 권장합니다.
