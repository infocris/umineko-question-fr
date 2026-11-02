#!/usr/bin/env python3
"""Valide un lot traduit : tlcheck.py work/chunks/NN

Lit NN.en.jsonl et NN.fr.txt, écrit NN.fr.jsonl si tout est correct.
"""
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from umitl import check_seg  # noqa: E402

base = sys.argv[1]
en = [json.loads(l) for l in open(base + ".en.jsonl", encoding="utf-8") if l.strip()]
errors, fr = [], {}
for n, l in enumerate(open(base + ".fr.txt", encoding="utf-8"), 1):
    l = l.rstrip("\n")
    if not l.strip():
        continue
    if "|" not in l:
        errors.append(f"ligne {n}: pas de '|'")
        continue
    i, t = l.split("|", 1)
    try:
        i = int(i)
    except ValueError:
        errors.append(f"ligne {n}: id invalide {i!r}")
        continue
    if i in fr:
        errors.append(f"id {i}: en double")
    fr[i] = t.split("‖")

ids = [d["id"] for d in en]
missing = [i for i in ids if i not in fr]
extra = [i for i in fr if i not in set(ids)]
if missing:
    errors.append(f"ids manquants ({len(missing)}): {missing[:15]}")
if extra:
    errors.append(f"ids inconnus: {extra[:15]}")
for d in en:
    segs = fr.get(d["id"])
    if segs is None:
        continue
    if len(segs) != len(d["en"]):
        errors.append(f"id {d['id']}: {len(d['en'])} segments attendus, {len(segs)} reçus")
        continue
    for j, a in enumerate(d["en"]):
        # Espaces de tête/fin recalés automatiquement sur l'anglais (l'éditeur les perd souvent).
        lead = len(a) - len(a.lstrip(" "))
        b = " " * lead + segs[j].strip(" ")
        if a.endswith(" ") and a.strip():
            b += " "
        segs[j] = b
    for a, b in zip(d["en"], segs):
        e = check_seg(a, b)
        if "|" in b:
            e.append("'|' dans le texte")
        if e:
            errors.append(f"id {d['id']}: {', '.join(e)} :: {b[:60]!r}")
if errors:
    print(f"{len(errors)} ERREUR(S)")
    for e in errors[:60]:
        print("  ", e)
    sys.exit(1)
with open(base + ".fr.jsonl", "w", encoding="utf-8") as o:
    for d in en:
        o.write(json.dumps({"id": d["id"], "fr": fr[d["id"]]}, ensure_ascii=False) + "\n")
print(f"OK — {len(en)} lignes validées")
