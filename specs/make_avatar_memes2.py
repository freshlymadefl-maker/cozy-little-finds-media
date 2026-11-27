"""Batch 2 of avatar memes (Nov 27 2026): 16 photos, POV-style text kept off faces, soft dark gradient
behind the text for readability. Owner rules: don't cover her face; keep her identity a mystery."""
import subprocess, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "posts" / "avatar2"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
M = {  # file: (text, 'top'|'bottom')
 "b01": ("POV: walking the<br>Christmas lights<br>with hot cocoa", "bottom"),
 "b02": ("Holiday happy hour:<br>the only meeting<br>worth attending", "bottom"),
 "b03": ("Every friend group<br>needs the one who<br>says \u201cjust one drink\u201d", "top"),
 "b04": ("When someone asks<br>how much you spent<br>on gifts this year", "bottom"),
 "b05": ("Getting ready for the<br>holiday party like<br>it\u2019s the Met Gala", "bottom"),
 "b06": ("POV: buying cookies<br>for the neighbors<br>(and a tin for the car)", "bottom"),
 "b07": ("POV: you came in<br>for one sweater", "bottom"),
 "b08": ("Weekend errands:<br>iced coffee first,<br>responsibilities later", "bottom"),
 "b09": ("Shopping for everyone<br>else is exhausting.<br>Cake is medically necessary.", "bottom"),
 "b10": ("Retail therapy:<br>still cheaper than<br>actual therapy", "bottom"),
 "b11": ("Handling the vintage<br>ornaments like a<br>bomb technician", "bottom"),
 "b12": ("Plans tonight:<br>absolutely none", "top"),
 "b13": ("The \u201cquick\u201d errand:<br>2 hours, 4 bags,<br>1 latte", "bottom"),
 "b14": ("When the trunk is full<br>but the list<br>still isn\u2019t done", "bottom"),
 "b15": ("Wrapping supplies: \u2705<br>Wrapping motivation: \u274c", "bottom"),
 "c01": ("POV: the delivery driver<br>knows you by name", "bottom"),
 "c02": ("When you find the<br>vintage Santa you didn’t<br>know you needed", "bottom"),
 "c03": ("POV: you said “just<br>a few gifts” this year", "bottom"),
 "c04": ("POV: the best gift is<br>the one you buy yourself", "bottom"),
 "d01": ("POV: you opened the<br>white elephant gift<br>everyone wanted", "bottom"),
 "d02": ("Went in for<br>ginger snaps", "bottom"),
 "d03": ("Ugly sweater day<br>but you own 47<br>ugly sweaters", "bottom"),
 "d04": ("Christmas Eve,<br>11pm, wrapping<br>break #6", "top"),
 "f01": ("NYE outfit crisis:<br>velvet or sequins?", "bottom"),
 "f02": ("The star crown is<br>non-negotiable", "bottom"),
 "f03": ("New year, new me.<br>Kidding. Same socks.", "top"),
 "f04": ("Made it to midnight.<br>Barely. Proudly.", "bottom"),
 "g03": ("January: the month we<br>“take a break<br>from spending”", "bottom"),
 "h_trunk": ("Went in for<br>toilet paper", "bottom"),
 "h_cozybed": ("Had big plans today.<br>The bed had<br>bigger ones.", "bottom"),
 "h_fries": ("The January salad era<br>lasted 11 days", "bottom"),
 "h_citylights": ("She’s the reason I have<br>no money and<br>excellent stories", "bottom"),
 "h_pizza": ("Came for one pizza.<br>Stayed three hours.", "bottom"),
 "h_brunch": ("Sunday debrief:<br>nobody is fine", "bottom"),
 "h_carflowers": ("The flowers got<br>the passenger seat", "top"),
 "i_car": ("Passenger princess<br>reporting for duty", "top"),
 "i_pasta": ("The recipe said a splash<br>of wine. I don’t know her.", "top"),
 "i_mirrorkiss": ("Every girls’ night ends<br>at the bathroom mirror", "bottom"),
 "i_cozylegs": ("Sunday reset, step one:<br>don’t get up", "top"),
 "i_peonies": ("Fresh flowers are a<br>grocery staple.<br>Don’t fact-check me.", "top"),
 "b16": ("December personality:<br>Christmas movies,<br>popcorn, zero plans", "bottom"),
}
def html(img, text, where):
    grad = ("bottom:0;height:46%;background:linear-gradient(to top,rgba(0,0,0,.55),rgba(0,0,0,0))" if where == "bottom"
            else "top:0;height:40%;background:linear-gradient(to bottom,rgba(0,0,0,.55),rgba(0,0,0,0))")
    pos = "bottom:70px" if where == "bottom" else "top:60px"
    return f"""<html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@800&display=swap" rel="stylesheet">
<style>*{{margin:0;padding:0}} body{{width:1080px;height:1350px;overflow:hidden;position:relative;background:#000}}
img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}} .g{{position:absolute;left:0;right:0;{grad}}}
.t{{position:absolute;{pos};left:40px;right:40px;text-align:center;font-family:Montserrat;font-weight:800;font-size:72px;line-height:1.08;
color:#f6dc8f;letter-spacing:-1px;text-shadow:0 3px 14px rgba(0,0,0,.6),0 1px 3px rgba(0,0,0,.7)}}</style></head>
<body><img src="{img}"><div class="g"></div><div class="t">{text}</div></body></html>"""
if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, (text, where) in M.items():
        if __import__("sys").argv[1:] and name not in __import__("sys").argv[1:]: continue
        p = OUT / f"{name}.html"; p.write_text(html((ROOT/'src'/'avatar'/f'{name}.png').as_uri(), text, where), encoding="utf-8")
        subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--window-size=1080,1350",
                        "--virtual-time-budget=5000", f"--screenshot={(OUT/f'{name}.png').as_posix()}", p.as_uri()], check=True, capture_output=True)
    print("done")
