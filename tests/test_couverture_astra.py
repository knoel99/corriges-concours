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


@pytest.mark.parametrize("titre", ["", '<p class="document__titre">Corrigé guidé</p>'])
def test_signature_dans_le_corrige_visible_et_pdf_de_la_fiche_simple(titre):
    page = couverture.LectureHTML("brut")
    page.feed(f"""
      <div>Révision · GPT-6.2 Astra Ultra standard</div>
      <article class="copie-prose">{titre}<p><i>Corrigé rédigé par IA, non officiel.</i></p>
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


def test_rectification_exige_le_remplacement_des_deux_editions(tmp_path, monkeypatch):
    import hashlib

    slug = "ens-rennes_d-e_mathematiques-appliquees_2026"
    dossier = tmp_path / slug
    dossier.mkdir()
    entree = {"phase": "redaction", "modele": "gpt-6.2-astra", "effort": "ultra"}
    (dossier / "meta.json").write_text(
        json.dumps(
            {
                "contributions": [entree],
                "epreuve": {"matiere": "Mathématiques appliquées"},
            }
        )
    )
    signature = "**Rédaction** · GPT-6.2 Astra Ultra · vitesse non renseignée"
    ancienne = f"# Épreuve\n\n{signature}\n\n## Ancien exercice\n"
    empreinte = hashlib.sha256(ancienne.encode()).hexdigest()
    monkeypatch.setattr(
        couverture,
        "editions_retirees",
        lambda: {slug: [("brut", empreinte), ("guide", empreinte)]},
    )
    for nom in ("brut", "guide"):
        (dossier / f"{nom}.md").write_text(ancienne)
    for nom in ("brut", "guide"):
        assert not couverture.verifier_paire(dossier)[1]
        (dossier / f"{nom}.md").write_text(
            ancienne.replace("Ancien exercice", "Sujet vérifié")
        )
    assert couverture.verifier_paire(dossier)[1] == {signature}


def test_libelle_de_matiere_change_l_adresse_de_publication(tmp_path):
    dossier = tmp_path / "x-ens_pc_maths-pc_2025"
    dossier.mkdir()
    signature = "**Rédaction** · GPT-6.2 Astra Ultra · vitesse non renseignée"
    for edition in ("brut", "guide"):
        (dossier / f"{edition}.md").write_text(f"# Maths\n\n{signature}\n")
    meta = {
        "contributions": [
            {"phase": "redaction", "effort": "ultra", "modele": "gpt-6.2-astra"}
        ],
        "epreuve": {"matiere": "Mathématiques"},
    }
    fichier = dossier / "meta.json"
    fichier.write_text(json.dumps(meta))
    assert couverture.verifier_paire(dossier) == (
        "identité de matière à corriger pour publier sur la fiche",
        set(),
    )
    meta["epreuve"]["matiere"] = "Maths PC"
    fichier.write_text(json.dumps(meta))
    assert couverture.verifier_paire(dossier) == ("signature présente", {signature})
