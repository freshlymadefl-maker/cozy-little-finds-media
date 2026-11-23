"""Remove a plain white/light background from a product photo and trim it.

Usage: python cutout.py in.png out.png [tolerance]
Flood-fills from every border pixel through near-white pixels, makes them
transparent, feathers the edge slightly and crops to the object.
"""
import sys
from collections import deque
from PIL import Image, ImageFilter


def cutout(src, dst, tol=28):
    im = Image.open(src).convert("RGBA")
    w, h = im.size
    px = im.load()
    bg = [0] * (w * h)
    q = deque()

    def light(x, y):
        r, g, b, _ = px[x, y]
        return r > 255 - tol and g > 255 - tol and b > 255 - tol

    for x in range(w):
        for y in (0, h - 1):
            if light(x, y) and not bg[y * w + x]:
                bg[y * w + x] = 1; q.append((x, y))
    for y in range(h):
        for x in (0, w - 1):
            if light(x, y) and not bg[y * w + x]:
                bg[y * w + x] = 1; q.append((x, y))
    while q:
        x, y = q.popleft()
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < w and 0 <= ny < h and not bg[ny * w + nx] and light(nx, ny):
                bg[ny * w + nx] = 1; q.append((nx, ny))

    mask = Image.new("L", (w, h), 255)
    mp = mask.load()
    for y in range(h):
        for x in range(w):
            if bg[y * w + x]:
                mp[x, y] = 0
    mask = mask.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2))
    im.putalpha(mask)
    box = mask.point(lambda v: 255 if v > 20 else 0).getbbox()
    im.crop(box).save(dst)
    print(dst, im.crop(box).size)


if __name__ == "__main__":
    cutout(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 28)
