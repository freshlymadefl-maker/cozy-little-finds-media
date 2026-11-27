"""Black Friday deal Stories (Nov 26 2026) in the owner's liked deal-Story style:
real product photos, price pills "$now reg $was | $X off", IG-native text boxes,
space left for the IG link sticker. Prices captured from Walmart Creator's
"Best of ...: Black Friday Deals" carousels on Nov 26 2026."""
import subprocess, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "posts" / "bf-stories" / "src"
OUT = ROOT / "posts" / "bf-stories"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

FONTS = '<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Inter:wght@500;700;800&display=swap" rel="stylesheet">'

GRID = [  # file, now, was
    ("slushi.jpg", 169, 319), ("dyson.jpg", 399.99, 729.99), ("delonghi.jpg", 79, 149.95),
    ("shark.jpg", 144, 379.99), ("sheets.jpg", 16.99, 38.99), ("nex.png", 209, 299),
    ("knives.png", 31.99, 199.99), ("carote.jpg", 77, 159.99), ("clog.jpg", 27.99, 60),
]

def money(v):
    return f"${v:,.2f}".replace(".00", "")

def pill(now, was, size=1.0):
    off = round(was - now)
    return (f'<div class="pill" style="font-size:{26*size}px"><b>{money(now)}</b>'
            f'<span class="reg">reg <s>{money(was)}</s></span>'
            f'<span class="off">${off} off</span></div>')

BOW = '''<svg viewBox="0 0 400 170" width="{w}" style="display:block;margin:0 auto">
<g fill="none" stroke="{c}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
<path d="M200 70 C150 10, 60 0, 40 40 C25 75, 120 95, 200 70 Z"/>
<path d="M200 70 C250 10, 340 0, 360 40 C375 75, 280 95, 200 70 Z"/>
<path d="M190 72 C165 110, 140 140, 110 165"/><path d="M210 72 C235 110, 260 140, 290 165"/>
<ellipse cx="200" cy="72" rx="16" ry="12"/></g></svg>'''

BASE_CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1920px;overflow:hidden;font-family:Inter,sans-serif}
.pill{display:inline-flex;align-items:center;gap:8px;background:#fff;border-radius:999px;padding:8px 16px;
 color:#c8102e;box-shadow:0 3px 10px rgba(0,0,0,.18);white-space:nowrap}
.pill b{font-weight:800;font-size:1.35em}
.pill .reg{color:#555;font-weight:500;font-size:.9em}
.pill .off{background:#fde3e6;color:#c8102e;border-radius:999px;padding:3px 10px;font-weight:700;font-size:.8em}
.paid{position:absolute;font-family:'DM Serif Display',serif;color:#fff;font-size:34px;opacity:.95}
"""

def grid_story():
    tiles = "".join(
        f'<div class="tile"><div class="ph"><img src="{(SRC/f).as_uri()}"></div>{pill(n, w, .66)}</div>'
        for f, n, w in GRID)
    html = f"""<html><head>{FONTS}<style>{BASE_CSS}
body{{background:#b8323a}}
h1{{font-family:'DM Serif Display',serif;color:#fff;font-size:118px;line-height:.98;text-align:center;letter-spacing:-2px;margin-top:8px}}
h1 i{{color:#f8e2a8}}
.sub{{text-align:center;color:#fff;font-size:34px;font-weight:700;margin-top:18px}}
.gap{{height:110px}}
.grid{{margin:0 30px;background:rgba(0,0,0,.10);border-radius:40px;padding:26px 18px 30px;
 display:grid;grid-template-columns:repeat(3,1fr);gap:34px 10px}}
.tile{{display:flex;flex-direction:column;align-items:center;gap:10px}}
.ph{{width:290px;height:290px;background:#fff;border-radius:28px;overflow:hidden;display:flex;align-items:center;justify-content:center}}
.ph img{{max-width:88%;max-height:88%;object-fit:contain}}
</style></head><body>
<div style="padding-top:90px">{BOW.format(w=330, c='#f4ebdd')}</div>
<h1>All the Walmart<br><i>Black Friday</i> deals!</h1>
<div class="sub">the ones I'd actually buy ‼️</div>
<div class="gap"></div>
<div class="grid">{tiles}</div>
<div class="paid" style="left:60px;bottom:40px">Paid link · #WalmartPartner</div>
<div class="paid" style="right:60px;bottom:40px;font-size:28px">prices as of 11/26, can change fast</div>
</body></html>"""
    return html

FRAME = '''<svg viewBox="0 0 1000 1700" style="position:absolute;left:40px;top:110px;width:1000px;height:1700px">
<g fill="none" stroke="#4f6b5e" stroke-width="5" stroke-linecap="round">
<path d="M90 30 H910 Q920 30 925 45 L930 70 H970 V1630 H930 L925 1655 Q920 1670 910 1670 H90 Q80 1670 75 1655 L70 1630 H30 V70 H70 L75 45 Q80 30 90 30 Z"/>
<path d="M110 60 H890 L900 95 H940 V1605 H900 L890 1640 H110 L100 1605 H60 V95 H100 Z" stroke-width="3"/>
</g></svg>'''

def single(fname, out, title, now, was, line1, tilt, imgh=1000):
    html = f"""<html><head>{FONTS}<style>{BASE_CSS}
body{{background:#8fa79b;position:relative}}
.box{{position:absolute;left:50%;transform:translateX(-50%);font-family:'DM Serif Display',serif;text-align:center;padding:14px 28px;white-space:nowrap}}
.t1{{top:250px;background:#c2187a;color:#fff;font-size:70px}}
.card{{position:absolute;left:150px;top:400px;width:780px;height:{imgh}px;background:#fff;border-radius:36px;overflow:hidden;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 30px rgba(0,0,0,.15)}}
.card img{{max-width:92%;max-height:94%;object-fit:contain}}
.pw{{position:absolute;top:{400+imgh-60}px;left:0;width:1080px;text-align:center}}
.t2{{top:{400+imgh+70}px;background:#fbd9ea;color:#a8125f;font-size:52px;line-height:1.15;white-space:normal;width:820px}}
.t3{{top:{400+imgh+250}px;background:#c2187a;color:#fff;font-size:44px;transform:translateX(-50%) rotate(-3deg)}}
</style></head><body>
{FRAME}
<div class="box t1">{title}</div>
<div class="card"><img src="{(SRC/fname).as_uri()}"></div>
<div class="pw">{pill(now, was, 1.5)}</div>
<div class="box t2">{line1}</div>
<div class="box t3">{tilt}</div>
<div class="paid" style="left:0;width:1080px;text-align:center;bottom:50px;color:#2f4a3a;font-size:30px">Paid link · #WalmartPartner · price as of 11/26</div>
</body></html>"""
    return out, html

def render(name, html):
    page = OUT / f"{name}.html"
    page.write_text(html, encoding="utf-8")
    png = OUT / f"{name}.png"
    subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--window-size=1080,1920",
                    "--virtual-time-budget=6000", f"--screenshot={png.as_posix()}", page.as_uri()], check=True,
                   capture_output=True)
    print(png)

if __name__ == "__main__":
    render("bf-1-grid", grid_story())
    for name, html in [
        single("earrings.jpg", "bf-2-earrings", "Diamond studs – 50% off‼️", 64, 128,
               "half a carat of sparkle for<br>under $65… yes really", "(the easiest gift for her!)", 860),
        single("pjs_crop.jpg", "bf-3-pjs", "Velvet PJ set – 60% off‼️", 18.99, 46.99,
               "softest set for Christmas<br>morning, under $20", "(what all the girls want!)", 980),
        single("clog.jpg", "bf-4-clog", "Suede clog slippers – half off‼️", 27.99, 60,
               "the cozy clog everyone's<br>wearing, under $30", "(buy one, keep one)", 820),
    ]:
        render(name, html)
