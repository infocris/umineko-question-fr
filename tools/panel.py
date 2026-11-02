#!/usr/bin/env python3
"""Réécrit les encadrés de texte de l'écran titre (texte clair sur fond sombre).

  panel.py <spec.json> <dossier_source> <dossier_sortie> [--preview fichier.png]

spec.json : { "chemin.png": {"title": "Titre" | null, "subtitle": "..." (optionnel),
                              "paras": ["paragraphe", ...]} }
Le texte d'origine est effacé (inpainting), puis le français est posé avec la
même marge, la même position de titre et le même interligne, avec retour à la
ligne automatique.
"""
import json, os, sys
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

REG = "/System/Library/Fonts/Supplemental/Times New Roman.ttf"
LEFT, RIGHT_MARGIN, PITCH = 29, 24, 21.6


def lines_of(mask):
    rows = mask.any(axis=1)
    out, y = [], 0
    while y < len(rows):
        if rows[y]:
            s = y
            while y < len(rows) and rows[y]:
                y += 1
            out.append((s, y))
        y += 1
    return out


def wrap(text, f, width):
    words, lines, cur = text.split(" "), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if f.getlength(t) <= width or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def render(src, spec):
    im = Image.open(src).convert("RGBA")
    a = np.array(im)
    lum = a[..., :3].max(axis=2)
    mask = ((lum > 45) & (a[..., 3] > 0)).astype(np.uint8)
    rows = lines_of(mask)
    color = tuple(int(c) for c in np.median(a[..., :3][lum > 150], axis=0))
    erase = cv2.dilate(mask, np.ones((3, 3), np.uint8), iterations=3) * 255
    rgb = cv2.inpaint(np.ascontiguousarray(a[..., :3]), erase, 4, cv2.INPAINT_TELEA)
    al = cv2.inpaint(np.ascontiguousarray(a[..., 3]), erase, 4, cv2.INPAINT_TELEA)
    out = Image.fromarray(np.dstack([rgb, al]), "RGBA")
    d = ImageDraw.Draw(out)
    k = im.width / 560
    LEFT_, PITCH_ = round(29 * k), 21.6 * k
    width = im.width - LEFT_ - round(24 * k)
    fbody, ftitle = ImageFont.truetype(REG, round(17 * k)), ImageFont.truetype(REG, round(22 * k))
    # Repères d'origine : la première ligne donne la position du titre.
    top = rows[0][0]
    y = top + 15 * k
    if spec.get("title"):
        d.text((LEFT_, y), spec["title"], font=ftitle, fill=color, anchor="ls")
        y += 28 * k
        if spec.get("subtitle"):
            d.text((LEFT_, y), spec["subtitle"], font=ftitle, fill=color, anchor="ls")
        y = top + (15 + 28 * (2 if spec.get("subtitle") else 1) + 26) * k
    body = []
    for i, p in enumerate(spec["paras"]):
        if i:
            body.append("")
        body += wrap(p, fbody, width)
    pitch = PITCH_
    while y + pitch * (len(body) - 1) > im.height - 14 * k and pitch > 16 * k:
        pitch -= 0.5
    for i, line in enumerate(body):
        if line:
            d.text((LEFT_, y + i * pitch), line, font=fbody, fill=color, anchor="ls")
    return im, out


def main():
    spec_path, src, dst = sys.argv[1:4]
    preview = sys.argv[sys.argv.index("--preview") + 1] if "--preview" in sys.argv else None
    spec = json.load(open(spec_path, encoding="utf-8"))
    pairs = []
    for rel, s in spec.items():
        a, b = render(os.path.join(src, rel), s)
        p = os.path.join(dst, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        b.save(p)
        pairs.append((rel, a, b))
    print(f"{len(pairs)} encadrés générés dans {dst}")
    if preview:
        w, h = pairs[0][1].size
        sheet = Image.new("RGB", (w * 2 + 10, len(pairs) * (h + 14)), (40, 40, 60))
        dd = ImageDraw.Draw(sheet)
        for i, (rel, a, b) in enumerate(pairs):
            y = i * (h + 14)
            dd.text((2, y), rel, fill=(255, 255, 0))
            sheet.paste(a, (0, y + 12), a)
            sheet.paste(b, (w + 10, y + 12), b)
        sheet.save(preview)


if __name__ == "__main__":
    main()
