# Umineko (Question Arcs) — traduction française amateur

Usage personnel. Traduction des dialogues (lignes `langen` du script) et des images d'interface.

- `STYLE.md` : guide de traduction, glossaire, choix fixés.
- `tools/` : extraction / validation / injection du script, retouche des images.
- `work/` : traductions des dialogues (`chunks/` = épisode 1 jeu d'origine, `ep2/` = épisode 2
  et Tea Parties 1-2 sur le script 07th-mod), fiches et Infos (`pages/fr/`).
- `mod/` : portage sur le script 07th-mod (`0.u`) — alignement épisode 1.
- `ui/*.txt`, `ui/*.md5` : manifestes des images installées (les images ne sont pas versionnées).
- `desinstaller.sh` : remet le jeu en anglais.

Non versionnés (fichiers du jeu ou régénérables) : scripts d'origine, `0.u` français,
images extraites et générées.

Reconstruire le script 07th-mod français :

    python3 -I tools/modapply.py mod/0.u.original mod/direct_ep1.fr.jsonl mod/todo111.fr.jsonl mod/special_ep1.fr.jsonl \
      work/ep2/??.fr.jsonl -o mod/0.u.fr
