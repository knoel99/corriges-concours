"""Fonctions pures de l'export : Markdown KaTeX → Markdown prêt pour pandoc, variables du
gabarit, lecture du journal lualatex, bilan. Aucun appel externe ici (voir `exporter.py`).
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

RESSOURCES = Path(__file__).resolve().parent / "ressources"
GABARIT = RESSOURCES / "corrige.latex"
FILTRE = RESSOURCES / "corrige.lua"

NATURES: dict[str, str] = {"brut": "Corrigé brut", "guide": "Corrigé guidé"}

# Lecture pandoc : maths `$…$`/`$$…$$` et `\(…\)` (produit par `normaliser_maths`), sans
# LaTeX ni HTML brut (le site les neutralise : le PDF doit montrer la même chose).
FORMAT_ENTREE = "markdown+tex_math_single_backslash-raw_tex-raw_html-raw_attribute"

# Même motif que `verifier.IMAGE` : texte alternatif à crochets échappés, titre optionnel.
_FIGURE_MD = re.compile(r'!\[(?:\\.|[^\]\\])*\]\((figures/[^)\s]+\.svg)(?:\s+"[^"]*")?\)')


# ---------------------------------------------------------------------------
# Fonctions pures
# ---------------------------------------------------------------------------


def echapper_latex(texte: str) -> str:
    """Échappe un texte brut pour l'insérer dans le gabarit (titre, matière…)."""
    remplacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(remplacements.get(c, c) for c in texte)


def _fin_code_en_ligne(texte: str, i: int) -> int:
    """Indice après un code en ligne qui commence en `i` (suite de backticks), ou -1."""
    n = 0
    while i + n < len(texte) and texte[i + n] == "`":
        n += 1
    fermeture = re.compile(r"(?<!`)" + "`" * n + r"(?!`)")
    m = fermeture.search(texte, i + n)
    return m.end() if m else -1


_COUPURES_MATHRM = ("\\longrightarrow", "\\rightleftharpoons", "\\rightarrow", "\\to", "+", "=")


def couper_mathrm(formule: str) -> str:
    """`\\mathrm{A + B = C}` → `\\mathrm{A} + \\mathrm{B} = \\mathrm{C}` (même rendu).

    Une équation chimique écrite d'un bloc dans `\\mathrm{…}` est un groupe : TeX ne
    peut pas la couper en fin de ligne et elle déborde dans la marge. Sortir les
    opérateurs de premier niveau du groupe rend les coupures possibles après `+`, `=`
    ou une flèche, sans changer l'affichage. Un `+` d'exposant (`HO^+`, `{+}`) reste.
    """
    coeur = formule.strip()
    if not coeur.startswith("\\mathrm{") or not coeur.endswith("}"):
        return formule
    interieur = coeur[len("\\mathrm{") : -1]
    profondeur, morceaux, debut, i = 0, [], 0, 0
    while i < len(interieur):
        c = interieur[i]
        if c == "\\":
            commande = next(
                (
                    op
                    for op in _COUPURES_MATHRM
                    if op.startswith("\\") and interieur.startswith(op, i)
                ),
                None,
            )
            if (
                commande
                and profondeur == 0
                and not interieur[i + len(commande) : i + len(commande) + 1].isalpha()
            ):
                morceaux += [interieur[debut:i], commande]
                i += len(commande)
                debut = i
                continue
            i += 2
            continue
        if c == "{":
            profondeur += 1
        elif c == "}":
            profondeur -= 1
            if profondeur < 0:
                return formule
        elif c in "+=" and profondeur == 0 and (i == 0 or interieur[i - 1] not in "^_"):
            morceaux += [interieur[debut:i], c]
            debut = i + 1
        i += 1
    if profondeur != 0 or not morceaux:
        return formule
    morceaux.append(interieur[debut:])
    sortie = []
    for k, morceau in enumerate(morceaux):
        if k % 2:
            sortie.append(f" {morceau} ")
        elif morceau.strip():
            sortie.append("\\mathrm{" + morceau.strip() + "}")
    return "".join(sortie).strip()


_COMMANDE_ARGUMENT = re.compile(
    r"([_^])\s*(\\(?:mathcal|mathbb|mathrm|mathbf|mathscr|mathfrak|mathsf|mathtt|mathit"
    r"|boldsymbol|text|textrm|textbf|textit|operatorname|vec|hat|bar|tilde|overline)\s*)\{"
)


def proteger_indices(formule: str) -> str:
    """`x_\\mathcal{C}` → `x_{\\mathcal{C}}` : KaTeX l'accepte, LaTeX (unicode-math) non."""
    morceaux: list[str] = []
    debut = 0
    for m in _COMMANDE_ARGUMENT.finditer(formule):
        if m.start() < debut:
            continue
        # Fin de l'argument entre accolades (équilibré).
        profondeur, j = 0, m.end() - 1
        while j < len(formule):
            c = formule[j]
            if c == "\\":
                j += 2
                continue
            if c == "{":
                profondeur += 1
            elif c == "}":
                profondeur -= 1
                if profondeur == 0:
                    break
            j += 1
        if j >= len(formule):
            continue
        morceaux += [formule[debut : m.start()], m.group(1), "{", formule[m.start(2) : j + 1], "}"]
        debut = j + 1
    morceaux.append(formule[debut:])
    resultat = "".join(morceaux)
    # Une commande peut en contenir une autre (`_\\text{\\mathrm{…}}` n'arrive pas, mais
    # `_\\vec{x}_\\mathrm{a}` si) : une seconde passe ne change rien d'autre.
    return resultat if resultat == formule else proteger_indices(resultat)


_MOT_ACCENTUE = re.compile(r"(?<![\\A-Za-z])[A-Za-zÀ-ÖØ-öø-ÿœŒ]*[À-ÖØ-öø-ÿœŒ][A-Za-zÀ-ÖØ-öø-ÿœŒ]*")


def accents_en_texte(formule: str) -> str:
    """Mot accentué dans une formule (`E_{consommée}`) → `\\text{consommée}`.

    KaTeX affiche ces lettres en police de texte ; en mode mathématique LaTeX, elles
    n'existent pas dans la police (glyphe perdu). Un `\\text{…}` redondant est sans effet.
    """
    return _MOT_ACCENTUE.sub(lambda m: "\\text{" + m.group(0) + "}", formule)


_ALPHABETS = "mathrm|mathcal|mathbb|mathbf|mathscr|mathfrak|mathsf|mathtt|mathit|boldsymbol"
_INDICE_SANS_ACCOLADES = re.compile(
    rf"([_^])\s*(\\(?:{_ALPHABETS})\s*)([A-Za-z0-9]|\\[A-Za-z]+)(?![A-Za-z])"
)
_ALPHABET_OUVERT = re.compile(rf"\\(?:{_ALPHABETS})\s*\{{")


def _fin_groupe(formule: str, ouvrante: int) -> int:
    """Indice de l'accolade fermante appariée à celle en `ouvrante`, ou -1."""
    profondeur, j = 0, ouvrante
    while j < len(formule):
        c = formule[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            profondeur += 1
        elif c == "}":
            profondeur -= 1
            if profondeur == 0:
                return j
        j += 1
    return -1


def isoler_alphabets(formule: str) -> str:
    """Rend explicites deux tolérances de KaTeX que LaTeX (unicode-math) refuse.

    * `E_\\mathrm p` → `E_{\\mathrm p}` (argument d'indice sans accolades) ;
    * `\\mathrm{I_3^-}_{(aq)}` → `{\\mathrm{I_3^-}}_{(aq)}` : avec `mathrm=sym`,
      l'indice suivant s'accrocherait au dernier atome du groupe (« Double subscript »).
    """
    formule = _INDICE_SANS_ACCOLADES.sub(r"\1{\2\3}", formule)
    sortie, debut = [], 0
    for m in _ALPHABET_OUVERT.finditer(formule):
        if m.start() < debut:
            continue
        fin = _fin_groupe(formule, m.end() - 1)
        if fin < 0:
            continue
        suite = formule[fin + 1 :].lstrip()
        if suite[:1] in ("_", "^"):
            sortie += [formule[debut : m.start()], "{", formule[m.start() : fin + 1], "}"]
            debut = fin + 1
    sortie.append(formule[debut:])
    return "".join(sortie)


_DEBUT_ALIGNE = re.compile(r"(\\begin\{(?:aligned|alignedat|split)\}(?:\{\d+\})?)\s*&")


def proteger_debut_aligne(formule: str) -> str:
    """`\\begin{aligned}&…` → `\\begin{aligned}{}&…` (rendu inchangé).

    Passé en argument de `\\equationajustee`, un environnement dont la première cellule
    commence par `&` fait échouer lualatex (« Missing control sequence inserted »,
    `\\inaccessible`) : un groupe vide dans la cellule de gauche suffit à l'éviter.
    """
    return _DEBUT_ALIGNE.sub(lambda m: m.group(1) + "{}&", formule)


def ajuster_formule(formule: str) -> str:
    """Ajustements communs aux maths en ligne et hors texte (rendu inchangé)."""
    return accents_en_texte(isoler_alphabets(proteger_indices(proteger_debut_aligne(formule))))


def couper_listes(formule: str, seuil: int = 60) -> str:
    """Longue formule en ligne : coupure permise après les virgules de premier niveau.

    TeX ne coupe une formule en ligne qu'après un opérateur ou une relation ; une liste
    `\\{0,2\\},\\{0,3\\},…` déborde sinon (cellules de tableau surtout).
    """
    if len(formule) <= seuil:
        return formule
    sortie, profondeur, i = [], 0, 0
    while i < len(formule):
        c = formule[i]
        if c == "\\":
            sortie.append(formule[i : i + 2])
            i += 2
            continue
        if c == "{":
            profondeur += 1
        elif c == "}":
            profondeur -= 1
        sortie.append(c)
        if c == "," and profondeur == 0:
            sortie.append("\\allowbreak ")
        i += 1
    return "".join(sortie)


def _normaliser_paragraphe(texte: str) -> str:
    """Réécrit les maths en ligne `$…$` d'un paragraphe en `\\(…\\)`.

    Mêmes règles que remark-math (le rendu du site) : une paire de `$` simples délimite des
    maths quels que soient les espaces autour, `\\$` est un dollar littéral, le code en ligne
    est opaque. Pandoc, lui, refuse `$x $` ou `$x$2` : sans cette passe, ces formules
    sortiraient en texte brut. Les `$$…$$` sont laissés tels quels.
    """
    sortie: list[str] = []
    i, n = 0, len(texte)
    while i < n:
        c = texte[i]
        if c == "\\" and i + 1 < n:
            sortie.append(texte[i : i + 2])
            i += 2
            continue
        if c == "`":
            fin = _fin_code_en_ligne(texte, i)
            if fin < 0:
                j = i
                while j < n and texte[j] == "`":
                    j += 1
                sortie.append(texte[i:j])
                i = j
                continue
            sortie.append(texte[i:fin])
            i = fin
            continue
        if c == "$":
            if texte.startswith("$$", i):
                fin = texte.find("$$", i + 2)
                if fin < 0:
                    sortie.append(texte[i:])
                    break
                sortie.append("$$" + ajuster_formule(texte[i + 2 : fin]) + "$$")
                i = fin + 2
                continue
            # Dollar simple : chercher le prochain `$` simple non échappé.
            j = i + 1
            while j < n:
                if texte[j] == "\\":
                    j += 2
                    continue
                if texte[j] == "$":
                    break
                j += 1
            if j >= n or texte.startswith("$$", j):
                sortie.append(c)
                i += 1
                continue
            contenu = texte[i + 1 : j]
            coeur = contenu.strip()
            # Un `\ ` final (espace insécable LaTeX) ne doit pas perdre son espace.
            if coeur.endswith("\\"):
                coeur += " "
            if coeur:
                sortie.append("\\(" + couper_listes(couper_mathrm(ajuster_formule(coeur))) + "\\)")
            else:
                sortie.append(texte[i : j + 1])
            i = j + 1
            continue
        sortie.append(c)
        i += 1
    return "".join(sortie)


_CLOTURE = re.compile(r"^\s*(?:>\s*)*(`{3,}|~{3,})")
_DELIMITEUR_BLOC_MATH = re.compile(r"( {0,3}(?:> {0,3})*)\$\$[ \t]*")


def _fin_bloc_math(lignes: list[str], debut: int, citation: int) -> int | None:
    """Retrouve le délimiteur fermant avant une clôture de code ou un changement de citation."""
    for fin in range(debut + 1, len(lignes)):
        ligne = lignes[fin]
        if _CLOTURE.match(ligne):
            break
        if "$$" in ligne:
            delimiteur = _DELIMITEUR_BLOC_MATH.fullmatch(ligne)
            if delimiteur and delimiteur[1].count(">") == citation:
                return fin
            break
        if citation and re.match(r"^ *(?:> *)*", ligne)[0].count(">") != citation:
            break
    return None


def normaliser_maths(markdown: str) -> str:
    """Applique `_normaliser_paragraphe` hors des blocs de code, paragraphe par paragraphe."""
    lignes = markdown.split("\n")
    sortie: list[str] = []
    paragraphe: list[str] = []
    cloture: str | None = None

    def vider() -> None:
        if paragraphe:
            sortie.extend(_normaliser_paragraphe("\n".join(paragraphe)).split("\n"))
            paragraphe.clear()

    prochaine_ligne = 0
    for indice, ligne in enumerate(lignes):
        if indice < prochaine_ligne:
            continue
        m = _CLOTURE.match(ligne)
        if cloture is not None:
            sortie.append(ligne)
            if (
                m
                and m.group(1)[0] == cloture[0]
                and len(m.group(1)) >= len(cloture)
                and ligne.strip().lstrip(">").strip() == m.group(1)
            ):
                cloture = None
            continue
        if m:
            vider()
            cloture = m.group(1)
            sortie.append(ligne)
            continue
        delimiteur = _DELIMITEUR_BLOC_MATH.fullmatch(ligne)
        # Un délimiteur isolé peut aussi fermer une formule ouverte en fin de ligne.
        if delimiteur and sum(ligne_precedente.count("$$") for ligne_precedente in paragraphe) % 2 == 0:
            citation = delimiteur[1].count(">")
            fin = _fin_bloc_math(lignes, indice, citation)
            if fin is not None:
                # Pandoc ferme les maths au premier paragraphe vide. Garder les sauts
                # de ligne non vides, notamment après un commentaire TeX.
                formule = lignes[indice : fin + 1]
                vide = re.compile(r"[ \t]*" + r">[ \t]*" * citation).fullmatch
                contenu = formule[1:-1]
                if any(vide(ligne_math) for ligne_math in contenu) and any(not vide(ligne_math) for ligne_math in contenu):
                    paragraphe.extend(ligne_math for ligne_math in formule if not vide(ligne_math))
                    vider()
                    prochaine_ligne = fin + 1
                    continue
        if not ligne.strip() or ligne.strip(" >") == "":
            vider()
            sortie.append(ligne)
            continue
        paragraphe.append(ligne)
    vider()
    return "\n".join(sortie)


def extraire_titre(markdown: str) -> tuple[str, str]:
    """Sépare le titre `# …` de tête (repris par le gabarit) du reste du document."""
    lignes = markdown.split("\n")
    for k, ligne in enumerate(lignes):
        if not ligne.strip():
            continue
        if ligne.startswith("# "):
            return ligne[2:].strip(), "\n".join(lignes[k + 1 :]).lstrip("\n")
        break
    return "", markdown


def preparer_markdown(markdown: str) -> tuple[str, str]:
    """Titre + Markdown prêt pour pandoc (titre retiré, maths normalisées)."""
    titre, corps = extraire_titre(markdown)
    return titre, normaliser_maths(corps)


def figures_citees(markdown: str) -> list[str]:
    """Chemins `figures/<slug>/<nom>.svg` cités dans le Markdown, dans l'ordre, sans doublon."""
    vus: list[str] = []
    for m in _FIGURE_MD.finditer(markdown):
        if m.group(1) not in vus:
            vus.append(m.group(1))
    return vus




def variables_gabarit(meta: dict, nature: str, titre: str) -> dict[str, str]:
    """Variables pandoc (`-V`) du gabarit, déjà échappées pour LaTeX."""
    ep = meta.get("epreuve") or {}
    libelle = NATURES[nature]
    # La nature est déjà affichée au-dessus du titre : « … · Corrigé guidé » ferait doublon.
    titre = re.sub(r"\s*·\s*Corrigé(?:\s+(?:brut|guidé))?\s*$", "", titre, flags=re.I)
    titre = titre or f"{ep.get('concours', '')} {ep.get('filiere', '')} — {ep.get('matiere', '')}"
    variables = {
        "nature": libelle,
        "titre": echapper_latex(titre),
        "concours": echapper_latex(str(ep.get("concours", ""))),
        "filiere": echapper_latex(str(ep.get("filiere", ""))),
        "matiere": echapper_latex(str(ep.get("matiere", ""))),
        "annee": echapper_latex(str(ep.get("annee", ""))),
    }

    # Trente caractères latins, même aussi larges que W, laissent la place
    # au mode, à l’année et aux blancs dans les 16,6 cm du gabarit.
    # Garder le même .tex permet de réutiliser les PDF courts déjà compilés.
    libelles = "".join(str(ep.get(cle, "")) for cle in ("concours", "filiere", "matiere"))
    if not (
        re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9 .’'()/+-]{0,30}", libelles)
        and re.fullmatch(r"[0-9]{4}", variables["annee"])
    ):
        variables["mesurerentete"] = "true"
    return variables


_OVERFULL = re.compile(r"^Overfull \\[hv]box \(([\d.]+)pt too (?:wide|high)\)(.*)$", re.M)
_PAGES = re.compile(r"Output written on .*?\((\d+) pages?")


@dataclass
class Diagnostic:
    """Ce que le journal lualatex dit d'une compilation."""

    pages: int = 0
    missing_dollar: int = 0
    images_manquantes: list[str] = field(default_factory=list)
    caracteres_manquants: list[str] = field(default_factory=list)
    overfull: list[float] = field(default_factory=list)
    erreurs: list[str] = field(default_factory=list)

    def overfull_au_dela(self, seuil: float = 20.0) -> list[float]:
        return [x for x in self.overfull if x > seuil]

    @property
    def propre(self) -> bool:
        return (
            self.pages > 0
            and not self.missing_dollar
            and not self.images_manquantes
            and not self.caracteres_manquants
            and not self.erreurs
            and not self.overfull_au_dela()
        )


def analyser_journal(journal: str) -> Diagnostic:
    """Lit un `.log` lualatex : pages, « Missing $ », images absentes, débordements, erreurs."""
    d = Diagnostic()
    m = _PAGES.search(journal)
    if m:
        d.pages = int(m.group(1))
    d.missing_dollar = journal.count("Missing $ inserted")
    for m in re.finditer(r"File `([^']+)' not found", journal):
        d.images_manquantes.append(m.group(1))
    for m in re.finditer(r"Missing character: There is no (\S+)", journal):
        if m.group(1) not in d.caracteres_manquants:
            d.caracteres_manquants.append(m.group(1))
    d.overfull = [float(m.group(1)) for m in _OVERFULL.finditer(journal)]
    for m in re.finditer(r"^! (.+)$", journal, re.M):
        d.erreurs.append(m.group(1).strip())
    return d


@dataclass
class Resultat:
    slug: str
    nature: str
    tex: Path | None = None
    pdf: Path | None = None
    diagnostic: Diagnostic | None = None
    message: str = ""

    @property
    def ok(self) -> bool:
        return self.pdf is not None and self.diagnostic is not None and self.diagnostic.propre


def _cellule(r: Resultat | None) -> str:
    if r is None:
        return "—"
    if r.pdf is None:
        return "échec"
    return "ok" if r.ok else "à revoir"


def _remarques(r: Resultat | None) -> list[str]:
    if r is None or r.diagnostic is None:
        return [f"{r.nature} : {r.message}"] if r is not None and r.message else []
    d = r.diagnostic
    rem: list[str] = []
    if d.erreurs:
        rem.append(f"{r.nature} : {len(d.erreurs)} erreur(s) LaTeX ({d.erreurs[0][:60]})")
    if d.missing_dollar:
        rem.append(f"{r.nature} : {d.missing_dollar} « Missing $ »")
    if d.images_manquantes:
        rem.append(f"{r.nature} : image(s) manquante(s) {', '.join(d.images_manquantes)}")
    if d.caracteres_manquants:
        rem.append(f"{r.nature} : glyphe(s) absent(s) {' '.join(d.caracteres_manquants)}")
    grands = d.overfull_au_dela()
    if grands:
        rem.append(f"{r.nature} : {len(grands)} débordement(s) > 20 pt (max {max(grands):.0f} pt)")
    if r.message:
        rem.append(f"{r.nature} : {r.message}")
    return rem


def bilan_markdown(resultats: list[Resultat], titre: str = "Bilan de l'export PDF") -> str:
    """Tableau `| slug | brut | guidé | pages | remarques |` des corrigés exportés."""
    par_slug: dict[str, dict[str, Resultat]] = {}
    for r in resultats:
        par_slug.setdefault(r.slug, {})[r.nature] = r
    total = len(resultats)
    reussis = sum(1 for r in resultats if r.pdf is not None)
    propres = sum(1 for r in resultats if r.ok)
    lignes = [
        f"# {titre}",
        "",
        f"{reussis}/{total} documents compilés, dont {propres} sans avertissement bloquant "
        "(zéro « Missing $ », zéro image ni glyphe manquant, aucun débordement > 20 pt).",
        "",
        "| slug | brut | guidé | pages | remarques |",
        "|---|---|---|---|---|",
    ]
    for slug in sorted(par_slug):
        brut, guide = par_slug[slug].get("brut"), par_slug[slug].get("guide")
        pages = [
            str(r.diagnostic.pages) if r and r.diagnostic and r.diagnostic.pages else "—"
            for r in (brut, guide)
        ]
        rem = "; ".join(_remarques(brut) + _remarques(guide)).replace("|", "\\|")
        lignes.append(
            f"| `{slug}` | {_cellule(brut)} | {_cellule(guide)} | {' + '.join(pages)} | {rem} |"
        )
    return "\n".join(lignes) + "\n"
