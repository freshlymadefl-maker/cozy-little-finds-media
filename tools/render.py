"""Render Cozy Little Finds posts (1080x1350 PNG) from a JSON spec using headless Edge.

Usage: python render.py specs.json
Each spec: {"name": "...", "type": "vintage|plain|engraving|board|cta", ...fields}
Images referenced by "img" are paths relative to this folder (e.g. "src/x.png").
"""
import html, json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
if HERE.name == "tools":  # in the repo, src/ and out/ live at the repo root
    HERE = HERE.parent
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


LINK_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="#3B82F6" stroke-width="2.4" stroke-linecap="round" '
            'stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/>'
            '<path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>')


def collage(s):
    """Hand-assembled cut-out collage (like the owner's "classic + cozy" post).
    Fields: bg (pattern image), photo (optional outfit/scene photo for the left panel), photo_pos (CSS bg position/size,
    default "50% 85%/auto 1700px"), photo_w (default 520), items: [{img, x, y, w, rot}] in paint order (earlier = behind),
    tag (typewriter label, use \\n for a line break), tag_x/tag_y, link (sticker text, default "All on amazon"),
    tag_side "left"|"right". Cut-outs come from tools/cutout.py (transparent PNGs)."""
    pw = s.get("photo_w", 520)
    photo = (f'<div class="photo" style="width:{pw}px;background:url(\'{s["photo"]}\') {s.get("photo_pos", "50% 85%/auto 1700px")} no-repeat"></div>'
             if s.get("photo") else "")
    items = "".join(
        f'<img class="item" src="{i["img"]}" style="left:{i["x"]}px;top:{i["y"]}px;width:{i["w"]}px;transform:rotate({i.get("rot", 0)}deg)">'
        for i in s["items"])
    tx, ty = s.get("tag_x", 64), s.get("tag_y", 820)
    tag = "<br>".join(html.escape(t) for t in s["tag"].split("\n"))
    return f"""<style>{BASE}
body{{background:#2F4A3A url("{s['bg']}") center/cover no-repeat}}
.photo{{position:absolute;left:0;top:0;height:1350px;box-shadow:6px 0 18px rgba(0,0,0,.25)}}
.item{{position:absolute;filter:drop-shadow(0 10px 14px rgba(0,0,0,.38))}}
.tag{{position:absolute;left:{tx}px;top:{ty}px;background:#fff;color:#111;font:400 64px/1.1 "Courier Prime",monospace;padding:22px 34px;text-align:center;box-shadow:0 6px 18px rgba(0,0,0,.25)}}
.link{{position:absolute;left:{tx}px;top:{ty + s.get('link_gap', 190)}px;display:flex;align-items:center;gap:14px;background:#fff;border-radius:22px;padding:16px 30px 16px 22px;font:500 46px "DM Sans",sans-serif;color:#111;box-shadow:0 6px 18px rgba(0,0,0,.25)}}
.link svg{{width:46px;height:46px}}
.ad{{position:absolute;right:28px;bottom:28px;background:#F4EBDD;color:#2F4A3A;font:700 24px "Courier Prime",monospace;letter-spacing:.06em;padding:6px 12px;border-radius:6px}}
</style>{photo}{items}<div class="tag">{tag}</div><div class="link">{LINK_SVG}{html.escape(s.get('link', 'All on amazon'))}</div><div class="ad">#AD</div>"""


def guide(s):
    """Packed gift-guide collage (like the owner's best post, "Holiday Favorites": 2.6K views).
    Fields: items [{img,x,y,w,rot}] packed edge to edge over the top ~75%, eyebrow (small caps line, e.g. "GIFTS FOR HIM"),
    title (big, e.g. "Holiday Favorites"), bg (optional pattern image; default solid pine with a soft diagonal band)."""
    items = "".join(
        f'<img class="item" src="{i["img"]}" style="left:{i["x"]}px;top:{i["y"]}px;width:{i["w"]}px;transform:rotate({i.get("rot", 0)}deg)">'
        for i in s["items"])
    bg = f'url("{s["bg"]}") center/cover no-repeat' if s.get("bg") else "linear-gradient(135deg,#2F4A3A 0 46%,#365444 46% 58%,#2F4A3A 58%)"
    return f"""<style>{BASE}
body{{background:{bg};background-color:#2F4A3A}}
.item{{position:absolute;filter:drop-shadow(0 12px 16px rgba(0,0,0,.42))}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:300px;background:linear-gradient(180deg,rgba(47,74,58,0) 0,rgba(47,74,58,.92) 38%,#2F4A3A 100%)}}
.eb{{position:absolute;left:0;right:0;bottom:200px;text-align:center;color:#F8E2A8;font:700 34px "Courier Prime",monospace;letter-spacing:.2em}}
.title{{position:absolute;left:0;right:0;bottom:64px;text-align:center;color:#F4EBDD;font:600 {s.get('size', 128)}px/1 "Fraunces",serif;letter-spacing:-.015em}}
.link{{position:absolute;left:36px;top:36px;display:flex;align-items:center;gap:12px;background:#fff;border-radius:20px;padding:12px 24px 12px 18px;font:500 36px "DM Sans",sans-serif;color:#111;box-shadow:0 6px 18px rgba(0,0,0,.25);z-index:5}}
.link svg{{width:38px;height:38px}}
.ad{{position:absolute;right:28px;bottom:24px;background:#F4EBDD;color:#2F4A3A;font:700 22px "Courier Prime",monospace;letter-spacing:.06em;padding:5px 11px;border-radius:6px}}
</style>{items}<div class="foot"></div><div class="eb">{html.escape(s.get('eyebrow', ''))}</div><div class="title">{em(s['title'])}</div>
<div class="ad">#AD</div>"""


def tweet(s):
    """Viral plain-text one-liner (looks like a screenshot-able thought, huge send rates).
    Fields: text (use \\n for line breaks), align left|center, bg (default near-white), size (default 62)."""
    lines = "<br>".join(html.escape(t) for t in s["text"].split("\n"))
    al = s.get("align", "left")
    return f"""<style>{BASE}
body{{background:{s.get('bg', '#FBFAF8')};display:flex;align-items:center;justify-content:center}}
.t{{width:960px;text-align:{al};color:#141414;font:500 {s.get('size', 62)}px/1.32 "DM Sans",-apple-system,"Segoe UI",sans-serif;letter-spacing:-.01em}}
.h{{position:absolute;left:0;right:0;bottom:56px;text-align:center;color:#141414;opacity:.28;font:500 24px "DM Sans";letter-spacing:.06em}}
</style><div class="t">{lines}</div><div class="h">@cozylittlefindsdaily</div>"""


def outfit(s):
    """One outfit per slide (for multi-slide outfit carousels, like the owner's reference "Thanksgiving outfits" 13-slide post).
    The garment is the cut-out centerpiece (no person), accessories around it, an occasional whimsical prop.
    Fields: bg (pattern image) or bg_color, title, title_style "script" (handwritten, white) | "banner" (bold caps on a plum bar),
    note (optional small script line bottom-left), items [{img,x,y,w,rot}] (first = garment, paint order = list order)."""
    bg = f'url("{s["bg"]}") center/cover no-repeat' if s.get("bg") else s.get("bg_color", "#4A1430")
    items = "".join(
        f'<img class="item" src="{i["img"]}" style="left:{i["x"]}px;top:{i["y"]}px;width:{i["w"]}px;transform:rotate({i.get("rot", 0)}deg)">'
        for i in s["items"])
    if s.get("title_style") == "banner":
        title = f'<div class="banner">{html.escape(s["title"])}</div>'
    else:
        title = f'<div class="script">{html.escape(s["title"])}</div>'
    note = f'<div class="note">{html.escape(s["note"])}</div>' if s.get("note") else ""
    return f"""<link href="https://fonts.googleapis.com/css2?family=Caveat+Brush&family=Anton&display=swap" rel="stylesheet"><style>{BASE}
body{{background:{bg}}}
.item{{position:absolute;filter:drop-shadow(0 8px 12px rgba(0,0,0,.3))}}
.script{{position:absolute;left:40px;right:40px;top:44px;text-align:center;color:#fff;font:400 88px/1.05 "Caveat Brush",cursive;text-shadow:0 2px 10px rgba(0,0,0,.35);z-index:5}}
.banner{{position:absolute;left:90px;right:90px;top:50px;background:#4A1430;color:#fff;text-align:center;font:400 72px/1.25 "Anton",sans-serif;letter-spacing:.01em;padding:10px 20px;z-index:5}}
.note{{position:absolute;left:60px;bottom:70px;max-width:520px;color:#fff;font:400 54px/1.1 "Caveat Brush",cursive;text-shadow:0 2px 8px rgba(0,0,0,.35);z-index:5}}
.ad{{position:absolute;right:24px;bottom:22px;background:#F4EBDD;color:#2F4A3A;font:700 22px "Courier Prime",monospace;padding:5px 11px;border-radius:6px;z-index:6}}
</style>{items}{title}{note}<div class="ad">#AD</div>"""


KINDS = {"outfit": outfit, "tweet": tweet, "vintage": vintage, "plain": plain, "engraving": engraving, "board": board, "cta": cta, "collage": collage, "guide": guide}


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
