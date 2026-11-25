"""Nov 25 2026 'start the freebies today' push (owner request): new pack carousel, Story and 4 fresh pins.
Reuses the Chaos promo look (pine/cream, Fraunces). Output: posts/2026-chaos/today-*.png"""
import pathlib, subprocess, shutil
SRC = pathlib.Path(__file__).with_name("make_chaos_promo.py").read_text(encoding="utf-8")
exec(SRC.split("OUT.mkdir(parents")[0])
R = ROOT / "out"
POSTS = ROOT / "posts" / "2026-chaos"
CREAM = '<style>body{background:#F4EBDD;color:#2F4A3A}.q em{color:#9E2B32}.eb{color:#9E2B32}.sub{color:#3A2A20}.pill{background:#2F4A3A;color:#F4EBDD}.handle{color:#2F4A3A}</style>'
def im(p, x, y, h, r=0):
    return f'<img class="c" src="{p.as_uri()}" style="left:{x}px;top:{y}px;height:{h}px;border-radius:10px;transform:rotate({r}deg)">'
TR, B1, B2, SA, PK = D / "tracker.png", D / "bingo1.png", D / "bingo2.png", R / "sampler-p1.png", R / "pack-p1.png"
F = {}
F["car-1"] = (1080, 1350, f"""{CREAM}{spk(1080,1350)}<div class="tc" style="top:90px"><div class="eb">3 FREE PRINTABLES</div>
<div class="q" style="margin-top:20px;font-size:86px">December, <em>printed</em><br>and sorted.</div></div>
{im(TR,60,540,600,-8)}{im(B1,320,510,630,2)}{im(SA,590,550,600,8)}{H}""")
F["car-2"] = (1080, 1350, f"""{spk(1080,1350)}<div class="tc" style="top:90px"><div class="eb">01 · FOR THE LIST-MAKER</div>
<div class="q" style="margin-top:20px;font-size:78px">Who's done. Who's not.<br><em>Who's getting socks.</em></div></div>
{im(TR,215,470,760,-2)}{H}""")
F["car-3"] = (1080, 1350, f"""{CREAM}{spk(1080,1350)}<div class="tc" style="top:90px"><div class="eb">02 · FOR MOVIE NIGHT</div>
<div class="q" style="margin-top:20px;font-size:78px">Somebody yells <em>BINGO</em><br>at the kiss in the snow.</div></div>
{im(B2,110,500,740,-6)}{im(B1,380,480,760,4)}{H}""")
F["car-4"] = (1080, 1350, f"""{spk(1080,1350)}<div class="tc" style="top:90px"><div class="eb">03 · FOR THE GIFT SWAP</div>
<div class="q" style="margin-top:20px;font-size:78px">8 white elephant cards.<br><em>Free.</em> Mildly evil.</div></div>
{im(SA,215,470,760,2)}{H}""")
F["car-5"] = (1080, 1350, f"""{CREAM}{spk(1080,1350)}<div class="tc" style="top:300px"><div class="eb">HOW TO GET THEM</div>
<div class="q" style="margin-top:28px;font-size:84px">Comment <em>TRACKER</em>,<br><em>BINGO</em> or <em>SAMPLER</em></div>
<div class="sub" style="margin:40px auto 0;max-width:800px">and I'll DM you the printable. Want all three in one? Tap the link in my bio, then "Free printables".</div>
<div style="margin-top:60px"><span class="pill">Save this for December ✦</span></div></div>{H}""")
F["car-6"] = (1080, 1350, f"""{spk(1080,1350)}<div class="tc" style="top:100px"><div class="eb">LIKED THE SAMPLER?</div>
<div class="q" style="margin-top:22px;font-size:84px">The full deck is<br><em>34 cards of chaos.</em></div></div>
{card(12,100,560,300,-8)}{card(21,390,530,300,0)}{card(13,680,560,300,8)}
<div class="tc" style="top:1060px"><span class="pill">Chaos Cards · link in bio ✦</span></div>{H}""")
F["story"] = (1080, 1920, f"""{CREAM}{spk(1080,1920)}<div class="tc" style="top:260px"><div class="eb">FREE · 3 PRINTABLES</div>
<div class="q" style="margin-top:24px">Gift tracker, movie bingo<br>+ a <em>gift swap game</em></div></div>
{im(TR,80,700,560,-8)}{im(B1,360,680,580,2)}{im(SA,600,720,540,9)}
<div class="tc" style="top:1780px"><div class="sub" style="font-size:30px;opacity:.75">tap the link ↑ it's free</div></div>""")
F["pin-tracker"] = (1000, 1500, f"""{spk(1000,1500)}<div class="tc" style="top:90px"><div class="eb">FREE CHRISTMAS PRINTABLE</div>
<div class="q" style="margin-top:20px;font-size:92px">Holiday Gift<br><em>Shopping List</em></div>
<div class="sub" style="margin-top:16px">who's done, who's not, what's wrapped</div></div>
{im(TR,150,560,860,3)}""")
F["pin-bingo"] = (1000, 1500, f"""{CREAM}{spk(1000,1500)}<div class="tc" style="top:90px"><div class="eb">FREE PRINTABLE GAME</div>
<div class="q" style="margin-top:20px;font-size:92px">Cheesy Christmas<br><em>Movie Bingo</em></div>
<div class="sub" style="margin-top:16px">4 cards · print for the whole couch</div></div>
{im(B1,110,560,820,-4)}{im(B2,360,600,800,6)}""")
F["pin-sampler"] = (1000, 1500, f"""{spk(1000,1500)}<div class="tc" style="top:90px"><div class="eb">FREE PRINTABLE</div>
<div class="q" style="margin-top:20px;font-size:92px">White Elephant<br><em>Game Cards</em></div>
<div class="sub" style="margin-top:16px">8 free twist cards for your gift swap</div></div>
{im(SA,150,560,860,-3)}""")
F["pin-chaos"] = (1000, 1500, f"""{CREAM}{spk(1000,1500)}<div class="tc" style="top:90px"><div class="eb">OFFICE PARTY · FAMILY SWAP</div>
<div class="q" style="margin-top:20px;font-size:88px">The Gift Exchange<br>Game That Ends in<br><em>Friendly Betrayal</em></div></div>
{card(24,80,780,280,-8)}{card(12,360,750,280,0)}{card(28,640,780,280,8)}
<div class="tc" style="bottom:70px"><span class="pill">printable · play tonight</span></div>""")
POSTS.mkdir(parents=True, exist_ok=True)
for name, (w, h, body) in F.items():
    f = R / f"_today-{name}.html"
    f.write_text(f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{css(w, h)}</style></head><body>{body}</body></html>', encoding="utf-8")
    png = POSTS / f"today-{name}.png"
    subprocess.run([EDGE, "--headless", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size={w},{h}", "--virtual-time-budget=6000", f"--screenshot={png}", f.as_uri()], check=True, capture_output=True)
    print(png.name)
