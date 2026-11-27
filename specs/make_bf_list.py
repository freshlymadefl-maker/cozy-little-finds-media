"""Black Friday deals brand list (Nov 27 2026, owner loved @styledbyacadams' list post).
All % verified on Amazon (our lists 130E7ZOARI2MV + 10QSDVIGJ8PAN) and the Walmart Creator homepage
around 12:30am ET Nov 27. Prices change; caption says 'at time of posting'."""
import subprocess, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "posts" / "bf-list"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
AMZ = [("AirPods Pro 3", "$100 off"), ("Beats Studio Pro", "50% off"), ("Bedsure Satin Pillowcases", "62% off"),
       ("Bose QuietComfort", "53% off"), ("Bose SoundLink Flex", "$50 off"), ("Columbia Fleece", "43% off"),
       ("Cuisinart Ice Cream Maker", "40% off"), ("Echo Show 15", "$120 off"), ("Keurig K-Elite", "$90 off"),
       ("Kindle Paperwhite", "$70 off"), ("Laneige Lip Mask", "25% off"), ("Leatherman Wave+", "20% off"),
       ("Marshall Speaker", "50% off"), ("Ninja SLUSHi", "$120 off"), ("Oakley Holbrook", "57% off"),
       ("Revlon One-Step", "43% off"), ("Shark FlexStyle", "$135 off"), ("Shark Robot Vacuum", "47% off"),
       ("Sol de Janeiro Mist", "25% off"), ("Thermapen ONE", "20% off")]
WMT = [("Blackstone Griddle", "33% off"), ("CAROTE Cookware Set", "52% off"), ("Celebrity Pink Booties", "62% off"),
       ("Costway Flocked Tree", "53% off"), ("De\u2019Longhi Espresso", "47% off"), ("Dyson V12", "45% off"),
       ("GE Opal Ice Maker", "36% off"), ("Hanes Hoodies", "68% off"), ("Hisense 65\" 4K TV", "43% off"),
       ("Instax Mini SE Bundle", "43% off"), ("Levi\u2019s Bootcut Jeans", "44% off"), ("Michael Kors Crossbody", "58% off"),
       ("Michael Kors Watch", "39% off"), ("Nestl Sheet Set", "56% off"), ("Nex Playground", "30% off"),
       ("Ninja SLUSHi XL", "47% off"), ("Razor E90 Scooter", "30% off"), ("Shark Lift-Away", "62% off"),
       ("SHEWIN Puffer", "49% off"), ("UVN Pajama Set", "49% off")]

def col(title, rows):
    r = "".join(f"<div class='r'><b>{b}</b> - {d}</div>" for b, d in rows)
    return f"<div class='c'><div class='h'>{title}</div>{r}</div>"

HTML = f"""<html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600&family=Allura&family=Montserrat:wght@400;600&display=swap" rel="stylesheet">
<style>*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:#fbf7f1;position:relative;font-family:Montserrat;color:#1b1b1b}}
.frame{{position:absolute;left:54px;right:54px;top:78px;bottom:70px;border:3px solid #e3a6c4}}
.t{{position:absolute;top:22px;left:0;right:0;text-align:center;font-family:'Playfair Display';font-weight:500;font-size:104px;letter-spacing:2px}}
.t span{{background:#fbf7f1;padding:0 18px}}
.d{{position:absolute;top:104px;left:0;right:0;text-align:center;font-family:Allura;font-size:118px;color:#d98ab3;transform:rotate(-4deg)}}
.cols{{position:absolute;top:262px;left:70px;right:70px;display:flex;gap:30px}}
.c{{flex:1;text-align:center}}
.h{{font-family:'Playfair Display';font-style:italic;font-size:34px;color:#b5578a;margin-bottom:12px}}
.r{{font-size:25px;line-height:1.74;white-space:nowrap}}
.r b{{font-weight:600}}
.f{{position:absolute;bottom:92px;left:0;right:0;text-align:center;font-size:21px;color:#6b6b6b}}
.s{{position:absolute;bottom:22px;left:0;right:0;text-align:center;font-size:22px;letter-spacing:3px;color:#9a9a9a}}
</style></head><body><div class="frame"></div>
<div class="t"><span>BLACK FRIDAY</span></div><div class="d">deals</div>
<div class="cols">{col("on Amazon", AMZ)}{col("at Walmart", WMT)}</div>
<div class="f">Prices as of Nov 27 and can change fast. Links in bio. #ad #WalmartPartner</div>
<div class="s">@COZYLITTLEFINDSDAILY</div></body></html>"""

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    p = OUT / "bf-list.html"; p.write_text(HTML, encoding="utf-8")
    subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--window-size=1080,1350",
                    "--virtual-time-budget=6000", f"--screenshot={(OUT/'bf-list.png').as_posix()}", p.as_uri()], check=True, capture_output=True)
    print("done")
