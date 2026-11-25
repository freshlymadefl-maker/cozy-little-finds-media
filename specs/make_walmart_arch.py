"""Walmart arch carousels + product pins (Nov 25 2026). ADDED to the mix; launch Reel + lifestyle pins stay as-is.
Product photos: untouched Walmart images (src/wmp), no faces. Lifestyle photos: src/wm."""
import pathlib, subprocess, os
ONLY = set(filter(None, os.environ.get("ONLY", "").split(",")))
FILL = set()
ROOT = pathlib.Path(__file__).resolve().parent.parent
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;'
         '1,9..144,400;1,9..144,500&family=DM+Sans:wght@500;700&family=Courier+Prime:wght@700&display=swap">')
OUT = ROOT / "posts" / "walmart"
P = lambda n: (ROOT / "src" / "wmp" / f"{n}.jpg").as_uri()
L = lambda n: (ROOT / "src" / "wm" / f"{n}.jpg").as_uri()
BASE = """*{box-sizing:border-box}html,body{margin:0;overflow:hidden}body{position:relative;font-family:'DM Sans',sans-serif;color:#2F4A3A}"""
ARCH = BASE + """html,body{width:1080px;height:1350px}body{background:#F4EBDD}
.eb{position:absolute;left:0;right:0;top:70px;text-align:center;font:700 30px 'Courier Prime',monospace;letter-spacing:.18em;color:#B07F2E}
.hook{position:absolute;left:60px;right:60px;top:116px;height:296px;display:flex;align-items:center;justify-content:center;text-align:center;font:600 80px/1.03 Fraunces,serif;letter-spacing:-.015em}.hook em{font-style:italic;font-weight:400;color:#9E2B32}
.frame{position:absolute;left:210px;right:210px;top:430px;height:620px;border-radius:330px 330px 24px 24px;overflow:hidden;background:#fff;box-shadow:0 16px 36px rgba(47,74,58,.16)}
.frame img{width:100%;height:100%;object-fit:contain;padding:70px 46px 26px}
.name{position:absolute;left:60px;right:60px;top:1080px;text-align:center;font:italic 400 40px Fraunces,serif;color:#3A2A20}
.bar{position:absolute;left:0;right:0;bottom:0;height:150px;background:#2F4A3A;display:flex;align-items:center;justify-content:center;gap:20px;color:#F4EBDD;font:600 42px 'DM Sans'}
.bar b{background:#F8E2A8;color:#2F4A3A;font:700 48px 'Courier Prime',monospace;padding:8px 24px;border-radius:10px;letter-spacing:.06em}
.ad{position:absolute;right:22px;top:20px;background:#2F4A3A;color:#F4EBDD;font:700 18px 'Courier Prime',monospace;padding:4px 10px;border-radius:6px}"""
PHOTO = BASE + """html,body{width:1080px;height:1350px}
.ph{position:absolute;inset:0;background-size:cover;background-position:center}
.card{position:absolute;left:70px;right:70px;top:90px;background:#F4EBDD;border-radius:28px;padding:56px 54px 54px;text-align:center;box-shadow:0 24px 60px rgba(0,0,0,.35)}
.ceb{font:700 30px 'Courier Prime',monospace;letter-spacing:.22em;color:#9E2B32}
.t{margin-top:18px;font:600 96px/1.0 Fraunces,serif;letter-spacing:-.02em}.t em{font-style:italic;font-weight:400;color:#9E2B32}
.s{margin-top:22px;font:italic 400 40px/1.2 Fraunces,serif;color:#3A2A20}
.pill{position:absolute;left:50%;transform:translateX(-50%);bottom:120px;white-space:nowrap;background:#9E2B32;color:#F4EBDD;font:700 46px 'DM Sans';padding:26px 54px;border-radius:70px;box-shadow:0 12px 30px rgba(0,0,0,.35)}
.under{position:absolute;left:0;right:0;bottom:62px;text-align:center;font:600 32px 'DM Sans';color:#F4EBDD;text-shadow:0 2px 10px rgba(0,0,0,.7)}
.ad{position:absolute;right:22px;top:20px;background:#2F4A3A;color:#F4EBDD;font:700 18px 'Courier Prime',monospace;padding:4px 10px;border-radius:6px;z-index:3}"""
FILLCSS = ' style="object-fit:cover;padding:0"'
C = {
 "her": ("1795330796412-80b543884f4c", "WALMART GIFT GUIDE", "Cozy gifts for her <em>under $50</em>", "the ones she'll actually use", "1734898537962-2dc575c99e11", [
   ("slip-puff-trim", "JOYSPUN", "Fancy enough to <em>answer the door in.</em>", "Faux Fur Puff Scuff Slippers"),
   ("slip-litfun", "LITFUN", "Memory foam for the <em>6am lunch shift.</em>", "Chenille Knit Memory Foam Slippers"),
   ("sherpa", "LOMAO", "The couch's new <em>favorite accessory.</em>", "Sherpa Fleece Throw Blanket"),
   ("socks", "MUK LUKS", "Six pairs. <em>Zero cold feet.</em>", "Fluffy Dream Crew Socks, 6-Pack")]),
 "kids": ("1546512347-b93b3f59e231", "TRENDING TOYS 2026", "What the kids <em>actually</em> want", "so you don't have to Google it", "1703319955806-8104553f0b92", [
   ("squish", "SQUISHMALLOWS", "The one they'll <em>sleep with</em> every night.", "Hello Kitty Squishmallow, 8 in"),
   ("needoh-adv", "NEEDOH", "24 days of squish. <em>Zero glitter.</em>", "NeeDoh Advent Calendar"),
   ("beyblade", "BEYBLADE X", "Battle royale, <em>living room edition.</em>", "Beyblade X Xtreme Battle Set"),
   ("lego-unicorn", "LEGO FRIENDS", "Built in an afternoon. <em>Played all break.</em>", "Unicorn Cake Delivery Car"),
   ("magtiles", "MAGNETIC TILES", "The gift that <em>quiets the house.</em> (For an hour.)", "Magnetic Building Tiles")]),
 "host": ("1688437307687-fe226bddfab1", "HOLIDAY HOSTING", "Make your house look <em>catered</em>", "(even if dessert is store-bought)", "1763463608554-1a1d7ec7147b", [
   ("board-hecef", "HECEF", "The board that does <em>the hosting for you.</em>", "Acacia Charcuterie Board Set"),
   ("board-farb", "FARBERWARE", "Build-a-board. <em>No recipe required.</em>", "Build-a-Board Bamboo Charcuterie Board"),
   ("taper-red", "MAINSTAYS", "One red candle = <em>instant Christmas.</em>", "Red Twist Taper Candle"),
   ("taper-ivory", "MAINSTAYS", "Classic, calm, <em>candlelit.</em>", "Ivory Taper Candles, 4-Pack"),
   ("coupe-bhg", "BETTER HOMES &amp; GARDENS", "Champagne just tastes <em>better in a coupe.</em>", "Ribbed Coupe Glass")]),
 "games": ("1629760946220-5693ee4c46ac", "CHRISTMAS BREAK", "Phones-down <em>family game night</em>", "games they'll actually play", "1659480141041-c41defa79a71", [
   ("uno", "UNO", "Brutal. Ruthless. <em>Family-approved.</em>", "UNO Show 'Em No Mercy"),
   ("phase10", "PHASE 10", "The one <em>grandma always wins.</em>", "Phase 10 Card Game"),
   ("mdeal", "MONOPOLY DEAL", "Monopoly, minus the <em>three-hour fight.</em>", "Monopoly Deal Card Game"),
   ("tapple", "TAPPLE", "Fast, loud and <em>everyone can play.</em>", "Tapple Word Game"),
   ("puzzle-xmas", "MASTERPIECES", "Christmas break, <em>one piece at a time.</em>", "300-Piece EZ Grip Christmas Puzzle")]),
}


# Auto-fit: grow each .fit title until it fills its zone (owner Nov 25: "if there's extra space, the words can just be bigger")
FIT = ("<script>document.fonts.ready.then(()=>{document.querySelectorAll('.fit').forEach(e=>{const H=+e.dataset.h,M=+e.dataset.max;"
       "let s=60;e.style.fontSize=s+'px';while(s<M){e.style.fontSize=(s+2)+'px';"
       "if(e.offsetHeight>H||e.scrollWidth>e.parentElement.clientWidth){e.style.fontSize=s+'px';break}s+=2}})})</script>")


def shot(name, css, body, w, h):
    if ONLY and name not in ONLY:
        return name
    f = ROOT / f"_{name}.html"
    f.write_text(f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{css}</style></head><body>{body}{FIT}</body></html>', encoding="utf-8")
    png = OUT / f"{name}.png"
    subprocess.run([EDGE, "--headless", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1", f"--window-size={w},{h}",
                    "--virtual-time-budget=6000", f"--screenshot={png}", f.as_uri()], check=True, capture_output=True)
    return png.name


for key, (ph, eb, t, s, ph2, items) in C.items():
    n = 1
    shot(f"wm-arch-{key}-{n}", PHOTO, f'<div class="ph" style="background-image:url({L(ph)})"></div><div class="ad">#AD</div><div class="card"><div class="ceb">{eb}</div><div class="t">{t}</div><div class="s">{s}</div></div><div class="pill">Swipe for my picks &#8594;</div>', 1080, 1350)
    for img, brand, hook, prod in items:
        n += 1
        shot(f"wm-arch-{key}-{n}", ARCH, f'<div class="ad">#AD</div><div class="eb">WALMART FIND &#183; {brand}</div><div class="hook"><div class="fit" data-h="296" data-max="132">{hook}</div></div><div class="frame"><img src="{P(img)}"{FILLCSS if img in FILL else ""}></div><div class="name">{prod}</div><div class="bar">Tap to shop <span style="opacity:.6">&#183;</span> or comment <b>WALMART</b></div>', 1080, 1350)
    n += 1
    shot(f"wm-arch-{key}-{n}", PHOTO, f'<div class="ph" style="background-image:url({L(ph2)})"></div><div class="ad">#AD</div><div class="card" style="top:300px"><div class="ceb">THE WHOLE LIST</div><div class="t" style="font-size:84px">Shop it all at my <em>Walmart storefront</em></div></div><div class="pill">Comment WALMART &#10022;</div><div class="under">or tap the link in my bio</div>', 1080, 1350)
    print(key, n)

PIN = BASE + """html,body{width:1000px;height:1500px}body{background:#F4EBDD}
.eb{position:absolute;left:0;right:0;top:70px;text-align:center;font:700 30px 'Courier Prime',monospace;letter-spacing:.2em;color:#9E2B32}
.t{position:absolute;left:44px;right:44px;top:112px;height:306px;display:flex;align-items:center;justify-content:center;text-align:center;font:600 92px/1.02 Fraunces,serif;letter-spacing:-.02em}.t em{font-style:italic;font-weight:400;color:#9E2B32}
.g{position:absolute;left:60px;right:60px;top:440px;display:grid;grid-template-columns:1fr 1fr;gap:28px}
.a{height:430px;border-radius:220px 220px 20px 20px;background:#fff;overflow:hidden;box-shadow:0 12px 28px rgba(47,74,58,.14)}
.a img{width:100%;height:100%;object-fit:contain;padding:56px 26px 18px}
.pill{position:absolute;left:50%;transform:translateX(-50%);bottom:56px;white-space:nowrap;background:#2F4A3A;color:#F4EBDD;font:700 34px 'DM Sans';padding:22px 46px;border-radius:60px}"""
PINS = {"her": ("COZY GIFTS FOR HER", "Gifts she'll <em>actually</em> use", ["slip-puff-trim", "sherpa", "socks", "slip-litfun"]),
        "kids": ("TRENDING TOYS 2026", "The toys on <em>every</em> list", ["squish", "beyblade", "needoh-adv", "lego-unicorn"]),
        "host": ("HOLIDAY HOSTING", "Hosting, <em>done easy</em>", ["board-hecef", "taper-red", "coupe-bhg", "board-farb"]),
        "games": ("FAMILY GAME NIGHT", "Games they'll <em>actually</em> play", ["uno", "phase10", "mdeal", "tapple"])}
for key, (eb, t, imgs) in PINS.items():
    tiles = "".join(f'<div class="a"><img src="{P(i)}"{FILLCSS if i in FILL else ""}></div>' for i in imgs)
    shot(f"wm-ppin-{key}", PIN, f'<div class="eb">{eb}</div><div class="t"><div class="fit" data-h="306" data-max="150">{t}</div></div><div class="g">{tiles}</div><div class="pill">Shop my Walmart storefront &#10022;</div>', 1000, 1500)
print("pins ok")
