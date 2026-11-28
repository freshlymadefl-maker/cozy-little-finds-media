"""Trial Reels top-up for Sun Nov 29 2026 (owner Nov 28: 4 trial reels/day).
9:30am Amazon relatable reel "Things I'd buy if my husband stopped checking the Amazon app" -> SPOIL list (no prices shown).
3:00pm avatar meme trial reel from posts/avatar2/b07.png (fitting room, fed Nov 28)."""
import pathlib, subprocess
ROOT = pathlib.Path(__file__).resolve().parent.parent
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
OUT = ROOT / "posts" / "trials-1129b"; OUT.mkdir(parents=True, exist_ok=True)
S = lambda n: (ROOT / "src" / n).as_uri()
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




HOOK = film("trend/candles.jpg", "center 60%")
DIM = '<div style="position:absolute;inset:0;background:rgba(20,16,12,.45)"></div>'
d = [shot("am-1", HOOK + '<div class="stack" style="top:470px;font-size:76px">'
          '<span class="tw" style="background:#fff;color:#111">Things I&rsquo;d buy if my husband stopped checking the Amazon app</span></div>'
          '<div class="stack" style="top:1150px;font-size:46px"><span class="tw" style="background:#9E2B32;color:#fff">(asking for me)</span></div>')]
ITEMS = [("bf/thera_w.jpg", "My shoulders have held a grudge since October.", "Theragun"),
         ("bf/blissy_w.jpg", "A silk pillowcase. My hair has been through enough.", "Blissy silk pillowcase"),
         ("u25/laneige.jpg", "Gingerbread lip mask. It&rsquo;s seasonal, so it&rsquo;s mandatory.", "Laneige lip sleeping mask"),
         ("u25/sdj_c.png", "To smell like a vacation I&rsquo;m not taking.", "Sol de Janeiro Cheirosa 62")]
for i, (img, line, name) in enumerate(ITEMS, 2):
    d.append(shot(f"am-{i}", HOOK + DIM +
                  f'<div class="stack" style="top:290px;font-size:54px"><span class="tw" style="background:#F6C9D0;color:#111">{line}</span></div>'
                  f'<div class="card"><img src="{S(img)}"></div>'
                  f'<div class="stack" style="top:1320px"><div class="asof" style="font-size:36px">{name}</div></div>'))
d.append(shot("am-6", HOOK + DIM +
              '<div class="stack" style="top:600px;font-size:72px"><span class="tw" style="background:#fff;color:#111">Comment SPOIL and I&rsquo;ll DM you the list</span></div>'
              '<div class="stack" style="top:1060px;font-size:44px"><span class="tw" style="background:#9E2B32;color:#fff">he doesn&rsquo;t check Instagram.</span></div>'))
build("amazon-husband-app", d, [3.0, 2.6, 2.6, 2.6, 2.6, 3.2])

# 3:00pm avatar meme trial reel (b07 fitting room, fed Nov 28 7:30pm)
AV = ROOT / "posts" / "avatar-reels"
meme = ROOT / "posts" / "avatar2" / "b07.png"
fc = ("[0:v]scale=1080:1350,split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:5,eq=brightness=-0.15[bg];"
      "[b]scale=1144:1430,zoompan=z='min(1+0.0003*on,1.06)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=210:s=1080x1350:fps=30[fg];"
      "[bg][fg]overlay=0:285,format=yuv420p[v]")
mp4 = AV / "fittingroom.mp4"
subprocess.run(["ffmpeg", "-y", "-loop", "1", "-i", str(meme), "-f", "lavfi", "-i", "anullsrc", "-t", "7", "-filter_complex", fc,
                "-map", "[v]", "-map", "1:a", "-c:v", "libx264", "-crf", "20", "-c:a", "aac", "-shortest", "-movflags", "+faststart", str(mp4)],
               check=True, capture_output=True)
subprocess.run(["ffmpeg", "-y", "-ss", "3", "-i", str(mp4), "-frames:v", "1", "-q:v", "3", str(AV / "fittingroom_thumb.jpg")], check=True, capture_output=True)
print("avatar reel done")
