from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from verifier_bilan_site import verifier_page

DATE = "2026-11-25T05:43:35+01:00"
DOSSIER = "https://github.com/knoel99/corriges-concours/tree/abc/2026/x/exemple"
SIGNATURE = "Révision · GPT-6.2 Astra Ultra · vitesse non renseignée · session exemple"

SUJET = {
    "identifiant": "exemple", "épreuve": "Mathématiques",
    "fiche du site": "https://sujet-corriges.ai/epreuves/exemple?doc=corrige",
    "couverture GitHub": "Complet", "dossier GitHub": DOSSIER,
    "site": "Édition vérifiée", "historique éditorial": SIGNATURE, "contrôle positif UTC": "2026-11-25T02:00:00Z",
}
PAGE = f"""<main><p><time datetime="{DATE}"></time></p><table><tbody><tr>
<th><a href="/epreuves/exemple?doc=corrige">Mathématiques</a></th><td>Complet</td>
<td><details><ol><li>{SIGNATURE}</li></ol></details></td>
<td>Édition vérifiée <time datetime="2026-11-25T02:00:00Z"></time></td>
<td><a href="{DOSSIER}">GitHub</a>
<a href="{DOSSIER.replace('/tree/', '/blob/')}/meta.json">Journal des interventions</a>
</td></tr></tbody></table></main>"""


def test_releve_identique():
    verifier_page(PAGE, [SUJET], DATE)


def test_rapport_seul_sans_fiche_ni_enonce():
    rapport = "https://www.banquept.fr/IMG/pdf/rapport_oral2_mathematiques_2003.pdf"
    donnees = {**SUJET, "fiche du site": "", "sujet": "", "rapport": rapport}
    page = PAGE.replace(
        '<a href="/epreuves/exemple?doc=corrige">Mathématiques</a>', "<span>Mathématiques</span>"
    ).replace("</td></tr>", f'<a href="{rapport}">Rapport du jury</a></td></tr>')
    verifier_page(page, [donnees], DATE)
    with pytest.raises(ValueError, match="lien"):
        verifier_page(page.replace("Rapport du jury", "Sujet"), [donnees], DATE)


def test_quatre_fichiers_du_bon_sujet_et_du_bon_releve():
    date = "2026-11-25T04:48:00Z"
    donnees = {**SUJET, "contrôle des fichiers UTC": date}
    liens = "".join(f'<a href="/api/catalog/documents/corriges/exemple/{mode}.{ext}">{ext}</a>'
                    for mode in ("brut", "guide") for ext in ("pdf", "md"))
    page = PAGE.replace("Édition vérifiée <time", f'Édition vérifiée <time datetime="{date}"></time>{liens}<time')
    verifier_page(page, [donnees], DATE)
    with pytest.raises(ValueError, match="liens des fichiers"):
        verifier_page(page.replace("exemple/guide.pdf", "autre/guide.pdf"), [donnees], DATE)
    with pytest.raises(ValueError, match="date du contrôle des fichiers"):
        verifier_page(page.replace(date, DATE), [donnees], DATE)


@pytest.mark.parametrize("ancien,nouveau", [
    (DATE, "2026-11-24"),
    ("vitesse non renseignée", "vitesse standard"),
    ("session exemple", "session sans rapport"),
    ("meta.json", "guide.md"),
    ("Complet", "Partiel"),
])
def test_releve_divergent(ancien, nouveau):
    with pytest.raises(ValueError):
        verifier_page(PAGE.replace(ancien, nouveau), [SUJET], DATE)
