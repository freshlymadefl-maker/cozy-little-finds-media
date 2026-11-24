import json
H=lambda n,img,eb,t,sub,size=106,subtop=420,pos="center center":{"name":n,"type":"hook","img":img,"eyebrow":eb,"title":t,"sub":sub,"size":size,"subtop":subtop,"pos":pos}
E=lambda n,eb,t,line,items,start=1:{"name":n,"type":"edit","eyebrow":eb,"title":t,"line":line,"items":items,"start":start}
C=lambda n,kw,cnt,third,sub="Prices and deals at time of posting. Check before you buy.":{"name":n,"type":"cta","title":f"Comment {kw}","items":[f"I'll DM you all {cnt} links","Or tap the link in bio",third],"sub":sub}
g=[]
g+= [H("t-1","src/dec2/teacher.jpg","TEACHER + COWORKER GIFTS","Gifts they'll *actually* use","…not another mug."),
 E("t-2","THE SIPS","Fill their *cup*","Caffeine is a love language.",["Teacher tumbler","YETI Rambler","Tea sampler","Coffee sampler","Hot cocoa bombs","Chocolate gift basket","Snack box"]),
 E("t-3","THE PAMPER","A little *self-care*","They deserve it. Truly.",["Goat milk hand cream","Burt's Bees lip set","Bath bomb set","Fuzzy socks","Rechargeable hand warmer"],8),
 E("t-4","THE DESK GLOW","Make the desk *cozy*","Fluorescent lights, who?",["Teacher candle","Candle gift set","Faux succulents","Ceramic plant pots"],13),
 E("t-5","THE DESK","The *pretty* basics","Stationery, but make it nice.",["Gold luxury pen","Pretty notebook","Clear sticky notes","Desk organizer","Corduroy tote"],17),
 C("t-6","TEACHER",21,"Send this to the room parent")]
g+= [H("h-1","src/dec2/him.jpg","GIFTS FOR HIM","He said he doesn't *need* anything","…he's getting these.",100,440),
 E("h-2","THE EVERYDAY","Stuff he'll use *daily*","Practical is romantic.",["RFID leather wallet","Apple AirTag 4-pack","Anker power bank","Leatherman multitool","Car trash can","YETI Rambler"]),
 E("h-3","THE COZY","Make him *warm*","Flannel season is here.",["Carhartt beanie","Bluetooth beanie","Memory foam slippers","Plush robe","Merino wool socks","Flannel shirt","Quarter-zip fleece"],7),
 E("h-4","THE GRILL + BAR","For the *grill guy*","You know the one.",["Grill tool set","Meat thermometer","Hot sauce gift set","Whiskey rocks glasses"],14),
 E("h-5","THE EXTRAS","A few *nice* things","He'll pretend he isn't thrilled.",["Beard grooming kit","Nautica Voyage cologne","Leather journal","Echo Dot"],18),
 C("h-6","GENT",21,"Send this to his person")]
g+= [H("p-1","src/dec2/pjs.jpg","THE PAJAMA EDIT","Matching pajamas are *mandatory*","…the dog too.",104,430),
 E("p-2","THE MATCHING SET","Photos at *7am sharp*","Everyone matches. No exceptions.",["Family matching pajamas","Kids' Christmas pajamas","Baby Christmas pajamas","Couples plaid set","Dog Christmas pajamas"]),
 E("p-3","FOR HER","Soft, *softer*, softest","Lounging is a lifestyle.",["Plaid flannel set","Satin pajama set","Fleece pajama set","Knit lounge set","Waffle knit robe","Cozy cardigan","Sherpa zip hoodie"],6),
 E("p-4","FOR HIM + THE KIDS","Everyone gets *cozy*","Even the ones who complain.",["Flannel pajama pants","Plush robe","Moccasin slippers","Kids' animal slippers"],13),
 E("p-5","THE EXTRAS","Finish the *look*","Slippers and throws, obviously.",["UGG slippers","Fuzzy slipper socks","Christmas socks","Silk sleep mask","Fleece throw","Sherpa throw"],17),
 C("p-6","PJS",22,"Send this to the family chat")]
g+= [H("w-1","src/dec2/wrap.jpg","THE WRAPPING EDIT","Gifts that look *boutique-wrapped*","…for a lot less.",100,440),
 E("w-2","THE PAPER","Start with *kraft*","Simple paper, big impact.",["Kraft paper roll","Red plaid paper","Christmas tissue paper","Kraft gift bags","Magnetic gift boxes"]),
 E("w-3","THE RIBBON","Velvet does the *work*","Ribbon is the whole look.",["Red velvet ribbon","Ivory satin ribbon","Jute twine","EZ Bow Maker","Kraft gift tags"],6),
 E("w-4","THE DETAILS","The *boutique* touches","This is where the magic is.",["Wax seal kit","Gold embossed seals","Gold paint pens","Dried orange slices","Cinnamon sticks","Christmas gift tags"],11),
 E("w-5","THE TOOLS","Wrap *faster*","Less tape drama.",["Tape dispenser","Wrapping paper cutter","Fiskars scissors","Wrap organizer","Under-bed storage"],17),
 C("w-6","WRAP",21,"Save this for wrapping night")]
g+= [H("f-1","src/dec2/fast.jpg","LAST-MINUTE GIFTS","Forgot someone? *Same.*","…these ship fast.",112,400),
 E("f-2","FOR HER","The *sure* things","She'll think you planned ahead.",["UGG Tasman slippers","Laneige lip mask","Sol de Janeiro mist","Kendra Scott necklace","Blissy pillowcase","Barefoot Dreams throw","Revlon One-Step"]),
 E("f-3","THE TECH","Plug in, *wow*","The ones everyone asks for.",["Kindle Paperwhite","AirPods Pro 3","Bose QuietComfort","Instax Mini 12","Apple Watch band"],8),
 E("f-4","THE BIG ONES","Go *big*","When it has to be impressive.",["Shark FlexStyle","Theragun mini","Nespresso Vertuo pods","Ninja Creami"],13),
 E("f-5","THE EASY WINS","Can't *miss*","Everyone uses these.",["Stanley Quencher","Owala FreeSip","YETI Rambler","LEGO flower bouquet"],17),
 C("f-6","RUSH",20,"Check delivery dates at checkout","Prices at time of posting. Delivery dates vary, so check before you buy.")]
g+= [H("d-1","src/dec2/dog.jpg","GIFTS FOR THE DOG MOM","The dog gets a *stocking* too","…obviously.",104,430),
 E("d-2","FOR THE DOG","Good boy *gifts*","Toys they won't destroy by noon.",["KONG Classic","Benebone wishbone","No-stuffing squeaky toys","Puzzle toy","Snuffle mat","Lick mat","Calming dog bed"]),
 E("d-3","THE CHRISTMAS CARD","Dressed for the *photo*","Bribery treats not included.",["Christmas sweater","Christmas pajamas","Christmas bandanas","Burlap stockings"],8),
 E("d-4","FOR THE DOG MOM","Dog mom *essentials*","Life, but easier.",["Dog mom sweatshirt","Furbo pet camera","ChomChom hair roller","Ceramic treat jar","AirTag collar holder","Car seat cover"],12),
 E("d-5","THE GROOMING","Spa day, *for them*","Muddy paws, be gone.",["MudBuster paw cleaner","Oatmeal shampoo","Quiet nail grinder","Travel water bottle"],18),
 C("d-6","WOOF",21,"Send this to a dog mom")]
json.dump(g,open('specs/dec2-guides.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)

R=[]
def reel(code,img,eb1,t1,mid_t,items,end_t,end_sub,kw):
    R.append({"name":f"{code}-1","type":"reel","img":img,"eyebrow":eb1,"text":t1})
    for i,k in enumerate([1,2,4]):
        R.append({"name":f"{code}-{i+2}","type":"reel","img":img,"dim":0.6,"eyebrow":eb1,"text":mid_t,"items":items[:k]})
    R.append({"name":f"{code}-5","type":"reel","img":img,"dim":0.62,"ad":True,"text":end_t,"sub":end_sub,"pill":f"Comment {kw}"})
reel("rm","src/dec/mom.jpg","GIFTS FOR MOM","Mom: \"I don't want *anything.*\"","Also mom, opening:",["Aura photo frame","Heated eye mask","Plush robe","Mom's Story journal"],"She *cried.* (Happy tears.)","22 gifts for mom on Amazon","MOM")
reel("rv","src/dec2/spoil.jpg","SHE HAS EVERYTHING","What do you get the girl who has *everything?*","Things she'd never buy herself:",["Blissy silk pillowcase","Barefoot Dreams throw","Kendra Scott necklace","Laneige lip mask"],"*Spoiled.*","22 gifts for her on Amazon","SPOIL")
reel("rn","src/dec/morn.jpg","CHRISTMAS MORNING","The real gift is *coffee* at 6am","The morning lineup:",["Matching pajamas","Milk frother","Belgian waffle maker","Champagne flutes"],"Merry *everything.*","21 Christmas morning finds","MORNING")
reel("rk","src/dec2/stocking.jpg","STOCKING STUFFERS","The stocking is the *best* part. Don't argue.","Hers, this year:",["Fuzzy socks","Claw clip","Silk scrunchies","Hand cream"],"Little things, *big* love.","26 stocking stuffers on Amazon","STOCKING")
reel("ru","src/dec2/whiskey.jpg","FOR THE HUSBAND","Him: \"Don't get me *anything.*\"","Me, adding to cart:",["Shearling slippers","Whiskey glass + ice sphere","Leather wallet","Cozy quarter-zip"],"He *loved* it.","28 gifts for him on Amazon","HUSBAND")
reel("ry","src/dec2/cocoa.jpg","HOLIDAY SURVIVAL KIT","One week left. *Deep breaths.*","Survival kit:",["Barefoot Dreams throw","Blissy pillowcase","Voluspa candle","Theragun"],"You've *got* this.","22 holiday survival finds","HOLIDAY")
reel("rl","src/dec2/gifts.jpg","GIFTS UNDER $25","Gifts that look *expensive*","Nobody has to know:",["Laneige lip mask","Sol de Janeiro mist","Satin pillowcase","Claw clips"],"Looks *luxe.*","25 gifts under $25 on Amazon","LUXE")
json.dump(R,open('specs/dec2-reels.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)

V=[{"name":"wrap-cheat","type":"numbers","eyebrow":"SAVE THIS FOR WRAPPING NIGHT","title":"Gift wrapping *cheat sheet*","listtop":370,"rows":[
 {"name":"The *length* rule","num":"Around once + 2 in","note":"Wrap it around the box, then add 2 inches of overlap"},
 {"name":"The *ends* rule","num":"Box height + 1 in","note":"Paper past each end, just over the box's height"},
 {"name":"The *tape* rule","num":"Double-sided","note":"Tape under the seams, so none shows"},
 {"name":"The *ribbon* rule","num":"4 sides + 20 in","note":"Go around both ways, plus extra for the bow"}],"foot":"@cozylittlefindsdaily · comment WRAP for my wrapping list"},
 {"name":"eve-timeline","type":"numbers","eyebrow":"SAVE THIS FOR CHRISTMAS EVE","title":"The hosting *countdown*","listtop":370,"rows":[
 {"name":"3 days *out*","num":"Shop + set","note":"Set the table, iron napkins, buy extra ice"},
 {"name":"1 day *out*","num":"Prep + chill","note":"Make the dips, chill the bubbly, pick the playlist"},
 {"name":"3 hours *out*","num":"Candles + coupes","note":"Set out glasses, light candles, start the oven"},
 {"name":"30 minutes *out*","num":"Sit down.","note":"Pour yourself one first. You earned it."}],"foot":"@cozylittlefindsdaily · comment HOSTING for my hosting list"},
 {"name":"movies-1","type":"edit","eyebrow":"THE CHRISTMAS MOVIE COUNTDOWN","title":"One movie a *night*","line":"Dec 13 to 24. Pajamas required.","ad":False,"items":["White Christmas","Miracle on 34th Street","The Polar Express","Elf","The Holiday","Klaus"],"start":13},
 {"name":"movies-2","type":"edit","eyebrow":"THE CHRISTMAS MOVIE COUNTDOWN","title":"The *home stretch*","line":"Saving the best for Christmas Eve.","ad":False,"items":["Home Alone","The Grinch","Christmas Vacation","Love Actually","It's a Wonderful Life","Muppet Christmas Carol"],"start":19}]
J=[("j-1208","My love language is someone *else* wrapping the presents.",False),
 ("j-1209","Me: I'm on a budget this year. Also me: *it's for the stockings.*",True),
 ("j-1210","Pretending the Elf on the Shelf moved itself. *Again.*",False),
 ("j-1213","Christmas cookies count as a food group in December. *I checked.*",True),
 ("j-1215","Every year I say I'll start shopping in October. *Every year.*",False),
 ("j-1216","Currently hiding presents in places *I will absolutely forget.*",True),
 ("j-1217","Me at the gift exchange, pretending I didn't want *the waffle maker.*",False),
 ("j-1219","Last-minute shopping is a sport and I am *an athlete.*",True),
 ("j-1220","Officially out of tape. *Merry Christmas.*",False)]
for n,t,d in J: V.append({"name":n,"type":"plain","text":t,"dark":d,"size":84})
json.dump(V,open('specs/dec2-extras.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
