"""Etsy listing photos (2700x2024) for Chaos Cards, sold in the FreshlyMadeFL shop at $4.99.
Uses the product's own palette (green/cream/burgundy/gold) so photos match the real file.
Needs out/chaos-cards/*.png (cut from the PDF). Run: python specs/make_chaos_listing.py
"""
import pathlib, subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
D = ROOT / "out" / "chaos-cards"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@800&family=Inter:wght@500;700'
         '&family=Fraunces:ital,opsz,wght@1,9..144,500&display=swap">')
BG, INK, POP, GOLD, CREAM = "#2F4A3A", "#F4EBDD", "#F8E2A8", "#B0862F", "#F4EBDD"
SPARK = ('<svg class="sp {c}" viewBox="0 0 100 100"><path d="M50 0C54 34 66 46 100 50C66 54 54 66 50 100C46 66 34 54 0 50C34 46 46 34 50 0Z"/></svg>')
CSS = f"""*{{box-sizing:border-box}}html,body{{margin:0;width:2700px;height:2024px;overflow:hidden}}
body{{background:{BG};color:{INK};font-family:Inter,sans-serif;position:relative}}
.blob{{position:absolute;border-radius:50%;background:rgba(244,235,221,.08)}}
.sp{{position:absolute;fill:{POP}}}.sp.w{{fill:rgba(244,235,221,.85)}}.sp.r{{fill:#E0767C}}
.pill{{display:inline-block;background:{POP};color:{BG};font:700 46px Inter;letter-spacing:.08em;padding:18px 40px;border-radius:60px}}
h1{{margin:0;font:800 230px/.92 Poppins;letter-spacing:-6px}}h1 .p{{color:{POP}}}
.kick{{font:700 44px Inter;letter-spacing:.2em;color:{POP}}}
h2{{margin:18px 0 0;font:800 128px/1 Poppins;letter-spacing:-3px}}
.c{{position:absolute;border-radius:26px;box-shadow:0 24px 60px rgba(0,0,0,.35)}}
.box{{background:{CREAM};color:{BG};border:6px solid {POP};border-radius:34px;padding:34px 50px;font:700 56px/1.15 Inter;box-shadow:0 16px 40px rgba(0,0,0,.3)}}
.box b{{font:800 96px Poppins;color:#9E2B32;letter-spacing:-2px}}
.note{{position:absolute;right:70px;bottom:46px;font:500 34px Inter;opacity:.6}}
.sq{{position:absolute;left:338px;top:0;width:2024px;height:2024px}}
"""


def deco():
    return ('<div class="blob" style="width:900px;height:900px;left:-380px;top:-380px"></div>'
            '<div class="blob" style="width:1000px;height:1000px;right:-420px;bottom:-460px"></div>'
            + SPARK.format(c="") .replace('class="sp "', 'class="sp" style="left:120px;top:150px;width:110px"')
            + SPARK.format(c="r").replace('class="sp r"', 'class="sp r" style="right:140px;top:200px;width:80px"')
            + SPARK.format(c="w").replace('class="sp w"', 'class="sp w" style="left:200px;bottom:170px;width:60px"')
            + SPARK.format(c="w").replace('class="sp w"', 'class="sp w" style="right:260px;bottom:260px;width:50px"'))


def card(n, x, y, w, rot):
    return f'<img class="c" src="{(D / f"card{n:02d}.png").as_uri()}" style="left:{x}px;top:{y}px;width:{w}px;transform:rotate({rot}deg)">'


P = {}
# 1. Thumbnail: everything inside the centered 2024 square
P["01-thumb"] = f"""{deco()}<div class="sq">
<div style="position:absolute;top:120px;left:0;right:0;text-align:center"><span class="pill">PRINTABLE · INSTANT DOWNLOAD</span></div>
<h1 style="position:absolute;top:300px;left:0;right:0;text-align:center">White Elephant<br><span class="p">Chaos Cards</span></h1>
{card(1, 260, 870, 470, -10)}{card(21, 777, 820, 470, 0)}{card(13, 1294, 870, 470, 10)}
<div class="box" style="position:absolute;left:50%;transform:translateX(-50%);bottom:90px;white-space:nowrap;text-align:center">
<b>36</b> twist cards · works with any gift swap</div></div>"""

# 2. Real card sheet
P["02-sheet"] = f"""{deco()}
<div style="position:absolute;left:170px;top:330px;width:1100px">
<div class="kick">WHAT YOU GET</div><h2>36 cards,<br>4 kinds of<br><span style="color:{POP}">chaos</span></h2>
<div style="margin-top:70px;display:grid;gap:30px;font:500 52px/1.3 Inter">
<div><span style="color:#E0767C;font-weight:700">STEAL</span> take someone's gift</div>
<div><span style="color:#9FC2A8;font-weight:700">SWAP</span> trade gifts around</div>
<div><span style="color:{POP};font-weight:700">SAVE IT</span> pocket it, play it later</div>
<div><span style="color:#CBB9A6;font-weight:700">WILD</span> changes it for everyone</div></div></div>
<img class="c" src="{(D / 'sheet1.png').as_uri()}" style="right:200px;top:150px;height:1720px;border-radius:10px;transform:rotate(2deg)">
<div class="note">Print at home on cardstock. 9 cards per page.</div>"""

# 3. Funny card close-ups
P["03-funny"] = f"""{deco()}
<div style="position:absolute;top:150px;left:0;right:0;text-align:center"><div class="kick">READ IT OUT LOUD</div>
<h2>Then watch the <span style="color:{POP}">drama</span></h2></div>
{card(12, 260, 560, 640, -6)}{card(28, 1030, 520, 640, 0)}{card(21, 1800, 560, 640, 6)}"""

# 4. Rules page
P["04-rules"] = f"""{deco()}
<div style="position:absolute;left:170px;top:420px;width:900px">
<div class="kick">EASY TO PLAY</div><h2>Learn it in<br><span style="color:{POP}">30 seconds</span></h2>
<div style="margin-top:70px;font:500 56px/1.45 Inter">Play your usual white elephant or Yankee swap. Open or steal a gift? <b style="color:{POP}">Draw a card.</b></div></div>
<img class="c" src="{(D / 'rules.png').as_uri()}" style="right:220px;top:150px;height:1720px;border-radius:10px;transform:rotate(-2deg)">
<div class="note">Rules page included.</div>"""

# 5. What's included + steps
P["05-included"] = f"""{deco()}
<div style="position:absolute;left:150px;top:260px;width:1080px">
<div class="kick">WHAT'S INCLUDED</div><h2>Print, cut,<br><span style="color:{POP}">shuffle.</span></h2>
<div style="margin-top:80px;display:grid;gap:40px;font:500 56px/1.3 Inter">
<div>✦ 1 PDF, 6 pages, US Letter</div><div>✦ 34 twist cards + 2 blank cards</div>
<div>✦ Rules page and cover</div><div>✦ Print again for every party</div></div>
<div class="box" style="margin-top:80px;display:inline-block">Instant download · no shipping</div></div>
<img class="c" src="{(D / 'cover.png').as_uri()}" style="right:230px;top:240px;height:1540px;border-radius:10px;transform:rotate(3deg)">
<div class="note">Digital file only. Nothing will be shipped.</div>"""

OUT = ROOT / "out" / "chaos-listing"
OUT.mkdir(exist_ok=True)
for name, body in P.items():
    f = OUT / f"_{name}.html"
    f.write_text(f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{body}</body></html>', encoding="utf-8")
    png = OUT / f"chaos-{name}.png"
    subprocess.run([EDGE, "--headless", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--window-size=2700,2024", "--virtual-time-budget=6000", f"--screenshot={png}", f.as_uri()],
                   check=True, capture_output=True)
    print(png.name)
