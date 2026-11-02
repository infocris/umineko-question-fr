#!/bin/sh
# Retire la traduction française d'Umineko (script + images).
# Prudent : ne touche qu'aux fichiers encore identiques à ceux installés par la traduction,
# pour ne rien casser si un autre patch (07th-mod…) a été installé entre-temps.
set -e
G="$HOME/Library/Application Support/Steam/steamapps/common/Umineko"
D="$(cd "$(dirname "$0")" && pwd)"

if [ -f "$G/0.utf.original-en" ] && [ "$(md5 -q "$G/0.utf")" = "$(cat "$D/work/0.fr.utf.md5")" ]; then
  cp "$G/0.utf.original-en" "$G/0.utf"
  echo "Script anglais restauré."
else
  echo "Script : 0.utf n'est pas la version française installée par la traduction — laissé tel quel."
fi

if [ -f "$G/0.u" ] && [ -f "$D/mod/0.u.fr.md5" ] && [ "$(md5 -q "$G/0.u")" = "$(cat "$D/mod/0.u.fr.md5")" ]; then
  cp "$D/mod/0.u.original" "$G/0.u"
  echo "Script du patch 07th-mod (0.u) remis en anglais."
fi

n=0; k=0
while read -r sum f; do
  [ -z "$f" ] && continue
  if [ -f "$G/$f" ] && [ "$(md5 -q "$G/$f")" = "$sum" ]; then rm -f "$G/$f"; n=$((n+1)); else k=$((k+1)); fi
done < "$D/ui/installed_files.md5"
find "$G/en" "$G/bmp" -type d -empty -delete 2>/dev/null || true
echo "Images françaises retirées : $n (laissées car modifiées ou absentes : $k)."

# Version 07th-mod : remet les images anglaises du patch (sauvegardées dans ui/mod_original).
if [ -f "$D/ui/installed_files_mod.md5" ]; then
  r=0
  while read -r sum f; do
    [ -z "$f" ] && continue
    if [ -f "$G/$f" ] && [ "$(md5 -q "$G/$f")" = "$sum" ] && [ -f "$D/ui/mod_original/$f" ]; then
      cp "$D/ui/mod_original/$f" "$G/$f"; r=$((r+1))
    fi
  done < "$D/ui/installed_files_mod.md5"
  echo "Images anglaises du patch remises : $r."
fi
