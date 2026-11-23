"""Render Cozy Little Finds posts (1080x1350 PNG) from a JSON spec using headless Edge.

Usage: python render.py specs.json
Each spec: {"name": "...", "type": "vintage|plain|engraving|board|cta", ...fields}
Images referenced by "img" are paths relative to this folder (e.g. "src/x.png").
"""
import html, json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;'
         '0,9..144,500;0,9..144,600;1,9..144,400;1,9..144,500&family=DM+Sans:wght@500;700&family=Courier+Prime:wght@700'
         '&family=Fredoka:wght@700&display=swap">')
BASE = "html,body{margin:0;width:1080px;height:1350px}body{position:relative;overflow:hidden}"
HANDLE = '<div class="handle">@cozylittlefindsdaily</div>'


def em(text):
    """Escape, then turn *word* into an accent <em>."""
    out, parts = [], html.escape(text).split("*")
    for i, p in enumerate(parts):
        out.append(f"<em>{p}</em>" if i % 2 else p)
    return "".join(out)


def vintage(s):
    pos = s.get("box", "bottom")
    where = "bottom:150px" if pos == "bottom" else "top:110px"
    return f"""<style>{BASE}
body{{background:#3A2A20 url("{s['img']}") center {s.get('focus','30%')}/cover no-repeat}}
.cap{{position:absolute;left:50%;{where};transform:translateX(-50%);width:max-content;max-width:840px;box-sizing:border-box;
background:#fff;color:#111;border-radius:26px;padding:30px 44px;text-align:center;font:700 {s.get('size',54)}px/1.18 "DM Sans",sans-serif;
box-shadow:0 6px 24px rgba(0,0,0,.25)}}
.handle{{position:absolute;left:0;right:0;bottom:56px;text-align:center;color:#fff;font:500 28px "DM Sans";letter-spacing:.03em;text-shadow:0 1px 6px rgba(0,0,0,.6)}}
</style><div class="cap">{html.escape(s['text'])}</div>{HANDLE}"""


def plain(s):
    bg, fg, acc = (("#2F4A3A", "#F4EBDD", "#F8E2A8") if s.get("dark") else ("#F4EBDD", "#2F4A3A", "#9E2B32"))
    eyebrow = f'<div class="eb">{html.escape(s["eyebrow"])}</div>' if s.get("eyebrow") else ""
    return f"""<style>{BASE}
body{{background:{bg};color:{fg};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:34px}}
.eb{{font:700 30px "Courier Prime",monospace;letter-spacing:.18em;color:{acc}}}
.q{{width:840px;text-align:center;font:400 {s.get('size',80)}px/1.14 "Fraunces",serif;letter-spacing:-.01em}}
.q em{{font-style:italic;color:{acc}}}
.mark{{position:absolute;left:0;right:0;bottom:72px;text-align:center;font:700 26px/.95 "Fredoka",sans-serif;letter-spacing:.06em;opacity:.55}}
</style>{eyebrow}<div class="q">{em(s['text'])}</div><div class="mark">COZY<br>LITTLE<br>FINDS</div>"""


def engraving(s):
    bg = s.get("bg", "rgb(13,78,62)")
    eyebrow = f'<div class="eb">{html.escape(s["eyebrow"])}</div>' if s.get("eyebrow") else ""
    sub = f'<div class="sub">{em(s["sub"])}</div>' if s.get("sub") else ""
    return f"""<style>{BASE}
body{{background:{bg};font-family:"DM Sans",sans-serif}}
.top{{position:absolute;left:100px;right:100px;top:130px;display:flex;flex-direction:column;align-items:center;gap:24px;text-align:center}}
.eb{{color:#F8E2A8;font:700 30px "Courier Prime",monospace;letter-spacing:.18em}}
.q{{color:#F4EBDD;font:500 {s.get('size',80)}px/1.08 "Fraunces",serif;letter-spacing:-.01em}}
.q em{{color:#F8E2A8;font-style:italic}}
.sub{{color:#F4EBDD;opacity:.9;font:500 34px/1.4 "DM Sans",sans-serif;max-width:820px}}
.sub em{{font-style:normal;color:#F8E2A8;font-weight:700}}
.art{{position:absolute;left:50%;top:{s.get('art_top',560)}px;width:{s.get('art',640)}px;height:{s.get('art',640)}px;transform:translateX(-50%);
background:{bg} url("{s['img']}") center/cover no-repeat;-webkit-mask-image:radial-gradient(closest-side,#000 72%,transparent 100%)}}
.handle{{position:absolute;left:0;right:0;bottom:56px;text-align:center;color:#F4EBDD;font:500 28px "DM Sans";letter-spacing:.03em;opacity:.8}}
</style><div class="top">{eyebrow}<div class="q">{em(s['text'])}</div>{sub}</div><div class="art"></div>{HANDLE}"""


def board(s):
    dots = "".join(
        f'<div class="dot{" h" if i % 3 == 1 else ""}" style="left:{x}px;top:{y}px">{i + 1}</div>'
        for i, (x, y) in enumerate(s["dots"]))
    return f"""<style>{BASE}
body{{background:#F4EBDD url("{s['img']}") center/cover no-repeat}}
.tag{{position:absolute;left:56px;top:56px;background:#FFFBF4;color:#3A2A20;font:700 44px/1 "Courier Prime",monospace;padding:20px 30px 20px 60px;border-radius:10px;transform:rotate(-3deg);box-shadow:0 4px 14px rgba(58,42,32,.28)}}
.tag::before{{content:"";position:absolute;left:24px;top:50%;width:18px;height:18px;margin-top:-9px;border-radius:50%;background:#F4EBDD;box-shadow:inset 0 0 0 2px #E6D6BF}}
.ad{{position:absolute;left:64px;top:150px;background:#9E2B32;color:#F4EBDD;font:700 26px "Courier Prime",monospace;letter-spacing:.06em;padding:8px 16px;border-radius:8px;transform:rotate(-3deg)}}
.dot{{position:absolute;width:72px;height:72px;border-radius:50%;background:#2F4A3A;color:#F4EBDD;font:700 36px/64px "Courier Prime",monospace;text-align:center;box-shadow:0 3px 12px rgba(0,0,0,.28);border:4px solid #F4EBDD;box-sizing:border-box}}
.dot.h{{background:#C8963E;color:#3A2A20}}
</style><div class="tag">{html.escape(s['tag'])}</div><div class="ad">#AD</div>{dots}"""


def cta(s):
    items = "".join(f"<li>{html.escape(t)}</li>" for t in s["items"])
    return f"""<style>{BASE}
body{{background:#2F4A3A;color:#F4EBDD;font-family:"DM Sans",sans-serif}}
.wrap{{position:absolute;left:110px;right:110px;top:50%;transform:translateY(-54%);display:flex;flex-direction:column;gap:40px}}
h1{{margin:0;font:600 88px/1.0 "Fraunces",serif}}
ol{{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:22px;counter-reset:n}}
li{{counter-increment:n;display:flex;gap:24px;align-items:center;font:500 42px/1.2 "DM Sans",sans-serif}}
li::before{{content:counter(n);flex:none;width:60px;height:60px;border-radius:50%;background:#F4EBDD;color:#2F4A3A;font:700 30px/60px "Courier Prime",monospace;text-align:center}}
li:nth-child(3n+2)::before{{background:#C8963E;color:#3A2A20}}
.key{{align-self:flex-start;background:#F8E2A8;color:#2F4A3A;font:700 46px "Courier Prime",monospace;padding:16px 30px;border-radius:10px;transform:rotate(-2deg);margin-top:10px}}
.sub{{font:500 32px/1.35 "DM Sans",sans-serif;opacity:.9}}
.handle{{position:absolute;left:0;right:0;bottom:64px;text-align:center;font:500 28px "DM Sans";letter-spacing:.03em;opacity:.85}}
</style><div class="wrap"><h1>{html.escape(s.get('title','Shop the picks'))}</h1><ol>{items}</ol>
<div class="key">link in bio</div><div class="sub">My Amazon favorites for every item, all in one place.</div></div>{HANDLE}"""


KINDS = {"vintage": vintage, "plain": plain, "engraving": engraving, "board": board, "cta": cta}


def render(spec):
    body = KINDS[spec["type"]](spec)
    page = HERE / f"_{spec['name']}.html"
    page.write_text(f'<!doctype html><html><head><meta charset="utf-8">{FONTS}</head><body>{body}</body></html>', encoding="utf-8")
    out = HERE / "out" / f"{spec['name']}.png"
    out.parent.mkdir(exist_ok=True)
    subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--window-size=1080,1350",
                    "--virtual-time-budget=5000", f"--screenshot={out.as_posix()}", page.as_uri()],
                   capture_output=True, timeout=90)
    print(out.name, "ok" if out.exists() else "FAILED")


if __name__ == "__main__":
    for spec in json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")):
        render(spec)
