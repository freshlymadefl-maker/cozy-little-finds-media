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


def cut(src, tol=30, grab=False):
    """Flood-fill the background from the border by colour distance to the border colour (works on white AND grey studio bgs)."""
    dst = CUT / (pathlib.Path(src).stem + ".png")
    if dst.exists():
        return Image.open(dst)
    im = Image.open(SRC / src).convert("RGBA")
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
    mask = Image.frombytes("L", (w, h), bytes(0 if s else 255 for s in seen))
    if grab:   # photo with a grey/gradient studio bg (models): refine with OpenCV GrabCut seeded by the flood fill
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
 "her-cozy": dict(bg=stripes, items=[
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
}


def build(name):
    L = LAYOUTS[name]
    canvas = L["bg"]().convert("RGBA")
    for f, x, y, w, rot, tol, *g in L["items"]:
        place(canvas, cut(f, tol, bool(g)), x, y, w, rot)
    for s in L.get("stickers", []):
        sticker(canvas, *s)
    OUT.mkdir(parents=True, exist_ok=True)
    p = OUT / f"{name}.png"; canvas.convert("RGB").save(p, quality=95); print(p)


if __name__ == "__main__":
    for n in (sys.argv[1:] or LAYOUTS):
        build(n)
