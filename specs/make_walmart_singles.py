"""Walmart single-product Pins (1000x1500) + single 'Walmart find' IG/FB posts (1080x1350), Nov 25 2026.
Owner: pin 10+ things today; Walmart on IG/FB too. Each pin gets its own link where possible (avoid same-URL spam)."""
import pathlib, subprocess, os
ROOT = pathlib.Path(__file__).resolve().parent.parent
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;'
         '1,9..144,400;1,9..144,500&family=DM+Sans:wght@500;700&family=Courier+Prime:wght@700&display=swap">')
OUT = ROOT / "posts" / "walmart"
ONLY = set(filter(None, os.environ.get("ONLY", "").split(",")))
P = lambda n: (ROOT / "src" / "wmp" / f"{n}.jpg").as_uri()
FIT = ("<script>document.fonts.ready.then(()=>{document.querySelectorAll('.fit').forEach(e=>{const H=+e.dataset.h,M=+e.dataset.max;"
       "let s=60;e.style.fontSize=s+'px';while(s<M){e.style.fontSize=(s+2)+'px';"
       "if(e.offsetHeight>H||e.scrollWidth>e.parentElement.clientWidth){e.style.fontSize=s+'px';break}s+=2}})})</script>")
BASE = "*{box-sizing:border-box}html,body{margin:0;overflow:hidden}body{position:relative;font-family:'DM Sans',sans-serif;color:#2F4A3A;background:#F4EBDD}"
PIN = BASE + """html,body{width:1000px;height:1500px}
.eb{position:absolute;left:0;right:0;top:70px;text-align:center;font:700 30px 'Courier Prime',monospace;letter-spacing:.2em;color:#B07F2E}
.hook{position:absolute;left:50px;right:50px;top:116px;height:320px;display:flex;align-items:center;justify-content:center;text-align:center;font:600 90px/1.03 Fraunces,serif;letter-spacing:-.015em}
.hook em{font-style:italic;font-weight:400;color:#9E2B32}
.frame{position:absolute;left:150px;right:150px;top:460px;height:760px;border-radius:360px 360px 26px 26px;overflow:hidden;background:#fff;box-shadow:0 16px 36px rgba(47,74,58,.16)}
.frame img{width:100%;height:100%;object-fit:contain;padding:90px 50px 30px}
.name{position:absolute;left:50px;right:50px;top:1246px;text-align:center;font:italic 400 42px Fraunces,serif;color:#3A2A20}
.pill{position:absolute;left:50%;transform:translateX(-50%);bottom:56px;white-space:nowrap;background:#2F4A3A;color:#F4EBDD;font:700 34px 'DM Sans';padding:22px 46px;border-radius:60px}"""
POST = BASE + """html,body{width:1080px;height:1350px}
.eb{position:absolute;left:0;right:0;top:70px;text-align:center;font:700 30px 'Courier Prime',monospace;letter-spacing:.18em;color:#B07F2E}
.hook{position:absolute;left:60px;right:60px;top:116px;height:296px;display:flex;align-items:center;justify-content:center;text-align:center;font:600 80px/1.03 Fraunces,serif;letter-spacing:-.015em}
.hook em{font-style:italic;font-weight:400;color:#9E2B32}
.frame{position:absolute;left:210px;right:210px;top:430px;height:620px;border-radius:330px 330px 24px 24px;overflow:hidden;background:#fff;box-shadow:0 16px 36px rgba(47,74,58,.16)}
.frame img{width:100%;height:100%;object-fit:contain;padding:70px 46px 26px}
.name{position:absolute;left:60px;right:60px;top:1080px;text-align:center;font:italic 400 40px Fraunces,serif;color:#3A2A20}
.bar{position:absolute;left:0;right:0;bottom:0;height:150px;background:#2F4A3A;display:flex;align-items:center;justify-content:center;gap:20px;color:#F4EBDD;font:600 42px 'DM Sans'}
.bar b{background:#F8E2A8;color:#2F4A3A;font:700 48px 'Courier Prime',monospace;padding:8px 24px;border-radius:10px;letter-spacing:.06em}
.ad{position:absolute;right:22px;top:20px;background:#2F4A3A;color:#F4EBDD;font:700 18px 'Courier Prime',monospace;padding:4px 10px;border-radius:6px}"""
# name, img, eyebrow, hook, product
PINS = [
 ("wm-spin-squish", "squish", "WALMART FIND · SQUISHMALLOWS", "The one they'll <em>sleep with</em> every night.", "Hello Kitty Squishmallow, 8 in"),
 ("wm-spin-needoh-adv", "needoh-adv", "WALMART FIND · NEEDOH", "24 days of squish. <em>Zero glitter.</em>", "NeeDoh Advent Calendar"),
 ("wm-spin-needoh-ice", "needoh-ice", "WALMART FIND · NEEDOH", "The stocking stuffer they <em>won't put down.</em>", "NeeDoh Nice Ice Baby, 4-Pack"),
 ("wm-spin-beyblade", "beyblade", "WALMART FIND · BEYBLADE X", "Battle royale, <em>living room edition.</em>", "Beyblade X Xtreme Battle Set"),
 ("wm-spin-lego-unicorn", "lego-unicorn", "WALMART FIND · LEGO FRIENDS", "Built in an afternoon. <em>Played all break.</em>", "Unicorn Cake Delivery Car"),
 ("wm-spin-lego-panda", "lego-panda", "WALMART FIND · LEGO FRIENDS", "For the kid who <em>loves every animal.</em>", "LEGO Friends Panda Sanctuary"),
 ("wm-spin-uno", "uno", "FAMILY GAME NIGHT", "Brutal. Ruthless. <em>Family-approved.</em>", "UNO Show 'Em No Mercy"),
 ("wm-spin-phase10", "phase10", "FAMILY GAME NIGHT", "The one <em>grandma always wins.</em>", "Phase 10 Card Game"),
 ("wm-spin-connect4", "connect4", "FAMILY GAME NIGHT", "The classic that <em>never gets old.</em>", "Connect 4 Classic Grid"),
 ("wm-spin-coupe", "coupe-thyme", "HOLIDAY HOSTING", "Gold rims make everything <em>taste fancier.</em>", "Thyme &amp; Table Gold Rim Coupes"),
]
POSTS = [
 ("wm-find-needoh-ice", "needoh-ice", "WALMART FIND · NEEDOH", "The stocking stuffer they <em>won't put down.</em>", "NeeDoh Nice Ice Baby, 4-Pack"),
 ("wm-find-lego-panda", "lego-panda", "WALMART FIND · LEGO FRIENDS", "For the kid who <em>loves every animal.</em>", "LEGO Friends Panda Sanctuary"),
]


def shot(name, css, body, w, h):
    if ONLY and name not in ONLY:
        return
    f = ROOT / f"_{name}.html"
    f.write_text(f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{css}</style></head><body>{body}{FIT}</body></html>', encoding="utf-8")
    subprocess.run([EDGE, "--headless", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1", f"--window-size={w},{h}",
                    "--virtual-time-budget=6000", f"--screenshot={OUT / (name + '.png')}", f.as_uri()], check=True, capture_output=True)
    print(name)


for name, img, eb, hook, prod in PINS:
    shot(name, PIN, f'<div class="eb">{eb}</div><div class="hook"><div class="fit" data-h="320" data-max="128">{hook}</div></div>'
         f'<div class="frame"><img src="{P(img)}"></div><div class="name">{prod}</div><div class="pill">Shop it at Walmart &#10022;</div>', 1000, 1500)
for name, img, eb, hook, prod in POSTS:
    shot(name, POST, f'<div class="ad">#AD</div><div class="eb">{eb}</div><div class="hook"><div class="fit" data-h="296" data-max="132">{hook}</div></div>'
         f'<div class="frame"><img src="{P(img)}"></div><div class="name">{prod}</div><div class="bar">Tap to shop <span style="opacity:.6">&#183;</span> or comment <b>WALMART</b></div>', 1080, 1350)
