"""Walmart Creator launch pins (Nov 25 2026): full-bleed no-face lifestyle photo + cream title card. 1000x1500."""
import pathlib, subprocess, json
ROOT = pathlib.Path(__file__).resolve().parent.parent
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;'
         '1,9..144,400;1,9..144,500&family=DM+Sans:wght@500;700&family=Courier+Prime:wght@700&display=swap">')
OUT = ROOT / "posts" / "walmart"; OUT.mkdir(parents=True, exist_ok=True)
P = [
 ("wm-pin-her-a", "1795330796412-80b543884f4c", "WALMART GIFT GUIDE", "Cozy Gifts for Her <em>Under $50</em>", "pajama sets · slippers · sherpa throws", "top"),
 ("wm-pin-her-b", "1734898537962-2dc575c99e11", "GIFTS SHE'LL ACTUALLY USE", "The <em>cozy</em> gift guide", "every pick rated 4★ and up at Walmart", "bottom"),
 ("wm-pin-kids-a", "1546512347-b93b3f59e231", "TRENDING TOYS 2026", "What kids want <em>this year</em>", "Squishmallows · NeeDoh · Beyblade X · LEGO", "top"),
 ("wm-pin-kids-b", "1703319955806-8104553f0b92", "WALMART BEST SELLERS", "The toys on <em>every</em> list", "so you don't have to Google it", "bottom"),
 ("wm-pin-host-a", "1688437307687-fe226bddfab1", "HOLIDAY HOSTING", "Hosting Christmas, <em>done easy</em>", "boards · taper candles · coupes · cake stand", "top"),
 ("wm-pin-host-b", "1780480643131-f86e5c1facf5", "WALMART HOSTING FINDS", "Make your house look <em>catered</em>", "(even if dessert is store-bought)", "bottom"),
 ("wm-pin-games-a", "1629760946220-5693ee4c46ac", "CHRISTMAS BREAK", "Phones-down <em>family game night</em>", "UNO No Mercy · Phase 10 · Monopoly Deal", "top"),
 ("wm-pin-games-b", "1659480141041-c41defa79a71", "FAMILY GAME NIGHT", "Games they'll <em>actually</em> play", "best-selling games + puzzles at Walmart", "bottom"),
]
CSS = """*{box-sizing:border-box}html,body{margin:0;width:1000px;height:1500px;overflow:hidden}
body{position:relative;font-family:'DM Sans',sans-serif;background:#2F4A3A}
.ph{position:absolute;inset:0;background-size:cover;background-position:center}
.card{position:absolute;left:60px;right:60px;background:#F4EBDD;border-radius:28px;padding:54px 50px 50px;text-align:center;color:#2F4A3A;box-shadow:0 24px 60px rgba(0,0,0,.35)}
.top{top:70px}.bottom{bottom:150px}
.eb{font:700 28px 'Courier Prime',monospace;letter-spacing:.22em;color:#9E2B32}
.t{margin-top:18px;font:600 92px/1.0 Fraunces,serif;letter-spacing:-.02em}.t em{font-style:italic;font-weight:400;color:#9E2B32}
.s{margin-top:22px;font:italic 400 38px/1.2 Fraunces,serif;color:#3A2A20}
.pill{position:absolute;left:50%;transform:translateX(-50%);white-space:nowrap;background:#9E2B32;color:#F4EBDD;font:700 34px 'DM Sans';padding:22px 44px;border-radius:60px;box-shadow:0 12px 30px rgba(0,0,0,.35)}
.pt{bottom:60px}.pb{bottom:56px}
.h{position:absolute;left:0;right:0;font:700 24px 'Courier Prime',monospace;letter-spacing:.14em;color:#F4EBDD;text-align:center;text-shadow:0 2px 8px rgba(0,0,0,.6)}"""
for name, ph, eb, t, s, pos in P:
    img = (ROOT / "src" / "wm" / f"{ph}.jpg").as_uri()
    pill = "Shop my Walmart storefront ✦"
    body = f'<div class="ph" style="background-image:url({img})"></div><div class="card {pos}"><div class="eb">{eb}</div><div class="t">{t}</div><div class="s">{s}</div></div><div class="pill pb">{pill}</div>'
    f = ROOT / f"_{name}.html"
    f.write_text(f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{body}</body></html>', encoding="utf-8")
    png = OUT / f"{name}.png"
    subprocess.run([EDGE, "--headless", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1", "--window-size=1000,1500",
                    "--virtual-time-budget=6000", f"--screenshot={png}", f.as_uri()], check=True, capture_output=True)
    print(png.name)
