#!/usr/bin/env python3
"""Construit l'archive de la traduction française pour le 07th-mod Installer.

  python3 -I tools/package.py <0.u anglais 07th-mod> [-o dist/umineko-question-fr.zip]

- Vérifie que le script anglais est bien celui sur lequel les traductions sont alignées
  (mod/BASE.txt) ; refuse sinon (lignes décalées = texte au mauvais endroit).
- Injecte les traductions listées dans mod/translations.txt (tools/modapply.py).
- Ajoute les images françaises de patch/ (arborescence = dossier du jeu).
- Produit une archive à extraire telle quelle à la racine du dossier du jeu, après le
  patch 07th-mod : c'est ce que fait l'installer (option « Translations »).
"""
import hashlib, os, subprocess, sys, tempfile, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAPTION = 'caption "Umineko: When The Seagulls Cry - traduction française"'


def conf(path):
    return [l.strip() for l in open(os.path.join(ROOT, path), encoding="utf-8")
            if l.strip() and not l.startswith("#")]


def main(a):
    if not a or a[0].startswith("-"):
        print(__doc__)
        return 2
    src = a[0]
    out = a[a.index("-o") + 1] if "-o" in a else os.path.join(ROOT, "dist", "umineko-question-fr.zip")
    base = dict(l.split("=", 1) for l in conf("mod/BASE.txt"))
    md5 = hashlib.md5(open(src, "rb").read()).hexdigest()
    if md5 != base["md5"]:
        print(f"ERREUR : {src} n'est pas le script 07th-mod {base['tag']} attendu "
              f"(md5 {md5} au lieu de {base['md5']}). Réaligner les traductions d'abord.")
        return 1
    with tempfile.TemporaryDirectory() as tmp:
        script = os.path.join(tmp, "0.u")
        files = [os.path.join(ROOT, p) for p in conf("mod/translations.txt")]
        r = subprocess.run([sys.executable, "-I", os.path.join(ROOT, "tools", "modapply.py"), src, *files,
                            "-o", script], capture_output=True, text=True)
        print(r.stdout.strip())
        if r.returncode:
            print(r.stderr)
            return 1
        data = open(script, encoding="utf-8", newline="").read()
        old = 'caption "Umineko: When The Seagulls Cry"'
        if old in data:
            data = data.replace(old, CAPTION, 1)
        os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
        n = 0
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            z.writestr("0.u", data.encode("utf-8"))
            pdir = os.path.join(ROOT, "patch")
            for dp, _, fns in sorted(os.walk(pdir)):
                for fn in sorted(fns):
                    if fn.startswith("."):
                        continue
                    p = os.path.join(dp, fn)
                    z.write(p, os.path.relpath(p, pdir))
                    n += 1
    print(f"{out} : 0.u + {n} images ({os.path.getsize(out) / 1e6:.1f} Mo)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
