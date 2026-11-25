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
