import csv
import importlib.util
import json
from pathlib import Path

import pytest

racine = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("agreger_bilan", racine / "scripts/agreger_bilan.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_bilan_par_matiere_et_banque_est_reproductible_depuis_ses_epreuves():
    dossier = racine / "campagnes/x-ens/bilans"
    bilan = json.loads((dossier / "dernier.json").read_text(encoding="utf-8"))
    with (dossier / bilan["fichier"]).open(encoding="utf-8", newline="") as fichier:
        sujets = list(csv.DictReader(fichier, delimiter="\t"))
    assert module.agreger(sujets) == bilan["toutes_modalites"]
    ecrits = module.agreger(s for s in sujets if s["modalité"] == "écrit")
    for section in ("matieres", "banques"):
        assert ecrits[section] == bilan[section]
    total = next(p for p in bilan["perimetres"] if p["nom"] == "Toutes les épreuves")
    compteurs = set(total) - {"nom"}
    for groupes in bilan["toutes_modalites"].values():
        for compteur in compteurs:
            assert sum(g[compteur] for g in groupes) == total[compteur]
    assert total["recenses"] == len(sujets)


def test_refuse_de_recompter_un_sujet_commun():
    ligne = {
        "identifiant": "exemple",
        "matière": "Arts",
        "concours ou banque": "X-ENS",
        "couverture GitHub": "Partiel",
        "site": "Édition vérifiée",
        "dossier GitHub": "https://github.com/exemple",
        "schémas SVG": "2",
    }
    with pytest.raises(ValueError, match="dupliqué"):
        module.agreger([ligne, ligne])


def test_signatures_editoriales_conservent_les_attributions_successives():
    entrees = [
        {"phase": "redaction", "famille_modele": "GPT-6"},
        {"phase": "lecture_rapport_jury", "modele": "autre"},
        {"phase": "relecture_corrige", "modele": "gpt-6.2-astra", "effort": "ultra",
         "vitesse": "ultrafast", "tour": 2, "session": "lecture", "date": "2026-11-25"},
    ]
    assert module.signatures_editoriales({"contributions": entrees}) == [
        "Rédaction · famille GPT-6 · effort non renseigné · vitesse non renseignée · session non renseignée",
        "Révision (tour 2) · GPT-6.2 Astra Ultra · vitesse ultrafast · session lecture · 2026-11-25",
    ]
