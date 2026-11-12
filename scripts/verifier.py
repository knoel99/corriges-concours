#!/usr/bin/env python3
"""Contrôle de forme des corrigés de ce dépôt, sans dépendance.

    python3 scripts/verifier.py              # tous les corrigés
    python3 scripts/verifier.py <slug> ...   # une ou plusieurs épreuves

Ne juge pas le fond. Vérifie : titre et avertissement en tête, $$ appariés, constructions que
KaTeX ne rend pas, figures (fichier existant, chemin relatif figures/<nom>.svg, déclarées dans
meta.json, SVG sans script ni lien externe), et qu'aucun fichier revue*, rapport* ou sujet*
n'est présent dans le dépôt (ni revues, ni rapports de jury, ni sujets). Code de sortie 1 en
cas d'erreur.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
AVERTISSEMENT = "Corrigé rédigé par IA"
INTERDITS = [
    r"\\begin\{tikzpicture\}", r"\\newcommand", r"\\usepackage", r"\\documentclass",
    r"\\begin\{align\*?\}", r"\\begin\{equation\*?\}", r"\\begin\{itemize\}",
    r"\\begin\{enumerate\}", r"\\section\{",
]
IMAGE = re.compile(r"!\[(?:\\.|[^\]\\])*\]\(([^)\s]*)(?:\s+\"[^\"]*\")?\)")
HTML = re.compile(r"<\s*(svg|img)\b", re.I)
FIGURE = re.compile(r"figures/[a-z0-9]+(?:-[a-z0-9]+)*\.svg")
SVG_INTERDITS = [
    (re.compile(r"<\s*script\b", re.I), "<script>"),
    (re.compile(r"<[^>]*\son[a-z]+\s*=", re.I), "gestionnaire on…="),
    (re.compile(r"<\s*foreignObject\b", re.I), "<foreignObject>"),
    (re.compile(r"javascript:", re.I), "URL javascript:"),
    (
        re.compile(r"""(?:\b(?:xlink:)?href|\bsrc)\s*=\s*["'](?!\s*(?:#|data:))""", re.I),
        "lien externe",
    ),
]

PREFIXES_INTERDITS = ("revue", "rapport", "sujet")


def fichiers_interdits(racine: Path) -> list[str]:
    """Signale tout fichier dont le nom commence par revue, rapport ou sujet (hors .git)."""
    return [
        f"fichier interdit (ni revues, ni rapports de jury, ni sujets) : {p.relative_to(racine)}"
        for p in sorted(racine.rglob("*"))
        if p.is_file() and ".git" not in p.relative_to(racine).parts
        and p.name.lower().startswith(PREFIXES_INTERDITS)
    ]


def verifier(dossier: Path) -> list[str]:
    err: list[str] = []
    try:
        meta = json.loads((dossier / "meta.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{dossier.name} : meta.json illisible ({exc})"]
    declarees = {f.get("fichier") for f in meta.get("figures", [])}
    citees: set[str] = set()
    for nature in ("brut", "guide"):
        md = dossier / f"{nature}.md"
        if not md.exists():
            err.append(f"{dossier.name} : {nature}.md manquant")
            continue
        texte = md.read_text(encoding="utf-8")
        corps = re.sub(r"```.*?```", "", texte, flags=re.S)
        nom = f"{dossier.name}/{nature}.md"
        if not texte.lstrip().startswith("# "):
            err.append(f"{nom} : la première ligne doit être un titre « # … »")
        if AVERTISSEMENT not in texte[:600]:
            err.append(f"{nom} : avertissement « {AVERTISSEMENT}… » absent de l'en-tête")
        if corps.count("$$") % 2:
            err.append(f"{nom} : nombre impair de $$")
        err += [f"{nom} : construction non rendue : {m}" for m in INTERDITS if re.search(m, corps)]
        if HTML.search(corps):
            err.append(f"{nom} : HTML <svg>/<img> interdit, utilisez ![…](figures/<nom>.svg)")
        for cible in IMAGE.findall(corps):
            if not FIGURE.fullmatch(cible):
                err.append(f"{nom} : image hors du motif figures/<nom>.svg : {cible}")
            elif not (dossier / cible).exists():
                err.append(f"{nom} : figure absente : {cible}")
            citees.add(cible)
    for f in sorted(citees - declarees):
        err.append(f"{dossier.name} : figure citée mais absente de meta.json : {f}")
    for svg in sorted((dossier / "figures").glob("*.svg")):
        contenu = svg.read_text(encoding="utf-8", errors="replace")
        nom = f"{dossier.name}/figures/{svg.name}"
        err += [f"{nom} : {lib}" for motif, lib in SVG_INTERDITS if motif.search(contenu)]
    return err


def main(argv: list[str]) -> int:
    dossiers = sorted(p.parent for p in RACINE.glob("*/*/*/meta.json"))
    if argv:
        dossiers = [d for d in dossiers if d.name in set(argv)]
        if not dossiers:
            print("aucune épreuve trouvée pour :", " ".join(argv))
            return 1
    erreurs = fichiers_interdits(RACINE) + [e for d in dossiers for e in verifier(d)]
    for e in erreurs:
        print("ERREUR", e)
    print(f"{len(dossiers)} épreuve(s), {len(erreurs)} erreur(s)")
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
