"""Daily Trial Reel for Sun Nov 29 2026 (IG TRIAL_REEL, native look), evening deal reel only (noon slot already has the avatar cafe reel).
deal: 'December purchases I've filed under "household essentials"' -> 3 Walmart deals verified Nov 28 on creator.walmart.com:
MaxKare heated throw (4.4*, 14k reviews), 5-in-1 electric wine opener set (4.9*, 520), Cshidworld massage gun (4.5*, 2.4k, Best seller).
Run: python specs/make_trials_1129.py -> posts/trials-1129/*.png + *.mp4"""
import pathlib, subprocess
ROOT = pathlib.Path(__file__).resolve().parent.parent
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
OUT = ROOT / "posts" / "trials-1129"; OUT.mkdir(parents=True, exist_ok=True)
S = lambda n: (ROOT / "src" / "tr1129" / n).as_uri()
FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@500;600;700&family=Courier+Prime:wght@400;700&display=swap">'
GRAIN = ("url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'>"
         "<feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .5 0 0 0 0 .5 0 0 0 0 .5 0 0 0 .55 0'/></filter>"
         "<rect width='100%' height='100%' filter='url(%23n)'/></svg>\")")
CSS = """*{box-sizing:border-box}html,body{margin:0;width:1080px;height:1920px;overflow:hidden}
body{position:relative;background:#1a1714;font-family:Inter,sans-serif}
.ph{position:absolute;inset:0;background-size:cover;background-position:center;filter:sepia(.28) saturate(.82) contrast(1.06) brightness(.92)}
.grain{position:absolute;inset:0;background-image:GRAIN;opacity:.22;mix-blend-mode:overlay}
.vig{position:absolute;inset:0;background:radial-gradient(ellipse at center,rgba(0,0,0,0) 45%,rgba(0,0,0,.45) 100%)}
.cl{position:absolute;left:80px;right:160px;text-align:center;color:#fff;font-weight:600;text-shadow:0 2px 10px rgba(0,0,0,.55),0 0 2px rgba(0,0,0,.4)}
.tw{font-family:'Courier Prime',monospace;font-weight:700;display:inline;padding:6px 18px;line-height:1.55;-webkit-box-decoration-break:clone;box-decoration-break:clone;border-radius:8px}
.stack{position:absolute;left:70px;right:160px;text-align:center}
.card{position:absolute;left:110px;width:720px;top:560px;height:720px;background:#fff;border-radius:22px;overflow:hidden;box-shadow:0 20px 50px rgba(0,0,0,.4)}
.card img{width:100%;height:100%;object-fit:contain;padding:30px}
.pill{display:inline-block;background:#fff;color:#111;font:700 46px Inter;padding:20px 38px;border-radius:60px;box-shadow:0 6px 18px rgba(0,0,0,.3)}
.pill b{color:#C8102E}
.asof{margin-top:16px;font:600 30px Inter;color:#fff;text-shadow:0 2px 8px rgba(0,0,0,.7)}""".replace("GRAIN", GRAIN)


def shot(name, body):
    f = ROOT / f"_{name}.html"
    f.write_text(f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{body}</body></html>', encoding="utf-8")
    png = OUT / f"{name}.png"
    subprocess.run([EDGE, "--headless", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1", "--window-size=1080,1920",
                    "--virtual-time-budget=6000", f"--screenshot={png}", f.as_uri()], check=True, capture_output=True)
    f.unlink()
    return png


def film(img, pos="center"):
    return f'<div class="ph" style="background-image:url({S(img)});background-position:{pos}"></div><div class="grain"></div><div class="vig"></div>'


def build(key, frames, dur):
    args = ["ffmpeg", "-y"]
    for p, d in zip(frames, dur):
        args += ["-loop", "1", "-t", str(d), "-i", str(p)]
    fc, last, off = [], "[0:v]", 0
    for k in range(1, len(frames)):
        off += dur[k - 1] - 0.4
        fc.append(f"{last}[{k}:v]xfade=transition=fade:duration=0.4:offset={off:.2f}[v{k}]")
        last = f"[v{k}]"
    fc.append(f"{last}format=yuv420p,scale=1080:1920[out]")
    args += ["-filter_complex", ";".join(fc), "-map", "[out]", "-r", "30", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
             "-movflags", "+faststart", str(OUT / f"{key}.mp4")]
    subprocess.run(args, check=True, capture_output=True)
    print(key, round(sum(dur) - 0.4 * (len(dur) - 1), 1), "s")



HOOK = film("1701848734617-192d502be55a.jpg", "center 55%")
d = [shot("deal-1", HOOK + '<div class="stack" style="top:470px;font-size:76px">'
          '<span class="tw" style="background:#9E2B32;color:#fff">December purchases I&rsquo;ve filed under &ldquo;household essentials&rdquo;</span></div>'
          '<div class="stack" style="top:1120px;font-size:46px"><span class="tw" style="background:#fff;color:#111">(Walmart edition)</span></div>')]
ITEMS = [("throw.jpeg", "The house is cold. This is a utility.", "$24.99", "reg $59.99", "$35 off", "MaxKare heated throw &middot; 14K reviews"),
         ("wine.png", "For hosting. Strictly for hosting.", "$16.98", "reg $36.99", "$20 off", "5-in-1 electric wine opener set"),
         ("gun.jpeg", "Wrapping season is a contact sport.", "$24.99", "reg $37.99", "$13 off", "Cshidworld massage gun")]
for i, (img, line, now, was, off, name) in enumerate(ITEMS, 2):
    d.append(shot(f"deal-{i}", HOOK + '<div style="position:absolute;inset:0;background:rgba(20,16,12,.45)"></div>'
                  f'<div class="stack" style="top:290px;font-size:54px"><span class="tw" style="background:#F6C9D0;color:#111">{line}</span></div>'
                  f'<div class="card"><img src="{S(img)}"></div>'
                  f'<div class="stack" style="top:1310px"><div class="pill">{now} <span style="font-weight:500;color:#555">{was}</span> | <b>{off}</b></div>'
                  f'<div class="asof">{name} &middot; price as of Nov 28</div></div>'))
d.append(shot("deal-5", HOOK + '<div style="position:absolute;inset:0;background:rgba(20,16,12,.45)"></div>'
              '<div class="stack" style="top:600px;font-size:72px"><span class="tw" style="background:#fff;color:#111">Comment WALMART and I&rsquo;ll DM you the link</span></div>'
              '<div class="stack" style="top:1060px;font-size:44px"><span class="tw" style="background:#9E2B32;color:#fff">prices change fast. so do I.</span></div>'))
build("deal-household-essentials", d, [3.0, 2.9, 2.9, 2.9, 3.2])
