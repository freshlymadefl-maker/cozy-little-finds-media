"""Pinterest pins (2:3) for each gift guide: keyword title + product grid."""
import json
P = {"kong": "src/dec3/kong.jpg", "benebone": "src/dec3/benebone.jpg", "bdthrow": "src/bf/barefoot.jpg", "stanley": "src/bf/stanley_w.jpg",
 "yankee": "src/dec3/yankee.jpg", "bdsocks": "src/bfd/BDWCC27064_STONE_MULTI_FRONT.jpg", "ugg": "src/brand/ugg.png", "blissy": "src/bf/blissy_w.jpg",
 "dash": "src/dec3/dash.jpg", "yeti": "src/him/yeti.png", "jbl": "src/brand/jbl.png", "kendra": "src/dec3/kendra.jpg", "boseflex": "src/dec3/bose_flex.jpg",
 "tiesta": "src/dec3/tiesta.png", "laneige": "src/u25/laneige.jpg", "airtag": "src/him/airtag.jpg", "beanie": "src/him/beanie.jpg", "leatherman": "src/him/leatherman.jpg",
 "boseqc": "src/brand/bose.png", "thera": "src/bf/thera_w.jpg", "sdj": "src/u25/sdj.jpg", "ribbon": "src/dec3/ribbon.jpg", "kraft": "src/dec3/kraft.jpg",
 "oranges": "src/dec3/oranges.jpg", "ribbons2": "src/dec3/ribbons2.jpg", "candle": "src/u25/candle.jpg", "claw": "src/u25/claw.jpg", "pillow": "src/u25/pillow.jpg"}
out = []
def pin(name, eb, title, sub, keys, size=112):
    out.append({"name": "pin-" + name, "type": "pin", "eyebrow": eb, "title": title, "sub": sub, "imgs": [P[k] for k in keys], "size": size})
pin("mom", "GIFT GUIDE", "Gifts for the mom who has *everything*", "…she'll actually use these.", ["kendra", "boseflex", "bdthrow", "blissy"], 100)
pin("morn", "CHRISTMAS MORNING", "Cozy Christmas *morning* gifts", "slippers, socks + silk", ["yankee", "ugg", "bdsocks", "blissy"])
pin("teach", "GIFT GUIDE", "Teacher gifts they'll *actually* use", "…not another mug.", ["yeti", "tiesta", "laneige", "stanley"], 104)
pin("him", "GIFT GUIDE", "Gifts for the man who wants *nothing*", "he'll use these every day", ["airtag", "beanie", "leatherman", "yeti"], 100)
pin("rush", "LAST-MINUTE GIFTS", "Last-minute gifts that *ship fast*", "everyone actually wants these", ["ugg", "laneige", "boseqc", "thera", "stanley", "kendra", "sdj", "blissy", "bdthrow"], 104)
pin("dog", "GIFT GUIDE", "Gifts for the *dog mom*", "(and the dog)", ["kong", "benebone", "bdthrow", "stanley"], 120)
pin("cozy", "COZY NIGHT IN", "Cozy gifts for a night *in*", "blankets, candles + socks", ["yankee", "bdthrow", "bdsocks", "ugg"], 112)
pin("swap", "WHITE ELEPHANT", "White elephant gifts people *steal*", "gift exchange ideas", ["dash", "stanley", "yeti", "jbl"], 104)
pin("pjs", "CHRISTMAS EVE", "Christmas Eve *box* ideas", "cozy layers for the whole family", ["ugg", "bdsocks", "blissy", "bdthrow"], 112)
pin("wrap", "GIFT WRAPPING", "Pretty gift wrapping *ideas*", "kraft paper, velvet ribbon + oranges", ["ribbon", "kraft", "oranges", "ribbons2"], 112)
pin("u25", "UNDER $25", "Gifts under $25 that look *expensive*", "stocking stuffers + small gifts", ["laneige", "sdj", "candle", "claw"], 100)
json.dump(out, open("specs/pins.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
