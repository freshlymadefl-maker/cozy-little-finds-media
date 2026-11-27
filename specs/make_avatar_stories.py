"""Avatar Story versions (Nov 27 2026). Owner: max one avatar meme per day in the feed; extras go to Stories.
1080x1920: blurred photo fill, full 4:5 photo in the middle, text in the band above the photo (never on faces)."""
import subprocess, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "posts" / "avatar-stories"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
S = {
 "e01": "Holiday hosting rule:<br>if there\u2019s a candle,<br>it\u2019s a party",
 "e02": "Taste-testing is<br>part of the job",
 "e03": "Half the dough never<br>makes it to the oven",
 "e04": "When the tiny pink<br>tree finally arrives",
 "e05": "Errands, but make it a<br>cookie the size of your face",
 "e07": "They’re not burnt,<br>they’re “extra toasty”",
 "e06": "The bigger the bow,<br>the better the day",
}
def html(img, text):
    return f"""<html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@800&display=swap" rel="stylesheet">
<style>*{{margin:0;padding:0}} body{{width:1080px;height:1920px;overflow:hidden;position:relative;background:#111}}
.bg{{position:absolute;inset:-60px;background:url('{img}') center/cover;filter:blur(34px) brightness(.5)}}
.ph{{position:absolute;left:0;top:450px;width:1080px;height:1350px;object-fit:cover}}
.t{{position:absolute;top:130px;left:50px;right:50px;height:290px;display:flex;align-items:center;justify-content:center;text-align:center;
font-family:Montserrat;font-weight:800;font-size:64px;line-height:1.1;color:#f6dc8f;text-shadow:0 3px 12px rgba(0,0,0,.6)}}</style></head>
<body><div class="bg"></div><div class="t">{text}</div><img class="ph" src="{img}"></body></html>"""
if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for n, t in S.items():
        if sys.argv[1:] and n not in sys.argv[1:]: continue
        img = (ROOT/'src'/'avatar'/f'{n}.png').as_uri()
        p = OUT/f"{n}.html"; p.write_text(html(img, t), encoding="utf-8")
        subprocess.run([EDGE,"--headless=new","--disable-gpu","--hide-scrollbars","--window-size=1080,1920","--virtual-time-budget=5000",
                        f"--screenshot={(OUT/f'{n}.png').as_posix()}", p.as_uri()], check=True, capture_output=True)
    print("done")
