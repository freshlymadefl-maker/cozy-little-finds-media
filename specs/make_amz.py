"""Amazon storefront versions of the guide covers: product grids only, no SWIPE (owner: storefront images must show products)."""
import json
v2 = {s["name"]: s for s in json.load(open("specs/v2-guides.json", encoding="utf-8"))}
out = []
for code in ["v-mom", "v-morn", "v-teach", "v-him", "v-rush"]:
    s = dict(v2[code + "-1"]); s["name"] = "amz-" + code[2:]; s["swipe"] = False; out.append(s)
P = {"kong": "src/dec3/kong.jpg", "benebone": "src/dec3/benebone.jpg", "bdthrow": "src/bf/barefoot.jpg", "stanley": "src/bf/stanley_w.jpg",
     "yankee": "src/dec3/yankee.jpg", "bdsocks": "src/bfd/BDWCC27064_STONE_MULTI_FRONT.jpg", "ugg": "src/brand/ugg.png", "blissy": "src/bf/blissy_w.jpg",
     "dash": "src/dec3/dash.jpg", "yeti": "src/him/yeti.png", "jbl": "src/brand/jbl.png"}
def c(name, keys, eb, title, sub, size):
    out.append({"name": name, "type": "cover", "fit": "contain", "swipe": False, "imgs": [P[k] for k in keys], "eyebrow": eb, "title": title, "sub": sub, "size": size})
c("amz-dog", ["kong", "benebone", "bdthrow", "stanley"], "GIFTS FOR THE DOG MOM", "The dog gets a *stocking*", "…obviously.", 112)
c("amz-cozy", ["yankee", "bdthrow", "bdsocks", "ugg"], "THE COZY NIGHT IN EDIT", "My idea of a *wild night*", "…is staying in.", 112)
c("amz-swap", ["dash", "stanley", "yeti", "jbl"], "GIFT EXCHANGE EDIT", "Gifts people *steal*", "…bring one of these.", 128)
c("amz-pjs", ["ugg", "bdsocks", "blissy", "bdthrow"], "THE PAJAMA EDIT", "PJs are *mandatory*", "…the dog too.", 128)
json.dump(out, open("specs/amz-covers.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(len(out))
