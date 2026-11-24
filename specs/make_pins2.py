"""Pinterest designs B (pine, 2x2) and C (cream, 3x3) per guide + new guides."""
import json
exec(open("specs/make_pins.py",encoding="utf-8").read().split("out = []")[0]); P["jellycat"]="src/dec3/jellycat.jpg"
out=[]
def pin(name, eb, title, sub, keys, size=108, dark=False):
    out.append({"name":"pin-"+name,"type":"pin","eyebrow":eb,"title":title,"sub":sub,"imgs":[P[k] for k in keys],"size":size,"dark":dark})
# design B: pine background, 2x2
pin("mom-b","CHRISTMAS 2026","Mom gifts she'll *love*","the ones she won't return",["blissy","kendra","bdthrow","boseflex"],104,True)
pin("him-b","CHRISTMAS 2026","Gifts *he.ll* actually use","husband · dad · brother",["yeti","leatherman","beanie","airtag"],104,True)
pin("rush-b","SHIPS FAST","Last-minute gifts she'll *love*","order by Dec 18",["ugg","kendra","laneige","sdj"],104,True)
pin("swap-b","GIFT EXCHANGE","White elephant gifts *under $50*","the ones people steal",["stanley","dash","jbl","yeti"],100,True)
pin("teach-b","TEACHER GIFTS","Teacher gifts that aren't *another mug*","they'll actually use these",["tiesta","laneige","yeti","stanley"],98,True)
pin("cozy-b","COZY GIFTS","Cozy gifts for *her*","blankets · slippers · candles",["bdthrow","ugg","yankee","bdsocks"],120,True)
pin("dog-b","DOG LOVER GIFTS","Gifts for *dog lovers*","and a stocking for the pup",["kong","benebone","bdthrow","stanley"],112,True)
pin("morn-b","CHRISTMAS MORNING","Cozy Christmas *morning*","cozy, slow + a little luxe",["ugg","blissy","yankee","bdsocks"],100,True)
pin("pjs-b","CHRISTMAS EVE","Christmas Eve box *ideas*","for the whole family",["bdthrow","ugg","bdsocks","blissy"],112,True)
pin("wrap-b","GIFT WRAP","Gift wrapping that looks *expensive*","for under $30",["kraft","ribbon","oranges","ribbons2"],100,True)
pin("u25-b","STOCKING STUFFERS","Stocking stuffers *for her*","all under $25",["sdj","laneige","claw","candle"],112,True)
# design C: cream 3x3 "Amazon finds"
pin("her-c","AMAZON FINDS","Christmas gifts for *her*","the ones on every wishlist",["ugg","blissy","kendra","laneige","sdj","bdthrow","stanley","thera","bdsocks"],108)
pin("him-c","AMAZON FINDS","Gifts for the man who has *everything*","practical + actually cool",["yeti","airtag","leatherman","beanie","boseqc","thera","stanley","jbl","dash"],96)
pin("cozy-c","AMAZON FINDS","Cozy Amazon finds for *winter*","everything soft + warm",["bdthrow","ugg","bdsocks","yankee","blissy","candle","pillow","laneige","stanley"],108)
pin("u25-c","AMAZON FINDS","Gifts under $25 that look *expensive*","small gifts, big wow",["laneige","sdj","claw","candle","pillow","ribbon","bdsocks","tiesta","oranges"],96)
pin("swap-c","AMAZON FINDS","Best white elephant gifts *2026*","fun, useful + steal-worthy",["dash","stanley","yeti","jbl","jellycat","kong","tiesta","bdsocks","laneige"],100)
# new guides
pin("spoil-a","GIFT GUIDE","Gifts for the woman who has *everything*","spoil her a little",["thera","sdj","laneige","blissy"],100)
pin("spoil-b","SELF-CARE GIFTS","Luxe self-care gifts *she'll love*","spa night, at home",["blissy","thera","bdthrow","sdj"],104,True)
pin("stock-a","STOCKING STUFFERS","Stocking stuffers *she'll actually use*","beauty + cozy minis",["laneige","sdj","claw","bdsocks"],104)
json.dump(out,open("specs/pins2.json","w",encoding="utf-8"),ensure_ascii=False,indent=0)
print(len(out))
