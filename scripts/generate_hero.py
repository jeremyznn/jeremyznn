from pathlib import Path
from datetime import datetime, timezone
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
import os

W, H = 846, 318
FRAMES = 42
DURATION = 80
OUT = Path("assets/generated")
OUT.mkdir(parents=True, exist_ok=True)

STAMP = datetime.now(timezone.utc).strftime("%Y.%m.%d")

def font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

F_NAME = font(50, True)
F_ROLE = font(17, True)
F_COMPANY = font(17, True)
F_BODY = font(13)
F_MONO = font(10)
F_NODE = font(10, True)

def make_gradient(top, bottom):
    im = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(im)
    for y in range(H):
        t = y / max(1, H - 1)
        c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        draw.line((0, y, W, y), fill=c)
    return im.convert("RGBA")

def rounded_label(draw, x, y, text, colors, active):
    panel, fg, border, accent = colors
    bbox = draw.textbbox((0, 0), text, font=F_NODE)
    tw = bbox[2] - bbox[0]
    width = max(66, tw + 28)
    height = 28
    x0, y0 = int(x - width/2), int(y - height/2)
    alpha = int(150 + active * 80)
    fill = (*panel, alpha)
    outline = (*accent, int(80 + active * 120))
    draw.rounded_rectangle((x0, y0, x0 + width, y0 + height), radius=14, fill=fill, outline=outline, width=1)
    draw.ellipse((x0 + 10, y0 + 11, x0 + 16, y0 + 17), fill=(*accent, 230))
    draw.text((x0 + 22, y0 + 7), text, font=F_NODE, fill=(*fg, 255))

def render(theme):
    dark = theme == "dark"
    top = (8, 10, 18) if dark else (249, 250, 253)
    bottom = (15, 12, 34) if dark else (235, 236, 246)
    panel = (17, 20, 32) if dark else (255, 255, 255)
    fg = (246, 248, 255) if dark else (25, 27, 36)
    muted = (159, 167, 191) if dark else (93, 99, 119)
    violet = (139, 92, 246) if dark else (109, 77, 224)
    cyan = (34, 211, 238) if dark else (8, 145, 178)
    line = (56, 61, 83) if dark else (207, 211, 225)

    frames = []
    labels = [
        ("NEXT.JS", 0.00),
        ("TYPESCRIPT", 0.16),
        ("REACT", 0.32),
        ("NODE", 0.48),
        ("FLUTTER", 0.64),
        ("AWS", 0.80),
    ]

    for idx in range(FRAMES):
        phase = idx / FRAMES
        im = make_gradient(top, bottom)

        glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        gd = ImageDraw.Draw(glow)
        gd.ellipse((500, -110, 920, 330), fill=(*violet, 45))
        gd.ellipse((485, 90, 800, 390), fill=(*cyan, 25))
        glow = glow.filter(ImageFilter.GaussianBlur(62))
        im = Image.alpha_composite(im, glow)

        d = ImageDraw.Draw(im)

        # Safe perspective grid: right side only.
        horizon = 225
        grid_fill = (*violet, 30 if dark else 22)
        for x in range(474, 846, 44):
            d.line((655, horizon, x, H), fill=grid_fill, width=1)
        for y in range(horizon, H + 1, 18):
            d.line((470, y, 846, y), fill=grid_fill, width=1)

        # Status.
        d.rounded_rectangle((40, 32, 256, 62), radius=15, fill=(*panel, 205), outline=(*violet, 95), width=1)
        pulse = 0.55 + 0.45 * math.sin(phase * math.tau)
        d.ellipse((55, 43, 64, 52), fill=(*cyan, int(150 + 80 * pulse)))
        d.text((76, 42), "PROFILE SYSTEM // ONLINE", font=F_MONO, fill=(*muted, 255))

        # Stable content block: never moves.
        d.text((40, 88), "JÉRÉMY", font=F_NAME, fill=(*fg, 255))
        d.text((42, 148), "FULL‑STACK ENGINEER", font=F_ROLE, fill=(*violet, 255))
        d.text((42, 185), "SKOLEOM PLATFORM INC.", font=F_COMPANY, fill=(*fg, 255))
        d.text((42, 214), "Product Engineering · Cloud · Mobile · AI", font=F_BODY, fill=(*muted, 255))
        d.line((42, 250, 346, 250), fill=(*line, 230), width=1)
        d.text((42, 268), "PARIS / FRANCE", font=F_MONO, fill=(*muted, 255))
        d.text((42, 287), f"BUILD {STAMP}", font=F_MONO, fill=(*muted, 255))

        # Calm 3D orbit. Only this area moves.
        cx, cy = 655, 150
        rx, ry = 147, 61
        d.ellipse((cx-rx, cy-ry, cx+rx, cy+ry), outline=(*violet, 78), width=1)
        d.ellipse((cx-rx-28, cy-ry-16, cx+rx+28, cy+ry+16), outline=(*cyan, 42), width=1)

        core_r = 38
        d.ellipse((cx-core_r, cy-core_r, cx+core_r, cy+core_r), fill=(*panel, 240), outline=(*cyan, 140), width=2)
        d.text((cx-18, cy-13), "SHIP", font=F_NODE, fill=(*fg, 255))
        d.text((cx-25, cy+7), "BUILD / SCALE", font=F_MONO, fill=(*muted, 255))

        nodes = []
        for label, start in labels:
            a = (start + phase * 0.46) * math.tau
            z = (math.sin(a) + 1) / 2
            x = cx + math.cos(a) * rx
            y = cy + math.sin(a) * ry
            nodes.append((z, label, x, y))

        for z, label, x, y in sorted(nodes, key=lambda item: item[0]):
            d.line((cx, cy, int(x), int(y)), fill=(*violet, int(20 + z * 55)), width=1)
            rounded_label(d, x, y, label, (panel, fg, line, cyan if z > .5 else violet), z)

        frames.append(im.convert("P", palette=Image.Palette.ADAPTIVE, colors=160))

    target = OUT / f"hero.{theme}.gif"
    frames[0].save(
        target,
        save_all=True,
        append_images=frames[1:],
        optimize=True,
        duration=DURATION,
        loop=0,
        disposal=2,
    )
    print("generated", target)

render("dark")
render("light")
