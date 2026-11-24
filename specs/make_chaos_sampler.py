"""Free 'Chaos Cards Sampler' (2 pages): 8 cards + an upsell card to the $4.99 Etsy deck.
Hosted free on GitHub (raw PDF). Run: python specs/make_chaos_sampler.py
"""
import pathlib, subprocess

SRC = pathlib.Path(__file__).with_name("make_chaos.py").read_text(encoding="utf-8")
exec(SRC.split("cover = f")[0])  # CARDS, K, em, card, CSS, FONTS, ROOT, OUT, EDGE

ETSY = "https://freshlymadefl.etsy.com/listing/4624952800/white-elephant-game-cards-printable"
PICK = [0, 1, 2, 4, 6, 10, 14, 28]  # Heist, Left Right Chaos, Bodyguard, Ice Queen, Blind Date, Regift, Compliment Tax, A Toast
up = (f'<div class="card" style="--c:#2F4A3A"><a class="in up" href="{ETSY}">'
      '<div class="kind">WANT MORE?</div><div class="t">26 more cards</div><div class="rule"></div>'
      '<div class="b">Including <em>December Baby</em>, <em>Cart Confession</em> and <em>The Secret</em>.<br><br>'
      'Get the full deck at <b>freshlymadefl.etsy.com</b></div><div class="ft">CHAOS CARDS</div></a></div>')
EXTRA = ".up{text-decoration:none;color:inherit;background:#2F4A3A!important;color:#F4EBDD}.up .t,.up .b em{color:#F8E2A8!important}.up .kind{background:#F8E2A8;color:#2F4A3A}.up .rule{background:#F8E2A8}"
p1 = f"""<div class="page"><div class="full rules">
<div style="font:700 11pt 'Courier Prime',monospace;letter-spacing:.24em;color:#9E2B32">FREE SAMPLER</div>
<h2 style="margin-top:.12in">Chaos Cards <em>(the sampler)</em></h2>
<div class="lede">8 free twist cards for your white elephant, Yankee swap or gift exchange. Print page 2, cut, shuffle.</div>
<ol>
<li><span>Play your usual gift exchange. Put the shuffled cards face down next to the gifts.</span></li>
<li><span>Every time someone <b>opens</b> or <b>steals</b> a gift, they draw a card and read it out loud.</span></li>
<li><span>Do what it says right away, unless it says <b>Keep this card</b>. Pocket those and play them later.</span></li>
<li><span>The host's word is final. <b>Mostly.</b></span></li>
</ol>
<div class="tips" style="margin-top:.3in"><b>Want the full deck?</b> 34 cards plus 2 blank ones for your own house rules, including the fan favorites
<b>December Baby</b>, <b>Cart Confession</b> and <b>The Secret</b>. Instant download at
<a href="{ETSY}" style="color:#9E2B32;font-weight:700">freshlymadefl.etsy.com</a>.<br><br>
Free for personal use. Share the love by sending friends to <b>@cozylittlefindsdaily</b>.</div>
</div></div>"""
p2 = '<div class="page"><div class="grid">' + "".join(card(*CARDS[i]) for i in PICK) + up + "</div></div>"
doc = f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}{EXTRA}</style></head><body>{p1}{p2}</body></html>'
src = OUT / "chaos-sampler.html"
src.write_text(doc, encoding="utf-8")
pdf = OUT / "Chaos-Cards-Free-Sampler.pdf"
subprocess.run([EDGE, "--headless", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=8000",
                f"--print-to-pdf={pdf}", src.as_uri()], check=True, capture_output=True)
print(pdf, pdf.stat().st_size)
