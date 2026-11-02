#!/usr/bin/env python3
"""Rend les fiches personnages / pages d'Infos traduites.

  pagerender.py <pages.json> <dossier_fr> <dossier_sortie> [--only hash,...] [--preview f.png]

- Fiches (cha) : calque transparent, texte blanc détouré de noir, marge gauche 30 px.
- Infos (tips) : texte posé sur le fond vierge du jeu (txt_tips*.png), justifié.
Le bloc de texte est centré verticalement sur la position du bloc anglais d'origine.
"""
import json, os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.environ.get("PAGE_ROOT", "ui/en_original/en/bmp/r_click/text/")
BG = {(472, 772): "txt_def.png", (472, 806): "txt_def2.png", (886, 772): "txt_tips.png", (886, 806): "txt_tips2.png"}
FONT = "/System/Library/Fonts/Supplemental/Charter.ttc"


def F(size, bold=True):
    return ImageFont.truetype(FONT, size, index=3 if bold else 0)


def calibrate(sample, target_w, bold=True):
    s = 6
    while F(s + 1, bold).getlength(sample) <= target_w:
        s += 1
    return s


# Calibrage sur des lignes anglaises non justifiées mesurées dans les images d'origine.
CHA = dict(body=calibrate("The aged head of the Ushiromiya family.", 335) + 1,
           title=calibrate("Ushiromiya Kinzo", 197), pitch=28, title_pitch=31, margin=30)
TIPS = dict(body=calibrate("to gain the Endless Power in its truest sense.", 496) + 1,
            title=calibrate("Mariage Sorcière", 231), pitch=36, title_pitch=44, margin=31)


def bg_for(size):
    """Fond vierge le plus proche en taille (le patch a des fonds à ±1 px)."""
    cands = {}
    for b in ("txt_def.png", "txt_def2.png", "txt_tips.png", "txt_tips2.png"):
        if os.path.exists(ROOT + b):
            cands[b] = Image.open(ROOT + b).size
    best = min(cands, key=lambda b: abs(cands[b][0] - size[0]) + abs(cands[b][1] - size[1]))
    im = Image.open(ROOT + best).convert("RGBA")
    return im if im.size == size else im.resize(size, Image.LANCZOS)


def text_rows(img, kind):
    a = np.array(img.convert("RGBA")).astype(int)
    if kind == "cha":
        m = (a[..., 3] > 100) & (a[..., :3].max(axis=2) > 150)
    else:
        b = np.array(bg_for(img.size).convert("RGB")).astype(int)
        m = np.abs(a[..., :3] - b).max(axis=2) > 60
    ys, xs = np.nonzero(m)
    return (ys.min(), ys.max(), xs.min()) if len(ys) else (img.height // 3, img.height * 2 // 3, 30)


NB = "\u00a0"


def protect(text):
    """Espaces insécables : « mot », mot !, mot ?, mot :, mot ;"""
    import re
    text = re.sub(r"« +", "«" + NB, text)
    text = re.sub(r" +([»!?:;])", NB + r"\1", text)
    return text


def wrap(text, f, width):
    words, lines, cur = [w for w in protect(text).split(" ") if w], [], []
    for w in words:
        t = " ".join(cur + [w])
        if cur and f.getlength(t) > width:
            lines.append((cur, False))
            cur = [w]
        else:
            cur.append(w)
    if cur:
        lines.append((cur, True))
    return lines  # (mots, dernière_ligne_du_paragraphe)


def scaled(P, k):
    return dict(body=max(6, round(P["body"] * k)), title=max(6, round(P["title"] * k)),
                pitch=P["pitch"] * k, title_pitch=P["title_pitch"] * k, margin=round(P["margin"] * k))


def layout(txt, P, width, scale):
    body, title = F(max(6, int(P["body"] * scale))), F(max(6, int(P["title"] * scale)))
    pitch, tpitch = P["pitch"] * scale, P["title_pitch"] * scale
    ops, y = [], 0.0
    src = txt.strip("\n").split("\n")
    for i, line in enumerate(src):
        if line.startswith("# "):
            ops.append(("title", y, line[2:].strip(), title))
            y += tpitch
        elif not line.strip():
            y += pitch
        else:
            for words, last in wrap(line.strip(), body, width):
                ops.append(("body", y, (words, last), body))
                y += pitch
    return ops, y


def draw_words(d, x, y, words, last, f, width, justify, **kw):
    words = [w.replace(NB, " ") for w in words]
    if not justify or last or len(words) == 1:
        d.text((x, y), " ".join(words), font=f, anchor="ls", **kw)
        return
    total = sum(f.getlength(w) for w in words)
    gap = (width - total) / (len(words) - 1)
    for w in words:
        d.text((x, y), w, font=f, anchor="ls", **kw)
        x += f.getlength(w) + gap


SCALES = {}


def render(kind, size, orig, txt):
    W, H = size
    k = W / (472 if kind == "cha" else 886)
    P = scaled(CHA if kind == "cha" else TIPS, k)
    top, bottom, left = text_rows(orig, kind)
    left = P["margin"] if kind == "cha" else max(P["margin"], min(left, round(80 * k)))
    width = W - 2 * left
    scale = 1.0
    while True:
        ops, h = layout(txt, P, width, scale)
        if h <= H - 70 * k or scale < 0.6:
            break
        scale -= 0.04
    SCALES[id(txt)] = scale
    center = (top + bottom) / 2
    first_base = center - (h - P["pitch"] * scale) / 2 + P["body"] * scale * 0.35
    first_base = max(first_base, 36 * k)
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    shadow = Image.new("RGBA", size, (0, 0, 0, 0))
    dl, ds = ImageDraw.Draw(layer), ImageDraw.Draw(shadow)
    for kind_op, y, content, f in ops:
        yb = first_base + y
        if kind_op == "title":
            for d, off, kw in ((ds, 1, dict(fill=(0, 0, 0, 255), stroke_width=2, stroke_fill=(0, 0, 0, 255))),
                               (dl, 0, dict(fill=(255, 255, 255, 255), stroke_width=1, stroke_fill=(0, 0, 0, 255)))):
                d.text((left + off, yb + off), content, font=f, anchor="ls", **kw)
        else:
            words, last = content
            for d, off, kw in ((ds, 1, dict(fill=(0, 0, 0, 255), stroke_width=2, stroke_fill=(0, 0, 0, 255))),
                               (dl, 0, dict(fill=(255, 255, 255, 255), stroke_width=1, stroke_fill=(0, 0, 0, 255)))):
                draw_words(d, left + off, yb + off, words, last, f, width, kind == "tips", **kw)
    text = Image.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(1.5)), layer)
    if kind == "cha":
        return text
    return Image.alpha_composite(bg_for(size), text)


def main():
    pages_path, fr_dir, out = sys.argv[1:4]
    only = set(sys.argv[sys.argv.index("--only") + 1].split(",")) if "--only" in sys.argv else None
    preview = sys.argv[sys.argv.index("--preview") + 1] if "--preview" in sys.argv else None
    pages = json.load(open(pages_path, encoding="utf-8"))
    done, missing, prev = 0, [], []
    for h, v in pages.items():
        if only and h not in only:
            continue
        p = os.path.join(fr_dir, h + ".txt")
        if not os.path.exists(p):
            missing.append(h)
            continue
        txt = open(p, encoding="utf-8").read()
        if not os.path.exists(ROOT + v["files"][0]):
            print("  absente dans la source :", v["files"][0])
            continue
        orig = Image.open(ROOT + v["files"][0])
        img = render(v["kind"], orig.size, orig, txt)
        sc = SCALES.get(id(txt), 1.0)
        if sc < 1.0:
            print(f"  réduit à {sc:.2f} : {v['files'][0]}")
        for rel in v["files"]:
            if not os.path.exists(ROOT + rel):
                continue
            o2 = Image.open(ROOT + rel)
            if o2.size != orig.size:
                img2 = render(v["kind"], o2.size, o2, txt)
            else:
                img2 = img
            dst = os.path.join(out, "en/bmp/r_click/text", rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            img2.save(dst)
            done += 1
        prev.append((v, orig, img))
    print(f"{done} images écrites, {len(missing)} pages sans traduction")
    if preview and prev:
        rows = []
        for v, o, n in prev:
            dark = Image.new("RGBA", o.size, (20, 10, 10, 255))
            if v["kind"] == "cha":
                bg = Image.alpha_composite(dark, bg_for(o.size))
            else:
                bg = dark
            o = Image.alpha_composite(bg, o.convert("RGBA"))
            n = Image.alpha_composite(bg, n.convert("RGBA"))
            rows.append((o.convert("RGB"), n.convert("RGB")))
        W = max(o.width for o, n in rows) * 2 + 10
        sheet = Image.new("RGB", (W, sum(o.height + 6 for o, n in rows)), (255, 0, 255))
        y = 0
        for o, n in rows:
            sheet.paste(o, (0, y))
            sheet.paste(n, (o.width + 10, y))
            y += o.height + 6
        sheet.save(preview)


if __name__ == "__main__":
    main()
