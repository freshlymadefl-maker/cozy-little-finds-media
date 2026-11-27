"""'The Amazon List I Sent My Husband' carousel (Nov 26 2026), in the format the owner loved
(Bloom and Babe style): cozy film-look cover with a huge stacked white condensed headline,
then one product per slide with a chatty serif line on a dark see-through band.
Cover photo: Unsplash (free license) photo-1701849392147 (woman from behind, no face)."""
import subprocess, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
OUT = ROOT / "posts" / "husband-list"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@600;700&'
         'family=Playfair+Display:ital,wght@0,500;1,500&display=swap" rel="stylesheet">')
BG = (OUT / "cover-bg.jpg").as_uri()

BASE = """*{margin:0;padding:0;box-sizing:border-box} body{width:1080px;height:1350px;overflow:hidden;position:relative}
.bg{position:absolute;inset:0;background:url('%s') center 35%%/cover}
""" % BG

def cover():
    words = "The Amazon List I Sent My Husband So He Stops Asking What I Want".split()
    lines = ["The", "Amazon", "List I Sent", "My", "Husband", "So He", "Stops", "Asking", "What I", "Want"]
    h = "".join(f"<div>{l}</div>" for l in lines)
    return f"""<html><head>{FONTS}<style>{BASE}
.bg{{filter:brightness(.78) saturate(1.05) sepia(.12)}}
.t{{position:absolute;left:0;right:0;top:95px;text-align:center;font-family:Oswald;font-weight:700;color:#fff;
font-size:116px;line-height:.9;letter-spacing:-2px;text-shadow:0 4px 22px rgba(0,0,0,.45)}}
.tag{{position:absolute;bottom:28px;left:0;right:0;text-align:center;font-family:'Playfair Display';font-style:italic;
color:#fff;font-size:40px;text-shadow:0 2px 10px rgba(0,0,0,.6)}}
</style></head><body><div class="bg"></div><div class="t">{h}</div>
<div class="tag">swipe for the list →</div></body></html>"""

ITEMS = [
    ("bfd/cardi_c.jpg", "The <i>Barefoot Dreams</i> cardigan. Yes, it really is worth the hype."),
    ("trend/nest.jpg", "A <i>NEST Holiday</i> candle, so the whole house smells like Christmas."),
    ("bf/stanley.png", "The <i>Stanley</i>, in a color I'd actually pick for myself."),
    ("u25/pillow_c.png", "A satin pillowcase. Tiny gift, <i>big</i> hair difference."),
    ("loafers.png", "Velvet loafers in <i>oxblood</i>, the color of the season."),
    ("bag.png", "A quilted bag that looks <i>way</i> more expensive than it is."),
    ("earrings.png", "Pearl drops for every <i>holiday party</i> on the calendar."),
    ("bfd/BDWCC27064_STONE_MULTI_FRONT.jpg", "Barefoot Dreams socks. The <i>coziest</i> stocking stuffer."),
]

def item(img, line):
    return f"""<html><head>{FONTS}<style>{BASE}
.bg{{filter:blur(26px) brightness(.62) saturate(1.1);transform:scale(1.15)}}
.card{{position:absolute;left:110px;top:110px;width:860px;height:860px;background:#fbf8f3;border-radius:28px;
display:flex;align-items:center;justify-content:center;overflow:hidden;box-shadow:0 18px 50px rgba(0,0,0,.35)}}
.card img{{max-width:86%;max-height:86%;object-fit:contain}}
.band{{position:absolute;left:70px;right:70px;top:1010px;background:rgba(28,44,34,.82);padding:30px 40px;
font-family:'Playfair Display';font-weight:500;color:#fff;font-size:52px;line-height:1.18;text-align:center}}
.band i{{color:#f3dfa2}}
.ad{{position:absolute;right:40px;bottom:26px;font-family:Oswald;color:rgba(255,255,255,.85);font-size:26px;letter-spacing:1px}}
</style></head><body><div class="bg"></div><div class="card"><img src="{(SRC/img).as_uri()}"></div>
<div class="band">{line}</div><div class="ad">#AD</div></body></html>"""

def last():
    return f"""<html><head>{FONTS}<style>{BASE}
.bg{{filter:brightness(.55) sepia(.15)}}
.t{{position:absolute;left:80px;right:80px;top:330px;text-align:center;color:#fff}}
.t .a{{font-family:Oswald;font-weight:700;font-size:118px;line-height:.95}}
.t .b{{font-family:'Playfair Display';font-style:italic;font-size:56px;margin-top:40px;line-height:1.25}}
.pill{{display:inline-block;margin-top:56px;background:#fff;color:#1c2c22;font-family:Oswald;font-weight:600;
font-size:52px;padding:20px 46px;border-radius:999px}}
</style></head><body><div class="bg"></div><div class="t">
<div class="a">Want the whole list?</div>
<div class="b">Send this to him (or just screenshot it).</div>
<div class="pill">Comment SPOIL for the links</div></div></body></html>"""

def render(name, html):
    p = OUT / f"{name}.html"
    p.write_text(html, encoding="utf-8")
    png = OUT / f"{name}.png"
    subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--window-size=1080,1350",
                    "--virtual-time-budget=6000", f"--screenshot={png.as_posix()}", p.as_uri()], check=True,
                   capture_output=True)

if __name__ == "__main__":
    render("01-cover", cover())
    for i, (img, line) in enumerate(ITEMS, start=2):
        render(f"{i:02d}-item", item(img, line))
    render("10-last", last())
    print("done")
