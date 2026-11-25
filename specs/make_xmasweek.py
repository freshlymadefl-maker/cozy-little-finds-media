"""Christmas week Dec 21-27 2026 (post-holiday-plan cadence): 1 product + 1 fun post a day, 2 Stories a day, 2 Reels."""
import json, pathlib
P1, P2 = "src/xw/gifts.png", "src/xw/after.png"
feed = [
 {"name":"xw-1221-giftrules","type":"edit","eyebrow":"4 DAYS TO GO","title":"Last-minute *gift rules*","line":"for the one still on your list","items":["Check “arrives by” first","One nice thing beats three okay things","Mini luxe sets look *planned*","Wrap it like you meant it"]},
 {"name":"xw-1221-tote","type":"tweet","text":"me on december 21st: i'm done shopping\n\nme on december 22nd: holding a tote bag of “one more little thing” for every person i've ever met"},
 {"name":"xw-1222-stocking","type":"edit","eyebrow":"STOCKING EMERGENCY","title":"Her stocking is *still empty*","line":"and it's the 22nd. the plan:","items":["Something for her lips","Something for her hair","Something cozy for her feet","One tiny luxury she'd *never* buy herself"]},
 {"name":"xw-1222-bed","type":"plain","eyebrow":"A HOLIDAY TRUTH","text":"Christmas is a state of mind. So is being *in bed by nine.*","size":92},
 {"name":"xw-1223-morning","type":"edit","eyebrow":"CHRISTMAS MORNING","title":"The cold girl *dress code*","line":"for the coziest morning of the year","items":["Pajamas, obviously","The fuzzy socks","A blanket for the couch","Coffee in your *nicest* mug"]},
 {"name":"xw-1223-tape","type":"tweet","text":"december 23rd is when everyone in the house wraps presents in a different room and pretends they can't hear each other's tape"},
 {"name":"xw-1224-martini","type":"edit","eyebrow":"CHRISTMAS EVE","title":"Martini *hour*","line":"the only plan you need tonight","items":["Coupes in the freezer, 20 minutes","Olives on a pretty pick","The candle you've been saving","One record, on repeat"]},
 {"name":"xw-1224-dishes","type":"plain","dark":True,"eyebrow":"MERRY CHRISTMAS EVE","text":"Pour something nice. *Leave the dishes.*","size":104},
 {"name":"xw-1225-merry","type":"plain","eyebrow":"DECEMBER 25","text":"Merry Christmas from our cozy little corner to *yours.*","size":96},
 {"name":"xw-1225-giftcard","type":"edit","eyebrow":"GOT A GIFT CARD?","title":"Spend it like *this*","line":"pieces under $25 that look expensive","items":["Skip the “useful” thing","Buy what you keep un-carting","Go for one that looks *pricey*","Screenshot this for later"]},
 {"name":"xw-1226-pjs","type":"tweet","text":"december 26th: i have officially switched from “festive” to “wearing the new pajamas until further notice”"},
 {"name":"xw-1226-pearls","type":"edit","eyebrow":"NEW YEAR'S EVE IN 5 DAYS","title":"Plaid, pearls + *one bow*","line":"the outfit that works from now to midnight","items":["A plaid piece you'll rewear","Pearls (more than you think)","One bow, somewhere","Shoes you can actually *dance in*"]},
 {"name":"xw-1227-softlaunch","type":"plain","eyebrow":"THE WEEK BETWEEN","text":"The days after Christmas are a *soft launch* for January.","size":96},
 {"name":"xw-1227-offline","type":"edit","eyebrow":"PHONES IN A BASKET","title":"The great *offline* week","line":"family gifts that get everyone off their phones","items":["A puzzle on the coffee table","A game that ends in yelling (lovingly)","The book someone gave you","Phones away till nine"]},
]
stories = [
 ("1221a","4 DAYS TO GO","Still *shopping?*",P1,"today's list at noon","we've got you."),
 ("1221b","NEW POST","Gifts she'll *actually* use",P1,"comment TRENDLIST","or tap the link in my bio"),
 ("1222a","3 DAYS TO GO","Stocking *check*",P1,"see today's post","no judgment. we're behind too."),
 ("1222b","NEW POST","Stocking stuffers for *her*",P1,"comment STOCKING","or tap the link in my bio"),
 ("1223a","2 DAYS TO GO","Wrap night *energy*",P1,"tape, ribbon, wine","in that order."),
 ("1223b","NEW POST","The cold girl *dress code*",P1,"comment COLD","or tap the link in my bio"),
 ("1224a","CHRISTMAS EVE","Martini *hour*",P1,"link in bio","the bar cart list is up."),
 ("1224b","TONIGHT","Leave the *dishes*",P1,"merry christmas eve","see you in the morning."),
 ("1225a","DECEMBER 25","Merry *Christmas*",P2,"from us to you","thank you for being here."),
 ("1225b","GOT A GIFT CARD?","Spend it *beautifully*",P2,"comment GIFTS","under-$25 pieces that look expensive"),
 ("1226a","NEW YEAR'S IN 5 DAYS","Pearls *on*",P2,"comment PEARLS","or tap the link in my bio"),
 ("1226b","DECEMBER 26","Pajama day *two*",P2,"no notes","stay cozy."),
 ("1227a","THE WEEK BETWEEN","Phones *down*",P2,"comment UNPLUG","family gifts to unplug"),
 ("1227b","SUNDAY","Puzzle on the *table*",P2,"link in bio","the slowest, best week."),
]
st = [{"name":f"xw-st-{n}","type":"story","eyebrow":e,"title":t,"cta":c,"note":no} for n,e,t,i,c,no in stories]

# Gap fill: Dec 8-20 had almost no Stories. One per day promoting that day's product post.
gap = [(8,"TEACHER","Teacher gifts they'll *use*"),(9,"MOM","For the mom who wants *nothing*"),(10,"GENT","He said he needs *nothing*"),
 (11,"SPOIL","The girl who has *everything*"),(12,"PJS","Matching pajamas, *mandatory*"),(13,"MORNING","Christmas morning, *cozy*"),
 (14,"WRAP","Boutique wrap, *for less*"),(15,"STOCKING","The stocking is the *best part*"),(16,"RUSH","Forgot someone? *Same.*"),
 (17,"HUSBAND","For him who wants *nothing*"),(18,"WOOF","The dog gets a *stocking*"),(19,"HOLIDAY","One week left. *Breathe.*"),
 (20,"LUXE","Looks expensive. *Isn't.*")]
st += [{"name":f"xw-gap-{d}","type":"story","eyebrow":f"{25-d} DAYS TO CHRISTMAS","title":t,"cta":f"comment {k}","note":"or tap the link in my bio"} for d,k,t in gap]
reels = [
 {"name":"xw-reel-rule","type":"reel","img":P1,"eyebrow":"MY LAST-MINUTE GIFT RULE","text":"If it arrives after the 24th, it's a *New Year's gift* now.","size":104,"top":560,"dim":.42},
 {"name":"xw-reel-card","type":"reel","img":P2,"eyebrow":"MY GIFT CARD RULE","text":"Spend it on the thing you'd *never buy yourself.*","size":104,"top":560,"dim":.42},
]
pathlib.Path(__file__).with_name("xmasweek.json").write_text(json.dumps(feed+st+reels, indent=1), encoding="utf-8")
