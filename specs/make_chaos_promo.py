"""Promo graphics for Chaos Cards: IG/FB carousel (1080x1350), Pins (1000x1500), Story (1080x1920).
Brand rule: no exact prices. Needs out/chaos-cards/card*.png. Run: python specs/make_chaos_promo.py
"""
import pathlib, subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
D = ROOT / "out" / "chaos-cards"
OUT = ROOT / "out" / "chaos-promo"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;'
         '1,9..144,500&family=DM+Sans:wght@500;700&family=Courier+Prime:wght@700&display=swap">')
SP = '<svg style="position:absolute;{s}" viewBox="0 0 100 100" fill="{c}"><path d="M50 0C54 34 66 46 100 50C66 54 54 66 50 100C46 66 34 54 0 50C34 46 46 34 50 0Z"/></svg>'


def css(w, h):
    return f"""*{{box-sizing:border-box}}html,body{{margin:0;width:{w}px;height:{h}px;overflow:hidden}}
body{{background:#2F4A3A;color:#F4EBDD;font-family:"DM Sans",sans-serif;position:relative}}
.eb{{font:700 30px "Courier Prime",monospace;letter-spacing:.2em;color:#F8E2A8}}
.q{{font:500 92px/1.02 Fraunces,serif;letter-spacing:-.01em}}.q em{{font-style:italic;color:#F8E2A8}}
.sub{{font:500 36px/1.35 "DM Sans";opacity:.9}}
.c{{position:absolute;border-radius:22px;box-shadow:0 20px 50px rgba(0,0,0,.35)}}
.handle{{position:absolute;left:0;right:0;bottom:48px;text-align:center;font:500 28px "DM Sans";letter-spacing:.03em;opacity:.75}}
.pill{{display:inline-block;background:#F8E2A8;color:#2F4A3A;font:700 38px "DM Sans";padding:20px 44px;border-radius:60px}}
.tc{{position:absolute;left:0;right:0;text-align:center}}"""


def card(n, x, y, w, r=0):
    return f'<img class="c" src="{(D / f"card{n:02d}.png").as_uri()}" style="left:{x}px;top:{y}px;width:{w}px;transform:rotate({r}deg)">'


def spk(w, h):
    return (SP.format(s="left:70px;top:80px;width:70px", c="#F8E2A8") + SP.format(s=f"right:80px;top:140px;width:46px", c="#E0767C")
            + SP.format(s=f"left:110px;bottom:150px;width:36px", c="#F4EBDD"))


H = '<div class="handle">@cozylittlefindsdaily</div>'
P = {}
# Carousel 1080x1350
P["car-1"] = (1080, 1350, f"""{spk(1080,1350)}<div class="tc" style="top:120px"><div class="eb">GIFT EXCHANGE SEASON</div>
<div class="q" style="margin-top:28px">Your white elephant<br>needs <em>chaos.</em></div></div>
{card(12,90,640,330,-9)}{card(21,375,600,330,0)}{card(13,660,640,330,9)}{H}""")
for i, (n, line) in enumerate([(12, "Finally, *justice.*"), (21, "We've *all* been there."), (28, "Short. *Brutal.*"),
                               (13, "The *plot twist* card."), (24, "Somebody's *getting exposed.*")], 2):
    q = line.replace("*", "<em>", 1).replace("*", "</em>", 1)
    P[f"car-{i}"] = (1080, 1350, f"""{spk(1080,1350)}<div class="tc" style="top:110px"><div class="eb">FROM THE DECK</div>
<div class="q" style="margin-top:22px;font-size:84px">{q}</div></div>{card(n,250,380,580,-2)}{H}""")
P["car-7"] = (1080, 1350, f"""{spk(1080,1350)}<div class="tc" style="top:250px"><div class="eb">CHAOS CARDS</div>
<div class="q" style="margin-top:28px">Print tonight.<br><em>Ruin</em> the party.</div>
<div class="sub" style="margin:40px auto 0;max-width:760px">34 twist cards + 2 blank ones for your own house rules. Instant download, works with any gift swap.</div>
<div style="margin-top:70px"><span class="pill">Link in bio ✦</span></div>
<div class="sub" style="margin-top:40px;font-size:30px;opacity:.7">Send this to whoever's hosting.</div></div>{H}""")
# Pins 1000x1500
P["pin-a"] = (1000, 1500, f"""{spk(1000,1500)}<div class="tc" style="top:110px"><div class="eb">PRINTABLE PARTY GAME</div>
<div class="q" style="margin-top:26px;font-size:104px">White Elephant<br><em>Chaos Cards</em></div>
<div class="sub" style="margin-top:26px">twist cards for any gift exchange</div></div>
{card(1,70,720,320,-9)}{card(21,340,680,320,0)}{card(13,610,720,320,9)}
<div class="tc" style="bottom:70px"><span class="pill">Print at home tonight</span></div>""")
P["pin-b"] = (1000, 1500, f"""{spk(1000,1500)}<div class="tc" style="top:110px"><div class="eb">YANKEE SWAP, UPGRADED</div>
<div class="q" style="margin-top:26px;font-size:96px">The gift exchange<br>game everyone<br><em>talks about</em></div></div>
{card(12,90,800,260,-7)}{card(28,370,770,260,0)}{card(5,650,800,260,7)}
<div class="tc" style="bottom:70px"><span class="pill">34 cards · instant download</span></div>""")
# Story 1080x1920 (leave space for link sticker around y 1450-1650)
P["story"] = (1080, 1920, f"""{spk(1080,1920)}<div class="tc" style="top:230px"><div class="eb">HOSTING THE GIFT SWAP?</div>
<div class="q" style="margin-top:30px">Add a little<br><em>chaos.</em></div></div>
{card(12,90,640,330,-9)}{card(21,375,600,330,0)}{card(13,660,640,330,9)}
<div class="tc" style="top:1780px"><div class="sub" style="font-size:30px;opacity:.75">tap the link ↑ print tonight</div></div>""")

OUT.mkdir(parents=True, exist_ok=True)
for name, (w, h, body) in P.items():
    f = OUT / f"_{name}.html"
    f.write_text(f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{css(w, h)}</style></head><body>{body}</body></html>', encoding="utf-8")
    png = OUT / f"chaos-{name}.png"
    subprocess.run([EDGE, "--headless", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size={w},{h}", "--virtual-time-budget=6000", f"--screenshot={png}", f.as_uri()], check=True, capture_output=True)
    print(png.name)

# --- extra pins (round 2) + reel frames ---
P2 = {}
CREAM = 'body{background:#F4EBDD;color:#2F4A3A}.q em{color:#9E2B32}.eb{color:#9E2B32}.sub{color:#3A2A20}.pill{background:#2F4A3A;color:#F4EBDD}'
P2["pin-c"] = (1000, 1500, f"""<style>{CREAM}</style>{spk(1000,1500)}<div class="tc" style="top:100px"><div class="eb">CHRISTMAS PARTY GAMES</div>
<div class="q" style="margin-top:24px;font-size:98px">The game that<br><em>ruins</em> (and makes)<br>the party</div></div>
{card(24,330,760,340,0)}{card(5,60,820,300,-10)}{card(16,640,820,300,10)}
<div class="tc" style="bottom:60px"><span class="pill">Printable · play tonight</span></div>""")
P2["pin-d"] = (1000, 1500, f"""{spk(1000,1500)}<div class="tc" style="top:100px"><div class="eb">YANKEE SWAP RULES, BUT BETTER</div>
<div class="q" style="margin-top:24px;font-size:100px">34 twists for<br>your <em>gift swap</em></div></div>
{card(1,60,620,280,-8)}{card(13,360,580,280,0)}{card(29,660,620,280,8)}
{card(7,210,1000,260,-4)}{card(25,530,1000,260,5)}""")
P2["pin-e"] = (1000, 1500, f"""<style>{CREAM}</style>{spk(1000,1500)}<div class="tc" style="top:100px"><div class="eb">OFFICE PARTY GAME</div>
<div class="q" style="margin-top:24px;font-size:96px">White elephant,<br>but make it<br><em>dramatic</em></div></div>
{card(30,90,770,380,-6)}{card(18,530,770,380,6)}
<div class="tc" style="bottom:60px"><span class="pill">Instant download</span></div>""")
R = {}
R["reel-1"] = f"""{spk(1080,1920)}<div class="tc" style="top:330px"><div class="eb">POV</div>
<div class="q" style="margin-top:24px">Your gift swap just<br>got <em>Chaos Cards</em></div></div>
{card(12,60,820,360,-9)}{card(21,330,780,360,0)}{card(13,600,820,360,9)}"""
for i, n in enumerate([12, 21, 13, 28, 24], 2):
    R[f"reel-{i}"] = f"""{spk(1080,1920)}{card(n,190,360,640,-2 if i % 2 else 2)}"""
R["reel-7"] = f"""{spk(1080,1920)}<div class="tc" style="top:520px"><div class="eb">CHAOS CARDS</div>
<div class="q" style="margin-top:28px">Print tonight.<br><em>Ruin</em> the party.</div>
<div class="sub" style="margin:40px auto 0;max-width:760px">34 twist cards for any white elephant or Yankee swap</div>
<div style="margin-top:60px"><span class="pill">Link in bio ✦</span></div></div>"""
for name, (w, h, body) in P2.items():
    P[name] = (w, h, body)
for name, body in R.items():
    P[name] = (1080, 1920, body)
for name in list(P2) + list(R):
    w, h, body = P[name]
    f = OUT / f"_{name}.html"
    f.write_text(f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{css(w, h)}</style></head><body>{body}</body></html>', encoding="utf-8")
    png = OUT / f"chaos-{name}.png"
    subprocess.run([EDGE, "--headless", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size={w},{h}", "--virtual-time-budget=6000", f"--screenshot={png}", f.as_uri()], check=True, capture_output=True)
    print(png.name)
