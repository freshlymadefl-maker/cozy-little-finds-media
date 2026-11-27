"""Daily pins run Nov 26-27 2026 (cozy-daily-pins): 8 Walmart single-product arch pins + 7 type-only Amazon list pins.
Photos: untouched i5.walmartimages.com images in src/dp1127 (gitignored). ONLY=name1,name2 re-renders just those."""
import pathlib, subprocess, os
ROOT = pathlib.Path(__file__).resolve().parent.parent
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;'
         '1,9..144,400;1,9..144,500&family=DM+Sans:wght@500;700&family=Courier+Prime:wght@700&display=swap">')
OUT = ROOT / "posts" / "pins-1127"
OUT.mkdir(parents=True, exist_ok=True)
ONLY = set(filter(None, os.environ.get("ONLY", "").split(",")))
SRC = ROOT / "src" / "dp1127"
P = lambda n: next(SRC.glob(n + ".*")).as_uri()
FIT = ("<script>document.fonts.ready.then(()=>{document.querySelectorAll('.fit').forEach(e=>{const H=+e.dataset.h,M=+e.dataset.max;"
       "let s=50;e.style.fontSize=s+'px';while(s<M){e.style.fontSize=(s+2)+'px';"
       "if(e.offsetHeight>H||e.scrollWidth>e.parentElement.clientWidth){e.style.fontSize=s+'px';break}s+=2}})})</script>")
BASE = ("*{box-sizing:border-box}html,body{margin:0;overflow:hidden;width:1000px;height:1500px}"
        "body{position:relative;font-family:'DM Sans',sans-serif;color:#2F4A3A;background:#F4EBDD}"
        ".eb{position:absolute;left:0;right:0;top:70px;text-align:center;font:700 30px 'Courier Prime',monospace;letter-spacing:.2em;color:#B07F2E}"
        ".pill{position:absolute;left:50%;transform:translateX(-50%);bottom:56px;white-space:nowrap;background:#2F4A3A;color:#F4EBDD;font:700 34px 'DM Sans';padding:22px 46px;border-radius:60px}")
PROD = BASE + """
.hook{position:absolute;left:50px;right:50px;top:116px;height:320px;display:flex;align-items:center;justify-content:center;text-align:center;font:600 90px/1.03 Fraunces,serif;letter-spacing:-.015em}
.hook em{font-style:italic;font-weight:400;color:#9E2B32}
.frame{position:absolute;left:150px;right:150px;top:460px;height:760px;border-radius:360px 360px 26px 26px;overflow:hidden;background:#fff;box-shadow:0 16px 36px rgba(47,74,58,.16)}
.frame img{width:100%;height:100%;object-fit:contain;padding:90px 50px 30px}
.name{position:absolute;left:50px;right:50px;top:1246px;text-align:center;font:italic 400 42px Fraunces,serif;color:#3A2A20}"""
LIST = BASE + """
.title{position:absolute;left:60px;right:60px;top:120px;height:300px;display:flex;align-items:center;justify-content:center;text-align:center;font:600 96px/1.02 Fraunces,serif;letter-spacing:-.015em}
.title em{font-style:italic;font-weight:400;color:#9E2B32}
.arch{position:absolute;left:110px;right:110px;top:450px;height:830px;border:3px solid #2F4A3A;border-radius:390px 390px 24px 24px;background:#FBF5EC}
.arch .in{position:absolute;left:60px;right:60px;top:190px;bottom:50px;display:flex;flex-direction:column;justify-content:space-between}
.arch .star{position:absolute;left:0;right:0;top:90px;text-align:center;font:400 54px Fraunces,serif;color:#B07F2E}
.row{display:flex;align-items:baseline;gap:22px;border-bottom:1.5px dashed rgba(47,74,58,.3);padding-bottom:16px}
.row:last-child{border-bottom:none}
.row b{font:700 30px 'Courier Prime',monospace;color:#B07F2E;min-width:44px}
.row span{font:italic 400 44px/1.1 Fraunces,serif;color:#3A2A20}
.foot{position:absolute;left:0;right:0;top:1300px;text-align:center;font:700 26px 'Courier Prime',monospace;letter-spacing:.16em;color:#2F4A3A}"""

# name, img, eyebrow, hook, product name
WALMART = [
 ("dp-marc", "marc", "TRENDING GIFT · PERFUME MINIS", "Four tiny bottles. <em>One very happy her.</em>", "Marc Jacobs Daisy Mini Gift Set"),
 ("dp-sunbeam", "sunbeam", "COZY GIFTS FOR HER", "Faux fur. Heated. <em>No getting up.</em>", "Sunbeam Heated Faux Fur Throw"),
 ("dp-clog", "clog", "TRENDING · SUEDE CLOG SLIPPERS", "The cozy clog look, <em>minus the waitlist.</em>", "Joyspun Women's Suede Clog Slippers"),
 ("dp-orchid", "orchid", "GIFTS FOR HER · LEGO BOTANICALS", "Flowers she <em>can't</em> forget to water.", "LEGO Botanicals Orchid"),
 ("dp-jewel", "jewel", "STOCKING STUFFER FOR HER", "Every earring, <em>finally</em> in one place.", "Casegrace Mini Travel Jewelry Case"),
 ("dp-kcole", "kcole", "GIFTS FOR HIM · COLOGNE SET", "Three scents. <em>He'll pick a favorite.</em>", "Kenneth Cole Mini Cologne Set"),
 ("dp-mukclog", "mukclog", "STOCKING STUFFER · SLIPPERS", "Santa, but make it <em>slippers.</em>", "MUK LUKS Cozy Holiday Clog Slippers"),
 ("dp-tytan", "tytan", "WHAT KIDS WANT · MAGNETIC TILES", "Quiet building time. <em>Finally.</em>", "Tytan 60-Piece Magnetic Tiles"),
]
# name, eyebrow, title, rows, foot
AMAZON = [
 ("dp-a-trend", "TRENDING GIFTS FOR HER", "What's on <em>her</em> list", ["Perfume discovery set", "Pearl huggie earrings", "Lip butter balm minis", "The lymphatic face brush", "A red cardigan", "A cherry bag charm"], "ALL 20 IN ONE LIST"),
 ("dp-a-kids", "THE 2026 KID WISH LIST", "Top of <em>every</em> letter to Santa", ["Squishy advent calendars", "Toniebox 2", "Beyblade X", "Jellycat", "Yoto Mini", "Magna-Tiles"], "ALL 17 IN ONE LIST"),
 ("dp-a-unplug", "GIFTS TO UNPLUG", "Phones down,<br><em>fun&nbsp;up.</em>", ["Instax Mini 12", "Ticket to Ride", "Codenames", "A cozy 1000-piece puzzle", "LEGO wildflower bouquet", "A watercolor set"], "16 FAMILY GIFTS, ONE LIST"),
 ("dp-a-host", "HOSTING CHRISTMAS", "What guests <em>actually</em> notice", ["The candle by the door", "A kettle for cocoa", "A pretty cake stand", "Coupes for the toast", "A board worth photographing"], "CANDLES TO COUPES, ONE LIST"),
 ("dp-a-him", "GIFTS FOR HIM", "For the man who wants <em>“nothing”</em>", ["He'll use it every day", "An upgrade, not a gadget", "Fits under the tree", "Zero assembly required"], "THE RULES I SHOP BY"),
 ("dp-a-stock", "STOCKING STUFFERS FOR HER", "Small, cute, <em>actually used.</em>", ["Fits in the stocking", "Used by New Year's", "No clutter, no junk", "Looks pricier than it is"], "THE RULES I SHOP BY"),
 ("dp-a-luxe", "GIFTS THAT LOOK EXPENSIVE", "Looks <em>splurgy.</em> Isn't.", ["Velvet, gold + glass", "Gift-box ready", "4.4 stars or better", "Nobody needs to know"], "THE RULES I SHOP BY"),
]


def shot(name, css, body):
    if ONLY and name not in ONLY:
        return
    f = ROOT / f"_{name}.html"
    f.write_text(f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{css}</style></head><body>{body}{FIT}</body></html>', encoding="utf-8")
    subprocess.run([EDGE, "--headless", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1", "--window-size=1000,1500",
                    "--virtual-time-budget=6000", f"--screenshot={OUT / (name + '.png')}", f.as_uri()], check=True, capture_output=True)
    f.unlink()
    print(name)


for name, img, eb, hook, prod in WALMART:
    shot(name, PROD, f'<div class="eb">{eb}</div><div class="hook"><div class="fit" data-h="320" data-max="124">{hook}</div></div>'
         f'<div class="frame"><img src="{P(img)}"></div><div class="name">{prod}</div><div class="pill">Shop it at Walmart &#10022;</div>')
for name, eb, title, rows, foot in AMAZON:
    r = "".join(f'<div class="row"><b>{i:02d}</b><span>{t}</span></div>' for i, t in enumerate(rows, 1))
    shot(name, LIST, f'<div class="eb">{eb}</div><div class="title"><div class="fit" data-h="300" data-max="120">{title}</div></div>'
         f'<div class="arch"><div class="star">&#10022;</div><div class="in">{r}</div></div><div class="foot">{foot}</div>'
         f'<div class="pill">Shop the list on Amazon &#10022;</div>')
