"""Walmart Trial Reels (IG TRIAL_REEL, shown to non-followers), Nov 25 2026.
Recipe from the winning Reel (owner): moody pretty photo + elegant serif hook + good music; real products shown as arch 'stickers' over the photo.
Run: python specs/make_walmart_trials.py  -> posts/walmart/wm-trial-<key>.mp4 + frames"""
import pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;'
         '1,9..144,400&family=DM+Sans:wght@500;700&family=Courier+Prime:wght@700&display=swap">')
OUT = ROOT / "posts" / "walmart"
L = lambda n: (ROOT / "src" / "wm" / f"{n}.jpg").as_uri()
P = lambda n: (ROOT / "src" / "wmp" / f"{n}.jpg").as_uri()
CSS = """*{box-sizing:border-box}html,body{margin:0;width:1080px;height:1920px;overflow:hidden}
body{position:relative;font-family:'DM Sans',sans-serif;background:#111;color:#F4EBDD}
.ph{position:absolute;inset:0;background-size:cover;background-position:center}
.dim{position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,18,14,.62) 0%,rgba(20,18,14,.35) 45%,rgba(20,18,14,.65) 100%)}
.top{position:absolute;left:90px;right:170px;top:300px;text-align:center}
.eb{font:700 34px 'Courier Prime',monospace;letter-spacing:.24em;color:#F8E2A8}
.t{margin-top:24px;font:500 96px/1.04 Fraunces,serif;letter-spacing:-.015em;text-shadow:0 4px 24px rgba(0,0,0,.45)}.t em{font-style:italic;font-weight:400;color:#F8E2A8}
.mid{position:absolute;left:90px;right:170px;top:560px;text-align:center}
.arch{position:absolute;left:250px;width:500px;top:760px;height:620px;border-radius:260px 260px 24px 24px;background:#fff;overflow:hidden;box-shadow:0 24px 60px rgba(0,0,0,.45)}
.arch img{width:100%;height:100%;object-fit:contain;padding:70px 36px 24px}
.name{position:absolute;left:90px;right:170px;top:1405px;text-align:center;font:italic 400 40px Fraunces,serif;color:#F4EBDD;text-shadow:0 2px 12px rgba(0,0,0,.7)}
.pill{display:inline-block;margin-top:50px;background:#9E2B32;color:#F4EBDD;font:700 44px 'DM Sans';padding:26px 50px;border-radius:70px}
.sm{margin-top:28px;font:500 34px 'DM Sans';opacity:.85}"""
REELS = {
 "her": ("1795330796412-80b543884f4c", "MY GIFT RULE", "If she wouldn't buy it <em>for herself</em>, it's the perfect gift.", [
   ("1766393030565-12f744515335", "juicy", "Perfume sets", "<em>(this year's #1 gift set)</em>", "Juicy Couture Viva La Juicy Travel Set"),
   ("1795330796361-66200522dde4", "satin", "Satin everything", "<em>beauty sleep, upgraded</em>", "Satin Pillowcases, 2-Pack"),
   ("1734898537962-2dc575c99e11", "claw", "Claw clips", "<em>her whole hairstyle</em>", "Scunci Open Cut Claw Clips"),
   ("1795330796412-80b543884f4c", "coach", "The splurge", "<em>smells like a designer bag</em>", "Coach Signature Perfume Gift Set")],
  "1640505933280-82074a4836d6"),
 "kids": ("1546512347-b93b3f59e231", "MY TOY RULE", "No batteries. No screens. <em>Still the favorite.</em>", [
   ("1703319955806-8104553f0b92", "squish", "The one they'll", "<em>sleep with every night</em>", "Hello Kitty Squishmallow"),
   ("1629760946220-5693ee4c46ac", "beyblade", "Battle royale,", "<em>living room edition</em>", "Beyblade X Xtreme Battle Set"),
   ("1766393030565-12f744515335", "lego-unicorn", "Built in an afternoon,", "<em>played all break</em>", "LEGO Friends Unicorn Cake Car"),
   ("1546512347-b93b3f59e231", "needoh-ice", "The stocking stuffer", "<em>they won't put down</em>", "NeeDoh Nice Ice Baby")],
  "1640505933280-82074a4836d6"),
}


def shot(name, body):
    f = ROOT / f"_{name}.html"
    f.write_text(f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{body}</body></html>', encoding="utf-8")
    png = OUT / f"{name}.png"
    subprocess.run([EDGE, "--headless", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1", "--window-size=1080,1920",
                    "--virtual-time-budget=6000", f"--screenshot={png}", f.as_uri()], check=True, capture_output=True)
    return png


for key, (ph, eb, hook, items, endph) in REELS.items():
    if len(sys.argv) > 1 and key not in sys.argv[1:]:
        continue
    frames = [shot(f"wm-trial-{key}-1", f'<div class="ph" style="background-image:url({L(ph)})"></div><div class="dim"></div>'
                   f'<div class="mid"><div class="eb">{eb}</div><div class="t" style="font-size:104px">{hook}</div></div>')]
    for i, (bg, img, a, b, prod) in enumerate(items, 2):
        frames.append(shot(f"wm-trial-{key}-{i}", f'<div class="ph" style="background-image:url({L(bg)})"></div><div class="dim"></div>'
                           f'<div class="top"><div class="t" style="font-size:84px">{a}<br>{b}</div></div>'
                           f'<div class="arch"><img src="{P(img)}"></div><div class="name">{prod}</div>'))
    n = len(frames) + 1
    frames.append(shot(f"wm-trial-{key}-{n}", f'<div class="ph" style="background-image:url({L(endph)})"></div><div class="dim"></div>'
                       f'<div class="mid"><div class="eb">ALL AT WALMART</div><div class="t">Find them in my <em>Walmart storefront</em> &#10022;</div>'
                       f'<div class="pill">Comment WALMART &#10022;</div><div class="sm">or tap the link in my bio</div></div>'))
    dur = [3.2] + [2.4] * (len(frames) - 2) + [3.4]
    args = ["ffmpeg", "-y"]
    for p, d in zip(frames, dur):
        args += ["-loop", "1", "-t", str(d), "-i", str(p)]
    fc, last, off = [], "[0:v]", 0
    for k in range(1, len(frames)):
        off += dur[k - 1] - 0.4
        fc.append(f"{last}[{k}:v]xfade=transition=fade:duration=0.4:offset={off:.2f}[v{k}]")
        last = f"[v{k}]"
    fc.append(f"{last}format=yuv420p,scale=1080:1920[out]")
    args += ["-filter_complex", ";".join(fc), "-map", "[out]", "-r", "30", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-movflags", "+faststart", str(OUT / f"wm-trial-{key}.mp4")]
    subprocess.run(args, check=True, capture_output=True)
    print(key, "ok", round(sum(dur) - 0.4 * (len(dur) - 1), 1), "s")
