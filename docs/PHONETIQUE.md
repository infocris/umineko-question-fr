# Dictionnaire phonétique (TTS)

Prononciation des mots étrangers de la traduction (épisodes 1 à 8) pour une voix de synthèse française.
Généré par `tools/mkphonetique.py` depuis `tools/phonetique.tsv` (à éditer), avec :

- `tools/phonetique.json` : entrées, règles de prétraitement, onomatopées ;
- `tools/phonetique-alias.pls` : lexique [PLS](https://www.w3.org/TR/pronunciation-lexicon/) par substitution (`<alias>`), le plus portable : la graphie proposée se lit correctement avec n'importe quelle voix française ;
- `tools/phonetique-api.pls` : le même en API (`<phoneme>`), pour les moteurs qui l'acceptent.

**Principes.** Les noms japonais suivent la prononciation des voix japonaises du jeu, adaptée au français : `u` → « ou », `e` → « é », `sh` → « ch », `ch` → « tch », `j` → « dj », `g` dur, `s` jamais « z », `n` final ou devant consonne doublé (« Kinnzô », « Kanonn ») pour éviter les voyelles nasales françaises, voyelles longues (`ou`, `oh`, `ō`) en « ô ». Les noms d'origine occidentale gardent la lecture de leur langue, comme dans le jeu : Beatrice à l'italienne (« Béatritché »), George et Jessica à l'anglaise, Bernkastel à l'allemande. Ange et Lion gardent leur lecture française.

Occurrences : Q = épisodes 1-4, R = épisodes 5-8. « auto » = transcription calculée depuis le romaji.


## Personnages, noms japonais

| Graphie | Prononciation | API | Q | R | Note |
|---|---|---|---:|---:|---|
| Battler | Batlèr | /batlɛʁ/ | 1024 | 1715 | 戦人 Batora ; « Bat-lère », pas « Bateur » |
| Maria | *(lecture française)* |  | 2145 | 535 | lecture française |
| Natsuhi | Natsouhi | /natsɯçi/ | 583 | 920 | *auto* |
| Kinzo | Kinnzô | /kinzoː/ | 701 | 795 | 金蔵 Kinzō |
| Kanon | Kanonn | /kanoɴ/ | 1028 | 394 | 嘉音 ; éviter le « on » nasal |
| Ange | *(lecture française)* |  | 438 | 967 | 縁寿 Enje : garder la lecture française « Ange » [ɑ̃ʒ], aucune substitution |
| Ushiromiya | Ouchiromiya | /ɯɕiɾomija/ | 711 | 677 | *auto* |
| Shannon | Chanonn | /ɕanoɴ/ | 902 | 475 | 紗音 |
| Jessica | Djèssika | /dʑesika/ | 903 | 422 | ジェシカ, prénom anglais |
| Eva | Éva | /eva/ | 823 | 453 |  |
| George | Djordj | /dʒɔʁdʒ/ | 780 | 443 | prénom anglais (譲治 Jōji), pas « Georges » |
| Rosa | Roza | /ɾoza/ | 979 | 202 |  |
| Erika | Érika | /eɾika/ | 0 | 1138 |  |
| Krauss | Kraouss | /kɾaɯsɯ/ | 477 | 401 | クラウス : à l'allemande, pas « Krôss » |
| Genji | Guénndji | /ɡeɴdʑi/ | 479 | 307 | *auto* |
| Kyrie | Kirié | /kiɾie/ | 428 | 253 | 霧江 Kirie |
| Gohda | Gôda | /ɡoːda/ | 391 | 207 | 郷田 |
| Nanjo | Nanndjô | /naɴdʑoː/ | 395 | 155 | 南條 |
| Kumasawa | Koumassawa | /kɯmasawa/ | 312 | 190 | *auto* |
| Rudolf | Roudolf | /ɾɯdoɾɸ/ | 230 | 265 |  |
| Rokkenjima | Rokkénndjima | /ɾokkeɴdʑima/ | 218 | 262 | *auto* |
| Hideyoshi | Hidéyochi | /çidejoɕi/ | 296 | 132 | *auto* |
| Sakutarou | Sakoutarô | /sakɯtaɾoː/ | 365 | 33 | *auto* |
| Hachijo | Hatchidjô | /hatɕidʑoː/ | 0 | 109 | 八城 |
| Furudo | Fouroudo | /ɸɯɾɯdo/ | 0 | 106 |  |
| Asumu | Assoumou | /asɯmɯ/ | 38 | 55 | *auto* |
| Yasu | Yassou | /jasɯ/ | 0 | 84 | *auto* |
| Amakusa | Amakoussa | /amakɯsa/ | 39 | 41 | *auto* |
| Kasumi | Kassoumi | /kasɯmi/ | 73 | 7 | *auto* |
| Sumadera | Soumadéra | /sɯmadeɾa/ | 53 | 26 | *auto* |
| Tohya | Tôya | /toːja/ | 0 | 71 | 十八 |
| Okonogi | Okonogui | /okonoɡi/ | 24 | 26 | *auto* |
| Yamamoto | Yamamoto | /jamamoto/ | 0 | 36 | *auto* |
| Ikuko | Ikouko | /ikɯko/ | 0 | 33 | *auto* |
| Miyoko | Miyoko | /mijoko/ | 0 | 26 | *auto* |
| Sayo | Sayo | /sajo/ | 16 | 6 | *auto* |
| Itouikukuro | Itô Ikoukourô | /itoː ikɯkɯɾoː/ | 0 | 21 | 伊藤幾九郎 : deux mots |
| Yoshiya | Yochiya | /joɕija/ | 0 | 17 | *auto* |
| Kotobuki | Kotobouki | /kotobɯki/ | 0 | 16 | *auto* |
| Belne | Bèlné | /beɾune/ | 0 | 15 | 鐘音 Berune |
| Sakutaro | Sakoutarô | /sakɯtaɾoː/ | 0 | 11 |  |
| Kawabata | Kawabata | /kawabata/ | 1 | 7 | *auto* |
| Rika | Rika | /ɾika/ | 0 | 8 | *auto* |
| Tajima | Tadjima | /tadʑima/ | 0 | 7 | *auto* |
| Yukari | Youkari | /jɯkaɾi/ | 0 | 7 | *auto* |
| Sakusuke | Sakoussouké | /sakɯsɯke/ | 3 | 3 | *auto* |
| Asne | Assouné | /asɯne/ | 0 | 6 | 明日音 |
| Ayumi | Ayoumi | /ajɯmi/ | 0 | 5 | *auto* |
| Sakukichi | Sakoukitchi | /sakɯkitɕi/ | 2 | 3 | *auto* |
| Ootsuki | Ôtsouki | /oːtsɯki/ | 0 | 4 |  |
| Satoko | Satoko | /satoko/ | 0 | 4 | *auto* |
| Lunon | Lounonn | /ɾɯnoɴ/ | 3 | 1 | 留音 (domestique) |
| Reigonamu | Rèigonamou | /ɾeːɡonamɯ/ | 0 | 3 |  |
| Hayakawa | Hayakawa | /hajakawa/ | 3 | 0 | *auto* |
| Sonezaki | Sonézaki | /sonezaki/ | 0 | 3 | *auto* |
| Ronoue | Ronoué | /ɾonoɯe/ | 0 | 2 | 源次 Ronoue Genji |
| Chiyo | Tchiyo | /tɕijo/ | 2 | 0 | *auto* |
| Terumasa | Téroumassa | /teɾɯmasa/ | 2 | 0 | *auto* |
| Kuwabara | Kouwabara | /kɯwabaɾa/ | 1 | 1 | *auto* |
| Watanabe | Watanabé | /watanabe/ | 2 | 0 | *auto* |
| Shimada | Chimada | /ɕimada/ | 0 | 2 | *auto* |
| Tanaka | Tanaka | /tanaka/ | 0 | 2 | *auto* |
| Hiraoka | Hiraoka | /çiɾaoka/ | 0 | 2 | *auto* |
| Manon | *(lecture française)* |  | 1 | 1 | マノン : lecture française « Manon » |
| Toshiro | Toshirô | /toɕiɾoː/ | 0 | 1 |  |
| Fumiya | Foumiya | /ɸɯmija/ | 1 | 0 | *auto* |
| Tetsurou | Tétsourô | /tetsɯɾoː/ | 1 | 0 | *auto* |
| Sanae | Sanaé | /sanae/ | 1 | 0 | *auto* |
| Garashi | Garachi | /ɡaɾaɕi/ | 0 | 1 | *auto* |
| Yasuda | Yassouda | /jasɯda/ | 0 | 1 | *auto* |
| Takamiya | Takamiya | /takamija/ | 1 | 0 | *auto* |
| Emoto | Émoto | /emoto/ | 1 | 0 | *auto* |
| Leion | Léionn | /ɾeioɴ/ | 0 | 1 |  |

## Personnages, noms occidentaux

| Graphie | Prononciation | API | Q | R | Note |
|---|---|---|---:|---:|---|
| Beatrice | Béatritché | /beatɾiːtʃe/ | 1254 | 1022 | ベアトリーチェ, à l'italienne |
| Beato | Béato | /beato/ | 479 | 1112 |  |
| Bernkastel | Bèrnkastèl | /bɛʁnkastɛl/ | 50 | 460 |  |
| Lambdadelta | Lammdadèlta | /lambdadɛlta/ | 34 | 305 | pas de « am » nasal : « Lam-da-dèl-ta » |
| Dlanor | Dlanor | /dlanɔʁ/ | 0 | 265 |  |
| Ronove | Ronové | /ɾonowe/ | 184 | 77 | ロノウェ |
| Lion | *(lecture française)* |  | 0 | 240 | 理御 Rion : lecture française « Lion », aucune substitution |
| Virgilia | Virdjilia | /viʁdʒilja/ | 95 | 91 | à l'italienne |
| Bern | Bèrn | /bɛʁn/ | 36 | 129 |  |
| Will | Ouil | /wil/ | 0 | 158 | anglais |
| Gaap | Gâp | /ɡaːp/ | 76 | 75 | ガァプ |
| Chiester | Chièstère | /ɕiestɛʁ/ | 47 | 80 | シエスタ (« siesta ») |
| Mammon | Mammonn | /mamɔn/ | 85 | 3 |  |
| Featherine | Fézarine | /fezaʁin/ | 0 | 85 | フェザリーヌ |
| Knox | Nokss | /nɔks/ | 1 | 83 | anglais, k muet |
| Lambda | Lammda | /lamda/ | 11 | 69 |  |
| Lucifer | *(lecture française)* |  | 49 | 14 | lecture française |
| Clair | *(lecture française)* |  | 1 | 48 | lecture française « Claire » (Clair Vaux Bernardus) |
| Cornelia | Kornélia | /kɔʁnelja/ | 0 | 46 |  |
| Zepar | Zépar | /zepaʁ/ | 0 | 46 |  |
| Furfur | Fourfour | /fuʁfuʁ/ | 0 | 45 |  |
| Gertrude | Guèrtroud | /ɡɛʁtʁud/ | 0 | 40 |  |
| Goldsmith | Goldsmiss | /ɡɔldsmis/ | 18 | 14 | anglais |
| Angelo | Andjélo | /andʒelo/ | 0 | 31 | italien |
| Satan | *(lecture française)* |  | 18 | 6 | lecture française |
| Leviathan | Léviatann | /leviatan/ | 19 | 4 |  |
| Belphegor | Bèlfégor | /bɛlfeɡɔʁ/ | 23 | 0 |  |
| Aurora | Aourôra | /auɾoːɾa/ | 0 | 20 |  |
| Gretel | Grétel | /ɡʁetɛl/ | 17 | 1 |  |
| Beelzebub | Bé-èlzéboub | /beɛlzebub/ | 14 | 2 |  |
| Asmodeus | Asmodéouss | /asmodeus/ | 12 | 1 |  |
| Willard | Ouilarde | /wilaʁd/ | 0 | 13 | anglais |
| Bice | Bitché | /bitʃe/ | 0 | 12 | italien |
| Wright | Raïte | /ʁajt/ | 0 | 10 | anglais, w muet |
| Asmo | Asmo | /asmo/ | 7 | 2 |  |
| Augustus | Ogousstouss | /oɡustus/ | 0 | 8 |  |
| Chiesters | Chièstère | /ɕiestɛʁ/ | 0 | 5 |  |
| Castiglioni | Kastilyoni | /kastiʎʎoni/ | 0 | 4 | italien (gli = « lli ») |
| Levia | Lévia | /levja/ | 4 | 0 |  |
| Belphe | Bèlfé | /bɛlfe/ | 3 | 1 |  |
| Luci | Loutchi | /lutʃi/ | 2 | 2 |  |
| Belze | Bèlzé | /bɛlze/ | 3 | 0 |  |
| Gino | Djino | /dʒino/ | 0 | 2 | italien |
| Hansel | Hannzel | /hanzɛl/ | 2 | 0 |  |

## Lieux

| Graphie | Prononciation | API | Q | R | Note |
|---|---|---|---:|---:|---|
| Kuwadorian | Kouwadoriann | /kɯwadoɾiaɴ/ | 27 | 43 | *auto* |
| Fukuin | Foukou-inn | /ɸɯkɯiɴ/ | 9 | 53 | Maison Fukuin (福音) |
| Niijima | Niidjima | /niːdʑima/ | 19 | 24 |  |
| Odawara | Odawara | /odawaɾa/ | 26 | 13 | *auto* |
| Akujikishima | Akoudjikichima | /akɯdʑikiɕima/ | 4 | 18 | *auto* |
| Danshui | Dann-chouéï | /tanʂwei/ | 0 | 22 | chinois |
| Tokyo | Tôkyô | /toːkʲoː/ | 14 | 5 |  |
| Kirigan | Kirigann | /kiɾiɡaɴ/ | 0 | 16 |  |
| Kanto | Kanntô | /kantoː/ | 10 | 4 |  |
| Hokkaido | Hokkaïdô | /hokkaidoː/ | 11 | 3 |  |
| Okinawa | Okinawa | /okinawa/ | 9 | 0 | *auto* |
| Rebun | Rébounn | /ɾebɯɴ/ | 8 | 0 |  |
| Sogakishi | Sogakichi | /soɡakiɕi/ | 7 | 0 | *auto* |
| Taipei | Taïpèï | /tʰaipei/ | 0 | 6 |  |
| Izu | Izou | /izɯ/ | 5 | 0 | *auto* |
| Kyoto | Kyôto | /kʲoːto/ | 2 | 3 |  |
| Ginza | Guinnza | /ɡinza/ | 3 | 1 | *auto* |
| Atami | Atami | /atami/ | 3 | 0 | *auto* |
| Kansai | Kannsaï | /kansai/ | 2 | 0 | *auto* |
| Sapporo | Sapporo | /sappoɾo/ | 2 | 0 | *auto* |
| Yonaguni | Yonagouni | /jonaɡɯni/ | 2 | 0 | *auto* |
| Azukishima | Azoukichima | /azɯkiɕima/ | 1 | 1 | *auto* |
| Toraian | Toraïann | /toɾaiaɴ/ | 2 | 0 |  |
| Qilian | Tchi-liènn | /tɕʰiljɛn/ | 0 | 2 | chinois (Q = « tch ») |
| Delzney | Dèlzni | /dɛlzni/ | 1 | 1 | parodie de Disney |
| Hawaï | *(lecture française)* |  | 1 | 1 | lecture française |
| Kyushu | Kyoushou | /kʲɯːɕɯː/ | 0 | 1 |  |
| Narita | Narita | /naɾita/ | 0 | 1 | *auto* |
| Yokosuka | Yokossouka | /jokosɯka/ | 0 | 1 | *auto* |
| Shimoda | Chimoda | /ɕimoda/ | 1 | 0 | *auto* |
| Shikinejima | Chikinédjima | /ɕikinedʑima/ | 1 | 0 | *auto* |
| Sekihai | Sékihaï | /sekihai/ | 0 | 1 | *auto* |
| Zhuoshui | Djouo-chouéï | /ʈʂwoʂwei/ | 0 | 1 | chinois |
| Kaoping | Kao-pinng | /kʰaopʰiŋ/ | 0 | 1 | chinois |
| Zengwun | Dzeng-ouenn | /tsəŋwən/ | 0 | 1 | chinois |
| Dajia | Da-djia | /tatɕja/ | 0 | 1 | chinois |
| Dadu | Da-dou | /tatu/ | 0 | 1 | chinois |
| Saipan | Saïpann | /sajpan/ | 0 | 1 |  |
| Guam | Gouam | /ɡwam/ | 0 | 1 |  |

## Mots japonais

| Graphie | Prononciation | API | Q | R | Note |
|---|---|---|---:|---:|---|
| san | sann | /saɴ/ | 1474 | 1023 | suffixe (Battler-san) : « sann », jamais « sans » |
| chan | tchann | /tɕaɴ/ | 695 | 480 |  |
| sama | sama | /sama/ | 700 | 429 |  |
| kun | kounn | /kɯɴ/ | 567 | 230 |  |
| onee | oné | /oneː/ | 259 | 77 |  |
| aniki | aniki | /aniki/ | 285 | 49 | *auto* |
| nii | nii | /niː/ | 256 | 60 | nii-san, onii-chan |
| Onii | onii | /oniː/ | 33 | 180 |  |
| Nee | né | /neː/ | 87 | 44 |  |
| miko | miko | /miko/ | 0 | 54 | *auto* |
| Aneki | anéki | /aneki/ | 28 | 17 |  |
| sensei | sennsé | /senseː/ | 0 | 35 |  |
| oden | odénn | /odeɴ/ | 13 | 0 |  |
| shogi | chôgui | /ɕoːɡi/ | 3 | 9 |  |
| umeboshi | oumébochi | /ɯmeboɕi/ | 0 | 9 | *auto* |
| konpeito | konnpéïtô | /kompeːtoː/ | 2 | 7 |  |
| shiritori | chiritori | /ɕiɾitoɾi/ | 8 | 0 | *auto* |
| miso | misso | /miso/ | 0 | 8 |  |
| kanji | kanndji | /kaɴdʑi/ | 4 | 3 | *auto* |
| shinto | chinntô | /ɕintoː/ | 4 | 2 |  |
| Kaiten | Kaïténn | /kaiteɴ/ | 0 | 6 | *auto* |
| Sengoku | Sénngokou | /seŋɡokɯ/ | 4 | 2 | *auto* |
| Showa | Chôwa | /ɕoːwa/ | 5 | 0 |  |
| futon | foutonn | /ɸɯtoɴ/ | 2 | 2 |  |
| katakana | katakana | /katakana/ | 4 | 0 | *auto* |
| shugenja | chouguénndja | /ɕɯɡeɴdʑa/ | 2 | 2 | *auto* |
| tsume | tsoumé | /tsɯme/ | 0 | 4 | *auto* |
| Taishou | Taïchô | /taiɕoː/ | 1 | 3 |  |
| gomashio | gomachio | /ɡomaɕio/ | 0 | 3 | *auto* |
| tofu | tôfou | /toːɸɯ/ | 0 | 3 |  |
| Obon | Obonn | /oboɴ/ | 3 | 0 |  |
| Inari | Inari | /inaɾi/ | 3 | 0 | *auto* |
| tsundora | tsounndora | /tsɯndoɾa/ | 1 | 2 |  |
| konpeitou | konnpéïtô | /kompeːtoː/ | 0 | 2 |  |
| shimesaba | chiméssaba | /ɕimesaba/ | 2 | 0 | *auto* |
| daifuku | daïfoukou | /daiɸɯkɯ/ | 1 | 1 | *auto* |
| hassaku | hassakou | /hassakɯ/ | 0 | 2 | *auto* |
| shamisen | chamissénn | /ɕamiseɴ/ | 0 | 2 | *auto* |
| tanuki | tanouki | /tanɯki/ | 2 | 0 | *auto* |
| hiragana | hiragana | /çiɾaɡana/ | 2 | 0 | *auto* |
| katana | katana | /katana/ | 2 | 0 | *auto* |
| amanojaku | amanodjakou | /amanodʑakɯ/ | 0 | 2 | *auto* |
| Orihime | Orihimé | /oɾiçime/ | 0 | 2 | *auto* |
| Hikoboshi | Hikobochi | /çikoboɕi/ | 0 | 2 | *auto* |
| Taisho | Taïchô | /taiɕoː/ | 2 | 0 |  |
| senpai | sennpaï | /sempai/ | 0 | 1 |  |
| kotatsu | kotatsou | /kotatsɯ/ | 1 | 0 | *auto* |
| sashimi | sachimi | /saɕimi/ | 1 | 0 | *auto* |
| yakisoba | yakissoba | /jakisoba/ | 1 | 0 | *auto* |
| bento | bénntô | /bentoː/ | 1 | 0 |  |
| gyoza | guyôza | /ɡʲoːza/ | 0 | 1 |  |
| yokan | yôkann | /joːkaɴ/ | 0 | 1 |  |
| mirin | mirinn | /miɾiɴ/ | 0 | 1 | *auto* |
| nukamiso | noukamisso | /nɯkamiso/ | 0 | 1 | *auto* |
| donburi | donnbouri | /dombɯɾi/ | 0 | 1 | *auto* |
| chazuke | tchazouké | /tɕazɯke/ | 1 | 0 |  |
| hijiki | hidjiki | /çidʑiki/ | 0 | 1 | *auto* |
| kikurage | kikouragué | /kikɯɾaɡe/ | 1 | 0 | *auto* |
| shochu | chôtchou | /ɕoːtɕɯː/ | 1 | 0 |  |
| omurice | omouraïssou | /omɯɾaisɯ/ | 1 | 0 |  |
| yôkai | yôkaï | /joːkai/ | 1 | 0 |  |
| naginata | naguinata | /naɡinata/ | 0 | 1 | *auto* |
| yamabushi | yamabouchi | /jamabɯɕi/ | 1 | 0 | *auto* |
| kitsune | kitsouné | /kitsɯne/ | 1 | 0 | *auto* |
| seiza | séza | /seːza/ | 1 | 0 |  |
| omiai | omiaï | /omiai/ | 1 | 0 |  |
| ohajiki | ohadjiki | /ohadʑiki/ | 1 | 0 | *auto* |
| Tanabata | Tanabata | /tanabata/ | 0 | 1 | *auto* |
| kenpo | kennpô | /kempoː/ | 0 | 1 |  |
| Shinkansen | Chinnkannsénn | /ɕiŋkanseɴ/ | 1 | 0 | *auto* |
| Meiji | Mèïdji | /meːdʑi/ | 1 | 0 |  |
| Jomon | Djômonn | /dʑoːmoɴ/ | 1 | 0 |  |

## Histoire et culture japonaises

| Graphie | Prononciation | API | Q | R | Note |
|---|---|---|---:|---:|---|
| Purupuru | Pouroupourou | /pɯɾɯpɯɾɯ/ | 0 | 8 | *auto* |
| Takeda | Takéda | /takeda/ | 2 | 2 | *auto* |
| Shingen | Chinnguénn | /ɕiŋɡeɴ/ | 3 | 1 | *auto* |
| Piko | Piko | /piko/ | 0 | 4 | *auto* |
| Toyotomi | Toyotomi | /tojotomi/ | 2 | 1 | *auto* |
| Pikopuyo | Pikopouyo | /pikopɯjo/ | 0 | 3 | *auto* |
| Hidetsugu | Hidétsougou | /çidetsɯɡɯ/ | 0 | 2 | *auto* |
| Oda | Oda | /oda/ | 0 | 2 | *auto* |
| Nobunaga | Nobounaga | /nobɯnaɡa/ | 0 | 2 | *auto* |
| Shibata | Chibata | /ɕibata/ | 0 | 2 | *auto* |
| Hijikata | Hidjikata | /çidʑikata/ | 0 | 2 | *auto* |
| Souji | Sôdji | /soːdʑi/ | 0 | 2 |  |
| Higurashi | Higourachi | /çiɡɯɾaɕi/ | 2 | 0 | *auto* |
| Umineko | Ouminéko | /ɯmineko/ | 1 | 1 | *auto* |
| Hideyori | Hidéyori | /çidejoɾi/ | 0 | 1 | *auto* |
| Katsuie | Katsouié | /katsɯie/ | 0 | 1 |  |
| Uesugi | Ouéssougui | /ɯesɯɡi/ | 0 | 1 |  |
| Tokugawa | Tokougawa | /tokɯɡawa/ | 0 | 1 | *auto* |
| Akechi | Akétchi | /aketɕi/ | 0 | 1 | *auto* |
| Mōri | Môri | /moːɾi/ | 0 | 1 |  |
| Kondo | Kondô | /kondoː/ | 0 | 1 |  |
| Shotoku | Chôtokou | /ɕoːtokɯ/ | 1 | 0 |  |
| Taishi | Taïchi | /taiɕi/ | 1 | 0 | *auto* |
| Sakaguchi | Sakagoutchi | /sakaɡɯtɕi/ | 0 | 1 | *auto* |
| Ango | Anngo | /aŋɡo/ | 0 | 1 |  |
| Ayatsuji | Ayatsoudji | /ajatsɯdʑi/ | 0 | 1 | *auto* |
| Yukito | Youkito | /jɯkito/ | 0 | 1 | *auto* |
| Onikakushi | Onikakouchi | /onikakɯɕi/ | 1 | 0 | *auto* |
| Oyashiro | Oyachiro | /ojaɕiɾo/ | 1 | 0 | *auto* |
| Kamehameha | Kaméhaméha | /kamehameha/ | 1 | 0 | *auto* |
| Tenkaichi | Ténnkaïtchi | /teŋkaitɕi/ | 1 | 0 | *auto* |
| Budokai | Boudôkaï | /bɯdoːkai/ | 1 | 0 |  |
| Chiru | Tchirou | /tɕiɾɯ/ | 0 | 1 | *auto* |
| Pikomaru | Pikomarou | /pikomaɾɯ/ | 0 | 1 | *auto* |
| Momotarou | Momotarô | /momotaɾoː/ | 0 | 1 | *auto* |

## Expressions et mots anglais

| Graphie | Prononciation | API | Q | R | Note |
|---|---|---|---:|---:|---|
| Good | Goud | /ɡud/ | 1 | 45 |  |
| fantasy | fanntazi | /fantazi/ | 10 | 32 | « anti-fantasy » |
| quiz | kouiz | /kwiz/ | 0 | 26 |  |
| the | ze | /zə/ | 4 | 16 |  |
| whydunit | ouaïdounit | /waɪdʌnɪt/ | 0 | 19 | « pourquoi » |
| you | you | /ju/ | 10 | 7 |  |
| whodunit | houdounit | /huːdʌnɪt/ | 0 | 13 | « qui l'a fait » |
| howdunit | haoudounit | /haʊdʌnɪt/ | 0 | 12 | « comment » |
| Happy | Happi | /api/ | 9 | 3 |  |
| game | guéïm | /ɡɛjm/ | 5 | 6 | game over |
| over | ovère | /ovɛʁ/ | 5 | 6 |  |
| trick | trik | /tʁik/ | 7 | 3 | trick or treat |
| Death | Dèss | /dɛs/ | 0 | 10 |  |
| treat | trit | /tʁit/ | 7 | 1 |  |
| knock | nok | /nɔk/ | 0 | 8 | knock, knock |
| Endless | Ènndlèss | /ɛndlɛs/ | 1 | 6 | Endless Nine |
| Nine | Naïne | /najn/ | 1 | 6 |  |
| thank | sank | /sank/ | 4 | 3 | thank you |
| copy | kopi | /kɔpi/ | 0 | 7 |  |
| Mrs | Missiz | /misiz/ | 0 | 6 |  |
| week | ouik | /wik/ | 4 | 1 | week-end |
| Tea | Ti | /ti/ | 4 | 0 | Tea Party |
| Party | Parti | /paʁti/ | 4 | 0 |  |
| cute | kiout | /kjut/ | 0 | 4 |  |
| Witch | Ouitch | /witʃ/ | 1 | 3 |  |
| Dawn | Done | /dɔn/ | 0 | 4 |  |
| warp | ouorp | /wɔʁp/ | 0 | 4 |  |
| Zodiac | Zodiak | /zodjak/ | 0 | 4 |  |
| Mister | Mistère | /mistɛʁ/ | 0 | 3 |  |
| Die | Daï | /daj/ | 0 | 3 |  |
| perfect | peurfèkt | /pœʁfɛkt/ | 1 | 2 |  |
| light | laït | /lajt/ | 1 | 2 | light novel |
| Equalizer | Ikoualaïzeur | /ikwalajzœʁ/ | 0 | 3 |  |
| novel | novèl | /nɔvɛl/ | 1 | 1 |  |
| cheesecake | chizkèk | /ʃizkɛk/ | 2 | 0 |  |
| donut | donute | /donœt/ | 1 | 1 |  |
| scone | skonne | /skɔn/ | 0 | 2 |  |
| scones | skonnes | /skɔn/ | 0 | 2 |  |
| Gatekeeper | Guèïtkipeur | /ɡɛjtkipœʁ/ | 2 | 0 |  |
| Turn | Teurn | /tœʁn/ | 1 | 1 |  |
| pancakes | pannkèk | /pankɛk/ | 1 | 0 |  |
| Checkmate | Tchèkmèït | /tʃɛkmɛjt/ | 0 | 1 |  |
| Steam | Stim | /stim/ | 1 | 0 |  |

## Personnes et œuvres réelles ou citées

| Graphie | Prononciation | API | Q | R | Note |
|---|---|---|---:|---:|---|
| Hempel | Hèmpel | /ɛmpɛl/ | 15 | 2 | corbeau de Hempel |
| Dine | Daïne | /dajn/ | 1 | 11 | S.S. Van Dine |
| Eiserne | Aïzèrne | /ajzɛʁnə/ | 0 | 10 | Eiserne Jungfrau |
| Jungfrau | Younngfraou | /jʊŋfʁaʊ/ | 0 | 10 |  |
| Rubens | Roubènss | /ʁubɛ̃s/ | 0 | 7 |  |
| Wukong | Wou-kong | /uːkʊŋ/ | 0 | 7 | Sun Wukong |
| Pendragon | Pènndragonn | /pɛndʁaɡɔn/ | 6 | 0 |  |
| Christie | Kristi | /kʁisti/ | 1 | 4 |  |
| Dimbula | Dimmboula | /dimbula/ | 0 | 4 | thé de Ceylan |
| Agatha | Agata | /aɡata/ | 0 | 3 |  |
| Schrödinger | Chreudinguère | /ʃʁødiŋɛʁ/ | 3 | 0 |  |
| Dante | Dannté | /dante/ | 0 | 3 |  |
| Tokarev | Tokarèv | /tokaʁɛf/ | 0 | 3 |  |
| Salò | Salo | /salo/ | 0 | 3 |  |
| Ellery | Èleri | /ɛləʁi/ | 0 | 2 |  |
| Queen | Kouine | /kwin/ | 0 | 2 |  |
| Watson | Ouatsonn | /watsɔn/ | 0 | 2 |  |
| Mussolini | Moussolini | /musolini/ | 0 | 2 |  |
| Kasparov | Kasparof | /kaspaʁɔf/ | 1 | 1 |  |
| Sachertorte | Zakhèrtorté | /zaxɐtɔʁtə/ | 0 | 2 |  |
| Mytyl | Mitil | /mitil/ | 1 | 1 |  |
| Publius | Poubliouss | /publius/ | 0 | 2 |  |
| Maro | Maro | /maʁo/ | 0 | 2 |  |
| Ackroyd | Akroïd | /akʁɔjd/ | 0 | 1 |  |
| Holmes | Holmz | /ɔlmz/ | 0 | 1 |  |
| Alighieri | Aliguièri | /aliɡjɛʁi/ | 0 | 1 |  |
| Shakespeare | Chèkspir | /ʃɛkspiʁ/ | 0 | 1 |  |
| MacArthur | Makarseur | /makaʁsœʁ/ | 1 | 0 |  |
| Tyltyl | Tiltil | /tiltil/ | 1 | 0 |  |
| Humpty | Heumpti | /œmpti/ | 1 | 0 |  |
| Dumpty | Deumpti | /dœmpti/ | 1 | 0 |  |

## Onomatopées

Motifs (expressions régulières, mot entier) et lecture conseillée.

| Motif | Lecture | Occ. | Note |
|---|---|---:|---|
| `[Uu]u+-?` | Ouu | 1152 | tic de Maria (うー) : « ou » prolongé, jamais « u » français |
| `[Uu]ryu+` | Ouryou | 200 | tic de Sakutarou |
| `[Kk]ih+i(?:h?hi)*` | Ki-hi-hi | 168 | rire de Beatrice (h expiré) |
| `[Ii]hi(?:hi)*` | I-hi-hi | 75 | ricanement (h expiré) |
| `[Nn]ihi(?:hi)*` | Ni-hi-hi | 34 | rire de Lambdadelta |
| `[Kk]yaha(?:ha)*` | Kya-ha-ha | 7 | rire aigu |
| `[Kk]ya+h?` | Kyah | 66 | petit cri |
| `[Hh]ya+h?` | Hyah | 123 | cri d'effort |
| `[Gg]ya+h*` | Guyah | 41 | cri de douleur |
| `[Kk]u+h` | Kouh | 25 | grimace (くっ) |
| `[Ff]u+h?` | Fouh | 39 | soupir, rire bref |
| `[Gg]uh` | Gouh | 10 | grognement |
| `[Uu]kyu+` | Oukyou | 6 | petit cri plaintif |
| `[Kk]yu+` | Kyou | 12 | petit cri |
| `[Aa]u(?:au)+` | Aou-aou | 5 | bredouillement (あうあう) |
| `[Aa]wa(?:wa)+` | Awa-wa | 7 | panique (あわわ) |
| `[Nn]+[gh]+` | Nngh | 140 | gémissement : souffle nasal, ne pas épeler |
| `[Hh]m+[hpf]*` | Hmm | 390 | réflexion ou dédain (Hmph, Hmpf) |
| `[Tt]ch` | Tch | 33 | claquement de langue (ちっ) |
| `[Nn]yeh\|[Nn]ihe` | Nyé | 70 | tic de Chiester 410 |
| `[Ww]a+h+` | Wah | 188 | surprise |

Les autres cris (« Gwaaaah », « Nngyaaaah », « Wouaaah »…) sont des centaines de variantes uniques : les laisser lire tels quels, ou les remplacer par des sons enregistrés.

## Prétraitement du texte

| Règle | Motif | Action |
|---|---|---|
| Balises du script | `#[0-9a-fA-F]{6}\|</?i>\|~ib~\|\{[^}]*\}` | supprimer avant synthèse (couleurs des vérités rouge/bleue/violette/dorée, italique, marques internes). |
| Kanji entre parenthèses | `\s*[（(][　-鿿＀-￯]+[)）]` | supprimer : le texte donne parfois le kanji après la lecture, ex. « Belne (鐘音) ». |
| Caractères pleine chasse | `[！-～]` | normaliser en NFKC (« Ｅｘｅｃｕｔｅｄ » → « Executed »), puis lire en anglais. |
| Passages en langue étrangère | `<[^<>]+>\|『[^』]*』` | le texte entre < > est en anglais (ou en italien pour Bice), celui entre 『 』 en italien : basculer la voix dans cette langue (SSML <lang xml:lang="en-US"> / "it-IT"), ou garder la voix française si le moteur ne le permet pas. |
| Guillemets de citation | ``([^`']+)'` | `mot' marque un mot cité ou une pensée : retirer les signes, garder le mot. |
| Honorifiques après trait d'union | `(?<=-)(san\|chan\|sama\|kun\|senpai\|sensei\|nii\|nee)\b` | lire le suffixe à part avec l'entrée correspondante (Battler-san → « Batlèr sann ») ; « san » ne doit jamais devenir « sans ». |
| Lettres étirées | `([^\W\d_])\1{2,}` | cris et appels étirés (Battleeeer, Beatriiiice, Geooorge) : réduire la répétition à une lettre pour retrouver l'entrée (Battler), puis allonger la syllabe par la prosodie (SSML <prosody rate="slow">) plutôt qu'en épelant. |
| Mots en capitales | `\b[A-ZÀ-Ý]{3,}\b` | les capitales marquent un cri ou l'insistance de Dlanor (EVA, KNOX, PAS) : lire comme le mot en minuscules. Seuls les sigles ci-dessous s'épellent. |
| Sigles à épeler | `\b(GHQ\|SSVD\|RSI\|KGB\|VIP\|PDG\|CQFD\|SOS\|CD\|UV\|SARL\|IME\|CP\|FDT\|DZL)\b` | épeler lettre par lettre (NASA et OK se lisent comme des mots). |
