#!/usr/bin/env python3
"""Outils de traduction des dialogues anglais (lignes `langen`) du script Umineko (0.utf).

  extract <script> <label_debut> <label_fin> <sortie.jsonl>
      Extrait les segments de texte des lignes langen entre deux labels (*umi1_1 ... *umi1_2).
      Chaque ligne JSON : {"id": n°_de_ligne, "en": [segments]}

  apply <script> <traductions.jsonl>... -o <sortie>
      Réinjecte les traductions ({"id": n, "fr": [segments]}) après validation.

Format d'une ligne langen : langen^texte^ctrl^texte^ctrl...  (indices impairs = texte).
Les codes couleur #fefefe…#ffffff dans le texte deviennent <i>…</i> pour le traducteur.
"""
import json, re, sys

COLOR_ON, COLOR_OFF = "#fefefe", "#ffffff"
TRAIL = re.compile(r"[@\\/]+$")


def split_line(body):
    """body = ligne sans le préfixe 'langen'. Renvoie (parts, indices_texte, suffixe_ctrl)."""
    parts = body.split("^")
    suffix = ""
    # Ligne à ^ non fermé : le dernier segment texte embarque des codes de fin.
    if len(parts) % 2 == 0:
        m = TRAIL.search(parts[-1])
        if m:
            suffix = m.group(0)
            parts[-1] = parts[-1][: m.start()]
    idx = [i for i in range(1, len(parts), 2) if parts[i].strip()]
    return parts, idx, suffix


def to_tags(s):
    return s.replace(COLOR_ON, "<i>").replace(COLOR_OFF, "</i>")


def from_tags(s):
    return s.replace("<i>", COLOR_ON).replace("</i>", COLOR_OFF)


def read_lines(path):
    with open(path, encoding="utf-8", newline="") as f:
        return f.read().split("\n")


def label_range(lines, start, end):
    s = lines.index("*" + start)
    e = lines.index("*" + end) if end != "EOF" else len(lines)
    return s, e


def extract(script, start, end, out):
    lines = read_lines(script)
    s, e = label_range(lines, start, end)
    n = 0
    with open(out, "w", encoding="utf-8") as f:
        for i in range(s, e):
            l = lines[i]
            if not l.startswith("langen"):
                continue
            parts, idx, _ = split_line(l[6:])
            if not idx:
                continue
            f.write(json.dumps({"id": i + 1, "en": [to_tags(parts[k]) for k in idx]}, ensure_ascii=False) + "\n")
            n += 1
    print(f"{n} lignes extraites ({start} -> {end}) vers {out}")


def check_seg(en, fr):
    errs = []
    if fr.count("<i>") != en.count("<i>") or fr.count("</i>") != en.count("</i>"):
        errs.append("balises <i> différentes")
    if fr.lower().count("#ff0000") != en.lower().count("#ff0000"):
        errs.append("code rouge #ff0000 différent")
    if "ᵉ" in fr:
        errs.append("caractère ᵉ absent des polices du jeu (écrire 19e)")
    if fr.count("~") != en.count("~"):
        errs.append("balises ~ différentes")
    if re.search(r"[\^@\\]", fr):
        errs.append("caractère de contrôle (^ @ \\) dans la traduction")
    if fr.strip() == "":
        errs.append("segment vide")
    lead = len(en) - len(en.lstrip(" "))
    if lead and not fr.startswith(" " * lead):
        errs.append("espaces de tête perdus")
    if en.endswith(" ") and not fr.endswith(" "):
        errs.append("espace final perdu")
    return errs


def apply(script, tl_files, out):
    lines = read_lines(script)
    tl = {}
    for p in tl_files:
        with open(p, encoding="utf-8") as f:
            for ln in f:
                if ln.strip():
                    d = json.loads(ln)
                    tl[d["id"]] = d["fr"]
    errors, done = [], 0
    for lid, fr in sorted(tl.items()):
        l = lines[lid - 1]
        if not l.startswith("langen"):
            errors.append(f"{lid}: n'est pas une ligne langen")
            continue
        parts, idx, suffix = split_line(l[6:])
        if len(fr) != len(idx):
            errors.append(f"{lid}: {len(idx)} segments attendus, {len(fr)} reçus")
            continue
        bad = False
        for k, seg in zip(idx, fr):
            e = check_seg(to_tags(parts[k]), seg)
            if e:
                errors.append(f"{lid}: {', '.join(e)} :: {seg[:70]}")
                bad = True
        if bad:
            continue
        for k, seg in zip(idx, fr):
            parts[k] = from_tags(seg)
        lines[lid - 1] = "langen" + "^".join(parts) + suffix
        done += 1
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(lines))
    print(f"{done} lignes traduites appliquées, {len(errors)} rejetées -> {out}")
    for e in errors[:50]:
        print("  ERREUR", e)
    return 1 if errors else 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "extract" and len(a) == 5:
        extract(*a[1:])
    elif a and a[0] == "apply" and "-o" in a:
        o = a.index("-o")
        sys.exit(apply(a[1], a[2:o], a[o + 1]))
    else:
        print(__doc__)
        sys.exit(2)
