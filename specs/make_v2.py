"""Product-photo rebuild of the 10 December guides (owner: no list slides; rotate cover styles)."""
import json
I = {
 "bdthrow": ("src/bf/barefoot.jpg", "cover"), "bdsocks": ("src/bfd/BDWCC27064_STONE_MULTI_FRONT.jpg", "cover"),
 "ugg": ("src/brand/ugg.png", "contain"), "blissy": ("src/bf/blissy_w.jpg", "cover"), "stanley": ("src/bf/stanley_w.jpg", "cover"),
 "thera": ("src/bf/thera_w.jpg", "cover"), "boseqc": ("src/brand/bose.png", "contain"), "laneige": ("src/u25/laneige.jpg", "cover"),
 "sdj": ("src/u25/sdj.jpg", "cover"), "kendra": ("src/dec3/kendra.jpg", "contain"), "boseflex": ("src/dec3/bose_flex.jpg", "cover"),
 "yankee": ("src/dec3/yankee.jpg", "contain"), "dash": ("src/dec3/dash.jpg", "contain"), "jellycat": ("src/dec3/jellycat.jpg", "contain"),
 "yeti": ("src/him/yeti.png", "contain"), "tiesta": ("src/dec3/tiesta.png", "contain"), "kong": ("src/dec3/kong.jpg", "contain"),
 "benebone": ("src/dec3/benebone.jpg", "contain"), "airtag": ("src/him/airtag.jpg", "contain"), "beanie": ("src/him/beanie.jpg", "contain"),
 "leatherman": ("src/him/leatherman.jpg", "contain"), "ribbon": ("src/dec3/ribbon.jpg", "cover"), "kraft": ("src/dec3/kraft.jpg", "cover"),
 "seal": ("src/dec2/gifts.jpg", "cover"), "oranges": ("src/dec3/oranges.jpg", "cover"),
}
out = []
def guide(code, cover, prods, kw, count, third, sub="Prices and deals at time of posting. Check before you buy."):
    if cover:
        cover = dict(cover); cover["name"] = f"{code}-1"
        if cover["type"] in ("cover", "pack"):
            cover["imgs"] = [I[k][0] for k in cover.pop("keys")]
            cover["fit"] = "contain"
        out.append(cover)
    for n, (k, eb, label, line) in enumerate(prods, 1):
        img, fit = I[k]
        out.append({"name": f"{code}-{n+1}", "type": "product", "n": n, "img": img, "fit": fit, "eyebrow": eb, "label": label, "line": line})
    out.append({"name": f"{code}-{len(prods)+2}", "type": "cta", "title": f"Comment {kw}",
                "items": [f"I'll DM you all {count} links", "Or tap the link in bio", third], "sub": sub})

guide("v-cozy", None, [
 ("bdthrow", "BAREFOOT DREAMS COZYCHIC THROW", "The blanket", "The one everyone *fights over.*"),
 ("bdsocks", "BAREFOOT DREAMS COZYCHIC SOCKS", "The socks", "Because someone *always* sets the heat to 64."),
 ("ugg", "UGG TASMAN SLIPPERS", "The slippers", "Errands? *In these?* Absolutely."),
 ("yankee", "YANKEE CANDLE LARGE JAR", "The candle", "Instant \"I *totally* cleaned.\""),
], "COZY", 23, "Save this for tonight")
guide("v-mom", {"type": "cover", "keys": ["kendra", "boseflex", "bdthrow", "blissy"], "eyebrow": "GIFTS FOR MOM", "title": "She wants *nothing*", "sub": "…so get her these.", "size": 132}, [
 ("kendra", "KENDRA SCOTT ELISA NECKLACE", "The necklace", "She'll wear it *every single day.*"),
 ("boseflex", "BOSE SOUNDLINK FLEX", "The speaker", "Kitchen dance parties, *upgraded.*"),
 ("bdthrow", "BAREFOOT DREAMS COZYCHIC THROW", "The blanket", "The softest thing she'll *ever* own."),
 ("blissy", "BLISSY SILK PILLOWCASE", "The pillowcase", "Beauty sleep, *but make it silk.*"),
], "MOM", 24, "Send this to your siblings")
guide("v-swap", None, [
 ("dash", "DASH MINI WAFFLE MAKER", "The waffle maker", "The gift *everyone* steals."),
 ("stanley", "STANLEY QUENCHER", "The tumbler", "Instant *bidding war.*"),
 ("yeti", "YETI RAMBLER 20 OZ", "The other tumbler", "For the *Stanley skeptics.*"),
 ("jellycat", "JELLYCAT BASHFUL BUNNY", "The bunny", "Grown adults will *fight* for it."),
], "SWAP", 23, "Send this to your office")
guide("v-morn", {"type": "cover", "keys": ["yankee", "ugg", "bdsocks", "blissy"], "eyebrow": "CHRISTMAS MORNING", "title": "Christmas *morning*", "sub": "…but make it cozy.", "size": 128}, [
 ("yankee", "YANKEE CANDLE · SUGARED CINNAMON APPLE", "The candle", "Smells like cinnamon rolls, *no baking.*"),
 ("ugg", "UGG TASMAN SLIPPERS", "The slippers", "Cold floors, *who?*"),
 ("bdsocks", "BAREFOOT DREAMS COZYCHIC SOCKS", "The socks", "Stocking-sized, *cloud-soft.*"),
 ("blissy", "BLISSY SILK PILLOWCASE", "The pillowcase", "For sleeping in *after.*"),
], "MORNING", 24, "Save this for Christmas")
guide("v-teach", {"type": "cover", "keys": ["yeti", "tiesta", "laneige", "stanley"], "eyebrow": "TEACHER + COWORKER GIFTS", "title": "Gifts they'll *actually* use", "sub": "…not another mug.", "size": 108}, [
 ("yeti", "YETI RAMBLER 20 OZ", "The tumbler", "Coffee stays hot *through recess.*"),
 ("stanley", "STANLEY QUENCHER", "The big one", "Hydration for *parent-teacher night.*"),
 ("tiesta", "TIESTA TEA TOP SELLER SAMPLER", "The tea", "Eight flavors of *peace and quiet.*"),
 ("laneige", "LANEIGE LIP SLEEPING MASK", "The lip mask", "A little luxury *for the lounge.*"),
], "TEACHER", 23, "Send this to the room parent")
guide("v-him", {"type": "cover", "keys": ["airtag", "beanie", "leatherman", "yeti"], "eyebrow": "GIFTS FOR HIM", "title": "He'll *actually* use these", "sub": "…he said he needs nothing.", "size": 118}, [
 ("beanie", "CARHARTT KNIT CUFFED BEANIE", "The beanie", "He'll wear it *every single day.*"),
 ("leatherman", "LEATHERMAN WINGMAN", "The multitool", "Fixes everything. *Allegedly.*"),
 ("airtag", "APPLE AIRTAG 4-PACK", "The AirTags", "For the keys he *always* loses."),
 ("yeti", "YETI RAMBLER 20 OZ", "The tumbler", "Coffee, *still hot at noon.*"),
], "GENT", 21, "Send this to his person")
guide("v-pjs", None, [
 ("ugg", "UGG TASMAN SLIPPERS", "The slippers", "Matching pajamas *need* matching slippers."),
 ("bdsocks", "BAREFOOT DREAMS COZYCHIC SOCKS", "The socks", "Cozy toes for the *family photo.*"),
 ("blissy", "BLISSY SILK PILLOWCASE", "The pillowcase", "Christmas Eve, *silk edition.*"),
 ("bdthrow", "BAREFOOT DREAMS COZYCHIC THROW", "The blanket", "Movie night is *mandatory.*"),
], "PJS", 25, "Send this to the family chat")
guide("v-wrap", None, [
 ("ribbon", "RED VELVET RIBBON", "The ribbon", "Velvet does *all* the work."),
 ("kraft", "KRAFT PAPER + JUTE TWINE", "The paper", "Plain paper, *boutique* finish."),
 ("seal", "WAX SEAL KIT", "The seal", "The detail everyone *notices.*"),
 ("oranges", "DRIED ORANGE SLICES", "The garnish", "Smells like Christmas, *looks expensive.*"),
], "WRAP", 21, "Save this for wrapping night")
guide("v-rush", {"type": "pack", "keys": ["ugg", "laneige", "boseqc", "thera", "stanley", "kendra", "sdj", "blissy", "bdthrow"], "eyebrow": "LAST-MINUTE GIFTS", "title": "Forgot someone?", "sub": "*Same.* These ship fast.", "size": 118, "subtop": 1070}, [
 ("ugg", "UGG TASMAN SLIPPERS", "The slippers", "The gift *everyone* asked for."),
 ("laneige", "LANEIGE LIP SLEEPING MASK", "The lip mask", "Stocking-sized *cult favorite.*"),
 ("boseqc", "BOSE QUIETCOMFORT HEADPHONES", "The headphones", "Peace and quiet, *gift-wrapped.*"),
 ("thera", "THERAGUN MINI", "The massager", "For *after* all the shopping."),
 ("stanley", "STANLEY QUENCHER", "The tumbler", "Still *the* tumbler."),
], "RUSH", 20, "Check delivery dates at checkout", "Prices at time of posting. Delivery dates vary, so check before you buy.")
guide("v-dog", None, [
 ("kong", "KONG CLASSIC", "The KONG", "Peanut butter = *peace.*"),
 ("benebone", "BENEBONE WISHBONE", "The chew", "Survives *the power chewer.*"),
 ("bdthrow", "BAREFOOT DREAMS COZYCHIC THROW", "The blanket", "For dog-mom *couch naps.*"),
 ("stanley", "STANLEY QUENCHER", "The tumbler", "Walk fuel, *for her.*"),
], "WOOF", 23, "Send this to a dog mom")
json.dump(out, open("specs/v2-guides.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(len(out), "slides")
