# Umineko When They Cry – Question Arcs: French translation

An amateur French translation of *Umineko When They Cry – Question Arcs* (Steam app 406550) on
top of the [07th-mod](https://07th-mod.com/) patch: the PS3 voices and graphics stay in place.
Only the text changes.

**Status**

| Part | State |
|---|---|
| Episode 1 (*Legend of the Golden Witch*), Tea Party, ???? | translated, reviewed against the Japanese |
| Episode 2 (*Turn of the Golden Witch*), Tea Party, ???? | translated, reviewed against the Japanese |
| Episode 3 (*Banquet of the Golden Witch*), Tea Party, ???? | translated (Japanese used as reference), not yet reviewed against the Japanese |
| Episode 4 (*Alliance of the Golden Witch*), Tea Party, ???? | translated (Japanese used as reference), not yet reviewed against the Japanese |
| Menus, buttons, title screen, date and notice screens | translated (388 images) |
| Character profiles and Tips pages | translated (from OCR of the English pages) |

The translation is AI-assisted: it was first made from the official English (MangaGamer) text,
then checked line by line against the original Japanese. Nothing has been proofread by a human
yet, and the result has not been fully play-tested in-game.

## Installing

1. Install the game from Steam, GOG or MangaGamer.
2. Install the 07th-mod patch for the Question Arcs with the
   [07th-mod Installer](https://github.com/07th-mod/python-patcher/releases/latest).
3. Download `umineko-question-fr.zip` from the
   [latest release](https://github.com/infocris/umineko-question-fr/releases/latest) and extract it
   into the game folder (for example `Steam/steamapps/common/Umineko`), replacing files.

Rerunning the 07th-mod installer later overwrites the script and images. Extract the archive
again afterwards.

The archive is built for one specific 07th-mod script version (see `mod/BASE.txt`). If 07th-mod
ships a newer script, the translation has to be realigned first (see
[docs/WORKFLOW.md](docs/WORKFLOW.md#when-07th-mod-updates-its-script)).

## Repository layout

```
STYLE.md                 translation guide, glossary and fixed choices (in French, for translators)
tools/                   all scripts (Python 3; Pillow, NumPy, OpenCV for images)
mod/                     everything tied to the 07th-mod script
  BASE.txt               07th-mod script version the translations are aligned to (tag + md5)
  translations.txt       ordered list of translation files injected into the script
  direct_ep1.fr.jsonl    Episode 1, ported from the original-game translation
  todo111.fr.jsonl       Episode 1 lines that 07th-mod re-segmented, re-translated
  special_ep1.fr.jsonl   4 Episode 1 lines with malformed carets, stored as whole lines
work/
  chunks/                Episode 1 translation batches (original, unpatched script)
  ep2/                   Episode 2 and Tea Party batches (07th-mod script)
  ep3/, ep4/             Episode 3 and 4 batches, with their Tea Parties
  pages/fr/              character profile / Tips page texts, one file per page
review/                  review against the Japanese: batches, justified fixes, reviewer brief
patch/                   French images, laid out like the game folder (en/…, bmp/…)
installer/               entry to propose for the 07th-mod installer's installData.json
ui/*.txt, ui/*.md5       manifests of the images installed in the original (unpatched) game
desinstaller.sh          uninstaller: puts the English script and images back
```

Not versioned: game files (original scripts, extracted images), the generated French script
(`mod/0.u.fr`), and `dist/`. They are either copyrighted game data or reproducible from the
repository plus the game.

## Building

Requirements: Python 3 with Pillow, NumPy and OpenCV (images only), and the English `0.u` script
of 07th-mod at the version in `mod/BASE.txt`.

```sh
# French script only
python3 -I tools/modapply.py mod/0.u.original $(grep -v '^#' mod/translations.txt) -o mod/0.u.fr

# Release archive: French 0.u + patch/ images -> dist/umineko-question-fr.zip
python3 -I tools/package.py "<game folder>/0.u"
```

`package.py` refuses to build if the English script's md5 differs from `mod/BASE.txt`. Text
injected into a different script version would land on the wrong lines.

## Distribution through the 07th-mod installer

The installer's *Translations* option for *Umineko Question (Ch. 1-4)* downloads an archive and
extracts it over the patched game. This is also how the Italian (Beyond The Ataraxia) and
Ukrainian translations are delivered. `installer/installData-entry.json` is the entry to propose
upstream in [`installData.json`](https://github.com/07th-mod/python-patcher). It points at
`releases/latest/download/umineko-question-fr.zip`, so each new GitHub release is picked up
without changing the entry.

## How it works

See [docs/WORKFLOW.md](docs/WORKFLOW.md) for:

- the script format;
- how translation batches are extracted, translated, validated and injected;
- the review against the Japanese;
- how the images are re-lettered;
- how to add an episode or follow a 07th-mod update.

## Credits

- Original work: 07th Expansion (Ryukishi07).
- English translation: MangaGamer. 07th-mod patch: the 07th-mod team.
- French translation: [infocris](https://github.com/infocris), with Claude (Anthropic).

This project is not affiliated with 07th Expansion, MangaGamer or 07th-mod. You need to own the
game to use it.
