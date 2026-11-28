"""'The Big-Ticket Walmart List I Sent My Husband' (Nov 28 2026). Husband-list format (owner's best carousel).
In-stock items from Walmart collection 594012 'Big Ticket Deals' link walmrt.us/4CyweZS. Prices seen live Nov 28 3:15pm.
Photos: Walmart CDN (src/bigticket)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import make_husband_list as h

h.OUT = h.ROOT / "posts" / "bigticket"
h.OUT.mkdir(parents=True, exist_ok=True)

OLD = "".join(f"<div>{l}</div>" for l in
              ["The", "Amazon", "List I Sent", "My", "Husband", "So He", "Stops", "Asking", "What I", "Want"])
NEW = "".join(f"<div>{l}</div>" for l in
              ["The", "Big-Ticket", "Walmart List", "I Sent My", "Husband", "(It's All", "On Sale,", "So He Has", "No Excuse)"])

def cover():
    return h.cover().replace(OLD, NEW).replace("top:95px", "top:110px").replace("swipe for the list →", "prices as of Nov 28 · swipe →")

P = lambda now, was: f"<br><span style=\"font-family:Oswald;font-size:44px;letter-spacing:1px\">{now} <s style=\"opacity:.7\">{was}</s></span>"
ITEMS = [
    ("bigticket/5.jpg", "The <i>Dyson</i>. I've been very patient." + P("$399.99", "$729.99")),
    ("bigticket/1.jpg", "Nugget ice at home. <i>The good ice.</i>" + P("$179", "$279")),
    ("bigticket/2.jpg", "An espresso machine, so my coffee budget can <i>retire</i>." + P("$79", "$149.95")),
    ("bigticket/3.jpg", "A 15-piece knife set for <i>thirty-two dollars</i>." + P("$31.99", "$199.99")),
    ("bigticket/4.jpg", "The Blackstone. <i>He</i> cooks. Everyone wins." + P("$150", "$224")),
    ("bigticket/6.jpg", "A lit gold wreath so the front door looks <i>expensive</i>." + P("$77.99", "$129.99")),
    ("bigticket/7.jpg", "A mini projector. Movie night on the <i>bedroom wall</i>." + P("$42.99", "$99.99")),
]

def last():
    return (h.last().replace("Want the whole list?", "Want every link?")
            .replace("Send this to him (or just screenshot it).", "Send it to him. Prices change fast.")
            .replace("Comment SPOIL", "Comment WALMART"))

_render = h.render
def render(name, html):
    _render(name, html.replace("<html><head>", "<html><head><meta charset=\"utf-8\">"))

if __name__ == "__main__":
    render("01-cover", cover())
    for i, (img, line) in enumerate(ITEMS, start=2):
        render(f"{i:02d}-item", h.item(img, line).replace("top:1010px", "top:990px").replace(
            ".card img{max-width:86%;max-height:86%;object-fit:contain}",
            ".card img{width:86%;height:86%;object-fit:contain;mix-blend-mode:multiply}"))
    render("09-last", last())
    print("done")
