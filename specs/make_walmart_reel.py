"""Walmart launch Reel (Nov 25 2026): moody photo frames + serif text, music added via IG audio. Safe zone y 260-1460, right 140px clear."""
import pathlib, subprocess
ROOT = pathlib.Path(__file__).resolve().parent.parent
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;'
         '1,9..144,400&family=DM+Sans:wght@500;700&family=Courier+Prime:wght@700&display=swap">')
OUT = ROOT / "posts" / "walmart"
F = [
 ("1766393030565-12f744515335", "MY WALMART RULE", "If hundreds of people didn't rate it <em>4 stars</em>, it's not on my list.", ""),
 ("1795330796412-80b543884f4c", "FOR HER", "Cozy gifts <em>under $50</em>", "pajama sets · slippers · sherpa throws"),
 ("1546512347-b93b3f59e231", "FOR THE KIDS", "What they <em>actually</em> want", "Squishmallows · NeeDoh · Beyblade X"),
 ("1688437307687-fe226bddfab1", "FOR THE HOSTESS", "Hosting, <em>done easy</em>", "boards · taper candles · coupes"),
 ("1629760946220-5693ee4c46ac", "FOR CHRISTMAS BREAK", "Phones-down <em>game night</em>", "UNO No Mercy · Phase 10 · puzzles"),
 ("1640505933280-82074a4836d6", "NOW OPEN", "My Walmart <em>storefront</em> ✦", "PILL"),
]
CSS = """*{box-sizing:border-box}html,body{margin:0;width:1080px;height:1920px;overflow:hidden}
body{position:relative;font-family:'DM Sans',sans-serif;background:#111}
.ph{position:absolute;inset:0;background-size:cover;background-position:center}
.dim{position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,18,14,.55) 0%,rgba(20,18,14,.35) 45%,rgba(20,18,14,.6) 100%)}
.box{position:absolute;left:90px;right:170px;top:560px;text-align:center;color:#F4EBDD}
.eb{font:700 34px 'Courier Prime',monospace;letter-spacing:.24em;color:#F8E2A8}
.t{margin-top:26px;font:500 104px/1.04 Fraunces,serif;letter-spacing:-.015em;text-shadow:0 4px 24px rgba(0,0,0,.45)}.t em{font-style:italic;font-weight:400;color:#F8E2A8}
.s{margin-top:34px;font:italic 400 44px/1.25 Fraunces,serif;color:#F4EBDD;opacity:.92}
.pill{display:inline-block;margin-top:50px;background:#9E2B32;color:#F4EBDD;font:700 44px 'DM Sans';padding:26px 50px;border-radius:70px}
.sm{margin-top:28px;font:500 34px 'DM Sans';opacity:.85}"""
frames = []
for i, (ph, eb, t, s) in enumerate(F, 1):
    img = (ROOT / "src" / "wm" / f"{ph}.jpg").as_uri()
    sub = '<div class="pill">Comment WALMART ✦</div><div class="sm">or tap the link in my bio</div>' if s == "PILL" else (f'<div class="s">{s}</div>' if s else "")
    body = f'<div class="ph" style="background-image:url({img})"></div><div class="dim"></div><div class="box"><div class="eb">{eb}</div><div class="t">{t}</div>{sub}</div>'
    f = ROOT / f"_wm-reel-{i}.html"
    f.write_text(f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{body}</body></html>', encoding="utf-8")
    png = OUT / f"wm-reel-{i}.png"
    subprocess.run([EDGE, "--headless", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1", "--window-size=1080,1920",
                    "--virtual-time-budget=6000", f"--screenshot={png}", f.as_uri()], check=True, capture_output=True)
    frames.append(png)
# ffmpeg crossfade: first frame 3.5s (hook), middle 2.6s, last 3.5s, 0.5s fades
dur = [3.5, 2.6, 2.6, 2.6, 2.6, 3.5]
args = ["ffmpeg", "-y"]
for p, d in zip(frames, dur):
    args += ["-loop", "1", "-t", str(d), "-i", str(p)]
fc, last, off = [], "[0:v]", 0
for k in range(1, len(frames)):
    off += dur[k-1] - 0.5
    lab = f"[v{k}]"
    fc.append(f"{last}[{k}:v]xfade=transition=fade:duration=0.5:offset={off:.2f}{lab}")
    last = lab
fc.append(f"{last}format=yuv420p,scale=1080:1920[out]")
args += ["-filter_complex", ";".join(fc), "-map", "[out]", "-r", "30", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-movflags", "+faststart", str(OUT / "wm-launch-reel.mp4")]
subprocess.run(args, check=True, capture_output=True)
print("ok", sum(dur) - 0.5 * (len(dur) - 1))
