#!/usr/bin/env python3
"""Valide les corrections d'un lot de relecture : fixcheck.py review/NN

Lit review/NN.jsonl (id, en, fr, ja) et review/NN.fix.txt (lignes `id|seg1‖seg2`,
uniquement les répliques corrigées ; lignes `#` = commentaires) ; écrit review/NN.fix.jsonl.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from umitl import check_seg  # noqa: E402

base = sys.argv[1]
rows = {d["id"]: d for d in map(json.loads, open(base + ".jsonl", encoding="utf-8"))}
errors, fixes = [], {}
p = base + ".fix.txt"
if not os.path.exists(p):
    sys.exit(f"{p} absent")
for n, l in enumerate(open(p, encoding="utf-8"), 1):
    l = l.rstrip("\n")
    if not l.strip() or l.startswith("#"):
        continue
    if "|" not in l:
        errors.append(f"ligne {n}: pas de '|'"); continue
    i, t = l.split("|", 1)
    try:
        i = int(i)
    except ValueError:
        errors.append(f"ligne {n}: id invalide {i!r}"); continue
    if i not in rows:
        errors.append(f"ligne {n}: id {i} hors du lot"); continue
    if i in fixes:
        errors.append(f"id {i}: en double")
    en = rows[i]["en"]
    segs = t.split("‖")
    if len(segs) != len(en):
        errors.append(f"id {i}: {len(en)} segments attendus, {len(segs)} reçus"); continue
    for j, a in enumerate(en):
        lead = len(a) - len(a.lstrip(" "))
        b = " " * lead + segs[j].strip(" ")
        if a.endswith(" ") and a.strip():
            b += " "
        segs[j] = b
    for a, b in zip(en, segs):
        e = check_seg(a, b)
        if "|" in b:
            e.append("'|' dans le texte")
        if e:
            errors.append(f"id {i}: {', '.join(e)} :: {b[:60]!r}")
    fixes[i] = segs
if errors:
    print(f"{len(errors)} ERREUR(S)")
    for e in errors[:60]:
        print("  ", e)
    sys.exit(1)
same = [i for i, s in fixes.items() if s == rows[i]["fr"]]
with open(base + ".fix.jsonl", "w", encoding="utf-8") as o:
    for i in sorted(fixes):
        if i not in same:
            o.write(json.dumps({"id": i, "fr": fixes[i]}, ensure_ascii=False) + "\n")
print(f"OK — {len(fixes) - len(same)} répliques corrigées ({len(same)} identiques ignorées) sur {len(rows)}")
