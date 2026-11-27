"""Relatable meme posts using the owner's AI-made avatar (Nov 27 2026). Big warm-yellow bold text over the photo,
like @bumblebeebbee's 'Im tired I deserve a Chanel bag'. Always post with the AI label on."""
import subprocess, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "posts" / "avatar"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
MEMES = [
    ("cart", "My husband:<br>we have enough<br>decorations<br><br>Me:", "top:150px"),
    ("cafe", "Me pretending I<br>didn't just spend<br>$400 on Black Friday", "top:120px"),
    ("pjs", "Christmas Eve plans:<br>matching PJs,<br>champagne,<br>zero cooking", "top:120px"),
    ("wine", "Financially<br>irresponsible,<br>but festively", "top:760px"),
]
def html(img, text, pos):
    return f"""<html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@800&display=swap" rel="stylesheet">
<style>*{{margin:0;padding:0}} body{{width:1080px;height:1350px;overflow:hidden;position:relative;background:#000}}
img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.t{{position:absolute;{pos};left:40px;right:40px;text-align:center;font-family:Montserrat;font-weight:800;font-size:78px;line-height:1.08;
color:#f6dc8f;letter-spacing:-1px;text-shadow:0 3px 14px rgba(0,0,0,.55),0 1px 3px rgba(0,0,0,.6)}}</style></head>
<body><img src="{img}"><div class="t">{text}</div></body></html>"""
if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, text, pos in MEMES:
        p = OUT / f"{name}.html"; p.write_text(html((ROOT/'src'/'avatar'/f'{name}.png').as_uri(), text, pos), encoding="utf-8")
        subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--window-size=1080,1350",
                        "--virtual-time-budget=5000", f"--screenshot={(OUT/f'{name}.png').as_posix()}", p.as_uri()], check=True, capture_output=True)
    print("done")
