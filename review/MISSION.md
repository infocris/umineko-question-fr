# Mission : relire la traduction française d'Umineko contre le japonais original

Projet : `~/Documents/umineko-fr/` (lance tes commandes depuis ce dossier).

La traduction française a été faite **depuis l'anglais** (MangaGamer). Tu la relis en la
confrontant au **japonais original** pour corriger ce que la double traduction a abîmé.

1. Lis `STYLE.md` en entier (glossaire, registres, typographie, balises — toujours valables).
2. Ton lot : `review/NN.jsonl`, une ligne JSON par réplique :
   `{"id", "voix" (locuteurs, voir STYLE.md), "ja": japonais, "en": [segments], "fr": [segments]}`.
   Lis-le par tranches (Read offset/limit, ~150 lignes).
3. Pour chaque réplique, compare `ja` / `en` / `fr`. Corrige **seulement** quand ça vaut la
   peine :
   - contresens ou glissement de sens dû à l'anglais (l'anglais a mal compris, simplifié,
     ajouté ou omis quelque chose d'important) ;
   - registre faux : tu/vous, politesse (keigo des domestiques, ton archaïque de Beatrice/
     Kinzo, langage enfantin de Maria), manière de parler propre au personnage ;
   - jeux de mots, proverbes, références : préférer l'idée japonaise si elle passe en français ;
   - nuance de ton perdue (ironie, hésitation, emphase) ;
   - incohérence flagrante avec les répliques voisines.
   Ne réécris pas pour le style si le sens et le ton sont justes. Ne touche pas aux noms,
   au glossaire, ni aux choix fixés de STYLE.md. Le japonais d'une ligne peut couvrir
   plusieurs lignes anglaises (blocs séparés par ` / `) : raisonne sur le bloc.
4. **Contraintes techniques** (identiques à la traduction) : même nombre de segments que `en`,
   séparés par `‖` ; le français de chaque segment correspond au segment anglais (le jeu fait
   une pause / joue une voix par segment) ; balises `<i>…</i>`, `~ib~`, `#ff0000` conservées ;
   pas de `^ @ \ |`. Le découpage reste celui de l'anglais même si le japonais coupe ailleurs.
5. Écris **uniquement les répliques corrigées** dans `review/NN.fix.txt`, réplique entière :

       # 12345 : Kanon dit `boku' — l'anglais neutralise ; ton plus sec
       12345|segment 1 corrigé‖segment 2

   Une ligne `#` de justification courte avant chaque correction (en français).
6. Lance `python3 -I tools/fixcheck.py review/NN` jusqu'à `OK`. Ne modifie aucun autre fichier.

Compte rendu final (court) : nombre de corrections, types de problèmes les plus fréquents,
3 à 5 exemples marquants (id, avant → après, pourquoi), et toute remarque générale sur la
traduction anglaise ou française qui vaudrait pour les autres lots (registre d'un personnage
mal rendu partout, terme récurrent à changer…).

## Remarques des premiers lots (à appliquer)

- 苦笑い : l'anglais met « bitter smile » → presque toujours un sourire **gêné / contraint**, pas « amer ».
- ヘソを曲げる (Maria) : elle **boude**, elle n'est pas « en colère ».
- 魔女さま dans la bouche de Battler/Jessica = ironique → « Madame la sorcière ».
- 困ったな / 困ったね (George) : « C'est embêtant », « Voilà qui est embêtant ».
- 秀吉兄さん (Kyrie) → « Hideyoshi nii-san » (comme « Natsuhi nee-san »).
- Méfie-toi des ajouts dramatisants de l'anglais (« avant la fin du monde », « toute-puissante »)
  et des omissions de lore (ex. séisme du Kanto).
- Maria parle souvent d'elle à la 3ᵉ personne (真里亞は…) : rétablir (« Maria veut… »).
- Natsuhi **vouvoie** Eva (et toute sa belle-famille) : corriger tout tutoiement.
- Narration de Battler : il dit « Grand-père » là où le japonais a 祖父さま, même si l'anglais met « Kinzo ».
- 踵を鳴らす (Natsuhi) → « claquement de talons ».
- Vocabulaire souvent faussé par l'anglais : 溜め息 = soupir ; 憮然 = renfrogné ; 怪訝 = perplexe ;
  拍子抜け = décontenancé ; 一応 = pour la forme ; 腹の探りあい = jauger les intentions de l'autre.
- ボンクラ (Rudolf sur Battler) = « bon à rien ».
- **Règle générale tu/vous : suis le niveau de politesse du japonais** (です/ます, さん, keigo → vous ;
  forme neutre → tu), même si STYLE.md dit autre chose, sauf pour l'ironie évidente.
  Constats : Rosa vouvoie Kyrie ; Rudolf vouvoie Hideyoshi ; Gohda vouvoie tous les domestiques ;
  Natsuhi vouvoie sa belle-famille ; George tutoie Shannon.
- Kyrie vouvoie Gohda en japonais : la politesse réelle du japonais l'emporte sur la règle générale
  « famille → domestiques : tu » quand elle est marquée.
- 爪の垢 → « prendre de la graine ».
- Genji : l'anglais ajoute souvent « sir » / formules recherchées absentes du japonais.
- `chambre close` = mystère de la pièce fermée uniquement ; une pièce simplement fermée/sans aération → « pièce hermétiquement fermée ».
- 親父 dit par Rudolf (ou Eva/Rosa) à ses frères et sœurs → « le vieux » / « notre père », pas « mon père ».
- 甘えん坊 → « grand bébé ». お祖父さま dit par Kyrie (point de vue des enfants) → « Grand-père ».
- 会社を興す → « fonder une entreprise ». Typographie : espace avant ? ! : ; à vérifier au passage.
- 駄目 / 全然駄目 ≠ « inutile » : « ça va pas (du tout) », « raté », « c'est fichu ».
- チェス盤をひっくり返す → **« retourner l'échiquier »** (choix fixé, remplace « faire pivoter »).
- うみねこのなく頃に → « Quand les mouettes pleurent ».
- Natsuhi **tutoie** les enfants (Battler compris).
- 人間とトリック → « des humains et des astuces » (pas « astuces humaines »).
- お約束 → « la règle du genre » / « un grand classique ». 戦人とやら (Beatrice) → « le dénommé Battler ».
- Beatrice : ses 良い = « soit », « bien » (pas « merveilleux »). 杭 = toujours « pieux ».
- Honorifiques -sama des domestiques : à garder quand le japonais les a.
- お父様 dit par Eva/Krauss/Rudolf/Rosa = « Père » même devant les neveux (l'anglais met parfois « Grandfather »).
- 冒涜 (Beatrice) envers une personne → « manquer de respect à » (pas « profaner quelqu'un »). 意味深 → « ça en dit long ».
- “い”る : lieu précis → « `est là' » ; propos général → « existe ».
- Négations et sujets : l'anglais en perd/inverse souvent — vérifier qui fait quoi.
