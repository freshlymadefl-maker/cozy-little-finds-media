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
    dst = CUT / f"{pathlib.Path(src).stem}_{tol}_{grab or 'n'}.png"
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
    if grab == "shadow":
        q = deque((i % w, i // w) for i in range(w * h) if seen[i])
        while q:
            x, y = q.popleft()
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= nx < w and 0 <= ny < h and not seen[ny * w + nx]:
                    r, g, b, _ = px[nx, ny]
                    if r + g + b > 3 * 165 and max(r, g, b) - min(r, g, b) < 16:
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


def title(canvas, text, y, size=64, style="pill", fill="#FFFFFF", bgc="#1F3B2D", x="center", track=.05):
    """Refined title badge (owner: keep titles, but let the products lead). Semibold-bold sans with a little letter spacing.
    style 'pill' = text on a rounded colour badge; 'shadow' = white text with a soft dark shadow (pine backgrounds).
    Returns the badge rectangle so build() can keep products off it."""
    f = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", size)
    tr = round(size * track)
    def line_w(t):
        return sum(f.getlength(c) for c in t) + tr * (len(t) - 1)
    lines = text.split("\n"); asc, desc = f.getmetrics(); lh = asc + desc - size // 8
    tw = round(max(line_w(t) for t in lines)); th = lh * len(lines)
    px, py = (round(size * .55), round(size * .2)) if style == "pill" else (round(size * .2), round(size * .1))
    W2, H2 = tw + 2 * px, th + 2 * py
    layer = Image.new("RGBA", (W2 + 60, H2 + 60), (0, 0, 0, 0)); ox = oy = 30
    d = ImageDraw.Draw(layer)
    if style == "pill":
        sh = Image.new("RGBA", layer.size, (0, 0, 0, 0))
        ImageDraw.Draw(sh).rounded_rectangle([ox, oy + 5, ox + W2, oy + H2 + 5], radius=round(size * .32), fill=(0, 0, 0, 70))
        layer.alpha_composite(sh.filter(ImageFilter.GaussianBlur(7)))
        d.rounded_rectangle([ox, oy, ox + W2, oy + H2], radius=round(size * .32), fill=bgc)
    def draw_text(dr, dx, dy, col):
        for i, t in enumerate(lines):
            cx = ox + px + (tw - line_w(t)) / 2 + dx
            for c in t:
                dr.text((cx, oy + py + i * lh + dy - size * .08), c, font=f, fill=col); cx += f.getlength(c) + tr
    if style != "pill":
        sh = Image.new("RGBA", layer.size, (0, 0, 0, 0)); draw_text(ImageDraw.Draw(sh), 0, 4, (0, 0, 0, 210))
        layer.alpha_composite(sh.filter(ImageFilter.GaussianBlur(6)))
    draw_text(d, 0, 0, fill)
    X = (W - W2) // 2 if x == "center" else x
    _safe(canvas, layer, X - ox, y - oy)
    return (X, y, X + W2, y + H2)


def place(canvas, img, x, y, w, rot=0, shadow=.28, flip=False, erode=1):
    im = img.copy()
    if flip: im = im.transpose(Image.FLIP_LEFT_RIGHT)
    im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    a = im.getchannel("A")
    for _ in range(erode):
        a = a.filter(ImageFilter.MinFilter(3))
    im.putalpha(a.filter(ImageFilter.GaussianBlur(.7)) if erode else a)   # erode the edge 2px + re-feather: kills pale halos / leftover fringe from the cut
    if rot: im = im.rotate(-rot, expand=True, resample=Image.BICUBIC)
    if shadow:
        a = im.getchannel("A").point(lambda v: v * shadow)
        sh = Image.new("RGBA", im.size, (40, 30, 20, 0)); sh.putalpha(a)
        pad = Image.new("RGBA", (im.width + 60, im.height + 60), (0, 0, 0, 0)); pad.alpha_composite(sh, (30, 30))
        pad = pad.filter(ImageFilter.GaussianBlur(9))
        _safe(canvas, pad, x - 26, y - 20)
    _safe(canvas, im, x, y)
    return im


def _safe(canvas, im, x, y):
    layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0)); layer.paste(im, (x, y), im)
    canvas.alpha_composite(layer)


def sticker(canvas, text, x, y, size=64, fill="#FFFFFF", stroke="#1F3B2D"):
    f = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", size)
    ImageDraw.Draw(canvas).multiline_text((x, y), text, font=f, fill=fill, stroke_width=max(3, size // 14), stroke_fill=stroke, spacing=4)


TY = 1226   # title badge top (all collages): the badge sits in the bottom band, products stay above ~1210
LAYOUTS = {
 # Item: (file, x, y, width, rotation, cut tolerance, *opts)  opts: grab|dark|shadow (cut mode), flush (hero may bleed), thin (no edge erosion)
 "her-cozy": dict(bg=stripes, title=dict(text="Cozy Gifts for Her", y=TY, bgc="#7A1F2B"), items=[
   ("bfd/cardi_c.jpg", -60, -20, 660, 0, 16, "grab", "flush"),
   ("bow.png", 610, 20, 240, 8, 28),
   ("headband.png", 850, 24, 196, -10, 28),
   ("bag.png", 590, 270, 240, -3, 28, "thin"),
   ("wmp/juicy.jpg", 830, 260, 220, 4, 28),
   ("earrings.png", 870, 520, 170, 6, 28),
   ("bf/stanley.png", 650, 600, 150, -4, 28),
   ("trend/nest.jpg", 790, 760, 260, 0, 26),
   ("bfd/BDWCC27064_STONE_MULTI_FRONT.jpg", 16, 790, 190, -6, 42),
   ("loafers.png", 190, 925, 370, 4, 28),
   ("u25/pillow_c.png", 545, 900, 480, -4, 30),
 ]),
 "him-favorites": dict(bg=pine, title=dict(text="Holiday Favorites", y=TY, size=70, style="shadow"), items=[
   ("brand/bose_c.png", 24, 24, 370, -4, 28),
   ("brand/beanie_c.png", 400, 24, 320, 4, 28),
   ("brand/yeti_c.png", 750, 20, 290, 3, 28),
   ("wmp/puzzle-parks.jpg", 380, 320, 340, -3, 28),
   ("dec3/lodge.jpg", 30, 500, 320, -12, 28),
   ("brand/thera_c.png", 830, 380, 220, -8, 50, "dark"),
   ("watch.png", 720, 360, 118, 8, 28),
   ("wallet.png", 350, 650, 300, 6, 28),
   ("brand/airtag_c.png", 870, 660, 170, 10, 28),
   ("him/leatherman.jpg", 680, 720, 130, 18, 28),
   ("bfd/BDWCC27072_UMBER_MULTI_FRONT.jpg", 840, 820, 180, -8, 42),
   ("moccasins.png", 190, 860, 490, -3, 28),
 ]),
 "hosting-season": dict(bg=linen, title=dict(text="Hosting Season", y=TY, bgc="#7A1F2B"), items=[
   ("wmp/board-hecef.jpg", 24, 24, 500, -2, 28),
   ("trend/cosori.png", 550, 24, 300, 0, 28),
   ("brand/ember_c.png", 862, 50, 185, 4, 28),
   ("glass.png", 555, 315, 230, 0, 28),
   ("wmp/taper-red.jpg", 1006, 300, 42, 0, 28, "thin"),
   ("dec3/dash.jpg", 790, 330, 210, -4, 30, "shadow"),
   ("wmp/board-farb.jpg", 24, 540, 410, 0, 28),
   ("dec3/lodge.jpg", 450, 610, 340, -16, 28),
   ("wmp/coupe-thyme.jpg", 30, 950, 470, 0, 28, "thin"),
   ("trend/nest.jpg", 590, 1000, 440, 0, 26),
 ]),
 "cozy-night-in": dict(bg=stripes, title=dict(text="Cozy Night In", y=TY, bgc="#8C3A4B"), items=[
   ("bfd/robe_c.jpg", -40, -20, 520, 0, 34, "grab", "flush"),
   ("bfd/B503_Java_1_HR.jpg", 500, 24, 390, 3, 30, "dark"),
   ("jlab/lux_mauve.png", 870, 40, 170, 6, 28),
   ("trend/cosori.png", 860, 330, 195, 0, 28),
   ("dec3/jellycat.jpg", 490, 440, 300, -4, 30, "shadow"),
   ("brand/ember_c.png", 820, 540, 210, 0, 28),
   ("u25/sdj.jpg", 420, 620, 95, 4, 28),
   ("u25/candle_c.png", 560, 730, 250, 0, 28),
   ("wmp/puzzle-parks.jpg", 810, 800, 225, 4, 28),
   ("wmp/socks.jpg", 480, 880, 240, -4, 28),
   ("brand/ugg_c.png", 24, 1030, 420, -3, 28),
 ]),
 "stocking-stuffers": dict(bg=pine, title=dict(text="Stocking Stuffers", y=TY, size=70, style="shadow"), items=[
   ("trend/instax_pink.png", 24, 24, 300, -5, 28),
   ("dec3/jellycat.jpg", 340, 30, 330, 0, 30, "shadow"),
   ("wmp/coach.jpg", 690, 40, 360, 3, 28),
   ("brand/thera_c.png", 30, 420, 240, -8, 50, "dark"),
   ("jlab/air_rose.png", 300, 380, 270, 4, 55),
   ("wmp/claw.jpg", 600, 340, 140, -6, 28),
   ("wmp/mdeal.jpg", 760, 320, 210, 6, 28),
   ("earrings.png", 420, 700, 190, 0, 28),
   ("wmp/needoh-ice.jpg", 870, 620, 170, -6, 28),
   ("bfd/BDWNV27074_UMBER_MULTI_FRONT.jpg", 40, 760, 280, -10, 42),
   ("him/leatherman.jpg", 380, 900, 150, 64, 28),
   ("brand/airtag_c.png", 660, 760, 150, 10, 28),
   ("dec3/kong.jpg", 870, 900, 160, 8, 30, "shadow"),
 ]),
 "kid-approved": dict(bg=lambda: stripes("#F8F0EF", "#EFE0E1"), title=dict(text="Kid-Approved Gifts", y=TY, bgc="#5B3C88"), items=[
   ("wmp/magtiles.jpg", 24, 24, 390, 0, 28),
   ("wmp/connect4.jpg", 440, 24, 290, 3, 28),
   ("wmp/lego-panda.jpg", 760, 24, 290, 0, 28),
   ("wmp/uno.jpg", 30, 440, 230, -5, 28),
   ("wmp/beyblade.jpg", 280, 340, 320, 0, 28),
   ("trend/yoto_nohand.png", 630, 340, 200, 4, 28),
   ("wmp/squish.jpg", 840, 340, 220, 6, 28),
   ("wmp/needoh-adv.jpg", 290, 680, 330, 3, 28),
   ("trend/instax_d1.png", 690, 560, 265, -6, 28),
   ("wmp/puzzle-xmas.jpg", 30, 800, 290, -3, 28),
   ("wmp/needoh-ice.jpg", 380, 960, 180, 6, 28),
   ("wmp/karaoke.jpg", 720, 860, 300, 0, 30, "shadow"),
 ]),
}


MODES = {"grab", "dark", "shadow"}
MARGIN = 14


def opts(g):
    mode = next((o for o in g if o in MODES), False)
    return mode, ("flush" in g), (0 if "thin" in g else 2 if "trim" in g else 1)


def build(name, check=True):
    L = LAYOUTS[name]
    canvas = L["bg"]().convert("RGBA")
    placed = []
    for f, x, y, w, rot, tol, *g in L["items"]:
        mode, flush, er = opts(g)
        im = place(canvas, cut(f, tol, mode), x, y, w, rot, erode=er)
        bb = im.getchannel("A").point(lambda v: 255 if v > 40 else 0).getbbox()
        placed.append((f, flush, (x + bb[0], y + bb[1], x + bb[2], y + bb[3]), im, x, y))
    T = L["title"]; tb = title(canvas, **T)
    if check:
        for f, flush, (a, b, c, d), im, x, y in placed:
            if not flush and (a < MARGIN or b < MARGIN or c > W - MARGIN or d > H - MARGIN):
                print(f"  edge: {f} bbox={a,b,c,d}")
            # product pixels under the title badge
            ia = im.getchannel("A"); ov = 0
            for yy in range(max(tb[1], y), min(tb[3], y + im.height), 3):
                for xx in range(max(tb[0], x), min(tb[2], x + im.width), 3):
                    if ia.getpixel((xx - x, yy - y)) > 60: ov += 1
            if ov: print(f"  under title: {f} ({ov} samples)")
    OUT.mkdir(parents=True, exist_ok=True)
    p = OUT / f"{name}.png"; canvas.convert("RGB").save(p, quality=95); print(p.name)


def cutcheck(name):
    """Contact sheet of a layout's cut-outs on magenta, to spot grey remnants / ghosted parts."""
    items = LAYOUTS[name]["items"]; S = 260; C = 5
    sheet = Image.new("RGBA", (S * C, S * ((len(items) + C - 1) // C)), (255, 0, 255, 255))
    for i, (f, x, y, w, rot, tol, *g) in enumerate(items):
        im = cut(f, tol, opts(g)[0]).copy(); im.thumbnail((S - 10, S - 10)); sheet.alpha_composite(im, ((i % C) * S + 5, (i // C) * S + 5))
    p = ROOT / "out" / f"_cuts-{name}.png"; sheet.convert("RGB").save(p); print(p)


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[:1] == ["--cuts"]:
        for n in args[1:]: cutcheck(n)
    else:
        for n in (args or LAYOUTS):
            build(n)
