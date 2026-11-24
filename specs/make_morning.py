"""Daily 7:30am 'Morning find' series (owner, Nov 24 2026: a post every early morning)."""
import json
I = {
 "bdthrow": ("src/bf/barefoot.jpg", "cover"), "bdsocks": ("src/bfd/BDWCC27064_STONE_MULTI_FRONT.jpg", "cover"),
 "ugg": ("src/brand/ugg.png", "contain"), "blissy": ("src/bf/blissy_w.jpg", "cover"), "stanley": ("src/bf/stanley_w.jpg", "cover"),
 "thera": ("src/bf/thera_w.jpg", "cover"), "boseqc": ("src/brand/bose.png", "contain"), "laneige": ("src/u25/laneige.jpg", "cover"),
 "sdj": ("src/u25/sdj.jpg", "cover"), "kendra": ("src/dec3/kendra.jpg", "contain"), "boseflex": ("src/dec3/bose_flex.jpg", "cover"),
 "yankee": ("src/dec3/yankee.jpg", "contain"), "dash": ("src/dec3/dash.jpg", "contain"), "jellycat": ("src/dec3/jellycat.jpg", "contain"),
 "tiesta": ("src/dec3/tiesta.png", "contain"), "kong": ("src/dec3/kong.jpg", "contain"), "airtag": ("src/him/airtag.jpg", "contain"),
 "beanie": ("src/him/beanie.jpg", "contain"), "leatherman": ("src/him/leatherman.jpg", "contain"), "ribbon": ("src/dec3/ribbon.jpg", "cover"),
 "claw": ("src/u25/claw.jpg", "cover"), "pillow": ("src/u25/pillow.jpg", "cover"), "candle": ("src/u25/candle.jpg", "cover"),
}
L = {"COZY": "1NS08WQTADRJK", "SWAP": "WDTTRUUMBWB6", "MOM": "1C1D9BF3HX86P", "GENT": "38CPJYTLJ13GH", "MORNING": "P6V8V2VG6HIH",
     "TEACHER": "RY4NCYOFPW3L", "U25": "28EFTLVOUQR5C", "RUSH": "27GZT4NVS9HUG", "WOOF": "3B8R1HJU8LGPS", "WRAP": "2YYODQJGDA89R"}
# date, key, brand/product name, label, witty line (render), list
D = [
 ("2026-11-24T11:00", "laneige", "LANEIGE", "The lip mask", "On every nightstand *for a reason.*", "U25"),
 ("2026-11-29T07:30", "blissy", "BLISSY", "The pillowcase", "Sunday morning, *but make it silk.*", "MOM"),
 ("2026-11-30T07:30", "thera", "THERAGUN", "The massager", "Cyber Monday *self-care.*", "RUSH"),
 ("2026-12-01T07:30", "bdsocks", "BAREFOOT DREAMS", "The socks", "Cold floors, *who?*", "COZY"),
 ("2026-12-02T07:30", "dash", "DASH", "The waffle maker", "Breakfast, *but cuter.*", "SWAP"),
 ("2026-12-03T07:30", "kendra", "KENDRA SCOTT", "The necklace", "She'll wear it *every single day.*", "MOM"),
 ("2026-12-04T07:30", "boseflex", "BOSE", "The speaker", "Kitchen dance party, *7am edition.*", "MOM"),
 ("2026-12-05T07:30", "jellycat", "JELLYCAT", "The bunny", "Grown adults *will* fight for it.", "SWAP"),
 ("2026-12-06T07:30", "airtag", "APPLE", "The AirTag", "For the keys he *always* loses.", "GENT"),
 ("2026-12-07T07:30", "ugg", "UGG", "The slippers", "Coffee run? *In these.*", "MORNING"),
 ("2026-12-08T07:30", "tiesta", "TIESTA TEA", "The tea", "Eight flavors of *peace and quiet.*", "TEACHER"),
 ("2026-12-09T07:30", "bdthrow", "BAREFOOT DREAMS", "The blanket", "Five more minutes. *Ten, tops.*", "MOM"),
 ("2026-12-10T07:30", "leatherman", "LEATHERMAN", "The multitool", "Fixes everything. *Allegedly.*", "GENT"),
 ("2026-12-11T07:30", "sdj", "SOL DE JANEIRO", "The mist", "Smells like a vacation *you didn't take.*", "U25"),
 ("2026-12-12T07:30", "yankee", "YANKEE CANDLE", "The candle", "Instant \"I *totally* cleaned.\"", "MORNING"),
 ("2026-12-13T07:30", "claw", "KITSCH", "The claw clip", "The *entire* Sunday hairstyle.", "U25"),
 ("2026-12-14T07:30", "ribbon", "VELVET RIBBON", "The ribbon", "Velvet does *all* the work.", "WRAP"),
 ("2026-12-15T07:30", "pillow", "KITSCH", "The pillowcase", "Stocking-sized *beauty sleep.*", "U25"),
 ("2026-12-16T07:30", "boseqc", "BOSE", "The headphones", "Peace and quiet, *gift-wrapped.*", "RUSH"),
 ("2026-12-17T07:30", "beanie", "CARHARTT", "The beanie", "He'll wear it *every single day.*", "GENT"),
 ("2026-12-18T07:30", "kong", "KONG", "The KONG", "Peanut butter = *peace.*", "WOOF"),
 ("2026-12-19T07:30", "stanley", "STANLEY", "The tumbler", "Still *the* tumbler.", "RUSH"),
 ("2026-12-20T07:30", "candle", "VOLUSPA", "The candle", "Makes any bathroom *a hotel.*", "U25"),
]
out, meta = [], []
for n, (dt, k, eb, label, line, lst) in enumerate(D, 1):
    img, fit = I[k]
    name = f"mf-{dt[5:10]}"
    out.append({"name": name, "type": "product", "n": "☕", "img": img, "fit": fit, "eyebrow": "MORNING FIND · " + eb, "label": label, "line": line})
    meta.append({"name": name, "date": dt, "brand": eb.title(), "label": label, "line": line.replace("*", ""), "list": L[lst]})
json.dump(out, open("specs/morning.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
json.dump(meta, open("specs/morning-meta.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(len(out))
