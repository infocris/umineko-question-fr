# Traduction des fiches personnages et des pages « Infos » (Tips)

Chaque page est une image de texte anglais. Le texte a été lu par OCR (bloc ``` dans le lot) :
il contient des erreurs (lettres confondues, `!` lu `l`, mots manquants, lignes vides en trop
dans les pages d'Infos). **Ouvre l'aperçu PNG (Read tool) dès qu'un passage semble douteux**,
et systématiquement pour les pages d'Infos (type `tips`), pour retrouver le vrai texte et la
vraie structure (titres, paragraphes).

## Sortie : un fichier texte par page, `work/pages/fr/<hash>.txt`, UTF-8

- Ligne commençant par `# ` : **titre** (texte plus grand). Fiches (`cha`) : la première ligne
  est toujours le nom du personnage → `# Ushiromiya Kinzo`. Infos (`tips`) : mets `# ` seulement
  si la page a un titre visible plus grand sur l'aperçu.
- Une **ligne vide** = séparation de paragraphe (comme dans l'image).
- Un **retour à la ligne simple** = l'anglais commence une nouvelle ligne sans ligne vide
  (phrase qui repart à la ligne). Ne recopie PAS les coupures de ligne dues à la largeur de
  l'image : écris chaque phrase/groupe d'un seul tenant, le moteur de rendu recoupe tout seul.
- Ne mets ni numéro, ni balise, ni commentaire dans le fichier.

## Traduction

- Suis `STYLE.md` (racine du projet) : glossaire, noms propres, choix fixés (Terre dorée,
  Sorcière dorée, chambre close, porte-bonheur, Aigle à une aile…), typographie française
  (espace avant `! ? : ;`), pas de caractère `ᵉ` (écrire 19e).
- Les fiches parlent des personnages à la 3ᵉ personne, au présent, ton de notice concise.
  Les pages `_2` (citations, ex. Beatrice qui nargue le joueur) sont à la 1ʳᵉ personne : garde
  la voix du personnage (Beatrice tutoie le joueur ; Bernkastel aussi).
- Noms en ordre japonais comme l'anglais (« Ushiromiya Kinzo »). Garde -san, -sama, etc.
- L'épitaphe (pages d'Infos) : reprends **exactement** la version de `STYLE.md` / lot 03
  (« Vois la rivière aux ayus qui traverse mon pays natal bien-aimé. » …).
- Texte français un peu plus long que l'anglais : reste concis, l'espace est limité
  (une fiche fait ~16 lignes de ~55 caractères au maximum).
- Caractères autorisés : lettres latines accentuées, ponctuation courante, « » ’ … — et les
  chiffres. Pas d'emoji, pas de kanji sauf s'il y en a dans l'image.

## Contrôle

    python3 -I tools/pagecheck.py work/pages/batches/<N>.md

doit répondre OK (tous les fichiers présents, titre `# ` sur les fiches, caractères valides).
