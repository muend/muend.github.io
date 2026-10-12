#!/usr/bin/env python3
"""Emit assets/brand/share-card.png, the default link-preview image.

Same drawing as the GitHub profile banner, set on the site's paper colour at
1200x630. Pages with their own picture (a film poster) name it in
shell.OG_IMAGES instead. Needs Pillow and the Windows system fonts; the PNG is
committed, so the site build itself stays dependency-free.
"""
import pathlib

from PIL import Image, ImageDraw, ImageFont

W, H, S = 1200, 630, 2          # drawn at 2x, then downsampled for clean edges

PAPER, INK, SOFT, MUTE = "#F7F7F1", "#1A221C", "#454D47", "#5B635D"
HAIR, GREEN, AMBER = "#C7D2C9", "#06713F", "#96610F"

FONTS = pathlib.Path("C:/Windows/Fonts")


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size * S)


BOLD = font("segoeuib.ttf", 78)
SEMI = font("seguisb.ttf", 27)
MONO = font("consola.ttf", 15)
MONO_S = font("consola.ttf", 14)

img = Image.new("RGB", (W * S, H * S), PAPER)
d = ImageDraw.Draw(img)


def line(x1, y1, x2, y2, fill, width=1):
    d.line([(x1 * S, y1 * S), (x2 * S, y2 * S)], fill=fill, width=width * S)


def spaced(x, y, text, fnt, fill, gap, anchor="l"):
    """Draw text with letter spacing; Pillow has none of its own."""
    widths = [d.textlength(ch, font=fnt) / S for ch in text]
    total = sum(widths) + gap * (len(text) - 1)
    cx = x - total if anchor == "r" else x
    for ch, w in zip(text, widths):
        d.text((cx * S, y * S), ch, font=fnt, fill=fill)
        cx += w + gap


M, RIGHT = 84, 1116

# hairlines
line(0, 78, W, 78, HAIR)
line(0, 560, W, 560, HAIR)
line(M - 26, 0, M - 26, H, HAIR)

# masthead
spaced(M, 36, "SYSTEMS INDEX", MONO, GREEN, 6)
spaced(RIGHT, 36, "MEASURED BEFORE TRUSTED  /  2026", MONO, MUTE, 3, anchor="r")

# name + role
d.text(((M - 4) * S, 150 * S), "Muhammed Enes Duran", font=BOLD, fill=INK)
d.text((M * S, 262 * S), "AI engineer \u00b7 LLM evaluation \u00b7 agent systems \u00b7 MCP tooling",
       font=SEMI, fill=SOFT)

# work ruler
RULE_Y, SPAN = 452, 820
TICKS = ["LLM EVALUATION", "AGENT SKILLS", "MCP", "PYTORCH", "RUST"]
line(M, RULE_Y, M + SPAN, RULE_Y, HAIR)
for i, label in enumerate(TICKS):
    x = M + SPAN / (len(TICKS) - 1) * i
    line(x, RULE_Y, x, RULE_Y + 11, GREEN if i == 0 else MUTE, 2 if i == 0 else 1)
    spaced(x, RULE_Y + 22, label, MONO_S, MUTE, 2.4)

# interval plot: wins clear of zero, nulls across it, one loss
PX0, PX1, ZERO, Y0, STEP = 916, RIGHT, 1000, 352, 22
ROWS = [(1030, 1064, 1098, GREEN), (962, 995, 1028, MUTE), (1012, 1042, 1072, GREEN),
        (926, 954, 982, AMBER), (976, 1010, 1044, MUTE)]
for y in range(Y0 - 12, Y0 + STEP * 4 + 12, 7):
    line(ZERO, y, ZERO, y + 3, MUTE)
for i, (lo, mid, hi, col) in enumerate(ROWS):
    y = Y0 + STEP * i
    line(PX0, y, PX1, y, HAIR)
    line(lo, y, hi, y, col, 2)
    line(lo, y - 5, lo, y + 5, col, 2)
    line(hi, y - 5, hi, y + 5, col, 2)
    d.ellipse([(mid - 5) * S, (y - 5) * S, (mid + 5) * S, (y + 5) * S], fill=col)

# footer
spaced(M, 584, "muend.github.io", MONO, MUTE, 2)
spaced(RIGHT, 584, "\u0130ZM\u0130R \u00b7 T\u00dcRK\u0130YE", MONO, AMBER, 2, anchor="r")

out = pathlib.Path(__file__).resolve().parent.parent / "assets" / "brand" / "share-card.png"
img.resize((W, H), Image.LANCZOS).save(out, optimize=True)
print("wrote", out, out.stat().st_size, "bytes")
