import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import verifier_fichiers_site as publication


@pytest.mark.parametrize("prefixe", ["figures/", "figures/{slug}/", "/figures/corriges/{slug}/"])
def test_fichiers_des_deux_editions_et_liens_des_figures(tmp_path, monkeypatch, prefixe):
    dossier = tmp_path / "ens_mp_cinema_2017"
    dossier.mkdir()
    fichiers = {}
    for mode in ("brut", "guide"):
        texte = f"# {mode}\n\n![Plan](figures/plan.svg)\n"
        (dossier / f"{mode}.md").write_text(texte)
        fichiers[f"{mode}.md"] = texte.replace("](figures/", "](" + prefixe.format(slug=dossier.name)).encode()
        fichiers[f"{mode}.pdf"] = b"%PDF-" + mode.encode()
    monkeypatch.setattr(publication, "telecharger", lambda url: fichiers[url.rsplit("/", 1)[1]])
    monkeypatch.setattr(publication, "pdf_signe", lambda pdf, mots: pdf.startswith(b"%PDF-") and mots == {"signature"})
    preuve = publication.verifier_documents(dossier, {"**signature**"})
    assert set(preuve) == {"brut", "guide"}
    assert preuve["brut"]["sha256_pdf"] != preuve["guide"]["sha256_pdf"]
    fichiers["guide.md"] = b"# guide\n\n![Plan](figures/autre-sujet/plan.svg)\n"
    with pytest.raises(ValueError, match="Markdown guide"):
        publication.verifier_documents(dossier, {"**signature**"})
