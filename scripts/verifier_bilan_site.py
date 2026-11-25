"""Comparer toutes les lignes du bilan en ligne au relevé GitHub de la même version."""

import argparse
import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from time import sleep
from urllib.parse import urlsplit

from lxml import html

from couverture_astra import RACINE, SITE, telecharger


def verifier_page(contenu, lignes, date):
    page = html.fromstring(contenu)
    if page.xpath("//main//p/time/@datetime")[:1] != [date]:
        raise ValueError("Le site ne présente pas encore le relevé demandé.")
    affichage = page.xpath("//main//table/tbody/tr")
    if len(affichage) != len(lignes):
        raise ValueError(f"{len(affichage)} lignes visibles pour {len(lignes)} attendues.")

    for ligne, sujet in zip(affichage, lignes, strict=True):
        cellules = ligne.xpath("./td")
        slug = sujet["identifiant"]
        fiche = urlsplit(sujet["fiche du site"])
        signature = sujet["historique éditorial"].splitlines()
        dossier = sujet["dossier GitHub"]
        if (
            ligne.xpath("./th/a[1]/text()") != [sujet["épreuve"]]
            or ligne.xpath("./th/a[1]/@href") != [f"{fiche.path}?{fiche.query}"]
            or len(cellules) != 4
            or cellules[0].text_content().strip() != sujet["couverture GitHub"]
        ):
            raise ValueError(f"{slug} : identité, lien ou état du corrigé différent.")
        liens = ligne.xpath(".//a/@href")
        journal = ligne.xpath('.//a[normalize-space(.)="Journal des interventions"]/@href')
        attendu = [dossier.replace("/tree/", "/blob/") + "/meta.json"] if dossier else []
        if journal != attendu or (dossier and dossier not in liens):
            raise ValueError(f"{slug} : lien de provenance différent.")
        visible = [" ".join(e.text_content().split()) for e in ligne.xpath(".//details/ol/li")]
        if visible != [" ".join(s.split()) for s in signature]:
            raise ValueError(f"{slug} : les signatures ne correspondent pas au journal.")
        controle = sujet["contrôle positif UTC"]
        if sujet["site"] not in cellules[2].text_content():
            raise ValueError(f"{slug} : état de publication différent.")
        if controle and controle not in ligne.xpath(".//time/@datetime"):
            raise ValueError(f"{slug} : date de vérification différente.")


def verifier_tableau(dossier):
    bilan = json.loads((dossier / "dernier.json").read_text(encoding="utf-8"))
    tableau = dossier / bilan["fichier"]
    contenu = tableau.read_bytes()
    empreinte = hashlib.sha1(f"blob {len(contenu)}\0".encode() + contenu).hexdigest()
    if empreinte != bilan["blob_tableau"]:
        raise ValueError("Le TSV ne correspond pas à l’empreinte Git du bilan.")
    with tableau.open(encoding="utf-8", newline="") as fichier:
        sujets = list(csv.DictReader(fichier, delimiter="\t"))

    pages = []
    for debut in range(0, len(sujets), 30):
        numero = len(pages) + 1
        url = f"{SITE}/couverture-x-ens/epreuves?page={numero}"
        lignes = sujets[debut:debut + 30]
        verifier_page(telecharger(url), lignes, bilan["date"])
        pages.append({
            "url": url,
            "epreuves": len(lignes),
            "premiere": lignes[0]["identifiant"],
            "derniere": lignes[-1]["identifiant"],
            "utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        })
        if debut + 30 < len(sujets):
            sleep(0.5)
    return {
        "revision": bilan["revision"],
        "blob_tableau": empreinte,
        "date_releve": bilan["date"],
        "epreuves": len(sujets),
        "epreuves_signees": sum(
            s["couverture GitHub"] in {"Complet", "Partiel"}
            and s["modèle"] == "GPT-6.2 Astra" and s["effort"] == "Ultra"
            for s in sujets
        ),
        "interventions": sum(len(s["historique éditorial"].splitlines()) for s in sujets),
        "pages": pages,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path, required=True, help="sortie des vérifications datées")
    args = parser.parse_args()
    preuve = verifier_tableau(RACINE / "campagnes/x-ens/bilans")
    args.json.write_text(json.dumps(preuve, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{preuve['epreuves']} épreuves et {preuve['interventions']} interventions conformes "
          f"sur {len(preuve['pages'])} pages du site. Le relevé compte {preuve['epreuves_signees']} "
          f"épreuves signées, à la révision {preuve['revision']}.")
