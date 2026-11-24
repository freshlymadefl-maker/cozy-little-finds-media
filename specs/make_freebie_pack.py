"""One 'Free Holiday Printables' pack (cover + sampler + bingo + tracker) for the single bio button."""
import pathlib, subprocess, pymupdf
ROOT = pathlib.Path(__file__).resolve().parent.parent; OUT = ROOT / "out"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
ETSY = "https://freshlymadefl.etsy.com/listing/4624952800/white-elephant-game-cards-printable"
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;'
         '1,9..144,500&family=DM+Sans:wght@500;700&family=Courier+Prime:wght@700&display=swap">')
html = f"""<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>@page{{size:8.5in 11in;margin:0}}*{{box-sizing:border-box}}
body{{margin:0;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.p{{width:8.5in;height:11in;background:#2F4A3A;color:#F4EBDD;padding:1in .9in;font-family:'DM Sans';position:relative}}
.eb{{font:700 12pt 'Courier Prime',monospace;letter-spacing:.24em;color:#F8E2A8}}h1{{font:500 56pt/1 Fraunces,serif;margin:.2in 0 .25in}}h1 em{{color:#F8E2A8}}
.it{{border-top:1px solid #F4EBDD44;padding:.22in 0;font:500 14pt/1.4 'DM Sans'}}.it b{{font:600 20pt Fraunces,serif;color:#F8E2A8;display:block}}
.cta{{margin-top:.35in;background:#F4EBDD;color:#2F4A3A;border-radius:.15in;padding:.3in .35in;font:500 13pt/1.5 'DM Sans'}}
.cta b{{font:600 20pt Fraunces,serif;color:#9E2B32}}.cta a{{color:#9E2B32;font-weight:700}}
.h{{position:absolute;bottom:.5in;left:0;right:0;text-align:center;opacity:.75;font-size:11pt}}</style></head><body><div class="p">
<div class="eb">FREE FROM COZY LITTLE FINDS</div><h1>Holiday<br><em>printables</em></h1>
<div class="it"><b>Chaos Cards sampler · pages 2 to 3</b>8 twist cards for your white elephant or Yankee swap.</div>
<div class="it"><b>Cheesy Christmas Movie Bingo · pages 4 to 7</b>4 different cards. Five in a row picks the next movie.</div>
<div class="it"><b>The Christmas Gift Tracker · page 8</b>Who, what, budget, bought, wrapped.</div>
<div class="cta"><b>Want the full Chaos Cards deck?</b><br>34 cards, including December Baby, Cart Confession and The Secret.
Instant download: <a href="{ETSY}">freshlymadefl.etsy.com</a></div>
<div class="h">Gift guides + more finds: @cozylittlefindsdaily · free for personal use</div></div></body></html>"""
src = OUT / "_pack-cover.html"; src.write_text(html, encoding="utf-8"); cov = OUT / "_pack-cover.pdf"
subprocess.run([EDGE, "--headless", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=8000", f"--print-to-pdf={cov}", src.as_uri()], check=True, capture_output=True)
pack = pymupdf.open(cov)
for f in ["Chaos-Cards-Free-Sampler.pdf", "Christmas-Movie-Bingo.pdf", "Christmas-Gift-Tracker.pdf"]:
    pack.insert_pdf(pymupdf.open(OUT / f))
pack.save(OUT / "Free-Holiday-Printables.pdf"); print(pack.page_count)
