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


def test_lien_vers_fiche_simple_ou_filiere_administrative():
    assert (
        couverture.fiche_site("ccinp_mp-mpi-pc-psi-tpc-tsi_anglais_2026")
        == "ccinp_mp_anglais_2026"
    )
    assert (
        couverture.fiche_site("x_fui-ff-1_physique_2021") == "x_fui-ff-1_physique_2021"
    )


def test_signature_dans_le_corrige_visible_et_pdf_de_la_fiche_simple():
    page = couverture.LectureHTML("brut")
    page.feed("""
      <div>Révision · GPT-6.2 Astra Ultra standard</div>
      <article class="copie-prose"><p><i>Corrigé rédigé par IA, non officiel.</i></p>
      <p><strong>Rédaction</strong> · GPT-6.2 Astra Ultra · vitesse non renseignée · 24 novembre 2026</p>
      <p>Question 1</p><p>Révision · GPT-6.2 Astra Ultra standard</p></article>
      <a href="/api/catalog/documents/corriges/x-ens_mp_info_2026/brut.pdf">PDF</a>
      <a href="/api/catalog/documents/corriges/x-ens_mp_info_2026/guide.pdf">PDF guidé</a>
    """)
    assert page.signatures() == {
        "Rédaction · GPT-6.2 Astra Ultra · vitesse non renseignée"
    }
    assert page.documents == {
        "/api/catalog/documents/corriges/x-ens_mp_info_2026/brut.pdf"
    }
