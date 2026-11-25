"""Collage v2: the owner's OLD Amazon collage look (Nov 25 2026: "my old amazon collages are SOO much better").
What her old ones do: 12-16 clean cut-outs piled edge to edge, a model/apparel hero cropped flush to the frame,
heavy overlap (items layered like a pile), one tight palette, soft stripe / linen / deep-green background,
little or no text (optional bold sticker). Built here with PIL so placement is exact (no dragging in Amazon's editor).

Run: python specs/make_collage2.py <name>   (layouts in LAYOUTS below)  -> posts/collage2/<name>.png
Each item: (file, x, y, width, rotation). Paint order = list order (first = back)."""
import pathlib, sys
from collections import deque
from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageChops

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
CUT = SRC / "col"
OUT = ROOT / "posts" / "collage2"
W, H = 1080, 1350


def cut(src, tol=30, grab=False, cache=True):
    """Flood-fill the background from the border by colour distance to the border colour (works on white AND grey studio bgs)."""
    dst = CUT / (pathlib.Path(src).stem + ".png")
    if cache and dst.exists():
        return Image.open(dst)
    im = Image.open(SRC / src).convert("RGBA")
    if im.getextrema()[3][0] < 250 and tol >= 50:   # pre-cut PNG with a shadow/halo: flatten on white and re-cut harder
        flat = Image.new("RGBA", im.size, (255, 255, 255, 255)); flat.alpha_composite(im); im = flat
    if im.getextrema()[3][0] < 250:          # already transparent
        a = im.getchannel("A")
        out = im.crop(a.point(lambda v: 255 if v > 20 else 0).getbbox())
        out.save(dst); return out
    w, h = im.size
    px = im.load()
    border = [px[x, 0] for x in range(0, w, 7)] + [px[0, y] for y in range(0, h, 7)] + [px[w - 1, y] for y in range(0, h, 7)]
    br = sorted(border, key=lambda p: sum(p[:3]))[len(border) // 2]
    def bgish(x, y):
        r, g, b, _ = px[x, y]
        return abs(r - br[0]) + abs(g - br[1]) + abs(b - br[2]) < tol * 3 // 2
    seen = bytearray(w * h); q = deque()
    for x in range(w):
        for y in (0, h - 1):
            if bgish(x, y): seen[y * w + x] = 1; q.append((x, y))
    for y in range(h):
        for x in (0, w - 1):
            if bgish(x, y) and not seen[y * w + x]: seen[y * w + x] = 1; q.append((x, y))
    while q:
        x, y = q.popleft()
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < w and 0 <= ny < h and not seen[ny * w + nx] and bgish(nx, ny):
                seen[ny * w + nx] = 1; q.append((nx, ny))
    if grab == "dark":   # dark product on a light bg with a grey drop shadow: keep flooding through any light pixel
        q = deque((i % w, i // w) for i in range(w * h) if seen[i])
        while q:
            x, y = q.popleft()
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= nx < w and 0 <= ny < h and not seen[ny * w + nx]:
                    r, g, b, _ = px[nx, ny]
                    if r + g + b > 3 * 135:
                        seen[ny * w + nx] = 1; q.append((nx, ny))
    mask = Image.frombytes("L", (w, h), bytes(0 if s else 255 for s in seen))
    if grab is True or grab == "grab":   # photo with a grey/gradient studio bg (models): refine with OpenCV GrabCut seeded by the flood fill
        import cv2, numpy as np
        rgb = np.array(im.convert("RGB"))[:, :, ::-1].copy()
        m = np.where(np.array(mask) > 0, cv2.GC_PR_FGD, cv2.GC_BGD).astype("uint8")
        bgm, fgm = np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64)
        cv2.grabCut(rgb, m, None, bgm, fgm, 6, cv2.GC_INIT_WITH_MASK)
        mask = Image.fromarray(np.where((m == cv2.GC_FGD) | (m == cv2.GC_PR_FGD), 255, 0).astype("uint8"))
    mask = mask.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.1))
    im.putalpha(mask)
    out = im.crop(mask.point(lambda v: 255 if v > 20 else 0).getbbox())
    out.save(dst); return out


def stripes(a="#F4EFE7", b="#E8E0D2", n=9):
    bg = Image.new("RGB", (W, H), a); d = ImageDraw.Draw(bg); sw = W / n
    for i in range(1, n, 2):
        d.rectangle([i * sw, 0, (i + 1) * sw, H], fill=b)
    return bg


def pine():
    bg = Image.new("RGB", (W, H), "#1F3B2D"); g = Image.new("L", (W, H), 0); d = ImageDraw.Draw(g)
    d.polygon([(W * .55, 0), (W * .85, 0), (W * .3, H), (0, H)], fill=60)
    return Image.composite(Image.new("RGB", (W, H), "#2E5A43"), bg, g.filter(ImageFilter.GaussianBlur(90)))


def linen(base=(233, 223, 205)):
    """Warm oatmeal linen: fine noise + faint horizontal/vertical weave."""
    import random
    rnd = random.Random(7)
    sm = Image.new("L", (W // 2, H // 2)); sm.putdata([rnd.randint(0, 255) for _ in range(W * H // 4)])
    noise = sm.resize((W, H), Image.BILINEAR).filter(ImageFilter.GaussianBlur(.6))
    weave = Image.new("L", (W, H), 128); d = ImageDraw.Draw(weave)
    for y in range(0, H, 3):
        d.line([(0, y), (W, y)], fill=128 + rnd.randint(-22, 22))
    wv = Image.new("L", (W, H), 128); d = ImageDraw.Draw(wv)
    for x in range(0, W, 3):
        d.line([(x, 0), (x, H)], fill=128 + rnd.randint(-18, 18))
    tex = ImageChops.add(ImageChops.multiply(weave, wv), noise, scale=2)
    bg = Image.new("RGB", (W, H), base)
    dark = Image.new("RGB", (W, H), tuple(int(c * .9) for c in base))
    return Image.composite(bg, dark, tex.point(lambda v: min(255, int(v * 1.6) + 40)))


def title(canvas, text, x, y, size=88, style="shadow", fill="#FFFFFF", bgc="#1F3B2D", rot=0):
    """Bold title sticker like her old collages. style 'shadow' = white heavy sans with dark outline + soft shadow (for pine);
    'pill' = heavy text on a rounded colour pill (for cream/linen). x, y = top-left of the sticker."""
    f = ImageFont.truetype("C:/Windows/Fonts/seguibl.ttf", size)
    probe = ImageDraw.Draw(Image.new("L", (1, 1)))
    l, t, r, b = map(round, probe.multiline_textbbox((0, 0), text, font=f, spacing=-size // 10, align="center"))
    tw, th = r - l, b - t
    px, py = (int(size * .42), int(size * .26)) if style == "pill" else (int(size * .2), int(size * .2))
    layer = Image.new("RGBA", (tw + 2 * px + 40, th + 2 * py + 40), (0, 0, 0, 0))
    ox, oy = 20, 20
    if style == "pill":
        sh = Image.new("RGBA", layer.size, (0, 0, 0, 0))
        ImageDraw.Draw(sh).rounded_rectangle([ox, oy + 6, ox + tw + 2 * px, oy + th + 2 * py + 6], radius=int(size * .45), fill=(0, 0, 0, 90))
        layer.alpha_composite(sh.filter(ImageFilter.GaussianBlur(8)))
        ImageDraw.Draw(layer).rounded_rectangle([ox, oy, ox + tw + 2 * px, oy + th + 2 * py], radius=int(size * .45), fill=bgc)
        ImageDraw.Draw(layer).multiline_text((ox + px - l, oy + py - t), text, font=f, fill=fill, spacing=-size // 10, align="center")
    else:
        sh = Image.new("RGBA", layer.size, (0, 0, 0, 0))
        ImageDraw.Draw(sh).multiline_text((ox + px - l, oy + py - t + 6), text, font=f, fill=(0, 0, 0, 200), spacing=-size // 10, align="center",
                                          stroke_width=max(2, size // 22), stroke_fill=(0, 0, 0, 200))
        layer.alpha_composite(sh.filter(ImageFilter.GaussianBlur(7)))
        ImageDraw.Draw(layer).multiline_text((ox + px - l, oy + py - t), text, font=f, fill=fill, spacing=-size // 10, align="center",
                                             stroke_width=max(2, size // 26), stroke_fill=bgc)
    if rot:
        layer = layer.rotate(-rot, expand=True, resample=Image.BICUBIC)
    _safe(canvas, layer, x - ox, y - oy)


def place(canvas, img, x, y, w, rot=0, shadow=.28, flip=False):
    im = img.copy()
    if flip: im = im.transpose(Image.FLIP_LEFT_RIGHT)
    im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    if rot: im = im.rotate(-rot, expand=True, resample=Image.BICUBIC)
    if shadow:
        a = im.getchannel("A").point(lambda v: v * shadow)
        sh = Image.new("RGBA", im.size, (40, 30, 20, 0)); sh.putalpha(a)
        pad = Image.new("RGBA", (im.width + 60, im.height + 60), (0, 0, 0, 0)); pad.alpha_composite(sh, (30, 30))
        pad = pad.filter(ImageFilter.GaussianBlur(9))
        _safe(canvas, pad, x - 26, y - 20)
    _safe(canvas, im, x, y)


def _safe(canvas, im, x, y):
    layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0)); layer.paste(im, (x, y), im)
    canvas.alpha_composite(layer)


def sticker(canvas, text, x, y, size=64, fill="#FFFFFF", stroke="#1F3B2D"):
    f = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", size)
    ImageDraw.Draw(canvas).multiline_text((x, y), text, font=f, fill=fill, stroke_width=max(3, size // 14), stroke_fill=stroke, spacing=4)


LAYOUTS = {
 # Cozy gifts for her: cream stripes, cranberry + oatmeal + cream + gold
 "her-cozy": dict(bg=stripes, title=dict(text="Cozy Gifts\nfor Her", x=40, y=600, size=84, style="pill", bgc="#7A1F2B"), items=[
   ("bfd/cardi_c.jpg", -60, -30, 680, 0, 16, "grab"),        # hero apparel, cropped flush top-left
   ("bow.png", 550, 10, 320, 10, 28),
   ("headband.png", 860, 20, 210, -14, 28),
   ("dec3/yankee.jpg", 810, 290, 260, 4, 28),
   ("bag.png", 520, 330, 330, -4, 28),
   ("u25/pillow_c.png", 590, 930, 540, 6, 30),        # plaid satin pillowcase, bottom right
   ("u25/candle_c.png", 250, 640, 210, 0, 28),
   ("bfd/BDWCC27064_STONE_MULTI_FRONT.jpg", -30, 770, 260, -10, 42),
   ("u25/claw_c.png", 330, 790, 230, -6, 28),
   ("u25/sdj_c.png", 520, 720, 120, 8, 28),
   ("earrings.png", 860, 650, 200, 6, 28),
   ("trend/nest.jpg", 330, 1110, 410, -3, 26),
   ("loafers.png", 20, 1110, 380, 4, 28),
  ]),
 # Gifts for him: deep pine, browns/black/silver, white "Holiday Favorites" title at the bottom
 "him-favorites": dict(bg=pine, title=dict(text="Holiday Favorites", x=95, y=1180, size=104), items=[
   ("brand/bose_c.png", -20, 30, 470, -6, 28),
   ("brand/beanie_c.png", 410, -10, 300, 6, 28),
   ("brand/yeti_c.png", 760, 10, 270, 4, 28),
   ("trend/cosori.png", 20, 400, 330, -4, 28),
   ("brand/ember_c.png", 330, 330, 270, 0, 28),
   ("watch.png", 610, 290, 170, 12, 28),
   ("dec3/bose_flex.jpg", 760, 330, 300, -8, 28),
   ("dec3/lodge.jpg", 540, 520, 380, -18, 28),
   ("him/leatherman.jpg", 900, 560, 150, 18, 28),
   ("wallet.png", 300, 640, 280, 8, 28),
   ("brand/thera_c.png", 10, 740, 320, -10, 50, "dark"),
   ("bfd/BDWCC27072_UMBER_MULTI_FRONT.jpg", 270, 860, 210, -14, 42),
   ("moccasins.png", 560, 860, 470, -4, 28),
   ("brand/airtag_c.png", 440, 900, 170, 10, 28),
 ]),
 # Christmas hosting: oatmeal linen, red/cream/gold/black, cranberry pill title
 "hosting-season": dict(bg=linen, title=dict(text="Hosting Season", x=150, y=725, size=100, style="pill", bgc="#7A1F2B"), items=[
   ("bfd/BDWNV27074_UMBER_MULTI_FRONT.jpg", 0, 10, 200, -10, 42),
   ("dec3/lodge.jpg", 110, 30, 430, -20, 28),
   ("dec3/yankee.jpg", 470, 10, 260, 3, 28),
   ("trend/cosori.png", 700, 0, 390, 0, 28),
   ("u25/candle_c.png", 0, 380, 270, 0, 28),
   ("bow.png", 250, 420, 270, -8, 28),
   ("brand/ember_c.png", 520, 360, 240, -4, 28),
   ("glass.png", 770, 370, 280, 6, 28),
   ("dec3/bose_flex.jpg", -20, 870, 320, -6, 28),
   ("u25/pillow_c.png", -30, 1000, 500, -6, 30),
   ("bfd/B503_Java_1_HR.jpg", 330, 880, 400, 4, 30, "dark"),
   ("trend/nest.jpg", 640, 880, 450, 3, 26),
   ("brand/ugg_c.png", 690, 1110, 390, -4, 28),
 ]),
 # Cozy night in: cream stripes, rose/mauve/oatmeal/brown, rose pill title
 "cozy-night-in": dict(bg=stripes, title=dict(text="Cozy Night In", x=330, y=1180, size=92, style="pill", bgc="#8C3A4B"), items=[
   ("bfd/robe_c.jpg", -60, -20, 620, 0, 34, "grab"),
   ("bfd/B503_Java_1_HR.jpg", 560, 0, 430, 4, 30, "dark"),
   ("jlab/lux_mauve.png", 820, 300, 260, 10, 28),
   ("bf/stanley.png", 520, 330, 220, -4, 28),
   ("u25/sdj_c.png", 720, 470, 120, 8, 28),
   ("dec3/yankee.jpg", 820, 560, 240, 3, 28),
   ("brand/ember_c.png", 560, 620, 240, -3, 28),
   ("u25/candle_c.png", 330, 640, 220, 0, 28),
   ("bfd/BDWCC27064_STONE_MULTI_FRONT.jpg", -20, 760, 240, -10, 42),
   ("bfd/BDWCC27072_UMBER_MULTI_FRONT.jpg", 180, 800, 230, 8, 42),
   ("jlab/air_rose.png", 760, 860, 260, -6, 55),
   ("brand/ugg_c.png", 420, 880, 380, -6, 28),
   ("moccasins.png", 10, 1080, 420, 4, 28),
   ("trend/nest.jpg", 680, 1000, 380, -2, 26),
 ]),
 # Stocking stuffers: pine, small bright pieces, white title
 "stocking-stuffers": dict(bg=pine, title=dict(text="Stocking Stuffers", x=110, y=1190, size=104), items=[
   ("dec3/jellycat.jpg", 10, 10, 320, -4, 60),
   ("trend/instax_pink.png", 330, 0, 330, 6, 28),
   ("bow.png", 690, 0, 380, 10, 28),
   ("u25/candle_c.png", 0, 360, 290, 0, 28),
   ("brand/thera_c.png", 270, 330, 260, -10, 50, "dark"),
   ("headband.png", 540, 320, 260, -8, 28),
   ("dec3/kong.jpg", 840, 330, 220, 10, 28),
   ("bfd/BDWNV27074_UMBER_MULTI_FRONT.jpg", 0, 590, 250, -12, 42),
   ("dec3/bose_flex.jpg", 240, 690, 360, -6, 28),
   ("jlab/air_rose.png", 590, 600, 300, 6, 55),
   ("earrings.png", 890, 600, 170, 8, 28),
   ("watch.png", 60, 880, 170, -10, 28),
   ("brand/airtag_c.png", 260, 840, 210, 12, 28),
   ("him/leatherman.jpg", 420, 880, 170, 70, 28),
   ("jlab/pop_cloud.png", 690, 860, 340, -4, 50),
 ]),
 # Kids: blush stripes, pastel lilac/pink/sage, plum pill title
 "kid-approved": dict(bg=lambda: stripes("#F8F0EF", "#EFE0E1"), title=dict(text="Kid-Approved Gifts", x=150, y=1190, size=86, style="pill", bgc="#5B3C88"), items=[
   ("trend/magna.jpg", 10, 10, 540, -4, 28),
   ("trend/yoto.png", 560, 0, 320, 6, 55),
   ("dec3/jellycat.jpg", 820, 60, 260, 6, 60),
   ("trend/instax_d1.png", 520, 330, 300, -6, 28),
   ("trend/instax_pink.png", 30, 520, 290, 8, 28),
   ("dec3/dash.jpg", 320, 560, 260, -4, 28),
   ("jlab/lux_sage.png", 780, 430, 290, 10, 28),
   ("bf/stanley.png", 860, 700, 200, 6, 28),
   ("jlab/air_lilac.png", 600, 700, 260, -6, 28),
   ("u25/claw_c.png", 20, 860, 260, -8, 28),
   ("jlab/lux_mauve.png", 270, 820, 330, 4, 28),
   ("jlab/pop_cloud.png", 620, 900, 280, 6, 50),
 ]),
}


def build(name):
    L = LAYOUTS[name]
    canvas = L["bg"]().convert("RGBA")
    for f, x, y, w, rot, tol, *g in L["items"]:
        place(canvas, cut(f, tol, g[0] if g else False), x, y, w, rot)
    if L.get("title"):
        title(canvas, **L["title"])
    OUT.mkdir(parents=True, exist_ok=True)
    p = OUT / f"{name}.png"; canvas.convert("RGB").save(p, quality=95); print(p)


def cutcheck(name):
    """Contact sheet of a layout's cut-outs on magenta, to spot grey remnants / ghosted parts."""
    items = LAYOUTS[name]["items"]; S = 260; C = 5
    sheet = Image.new("RGBA", (S * C, S * ((len(items) + C - 1) // C)), (255, 0, 255, 255))
    for i, (f, x, y, w, rot, tol, *g) in enumerate(items):
        im = cut(f, tol, g[0] if g else False).copy(); im.thumbnail((S - 10, S - 10)); sheet.alpha_composite(im, ((i % C) * S + 5, (i // C) * S + 5))
    p = ROOT / "out" / f"_cuts-{name}.png"; sheet.convert("RGB").save(p); print(p)


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[:1] == ["--cuts"]:
        for n in args[1:]: cutcheck(n)
    else:
        for n in (args or LAYOUTS):
            build(n)
