"""'Wall text' avatar memes (Nov 27 2026): owner-sent reference style (serif text sitting in empty wall/sky space,
like the 'so what are your plans this weekend? me:' and 'Dear Santa I'm a size...' trend). Text goes in the empty
negative space, never on faces. Dark serif on light walls."""
import subprocess, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "posts" / "avatar-wall"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
W = {  # name: (text, top_px, color)
 "m_peek": ("Social battery: 2%.<br>Blanket fort:<br>fully operational.", 330, "#2e2622"),
 "m_robe": ("“Are you coming out tonight?”<br><br>Me:", 300, "#2e2622"),
 "m_shades": ("Did someone<br>say gossip?", 330, "#2e2622"),
 "m_door": ("Self-love is buying<br>the flowers. And the<br>other stuff too.", 170, "#2e2622", 60, 420),
}
def html(img, text, top, color, lft=120, rgt=120):
    return f"""<html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500&display=swap" rel="stylesheet">
<style>*{{margin:0;padding:0}} body{{width:1080px;height:1350px;overflow:hidden;position:relative}}
img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.t{{position:absolute;top:{top}px;left:{lft}px;right:{rgt}px;text-align:center;font-family:'Playfair Display';font-weight:500;
font-size:64px;line-height:1.08;letter-spacing:-1.5px;color:{color}}}</style></head>
<body><img src="{img}"><div class="t">{text}</div></body></html>"""
if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for n, v in W.items():
        t, top, c = v[:3]; lft, rgt = (v[3], v[4]) if len(v) > 3 else (120, 120)
        if sys.argv[1:] and n not in sys.argv[1:]: continue
        p = OUT/f"{n}.html"; p.write_text(html((ROOT/'src'/'avatar'/f'{n}.png').as_uri(), t, top, c, lft, rgt), encoding="utf-8")
        subprocess.run([EDGE,"--headless=new","--disable-gpu","--hide-scrollbars","--window-size=1080,1350","--virtual-time-budget=5000",
                        f"--screenshot={(OUT/f'{n}.png').as_posix()}", p.as_uri()], check=True, capture_output=True)
    print("done")
