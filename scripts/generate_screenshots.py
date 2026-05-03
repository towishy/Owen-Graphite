"""
Generate README screenshots from the real Obsidian capture.

The light screenshot is a resized copy of dev/temp/light-screenshot.png.
The dark screenshot is derived from the same pixels so layout, alignment,
and content stay identical between modes.
The report screenshot keeps the same capture layout with a quieter print-like
paper tone.
"""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageEnhance, ImageOps

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "screenshots"
OUT_DIR.mkdir(parents=True, exist_ok=True)
SOURCE_CANDIDATES = [
    ROOT / "dev" / "temp" / "light-screenshot.png",
    OUT_DIR / "light.png",
]

TARGET_WIDTH = 512


def resize_to_width(image: Image.Image, width: int = TARGET_WIDTH) -> Image.Image:
    ratio = width / image.width
    height = round(image.height * ratio)
    return image.resize((width, height), Image.Resampling.LANCZOS)


def darken_from_light(image: Image.Image) -> Image.Image:
    source = image.convert("RGB")
    gray = ImageOps.grayscale(source)
    neutral_dark = ImageOps.colorize(
        gray,
        black=(235, 241, 248),
        white=(19, 29, 43),
        mid=(64, 78, 101),
    ).convert("RGB")

    src = source.load()
    dst = neutral_dark.load()
    width, height = source.size

    for y in range(height):
        for x in range(width):
            red, green, blue = src[x, y]
            luma = int(0.2126 * red + 0.7152 * green + 0.0722 * blue)
            base_red, base_green, base_blue = dst[x, y]

            is_red = red > green + 22 and red > blue + 18
            is_cyan = blue > red + 16 and green > red - 4
            is_light_surface = luma > 238 and abs(red - green) < 12 and abs(green - blue) < 16
            is_soft_surface = 205 < luma <= 238 and abs(red - green) < 18 and abs(green - blue) < 22

            if is_light_surface:
                dst[x, y] = (21, 31, 46)
            elif is_soft_surface:
                dst[x, y] = (30, 42, 60)
            elif is_red:
                if luma > 180:
                    dst[x, y] = (82, 48, 56)
                else:
                    dst[x, y] = (248, 128, 128)
            elif is_cyan:
                if luma > 188:
                    dst[x, y] = (31, 51, 70)
                else:
                    dst[x, y] = (130, 211, 246)
            elif luma < 96:
                dst[x, y] = (236, 242, 250)
            else:
                dst[x, y] = (
                    min(255, int(base_red * 1.02)),
                    min(255, int(base_green * 1.02)),
                    min(255, int(base_blue * 1.04)),
                )

    return ImageEnhance.Contrast(neutral_dark).enhance(1.04)


def report_from_light(image: Image.Image) -> Image.Image:
    source = image.convert("RGB")
    softened = ImageEnhance.Color(source).enhance(0.72)
    softened = ImageEnhance.Contrast(softened).enhance(1.03)

    src = source.load()
    dst = softened.load()
    width, height = source.size

    for y in range(height):
        for x in range(width):
            red, green, blue = src[x, y]
            luma = int(0.2126 * red + 0.7152 * green + 0.0722 * blue)

            is_red = red > green + 22 and red > blue + 18
            is_cyan = blue > red + 16 and green > red - 4
            is_light_surface = luma > 238 and abs(red - green) < 12 and abs(green - blue) < 16
            is_soft_surface = 205 < luma <= 238 and abs(red - green) < 18 and abs(green - blue) < 22

            if is_light_surface:
                dst[x, y] = (255, 255, 253)
            elif is_soft_surface:
                dst[x, y] = (246, 248, 250)
            elif is_red:
                if luma > 180:
                    dst[x, y] = (253, 243, 243)
                else:
                    dst[x, y] = (190, 65, 65)
            elif is_cyan:
                if luma > 188:
                    dst[x, y] = (247, 251, 253)
                else:
                    dst[x, y] = (84, 116, 145)
            elif luma < 110:
                dst[x, y] = (28, 35, 47)

    return ImageEnhance.Sharpness(softened).enhance(1.05)


def main() -> int:
    source_path = next((path for path in SOURCE_CANDIDATES if path.exists()), None)
    if source_path is None:
        candidates = ", ".join(str(path) for path in SOURCE_CANDIDATES)
        print(f"[ERROR] Source screenshot not found. Tried: {candidates}", file=sys.stderr)
        return 1

    with Image.open(source_path) as original:
        light = resize_to_width(original.convert("RGB"))

    light_path = OUT_DIR / "light.png"
    light.save(light_path, "PNG", optimize=True)

    dark = darken_from_light(light)
    dark_path = OUT_DIR / "dark.png"
    dark.save(dark_path, "PNG", optimize=True)

    report = report_from_light(light)
    report_path = OUT_DIR / "report.png"
    report.save(report_path, "PNG", optimize=True)

    print(f"[OK] source -> {source_path}")
    print(f"[OK] light -> {light_path} ({light.width}x{light.height}, {light_path.stat().st_size // 1024} KB)")
    print(f"[OK] dark -> {dark_path} ({dark.width}x{dark.height}, {dark_path.stat().st_size // 1024} KB)")
    print(f"[OK] report -> {report_path} ({report.width}x{report.height}, {report_path.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
