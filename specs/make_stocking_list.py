"""'The Stocking Stuffers I "Accidentally" Left in His Amazon Cart' (Nov 26 2026). Bloom-and-Babe format;
products from the Stocking Stuffers list 1D13U8UFN510V (Amazon CDN photos in src/stk).
Cover: src/dec2/stocking.jpg cropped low (no family photos on the mantel in frame)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import make_husband_list as h

ROOT = h.ROOT
h.OUT = ROOT / "posts" / "stocking-list"
h.OUT.mkdir(parents=True, exist_ok=True)
BG = (ROOT / "src" / "dec2" / "stocking.jpg").as_uri()
h.BASE = h.BASE.replace(h.BG, BG).replace("center 35%", "center 72%")
h.BG = BG

OLD = "".join(f"<div>{l}</div>" for l in
              ["The", "Amazon", "List I Sent", "My", "Husband", "So He", "Stops", "Asking", "What I", "Want"])
NEW = "".join(f"<div>{l}</div>" for l in
              ["The", "Stocking", "Stuffers I", "“Accidentally”", "Left in", "His Amazon", "Cart"])

def cover():
    return h.cover().replace(OLD, NEW).replace("top:95px", "top:150px").replace("font-size:116px", "font-size:124px")

ITEMS = [
    ("stk/laneige.jpg", "The <i>Laneige</i> lip mask. Every girl's stocking, every year."),
    ("stk/biodance.jpg", "Collagen eye patches for the <i>morning after</i> the holiday party."),
    ("stk/lipoil.jpg", "e.l.f. lip oil, because I <i>always</i> need another one."),
    ("stk/burts.jpg", "A Burt's Bees tips + toes kit. <i>Tiny</i> and so cute."),
    ("stk/scrunchies.jpg", "Satin scrunchies so my hair stops <i>creasing</i>."),
    ("stk/mirror.jpg", "A light-up compact mirror for the <i>car</i> touch-ups."),
    ("stk/jewelry.jpg", "A travel jewelry case. My earrings need a <i>home</i>."),
    ("stk/hothands.jpg", "HotHands for every <i>cold</i> soccer game this winter."),
]

def last():
    return (h.last().replace("Send this to him (or just screenshot it).", "Leave this open on his phone. Trust me.")
            .replace("Comment SPOIL", "Comment STOCKING"))

_render = h.render
def render(name, html):
    _render(name, html.replace("<html><head>", "<html><head><meta charset=\"utf-8\">"))

if __name__ == "__main__":
    render("01-cover", cover())
    for i, (img, line) in enumerate(ITEMS, start=2):
        render(f"{i:02d}-item", h.item(img, line).replace(
            ".card img{max-width:86%;max-height:86%;object-fit:contain}",
            ".card img{width:86%;height:86%;object-fit:contain;mix-blend-mode:multiply}"))
    render("10-last", last())
    print("done")
