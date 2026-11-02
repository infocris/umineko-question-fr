# Guide de traduction — Umineko (Question Arcs) EN → FR

Traduction amateur, usage personnel. Source : la traduction anglaise officielle (MangaGamer)
contenue dans les lignes `langen` du script `0.utf`. Référence de ton : `work/umi1_0.fr.txt`
et `work/umi1_1.fr.txt` (déjà traduits et validés) — lis-en au moins 60 lignes avant de commencer.

## Format de travail

Tu reçois `work/chunks/NN.en.jsonl` : une ligne JSON par ligne de dialogue,
`{"id": <n° de ligne du script>, "en": [segments]}`.
Tu écris `work/chunks/NN.fr.txt` : une ligne par id, dans le même ordre :

    <id>|<segment 1>‖<segment 2>‖...

- **Exactement le même nombre de segments** que dans `en`, séparés par `‖` (U+2016).
- Un segment est souvent une phrase ou une réplique partielle : le jeu fait une pause entre
  deux segments (clic). Répartis le français pour que chaque segment corresponde au sens du
  segment anglais.
- **Conserve les espaces de tête** : un segment anglais qui commence par deux espaces
  (`"  Mais..."`) doit commencer par deux espaces en français. Idem pour un espace unique.
  Conserve aussi un espace final s'il existe en anglais (phrase coupée en deux segments).
- Une réplique peut être coupée sur plusieurs ids (guillemet ouvrant dans un id, fermant dans
  un autre) : respecte cette découpe, ne déplace pas de texte d'un id à l'autre.
- Interdits dans le texte : `^`, `@`, `\`, `‖` (sauf comme séparateur), `|` (sauf après l'id).
- Balises à recopier telles quelles, autour du mot traduit : `<i>…</i>` (texte coloré) et
  `~ib~…~ib~` (gras italique). Même nombre de `~` qu'en anglais.
- Les segments qui ne contiennent que de la ponctuation (`...`, `"`, `............?"`) :
  recopie-les (en adaptant la typographie si besoin).
- Le texte japonais (kanji : 朱志香, 右代宮 戦人…) reste tel quel.

## Typographie

- Guillemets droits `"` comme en anglais (pas de « »), aux mêmes endroits.
- Citations internes : garder la convention du jeu `` `mot' `` (accent grave + apostrophe).
- Espace avant `! ? ; :` (`"Quoi ?!"`, `"Uu- !"`). Pas d'espace avant `...`.
- Points de suspension : recopier le même nombre de points que l'anglais (`......`).
- Pas de tiret cadratin ajouté. `-` en fin de réplique interrompue : garder `-`.

## Ton et registres

- Narration de Battler : passé composé / imparfait, familier mais écrit
  (« J'ai bombé le torse », « Bon sang »). Les passages en présent restent au présent.
- Narrations à la 3ᵉ personne (scènes sans Battler) : passé simple, style littéraire.
- Battler, Jessica : très familiers (« t'es », « j'sais pas » avec modération, « bon sang »,
  « sérieux »), suppression fréquente du « ne ».
- George : poli, doux, tutoie ses cousins. Hideyoshi : jovial, familier (« Wah ha ha »).
- Eva : piquante, ironique. Rosa : douce mais stricte avec Maria. Kyrie : calme, pince-sans-rire.
- Rudolf : gouailleur. Krauss : autoritaire, soutenu. Natsuhi : très soutenue, raide.
- Kinzo : grandiloquent, archaïsant. Nanjo : courtois.
- Domestiques (Kumasawa, Genji, Shannon, Kanon, Gohda) : **vouvoient** la famille et
  utilisent les suffixes -sama / -san comme en anglais. Shannon est timide et polie.
- Maria : phrases enfantines courtes, tics « Uu- » (toujours écrit `Uu-`, `Uu-uu-`),
  répète les mots. Beatrice / sorcière : grandiloquente.

## Tutoiement / vouvoiement

- Cousins entre eux, parents → enfants, frères et sœurs (Krauss, Eva, Rudolf, Rosa) : **tu**.
- Neveux/nièces → oncles et tantes : **vous** si l'anglais est formel, sinon Battler tutoie
  (« Tante Eva, t'es trop méchante » toléré en panique) — par défaut **vous** pour Battler
  envers Krauss et Natsuhi, **tu** possible envers Rosa/Eva/Hideyoshi dans un moment familier.
  En cas de doute : vous.
- Battler → Kyrie : vous. Kyrie → Battler : tu.
- Famille → domestiques : tu (Battler peut vouvoyer Kumasawa, Genji, Nanjo par respect de l'âge).
- Domestiques → famille : vous. Domestiques entre eux : tu (Shannon/Kanon), vous envers Genji.
- Kinzo ↔ Nanjo : vous. Kinzo → Genji : tu.

## Glossaire (garder tel quel)

Noms : Ushiromiya, Battler, Jessica, George, Maria, Krauss, Natsuhi, Eva, Hideyoshi, Rudolf,
Kyrie, Rosa, Kinzo, Genji, Shannon, Kanon, Gohda, Kumasawa, Nanjo, Beatrice, Rokkenjima,
Niijima, Ange.
Suffixes conservés : -kun, -chan, -san, -sama, nii-san, nee-san, onii-chan, baa-chan,
Aniki (George), Aneki. « Aniki » sans article.

| Anglais | Français |
|---|---|
| Uncle X / Aunt X | Oncle X / Tante X (majuscule) |
| Dad / my dad / the old man | mon père, Papa, P'pa ; « old bastard » → « vieux salaud » / « mon vieux salaud de père » |
| Grandfather | Grand-père |
| Father (Kinzo, dit par ses enfants) | Père |
| the Head Family | la famille principale |
| the branch families | les branches cadettes |
| family conference | conférence familiale |
| the Golden Witch | la Sorcière dorée |
| the witch | la sorcière |
| the epitaph | l'épitaphe |
| the portrait | le portrait |
| the gold / the hidden gold | l'or / l'or caché |
| the head of the family / family head | le chef de famille |
| the ring (of the family head) | la bague (du chef de famille) |
| servant(s) | domestique(s) |
| the mansion | le manoir |
| the guesthouse | la maison d'hôtes |
| the study | le bureau |
| the rose garden | la roseraie |
| typhoon | typhon |
| Tips | Infos |
| Kuwabara, kuwabara | Kuwabara, kuwabara |
| *giggle* / *cackle* | *gloussement* / *ricanement* |
| Heheh / Ihihi / Wahahaha | Hé hé / Ihihi / Wah ha ha (onomatopées gardées, espacées à la française) |

Si un terme récurrent important n'est pas dans le glossaire, choisis une traduction et
**note-la** en fin de mission dans ton compte rendu (terme anglais → choix français).

## Contrôle

Avant de rendre, lance :

    python3 -I tools/tlcheck.py work/chunks/NN

Il vérifie ids, nombre de segments, balises, espaces de tête, caractères interdits. Corrige
jusqu'à `OK`. Ne modifie aucun autre fichier.

## Choix fixés après l'épisode 1 (à reprendre tels quels)

| Anglais | Français |
|---|---|
| Golden Land | la Terre dorée |
| Incipient's Chair | le Siège de l'Origine |
| My Beloved Witch Beatrice | Ma sorcière bien-aimée Beatrice |
| One-Winged Eagle | l'Aigle à une aile |
| Head's Ring | la bague du chef de famille |
| Successor | le successeur (Jessica : l'héritière) |
| Legend of the Gold | la Légende de l'or |
| charm (scorpion) | porte-bonheur (au scorpion) |
| closed room | chambre close |
| magic circle | cercle magique |
| Demons' Roulette | la Roulette des Démons |
| storehouse / shed | la remise |
| shutter | le rideau métallique |
| Madam / Milady / the Master | Madame / Mademoiselle / le Maître |
| Fukuin House | la Maison Fukuin |
| furniture (domestiques sur eux-mêmes) | meuble(s) |
| culprit | le coupable |
| *cough* | *toux* |
| 19th | 19e (jamais « ᵉ », absent des polices) |
| second floor / third floor | premier étage / deuxième étage |

Épitaphe (référence) : « Au premier crépuscule, offre en sacrifice les six que la clé aura choisis. »
« Au quatrième crépuscule, perce la tête et tue. » (poitrine, ventre, genou, jambe idem)
« Au neuvième crépuscule, la sorcière ressuscitera, et nul ne restera en vie. »
« Au dixième crépuscule, au terme du voyage, tu atteindras le pouvoir des trésors de la Terre dorée, une fois et pour la dernière fois. »
« La sorcière louera le sage et lui accordera quatre trésors. » « L'un sera… »

Registres : Natsuhi vouvoie sa belle-famille (Eva, Rudolf, Kyrie, Rosa, Hideyoshi) ; Eva la tutoie.
Natsuhi tutoie les enfants. Battler vouvoie Eva, Krauss, Natsuhi, Kyrie ; tutoie Rudolf (« P'pa »).

## Épisode 2 (Turn of the Golden Witch) — compléments

Fichiers : `work/ep2/NN.en.jsonl` → `work/ep2/NN.fr.txt`, contrôle `python3 -I tools/tlcheck.py work/ep2/NN`.
Chaque ligne JSON peut avoir un champ `"voix": "but,bea"` : préfixes des fichiers de voix =
qui parle (but Battler, bea Beatrice, sha Shannon, kan Kanon, jes Jessica, geo George,
mar Maria, ros Rosa, eva Eva, hid Hideyoshi, rud Rudolf, kir Kyrie, kla Krauss, nat Natsuhi,
kin Kinzo, gen Genji, goh Gohda, kum Kumasawa, nan Nanjo, ber Bernkastel). Sans `voix` :
narration. Sers-t'en pour le tutoiement/vouvoiement. Ne recopie pas ce champ dans ta sortie.

Balises supplémentaires :
- `#ff0000…</i>` = **texte rouge** (vérité rouge) : recopie `#ff0000` au même endroit et le `</i>` final.
- `<Happy Halloween>` et autres `<…>` = paroles prononcées **en anglais** dans la VO :
  garde le texte anglais tel quel entre `< >`.
- `♪`, `☆` : à garder.

| Anglais | Français |
|---|---|
| Endless Witch | la Sorcière de l'Infini |
| the red truth / speak in red | la vérité rouge / dire en rouge |
| Seven Stakes of Purgatory | les Sept Pieux du Purgatoire (Lucifer, Leviathan, Satan, Belphegor, Mammon, Beelzebub, Asmodeus) |
| stake(s) | pieu(x) |
| the game (Battler vs Beatrice) / gameboard / piece | la partie / l'échiquier / pièce |
| Tea Party / ??? | la Tea Party / ??? |
| golden butterflies | papillons dorés |
| the spider's thread (barrière) | le fil d'araignée |
| demon(s) | démon(s) ; butler demon Ronove → Ronove, le majordome démoniaque |
| Sakutarou | Sakutarou (le lion en peluche de Maria) |
| Ojou-sama / Milady | Mademoiselle |
| Beato (Maria) | Beato |
| meta-world / the room (Battler et Beatrice) | le méta-monde |
| denial / deny magic | nier la magie |
| Kuhkuhkuh / Ahyahyahya / Ihihihi (Beatrice) | Kuh kuh kuh / Ahya hya hya / Ihi hi hi |

Registres épisode 2 : Beatrice tutoie tout le monde (sauf ironie), parle de façon théâtrale,
archaïque et moqueuse ; Battler la tutoie. Ronove : vouvoiement exquis, « Pu ku ku ». Shannon
vouvoie George, George la tutoie ; Kanon vouvoie Jessica, Jessica le tutoie. Kanon ↔ Shannon : tu
(« Nee-san »). Rosa tutoie Maria ; Maria tutoie Rosa (« Mama »). Gohda vouvoie tout le monde.

## Choix fixés lors de la relecture contre le japonais

| Japonais / anglais | Français |
|---|---|
| チェス盤をひっくり返す / spin the chessboard around | retourner l'échiquier |
| うみねこのなく頃に | Quand les mouettes pleurent |
| 苦笑い / bitter smile | sourire gêné, contraint |
| 駄目 / useless | ça va pas, raté, fichu |
| 魔女さま (ironique) | Madame la sorcière |

Tu/vous : en cas de doute, le niveau de politesse du japonais fait foi.
| 人間とトリック / human tricks | des humains et des astuces |
| *cackle* isolé / *cackle*cackle*… | *ricanement* / *ricane*ricane*… (même nombre de répétitions) |
| ママは… (Rosa parlant d'elle) | « Maman » à la 3e personne (comme Maria → « Maria ») |
| 母さん / 父さん (George, Jessica) | Maman / Papa |
| 悪魔の証明 | la preuve du diable ; « 悪魔を証明した » = prouver l'existence du diable |
