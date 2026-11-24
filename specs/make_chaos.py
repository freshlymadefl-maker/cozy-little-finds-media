"""Gift Exchange Chaos Cards: free printable (owner picked idea #2, Nov 24 2026).

Builds out/chaos-cards.html -> out/chaos-cards.pdf (Letter, 6 pages) with headless Edge.
Run from the cozy-little-finds-media folder: python specs/make_chaos.py
"""
import html, pathlib, subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "out"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# kind -> (label, color)
K = {"steal": ("STEAL", "#9E2B32"), "swap": ("SWAP", "#2F4A3A"), "save": ("SAVE IT", "#B0862F"), "wild": ("WILD", "#3A2A20")}
CARDS = [
 ("steal", "The Heist", "Steal any gift in the room. Even a frozen one. *Act natural.*"),
 ("swap", "Left, Right, Chaos", "Everyone passes their gift one seat to the left. *Yes, even the person who just opened the good one.*"),
 ("save", "The Bodyguard", "Keep this card. Play it to block *one* steal aimed at you."),
 ("save", "Not on My Watch", "Keep this card. Cancel any Chaos Card someone else just played."),
 ("wild", "The Ice Queen", "Freeze any gift for the rest of the game. *Especially yours.*"),
 ("wild", "Plot Twist", "Turn order reverses. Whoever thought they were going last is now *very* nervous."),
 ("swap", "Blind Date", "Pick someone. Close your eyes, trade gifts, no peeking. *No take-backs.*"),
 ("wild", "The Hostess", "The host moves any one gift to anyone they want. *Bribes accepted.*"),
 ("swap", "The Sales Pitch", "You get 30 seconds to talk someone into trading with you. If they say yes, *swap.*"),
 ("steal", "Wrapped to Impress", "Steal from whoever wrapped the nicest gift tonight. *They tried. Respect it. Take it anyway.*"),
 ("swap", "The Regift", "Put your opened gift back in the pile and open a new one. *Bold.*"),
 ("steal", "December Baby", "Whoever's birthday is closest to Christmas steals any gift. *They've been shortchanged their whole life.*"),
 ("save", "The Secret", "Hide this card. *Tell no one.* At the very end of the game, reveal it and swap with anyone."),
 ("steal", "Rock, Paper, Mine", "Challenge anyone to rock-paper-scissors. Win, take their gift. Lose, *you smile and say nothing.*"),
 ("steal", "The Compliment Tax", "Give everyone a real compliment. Then steal any gift. *They'll be too flattered to mind.*"),
 ("swap", "Home Shopping Hour", "Sell your gift to the room in 20 seconds. Loud applause? *Swap with anyone.*"),
 ("wild", "Musical Gifts", "Everyone passes their gift to the right until the host says *stop.*"),
 ("swap", "Plausible Deniability", "Pick two other people. They swap gifts. *You had nothing to do with it.*"),
 ("save", "Untouchable", "Keep this card. Your gift is safe for the rest of the game. *Look smug.*"),
 ("steal", "The Chef", "The room votes for the best dish tonight. That person steals any gift. *Effort pays.*"),
 ("steal", "Cart Confession", "Read your most recent online order out loud. If it's embarrassing, *steal any gift.* We've all been there."),
 ("swap", "Return to Sender", "Give your gift back to whoever brought it. *Take theirs instead.*"),
 ("swap", "Season of Giving", "Give your gift to whoever looks least happy with theirs. *Keep this card as proof you're a good person.*"),
 ("steal", "The Snitch", "Point out the biggest thief of the night. *Their gift is now yours.*"),
 ("save", "One More Sleep", "Keep this card. Skip your turn now and *go dead last* instead."),
 ("swap", "Small Talk", "Swap with anyone, but first say one nice thing about their gift. *Mean it.*"),
 ("save", "Christmas Miracle", "Keep this card. Unfreeze any one gift, *whenever you like.*"),
 ("swap", "Stay in Your Lane", "Swap with the person on your left. *That's it. That's the card.*"),
 ("steal", "A Toast", "Stand and make a toast. If anyone clinks a glass, *steal any gift.*"),
 ("swap", "Sponsored Post", "Pose with your gift like it's an ad. If the room isn't convinced, *trade with the person on your right.*"),
 ("save", "Last Call", "Keep this card. Make one final steal after the last gift is opened. *No blocks allowed.*"),
 ("wild", "Fresh Eyes", "Everyone holding an opened gift closes their eyes. *The host shuffles two gifts.*"),
 ("steal", "Long Way Home", "Whoever traveled the farthest to be here steals any gift. *Gas money.*"),
 ("swap", "Group Chat", "Swap with whoever texted you most recently. *If they're not here, lucky them.*"),
 ("blank", "Your Rule", "______________________\n______________________\n______________________"),
 ("blank", "Your Rule", "______________________\n______________________\n______________________"),
]
assert len(CARDS) == 36, len(CARDS)


def em(t):
    out = html.escape(t).replace("\n", "<br>")
    parts = out.split("*")
    return "".join(f"<em>{p}</em>" if i % 2 else p for i, p in enumerate(parts))


def card(kind, title, body):
    label, col = K.get(kind, ("WRITE YOUR OWN", "#8A7A6A"))
    return (f'<div class="card" style="--c:{col}"><div class="in"><div class="kind">{label}</div>'
            f'<div class="t">{html.escape(title)}</div><div class="rule"></div>'
            + ('<div class="lines"><i></i><i></i><i></i><i></i></div>' if kind == "blank" else f'<div class="b">{em(body)}</div>')
            + '<div class="ft">CHAOS CARDS</div></div></div>')


CSS = """
@page{size:8.5in 11in;margin:0}
*{box-sizing:border-box}
html,body{margin:0;background:#fff}
body{font-family:"DM Sans",sans-serif;color:#3A2A20;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:8.5in;height:11in;position:relative;overflow:hidden;page-break-after:always;background:#fff}
.grid{position:absolute;left:.5in;top:.5in;width:7.5in;height:10.5in;display:grid;grid-template-columns:repeat(3,2.5in);grid-template-rows:repeat(3,3.5in);
 outline:1px dashed #c9bfb2}
.card{width:2.5in;height:3.5in;border:1px dashed #c9bfb2;padding:.12in;background:#fff}
.in{width:100%;height:100%;background:#F4EBDD;border-radius:.12in;border:2px solid var(--c);padding:.2in .18in .3in;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;position:relative}
.kind{position:absolute;top:.2in;font:700 9pt "Courier Prime",monospace;letter-spacing:.16em;color:#F4EBDD;background:var(--c);padding:2px 8px;border-radius:3px}
.t{font:600 20pt/1.05 "Fraunces",serif;color:var(--c)}
.rule{width:.5in;height:2px;background:var(--c);opacity:.5;margin:.13in 0}
.b{font:500 11.5pt/1.38 "DM Sans",sans-serif}
.b em{font-family:"Fraunces",serif;font-style:italic;font-weight:500;color:var(--c)}
.lines{width:100%;margin-top:.05in}.lines i{display:block;height:.3in;border-bottom:1.2px solid #8A7A6A88}
.ft{position:absolute;bottom:.12in;left:0;right:0;font:700 6.5pt "Courier Prime",monospace;letter-spacing:.2em;opacity:.55}
/* cover + rules */
.full{position:absolute;inset:0;background:#F4EBDD;padding:.9in .85in;display:flex;flex-direction:column}
.cover{background:#2F4A3A;color:#F4EBDD;align-items:center;justify-content:center;text-align:center}
.cover .eb{font:700 12pt "Courier Prime",monospace;letter-spacing:.24em;color:#F8E2A8}
.cover h1{font:500 74pt/.95 "Fraunces",serif;margin:.25in 0 .1in;letter-spacing:-.01em}
.cover h1 em{font-style:italic;color:#F8E2A8}
.cover .sub{font:500 17pt/1.4 "DM Sans",sans-serif;max-width:5.6in;opacity:.92}
.cover .fan{display:flex;gap:.14in;margin:.55in 0 .45in}
.cover .mini{width:1.15in;height:1.6in;border-radius:.1in;background:#F4EBDD;border:2px solid #F8E2A8;color:var(--c);display:flex;align-items:center;justify-content:center;padding:.08in;font:600 11.5pt/1.05 "Fraunces",serif;box-shadow:0 6px 14px rgba(0,0,0,.25)}
.cover .mini:nth-child(1){transform:rotate(-9deg) translateY(10px)}.cover .mini:nth-child(2){transform:rotate(-3deg)}
.cover .mini:nth-child(3){transform:rotate(3deg)}.cover .mini:nth-child(4){transform:rotate(9deg) translateY(10px)}
.cover .h{position:absolute;bottom:.6in;left:0;right:0;font:500 12pt "DM Sans";letter-spacing:.04em;opacity:.8}
.rules h2{font:600 38pt/1 "Fraunces",serif;margin:0 0 .1in;color:#2F4A3A}
.rules h2 em{font-style:italic;color:#9E2B32}
.rules .lede{font:500 13pt/1.45 "DM Sans";margin:0 0 .3in;max-width:6.4in}
.rules ol{margin:0;padding:0;list-style:none;counter-reset:n}
.rules li{counter-increment:n;display:flex;gap:.18in;align-items:flex-start;font:500 13pt/1.45 "DM Sans";margin-bottom:.17in}
.rules li::before{content:counter(n);flex:none;width:.36in;height:.36in;border-radius:50%;background:#2F4A3A;color:#F4EBDD;font:700 12pt/.36in "Courier Prime",monospace;text-align:center}
.rules li b{color:#9E2B32}
.keys{display:grid;grid-template-columns:1fr 1fr;gap:.12in .3in;margin:.15in 0 .3in}
.keys div{font:500 11.5pt/1.35 "DM Sans"}
.keys span{display:inline-block;font:700 9pt "Courier Prime",monospace;letter-spacing:.14em;color:#F4EBDD;padding:2px 8px;border-radius:3px;margin-right:6px}
.tips{margin-top:auto;border-top:1.5px solid #3A2A2033;padding-top:.2in;font:500 11pt/1.5 "DM Sans";opacity:.85}
.tips b{font-family:"Fraunces",serif;font-weight:600;font-size:13pt;color:#2F4A3A}
"""

FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;'
         '0,9..144,600;1,9..144,500&family=DM+Sans:wght@500;700&family=Courier+Prime:wght@700&display=swap">')

cover = f"""<div class="page"><div class="full cover">
<div class="eb">THE GIFT EXCHANGE UPGRADE</div>
<h1>Chaos<br><em>Cards</em></h1>
<div class="sub">34 twist cards for white elephant, Yankee swap or any gift exchange that needs a little drama.</div>
<div class="fan">
 <div class="mini" style="--c:#9E2B32">The Heist</div><div class="mini" style="--c:#B0862F">The Secret</div>
 <div class="mini" style="--c:#2F4A3A">Blind Date</div><div class="mini" style="--c:#3A2A20">Plot Twist</div></div>
<div class="sub" style="font-size:13pt;opacity:.75">Print, cut, shuffle. Ruin a friendship or two.</div>
<div class="h">@cozylittlefindsdaily</div>
</div></div>"""

keys = "".join(f'<div><span style="background:{c}">{l}</span>{d}</div>' for (l, c), d in [
    (K["steal"], "take a gift from someone"), (K["swap"], "trade gifts around"),
    (K["save"], "pocket it, play it later"), (K["wild"], "changes the game for everyone")])
rules = f"""<div class="page"><div class="full rules">
<h2>The rules <em>(loosely)</em></h2>
<div class="lede">Play your usual gift exchange. The cards just make sure nobody's gift is ever truly safe.</div>
<ol>
<li><span>Shuffle the cards and put them face down next to the gifts.</span></li>
<li><span>Every time someone <b>opens</b> or <b>steals</b> a gift, they draw one card and read it out loud.</span></li>
<li><span>Do what it says right away, unless it says <b>Keep this card</b>. Those go in your pocket to play whenever you want.</span></li>
<li><span>Your usual house rules still count, like a gift freezing after its third steal.</span></li>
<li><span>When the last gift is opened, anyone holding a saved card gets one last chance to play it.</span></li>
<li><span>The host's word is final. <b>Mostly.</b></span></li>
</ol>
<div class="keys">{keys}</div>
<div class="tips"><b>Printing tips.</b> Print pages 3 to 6 on cardstock at 100% (actual size) and cut along the dashed lines.
The two blank cards are for your own rules, family inside jokes encouraged.<br>
Personal use only, so please send friends to the shop instead of the file.<br>Playing this year? Tag <b>@cozylittlefindsdaily</b> so I can see the chaos.</div>
</div></div>"""

pages = [cover, rules]
for i in range(0, 36, 9):
    pages.append('<div class="page"><div class="grid">' + "".join(card(*c) for c in CARDS[i:i + 9]) + "</div></div>")

doc = f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
OUT.mkdir(exist_ok=True)
src = OUT / "chaos-cards.html"
src.write_text(doc, encoding="utf-8")
pdf = OUT / "chaos-cards.pdf"
subprocess.run([EDGE, "--headless", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=8000",
                f"--print-to-pdf={pdf}", src.as_uri()], check=True, capture_output=True)
print(pdf, pdf.stat().st_size)
