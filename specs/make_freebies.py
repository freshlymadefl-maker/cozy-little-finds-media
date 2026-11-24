"""Free printables for Cozy Little Finds (Nov 24 2026): Cheesy Christmas Movie Bingo (4 cards) and a Gift Tracker.
Outputs out/Christmas-Movie-Bingo.pdf, out/Christmas-Gift-Tracker.pdf. Run: python specs/make_freebies.py
"""
import pathlib, random, subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "out"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;'
         '1,9..144,500&family=DM+Sans:wght@500;700&family=Courier+Prime:wght@700&display=swap">')
XL = ('<a href="https://freshlymadefl.etsy.com/listing/4624952800/white-elephant-game-cards-printable" '
      'style="color:#9E2B32;font-weight:700;text-decoration:none">Hosting a gift swap? Get Chaos Cards, the white elephant twist game &#8594;</a>')
BASE = """@page{size:8.5in 11in;margin:0}*{box-sizing:border-box}html,body{margin:0}
body{font-family:'DM Sans',sans-serif;color:#2F4A3A;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:8.5in;height:11in;position:relative;overflow:hidden;page-break-after:always;background:#F4EBDD;padding:.55in .6in}
.eb{font:700 10pt 'Courier Prime',monospace;letter-spacing:.24em;color:#9E2B32;text-align:center}
h1{font:600 34pt/1 Fraunces,serif;text-align:center;margin:.08in 0 .04in}h1 em{font-style:italic;color:#9E2B32;font-weight:500}
.sub{text-align:center;font:500 11pt 'DM Sans';opacity:.8}
.ft{position:absolute;left:0;right:0;bottom:.28in;line-height:1.6;text-align:center;font:500 9pt 'DM Sans';opacity:.7}"""

SQ = ["Big-city career woman moves back home", "The small-town bakery is in trouble", "Hot cocoa with a mountain of whipped cream",
      "Snow starts at the perfect moment", "An ugly sweater", "The Christmas festival committee meets", "Someone says \"the true meaning of Christmas\"",
      "An almost-kiss gets interrupted", "Flannel shirt", "The ex shows up", "A Christmas tree farm", "Ice skating scene", "A secret prince",
      "Mistletoe moment", "Gingerbread contest", "Cookie-baking montage", "The inn might have to close", "Grandma gives life advice",
      "Snowball fight", "The laptop closes for good", "A dog in a holiday sweater", "A big misunderstanding", "Kiss in the snow",
      "Matching pajamas", "Sleigh ride", "Last-minute grand gesture", "Town tree lighting", "Carolers at the door",
      "\"I forgot what Christmas felt like\"", "Fake dating for the holidays", "Hot guy chopping wood"]


def bingo(seed):
    r = random.Random(seed)
    cells = r.sample(SQ, 24)
    cells.insert(12, "FREE<br><em>(pour the wine)</em>")
    tds = "".join(f'<div class="c{" fr" if i == 12 else ""}">{t}</div>' for i, t in enumerate(cells))
    return f"""<div class="page"><div class="eb">MOVIE NIGHT · CARD {seed}</div><h1>Cheesy Christmas <em>Movie Bingo</em></h1>
<div class="sub">Mark a square every time it happens. Five in a row picks the next movie.</div>
<div class="bg">{''.join(f'<div class="h">{l}</div>' for l in 'BINGO')}{tds}</div>
<div class="ft">{XL}<br>Free printable from @cozylittlefindsdaily · for personal use</div></div>"""


BCSS = """.bg{display:grid;grid-template-columns:repeat(5,1fr);gap:.06in;margin-top:.28in}
.h{font:600 30pt Fraunces,serif;color:#9E2B32;text-align:center;padding-bottom:.04in}
.c{height:1.42in;background:#FFFBF4;border:1.5px solid #2F4A3A;border-radius:.08in;display:flex;align-items:center;justify-content:center;
text-align:center;padding:.08in;font:500 10.5pt/1.25 'DM Sans'}
.c.fr{background:#2F4A3A;color:#F4EBDD;font:600 15pt/1.15 Fraunces,serif}.c.fr em{font:italic 500 10pt Fraunces;color:#F8E2A8}"""

TCSS = """table{width:100%;border-collapse:collapse;margin-top:.25in;font:500 10.5pt 'DM Sans'}
th{background:#2F4A3A;color:#F4EBDD;font:700 9pt 'Courier Prime',monospace;letter-spacing:.12em;padding:.08in;text-align:left}
td{height:.34in;border-bottom:1px solid #2F4A3A44;background:#FFFBF4}td.ck{width:.6in;text-align:center;color:#2F4A3A66}
.two{display:grid;grid-template-columns:1fr 1fr;gap:.25in;margin-top:.25in}
.box{border:1.5px solid #2F4A3A;border-radius:.1in;padding:.14in .18in;background:#FFFBF4;height:1.75in}
.box b{font:600 14pt Fraunces,serif;color:#9E2B32}.ln{border-bottom:1px solid #2F4A3A44;height:.26in}"""


def tracker():
    rows = "".join('<tr><td></td><td></td><td style="width:1in"></td><td class="ck">☐</td><td class="ck">☐</td></tr>' for _ in range(16))
    lines = '<div class="ln"></div>' * 4
    return f"""<div class="page"><div class="eb">FREE PRINTABLE</div><h1>The Christmas <em>Gift Tracker</em></h1>
<div class="sub">Who you're shopping for, what you're getting them, and whether it's actually wrapped.</div>
<table><tr><th>FOR</th><th>GIFT IDEA</th><th>BUDGET</th><th>BOUGHT</th><th>WRAPPED</th></tr>{rows}</table>
<div class="two"><div class="box"><b>Stocking stuffers</b>{lines}</div><div class="box"><b>Don't forget</b>
<div style="font:500 9.5pt 'DM Sans';opacity:.75;margin-top:.03in">teachers · mail carrier · hostess · dog</div>{lines}</div></div>
<div class="ft">{XL}<br>Stuck on ideas? My gift guides are linked in my bio: @cozylittlefindsdaily</div></div>"""


def build(name, css, pages):
    src = OUT / f"_{name}.html"
    src.write_text(f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{BASE}{css}</style></head><body>{pages}</body></html>', encoding="utf-8")
    pdf = OUT / f"{name}.pdf"
    subprocess.run([EDGE, "--headless", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=8000",
                    f"--print-to-pdf={pdf}", src.as_uri()], check=True, capture_output=True)
    print(pdf.name, pdf.stat().st_size)


build("Christmas-Movie-Bingo", BCSS, "".join(bingo(s) for s in (1, 2, 3, 4)))
build("Christmas-Gift-Tracker", TCSS, tracker())
