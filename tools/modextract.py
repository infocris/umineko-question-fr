#!/usr/bin/env python3
"""Extrait les segments anglais du script 07th-mod (CRLF) entre deux lignes (1-based, fin exclue).

  modextract.py <0.u> <ligne_debut> <ligne_fin> <sortie.jsonl>
Chaque ligne : {"id": n, "en": [segments], "voix": "but,kin", "ja": "texte japonais"}
(voix = préfixes des fichiers voix = locuteurs ; ja = work/ja.json produit par tools/jpalign.py).
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from umitl import to_tags  # noqa: E402
from modapply import split_line, MARK  # noqa: E402

src, a, b, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
JA = json.load(open(os.path.join(os.path.dirname(os.path.abspath(src)), "..", "work", "ja.json"), encoding="utf-8")) \
    if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(src)), "..", "work", "ja.json")) else {}
L = open(src, encoding="utf-8", newline="").read().split("\r\n")
n = 0
with open(out, "w", encoding="utf-8") as f:
    for i in range(a - 1, b - 1):
        l = L[i]
        if not l.startswith("langen"):
            continue
        parts, idx, _ = split_line(l[6:])
        if not idx:
            continue
        d = {"id": i + 1, "en": [to_tags(parts[k].replace(MARK, "")) for k in idx]}
        v = []
        for m in re.findall(r"dwave_eng \d+, *([a-z]+)_", l):
            if m not in v:
                v.append(m)
        if v:
            d["voix"] = ",".join(v)
        if str(i + 1) in JA:
            d["ja"] = JA[str(i + 1)]
        f.write(json.dumps(d, ensure_ascii=False) + "\n")
        n += 1
print(n, "lignes ->", out)
