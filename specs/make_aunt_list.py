"""'The Amazon List That Makes You the Favorite Aunt' (Nov 27 2026). Bloom-and-Babe format;
items from the kids list N8WUDSISFISR (KIDLIST DM). Cover: src/trend/presents.jpg (gifts under tree, no people)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import make_husband_list as h

ROOT = h.ROOT
h.OUT = ROOT / "posts" / "aunt-list"
h.OUT.mkdir(parents=True, exist_ok=True)
BG = (ROOT / "src" / "trend" / "presents.jpg").as_uri()
h.BASE = h.BASE.replace(h.BG, BG).replace("center 35%", "center 50%")
h.BG = BG

OLD = "".join(f"<div>{l}</div>" for l in
              ["The", "Amazon", "List I Sent", "My", "Husband", "So He", "Stops", "Asking", "What I", "Want"])
NEW = "".join(f"<div>{l}</div>" for l in ["The Amazon", "List That", "Makes You", "the", "Favorite", "Aunt"])

def cover():
    return (h.cover().replace(OLD, NEW).replace("top:95px", "top:200px").replace("font-size:116px", "font-size:140px")
            .replace("brightness(.78)", "brightness(.62)"))

ITEMS = [
    ("kids/kpop.jpg", "The <i>KPop Demon Hunters</i> bracelet kit. Every 8-year-old wants it."),
    ("kids/crayola.jpg", "The KPop Demon Hunters <i>art case</i>, for the little sister."),
    ("kids/pokemon.jpg", "A Pokémon Elite Trainer Box. You'll be a <i>legend</i>."),
    ("kids/tonies.jpg", "A Toniebox with Bluey. Screen-free, and <i>their parents</i> will love you."),
    ("kids/jellycat.jpg", "A Jellycat bear. Soft enough to <i>steal</i> back for yourself."),
    ("kids/charm.jpg", "A Jellycat bag charm for the <i>tween</i> who's too cool for toys."),
    ("kids/needoh.jpg", "A NeeDoh gummy bear. The fidget they're <i>all</i> obsessed with."),
    ("kids/playdoh.jpg", "Play-Doh cookie kit for the littles. <i>Mess</i> stays at their house."),
]

def last():
    return (h.last().replace("Want the whole list?", "Want the whole list?")
            .replace("Send this to him (or just screenshot it).", "Favorite-aunt status: secured.")
            .replace("Comment SPOIL", "Comment KIDLIST"))

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
