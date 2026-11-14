"""Export LaTeX/PDF : fonctions pures hors ligne ; pandoc et lualatex quand ils sont installés."""

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import pytest

from pur import (
    FILTRE,
    FORMAT_ENTREE,
    Diagnostic,
    Resultat,
    analyser_journal,
    bilan_markdown,
    echapper_latex,
    figures_citees,
    normaliser_maths,
    preparer_markdown,
    variables_gabarit,
)

META = {
    "slug": "ccinp_mp_physique_2026",
    "epreuve": {"concours": "CCINP", "filiere": "MP", "matiere": "Physique", "annee": 2026},
}

# --- Normalisation des maths (règles remark-math) --------------------------------


def test_maths_en_ligne_reecrites_en_parentheses():
    assert normaliser_maths("soit $x^2$ ici") == "soit \\(x^2\\) ici"


def test_espaces_internes_retires_comme_remark_math():
    # Pandoc refuse `$V = $` (espace avant le dollar fermant) ; le site l'affiche en maths.
    assert normaliser_maths("Variant : $V = $ len(dist).") == "Variant : \\(V =\\) len(dist)."


def test_dollar_suivi_d_un_chiffre():
    assert normaliser_maths("en S$_\\text{N}$2.") == "en S\\(_{\\text{N}}\\)2."


def test_espace_latex_final_conserve():
    assert normaliser_maths("$a\\ $ b") == "\\(a\\ \\) b"


def test_dollar_echappe_et_code_en_ligne_intacts():
    texte = "coût \\$5 et `x = $a$` puis $y$"
    assert normaliser_maths(texte) == "coût \\$5 et `x = $a$` puis \\(y\\)"


def test_maths_hors_texte_inchangees():
    texte = "$$\n\\frac{a}{b}\n$$\n\nPuis $$x$$ en ligne."
    assert normaliser_maths(texte) == texte


def test_blocs_de_code_ignores():
    texte = "```python\nprix = '$a$'\n```\n\nEt $b$."
    assert normaliser_maths(texte) == "```python\nprix = '$a$'\n```\n\nEt \\(b\\)."


def test_dollar_orphelin_conserve():
    assert normaliser_maths("un seul $ ici") == "un seul $ ici"


def test_maths_sur_deux_lignes_d_un_meme_paragraphe():
    assert normaliser_maths("> soit $a +\n> b$ fin") == "> soit \\(a +\n> b\\) fin"


def test_paragraphes_independants():
    # Un dollar orphelin ne s'apparie pas avec celui du paragraphe suivant.
    assert normaliser_maths("prix $\n\nfin $") == "prix $\n\nfin $"


# --- Titre, figures, gabarit ------------------------------------------------------


def test_preparer_markdown_retire_le_titre():
    titre, corps = preparer_markdown("# CCINP MP — Physique 2026 · Corrigé brut\n\n*Avert.*\n")
    assert titre == "CCINP MP — Physique 2026 · Corrigé brut"
    assert corps == "*Avert.*\n"


def test_figures_citees_sans_doublon():
    md = (
        "![Figure 1 — A](figures/s/a.svg)\n\n![Figure 1 — A](figures/s/a.svg)\n\n"
        "![Figure 2 — B](figures/s/b-c.svg)\n\n![x](https://ex.org/y.svg)"
    )
    assert figures_citees(md) == ["figures/s/a.svg", "figures/s/b-c.svg"]


def test_echapper_latex():
    assert echapper_latex("A&B_1 50% #x {y} ~^\\") == (
        "A\\&B\\_1 50\\% \\#x \\{y\\} \\textasciitilde{}\\textasciicircum{}\\textbackslash{}"
    )


def test_variables_gabarit():
    v = variables_gabarit(META, "guide", "CCINP MP — Physique 2026 · Corrigé guidé")
    assert v["nature"] == "Corrigé guidé"
    assert v["titre"] == "CCINP MP — Physique 2026"
    # Contenu agnostique : ni URL ni nom de site dans le PDF.
    assert "url" not in v
    assert (v["concours"], v["filiere"], v["matiere"], v["annee"]) == (
        "CCINP",
        "MP",
        "Physique",
        "2026",
    )


# --- Journal de compilation et bilan ------------------------------------------------

JOURNAL = """\
LaTeX Warning: File `figures/s/absente.pdf' not found on input line 12.
Overfull \\hbox (25.5pt too wide) in paragraph at lines 3--4
Overfull \\hbox (3.0pt too wide) in paragraph at lines 9--9
Missing character: There is no ⟧ (U+27E7) in font x!
! Missing $ inserted.
Output written on corrige-brut_s.pdf (12 pages, 123456 bytes).
"""


def test_analyser_journal():
    d = analyser_journal(JOURNAL)
    assert d.pages == 12
    assert d.missing_dollar == 1
    assert d.images_manquantes == ["figures/s/absente.pdf"]
    assert d.overfull == [25.5, 3.0]
    assert d.overfull_au_dela() == [25.5]
    assert d.caracteres_manquants == ["⟧"]
    assert d.erreurs == ["Missing $ inserted."]
    assert not d.propre


def test_journal_propre():
    d = analyser_journal("Output written on a.pdf (3 pages, 10 bytes).\n")
    assert d.propre


def test_bilan_markdown(tmp_path):
    propre = Diagnostic(pages=4)
    sale = Diagnostic(pages=9, overfull=[30.0])
    resultats = [
        Resultat("s", "brut", pdf=tmp_path / "a.pdf", diagnostic=propre),
        Resultat("s", "guide", pdf=tmp_path / "b.pdf", diagnostic=sale),
        Resultat("t", "brut", message="pandoc : erreur"),
    ]
    bilan = bilan_markdown(resultats)
    assert "| slug | brut | guidé | pages | remarques |" in bilan
    assert "| `s` | ok | à revoir | 4 + 9 | guide : 1 débordement(s) > 20 pt (max 30 pt) |" in bilan
    assert "| `t` | échec | — | — + — | brut : pandoc : erreur |" in bilan
    assert "2/3 documents compilés, dont 1 sans avertissement" in bilan


# --- Avec pandoc (et lualatex) ------------------------------------------------------

pandoc = pytest.mark.skipif(shutil.which("pandoc") is None, reason="pandoc absent")


def _pandoc(markdown: str) -> str:
    return subprocess.run(
        [
            "pandoc",
            "-f",
            FORMAT_ENTREE,
            "-t",
            "latex",
            "--lua-filter",
            str(FILTRE),
            "--shift-heading-level-by=-1",
        ],
        input=normaliser_maths(markdown),
        text=True,
        capture_output=True,
        check=True,
    ).stdout


@pandoc
def test_filtre_alertes_numerotees_et_reinitialisees():
    md = (
        "## Partie I\n\n### Question 1\n\n> [!INDICATION]\n> Piste $x$.\n\n"
        "> [!INDICATION]\n> Idée.\n\n#### Solution\n\nOK.\n\n> [!PIEGE]\n> Attention.\n\n"
        "### Question 2\n\n> [!INDICATION]\n> Encore.\n\n> [!METHODE]\n> M.\n\n> [!JURY]\n> J.\n"
    )
    tex = _pandoc(md)
    assert tex.count("\\begin{indication}{1}") == 2
    assert tex.count("\\begin{indication}{2}") == 1
    for env in ("piege", "methode", "jury"):
        assert f"\\begin{{{env}}}" in tex and f"\\end{{{env}}}" in tex
    assert "[!" not in tex
    assert "\\subsubsection{Solution}" in tex


@pandoc
def test_filtre_figures_et_maths():
    md = (
        "Texte.\n\n![Figure 1 — Circuit RLC](figures/s/q1-rlc.svg)\n\n"
        "> [!INDICATION]\n> Voir :\n>\n> ![Figure 2 — Schéma](figures/s/q2.svg)\n\n"
        "$$\na = b\n$$\n\nCode `x → y`.\n"
    )
    tex = _pandoc(md)
    assert "\\begin{figure}[H]" in tex
    assert "\\includegraphics{figures/s/q1-rlc.pdf}" in tex
    assert "\\caption*{Figure 1 --- Circuit RLC}" in tex
    assert "\\captionof*{figure}{Figure 2" in tex
    assert "\\equationajustee{" in tex
    assert "\\texttt{x\\ →\\ y}" in tex
    assert ".svg" not in tex


# --- Ajustements LaTeX des formules (sans changer le rendu) -------------------------


def test_couper_mathrm_equation_chimique():
    from pur import couper_mathrm

    assert couper_mathrm(r"\mathrm{NH_3 + HO^- = A{-}B}") == (
        r"\mathrm{NH_3} + \mathrm{HO^-} = \mathrm{A{-}B}"
    )
    assert couper_mathrm(r"\mathrm{Li^+}") == r"\mathrm{Li^+}"
    assert couper_mathrm(r"\mathrm{a}+\mathrm{b}") == r"\mathrm{a}+\mathrm{b}"
    assert couper_mathrm(r"\mathrm{A \to B}") == r"\mathrm{A} \to \mathrm{B}"


def test_proteger_indices():
    from pur import proteger_indices

    assert proteger_indices(r"\delta_\mathcal{C}(q)") == r"\delta_{\mathcal{C}}(q)"
    assert proteger_indices(r"x^\text{a{b}}_{y}") == r"x^{\text{a{b}}}_{y}"
    assert proteger_indices(r"x_{\mathcal C}") == r"x_{\mathcal C}"


def test_couper_listes_longues_seulement():
    from pur import couper_listes

    court = r"f(x,y)"
    assert couper_listes(court) == court
    longue = ",".join(rf"\{{{i},{i + 1}\}}" for i in range(12))
    sortie = couper_listes(longue)
    assert sortie.count(r"\allowbreak") == 23  # entre les ensembles et dedans
    assert sortie.replace(r"\allowbreak ", "") == longue


def test_normalisation_applique_les_ajustements():
    assert normaliser_maths(r"$\delta_\mathcal{C}$") == r"\(\delta_{\mathcal{C}}\)"
    assert normaliser_maths("$$x_\\mathbb{R}$$") == "$$x_{\\mathbb{R}}$$"


def test_accents_en_texte():
    from pur import accents_en_texte

    assert accents_en_texte(r"E_{consommée}=\alpha") == r"E_{\text{consommée}}=\alpha"
    assert accents_en_texte(r"x_{max}") == r"x_{max}"
    assert normaliser_maths("$D_{bâti}$") == r"\(D_{\text{bâti}}\)"


def test_isoler_alphabets():
    from pur import isoler_alphabets

    assert (
        isoler_alphabets(r"\chi_\mathrm I=E_\mathrm p(r)") == r"\chi_{\mathrm I}=E_{\mathrm p}(r)"
    )
    assert isoler_alphabets(r"\mathrm{I_3^-}_{(aq)}") == r"{\mathrm{I_3^-}}_{(aq)}"
    assert isoler_alphabets(r"\mathrm{d}x + \mathrm{dr}") == r"\mathrm{d}x + \mathrm{dr}"


def test_aligned_commencant_par_esperluette_recoit_un_groupe_vide():
    """`\\begin{aligned}&` fait échouer lualatex dans `\\equationajustee` : on insère `{}`."""
    src = "$$\n\\begin{aligned}\n& a = b \\\\\n& c = d\n\\end{aligned}\n$$"
    assert "\\begin{aligned}{}& a = b" in normaliser_maths(src)
    assert normaliser_maths("$$\\begin{aligned}& x\\end{aligned}$$") == (
        "$$\\begin{aligned}{}& x\\end{aligned}$$"
    )
    brut = "$$\\begin{alignedat}{2}&a&=b\\end{alignedat}$$"
    assert "\\begin{alignedat}{2}{}&" in normaliser_maths(brut)


def test_aligned_deja_protege_ou_a_cellule_non_vide_inchange():
    deja = "$$\\begin{aligned}{}& x\\end{aligned}$$"
    assert normaliser_maths(deja) == deja
    normal = "$$\\begin{aligned}x &= 1\\end{aligned}$$"
    assert normaliser_maths(normal) == normal


# --- Entrées-sorties (arborescence publique, compilation incrémentale) ---------------

import exporter as ex  # noqa: E402

SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="20">'
    '<rect width="40" height="20" fill="#ccc"/></svg>'
)
CORPS = (
    "# CCINP MP — Physique 2026 · Corrigé NATURE\n\n*Avertissement.*\n\n## Partie I\n\n"
    "### Question 1\n\n> [!INDICATION]\n> Penser à $\\vec g$.\n\n#### Solution\n\n"
    "$$\\boxed{T = 2\\pi\\sqrt{\\ell/g}}$$\n\n"
    "![Figure 1 — Pendule](figures/q1.svg)\n\n"
    "```python\nprint('é → ok')\n```\n"
)


def _depot(racine: Path) -> Path:
    dossier = racine / "2026" / "ccinp" / META["slug"]
    (dossier / "figures").mkdir(parents=True)
    (dossier / "meta.json").write_text(json.dumps(META), encoding="utf-8")
    (dossier / "figures" / "q1.svg").write_text(SVG, encoding="utf-8")
    for n in ("brut", "guide"):
        (dossier / f"{n}.md").write_text(CORPS.replace("NATURE", n), encoding="utf-8")
    return dossier


def test_dossiers_corriges(tmp_path):
    dossier = _depot(tmp_path)
    (tmp_path / "scripts").mkdir()
    assert ex.dossiers_corriges(tmp_path) == [dossier]


def test_empreinte_suit_markdown_et_figures(tmp_path):
    dossier = _depot(tmp_path)
    avant = ex.empreinte(dossier, "brut", pdf=True)
    assert ex.empreinte(dossier, "brut", pdf=True) == avant
    assert ex.empreinte(dossier, "brut", pdf=False) != avant
    assert ex.empreinte(dossier, "guide", pdf=True) != avant
    (dossier / "figures" / "q1.svg").write_text(SVG.replace("#ccc", "#000"), encoding="utf-8")
    apres_figure = ex.empreinte(dossier, "brut", pdf=True)
    assert apres_figure != avant
    (dossier / "brut.md").write_text("# T\n", encoding="utf-8")
    assert ex.empreinte(dossier, "brut", pdf=True) != apres_figure


def test_compiler_pdf_chemins_absolus(tmp_path, monkeypatch):
    """Chemin relatif : latexmk tourne dans le dossier du `.tex` ; `-outdir` doit être absolu."""
    dossier = tmp_path / "2026" / "x" / "s"
    dossier.mkdir(parents=True)
    (dossier / "brut.tex").write_text("x", encoding="utf-8")
    monkeypatch.chdir(tmp_path)
    vus = {}

    def faux_run(commande, cwd=None, **_):
        outdir = next(a for a in commande if a.startswith("-outdir="))[len("-outdir=") :]
        vus["outdir"], vus["cwd"] = outdir, cwd
        Path(outdir, "brut.log").write_text("Output written on x.pdf (3 pages)", encoding="utf-8")
        Path(outdir, "brut.pdf").write_bytes(b"%PDF")

    monkeypatch.setattr(ex.subprocess, "run", faux_run)
    pdf, diag, _ = ex.compiler_pdf(Path("2026/x/s/brut.tex"))
    assert Path(vus["outdir"]) == dossier / ".construction" / "brut"
    assert Path(vus["cwd"]).is_absolute()
    assert pdf == dossier / "brut.pdf" and pdf.exists() and diag.pages == 3


@pandoc
def test_tex_incremental(tmp_path):
    dossier = _depot(tmp_path)
    premiers = ex.exporter(racine=tmp_path, taches=1)
    assert all(r.tex for r in premiers) and not any(r.message == "inchangé" for r in premiers)
    seconds = ex.exporter(racine=tmp_path, taches=1)
    assert [r.message for r in seconds] == ["inchangé", "inchangé"]
    (dossier / "guide.md").write_text(CORPS.replace("NATURE", "guidé ") + "\nFin.\n")
    troisiemes = {r.nature: r.message for r in ex.exporter(racine=tmp_path, taches=1)}
    assert troisiemes == {"brut": "inchangé", "guide": ""}
    assert "figures/q1.pdf" in (dossier / "brut.tex").read_text(encoding="utf-8")


@pytest.mark.skipif(
    any(shutil.which(o) is None for o in ("pandoc", "latexmk", "lualatex", "rsvg-convert")),
    reason="chaîne LaTeX absente",
)
def test_export_complet_pdf(tmp_path):
    dossier = _depot(tmp_path)
    resultats = ex.exporter(racine=tmp_path, pdf=True, taches=2)
    assert all(r.ok for r in resultats), [(r.message, r.diagnostic) for r in resultats]
    assert (dossier / "guide.pdf").exists()
    assert (dossier / "figures" / "q1.pdf").exists()


def test_slugs_modifies(tmp_path):
    def git(*a):
        subprocess.run(["git", *a], cwd=tmp_path, check=True, capture_output=True)

    git("init", "-q", "-b", "master")
    git("config", "user.email", "t@example.invalid")
    git("config", "user.name", "t")
    dossier = _depot(tmp_path)
    git("add", ".")
    git("commit", "-qm", "init")
    (dossier / "brut.md").write_text("# T\n", encoding="utf-8")
    (tmp_path / "scripts" / "exporter").mkdir(parents=True)
    (tmp_path / "scripts" / "exporter" / "pur.py").write_text("x = 1\n")
    git("add", ".")
    git("commit", "-qm", "modif")
    assert ex.slugs_modifies("HEAD~1", tmp_path) == ([META["slug"]], True)

