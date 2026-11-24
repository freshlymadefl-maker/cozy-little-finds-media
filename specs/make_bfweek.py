"""Black Friday week push (Nov 24-27, 2026): extra pins, 2 Reels, 6 Stories, a Friday carousel."""
import json
exec(open("specs/make_pins.py", encoding="utf-8").read().split("out = []")[0])
out = []
def pin(name, eb, title, sub, keys, size=104, dark=False):
    out.append({"name": "pin-" + name, "type": "pin", "eyebrow": eb, "title": title, "sub": sub, "imgs": [P[k] for k in keys], "size": size, "dark": dark})
pin("bf-a", "BLACK FRIDAY 2026", "Black Friday deals *worth it*", "the only ones I'd buy", ["bdthrow", "blissy", "stanley", "thera"], 108)
pin("bf-b", "BLACK FRIDAY", "Big gifts to buy *on sale*", "the splurges worth waiting for", ["thera", "boseqc", "ugg", "bdthrow"], 108, True)
pin("bf-c", "AMAZON FINDS", "Best Black Friday *gift* finds", "for her, him + the house", ["bdthrow", "ugg", "blissy", "yeti", "thera", "kendra", "stanley", "boseqc", "laneige"], 100)
pin("bf-d", "CYBER MONDAY", "Cyber Monday gifts *worth it*", "last call on the good stuff", ["ugg", "kendra", "thera", "blissy"], 104, True)
pin("surv-a", "HOLIDAY SURVIVAL KIT", "Cozy things to get you *through December*", "blanket, silk + a big tumbler", ["bdthrow", "blissy", "stanley", "bdsocks"], 96)

# Reels (5 frames each)
R1 = "src/dec2/gifts.jpg"
out += [
 {"name": "rbf-1", "type": "reel", "img": R1, "eyebrow": "BLACK FRIDAY RULE", "text": "Only buy it on sale if you'd pay *full price* for it."},
 {"name": "rbf-2", "type": "reel", "img": R1, "dim": .6, "eyebrow": "PASSED THE TEST", "text": "Worth it:", "items": ["The Barefoot Dreams throw"]},
 {"name": "rbf-3", "type": "reel", "img": R1, "dim": .6, "eyebrow": "PASSED THE TEST", "text": "Worth it:", "items": ["The Barefoot Dreams throw", "A Blissy silk pillowcase"]},
 {"name": "rbf-4", "type": "reel", "img": R1, "dim": .6, "eyebrow": "PASSED THE TEST", "text": "Worth it:", "items": ["The Barefoot Dreams throw", "A Blissy silk pillowcase", "The Stanley", "A Theragun"]},
 {"name": "rbf-5", "type": "reel", "img": R1, "dim": .62, "ad": True, "text": "Everything else can *wait.*", "sub": "28 deals I'd actually buy", "pill": "Link in bio"},
]
R2 = "src/dec2/spoil.jpg"
out += [
 {"name": "rsg-1", "type": "reel", "img": R2, "eyebrow": "BLACK FRIDAY, HONESTLY", "text": "Went in for *one* gift for my sister."},
 {"name": "rsg-2", "type": "reel", "img": R2, "dim": .6, "eyebrow": "BLACK FRIDAY, HONESTLY", "text": "Somehow I bought:", "items": ["The blanket (for me)"]},
 {"name": "rsg-3", "type": "reel", "img": R2, "dim": .6, "eyebrow": "BLACK FRIDAY, HONESTLY", "text": "Somehow I bought:", "items": ["The blanket (for me)", "The slippers (also me)"]},
 {"name": "rsg-4", "type": "reel", "img": R2, "dim": .6, "eyebrow": "BLACK FRIDAY, HONESTLY", "text": "Somehow I bought:", "items": ["The blanket (for me)", "The slippers (also me)", "Silk pillowcase (me)", "Her gift (forgot)"]},
 {"name": "rsg-5", "type": "reel", "img": R2, "dim": .62, "ad": True, "text": "Self-gifting is *self-care.*", "size": 96, "sub": "the deals I caved on", "pill": "Link in bio"},
]

# Stories
def story(name, eb, title, img, note, cta="link in bio"):
    out.append({"name": name, "type": "story", "eyebrow": eb, "title": title, "img": img, "cta": cta, "note": note})
story("st-tue-pm", "COLD GIRL STARTER PACK", "Always *freezing?*", P["bdthrow"], "28 cozy gifts for her")
story("st-wed-am", "BLACK FRIDAY CAME EARLY", "Deals worth *it*", P["stanley"], "new post at 4 ✨")
story("st-wed-pm", "BEFORE TOMORROW'S CHAOS", "Gifts for *him*, sorted", P["beanie"], "he'll actually use these")
story("st-thu-pm", "BLACK FRIDAY STARTS NOW", "Leftovers + *deals*", P["thera"], "my deal sheet is up")
story("st-fri-4", "THE SPLURGE EDIT", "Wait for the *sale*", P["boseqc"], "big gifts worth it")
story("st-fri-9", "STILL SHOPPING?", "Same. *Same.*", P["ugg"], "everything's in one place")

# Friday 4pm carousel: big gifts worth buying on sale
I = {"thera": ("src/bf/thera_w.jpg", "cover"), "boseqc": ("src/brand/bose.png", "contain"), "ugg": ("src/brand/ugg.png", "contain"),
     "bdthrow": ("src/bf/barefoot.jpg", "cover"), "kendra": ("src/dec3/kendra.jpg", "contain")}
out.append({"name": "spl-1", "type": "cover", "eyebrow": "BLACK FRIDAY", "title": "Wait for the *sale*", "sub": "…the splurges worth it.", "size": 132,
            "imgs": [I[k][0] for k in ["thera", "boseqc", "ugg", "bdthrow"]], "fit": "contain"})
for n, (k, eb, label, line) in enumerate([
    ("thera", "THERAGUN", "The massager", "For whoever carried *every* bag in."),
    ("boseqc", "BOSE QUIETCOMFORT HEADPHONES", "The headphones", "Peace and quiet, *finally affordable.*"),
    ("ugg", "UGG TASMAN SLIPPERS", "The slippers", "If they dip, *grab them.*"),
    ("bdthrow", "BAREFOOT DREAMS COZYCHIC THROW", "The blanket", "The one you've been *waiting on.*"),
    ("kendra", "KENDRA SCOTT ELISA NECKLACE", "The necklace", "She'll wear it *every single day.*")], 1):
    img, fit = I[k]
    out.append({"name": f"spl-{n+1}", "type": "product", "n": n, "img": img, "fit": fit, "eyebrow": eb, "label": label, "line": line})
out.append({"name": "spl-7", "type": "cta", "title": "Shop the splurges",
            "items": ["Tap the link in my bio", "Check the price first", "Not on sale? Wait for Monday"],
            "sub": "Prices change fast, so check before you buy."})
json.dump(out, open("specs/bfweek.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(len(out))
