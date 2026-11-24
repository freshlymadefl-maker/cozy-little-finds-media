"""Morning find v2 (owner Nov 24 2026): strong first-person hook, verified Black Friday deal badge, tap-to-shop + comment keyword."""
import json
exec(open("specs/make_morning.py",encoding="utf-8").read().split("L = {")[0])
L = {"COZY":"1NS08WQTADRJK","SWAP":"WDTTRUUMBWB6","MOM":"1C1D9BF3HX86P","GENT":"38CPJYTLJ13GH","MORNING":"P6V8V2VG6HIH","TEACHER":"RY4NCYOFPW3L","LUXE":"28EFTLVOUQR5C","RUSH":"27GZT4NVS9HUG","WOOF":"3B8R1HJU8LGPS","WRAP":"2YYODQJGDA89R"}
# (slot, key, eyebrow, hook, name, keyword, deal?)
D = [
 ("2026-11-24T14:00","blissy","BLISSY","I'll never sleep on cotton *again.*","Blissy Silk Pillowcase","MOM",1),
 ("2026-11-25T10:30","boseqc","BOSE","The best gift I ever gave *myself.*","Bose QuietComfort Headphones","RUSH",1),
 ("2026-11-26T18:00","kendra","KENDRA SCOTT","The gift that never gets *returned.*","Kendra Scott Elisa Necklace","MOM",1),
 ("2026-11-27T10:00","thera","THERAGUN","Everyone on my list wants *this.*","Theragun","RUSH",1),
 ("2026-11-27T14:00","airtag","APPLE","He'll never lose his keys *again.*","Apple AirTag","GENT",1),
 ("2026-11-28T14:00","stanley","STANLEY","Still the gift they *actually* want.","Stanley Quencher","SWAP",1),
 ("2026-11-29T07:30","yankee","YANKEE CANDLE","My house smells like Christmas *all day.*","Yankee Candle Large Jar","MORNING",1),
 ("2026-11-30T07:30","sdj","SOL DE JANEIRO","A vacation in a bottle, *on sale.*","Sol de Janeiro Cheirosa Mist","LUXE",1),
 ("2026-11-30T14:00","boseflex","BOSE","Kitchen dance parties, *upgraded.*","Bose SoundLink Flex","MOM",1),
 ("2026-12-01T07:30","bdsocks","BAREFOOT DREAMS","My feet are never cold *anymore.*","Barefoot Dreams CozyChic Socks","COZY",0),
 ("2026-12-02T07:30","dash","DASH","The gift that *always* gets stolen.","Dash Mini Waffle Maker","SWAP",0),
 ("2026-12-03T07:30","kendra","KENDRA SCOTT","The gift that never gets *returned.*","Kendra Scott Elisa Necklace","MOM",0),
 ("2026-12-04T07:30","boseflex","BOSE","Kitchen dance parties, *upgraded.*","Bose SoundLink Flex","MOM",0),
 ("2026-12-05T07:30","jellycat","JELLYCAT","Grown adults *will* fight over this.","Jellycat Bashful Bunny","SWAP",0),
 ("2026-12-06T07:30","airtag","APPLE","He'll never lose his keys *again.*","Apple AirTag","GENT",0),
 ("2026-12-07T07:30","ugg","UGG","I live in these *November to March.*","UGG Tasman Slippers","MORNING",0),
 ("2026-12-08T07:30","tiesta","TIESTA TEA","The teacher gift they'll *actually* use.","Tiesta Tea Sampler","TEACHER",0),
 ("2026-12-09T07:30","bdthrow","BAREFOOT DREAMS","The softest thing I've *ever* owned.","Barefoot Dreams CozyChic Throw","MOM",0),
 ("2026-12-10T07:30","leatherman","LEATHERMAN","The gift he'll use *every single day.*","Leatherman Wingman","GENT",0),
 ("2026-12-11T07:30","sdj","SOL DE JANEIRO","Smells like a vacation *in a bottle.*","Sol de Janeiro Cheirosa Mist","LUXE",0),
 ("2026-12-12T07:30","yankee","YANKEE CANDLE","My house smells like Christmas *all day.*","Yankee Candle Large Jar","MORNING",0),
 ("2026-12-13T07:30","claw","KITSCH","My entire hairstyle, *honestly.*","Kitsch Puffy Claw Clip","LUXE",0),
 ("2026-12-14T07:30","ribbon","GIFT WRAP","Plain paper + this = *boutique wrap.*","Red Velvet Ribbon","WRAP",0),
 ("2026-12-15T07:30","pillow","KITSCH","The stocking stuffer she'll use *nightly.*","Kitsch Satin Pillowcase","LUXE",0),
 ("2026-12-16T07:30","boseqc","BOSE","The best gift I ever gave *myself.*","Bose QuietComfort Headphones","RUSH",0),
 ("2026-12-17T07:30","beanie","CARHARTT","He'll wear it *every single day.*","Carhartt Knit Beanie","GENT",0),
 ("2026-12-18T07:30","kong","KONG","Peanut butter inside = *30 quiet minutes.*","KONG Classic","WOOF",0),
 ("2026-12-19T07:30","stanley","STANLEY","Still the gift they *actually* want.","Stanley Quencher","RUSH",0),
 ("2026-12-20T07:30","candle","VOLUSPA","Makes any bathroom feel like *a hotel.*","Voluspa Petite Candle","LUXE",0),
]
out, meta = [], []
for dt,k,eb,hook,name,kw,deal in D:
    img, fit = I[k]; nm = f"f2-{dt[5:10]}-{dt[11:13]}"
    sp = {"name":nm,"type":"find","img":img,"fit":fit,"eyebrow":("☕ MORNING FIND · " if dt[11:16]=="07:30" else "")+eb,"hook":hook,"prod":name,"kw":kw}
    if deal: sp["deal"]="BLACK FRIDAY DEAL"; sp["eyebrow"]=eb
    out.append(sp); meta.append({"name":nm,"date":dt,"key":k,"hook":hook.replace("*",""),"prod":name,"kw":kw,"list":L[kw],"deal":deal})
json.dump(out,open("specs/find2.json","w",encoding="utf-8"),ensure_ascii=False,indent=0)
json.dump(meta,open("specs/find2-meta.json","w",encoding="utf-8"),ensure_ascii=False,indent=0)
print(len(out))
