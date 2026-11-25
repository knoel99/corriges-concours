"""Porte de fusion : `scripts/verifier.py` refuse ce que la publication ou l'export casseraient."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "verifier", Path(__file__).resolve().parent.parent / "scripts" / "verifier.py"
)
verifier = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(verifier)

CORPS = "# Titre\n\n*Corrigé rédigé par IA, à relire.*\n\n![Fig](figures/a.svg \"Titre\")\n"
SVG = '<svg xmlns="http://www.w3.org/2000/svg"><rect width="1" height="1"/></svg>'


def _dossier(tmp_path: Path, slug: str = "ccinp_mp_physique_2026", **meta) -> Path:
    dossier = tmp_path / "2026" / "ccinp" / "ccinp_mp_physique_2026"
    (dossier / "figures").mkdir(parents=True)
    (dossier / "figures" / "a.svg").write_text(SVG, encoding="utf-8")
    for nature in ("brut", "guide"):
        (dossier / f"{nature}.md").write_text(CORPS, encoding="utf-8")
    contenu = {"slug": slug, "figures": [{"fichier": "figures/a.svg"}], **meta}
    (dossier / "meta.json").write_text(json.dumps(contenu), encoding="utf-8")
    return dossier


def test_dossier_conforme(tmp_path):
    assert verifier.verifier(_dossier(tmp_path)) == []


def test_slug_different_du_dossier(tmp_path):
    """La publication (prepa, vers_publication.py) s'arrête sur ce cas."""
    erreurs = verifier.verifier(_dossier(tmp_path, slug="autre"))
    assert any("slug" in e for e in erreurs), erreurs


def test_figure_avec_titre_non_declaree(tmp_path):
    erreurs = verifier.verifier(_dossier(tmp_path, figures=[]))
    assert any("absente de meta.json" in e for e in erreurs), erreurs


def test_une_legende_ne_doit_pas_masquer_la_figure_au_lecteur(tmp_path):
    dossier = _dossier(tmp_path)
    brut = dossier / "brut.md"
    brut.write_text(CORPS.replace("![Fig]", "![Entre X[2] et X[3]]"))
    erreurs = verifier.verifier(dossier)
    assert len(erreurs) == 1
    assert "brut.md" in erreurs[0] and "image non reconnue" in erreurs[0]

    brut.write_text(CORPS.replace("![Fig]", r"![Entre X\[2\] et X\[3\]]"))
    assert verifier.verifier(dossier) == []
