#!/usr/bin/env python3
"""Lecture d'archives NSA (ONScripter).

  list <arc.nsa> [motif]
  extract <arc.nsa> <dossier_sortie> <motif>   (motif = sous-chaîne, insensible à la casse)

Seules les entrées non compressées (type 0) sont extraites, ce qui couvre les PNG.
"""
import os, struct, sys


def read_index(path):
    with open(path, "rb") as f:
        count, base = struct.unpack(">HI", f.read(6))
        entries = []
        for _ in range(count):
            name = b""
            while (c := f.read(1)) != b"\0":
                name += c
            ctype, off, length, orig = struct.unpack(">BIII", f.read(13))
            entries.append((name.decode("cp932", "replace"), ctype, base + off, length, orig))
    return entries


def main(a):
    if a[0] == "list":
        pat = (a[2] if len(a) > 2 else "").lower()
        for n, t, o, l, _ in read_index(a[1]):
            if pat in n.lower():
                print(f"{t} {l:>9} {n}")
    elif a[0] == "extract":
        arc, out, pat = a[1], a[2], a[3].lower()
        with open(arc, "rb") as f:
            for n, t, o, l, _ in read_index(arc):
                if pat not in n.lower():
                    continue
                if t != 0:
                    print("compressé, ignoré:", n)
                    continue
                rel = n.replace("\\", "/")
                if rel.startswith("/") or ".." in rel.split("/"):
                    print("chemin suspect, ignoré:", n)
                    continue
                dst = os.path.join(out, rel)
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                f.seek(o)
                with open(dst, "wb") as w:
                    w.write(f.read(l))
                print("extrait:", rel)
    else:
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
