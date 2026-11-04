#!/usr/bin/env python3
"""Dictionnaire phonétique des mots étrangers de la traduction, pour un moteur TTS français.

  mkphonetique.py [../umineko-answer-fr]

Source éditable : tools/phonetique.tsv (graphie, catégorie, prononciation, API, note).
Prononciation et API vides (et pas de note) : calculées depuis le romaji japonais.
Compte les occurrences dans la traduction des deux arcs (dernière surcouche gagnante) et écrit :
  tools/phonetique.json          entrées + règles de prétraitement
  tools/phonetique-alias.pls     lexique W3C PLS, substitution par graphie française (<alias>)
  tools/phonetique-api.pls       lexique W3C PLS, transcription API (<phoneme alphabet="ipa">)
  docs/PHONETIQUE.md             tableau lisible
"""
import json, re, sys, unicodedata
from xml.sax.saxutils import escape

V="aiueo"
SYL=["kya","kyu","kyo","gya","gyu","gyo","sha","shi","shu","she","sho","cha","chi","chu","che","cho","ja","ji","ju","je","jo","nya","nyu","nyo","hya","hyu","hyo","bya","byu","byo","pya","pyu","pyo","mya","myu","myo","rya","ryu","ryo","tsu","tsa","fu","fa","fi","fe","fo","wa","wo","we","wi","ya","yu","yo","ye"]
def syl(w):
    w=w.lower().replace("ō","oo").replace("ū","uu").replace("ô","oo").replace("û","uu").replace("â","aa").replace("ê","ee").replace("î","ii")
    out=[];i=0
    while i<len(w):
        if w[i]=="n" and (i+1==len(w) or (w[i+1] not in V+"y")):
            out.append("N");i+=1;continue
        if i+1<len(w) and w[i]==w[i+1] and w[i] not in V+"n":
            out.append("Q");i+=1;continue
        for L in (3,2,1):
            s=w[i:i+L]
            if (L>1 and s in SYL) or (len(s)==2 and s[0] in "kgsztdnhbpmr" and s[1] in V) or (L==1 and s in V):
                out.append(s);i+=L;break
        else:
            return None
    return out
FRC={"sh":"ch","ch":"tch","j":"dj","ts":"ts","f":"f","ky":"ky","gy":"guy","ny":"ny","hy":"hy","by":"by","py":"py","my":"my","ry":"ry","g":"g","s":"s","z":"z","t":"t","d":"d","n":"n","h":"h","b":"b","p":"p","m":"m","r":"r","k":"k","w":"w","y":"y","":""}
FRV={"a":"a","i":"i","u":"ou","e":"é","o":"o"}
def onset(s):
    for L in (2,1,0):
        if s[:L] in FRC and s[L:] in V and len(s)-L==1: return s[:L],s[L:]
    return None
def fr(w):
    S=syl(w)
    if not S: return None
    r="";prevv=None
    for k,s in enumerate(S):
        if s=="N": r+="nn" if k==len(S)-1 or S[k+1] not in ("Q",) else "nn"; prevv=None; continue
        if s=="Q": r+= "" ; prevv=None; cnt=True; continue
        c,v=onset(s)
        cc=FRC[c]
        if k>0 and S[k-1]=="Q": cc=(cc[0] if cc not in("tch",) else "t")+cc
        if c=="g" and v in "ei": cc="gu"
        if c=="s" and prevv: cc="ss"
        if c=="" and prevv and prevv+v in ("ou","oo","uu","ei","aa","ii","ee"):
            # voyelle longue
            if prevv+v in("ou","oo"): r=r[:-1]+"ô"; prevv="o"; continue
            if prevv+v=="uu": prevv="u"; continue
            if prevv+v=="ei": prevv="e"; continue
            if prevv+v in("aa","ii","ee"): prevv=v; continue
        if c=="" and prevv:
            vv={"a":"a","i":"ï","u":"ou","e":"é","o":"o"}[v]
            if prevv=="a" and v=="u": vv="ou"
            r+=vv
        else:
            r+=cc+FRV[v]
        prevv=v
    return r
IPAC={"sh":"ɕ","ch":"tɕ","j":"dʑ","ts":"ts","f":"ɸ","ky":"kʲ","gy":"ɡʲ","ny":"ɲ","hy":"ç","by":"bʲ","py":"pʲ","my":"mʲ","ry":"ɾʲ","g":"ɡ","r":"ɾ","y":"j","w":"w","":""}
def ipa(w):
    S=syl(w)
    if not S: return None
    r=[];prevv=None
    for k,s in enumerate(S):
        if s=="N":
            nx=S[k+1] if k+1<len(S) else ""
            r.append("m" if nx[:1] in "mpb" and nx else "ŋ" if nx[:1] in "kg" and nx else "n" if nx[:1] in "tdnrsz" and nx else "ɴ");prevv=None;continue
        if s=="Q": r.append("Q");prevv=None;continue
        c,v=onset(s)
        cc=IPAC.get(c,c)
        if c=="h" and v=="i": cc="ç"
        if c=="s" and v=="i": cc="ɕ"
        if c=="z" and v=="i": cc="dʑ"
        if c=="t" and v=="u": cc="ts"
        if r and r[-1]=="Q": r[-1]=cc[-1] if cc!="tɕ" else "t"
        if c=="" and prevv and prevv+v in("ou","oo","uu","ei","aa","ii","ee"):
            r.append("ː");prevv=None;continue
        r.append(cc+{"u":"ɯ"}.get(v,v));prevv=v
    return "".join(r)

REGLES = [
 {"nom": "Balises du script", "motif": r"#[0-9a-fA-F]{6}|</?i>|~ib~|\{[^}]*\}",
  "action": "supprimer avant synthèse (couleurs des vérités rouge/bleue/violette/dorée, italique, marques internes)."},
 {"nom": "Kanji entre parenthèses", "motif": r"\s*[（(][　-鿿＀-￯]+[)）]",
  "action": "supprimer : le texte donne parfois le kanji après la lecture, ex. « Belne (鐘音) »."},
 {"nom": "Caractères pleine chasse", "motif": r"[！-～]",
  "action": "normaliser en NFKC (« Ｅｘｅｃｕｔｅｄ » → « Executed »), puis lire en anglais."},
 {"nom": "Passages en langue étrangère", "motif": r"<[^<>]+>|『[^』]*』",
  "action": "le texte entre < > est en anglais (ou en italien pour Bice), celui entre 『 』 en italien : basculer la voix dans cette langue (SSML <lang xml:lang=\"en-US\"> / \"it-IT\"), ou garder la voix française si le moteur ne le permet pas."},
 {"nom": "Guillemets de citation", "motif": r"`([^`']+)'",
  "action": "`mot' marque un mot cité ou une pensée : retirer les signes, garder le mot."},
 {"nom": "Honorifiques après trait d'union", "motif": r"(?<=-)(san|chan|sama|kun|senpai|sensei|nii|nee)\b",
  "action": "lire le suffixe à part avec l'entrée correspondante (Battler-san → « Batlèr sann ») ; « san » ne doit jamais devenir « sans »."},
 {"nom": "Lettres étirées", "motif": r"([^\W\d_])\1{2,}",
  "action": "cris et appels étirés (Battleeeer, Beatriiiice, Geooorge) : réduire la répétition à une lettre pour retrouver l'entrée (Battler), puis allonger la syllabe par la prosodie (SSML <prosody rate=\"slow\">) plutôt qu'en épelant."},
 {"nom": "Mots en capitales", "motif": r"\b[A-ZÀ-Ý]{3,}\b",
  "action": "les capitales marquent un cri ou l'insistance de Dlanor (EVA, KNOX, PAS) : lire comme le mot en minuscules. Seuls les sigles ci-dessous s'épellent."},
 {"nom": "Sigles à épeler", "motif": r"\b(GHQ|SSVD|RSI|KGB|VIP|PDG|CQFD|SOS|CD|UV|SARL|IME|CP|FDT|DZL)\b",
  "action": "épeler lettre par lettre (NASA et OK se lisent comme des mots)."},
]
ONOMATOPEES = [
 # (motif, lecture, note)
 (r"[Uu]u+-?", "Ouu", "tic de Maria (うー) : « ou » prolongé, jamais « u » français"),
 (r"[Uu]ryu+", "Ouryou", "tic de Sakutarou"),
 (r"[Kk]ih+i(?:h?hi)*", "Ki-hi-hi", "rire de Beatrice (h expiré)"),
 (r"[Ii]hi(?:hi)*", "I-hi-hi", "ricanement (h expiré)"),
 (r"[Nn]ihi(?:hi)*", "Ni-hi-hi", "rire de Lambdadelta"),
 (r"[Kk]yaha(?:ha)*", "Kya-ha-ha", "rire aigu"),
 (r"[Kk]ya+h?", "Kyah", "petit cri"),
 (r"[Hh]ya+h?", "Hyah", "cri d'effort"),
 (r"[Gg]ya+h*", "Guyah", "cri de douleur"),
 (r"[Kk]u+h", "Kouh", "grimace (くっ)"),
 (r"[Ff]u+h?", "Fouh", "soupir, rire bref"),
 (r"[Gg]uh", "Gouh", "grognement"),
 (r"[Uu]kyu+", "Oukyou", "petit cri plaintif"),
 (r"[Kk]yu+", "Kyou", "petit cri"),
 (r"[Aa]u(?:au)+", "Aou-aou", "bredouillement (あうあう)"),
 (r"[Aa]wa(?:wa)+", "Awa-wa", "panique (あわわ)"),
 (r"[Nn]+[gh]+", "Nngh", "gémissement : souffle nasal, ne pas épeler"),
 (r"[Hh]m+[hpf]*", "Hmm", "réflexion ou dédain (Hmph, Hmpf)"),
 (r"[Tt]ch", "Tch", "claquement de langue (ちっ)"),
 (r"[Nn]yeh|[Nn]ihe", "Nyé", "tic de Chiester 410"),
 (r"[Ww]a+h+", "Wah", "surprise"),
]

def charge(repo):
    eff = {}
    for f in open(repo + "/mod/translations.txt", encoding="utf-8"):
        f = f.strip()
        if not f or f.startswith("#"):
            continue
        for l in open(repo + "/" + f, encoding="utf-8"):
            d = json.loads(l)
            if "fr" in d:
                eff[d["id"]] = d["fr"]
    return "\n".join(unicodedata.normalize("NFC", " ".join(s)) for s in eff.values())

def main():
    autre = sys.argv[1] if len(sys.argv) > 1 else "../umineko-answer-fr"
    textes = {"Q": charge("."), "R": charge(autre)}
    E, vus, section = [], set(), None
    for l in open("tools/phonetique.tsv", encoding="utf-8"):
        l = l.rstrip("\n")
        if not l or l.startswith("# "):
            continue
        if l.startswith("## "):
            section = l[3:]
            continue
        g, cat, pr, ap, note = (l.split("\t") + [""] * 5)[:5]
        if g in vus:
            continue
        vus.add(g)
        e = {"graphie": g, "section": section, "categorie": cat}
        if not pr and not note:
            pr, ap = fr(g), ipa(g)
            if not pr:
                sys.exit(f"romaji illisible : {g}")
            if g[0].isupper():
                pr = pr[0].upper() + pr[1:]
            e["auto"] = True
        if pr:
            e["prononciation"], e["api"] = pr, ap
        else:
            e["lecture_francaise"] = True
        if note:
            e["note"] = note
        rx = re.compile(r"(?<![^\W\d_])" + re.escape(g) + r"(?![^\W\d_])", 0 if g[0].isupper() else re.I)
        n = {a: len(rx.findall(t)) for a, t in textes.items()}
        e["occurrences"] = {"Q": n["Q"], "R": n["R"]}
        E.append(e)
    ono = []
    for m, lec, note in ONOMATOPEES:
        rx = re.compile(r"(?<![^\W\d_])(?:" + m + r")(?![^\W\d_])")
        ono.append({"motif": m, "lecture": lec, "note": note,
                    "occurrences": sum(len(rx.findall(t)) for t in textes.values())})
    doc = ("Dictionnaire phonétique des mots étrangers de la traduction (épisodes 1-8) pour un moteur TTS "
           "français. prononciation = graphie à substituer, lisible par une voix française ; api = transcription "
           "API (japonais : prononciation d'origine). lecture_francaise = la lecture française par défaut est la bonne. "
           "occurrences : Q = épisodes 1-4, R = épisodes 5-8. Généré par tools/mkphonetique.py depuis tools/phonetique.tsv.")
    json.dump({"_doc": doc, "regles": REGLES, "onomatopees": ono, "entrees": E},
              open("tools/phonetique.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for nom, kind in (("alias", "alias"), ("api", "ipa")):
        L = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<lexicon version="1.0" xmlns="http://www.w3.org/2005/01/pronunciation-lexicon"',
             '         alphabet="ipa" xml:lang="fr-FR">']
        for e in E:
            if e.get("lecture_francaise") or (kind == "ipa" and not e.get("api")):
                continue
            gs = [e["graphie"]] + ([e["graphie"].capitalize()] if e["graphie"].islower() else [])
            val = e["prononciation"] if kind == "alias" else e["api"]
            tag = f"<alias>{escape(val)}</alias>" if kind == "alias" else f"<phoneme>{escape(val)}</phoneme>"
            L.append("  <lexeme>" + "".join(f"<grapheme>{escape(g)}</grapheme>" for g in gs) + tag + "</lexeme>")
        L.append("</lexicon>")
        open(f"tools/phonetique-{nom}.pls", "w", encoding="utf-8").write("\n".join(L) + "\n")
    md = ["# Dictionnaire phonétique (TTS)", "",
          "Prononciation des mots étrangers de la traduction (épisodes 1 à 8) pour une voix de synthèse française.",
          "Généré par `tools/mkphonetique.py` depuis `tools/phonetique.tsv` (à éditer), avec :", "",
          "- `tools/phonetique.json` : entrées, règles de prétraitement, onomatopées ;",
          "- `tools/phonetique-alias.pls` : lexique [PLS](https://www.w3.org/TR/pronunciation-lexicon/) par substitution "
          "(`<alias>`), le plus portable : la graphie proposée se lit correctement avec n'importe quelle voix française ;",
          "- `tools/phonetique-api.pls` : le même en API (`<phoneme>`), pour les moteurs qui l'acceptent.", "",
          "**Principes.** Les noms japonais suivent la prononciation des voix japonaises du jeu, adaptée au français : "
          "`u` → « ou », `e` → « é », `sh` → « ch », `ch` → « tch », `j` → « dj », `g` dur, `s` jamais « z », "
          "`n` final ou devant consonne doublé (« Kinnzô », « Kanonn ») pour éviter les voyelles nasales françaises, "
          "voyelles longues (`ou`, `oh`, `ō`) en « ô ». Les noms d'origine occidentale gardent la lecture de leur langue, "
          "comme dans le jeu : Beatrice à l'italienne (« Béatritché »), George et Jessica à l'anglaise, "
          "Bernkastel à l'allemande. Ange et Lion gardent leur lecture française.", "",
          "Occurrences : Q = épisodes 1-4, R = épisodes 5-8. « auto » = transcription calculée depuis le romaji.", ""]
    sec = None
    for e in sorted(E, key=lambda e: (list(dict.fromkeys(x["section"] for x in E)).index(e["section"]), -(e["occurrences"]["Q"] + e["occurrences"]["R"]))):
        if e["section"] != sec:
            sec = e["section"]
            md += ["", f"## {sec}", "", "| Graphie | Prononciation | API | Q | R | Note |", "|---|---|---|---:|---:|---|"]
        p = "*(lecture française)*" if e.get("lecture_francaise") else e["prononciation"]
        a = f"/{e['api']}/" if e.get("api") else ""
        note = e.get("note", "") + (" *auto*" if e.get("auto") else "")
        md.append(f"| {e['graphie']} | {p} | {a} | {e['occurrences']['Q']} | {e['occurrences']['R']} | {note.strip()} |")
    md += ["", "## Onomatopées", "", "Motifs (expressions régulières, mot entier) et lecture conseillée.", "",
           "| Motif | Lecture | Occ. | Note |", "|---|---|---:|---|"]
    for o in ono:
        md.append(f"| `{o['motif'].replace('|', chr(92) + '|')}` | {o['lecture']} | {o['occurrences']} | {o['note']} |")
    md += ["", "Les autres cris (« Gwaaaah », « Nngyaaaah », « Wouaaah »…) sont des centaines de variantes uniques : "
           "les laisser lire tels quels, ou les remplacer par des sons enregistrés.", "",
           "## Prétraitement du texte", "", "| Règle | Motif | Action |", "|---|---|---|"]
    for r in REGLES:
        md.append(f"| {r['nom']} | `{r['motif'].replace('|', chr(92) + '|')}` | {r['action']} |")
    open("docs/PHONETIQUE.md", "w", encoding="utf-8").write("\n".join(md) + "\n")
    print(len(E), "entrées,", len(ono), "onomatopées,", len(REGLES), "règles")

if __name__ == "__main__":
    main()
