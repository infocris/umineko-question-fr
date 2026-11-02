#!/usr/bin/env python3
"""Associe à chaque ligne langen du script 07th-mod le texte japonais (langjp) correspondant.

  jpalign.py <0.u> <sortie.json>   -> {"<id langen>": "texte japonais", ...}

Le script alterne des blocs de lignes langjp puis langen. Si un bloc a autant de lignes
des deux côtés, appariement 1-1 ; sinon chaque ligne anglaise reçoit tout le bloc japonais.
"""
import json, re, sys

src, out = sys.argv[1], sys.argv[2]
L = open(src, encoding="utf-8", newline="").read().split("\r\n")


def clean(l):
    l = l[6:]
    l = re.sub(r":?dwave_jp [^:]*:", "", l)
    l = re.sub(r"#[0-9a-fA-F]{6}", "", l)
    l = re.sub(r"[@\\/]+$", "", l)
    l = l.replace("@", " ").replace("\\", " ").replace("\x10", "")
    return l.strip(" 　")


res, jp, en, prev = {}, [], [], None


def flush():
    if en:
        if len(jp) == len(en):
            for i, j in zip(en, jp):
                res[str(i)] = j
        else:
            for i in en:
                res[str(i)] = " / ".join(jp)


for n, l in enumerate(L, 1):
    if l.startswith("langjp"):
        if prev == "en":
            flush()
            jp, en = [], []
        jp.append(clean(l))
        prev = "jp"
    elif l.startswith("langen"):
        en.append(n)
        prev = "en"
flush()
json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False)
print(len(res), "lignes anglaises associées")
