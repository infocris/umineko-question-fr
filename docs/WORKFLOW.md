# Workflow

This document explains how the French translation is produced, checked and packaged. Every
command runs from the repository root. Python is always run with `-I` (isolated mode), because
some inputs come from game archives.

The translator-facing guides are in French, since they are written for people translating
*into* French:

- [`STYLE.md`](../STYLE.md): style guide, registers (tu/vous), glossary, fixed choices.
- [`work/ep2/MISSION.md`](../work/ep2/MISSION.md): brief for a translation batch.
- [`review/MISSION.md`](../review/MISSION.md): brief for a review batch, plus the recurring
  issues found so far.

## 1. The game script

The 07th-mod game runs on ONScripter-RU and reads a single script, `0.u`: UTF-8, CRLF line
endings, ~343,000 lines. Read it with `newline=""` in Python. Universal newlines break the CRLF
split.

Each piece of dialogue exists twice: a block of `langjp` lines followed by a block of `langen`
lines.

```
langjp　…なぜなら、私は「家具」だからだ。@
langjp　家具は道具に過ぎず、人間ではない。@
langen^...After all, I am furniture.^@
langen^Furniture is nothing more than a tool, not a human.^@
```

The French translation replaces the text of the `langen` lines. The Japanese is left untouched.

### Anatomy of a `langen` line

```
langen:dwave_eng 0, nan_1e1:^"Good morning.^@:dwave_eng 0, nan_1e2:^  Did you sleep well?"^\
```

- **Text segments:** splitting on `^` gives the text at odd indices. Each segment is one click
  or one voice clip. Translations must keep exactly the same number of segments.
- **Control parts:** voice commands (`dwave_eng 0, <file>:`) and end codes (`@` wait, `\` page
  break, `/`) sit between the segments and are never touched. The voice file prefix gives the
  speaker (`nan` = Nanjo, `but` = Battler…). Extraction exposes it as the `voix` field.
- **Unbalanced carets:** some lines don't close their last `^`. The trailing control characters
  are split off (`split_line` in `tools/modapply.py`).
- **U+0010 marker:** 07th-mod puts it at the start of some continuation segments. It is removed
  on extraction and put back on injection.
- **Inline markup** (shown to translators in a friendlier form):

  | In the script | In the batches | Meaning |
  |---|---|---|
  | `#fefefe…#ffffff` | `<i>…</i>` | coloured / emphasised text |
  | `#ff0000…#ffffff` | `#ff0000…</i>` | red truth |
  | `~ib~…~ib~` | same | bold italic |
  | `<Happy Halloween>` | same | spoken in English in the original, kept in English |

Line numbers in `0.u` (1-based) are the identifiers of everything in this repository. They are
only valid for the script version in `mod/BASE.txt`.

### Where the episodes are

| Content | Labels in `0.u` |
|---|---|
| Episode N main story | `*umiN_opning`, `*umiN_1` … (Episode 4: `*Umi4_*`) |
| Tea Party | `*teatime_N` |
| ???? (ura Tea Party) | `*ura_teatime_N` |
| bridge lines | `*prescroll_teatime_epN` |

Find their line ranges with
`grep -n '^\*\(umi\|Umi\|teatime\|ura_teatime\|prescroll\)' 0.u`.

## 2. Translating a batch

```sh
# 1. Japanese for every English line (once per script version) -> work/ja.json
python3 -I tools/jpalign.py mod/0.u.original work/ja.json

# 2. Extract a line range (start inclusive, end exclusive) -> {"id","en","voix","ja"} per line
python3 -I tools/modextract.py mod/0.u.original 141453 202657 work/ep3/all.en.jsonl
```

Split the result into batches of ~700 lines (`work/epN/NN.en.jsonl`). A batch is translated into
`work/epN/NN.fr.txt`, one line per id:

```
93366|La sorcière me l'a dit.‖  ~ib~Cela~ib~ est l'élément unique de ce monde.
93402|Mon esprit a vagabondé.
```

Segments are separated by `‖` (U+2016). Then validate:

```sh
python3 -I tools/tlcheck.py work/epN/NN     # -> work/epN/NN.fr.jsonl when OK
```

`tlcheck.py` (with `check_seg` in `tools/umitl.py`) rejects a batch that has any of these
problems:

- an id is missing, duplicated or unknown;
- a line has the wrong number of segments;
- a segment has a different count of `<i>`/`</i>`, `~` or `#ff0000` from the English;
- a segment contains `^ @ \ |`;
- a segment is empty;
- a segment uses `ᵉ`, which the game fonts don't have.

It also realigns leading and trailing spaces to the English automatically, because editors and
models tend to drop them.

Finally, add the new `NN.fr.jsonl` files to `mod/translations.txt`, before the `review/` entries.

## 3. Reviewing against the Japanese

The first two episodes were translated from English, then reviewed against the Japanese. A review
batch `review/NN.jsonl` holds, for each line, `ja`, `en` and the current `fr`. The reviewer writes
only the lines that need changing, each with a one-line justification:

```
# 88015 : contresens anglais : 無言を貫いた = Genji garde le silence jusqu'au bout
88015|...Genji-san a gardé le silence jusqu'au bout.
```

```sh
python3 -I tools/fixcheck.py review/NN      # -> review/NN.fix.jsonl when OK
```

Fixes are overlays. `mod/translations.txt` lists the translation files first and the review
fixes after them. `tools/modapply.py` applies the files in order, so a later entry for the same
id wins. The original translation files are never edited, and a fix can be dropped by removing
its line from `NN.fix.txt`.

| Review batch | Content |
|---|---|
| `review/01`–`10` | Episode 1 and its Tea Parties |
| `review/11`–`20` | Episode 2 and its Tea Parties |
| `review/21` | consistency pass: Natsuhi, Eva, Maria (Episode 1) |
| `review/22` | consistency pass: Rosa, Kyrie (Episodes 1 and 2) |
| `review/23` | consistency pass: Kanon, Shannon, George, Battler→Rosa (Episode 2) |
| `review/90` | mechanical fixes: missing quotes, glossary leftovers |

The git tag `avant-relecture-jp` marks the state before the review.

## 4. Injecting and packaging

```sh
python3 -I tools/modapply.py mod/0.u.original $(grep -v '^#' mod/translations.txt) -o mod/0.u.fr
python3 -I tools/package.py mod/0.u.original      # -> dist/umineko-question-fr.zip
```

`modapply.py` replaces only the text segments. It re-checks every segment against the English
and rejects the whole line on error. It keeps the CRLF line endings.

An entry of the form `{"id": n, "line": "..."}` replaces a whole line. This is used for the 4
Episode 1 lines whose carets are malformed in the English script.

`package.py` checks the base script's md5 against `mod/BASE.txt`, builds the French script and
sets the window caption. It then zips the script with `patch/`, laid out so the archive can be
extracted directly into the game folder.

## 5. Images

The game draws much of its interface text inside PNGs. Loose files in the game folder override
the `.nsa` archives, and English-specific images live under `en/`. The French images in `patch/`
use the same paths, so extracting them over the game is enough.

| Tool | What it rewrites | Spec |
|---|---|---|
| `tools/nsa.py` | lists and extracts PNGs from `arc*.nsa` | – |
| `tools/retext.py` | buttons (light text with drop shadow, normal/hover frames) | `tools/ui_buttons.json`, `ui_title.json`, `ui_menu2.json` |
| `tools/panel.py` | title-screen text panels | `tools/ui_panels.json` |
| `tools/card.py` | full-screen text cards: dates, notices, epitaph, manual | `tools/ui_cards.json`, `ui_notices.json`, `ui_epitaph.json`, `ui_op.json`, `ui_manual.json`, `ui_mod_cards.json` (generated by `tools/mk_mod_cards.py`) |
| `tools/pagerender.py` | character profiles and Tips pages | `work/pages/pages.json` + `work/pages/fr/<hash>.txt` |

`retext.py`, `panel.py` and `card.py` follow the same pattern:

1. find the English text;
2. erase it with OpenCV inpainting, keeping the alpha channel;
3. set the French text with matching size, position, colour, shadow or outline.

`pagerender.py` doesn't erase anything. It draws the French text on the game's blank page
backgrounds (Tips) or on a transparent layer (profiles).

Each one takes `<spec> <source folder> <output folder> [--preview sheet.png]`. The preview sheet
puts the original and the French side by side.

For profiles and Tips, the English pages were OCRed with Tesseract, then translated into one text
file per page:

- `# ` marks a title;
- a blank line marks a paragraph break.

`pages.json` maps each page hash to its image files. `tools/pagecheck.py` validates a batch. The
07th-mod images are larger than the original ones (×1.125, and 1920×1080 for the recomposed
cards), and the renderers scale their parameters accordingly. `PAGE_ROOT` points
`pagerender.py` at the 07th-mod copies.

Regenerating `patch/` needs the game's own images, which are not versioned. `patch/` is
committed so that releases can be built without them.

## 6. When 07th-mod updates its script

Translations are keyed by line number, so a new 07th-mod script shifts them. The game's
`0.u.version.txt` shows the installed version, and `package.py` refuses a script whose md5
doesn't match `mod/BASE.txt`. To follow an update:

1. Diff the old and new English scripts on their `langen` lines (`difflib`, as
   `mod/align_ep1.json` did for the port of Episode 1 from the unpatched game).
2. Remap every id in the translation and fix files through the old→new line mapping. Lines whose
   English text changed, or whose segmentation changed, need re-translating. During the
   Episode 1 port, 111 such lines were collected in `mod/todo111.*`.
3. Regenerate `work/ja.json`, update `mod/BASE.txt` (tag and md5), rebuild and play-test.

There is no dedicated script for step 2 yet.

## 7. Uninstalling

`desinstaller.sh` restores the English script and images, but only for files whose md5 shows
they are still the ones this project installed. Files changed by something else are left
alone.

## 8. Original, unpatched game

Episode 1 was first translated for the unpatched game, whose script is `0.utf` (LF line
endings): `tools/umitl.py extract/apply`, batches in `work/chunks/`. The 07th-mod port reused
those translations through `mod/align_ep1.json`. The review fixes were only applied to the
07th-mod script.
