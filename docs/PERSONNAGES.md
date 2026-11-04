# Personnages et voix

Inventaire pour attribuer une voix TTS à chaque locuteur. Source de vérité : `tools/personnages.json` (ce fichier en est le rendu).

- **Dossier** : dossier des fichiers voix du jeu (`voice\NN\`), le même dans les deux arcs.
- **Code** : préfixe des alias voix dans le script des épisodes 1-4 (`kin_1e1`) et code `voix` de `umineko-answer-fr/tools/voix.json`.
- **Répl. Q / R** : lignes de script doublées par ce dossier, épisodes 1-4 / 5-8 (une ligne = une réplique, souvent plusieurs fichiers voix).
- **Âge** : approximatif, en 1986 sauf mention.

Les cases « Spoiler » sont regroupées en fin de page.

| Dossier | Code | Personnage | Genre | Âge | Répl. Q | Répl. R | Voix | Ton |
|---|---|---|---|---|---:|---:|---|---|
| – | – | Narration (lignes sans voix) | au choix | adulte | 19480 | 18830 | Voix posée et neutre de conteur, assez grave, capable de passer du descriptif calme aux montées de tension. Certaines narrations sont au « je » de Battler (ép. 1-4 surtout) : une voix masculine d'âge moyen reste cohérente. | Récit au passé simple, souvent lent, ponctué de « ...... ». |
| 10 | `but` | Battler Ushiromiya | M | 18 | 2909 | 2347 | Jeune homme, voix forte et expressive, large palette (rires, cris, colère). | Héros. Gouailleur et blagueur au début, puis enragé dans les débats contre la sorcière, puis posé et assuré (ép. 5-8). Personnage le plus présent : voix à soigner en priorité. |
| 27 | `bea` | Beatrice | F | sans âge (sorcière, paraît ~20-25) | 2748 | 1833 | Jeune femme à la voix ample et théâtrale, grand rire (« kyahahaha »), capable aussi d'une voix fragile et douce (ép. 5-6). | Sorcière dorée : arrogante, archaïque et grandiloquente, provocatrice, moqueuse ; s'adoucit beaucoup à partir de l'ép. 5. Deuxième rôle le plus présent. |
| 11 | `enj` | Ange Ushiromiya | F | 18 ans en 1998 ; 6 ans en 1986 | 1122 | 1336 | Deux âges dans le même dossier : jeune femme à la voix sèche et grave (1998, la plupart des répliques) et petite fille (1986, ép. 4 et 8, parle d'elle-même à la 3e personne). Prévoir deux voix si le TTS le permet. | Adulte : froide, méfiante, tranchante, blessée. Enfant : capricieuse, solitaire. |
| 05 | `eva` | Eva Ushiromiya | F | ~51 | 1549 | 635 | Femme mûre, voix acérée, rire moqueur. | Ambitieuse, ironique, piquante, mère protectrice de George. Le même dossier porte aussi Eva-Beatrice (alias ev2, ép. 3) : voir dossier 34. |
| 46 | `eri` | Erika Furudo | F | ~16 | 0 | 1791 | Jeune fille, voix polie qui vire au rire hystérique et au sarcasme. | Détective autoproclamée, vouvoiement faussement poli, arrogante, sadique ; rire « ahahahaha ». Ép. 5-8, rôle majeur. |
| 13 | `mar` | Maria Ushiromiya | F | 9 | 1351 | 364 | Enfant, voix aiguë et chantante ; peut devenir glaçante. | Phrases courtes et enfantines, tic « Uu- », parle d'elle-même à la 3e personne ; passionnée d'occultisme, inquiétante quand elle parle de la sorcière. |
| 04 | `jes` | Jessica Ushiromiya | F | 18 | 1092 | 554 | Adolescente, voix vive et énergique. | Garçon manqué, franche, s'emporte vite, sentimentale au fond. |
| 15 | `sha` | Shannon | F | ~18 | 835 | 696 | Jeune femme, voix douce et timide. | Domestique, très polie (vouvoie), réservée, s'excuse beaucoup ; plus déterminée quand elle se bat (ép. 2-3). |
| 28 | `ber` | Bernkastel | F | sans âge (paraît enfant/adolescente) | 231 | 1293 | Voix basse, monocorde, lasse, presque sans intonation ; devient venimeuse. | Sorcière des miracles, froide, cynique, cruelle (ép. 5-8). |
| 07 | `geo` | George Ushiromiya | M | 23 | 999 | 466 | Jeune homme, voix douce et posée. | Grand cousin gentil et poli, rassurant, parfois anxieux face à sa mère. |
| 03 | `nat` | Natsuhi Ushiromiya | F | ~44 | 495 | 817 | Femme mûre, voix tenue, tranchante. | Digne, stricte, fière de son rôle d'épouse du chef ; tendue, s'adoucit rarement. |
| 12 | `ros` | Rosa Ushiromiya | F | ~32 | 1018 | 265 | Jeune adulte, voix douce qui peut devenir dure, voire hystérique. | Mère de Maria, gentille en apparence, sévère et à bout de nerfs avec sa fille. |
| 29 | `lam` | Lambdadelta | F | sans âge (paraît adolescente) | 266 | 861 | Voix aiguë, sucrée, enjouée, qui bascule en menace. | Sorcière de la certitude, capricieuse, enfantine, joueuse et cruelle. |
| 16 | `kan` | Kanon | M | ~16 | 685 | 432 | Adolescent, voix jeune, contenue, un peu sèche. | Domestique, se dit « simple meuble », taciturne, amer, protecteur envers Shannon. |
| 09 | `kir` | Kyrie Ushiromiya | F | ~44 | 552 | 436 | Femme mûre, voix calme et nette. | Belle-mère de Battler, pince-sans-rire, analytique, froide quand elle raisonne. |
| 08 | `rud` | Rudolf Ushiromiya | M | ~45 | 444 | 392 | Homme mûr, voix décontractée, un peu canaille. | Père de Battler, séducteur, blagueur, devient sérieux quand il complote. |
| 01 | `kin` | Kinzo Ushiromiya | M | très âgé (~85) | 465 | 351 | Grave, rauque, puissante, qui tonne. | Grandiloquent, archaïsant, colérique, tirades mystiques sur la sorcière ; tutoie tout le monde sauf Nanjo. |
| 02 | `kla` | Krauss Ushiromiya | M | ~54 | 511 | 304 | Baryton assuré, un peu pompeux. | Chef de famille, autoritaire et sûr de lui, souvent condescendant, peut s'emporter. |
| 54 | `wil` | Willard H. Wright | M | ~45 | 0 | 757 | Homme mûr, voix grave, traînante, rocailleuse. | Inquisiteur détective, désabusé, sarcastique, tutoie tout le monde, profondément humain. |
| 30 | `wal` | Virgilia | F | sans âge (paraît ~40) | 400 | 252 | Femme mûre, voix posée, maternelle. | Ancienne maîtresse de Beatrice, calme, sage, ironie légère. |
| 06 | `hid` | Hideyoshi Ushiromiya | M | ~54 | 398 | 203 | Homme jovial, chaleureux, un peu bourru. | Mari d'Eva, self-made man, bonhomme et conciliant ; parler du Kansai en japonais (familier, rond en français). |
| 14 | `gen` | Genji Ronoue | M | ~73 | 363 | 237 | Vieil homme, voix basse, calme, économe. | Majordome en chef, laconique, impassible, loyal à Kinzo. |
| 31 | `ron` | Ronove | M | sans âge (paraît ~30) | 413 | 174 | Baryton suave et courtois. | Majordome démoniaque, élégant, pince-sans-rire, petit rire « pu ku ku ». |
| 47 | `dla` | Dlanor A. Knox | F | paraît enfant | 0 | 579 | Petite voix grave et sérieuse, monocorde. | Inquisitrice, phrases solennelles avec des MAJUSCULES pour ses « décrets », digne et juste. |
| 99 | `v99` | Voix secondaires | mixte | - | 232 | 304 | Figurants : annonces d'aéroport, foules, policiers, journalistes… Une ou deux voix génériques par genre suffisent. | Neutre. |
| 53 | `lio` | Lion Ushiromiya | indéterminé | ~19 | 0 | 528 | Voix androgyne, ni clairement masculine ni féminine (le genre de Lion n'est jamais révélé) ; jeune, douce et assurée. | « Successeur » de la famille, idéaliste, poli, sérieux, chaleureux avec Will (ép. 7). |
| 32 | `gap` | Gaap | F | sans âge (paraît ~25) | 179 | 337 | Jeune femme, voix sensuelle et taquine. | Démone espiègle, provocante, se moque de Battler ; appelle Yasu « mon intime » (ép. 7). |
| 19 | `nan` | Terumasa Nanjo | M | ~70 | 345 | 129 | Vieil homme, voix douce et lente. | Médecin et ami de Kinzo, courtois, prudent, conciliant. |
| 18 | `kum` | Chiyo Kumasawa | F | ~70 | 220 | 213 | Vieille dame, voix chevrotante et malicieuse. | Domestique, rieuse (« ho ho ho »), raconte des histoires de fantômes, taquine. |
| 17 | `goh` | Toshiro Gohda | M | ~40 | 251 | 161 | Homme d'âge moyen, voix affable. | Cuisinier, obséquieux avec la famille, vouvoie tout le monde, fier de son métier. |
| 55 | `cla` | Clair Vaux Bernardus | F | paraît jeune femme | 0 | 361 | Voix éthérée, douce, mélancolique. | Témoin et narratrice de l'ép. 7, solennelle, confession. |
| 33 | `sak` | Sakutarou | M | peluche (voix d'enfant) | 267 | 46 | Petite voix aiguë et mignonne. | Lion en peluche de Maria, tic « uryuu », naïf et tendre. |
| 50 | `fea` | Featherine Augustus Aurora | F | sans âge (antique) | 0 | 303 | Voix lente, majestueuse, détachée, un peu rêveuse. | Sorcière du Théâtre, langage solennel et archaïque, curiosité d'observatrice. |
| 42 | `rg5` | Mammon (Sept Sœurs) | F | jeune | 210 | 35 | Voix vive, sèche. | L'avarice : cynique, piquante. |
| 38 | `rg1` | Lucifer (Sept Sœurs) | F | jeune | 144 | 69 | Voix hautaine. | Aînée, l'orgueil : arrogante, autoritaire avec ses sœurs. |
| 56 | `toh` | Ikuko / Hachijo Tohya | F | ~35-40 (1998) | 0 | 213 | Femme adulte, voix calme, cultivée, un peu ironique. | Romancière (Hachijo Tohya est son nom de plume) ; ép. 7-8. Ange la tutoie comme romancière, la vouvoie dans le ???? final. |
| 51 | `zep` | Zepar | F | sans âge (démon) | 0 | 208 | Voix théâtrale de présentatrice, enjouée. | Démon de l'amour, forme un duo avec Furfur, parle en vers et en écho, emphatique. |
| 52 | `fur` | Furfur | F | sans âge (démon) | 0 | 194 | Voix proche de Zepar, légèrement différente (plus douce ou plus aiguë). | Démon de l'amour, complète les phrases de Zepar. |
| 20 | `ama` | Tooru Amakusa | M | ~20-25 (1998) | 63 | 109 | Jeune homme, voix nonchalante, désinvolte. | Garde du corps d'Ange, ancien mercenaire, blagueur et détendu, appelle Ange « ojō ». |
| 60 | `v60` | Beato l'aînée | F | sans âge | 0 | 172 | Proche de Beatrice, plus mûre et plus cruelle. | Archaïque, sarcastique, tutoie ; ép. 6. |
| 00 | `duo` | Chœur (deux personnages) | mixte | - | 0 | 133 | Deux voix superposées (Zepar et Furfur, Bernkastel et Lambdadelta…) : mixer les deux voix TTS concernées. | Répliques entre 「「 」」 dans le japonais. |
| 58 | `kij` | Kinzo jeune | M | ~20 ans (années 1940) | 0 | 129 | Jeune homme, voix claire et ferme. | Militaire puis amoureux, sincère, emporté ; ép. 7 uniquement. |
| 43 | `rg6` | Beelzebub (Sept Sœurs) | F | jeune | 49 | 80 | Voix gourmande, joyeuse. | La gourmandise : légère, ne pense qu'à manger. |
| 22 | `kas` | Kasumi Sumadera | F | ~40 (1998) | 122 | 0 | Femme mûre, voix stridente et méprisante. | Sœur de Kyrie, hostile, vulgaire, rire mauvais ; ép. 4. |
| 34 | `evb` | Eva-Beatrice | F | jeune en apparence (Eva à ~16 ans) | 0 | 121 | Version jeune d'Eva, plus aiguë, ricanante. | Sorcière cruelle et capricieuse, rire sadique. Aux ép. 3-4 elle parle dans le dossier 05 (alias ev2). |
| 36 | `s41` | Chiester 410 | F | jeune (soldate) | 71 | 43 | Voix enjouée, nonchalante. | Soldate bavarde et désinvolte, finit ses phrases par un tic (« -nihe »). |
| 39 | `rg2` | Leviathan (Sept Sœurs) | F | jeune | 69 | 44 | Voix aigre. | L'envie : jalouse, râleuse. |
| 21 | `oko` | Okonogi | M | ~50 (1998) | 79 | 29 | Homme mûr, voix jovial et rocailleuse. | Associé d'Eva, bon vivant, bavard, protecteur envers Ange. |
| 41 | `rg4` | Belphegor (Sept Sœurs) | F | jeune | 84 | 20 | Voix posée et polie. | La paresse : la plus raisonnable et la plus calme. |
| 35 | `s45` | Chiester 45 | F | jeune (soldate) | 65 | 38 | Voix neutre de soldate, mécanique. | Lapine de la garde de Ciel, rapports militaires, sensible sous la discipline. |
| 59 | `bic` | Beatrice Castiglioni « Bice » | F | ~20 (années 1940) | 0 | 102 | Jeune femme, voix vive avec un accent italien. | Ép. 7 ; ses répliques en italien sont entre 『 』 : voix TTS capable d'italien. |
| 37 | `s00` | Chiester 00 | F | jeune (soldate) | 35 | 58 | Voix calme d'officière. | Cheffe de l'escouade, sérieuse, protectrice. |
| 40 | `rg3` | Satan (Sept Sœurs) | F | jeune | 52 | 35 | Voix forte et irritée. | La colère : s'emporte constamment. |
| 44 | `rg7` | Asmodeus (Sept Sœurs) | F | jeune (la cadette) | 39 | 46 | Voix aiguë et pétillante. | La luxure : romantique, enthousiaste, la plus jeune. |
| 48 | `ger` | Gertrude | F | adulte | 0 | 83 | Voix sévère, autoritaire. | Inquisitrice, stricte, juridique. |
| 49 | `cor` | Cornelia | F | jeune adulte | 0 | 81 | Voix ferme mais plus chaleureuse que Gertrude. | Inquisitrice, formelle, un peu plus humaine. |
| 24 | `kaw` | Capitaine Kawabata | M | ~60 | 52 | 7 | Homme mûr, voix rude de marin. | Pilote du bateau, bourru mais bienveillant. |
| 23 | `pro` | Professeur Ootsuki | M | âgé (1998) | 43 | 8 | Homme âgé, voix théâtrale de conférencier. | Spécialiste de l'occulte à la télévision, emphatique. |
| 57 | `v57` | Tohya (l'homme qui accompagne Ikuko) | M | ~30 (1998) | 0 | 43 | Homme jeune adulte, voix calme et douce. | Ép. 8 ; discret, poli. |
| 25 | `na2` | Fils de Nanjo | M | adulte (1998) | 36 | 0 | Homme d'âge moyen, voix polie et réticente. | Ép. 4 uniquement ; médecin, ne veut pas parler de l'affaire. |
| 26 | `ku2` | Fils de Kumasawa | M | adulte (1998) | 11 | 0 | Homme d'âge moyen, voix familière. | Ép. 4 uniquement ; pêcheur, parle de façon populaire. Identité déduite du contexte, à confirmer. |

Le tableau est trié par nombre total de répliques : les premières lignes sont les voix à soigner en priorité.

## Spoilers

<details><summary>Afficher (révèle l'intrigue des épisodes 5-8)</summary>

- **Shannon** (`sha`) : Shannon, Kanon et Beatrice sont liés (ép. 7) ; le jeu leur donne des voix distinctes, à garder distinctes.
- **Clair Vaux Bernardus** (`cla`) : Incarnation de la vérité de Beatrice : peut se rapprocher de la voix de Beatrice en plus fragile.
- **Tohya (l'homme qui accompagne Ikuko)** (`v57`) : C'est Battler adulte : voix de Battler en plus mûre et plus éteinte.

</details>
