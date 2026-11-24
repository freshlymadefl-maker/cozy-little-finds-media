"""Promo graphics for the Movie Bingo + Gift Tracker freebies (IG 1080x1350, Pins 1000x1500, Story 1080x1920)."""
import pathlib, subprocess
SRC = pathlib.Path(__file__).with_name("make_chaos_promo.py").read_text(encoding="utf-8")
exec(SRC.split("OUT.mkdir(parents")[0])
CREAM = '<style>body{background:#F4EBDD;color:#2F4A3A}.q em{color:#9E2B32}.eb{color:#9E2B32}.sub{color:#3A2A20}.pill{background:#2F4A3A;color:#F4EBDD}.handle{color:#2F4A3A}</style>'
def pg(f, x, y, h, r=0):
    return f'<img class="c" src="{(D / f).as_uri()}" style="left:{x}px;top:{y}px;height:{h}px;border-radius:8px;transform:rotate({r}deg)">'
F = {}
F["bingo-ig"] = (1080, 1350, f"""{spk(1080,1350)}<div class="tc" style="top:90px"><div class="eb">FREE PRINTABLE</div>
<div class="q" style="margin-top:20px;font-size:80px">Cheesy Christmas<br><em>Movie Bingo</em></div></div>
{pg('bingo2.png',120,470,760,-6)}{pg('bingo1.png',360,450,780,4)}{H}""")
F["bingo-ig2"] = (1080, 1350, f"""{spk(1080,1350)}<div class="tc" style="top:330px"><div class="eb">4 DIFFERENT CARDS</div>
<div class="q" style="margin-top:28px">Comment <em>BINGO</em><br>and I'll send it</div>
<div class="sub" style="margin:40px auto 0;max-width:780px">Print one for everyone on the couch. Five in a row picks the next movie.</div>
<div style="margin-top:60px"><span class="pill">Send this to the group chat ✦</span></div></div>{H}""")
F["tracker-ig"] = (1080, 1350, f"""{CREAM}{spk(1080,1350)}<div class="tc" style="top:90px"><div class="eb">FREE PRINTABLE</div>
<div class="q" style="margin-top:20px;font-size:80px">The Christmas<br><em>Gift Tracker</em></div></div>
{pg('tracker.png',200,470,800,-3)}{H}""")
F["tracker-ig2"] = (1080, 1350, f"""{CREAM}{spk(1080,1350)}<div class="tc" style="top:330px"><div class="eb">IT'S FREE</div>
<div class="q" style="margin-top:28px">Comment <em>TRACKER</em><br>and I'll send it</div>
<div class="sub" style="margin:40px auto 0;max-width:780px">Who you're buying for, what, and whether it's actually wrapped. Gift ideas are in my bio.</div>
<div style="margin-top:60px"><span class="pill">Save this ✦</span></div></div>{H}""")
F["pin-bingo"] = (1000, 1500, f"""{spk(1000,1500)}<div class="tc" style="top:90px"><div class="eb">FREE PRINTABLE</div>
<div class="q" style="margin-top:20px;font-size:96px">Christmas Movie<br><em>Bingo</em></div>
<div class="sub" style="margin-top:16px">4 cards for your cheesy movie night</div></div>
{pg('bingo2.png',90,560,780,-5)}{pg('bingo1.png',330,540,800,4)}""")
F["pin-tracker"] = (1000, 1500, f"""{CREAM}{spk(1000,1500)}<div class="tc" style="top:90px"><div class="eb">FREE PRINTABLE</div>
<div class="q" style="margin-top:20px;font-size:96px">Christmas Gift<br><em>List Tracker</em></div>
<div class="sub" style="margin-top:16px">Budget, bought, wrapped. Done.</div></div>
{pg('tracker.png',170,540,860,-3)}""")
F["story-bingo"] = (1080, 1920, f"""{spk(1080,1920)}<div class="tc" style="top:300px"><div class="eb">MOVIE NIGHT?</div>
<div class="q" style="margin-top:24px">Free cheesy<br><em>movie bingo</em></div></div>
{pg('bingo1.png',260,640,760,3)}<div class="tc" style="top:1780px"><div class="sub" style="font-size:30px;opacity:.75">tap the link ↑ it's free</div></div>""")
F["story-tracker"] = (1080, 1920, f"""{CREAM}{spk(1080,1920)}<div class="tc" style="top:300px"><div class="eb">FREE PRINTABLE</div>
<div class="q" style="margin-top:24px">Your gift list,<br><em>sorted</em></div></div>
{pg('tracker.png',250,640,780,-3)}<div class="tc" style="top:1780px"><div class="sub" style="font-size:30px;opacity:.75">tap the link ↑ it's free</div></div>""")
for name, (w, h, body) in F.items():
    f = OUT / f"_{name}.html"
    f.write_text(f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{css(w, h)}</style></head><body>{body}</body></html>', encoding="utf-8")
    png = OUT / f"free-{name}.png"
    subprocess.run([EDGE, "--headless", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size={w},{h}", "--virtual-time-budget=6000", f"--screenshot={png}", f.as_uri()], check=True, capture_output=True)
    print(png.name)
