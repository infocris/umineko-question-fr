# Umineko (Question Arcs) — traduction française amateur

Usage personnel. Traduction des dialogues (lignes `langen` du script) et des images d'interface.

- `STYLE.md` : guide de traduction, glossaire, choix fixés.
- `tools/` : extraction / validation / injection du script, retouche des images.
- `work/` : traductions des dialogues (`chunks/` = épisode 1 jeu d'origine, `ep2/` = épisode 2
  et Tea Parties 1-2 sur le script 07th-mod), fiches et Infos (`pages/fr/`).
- `review/` : relecture contre le japonais (`NN.jsonl` = lot, `NN.fix.txt` = corrections justifiées,
  `MISSION.md` = consignes et remarques récurrentes) ; `tools/jpalign.py` associe le japonais.
- `mod/` : portage sur le script 07th-mod (`0.u`) — alignement épisode 1.
- `ui/*.txt`, `ui/*.md5` : manifestes des images installées (les images ne sont pas versionnées).
- `desinstaller.sh` : remet le jeu en anglais.

Non versionnés (fichiers du jeu ou régénérables) : scripts d'origine, `0.u` français,
images extraites et générées.

Reconstruire le script 07th-mod français (traductions puis corrections de `review/`, dans l'ordre de `mod/translations.txt`) :

    python3 -I tools/modapply.py mod/0.u.original $(grep -v '^#' mod/translations.txt) -o mod/0.u.fr

## Distribution via le 07th-mod Installer

Même principe que la traduction italienne (Beyond The Ataraxia) : une archive extraite à la
racine du jeu **après** le patch 07th-mod, qui remplace le script `0.u` et des images.

- `patch/` : images françaises, arborescence = dossier du jeu (`en/…`, `bmp/…`).
- `mod/BASE.txt` : version du script 07th-mod sur laquelle les traductions sont alignées
  (tag + md5). `mod/translations.txt` : fichiers de traduction injectés, dans l'ordre.
- `tools/package.py` : construit `dist/umineko-question-fr.zip` (0.u français + `patch/`) à
  partir du `0.u` anglais du jeu ; refuse si ce n'est pas la version de `BASE.txt`.
- `installer/installData-entry.json` : entrée à proposer dans `installData.json` du
  [python-patcher](https://github.com/07th-mod/python-patcher), groupe « Translations » de
  « Umineko Question (Ch. 1-4) », sous-mod `full`.

Publier une version :

    python3 -I tools/package.py "<dossier du jeu>/0.u"   # 0.u anglais 07th-mod, ou mod/0.u.original
    # puis créer une release GitHub et y joindre dist/umineko-question-fr.zip
    # (URL stable : releases/latest/download/umineko-question-fr.zip)

Installation manuelle : installer le patch 07th-mod, puis extraire l'archive dans le dossier
du jeu en remplaçant les fichiers.

Si 07th-mod met à jour son script (`0.u.version.txt` du jeu ≠ tag de `BASE.txt`), réaligner
les traductions sur le nouveau script (comme pour le portage de l'épisode 1, voir
`mod/align_ep1.json`) puis mettre à jour `BASE.txt`.
