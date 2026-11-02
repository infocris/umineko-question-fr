#!/usr/bin/env python3
"""Remplace le texte d'images de boutons Umineko (texte clair + ombre portée).

  retext.py <spec.json> <dossier_source> <dossier_sortie> [--preview fichier.png]

spec.json : { "chemin/relatif.png": {"en": "Save", "fr": "Sauver", "frames": 2}, ... }
Chaque image est découpée en `frames` cases horizontales (normal / survol).
Dans chaque case : détection du texte clair, effacement (inpainting), puis
réécriture en français, même hauteur de capitales, même alignement, même couleur.
"""
import json, os, sys
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONT = "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf"


def font(size):
    return ImageFont.truetype(FONT, size)


def detect_text(rgb, alpha):
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    m = ((hsv[..., 2] > 225) & (hsv[..., 1] < 70) & (alpha > 230)).astype(np.uint8)
    n, lab, stats, _ = cv2.connectedComponentsWithStats(m, 8)
    keep = np.zeros_like(m)
    for i in range(1, n):
        if stats[i, cv2.CC_STAT_AREA] >= 4:
            keep[lab == i] = 1
    ys, xs = np.nonzero(keep)
    if len(xs) == 0:
        return None, None
    return keep, (xs.min(), ys.min(), xs.max() + 1, ys.max() + 1)


def size_for_cap_height(text, target_h):
    lo, hi = 4, 200
    while lo < hi:
        mid = (lo + hi + 1) // 2
        b = font(mid).getbbox(text, anchor="ls")
        if b[3] - b[1] <= target_h:
            lo = mid
        else:
            hi = mid - 1
    return lo


def process_frame(frame, en, fr, ref=None):
    """frame : PIL RGBA. ref : boîte (x0,y0,x1,y1) détectée sur la case de référence.
    Renvoie (case retraitée, boîte utilisée)."""
    arr = np.array(frame)
    rgb, alpha = arr[..., :3].copy(), arr[..., 3].copy()
    mask, box = detect_text(rgb, alpha)
    if ref is not None:
        # Ne garder que les pixels clairs situés dans la boîte du texte de référence.
        x0, y0, x1, y1 = ref
        lim = np.zeros_like(mask) if mask is not None else np.zeros(rgb.shape[:2], np.uint8)
        lim[max(0, y0 - 2):y1 + 2, max(0, x0 - 2):x1 + 2] = 1
        mask = (mask if mask is not None else lim * 0) * lim
        box = ref
    if box is None or mask.sum() == 0:
        raise ValueError("aucun texte détecté")
    x0, y0, x1, y1 = box
    h, w = rgb.shape[:2]
    color = tuple(int(c) for c in np.median(rgb[mask == 1], axis=0))
    sh = max(2, round((y1 - y0) / 12))
    k = np.ones((3, 3), np.uint8)
    big = cv2.dilate(mask, k, iterations=3)
    shifted = np.zeros_like(big)
    shifted[sh:, sh:] = big[:-sh, :-sh]
    erase = cv2.dilate(np.maximum(big, shifted), k, iterations=1)
    clean = cv2.inpaint(rgb, erase * 255, 6, cv2.INPAINT_TELEA)
    alpha = cv2.inpaint(alpha, erase * 255, 6, cv2.INPAINT_TELEA)
    en_lines, fr_lines = en.split("\n"), fr.split("\n")
    n = len(en_lines)
    line_h = (y1 - y0) / n
    # Hauteur d'une ligne anglaise (capitales + jambages) ≈ boîte / nb de lignes, moins l'interligne.
    size = size_for_cap_height(max(en_lines, key=len), line_h * (0.66 if n > 1 else 1))
    eb = font(size).getbbox(en_lines[0], anchor="ls")
    first_baseline = y0 - eb[1]
    lm, rm = x0, w - x1
    centered = n > 1 or (abs(lm - rm) < 0.25 * max(lm, rm, 1) and lm > 0.05 * w)
    right_aligned = not centered and (x0 + x1) / 2 > w * 0.5 and rm < lm
    if centered:
        avail = w - 2 * min(lm, rm) + 8
    else:
        avail = (x1 - 6) if right_aligned else (w - x0 - 6)
    f = font(size)
    while max(f.getlength(t) for t in fr_lines) > avail and size > 6:
        size -= 1
        f = font(size)
    pitch = line_h if n > 1 else 0
    if len(fr_lines) != n:
        pitch = (y1 - y0) / len(fr_lines)
        first_baseline = y0 + pitch * 0.8
    out = Image.fromarray(np.dstack([clean, alpha]), "RGBA")
    shadow = Image.new("RGBA", out.size, (0, 0, 0, 0))
    layer_txt = []
    for k, t in enumerate(fr_lines):
        tw = f.getlength(t)
        if centered:
            x = (x0 + x1) / 2 - tw / 2
        elif right_aligned:
            x = x1 - tw
        else:
            x = x0 - eb[0]
        layer_txt.append((x, first_baseline + k * pitch, t))
        ImageDraw.Draw(shadow).text((x + sh, first_baseline + k * pitch + sh), t, font=f, fill=(0, 0, 0, 220), anchor="ls")
    shadow = shadow.filter(ImageFilter.GaussianBlur(max(1, sh / 2)))
    layer = Image.alpha_composite(Image.new("RGBA", out.size, (0, 0, 0, 0)), shadow)
    for x, yb, t in layer_txt:
        ImageDraw.Draw(layer).text((x, yb), t, font=f, fill=color + (255,), anchor="ls")
    # Le texte reste opaque même au-dessus des ornements ajourés.
    la = np.array(layer)[..., 3]
    base = out.copy()
    base.putalpha(255)
    merged = Image.alpha_composite(base, layer)
    merged.putalpha(Image.fromarray(np.maximum(alpha, la).astype(np.uint8)))
    return merged, box


def process_alpha_frame(frame, en, fr):
    arr = np.array(frame)
    a = arr[..., 3]
    ys, xs = np.nonzero(a > 40)
    if len(xs) == 0:
        raise ValueError("case vide")
    x0, y0, x1, y1 = xs.min(), ys.min(), xs.max() + 1, ys.max() + 1
    rgb = arr[..., :3].astype(int)
    lum = rgb.max(axis=2)
    inner = (a > 200) & (lum > np.percentile(lum[a > 200], 60))
    color = tuple(int(c) for c in np.median(arr[..., :3][inner], axis=0))
    dark = (a > 200) & (lum < 60)
    stroke_col = tuple(int(c) for c in np.median(arr[..., :3][dark], axis=0)) if dark.sum() > 20 else (20, 20, 20)
    w = arr.shape[1]
    stroke = max(1, round((y1 - y0) / 16))
    size = int(frame.height * 0.68)
    f = font(size)
    eb = f.getbbox(en, anchor="ls")
    baseline = y0 + stroke - eb[1]
    lm, rm = x0, w - x1
    centered = abs(lm - rm) < 0.3 * max(lm, rm, 1)
    right_aligned = not centered and rm < lm
    avail = w - 4 if centered else ((x1 - 2) if right_aligned else (w - x0 - 2))
    while f.getlength(fr) + 2 * stroke > avail and size > 6:
        size -= 1
        f = font(size)
    tw = f.getlength(fr)
    x = (x0 + x1) / 2 - tw / 2 if centered else ((x1 - stroke - tw) if right_aligned else x0 + stroke - eb[0])
    out = Image.new("RGBA", frame.size, (0, 0, 0, 0))
    ImageDraw.Draw(out).text((x, baseline), fr, font=f, fill=color + (255,), anchor="ls",
                             stroke_width=stroke, stroke_fill=stroke_col + (255,))
    return out


def main():
    spec_path, src, dst = sys.argv[1:4]
    preview = sys.argv[sys.argv.index("--preview") + 1] if "--preview" in sys.argv else None
    spec = json.load(open(spec_path, encoding="utf-8"))
    done, rows = 0, []
    for rel, s in spec.items():
        if not os.path.exists(os.path.join(src, rel)):
            print(f"absente : {rel}")
            continue
        im = Image.open(os.path.join(src, rel))
        mode = im.mode
        im = im.convert("RGBA")
        n = s.get("frames", 2)
        fw = im.width // n
        out = Image.new("RGBA", im.size)
        try:
            ref = None
            if s.get("mode") == "alpha":
                for i in range(n):
                    out.paste(process_alpha_frame(im.crop((i * fw, 0, (i + 1) * fw, im.height)), s["en"], s["fr"]), (i * fw, 0))
            for i in (range(n) if s.get("mode") != "alpha" else []):
                fr_img, box = process_frame(im.crop((i * fw, 0, (i + 1) * fw, im.height)), s["en"], s["fr"], ref)
                ref = ref or box
                out.paste(fr_img, (i * fw, 0))
        except ValueError as e:
            print(f"ÉCHEC {rel}: {e}")
            continue
        p = os.path.join(dst, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        (out if mode == "RGBA" else out.convert(mode)).save(p)
        rows.append((rel, im, out))
        done += 1
    print(f"{done}/{len(spec)} images générées dans {dst}")
    if preview:
        W = max(r[1].width for r in rows) * 2 + 10
        H = sum(r[1].height + 14 for r in rows)
        sheet = Image.new("RGB", (W, H), (40, 40, 60))
        d = ImageDraw.Draw(sheet)
        y = 0
        for rel, a, b in rows:
            d.text((2, y), rel, fill=(255, 255, 0))
            y += 12
            sheet.paste(a, (0, y), a)
            sheet.paste(b, (a.width + 10, y), b)
            y += a.height + 2
        sheet.save(preview)


if __name__ == "__main__":
    main()
