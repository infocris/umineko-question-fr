#!/usr/bin/env python3
"""Génère tools/ui_mod_cards.json : zones de texte des écrans recomposés par 07th-mod (1920x1080)."""
import json

E = "en/bmp/background/efe/"
ep = json.load(open("tools/ui_epitaph.json", encoding="utf-8"))
ex = ep[E + "text010.png"]
cards = json.load(open("tools/ui_cards.json", encoding="utf-8"))
notices = json.load(open("tools/ui_notices.json", encoding="utf-8"))
manual = json.load(open("tools/ui_manual.json", encoding="utf-8"))

def c(src, **kw):
    d = {k: v for k, v in src.items() if k not in ("region", "rows", "thr", "min_h", "gap", "scale")}
    d.update(kw)
    return d

spec = {}
DATE = [600, 470, 1320, 700]
spec[E + "oct_4_1986.png"] = c(cards[E + "oct_4_1986.png"], region=DATE, en=["The First Day", "October 4th, 1986", None])
spec[E + "oct_5_1986.png"] = c(cards[E + "oct_5_1986.png"], region=DATE, en=["The Second Day", "October 5th, 1986", None])
spec[E + "oct_1998.png"] = c(cards[E + "oct_1998.png"], region=DATE, en=["The world 12 years later", "October, 1998", None])
spec[E + "enj_mirai01.png"] = c(cards[E + "enj_mirai01.png"], region=DATE)
spec[E + "ep2_text.png"] = c(cards[E + "ep2_text.png"], region=[300, 495, 1620, 585])
spec[E + "unknown01.png"] = c(cards[E + "unknown01.png"], region=[500, 480, 1420, 630])
for t in ("text001.png", "text1.png"):
    spec[E + t] = c(cards[E + t], region=[560, 440, 1720, 650], thr=60, white=True, shadow=True)
spec[E + "text002.png"] = c(notices[E + "text002.png"], region=[130, 730, 900, 1030])
b = notices[E + "text003.png"]["blocks"]
spec[E + "text003.png"] = {"blocks": [c(b[0], region=[130, 730, 900, 1030]), c(b[1], region=[1370, 945, 1730, 995])]}
spec[E + "text004.png"] = c(notices[E + "text004.png"], region=[1130, 680, 1780, 930])
spec[E + "text005.png"] = c(notices[E + "text005.png"], region=[1130, 750, 1810, 905])
spec[E + "text006.png"] = c(notices[E + "text006.png"], region=[1130, 650, 1800, 1000], min_h=10)
spec[E + "text007.png"] = c(notices[E + "text007.png"], region=[850, 925, 1860, 1000])
for t in ("text010.png", "text010a.png", "text010b.png", "text010c.png"):
    spec[E + t] = c(ex, region=[395, 45, 1600, 1035], thr=60)
spec[E + "text011.png"] = c(ep[E + "text011.png"], region=[420, 420, 1540, 670], thr=60)
spec[E + "text012.png"] = c(ep[E + "text012.png"], region=[300, 280, 1620, 775], thr=60)
spec[E + "op0101.png"] = {"region": [940, 505, 1710, 580], "align": "center", "shadow": True, "white": True, "thr": 60,
                         "en": ["Legend of the golden witch"], "lines": ["La Légende de la Sorcière dorée"]}
mb = manual["en/bmp/title/manual.png"]["blocks"]
spec["en/bmp/title/manual.png"] = {"blocks": [c(mb[0], region=[360, 225, 900, 845], gap=1, min_h=10, outline=True),
                                              c(mb[1], region=[360, 850, 900, 895], outline=True)]}
json.dump(spec, open("tools/ui_mod_cards.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(spec), "écrans")
