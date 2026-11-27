"""'The Amazon List I'm Sending My Mother-in-Law So She Stops Asking What He Wants' (Nov 26 2026).
Same Bloom-and-Babe format as make_husband_list.py; products from the Gifts for Him list 10QSDVIGJ8PAN
(Amazon CDN photos in src/mil). Cover: src/dec2/him.jpg (Unsplash fireplace, no people)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import make_husband_list as h

ROOT = h.ROOT
h.OUT = ROOT / "posts" / "mil-list"
h.OUT.mkdir(parents=True, exist_ok=True)
BG = (ROOT / "src" / "dec2" / "him.jpg").as_uri()
h.BASE = h.BASE.replace(h.BG, BG)
h.BG = BG

def cover():
    lines = ["The Amazon", "List I'm", "Sending My", "Mother-", "in-Law", "So She", "Stops", "Asking What", "He Wants"]
    return h.cover().replace("".join(f"<div>{l}</div>" for l in
        ["The", "Amazon", "List I Sent", "My", "Husband", "So He", "Stops", "Asking", "What I", "Want"]),
        "".join(f"<div>{l}</div>" for l in lines)).replace("top:95px", "top:120px")

ITEMS = [
    ("mil/leatherman.jpg", "The <i>Leatherman</i>. He will use it every single day. Every. Day."),
    ("mil/ugg.jpg", "UGG slippers, because his current pair is <i>held together by hope</i>."),
    ("mil/fleece.jpg", "A Columbia fleece he'll wear <i>until it falls apart</i>."),
    ("mil/thermapen.jpg", "The Thermapen. For the man who <i>talks about brisket</i>."),
    ("mil/lodge.jpg", "A Lodge cast iron, so he stops <i>borrowing mine</i>."),
    ("mil/stones.jpg", "Whiskey stones in a gift box. <i>Instant</i> fancy."),
    ("mil/wallet.jpg", "A real leather wallet. The old one is <i>a lost cause</i>."),
    ("mil/bose.jpg", "Bose headphones, so he can tune out <i>the whole family</i>. Lovingly."),
]

def last():
    return (h.last().replace("Send this to him (or just screenshot it).", "Send this to her (you're welcome, MIL).")
            .replace("Comment SPOIL", "Comment GENT"))

if __name__ == "__main__":
    h.render("01-cover", cover())
    for i, (img, line) in enumerate(ITEMS, start=2):
        h.render(f"{i:02d}-item", h.item(img, line).replace(
            ".card img{max-width:86%;max-height:86%;object-fit:contain}",
            ".card img{width:86%;height:86%;object-fit:contain;mix-blend-mode:multiply}"))
    h.render("10-last", last())
    print("done")
