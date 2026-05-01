"""
Owen Graphite v2.22.21 marketing screenshot generator (pure Pillow).

Renders three 1280x720 PNG mock-ups (light / dark / report) showcasing
the neutral liquid-glass baseline: graphite/gray frosted chrome at rest,
shallow sky rim/line only on selected or hovered workspace controls, report
layout parity, and stable readable content. Then downscales to 512x288 for
the marketplace listing.

Pure Pillow, no SVG. Uses Windows-installed Malgun Gothic for Korean
and Batang for serif (report mode).
"""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

OUT_DIR = Path(__file__).resolve().parent.parent / "screenshots"
OUT_DIR.mkdir(parents=True, exist_ok=True)

W, H = 1280, 720
THUMB = (512, 288)

FONT_DIRS = [
    Path(r"C:\Windows\Fonts"),
    Path("/System/Library/Fonts"),
    Path("/System/Library/Fonts/Supplemental"),
    Path("/Library/Fonts"),
]


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    for font_dir in FONT_DIRS:
        candidate = font_dir / name
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default(size=size)


def fonts(size: int, weight: str = "regular", serif: bool = False) -> ImageFont.FreeTypeFont:
    if serif:
        for f in ["batang.ttc", "NanumMyeongjo.ttf", "AppleMyungjo.ttf", "Songti.ttc", "Times New Roman.ttf"]:
            for font_dir in FONT_DIRS:
                if (font_dir / f).exists():
                    return font(f, size)
        return font("malgun.ttf", size)
    mac_regulars = ["AppleSDGothicNeo.ttc", "Arial Unicode.ttf", "Arial Unicode MS.ttf"]
    mac_bolds = ["AppleSDGothicNeo.ttc", "Arial Bold.ttf"]
    if weight == "bold":
        for f in ["malgunbd.ttf", *mac_bolds]:
            for font_dir in FONT_DIRS:
                if (font_dir / f).exists():
                    return font(f, size)
        return font("malgunbd.ttf", size)
    for f in ["malgun.ttf", *mac_regulars]:
        for font_dir in FONT_DIRS:
            if (font_dir / f).exists():
                return font(f, size)
    return font("malgun.ttf", size)


PALETTES = {
    "light": {
        "bg": (248, 250, 252),
        "panel": (255, 255, 255),
        "panel_alt": (241, 245, 249),
        "ribbon_bg": (226, 232, 240),
        "border": (226, 232, 240),
        "border_strong": (203, 213, 225),
        "text": (15, 23, 42),
        "text_muted": (71, 85, 105),
        "text_dim": (148, 163, 184),
        "accent": (14, 165, 233),
        "accent_dark": (7, 89, 133),
        "accent_soft": (224, 242, 254),
        "h1": (15, 23, 42),
        "callout_bg": (236, 254, 255),
        "callout_border": (6, 182, 212),
        "table_head": (241, 245, 249),
        "table_zebra": (248, 250, 252),
        "tab_active": (255, 255, 255),
        "tab_idle": (226, 232, 240),
        "glass_top": (255, 255, 255),
        "glass_bot": (241, 245, 249),
        "glass_border": (148, 163, 184),
        "shadow_alpha": 36,
    },
    "dark": {
        "bg": (15, 23, 42),
        "panel": (30, 41, 59),
        "panel_alt": (15, 23, 42),
        "ribbon_bg": (11, 18, 32),
        "border": (30, 41, 59),
        "border_strong": (51, 65, 85),
        "text": (248, 250, 252),
        "text_muted": (203, 213, 225),
        "text_dim": (100, 116, 139),
        "accent": (56, 189, 248),
        "accent_dark": (186, 230, 253),
        "accent_soft": (12, 74, 110),
        "h1": (248, 250, 252),
        "callout_bg": (12, 74, 110),
        "callout_border": (34, 211, 238),
        "table_head": (30, 41, 59),
        "table_zebra": (23, 32, 51),
        "tab_active": (30, 41, 59),
        "tab_idle": (11, 18, 32),
        "glass_top": (51, 65, 85),
        "glass_bot": (15, 23, 42),
        "glass_border": (203, 213, 225),
        "shadow_alpha": 110,
    },
    "report": {
        "bg": (255, 255, 255),
        "panel": (255, 255, 255),
        "panel_alt": (248, 250, 252),
        "ribbon_bg": (226, 232, 240),
        "border": (229, 231, 235),
        "border_strong": (203, 213, 225),
        "text": (17, 24, 39),
        "text_muted": (55, 65, 81),
        "text_dim": (156, 163, 175),
        "accent": (14, 165, 233),
        "accent_dark": (7, 89, 133),
        "accent_soft": (224, 242, 254),
        "h1": (17, 24, 39),
        "callout_bg": (250, 250, 249),
        "callout_border": (107, 114, 128),
        "table_head": (243, 244, 246),
        "table_zebra": (249, 250, 251),
        "tab_active": (255, 255, 255),
        "tab_idle": (229, 231, 235),
        "glass_top": (255, 255, 255),
        "glass_bot": (241, 245, 249),
        "glass_border": (148, 163, 184),
        "shadow_alpha": 42,
    },
}


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def vgradient(img, x, y, w, h, top, bot):
    band = Image.new("RGB", (1, h))
    for j in range(h):
        band.putpixel((0, j), lerp(top, bot, j / max(1, h - 1)))
    band = band.resize((w, h), Image.BILINEAR)
    img.paste(band, (x, y))


def rounded_glass(img, x, y, w, h, p, hovered=False, radius=6):
    if hovered:
        sh = Image.new("RGBA", (w + 24, h + 24), (0, 0, 0, 0))
        ImageDraw.Draw(sh).rounded_rectangle(
            (12, 14, 12 + w, 14 + h), radius=radius + 1,
            fill=(20, 25, 40, p["shadow_alpha"]))
        sh = sh.filter(ImageFilter.GaussianBlur(6))
        img.paste(sh, (x - 12, y - 12), sh)
        y -= 1

    glass = Image.new("RGB", (w, h), p["glass_bot"])
    vgradient(glass, 0, 0, w, h, p["glass_top"], p["glass_bot"])
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, w - 1, h - 1), radius=radius, fill=255)
    img.paste(glass, (x, y), mask)

    od = ImageDraw.Draw(img)
    od.rounded_rectangle((x, y, x + w - 1, y + h - 1), radius=radius,
                         outline=p["glass_border"], width=1)
    hl = Image.new("L", (w, h), 0)
    ImageDraw.Draw(hl).rounded_rectangle((1, 1, w - 2, h // 2), radius=radius - 1, fill=110)
    overlay = Image.new("RGB", (w, h), p["glass_top"])
    img.paste(overlay, (x, y), hl)


def toggle(img, x, y, p, enabled=True):
    od = ImageDraw.Draw(img)
    rounded_glass(img, x, y, 48, 26, p, hovered=False, radius=13)
    if enabled:
        od.rounded_rectangle((x, y, x + 47, y + 25), radius=13,
                             fill=lerp(p["accent"], p["panel"], 0.28),
                             outline=p["glass_border"], width=1)
        cx = x + 34
    else:
        cx = x + 14
    od.ellipse((cx - 10, y + 3, cx + 10, y + 23), fill=p["glass_top"], outline=p["border_strong"], width=1)
    od.arc((cx - 6, y + 7, cx + 6, y + 19), start=210, end=510, fill=p["accent_dark"], width=2)


def text(d, x, y, s, sz, color, weight="regular", serif=False):
    d.text((x, y), s, font=fonts(sz, weight=weight, serif=serif), fill=color)


def render_variant(variant):
    p = PALETTES[variant]
    is_report = variant == "report"
    serif = is_report

    img = Image.new("RGB", (W, H), p["bg"])
    d = ImageDraw.Draw(img)

    # Title bar
    d.rectangle((0, 0, W, 36), fill=p["panel"], outline=p["border"])
    for i, c in enumerate([(251, 113, 133), (251, 191, 36), (52, 211, 153)]):
        d.ellipse((14 + i * 16, 12, 26 + i * 16, 24), fill=c)
    text(d, 80, 12, "Owen Graphite — Sample Report", 12, p["text_muted"])

    rounded_glass(img, W - 78, 8, 24, 22, p, hovered=True)
    od = ImageDraw.Draw(img)
    od.rounded_rectangle((W - 72, 13, W - 60, 25), radius=2, outline=p["text_muted"], width=1)
    od.line((W - 67, 13, W - 67, 25), fill=p["text_muted"], width=1)

    rounded_glass(img, W - 46, 8, 24, 22, p, hovered=False)
    od = ImageDraw.Draw(img)
    od.rounded_rectangle((W - 40, 13, W - 28, 25), radius=2, outline=p["text_muted"], width=1)

    ribbon_w = 56
    od = ImageDraw.Draw(img)
    od.rectangle((0, 36, ribbon_w, H), fill=p["ribbon_bg"], outline=p["border"])
    for i, hovered in enumerate([False, True, False, False, False]):
        iy = 56 + i * 44
        rounded_glass(img, 12, iy, 32, 32, p, hovered=hovered)
        od2 = ImageDraw.Draw(img)
        cx, cy = 28, iy + 16
        od2.ellipse((cx - 6, cy - 6, cx + 6, cy + 6), outline=p["text_muted"], width=2)
        od2.line((cx - 4, cy, cx + 4, cy), fill=p["text_muted"], width=2)

    fx, fw = ribbon_w, 220
    od = ImageDraw.Draw(img)
    od.rectangle((fx, 36, fx + fw, H), fill=p["panel"], outline=p["border"])
    text(d, fx + 16, 46, "FILES", 11, p["text_dim"], weight="bold")
    files = [
        ("Reports", True, False, False),
        ("  FY26", True, False, False),
        ("  POSCO - MDA.md", False, True, False),
        ("  Board Brief.md", False, False, False),
        ("Research Notes", True, False, True),
        ("  Reading List.md", False, False, False),
        ("Archive", False, False, False),
    ]
    for i, (name, bold, active, hover) in enumerate(files):
        ty = 80 + i * 30
        if active:
            rounded_glass(img, fx + 8, ty - 4, fw - 16, 26, p, hovered=True, radius=6)
            od.line((fx + 28, ty + 20, fx + fw - 24, ty + 20), fill=lerp(p["accent"], p["border_strong"], 0.42), width=2)
        elif hover:
            rounded_glass(img, fx + 8, ty - 4, fw - 16, 26, p, hovered=False, radius=6)
        weight = "bold" if (bold or active) else "regular"
        color = p["text"] if (bold or active or hover) else p["text_muted"]
        text(d, fx + 18, ty, name, 12, color, weight=weight)

    tx = fx + fw
    tab_h = 36
    od = ImageDraw.Draw(img)
    od.rectangle((tx, 36, W, 36 + tab_h), fill=p["tab_idle"], outline=p["border"])
    od.rounded_rectangle((tx + 8, 40, tx + 228, 36 + tab_h - 4), radius=6,
                         fill=p["tab_active"], outline=p["border_strong"], width=1)
    text(d, tx + 22, 46, "q2-security-report.md", 12, p["text"], weight="bold")
    text(d, tx + 240, 46, "+", 16, p["text_muted"], weight="bold")
    rounded_glass(img, tx + 360, 42, 240, 24, p, hovered=True)
    text(d, tx + 372, 47, "outputs / q2 / report", 11, p["text_muted"])

    ex, ey = tx, 36 + tab_h
    ew = W - ex
    od = ImageDraw.Draw(img)
    od.rectangle((ex, ey, W, H), fill=p["panel"])

    if not is_report:
        bar_x, bar_y = ex + 88, ey + 12
        bar_w, bar_h = ew - 104, 32
        rounded_glass(img, bar_x, bar_y, bar_w, bar_h, p, hovered=False, radius=8)
        labels = ["B", "I", "U", "H", "<>", "❝"]
        for i, hovered in enumerate([False, False, True, False, False, False]):
            bx = bar_x + 12 + i * 36
            rounded_glass(img, bx, bar_y + 4, 24, 24, p, hovered=hovered)
            text(d, bx + 7, bar_y + 8, labels[i], 11, p["text_muted"], weight="bold")
        body_top = ey + 76
    else:
        od.rectangle((ex + 80, ey + 36, ex + 83, ey + 116), fill=p["border_strong"])
        text(d, ex + 96, ey + 36, "PREPARED BY", 9, p["text_dim"], weight="bold")
        text(d, ex + 96, ey + 50, "Security Office", 12, p["text"], weight="bold", serif=serif)
        text(d, ex + 96, ey + 76, "CONFIDENTIAL", 9, p["text_dim"], weight="bold")
        text(d, ex + 96, ey + 90, "Q2 2026 Review", 12, p["text"], weight="bold", serif=serif)
        body_top = ey + 144

    h1_text = "1. Q2 보안 검토" if is_report else "Owen Graphite"
    h1_x = ex + 80
    text(d, h1_x, body_top, h1_text, 30, p["h1"], weight="bold", serif=serif)
    rule_y = body_top + 44
    rule_w = 320
    for i in range(rule_w):
        c = lerp(p["accent_dark"], p["accent"], i / rule_w)
        d.line((h1_x + i, rule_y, h1_x + i, rule_y + 2), fill=c)

        sub = ("보고서 모드 · A3 가로 · 자동 넘버링 · 세리프 본문" if is_report
            else "Neutral glass chrome · Active path · Live Preview parity")
    text(d, h1_x, rule_y + 14, sub, 13, p["text_muted"], serif=serif)

    body_y = rule_y + 50
    body_lines = [
        "그래파이트 톤의 neutral liquid-glass 테마. 반복해서 보는 chrome은",
        "회색 frosted glass로 쉬게 두고, hover/active에서만 얕은 rim과 shadow를",
        "더해 현재 위치와 조작 대상을 조용하게 드러냅니다.",
    ]
    for i, line in enumerate(body_lines):
        text(d, h1_x, body_y + i * 22, line, 13, p["text"], serif=serif)

    cy = body_y + 80
    cw = ew - 160
    od.rounded_rectangle((h1_x, cy, h1_x + cw, cy + 56), radius=6,
                         fill=p["callout_bg"], outline=p["callout_border"], width=1)
    od.rectangle((h1_x, cy, h1_x + 3, cy + 56), fill=p["callout_border"])
    text(d, h1_x + 14, cy + 6, "💡  CONCLUSION", 11, p["callout_border"], weight="bold")
    text(d, h1_x + 14, cy + 28, "PDF 첫 페이지 헤더와 자동 넘버링이 정합 상태로 유지됩니다.",
         12, p["text"], serif=serif)

    ty = cy + 76
    th_h = 28
    row_h = 28
    od.rectangle((h1_x, ty, h1_x + cw, ty + th_h), fill=p["table_head"],
                 outline=p["border_strong"])
    headers = ["항목", "정책", "점수"]
    col_x = [h1_x + 16, h1_x + 220, h1_x + cw - 80]
    for cx, hdr in zip(col_x, headers):
        text(d, cx, ty + 6, hdr, 11, p["text_muted"], weight="bold")
    rows = [
        ("Baseline", "v2.22.21 롤백 기준", "Stable"),
        ("Active path", "선택 문서 · 포함 폴더", "Glass"),
        ("PDF 첫 페이지 헤더", "Side Bar + Two-line", "Ready"),
    ]
    for i, row in enumerate(rows):
        ry = ty + th_h + i * row_h
        bg = p["table_zebra"] if i % 2 == 0 else p["panel"]
        od.rectangle((h1_x, ry, h1_x + cw, ry + row_h), fill=bg, outline=p["border"])
        for cx, val in zip(col_x, row):
            text(d, cx, ry + 6, val, 11, p["text"], serif=serif)

    if not is_report:
        px, py = h1_x + cw - 246, body_y + 18
        rounded_glass(img, px, py, 224, 142, p, hovered=True, radius=10)
        text(d, px + 14, py + 12, "Command Palette", 12, p["text"], weight="bold")
        od.rounded_rectangle((px + 14, py + 34, px + 210, py + 58), radius=6,
                             fill=p["panel_alt"], outline=p["border_strong"], width=1)
        text(d, px + 24, py + 39, "Search command...", 10, p["text_dim"])
        rounded_glass(img, px + 12, py + 68, 200, 26, p, hovered=True, radius=6)
        text(d, px + 24, py + 74, "Toggle glass intensity", 10, p["text"])
        od.line((px + 24, py + 92, px + 146, py + 92), fill=lerp(p["accent"], p["border_strong"], 0.45), width=2)
        text(d, px + 24, py + 104, "Settings glass", 10, p["text_muted"])
        toggle(img, px + 154, py + 99, p, enabled=True)

    od.rectangle((ribbon_w, H - 28, W, H), fill=p["panel_alt"], outline=p["border"])
    text(d, ribbon_w + 16, H - 22, f"Owen Graphite 2.22.21  ·  {variant.title()} mode",
         11, p["text_dim"])

    big_path = OUT_DIR / f"_big-{variant}.png"
    img.save(big_path, "PNG", optimize=True)
    final = OUT_DIR / f"{variant}.png"
    with Image.open(big_path) as im:
        im = im.convert("RGB").resize(THUMB, Image.LANCZOS)
        im.save(final, "PNG", optimize=True)
    big_path.unlink(missing_ok=True)
    return final


def main():
    for v in ["light", "dark", "report"]:
        out = render_variant(v)
        print(f"[OK] {v} -> {out}  ({out.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
