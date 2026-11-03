# Mission : traduire un lot de l'épisode 4 d'Umineko (EN → FR)

Projet : `~/Documents/umineko-fr/` (lance tes commandes depuis ce dossier).

1. Lis `STYLE.md` en entier (y compris les sections « Épisode 2 », « Épisode 3 » et « Épisode 4 »), puis ~80 lignes de
   `work/umi1_1.fr.txt` comme référence de ton.
2. Lis ton lot `work/ep4/NN.en.jsonl` (par tranches avec Read offset/limit, c'est long).
   Pour le contexte, tu peux jeter un œil à la fin du lot précédent `work/ep4/(NN-1).en.jsonl`.
3. Écris la traduction dans `work/ep4/NN.fr.txt`, format `id|seg1‖seg2…`, une ligne par id,
   dans l'ordre, sans en sauter aucune. Le lot fait ~700 lignes : écris-le en plusieurs
   morceaux `work/ep4/NN.fr.part1.txt`, `part2`… (~150 ids chacun), puis concatène-les
   (`cat work/ep4/NN.fr.part*.txt > work/ep4/NN.fr.txt`, en vérifiant l'ordre part1..partK).
4. Lance `python3 -I tools/tlcheck.py work/ep4/NN` et corrige jusqu'à `OK`.
   (Les espaces de tête/de fin sont recalés automatiquement, ne t'en soucie pas.)
5. Ne modifie aucun autre fichier que les tiens (`work/ep4/NN.fr*`).

Japonais : chaque ligne a aussi un champ `"ja"` (texte japonais original). L'anglais reste
la base du découpage en segments, mais **en cas de doute sur le sens, le ton, le registre
(tu/vous, politesse, façon de parler) ou un jeu de mots, le japonais fait foi**. Ne recopie
pas le champ `ja` dans ta sortie.

Qualité attendue : français naturel et vivant, fidèle au sens, registres respectés
(tu/vous selon STYLE.md et le champ `voix`), cohérent d'une ligne à l'autre. Pas de
traduction mot à mot. Garde les jeux de mots compréhensibles en les adaptant si besoin.

Compte rendu final (court) : nombre de lignes, termes récurrents nouveaux non couverts par
le glossaire et le choix fait (anglais → français), passages délicats éventuels.

Lis aussi, dans `review/MISSION.md`, la liste des erreurs récurrentes relevées lors de la
relecture des épisodes 1 et 2 (contresens de l'anglais, guillemets oubliés, registres) : évite-les
d'emblée.

Lots 16-17 = Tea Party de l'épisode 4, puis ????. Contexte : fin de l'épisode 4.
