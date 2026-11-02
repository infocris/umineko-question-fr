#!/usr/bin/env python3
"""Réécrit des écrans de texte (dates, avertissements, notices) ligne par ligne.

  card.py <spec.json> <dossier_source> <dossier_sortie> [--preview fichier.png]

spec.json : { "chemin.png": {
    "lines": ["texte FR" | null, ...],   # une entrée par ligne détectée ; null = ligne gardée
    "region": [x0, y0, x1, y1],          # optionnel : zone où chercher le texte
    "align": "center" | "left",          # défaut : center
    "thr": 60,                           # optionnel : écart au fond pour détecter le texte
    "glow": true                         # optionnel : halo coloré autour du texte (ep2_text)
}}
Chaque ligne détectée est effacée (inpainting) puis réécrite à la même place, à la même
hauteur, dans la même couleur. Si la ligne française est trop large, la taille diminue.
"""
import json, os, sys
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONT = "/System/Library/Fonts/Supplemental/Charter.ttc"


FACE = {"roman": 0, "bold": 3}


def font(size, face="bold"):
    return ImageFont.truetype(FONT, size, index=FACE[face])


def line_rows(mask, min_gap=4):
    rows = mask.any(axis=1)
    out, y = [], 0
    while y < len(rows):
        if rows[y]:
            s = y
            gap = 0
            while y < len(rows) and (rows[y] or gap < min_gap):
                gap = 0 if rows[y] else gap + 1
                y += 1
            out.append((s, y - gap))
        y += 1
    return out


def fit_size(text, cap_h):
    lo, hi = 4, 300
    while lo < hi:
        mid = (lo + hi + 1) // 2
        b = font(mid).getbbox(text, anchor="ls")
        if b[3] - b[1] <= cap_h:
            lo = mid
        else:
            hi = mid - 1
    return lo


SYMBOLS = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
MISSING = set("■→「」")


def runs(text):
    """Découpe le texte en morceaux (texte, police_de_secours?)."""
    out, cur, fb = [], "", None
    for ch in text:
        f2 = ch in MISSING
        if cur and f2 != fb:
            out.append((cur, fb))
            cur = ""
        cur += ch
        fb = f2
    if cur:
        out.append((cur, fb))
    return out


def square_side(f):
    b = f.getbbox("H", anchor="ls")
    return b[3] - b[1]


def seg_len(t, fb, f, sym):
    if t == "■":
        return square_side(f) + max(2, square_side(f) // 6)
    return (sym if fb else f).getlength(t)


def text_len(text, f, sym):
    out = 0
    for t, fb in runs(text):
        for piece in (t.split("■") if "■" in t else [t]):
            pass
    return sum(seg_len(p, fb, f, sym) for t, fb in runs(text) for p in split_sq(t))


def split_sq(t):
    out, cur = [], ""
    for ch in t:
        if ch == "■":
            if cur:
                out.append(cur)
            out.append("■")
            cur = ""
        else:
            cur += ch
    if cur:
        out.append(cur)
    return out


def draw_text(draw, x, baseline, text, f, sym, **kw):
    for t, fb in runs(text):
        for p in split_sq(t):
            if p == "■":
                side = square_side(f)
                sw = kw.get("stroke_width", 0)
                draw.rectangle([x - sw, baseline - side - sw, x + side + sw, baseline + sw], fill=kw.get("fill"))
            else:
                draw.text((x, baseline), p, font=(sym if fb else f), anchor="ls", **kw)
            x += seg_len(p, fb, f, sym)


def render_block(orig, cur, spec):
    a = orig
    H, W = a.shape[:2]
    x0r, y0r, x1r, y1r = spec.get("region", [0, 0, W, H])
    reg = a[y0r:y1r, x0r:x1r]
    blur = cv2.medianBlur(reg.astype(np.uint8), 31).astype(int)
    diff = np.abs(reg - blur).max(axis=2)
    mask = (diff > spec.get("thr", 60))
    if spec.get("white"):
        mask &= reg.max(axis=2) > 185
    if spec.get("outline"):
        # Texte détouré de noir sur fond clair : on repère le contour noir.
        mask = reg.max(axis=2) < 70
    mask = mask.astype(np.uint8)
    rows = [r for r in line_rows(mask, spec.get("gap", 4)) if r[1] - r[0] >= spec.get("min_h", 6)]
    if spec.get("rows"):
        rows = [(a - y0r, b - y0r) for a, b in spec["rows"]]
    lines = spec["lines"]
    en_lines = spec.get("en") or [None] * len(lines)
    if len(rows) != len(lines):
        raise ValueError(f"{len(rows)} lignes détectées, {len(lines)} fournies : {[(r[0]+y0r, r[1]+y0r) for r in rows]}")
    full_mask = np.zeros((H, W), np.uint8)
    plan = []
    for (ys, ye), fr, en in zip(rows, lines, en_lines):
        if fr is None:
            continue
        m = mask[ys:ye]
        xs = np.nonzero(m.any(axis=0))[0]
        lx0, lx1 = xs.min() + x0r, xs.max() + 1 + x0r
        ly0, ly1 = ys + y0r, ye + y0r
        full_mask[ly0:ly1, lx0:lx1] |= m[:, xs.min():xs.max() + 1]
        px = reg[ys:ye][m.astype(bool)]
        lum = px.max(axis=1)
        if spec.get("color"):
            color = tuple(spec["color"])
        elif np.median(blur[ys:ye].max(axis=2)) < 128:
            color = tuple(int(c) for c in np.median(px[lum >= np.percentile(lum, 70)], axis=0))
        else:
            color = tuple(int(c) for c in np.median(px[lum <= np.percentile(lum, 30)], axis=0))
        if spec.get("glow"):
            color = (255, 255, 255)
        plan.append((lx0, ly0, lx1, ly1, fr, color, en))
    k = np.ones((3, 3), np.uint8)
    it = spec.get("erase_iter") or (8 if spec.get("glow") else (6 if spec.get("shadow") or spec.get("stroke") else 3))
    erase = cv2.dilate(full_mask, k, iterations=it) * 255
    clean = cv2.inpaint(np.array(cur.convert("RGB")), erase, 7, cv2.INPAINT_TELEA)
    out = Image.fromarray(clean).convert("RGBA")
    under = Image.new("RGBA", out.size, (0, 0, 0, 0))
    txt = Image.new("RGBA", out.size, (0, 0, 0, 0))
    align = spec.get("align", "center")
    def clean_en(t):
        return t.replace("■", "").replace("「", "").replace("」", "").replace("→", "") or "Ag"
    sizes = [fit_size(clean_en(en) if en else fr, ly1 - ly0) for lx0, ly0, lx1, ly1, fr, color, en in plan]
    common = int(np.median(sizes)) if spec.get("uniform", True) and sizes else None
    for (lx0, ly0, lx1, ly1, fr, color, en), own in zip(plan, sizes):
        size = max(6, int((common or own) * spec.get("scale", 1.0)))
        f, sym = font(size), ImageFont.truetype(SYMBOLS, int(size * 0.9))
        avail = {"center": W - 40, "left": W - lx0 - 20, "right": lx1 - 20}[align]
        while text_len(fr, f, sym) > avail and size > 6:
            size -= 1
            f, sym = font(size), ImageFont.truetype(SYMBOLS, int(size * 0.9))
        b = f.getbbox(clean_en(en) if en else fr, anchor="ls")
        baseline = ly1 - b[3]
        tl = text_len(fr, f, sym)
        x = {"center": (lx0 + lx1) / 2 - tl / 2, "left": lx0, "right": lx1 - tl}[align]
        if spec.get("glow"):
            draw_text(ImageDraw.Draw(under), x, baseline, fr, f, sym, fill=(255, 0, 0, 255), stroke_width=4, stroke_fill=(255, 0, 0, 255))
        if spec.get("shadow"):
            draw_text(ImageDraw.Draw(under), x + 2, baseline + 2, fr, f, sym, fill=(0, 0, 0, 255), stroke_width=3, stroke_fill=(0, 0, 0, 255))
        if spec.get("stroke"):
            draw_text(ImageDraw.Draw(txt), x, baseline, fr, f, sym, fill=color + (255,),
                      stroke_width=max(1, round(size / 12)), stroke_fill=(0, 0, 0, 255))
        else:
            draw_text(ImageDraw.Draw(txt), x, baseline, fr, f, sym, fill=color + (255,))
    if spec.get("glow") or spec.get("shadow"):
        out = Image.alpha_composite(out, under.filter(ImageFilter.GaussianBlur(6 if spec.get("glow") else 4)))
    return Image.alpha_composite(out, txt)


def render(path, spec):
    im = Image.open(path)
    mode = im.mode
    im = im.convert("RGB")
    orig = np.array(im).astype(int)
    cur = im
    for block in spec.get("blocks", [spec]):
        cur = render_block(orig, cur, block)
    return im, (cur.convert(mode) if mode in ("RGB", "RGBA", "L") else cur.convert("RGB"))


def main():
    spec_path, src, dst = sys.argv[1:4]
    preview = sys.argv[sys.argv.index("--preview") + 1] if "--preview" in sys.argv else None
    spec = json.load(open(spec_path, encoding="utf-8"))
    pairs = []
    for rel, s in spec.items():
        try:
            a, b = render(os.path.join(src, rel), s)
        except ValueError as e:
            print(f"ÉCHEC {rel}: {e}")
            continue
        p = os.path.join(dst, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        b.save(p, quality=95) if p.lower().endswith(".jpg") else b.save(p)
        pairs.append((rel, a, b))
    print(f"{len(pairs)}/{len(spec)} écrans générés dans {dst}")
    if preview and pairs:
        tw = 640
        rows = []
        for rel, a, b in pairs:
            r = tw / a.width
            rows.append((rel, a.convert("RGB").resize((tw, int(a.height * r))), b.convert("RGB").resize((tw, int(b.height * r)))))
        sheet = Image.new("RGB", (tw * 2 + 10, sum(x[1].height + 14 for x in rows)), (255, 0, 255))
        d = ImageDraw.Draw(sheet)
        y = 0
        for rel, a, b in rows:
            d.text((2, y), rel, fill=(0, 0, 0))
            sheet.paste(a, (0, y + 12))
            sheet.paste(b, (tw + 10, y + 12))
            y += a.height + 14
        sheet.save(preview)


if __name__ == "__main__":
    main()
