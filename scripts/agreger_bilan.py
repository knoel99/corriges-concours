"""Regrouper les preuves du tableau X et ENS sans recompter les épreuves communes."""

from __future__ import annotations

import argparse
import csv
import json
from collections.abc import Iterable
from pathlib import Path


def agreger(lignes: Iterable[dict[str, str]]) -> dict[str, list[dict]]:
    groupes: dict[str, dict[str, dict]] = {"matieres": {}, "banques": {}}
    identifiants: set[str] = set()
    for ligne in lignes:
        identifiant = ligne["identifiant"]
        if not identifiant or identifiant in identifiants:
            raise ValueError(f"Identifiant manquant ou dupliqué : {identifiant!r}")
        identifiants.add(identifiant)
        complet = ligne["couverture GitHub"] == "Complet"
        partiel = ligne["couverture GitHub"] == "Partiel"
        verifie = ligne["site"] == "Édition vérifiée"
        for section, champ in (("matieres", "matière"), ("banques", "concours ou banque")):
            nom = ligne[champ]
            if not nom:
                raise ValueError(f"{champ} absent pour {identifiant}")
            tableau = groupes[section]
            if nom not in tableau:
                tableau[nom] = dict(nom=nom, recenses=0, paires=0, complets=0,
                                    production=0, partiels=0, partiels_production=0, schemas=0)
            total = tableau[nom]
            total["recenses"] += 1
            total["paires"] += bool(ligne["dossier GitHub"])
            total["complets"] += complet
            total["production"] += complet and verifie
            total["partiels"] += partiel
            total["partiels_production"] += partiel and verifie
            if complet:
                total["schemas"] += int(ligne["schémas SVG"] or 0)
    return {section: [tableau[nom] for nom in sorted(tableau)] for section, tableau in groupes.items()}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tableau", type=Path, help="Tableau daté du registre, au format TSV")
    args = parser.parse_args()
    with args.tableau.open(encoding="utf-8", newline="") as fichier:
        synthese = agreger(csv.DictReader(fichier, delimiter="\t"))
    print(json.dumps(synthese, ensure_ascii=False, indent=2))
