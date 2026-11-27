"""'The Walmart Finds That Make My House Look Way More Expensive' (Nov 27 2026). Bloom-and-Babe format;
in-stock items from Walmart collection 585374 'Favorite Home Essentials (That Look Expensive)',
link walmrt.us/3Xbf5Fe. Photos: Walmart CDN (src/wmhome). Cover: src/dec/cozy.jpg (no people)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import make_husband_list as h

ROOT = h.ROOT
h.OUT = ROOT / "posts" / "walmart-home"
h.OUT.mkdir(parents=True, exist_ok=True)
BG = (ROOT / "src" / "dec" / "cozy.jpg").as_uri()
h.BASE = h.BASE.replace(h.BG, BG).replace("center 35%", "center 55%")
h.BG = BG

OLD = "".join(f"<div>{l}</div>" for l in
              ["The", "Amazon", "List I Sent", "My", "Husband", "So He", "Stops", "Asking", "What I", "Want"])
NEW = "".join(f"<div>{l}</div>" for l in
              ["The", "Walmart", "Finds That", "Make My", "House Look", "Way More", "Expensive"])

def cover():
    return h.cover().replace(OLD, NEW).replace("top:95px", "top:170px").replace("font-size:116px", "font-size:128px")

ITEMS = [
    ("wmhome/2.jpg", "The <i>Beautiful</i> air fryer. Finally one I don't hide in a cabinet."),
    ("wmhome/5.jpg", "The matching kettle. <i>White Icing</i> + gold = instant upgrade."),
    ("wmhome/3.jpg", "And the toaster, because the set <i>has</i> to match."),
    ("wmhome/4.jpg", "A white + gold knife block that looks <i>so</i> much pricier."),
    ("wmhome/6.jpg", "Cashmere Teak candle. Smells like a <i>fancy</i> hotel lobby."),
    ("wmhome/7.jpg", "A textured pillow that makes the couch look <i>styled</i>."),
    ("wmhome/8.jpg", "An ivory ceramic vase. Add grocery store stems. <i>Done.</i>"),
    ("wmhome/1.jpg", "Seagrass baskets that hide <i>all</i> the chaos."),
]

def last():
    return (h.last().replace("Want the whole list?", "Want every link?")
            .replace("Send this to him (or just screenshot it).", "No one has to know it's Walmart.")
            .replace("Comment SPOIL", "Comment WALMART"))

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
