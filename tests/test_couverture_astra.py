import importlib.util
import json
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location(
    "couverture", Path(__file__).resolve().parents[1] / "scripts/couverture_astra.py"
)
couverture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(couverture)


@pytest.mark.parametrize(
    ("phase", "role", "vitesse", "fin"),
    [
        ("redaction", "Rédaction", "ultrafast", " ultrafast"),
        ("relecture_corrige", "Révision", None, " · vitesse non renseignée"),
    ],
)
def test_deux_editions_signees(tmp_path, phase, role, vitesse, fin):
    entree = dict(
        phase=phase, modele="gpt-6.2-astra", effort="ultra", vitesse=vitesse, tour=2
    )
    signature = f"**{role} (tour 2)** · GPT-6.2 Astra Ultra{fin}"
    meta = {"contributions": [entree]}
    for nom in ("brut.md", "guide.md"):
        (tmp_path / nom).write_text(
            f"# Titre\n\n{signature} · 24 novembre 2026\n\n## Réponses"
        )
    (tmp_path / "meta.json").write_text(json.dumps(meta))
    assert couverture.verifier_paire(tmp_path) == ("signature présente", {signature})
    meta["couverture"] = {"statut": "partiel"}
    (tmp_path / "meta.json").write_text(json.dumps(meta))
    assert (
        couverture.verifier_paire(tmp_path)[0] == "signature présente, corrigé partiel"
    )
    (tmp_path / "guide.md").write_text(f"# Titre\n\n## Exemple\n\n{signature}")
    assert not couverture.verifier_paire(tmp_path)[1]


@pytest.mark.parametrize(
    "modification",
    [
        {"modele": "GPT-6"},
        {"modele": "gpt-6.2-sol"},
        {"effort": "high"},
        {"phase": "autocontrole"},
        {"phase": "retouches"},
    ],
)
def test_pas_de_relecture_attribuee_par_inference(modification):
    entree = dict(phase="relecture_corrige", modele="gpt-6.2-astra", effort="ultra")
    assert not couverture.signatures_qualifiantes(
        {"contributions": [entree | modification]}
    )
