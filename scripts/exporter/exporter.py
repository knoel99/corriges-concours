#!/usr/bin/env python3
"""Corrigés brut et guidé : Markdown (seule source) → LaTeX (pandoc) → PDF (lualatex).

    python3 scripts/exporter/exporter.py                    # .tex de tous les corrigés
    python3 scripts/exporter/exporter.py --pdf              # .tex + .pdf
    python3 scripts/exporter/exporter.py --pdf <slug> ...   # quelques épreuves
    python3 scripts/exporter/exporter.py --pdf --depuis origin/master   # épreuves modifiées

Outils : pandoc (toujours), latexmk + lualatex + rsvg-convert (avec --pdf). Bibliothèque
standard seulement.

Les sorties sont écrites à côté du Markdown et ne sont pas versionnées (.gitignore) :

    <année>/<banque>/<slug>/brut.tex   brut.pdf   guide.tex   guide.pdf
    <année>/<banque>/<slug>/figures/<nom>.pdf     (figures SVG converties pour LaTeX)
    <année>/<banque>/<slug>/.construction/        (journaux, empreintes)

La compilation est incrémentale : un document dont le Markdown, les figures citées, le gabarit,
le filtre et ces scripts n'ont pas changé depuis la dernière compilation n'est pas recompilé
(empreinte SHA-256 dans `.construction/<nature>.empreinte`). Quand l'outillage change, tous
les `.tex` sont régénérés (pandoc, rapide), mais lualatex ne repasse que sur ceux dont le `.tex`
ou une figure diffère vraiment (`.construction/<nature>.sortie`). `--forcer` recompile tout.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from pur import (
    FILTRE,
    FORMAT_ENTREE,
    GABARIT,
    NATURES,
    Diagnostic,
    Resultat,
    analyser_journal,
    bilan_markdown,
    figures_citees,
    preparer_markdown,
    variables_gabarit,
)

ICI = Path(__file__).resolve().parent
RACINE = ICI.parent.parent
# Une modification de ces fichiers change la sortie : elle invalide toutes les empreintes.
OUTILLAGE = (GABARIT, FILTRE, ICI / "pur.py", ICI / "exporter.py")
# Épreuves compilées en CI quand seul l'outillage change (aucun corrigé modifié).
ECHANTILLON = 3
OPTIONS_LATEXMK = ("-lualatex", "-interaction=nonstopmode", "-f")


def dossiers_corriges(racine: Path = RACINE) -> list[Path]:
    """`<année>/<banque>/<slug>/` qui ont un meta.json, triés."""
    return sorted(p.parent for p in racine.glob("[0-9][0-9][0-9][0-9]/*/*/meta.json"))


def outils_manquants(pdf: bool) -> list[str]:
    requis = ["pandoc"] + (["latexmk", "lualatex", "rsvg-convert"] if pdf else [])
    return [o for o in requis if shutil.which(o) is None]


def empreinte(dossier: Path, nature: str, pdf: bool) -> str:
    """SHA-256 de tout ce dont dépend la sortie d'un document."""
    h = hashlib.sha256(f"{nature}|pdf={pdf}".encode())
    source = dossier / f"{nature}.md"
    fichiers = [source, dossier / "meta.json", *OUTILLAGE]
    if source.exists():
        fichiers += [dossier / f for f in figures_citees(source.read_text(encoding="utf-8"))]
    for f in fichiers:
        h.update(str(f.relative_to(dossier) if f.is_relative_to(dossier) else f.name).encode())
        h.update(f.read_bytes() if f.exists() else b"<absent>")
    return h.hexdigest()


def empreinte_sortie(tex: Path, dossier: Path, markdown: str) -> str:
    """SHA-256 de ce que lualatex lit : le `.tex` produit, les SVG cités, ses options.

    Une modification de l'outillage invalide toutes les empreintes d'entrée, mais seuls les
    documents dont le `.tex` change vraiment repassent par lualatex (le coûteux).
    Les SVG, pas leurs PDF : rsvg-convert date ses sorties, leurs octets changent à chaque run.
    """
    h = hashlib.sha256(" ".join(OPTIONS_LATEXMK).encode())
    h.update(tex.read_bytes())
    for fig in figures_citees(markdown):
        svg = dossier / fig
        h.update(fig.encode())
        h.update(svg.read_bytes() if svg.exists() else b"<absent>")
    return h.hexdigest()


def convertir_figure(svg: Path, pdf: Path) -> None:
    """SVG → PDF vectoriel (rsvg-convert), seulement si le PDF manque ou est plus ancien."""
    if pdf.exists() and pdf.stat().st_mtime >= svg.stat().st_mtime:
        return
    pdf.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["rsvg-convert", "-f", "pdf", "-o", str(pdf), str(svg)], check=True, capture_output=True
    )


def convertir_figures(dossiers: list[Path]) -> None:
    """Convertit une seule fois chaque SVG cité par brut.md ou guide.md."""
    svgs: set[Path] = set()
    for dossier in dossiers:
        for nature in NATURES:
            source = dossier / f"{nature}.md"
            if source.exists():
                svgs.update(dossier / f for f in figures_citees(source.read_text(encoding="utf-8")))
    for svg in sorted(svgs):
        if svg.exists():
            convertir_figure(svg, svg.with_suffix(".pdf"))


def generer_tex(markdown: str, meta: dict, nature: str, sortie: Path) -> Path:
    """Markdown → `.tex` (pandoc + filtre + gabarit)."""
    titre, corps = preparer_markdown(markdown)
    commande = [
        "pandoc", "-f", FORMAT_ENTREE, "-t", "latex", "--standalone",
        "--template", str(GABARIT), "--lua-filter", str(FILTRE), "--listings",
        "--wrap=preserve", "-o", str(sortie),
    ]
    # Babel choisit la police et la direction des passages arabes dans ces copies bilingues.
    if re.search(r"[ء-يٱ-ۓ]", corps):
        commande += ["-M", "arabe=true"]
    if meta.get("epreuve", {}).get("matiere") == "Chinois":
        commande += ["-M", "chinois=true"]
    for cle, valeur in variables_gabarit(meta, nature, titre).items():
        commande += ["-V", f"{cle}={valeur}"]
    subprocess.run(commande, input=corps, text=True, check=True, capture_output=True)
    return sortie


def journal_de(tex: Path) -> Path:
    return tex.parent / ".construction" / tex.stem / f"{tex.stem}.log"


def lire_diagnostic(tex: Path) -> Diagnostic | None:
    journal = journal_de(tex)
    if not journal.exists():
        return None
    return analyser_journal(journal.read_text(encoding="utf-8", errors="replace"))


def compiler_pdf(tex: Path, delai: int = 600) -> tuple[Path | None, Diagnostic, str]:
    """`latexmk -lualatex` dans `.construction/<nature>/`, PDF recopié à côté du `.tex`.

    Chemins absolus : latexmk tourne dans le dossier du `.tex` (`cwd`).
    """
    tex = Path(tex).resolve()
    construction = journal_de(tex).parent
    construction.mkdir(parents=True, exist_ok=True)
    commande = ["latexmk", *OPTIONS_LATEXMK, f"-outdir={construction}", tex.name]
    message = ""
    try:
        subprocess.run(
            commande, cwd=tex.parent, capture_output=True, text=True, timeout=delai, check=False,
            # Journal sans retour à la ligne forcé : les motifs analysés tiennent sur une ligne.
            env={**os.environ, "max_print_line": "100000"},
        )
    except subprocess.TimeoutExpired:
        message = f"délai de compilation dépassé ({delai} s)"
    diagnostic = lire_diagnostic(tex) or Diagnostic()
    produit = construction / f"{tex.stem}.pdf"
    if produit.exists() and diagnostic.pages:
        cible = tex.with_suffix(".pdf")
        shutil.copy2(produit, cible)
        return cible, diagnostic, message
    return None, diagnostic, message or "pas de PDF produit"


def exporter_document(dossier: Path, nature: str, pdf: bool, forcer: bool = False) -> Resultat:
    meta = json.loads((dossier / "meta.json").read_text(encoding="utf-8"))
    res = Resultat(slug=meta.get("slug", dossier.name), nature=nature)
    source = dossier / f"{nature}.md"
    if not source.exists():
        res.message = f"source absente : {source.name}"
        return res
    tex = dossier / f"{nature}.tex"
    marque = dossier / ".construction" / f"{nature}.empreinte"
    voulue = empreinte(dossier, nature, pdf)
    a_jour = tex.exists() and (not pdf or tex.with_suffix(".pdf").exists())
    if not forcer and a_jour and marque.exists() and marque.read_text() == voulue:
        res.tex = tex
        if pdf:
            res.pdf, res.diagnostic = tex.with_suffix(".pdf"), lire_diagnostic(tex)
        res.message = "inchangé"
        return res
    markdown = source.read_text(encoding="utf-8")
    for fig in figures_citees(markdown):
        svg = dossier / fig
        if not svg.exists():
            res.message = f"figure absente : {fig}"
            continue
        if pdf:
            convertir_figure(svg, dossier / Path(fig).with_suffix(".pdf"))
    ancien_tex = tex.read_bytes() if tex.exists() else None
    try:
        generer_tex(markdown, meta, nature, tex)
    except subprocess.CalledProcessError as exc:
        res.message = f"pandoc : {exc.stderr.strip()[:200]}"
        return res
    res.tex = tex
    if pdf:
        marque_sortie = dossier / ".construction" / f"{nature}.sortie"
        sortie = empreinte_sortie(tex, dossier, markdown)
        deja = tex.with_suffix(".pdf")
        if marque_sortie.exists():
            identique = marque_sortie.read_text() == sortie
        else:
            # Cache antérieur aux marques de sortie : le `.tex` du run précédent en tient lieu.
            # Il ignore un SVG modifié dans le même run ; la marque écrite ensuite le couvre.
            identique = ancien_tex is not None and ancien_tex == tex.read_bytes()
        if not forcer and deja.exists() and identique:
            res.pdf, res.diagnostic = deja, lire_diagnostic(tex)
            res.message = res.message or "PDF inchangé (.tex identique)"
            marque_sortie.parent.mkdir(parents=True, exist_ok=True)
            marque_sortie.write_text(sortie)
        else:
            res.pdf, res.diagnostic, msg = compiler_pdf(tex)
            if msg:
                res.message = msg
            if res.pdf:
                marque_sortie.parent.mkdir(parents=True, exist_ok=True)
                marque_sortie.write_text(sortie)
    if res.tex and (res.pdf or not pdf):
        marque.parent.mkdir(parents=True, exist_ok=True)
        marque.write_text(voulue)
    return res


def slugs_modifies(depuis: str, racine: Path = RACINE) -> tuple[list[str], bool]:
    """Slugs dont un fichier a changé depuis `depuis`, et si l'outillage a changé."""
    sortie = subprocess.run(
        ["git", "diff", "--name-only", f"{depuis}...HEAD"],
        cwd=racine, capture_output=True, text=True, check=True,
    ).stdout.split()
    slugs, outillage = [], False
    for chemin in sortie:
        parties = Path(chemin).parts
        if len(parties) >= 4 and parties[0].isdigit() and parties[2] not in slugs:
            if (racine / Path(*parties[:3]) / "meta.json").exists():
                slugs.append(parties[2])
        elif parties[:2] == ("scripts", "exporter"):
            outillage = True
    return slugs, outillage


def exporter(
    slugs: list[str] | None = None,
    pdf: bool = False,
    taches: int | None = None,
    forcer: bool = False,
    racine: Path = RACINE,
) -> list[Resultat]:
    dossiers = [d for d in dossiers_corriges(racine) if not slugs or d.name in slugs]
    travaux = [(d, n) for d in dossiers for n in NATURES]
    if pdf:
        # brut et guide citent souvent les mêmes figures : convertir avant le pool évite
        # que deux threads écrivent le même PDF (ou qu'un lualatex le lise à moitié écrit).
        convertir_figures(dossiers)

    def un(travail: tuple[Path, str]) -> Resultat:
        dossier, nature = travail
        r = exporter_document(dossier, nature, pdf, forcer)
        etat = "ok" if r.ok or (not pdf and r.tex) else ("à revoir" if r.pdf else "ÉCHEC")
        pages = f" {r.diagnostic.pages} p." if r.diagnostic else ""
        print(f"  [{etat}] {dossier.name}/{nature}{pages} {r.message}".rstrip(), flush=True)
        return r

    with ThreadPoolExecutor(max_workers=taches or max(1, os.cpu_count() or 2)) as pool:
        return list(pool.map(un, travaux))


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("slugs", nargs="*", help="épreuves à exporter (défaut : toutes)")
    p.add_argument("--pdf", action="store_true", help="compile aussi le PDF (lualatex)")
    p.add_argument("--depuis", help="seulement les épreuves modifiées depuis cette révision git")
    p.add_argument("--forcer", action="store_true", help="ignore les empreintes, recompile tout")
    p.add_argument("--taches", type=int, default=None, help="compilations en parallèle")
    p.add_argument("--bilan", type=Path, default=None, help="écrit le bilan Markdown ici")
    args = p.parse_args(argv)

    slugs = args.slugs or None
    if args.depuis:
        modifies, outillage = slugs_modifies(args.depuis)
        if outillage and not modifies:
            modifies = [d.name for d in dossiers_corriges()[:ECHANTILLON]]
        if not modifies:
            print(f"Aucun corrigé modifié depuis {args.depuis}.")
            return 0
        slugs = sorted(set(modifies) | set(slugs or []))

    manquants = outils_manquants(args.pdf)
    if manquants:
        print(f"Outils introuvables : {', '.join(manquants)}", file=sys.stderr)
        return 2
    resultats = exporter(slugs, args.pdf, args.taches, args.forcer)
    if not resultats:
        print("Aucun corrigé trouvé.", file=sys.stderr)
        return 1
    if args.bilan:
        args.bilan.write_text(bilan_markdown(resultats), encoding="utf-8")
    if args.pdf:
        compiles = sum(1 for r in resultats if r.pdf)
        propres = sum(1 for r in resultats if r.ok)
        print(f"{compiles}/{len(resultats)} PDF compilés, {propres} propres.")
        return 0 if compiles == len(resultats) else 1
    faits = sum(1 for r in resultats if r.tex)
    print(f"{faits}/{len(resultats)} .tex générés.")
    return 0 if faits == len(resultats) else 1


if __name__ == "__main__":
    raise SystemExit(main())
