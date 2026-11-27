"""Regrouper les preuves du tableau X et ENS sans recompter les épreuves communes."""

from __future__ import annotations

import argparse
import csv
import json
from collections.abc import Iterable
from pathlib import Path


def signatures_editoriales(meta: dict) -> list[str]:
    """Auteurs, relecteurs et interventions ayant modifié le corrigé, dans l’ordre du journal."""
    phases = {"redaction": "Rédaction", "revision": "Révision", "relecture_corrige": "Révision", "retouches": "Retouches"}
    editions = {"autocontrole": "Autocontrôle avec modifications", "production_figures": "Production de figures"}
    noms = {
        "gpt-6.2-astra": "GPT-6.2 Astra", "gpt-6.2-sol": "GPT-6.2 Sol",
        "claude-opus-5-5": "Claude Opus 5.5", "claude-opus-4-8": "Claude Opus 4.8",
    }
    signatures = []
    for entree in meta.get("contributions", []):
        phase = entree.get("phase")
        if not isinstance(phase, str) or not phase:
            continue
        role = phases.get(phase)
        if role is None:
            if entree.get("modifications") is not True:
                continue
            role = editions.get(phase, f"Contribution ({phase.replace('_', ' ')})")
        if entree.get("tour") is not None:
            role += f" (tour {entree['tour']})"
        modele = entree.get("modele")
        if modele:
            libelle = noms.get(modele.lower(), modele)
        elif entree.get("famille_modele"):
            libelle = "famille " + entree["famille_modele"]
        else:
            libelle = "modèle non renseigné"
        effort = entree.get("effort")
        if effort:
            libelle += " " + (effort.capitalize() if libelle == "GPT-6.2 Astra" else effort)
        vitesse = entree.get("vitesse")
        elements = [role, libelle]
        if not effort:
            elements.append("effort non renseigné")
        elements.append("vitesse " + vitesse if vitesse else "vitesse non renseignée")
        auteurs = dict.fromkeys(entree[cle] for cle in ("agent", "session") if entree.get(cle))
        elements.append("session " + " / ".join(auteurs) if auteurs else "session non renseignée")
        if entree.get("date"):
            elements.append(str(entree["date"]))
        signatures.append(" · ".join(elements))
    return signatures


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
        a_confirmer = ligne["couverture GitHub"] == "Couverture à confirmer"
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
            if a_confirmer:
                total["a_confirmer"] = total.get("a_confirmer", 0) + 1
                if verifie:
                    total["a_confirmer_production"] = total.get("a_confirmer_production", 0) + 1
            if complet:
                total["schemas"] += int(ligne["schémas SVG"] or 0)
    if any("a_confirmer" in g for g in groupes["banques"].values()):
        for tableau in groupes.values():
            for total in tableau.values():
                total.setdefault("a_confirmer", 0)
                total.setdefault("a_confirmer_production", 0)
    return {section: [tableau[nom] for nom in sorted(tableau)] for section, tableau in groupes.items()}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tableau", type=Path, help="Tableau daté du registre, au format TSV")
    args = parser.parse_args()
    with args.tableau.open(encoding="utf-8", newline="") as fichier:
        synthese = agreger(csv.DictReader(fichier, delimiter="\t"))
    print(json.dumps(synthese, ensure_ascii=False, indent=2))
