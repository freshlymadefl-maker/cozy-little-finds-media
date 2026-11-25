"""Morning-find swaps (owner Nov 25 2026: 'we're sharing the same product over and over, do a variety').
Replaces 7 Dec morning finds that repeated Black Friday deal products with products not featured anywhere else."""
import json, pathlib, subprocess
ROOT = pathlib.Path(__file__).resolve().parent.parent
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
TPL = (ROOT / "_f2-12-03-07.html").read_text(encoding="utf-8")
L = {"MORNING": "P6V8V2VG6HIH", "GIFTS": "10QSDVIGJ8PAN", "WOOF": "3B8R1HJU8LGPS", "SWAP": "WDTTRUUMBWB6",
     "TEACHER": "RY4NCYOFPW3L", "WRAP": "2YYODQJGDA89R", "HUSBAND": "2SYJP9HLUNRNU"}
# date, img, eyebrow, hook(html), product, keyword
D = [
 ("12-03", "src/brand/ember.png", "EMBER", "His coffee, still hot <em>at 10am.</em>", "Ember Smart Mug", "GIFTS"),
 ("12-04", "src/dec3/benebone.jpg", "BENEBONE", "Survives the <em>power chewer.</em>", "Benebone Wishbone Chew", "WOOF"),
 ("12-06", "src/dec3/lodge.jpg", "LODGE", "Christmas breakfast, <em>done right.</em>", "Lodge Cast Iron Skillet", "MORNING"),
 ("12-11", "src/glass.png", "FOR HIM", "Whiskey on the rocks, <em>but fancy.</em>", "Whiskey Glass + Ice Sphere", "HUSBAND"),
 ("12-12", "src/him/yeti.png", "YETI", "Coffee stays hot <em>through recess.</em>", "YETI Rambler Tumbler", "TEACHER"),
 ("12-16", "src/moccasins.png", "FOR HIM", "His version of UGGs. <em>Don't tell him.</em>", "Men's Moccasin Slippers", "HUSBAND"),
 ("12-19", "src/dec3/oranges.jpg", "GIFT WRAP", "The wrap detail that <em>smells like Christmas.</em>", "Dried Orange Slices", "WRAP"),
]
out = ROOT / "posts" / "2026-f3"; out.mkdir(parents=True, exist_ok=True)
meta = []
for d, img, eb, hook, prod, kw in D:
    h = (TPL.replace("☕ MORNING FIND · KENDRA SCOTT", "☕ MORNING FIND · " + eb)
            .replace('The gift that never gets <em>returned.</em>', hook)
            .replace("src/dec3/kendra.jpg", img).replace("Kendra Scott Elisa Necklace", prod).replace("<b>MOM</b>", f"<b>{kw}</b>"))
    f = ROOT / f"_f3-{d}.html"; f.write_text(h, encoding="utf-8")
    png = out / f"f3-{d}.png"
    subprocess.run([EDGE, "--headless", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1", "--window-size=1080,1350",
                    "--virtual-time-budget=6000", f"--screenshot={png}", f.as_uri()], check=True, capture_output=True)
    meta.append({"date": d, "png": png.name, "hook": hook.replace("<em>", "").replace("</em>", ""), "prod": prod, "kw": kw, "list": L[kw]})
    print(png.name)
json.dump(meta, open(ROOT / "specs" / "find3-meta.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
