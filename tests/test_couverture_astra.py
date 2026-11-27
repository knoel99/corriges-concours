import importlib.util
import json
from http.client import IncompleteRead, RemoteDisconnected
from io import BytesIO
from pathlib import Path
from urllib.error import HTTPError

import pytest

spec = importlib.util.spec_from_file_location(
    "couverture", Path(__file__).resolve().parents[1] / "scripts/couverture_astra.py"
)
couverture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(couverture)


@pytest.mark.parametrize("incident", [RemoteDisconnected(), IncompleteRead(b"texte", 12)])
def test_lecture_interrompue_redemande_le_document_entier(monkeypatch, incident):
    appels = []

    def ouvrir(requete, timeout):
        appels.append(requete.full_url)
        if len(appels) == 1:
            raise incident
        return BytesIO(b"document complet")

    monkeypatch.setattr(couverture, "urlopen", ouvrir)
    monkeypatch.setattr(couverture.time, "sleep", lambda delai: None)
    url = "https://exemple.fr/document.pdf"
    assert couverture.telecharger(url) == b"document complet"
    assert appels == [url, url]


def test_document_introuvable_signale_sans_attente(monkeypatch):
    url = "https://exemple.fr/document.pdf"

    def ouvrir(requete, timeout):
        raise HTTPError(url, 404, "Not Found", {}, None)

    monkeypatch.setattr(couverture, "urlopen", ouvrir)
    monkeypatch.setattr(couverture.time, "sleep", lambda delai: pytest.fail("Nouvel essai"))
    with pytest.raises(HTTPError) as erreur:
        couverture.telecharger(url)
    assert erreur.value.code == 404


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
    assert couverture.verifier_paire(tmp_path, integralite=True)[0] == "signature présente, couverture à confirmer"
    for valeur in ("complet", {"statut": "complet"}):
        meta["couverture"] = valeur
        (tmp_path / "meta.json").write_text(json.dumps(meta))
        assert couverture.verifier_paire(tmp_path, integralite=True)[0] == "signature présente"
    for valeur in ("partielle", {"statut": "complet", "questions_non_traitees": [3]}):
        meta["couverture"] = valeur
        (tmp_path / "meta.json").write_text(json.dumps(meta))
        assert couverture.verifier_paire(tmp_path, integralite=True)[0] == "signature présente, corrigé partiel"
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
    assert couverture.fiches_site("x_m-prime-p-prime_deuxieme-composition-de-mathematiques_1990") == (
        "x_m-prime_deuxieme-composition-de-mathematiques_1990",
        "x_p-prime_deuxieme-composition-de-mathematiques_1990",
    )
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


@pytest.mark.parametrize(
    ("slug", "filiere", "reconnue"),
    [
        ("bel_bl_allemand_2017", "B/L", False),
        ("bel_bl_allemand_2017", "BL", True),
        ("x-ens_mp_allemand_2017", "MP-MPI", True),
        ("x-ens_mp-pc_allemand_2017", "MP", False),
    ],
)
def test_filiere_de_publication_du_corrige(tmp_path, slug, filiere, reconnue):
    dossier = tmp_path / slug
    dossier.mkdir()
    signature = "**Rédaction** · GPT-6.2 Astra Ultra · vitesse non renseignée"
    for edition in ("brut", "guide"):
        (dossier / f"{edition}.md").write_text(f"# Allemand\n\n{signature}\n")
    meta = {
        "epreuve": {"matiere": "Allemand", "filiere": filiere},
        "contributions": [{"phase": "redaction", "modele": "gpt-6.2-astra", "effort": "ultra"}],
    }
    (dossier / "meta.json").write_text(json.dumps(meta))
    etat, signatures = couverture.verifier_paire(dossier)
    if reconnue:
        assert signatures == {signature}
    else:
        assert etat == "identité de filière à corriger pour publier sur la fiche"
        assert not signatures


def test_exemple_du_jury_rattache_sans_ajouter_une_epreuve():
    sujets = couverture.registre()
    slug = "bel_al_grec-oral-option-exemple-du-jury-ploutos_2026"
    assert slug not in sujets
    assert couverture.exemples_documentes(sujets)[slug] == "exemple du jury"
    with pytest.raises(ValueError):
        couverture.exemples_documentes({**sujets, slug: "oral"})


def test_une_retouche_par_un_autre_modele_demande_une_nouvelle_relecture(tmp_path):
    redaction = {"phase": "redaction", "modele": "gpt-6.2-astra", "effort": "ultra"}
    correction = {"phase": "autocontrole", "modele": "autre", "modifications": True}
    signature = "**Rédaction** · GPT-6.2 Astra Ultra · vitesse non renseignée"
    revision = "**Révision** · GPT-6.2 Astra Ultra · vitesse non renseignée"
    for nom in ("brut.md", "guide.md"):
        (tmp_path / nom).write_text(f"# Épreuve\n\n{signature}\n\n{revision}\n\nRéponse")
    fichier = tmp_path / "meta.json"
    entrees = [redaction, correction, {**redaction, "phase": "retouches"}]
    fichier.write_text(json.dumps({"contributions": entrees}))
    assert not couverture.verifier_paire(tmp_path)[1]
    entrees.append({**redaction, "phase": "revision"})
    fichier.write_text(json.dumps({"contributions": entrees}))
    assert couverture.verifier_paire(tmp_path)[1] == {signature, revision}


def test_modifier_une_edition_ne_reutilise_pas_une_signature_anterieure(tmp_path, monkeypatch):
    import subprocess

    monkeypatch.setattr(couverture, "RACINE", tmp_path)
    dossier = tmp_path / "2026/x/x_mp_maths_2026"
    dossier.mkdir(parents=True)
    texte = dossier / "brut.md"
    ancien = "**Rédaction** · GPT-6.2 Astra Ultra · vitesse non renseignée"
    texte.write_text(f"# Épreuve\n\n{ancien}\n\nUne première réponse.")
    meta = dossier / "meta.json"
    redaction = {"phase": "redaction", "modele": "gpt-6.2-astra", "effort": "ultra",
                 "session": "lettres", "perimetre": "Rédaction des deux éditions."}
    journal = [redaction]
    meta.write_text(json.dumps({"contributions": journal}))

    def git(*args):
        return subprocess.check_output(["git", *args], text=True, cwd=tmp_path).strip()

    def commit():
        git("add", "--all")
        git("-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "-qm", "Version")

    git("init", "-q")
    commit()
    base = git("rev-parse", "HEAD")
    assert couverture.edition_attribuee_depuis(dossier, git("hash-object", "-t", "tree", "/dev/null"))
    texte.write_text(texte.read_text().replace(ancien, ancien + " · 25 novembre 2026"))
    commit()
    assert couverture.edition_attribuee_depuis(dossier, base)
    texte.write_text(texte.read_text().replace("première réponse", "réponse corrigée"))
    redaction["agent"] = "lettres"
    meta.write_text(json.dumps({"contributions": journal}))
    commit()
    assert not couverture.edition_attribuee_depuis(dossier, base)
    journal.insert(0, {**redaction, "perimetre": "Rédaction antérieure nouvellement documentée."})
    meta.write_text(json.dumps({"contributions": journal}))
    commit()
    assert not couverture.edition_attribuee_depuis(dossier, base)
    journal.append({**redaction, "phase": "autocontrole", "modifications": True,
                    "perimetre": "Rectification de la réponse."})
    meta.write_text(json.dumps({"contributions": journal}))
    commit()
    assert couverture.edition_attribuee_depuis(dossier, base)
    base = git("rev-parse", "HEAD")
    (dossier / "figures").mkdir()
    (dossier / "figures/schema.svg").write_text("<svg/>")
    commit()
    assert not couverture.edition_attribuee_depuis(dossier, base)


def test_controle_internet_examine_chaque_voie(tmp_path, monkeypatch):
    slug = "x-ens_mp_allemand_2017"
    dossier = tmp_path / "2017" / "x-ens" / slug
    dossier.mkdir(parents=True)
    (dossier / "meta.json").write_text(json.dumps({"epreuve": {"filiere": "MP-MPI"}}))
    visites = []

    def visite(dossier, fiche, signatures):
        visites.append(fiche)
        return fiche == slug

    monkeypatch.setattr(couverture, "RACINE", tmp_path)
    monkeypatch.setattr(couverture, "registre", lambda: {slug: "écrit"})
    monkeypatch.setattr(couverture, "exemples_documentes", lambda _: {})
    monkeypatch.setattr(couverture, "verifier_paire", lambda _, *, integralite: ("signature présente", {"signature"}))
    monkeypatch.setattr(couverture, "site_verifie", visite)
    monkeypatch.setattr(couverture.sys, "argv", ["controle", slug, "--site", "--exiger"])
    assert couverture.main() == 1
    assert visites == [slug, "x-ens_mpi_allemand_2017"]
