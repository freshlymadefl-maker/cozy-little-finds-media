"""Weekly Chaos Cards rotation (Dec 2026): tag-a-friend carousel, free sampler carousel + story,
how-to-play Reel, hosting-tips carousel, Pins f-i. Run: python specs/make_chaos_weekly.py
"""
import pathlib, subprocess

SRC = pathlib.Path(__file__).with_name("make_chaos_promo.py").read_text(encoding="utf-8")
exec(SRC.split("OUT.mkdir(parents")[0])  # css, card, spk, H, FONTS, D, OUT, EDGE
CREAM = '<style>body{background:#F4EBDD;color:#2F4A3A}.q em{color:#9E2B32}.eb{color:#9E2B32}.sub{color:#3A2A20}.pill{background:#2F4A3A;color:#F4EBDD}.handle{color:#2F4A3A}</style>'
W = {}


def slide(name, body, w=1080, h=1350):
    W[name] = (w, h, body)


def tip(num, title, body):
    return f"""{CREAM}{spk(1080,1350)}<div style="position:absolute;left:110px;right:110px;top:300px">
<div style="font:700 150px/1 Fraunces,serif;color:#9E2B32">{num}</div>
<div class="q" style="margin-top:30px;font-size:86px">{title}</div>
<div class="sub" style="margin-top:40px;font-size:42px;line-height:1.4">{body}</div></div>{H}"""


# 1) Tag-a-friend carousel (week of Dec 1)
slide("tag-1", f"""{spk(1080,1350)}<div class="tc" style="top:150px"><div class="eb">GIFT SWAP SEASON</div>
<div class="q" style="margin-top:28px">Tag the friend<br>who'd play <em>this</em> card</div></div>
{card(24,180,600,330,-7)}{card(15,560,600,330,7)}{H}""")
for i, (n, line) in enumerate([(24, "Tag the one who <em>keeps receipts.</em>"), (15, "Tag the one who could <em>sell sand at the beach.</em>"),
                               (5, "Tag the one who <em>never</em> shares the good snacks."), (25, "Tag the one who's <em>always late</em> anyway.")], 2):
    slide(f"tag-{i}", f"""{spk(1080,1350)}<div class="tc" style="top:100px"><div class="q" style="font-size:72px;padding:0 90px">{line}</div></div>
{card(n,250,420,580,-2)}{H}""")
slide("tag-6", f"""{spk(1080,1350)}<div class="tc" style="top:300px"><div class="eb">CHAOS CARDS</div>
<div class="q" style="margin-top:28px">34 cards.<br>Every friend <em>accounted for.</em></div>
<div class="sub" style="margin:40px auto 0;max-width:760px">Twist cards for any white elephant or Yankee swap. Instant download.</div>
<div style="margin-top:60px"><span class="pill">Comment CHAOS ✦</span></div></div>{H}""")

# 2) Free sampler carousel + story (week of Dec 8)
slide("free-1", f"""{CREAM}{spk(1080,1350)}<div class="tc" style="top:140px"><div class="eb">FREE PRINTABLE</div>
<div class="q" style="margin-top:28px">8 free cards to<br><em>ruin</em> your gift swap</div></div>
{card(1,130,620,300,-9)}{card(5,390,580,300,0)}{card(29,650,620,300,9)}{H}""")
slide("free-2", f"""{CREAM}{spk(1080,1350)}<div class="tc" style="top:110px"><div class="q" style="font-size:76px">Print. Cut. <em>Shuffle.</em></div>
<div class="sub" style="margin-top:20px">Draw a card every time someone opens or steals a gift.</div></div>
{card(2,120,480,270,-6)}{card(3,405,450,270,0)}{card(7,690,480,270,6)}
{card(11,260,880,270,-4)}{card(15,550,880,270,4)}{H}""")
slide("free-3", f"""{CREAM}{spk(1080,1350)}<div class="tc" style="top:300px"><div class="eb">IT'S FREE</div>
<div class="q" style="margin-top:28px">Comment <em>SAMPLER</em><br>and I'll send it</div>
<div class="sub" style="margin:40px auto 0;max-width:780px">Want all 34 (with December Baby and The Secret)? The full deck is in my bio.</div>
<div style="margin-top:60px"><span class="pill">Send this to the host ✦</span></div></div>{H}""")
slide("free-story", f"""{CREAM}{spk(1080,1920)}<div class="tc" style="top:300px"><div class="eb">FREE PRINTABLE</div>
<div class="q" style="margin-top:30px">8 free cards for<br>your <em>gift swap</em></div></div>
{card(1,90,700,330,-9)}{card(5,375,660,330,0)}{card(29,660,700,330,9)}
<div class="tc" style="top:1780px"><div class="sub" style="font-size:30px;opacity:.75">tap the link ↑ it's free</div></div>""", 1080, 1920)

# 3) How-to-play Reel frames (week of Dec 8)
for i, (eb, q, cards) in enumerate([
    ("HOW TO PLAY", "Chaos Cards<br>in <em>15 seconds</em>", [(12, 90, 840, 330, -9), (21, 375, 800, 330, 0), (13, 660, 840, 330, 9)]),
    ("STEP 1", "Play your usual<br><em>white elephant</em>", [(1, 260, 760, 560, -3)]),
    ("STEP 2", "Open or steal a gift?<br><em>Draw a card.</em>", [(20, 260, 760, 560, 3)]),
    ("STEP 3", "Do it now,<br>or <em>save it</em> for later", [(19, 260, 760, 560, -3)]),
    ("STEP 4", "The host's word is final.<br><em>Mostly.</em>", [(8, 260, 760, 560, 3)]),
    ("CHAOS CARDS", "Print tonight.<br><em>Ruin</em> the party.", [])], 1):
    cs = "".join(card(*c) for c in cards)
    extra = '<div style="margin-top:60px"><span class="pill">Link in bio ✦</span></div>' if not cards else ""
    top = 560 if not cards else 330
    slide(f"how-{i}", f"""{spk(1080,1920)}<div class="tc" style="top:{top}px"><div class="eb">{eb}</div>
<div class="q" style="margin-top:24px;font-size:84px">{q}</div>{extra}</div>{cs}""", 1080, 1920)

# 4) Hosting-tips carousel (week of Dec 15)
slide("host-1", f"""{spk(1080,1350)}<div class="tc" style="top:220px"><div class="eb">SAVE THIS FOR YOUR PARTY</div>
<div class="q" style="margin-top:28px">How to host a<br>white elephant<br>people <em>talk about</em></div>
<div class="sub" style="margin-top:40px">5 rules from someone who takes this too seriously</div></div>{H}""")
for i, (t, b) in enumerate([
    ("Pick a price range everyone agrees on", "Put it in the invite. No one wants to be the person who brought a candle to a gift-card fight."),
    ("Draw numbers, not names", "Number 1 goes first. The last person gets the best seat: they can steal anything."),
    ("Three steals and it's frozen", "After a gift is stolen three times, it stays put. Fewer tears."),
    ("Wrap it like you mean it", "Mystery is half the fun. A great box makes people fight over a mediocre gift."),
    ("Add a twist", "Chaos Cards: draw one every time someone opens or steals. 34 twists, zero safe gifts.")], 1):
    slide(f"host-{i+1}", tip(f"0{i}", t, b))
slide("host-7", f"""{spk(1080,1350)}<div class="tc" style="top:300px"><div class="eb">RULE 5, SOLVED</div>
<div class="q" style="margin-top:28px">Get the <em>Chaos Cards</em></div>
<div class="sub" style="margin:40px auto 0;max-width:760px">Comment CHAOS for the full deck, or SAMPLER for 8 free cards.</div>
<div style="margin-top:60px"><span class="pill">Link in bio ✦</span></div></div>{H}""")

# 5) Pins f-i (1000x1500)
slide("pin-f", f"""{CREAM}{spk(1000,1500)}<div class="tc" style="top:100px"><div class="eb">FREE PRINTABLE</div>
<div class="q" style="margin-top:24px;font-size:100px">Free white<br>elephant <em>game</em></div>
<div class="sub" style="margin-top:20px">8 printable twist cards for your gift exchange</div></div>
{card(1,70,700,300,-9)}{card(5,350,660,300,0)}{card(29,630,700,300,9)}
<div class="tc" style="bottom:60px"><span class="pill">Free download</span></div>""", 1000, 1500)
slide("pin-g", f"""{spk(1000,1500)}<div class="tc" style="top:100px"><div class="eb">HOSTING TIPS</div>
<div class="q" style="margin-top:24px;font-size:92px">How to host a<br>white elephant<br><em>people talk about</em></div></div>
<div style="position:absolute;left:120px;right:120px;top:640px;font:500 40px/1.6 'DM Sans'">
① Agree on a price range<br>② Draw numbers, not names<br>③ Three steals and it's frozen<br>④ Wrap it like you mean it<br>⑤ <span style="color:#F8E2A8">Add a twist (Chaos Cards)</span></div>
<div class="tc" style="bottom:70px"><span class="pill">Save for your party</span></div>""", 1000, 1500)
slide("pin-h", f"""{spk(1000,1500)}<div class="tc" style="top:100px"><div class="eb">WHITE ELEPHANT GAME</div>
<div class="q" style="margin-top:24px;font-size:92px">The card everyone<br><em>fights over</em></div></div>
{card(12,220,520,560,-3)}""", 1000, 1500)
slide("pin-i", f"""{CREAM}{spk(1000,1500)}<div class="tc" style="top:100px"><div class="eb">LAST-MINUTE PARTY GAME</div>
<div class="q" style="margin-top:24px;font-size:96px">Print it in<br><em>5 minutes</em></div>
<div class="sub" style="margin-top:20px">Twist cards for tonight's gift swap</div></div>
{card(29,80,700,290,-8)}{card(21,355,660,290,0)}{card(7,630,700,290,8)}
<div class="tc" style="bottom:60px"><span class="pill">Instant download</span></div>""", 1000, 1500)

for name, (w, h, body) in W.items():
    f = OUT / f"_{name}.html"
    f.write_text(f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{css(w, h)}</style></head><body>{body}</body></html>', encoding="utf-8")
    png = OUT / f"chaos-{name}.png"
    subprocess.run([EDGE, "--headless", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size={w},{h}", "--virtual-time-budget=6000", f"--screenshot={png}", f.as_uri()], check=True, capture_output=True)
    print(png.name)
