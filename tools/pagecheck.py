#!/usr/bin/env python3
"""Vérifie les traductions d'un lot de pages : pagecheck.py work/pages/batches/N.md"""
import os, re, sys

ALLOWED = re.compile(r"^[\sA-Za-z0-9À-ÖØ-öø-ÿŒœÆæ.,;:!?'’\"«»()\[\]\-–—…/&%*+=#°$@_~]*$")
batch = open(sys.argv[1], encoding="utf-8").read()
entries = re.findall(r"## (\w+)\n.*?type: (\w+)\n.*?sortie: (\S+)", batch, re.S)
errors = []
for h, kind, out in entries:
    if not os.path.exists(out):
        errors.append(f"{h}: fichier manquant {out}")
        continue
    txt = open(out, encoding="utf-8").read().strip("\n")
    if not txt.strip():
        errors.append(f"{h}: vide")
        continue
    lines = txt.split("\n")
    if kind == "cha" and not lines[0].startswith("# "):
        errors.append(f"{h}: la première ligne d'une fiche doit être le titre '# Nom'")
    for i, l in enumerate(lines, 1):
        if "ᵉ" in l:
            errors.append(f"{h}:{i}: caractère ᵉ interdit")
        elif not ALLOWED.match(l):
            bad = sorted({c for c in l if not ALLOWED.match(c)})
            errors.append(f"{h}:{i}: caractères non pris en charge {bad}")
        if len(l) > 400:
            errors.append(f"{h}:{i}: ligne très longue ({len(l)} car.) — paragraphe à scinder ?")
if errors:
    print(f"{len(errors)} ERREUR(S)")
    for e in errors[:50]:
        print("  ", e)
    sys.exit(1)
print(f"OK — {len(entries)} pages")
