#!/usr/bin/env python3
"""Injecte des traductions dans le script 07th-mod (0.u, fins de ligne CRLF).

  modapply.py <0.u source> <traductions.jsonl>... -o <0.u sortie>

Chaque traduction : {"id": n° de ligne (1-based) dans 0.u, "fr": [segments]}
ou {"id": n, "line": "ligne complète"} pour les lignes aux ^ mal formés.
Les lignes ressemblent à : langen:dwave_eng 0, nan_1e1:^texte^@:dwave_eng 0, nan_1e2:^texte^\\
Seuls les segments de texte (entre ^…^) sont remplacés ; commandes de voix, codes et
marqueur U+0010 de début de segment sont conservés.
"""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from umitl import check_seg, to_tags, from_tags  # noqa: E402

TRAIL = re.compile(r"[@\\/]+$")
MARK = "\x10"


def split_line(body):
    parts = body.split("^")
    suffix = ""
    if len(parts) % 2 == 0:
        m = TRAIL.search(parts[-1])
        if m:
            suffix = m.group(0)
            parts[-1] = parts[-1][: m.start()]
    idx = [i for i in range(1, len(parts), 2) if parts[i].strip(" " + MARK)]
    return parts, idx, suffix


def main(a):
    o = a.index("-o")
    src, files, out = a[0], a[1:o], a[o + 1]
    lines = open(src, encoding="utf-8", newline="").read().split("\r\n")
    tl = {}
    for p in files:
        for ln in open(p, encoding="utf-8"):
            if ln.strip():
                d = json.loads(ln)
                tl[d["id"]] = d["fr"] if "fr" in d else {"line": d["line"]}
    errors, done = [], 0
    for lid, fr in sorted(tl.items()):
        l = lines[lid - 1]
        if isinstance(fr, dict):  # ligne entière (^ mal formés dans le script anglais)
            lines[lid - 1] = fr["line"]
            done += 1
            continue
        if not l.startswith("langen"):
            errors.append(f"{lid}: pas une ligne langen")
            continue
        parts, idx, suffix = split_line(l[6:])
        if len(fr) != len(idx):
            errors.append(f"{lid}: {len(idx)} segments attendus, {len(fr)} reçus")
            continue
        new, bad = [], False
        for k, seg in zip(idx, fr):
            en = parts[k]
            seg = seg.replace(MARK, "")
            lead = MARK if en.startswith(MARK) else ""
            e = check_seg(to_tags(en.replace(MARK, "")), seg)
            if e:
                errors.append(f"{lid}: {', '.join(e)} :: {seg[:60]}")
                bad = True
            new.append(lead + from_tags(seg))
        if bad:
            continue
        for k, seg in zip(idx, new):
            parts[k] = seg
        lines[lid - 1] = "langen" + "^".join(parts) + suffix
        done += 1
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write("\r\n".join(lines))
    print(f"{done} lignes appliquées, {len(errors)} rejetées -> {out}")
    for e in errors[:40]:
        print("  ERREUR", e)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
