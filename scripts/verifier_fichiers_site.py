"""Comparer les deux Markdown téléchargeables à Git et lire les signatures des deux PDF."""

import argparse
import hashlib
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from http.client import IncompleteRead
from pathlib import Path

from couverture_astra import RACINE, SITE, pdf_signe, registre, telecharger, verifier_paire


def verifier_documents(dossier, signatures):
    slug = dossier.name
    libelles = {s.replace("**", "") for s in signatures}
    editions = {}
    for mode in ("brut", "guide"):
        url = f"{SITE}/api/catalog/documents/corriges/{slug}/{mode}"
        contenu = telecharger(url + ".md")
        attendu = (dossier / f"{mode}.md").read_text(encoding="utf-8").strip()
        # La publication adapte les chemins des illustrations à la variante du site.
        sources = {attendu.replace("](figures/", prefixe) for prefixe in (
            "](figures/", f"](figures/{slug}/", f"](/figures/corriges/{slug}/",
        )}
        if contenu.decode().strip() not in sources:
            raise ValueError(f"Le Markdown {mode} diffère de la version Git.")
        pdf = telecharger(url + ".pdf")
        if not pdf_signe(pdf, libelles):
            raise ValueError(f"Signature manquante dans le PDF {mode}.")
        editions[mode] = {
            "markdown": url + ".md", "pdf": url + ".pdf",
            "sha256_markdown": hashlib.sha256(contenu).hexdigest(),
            "sha256_pdf": hashlib.sha256(pdf).hexdigest(),
        }
    return editions


def controler(slug):
    chemin = Path(slug[-4:], slug.split("_")[0], slug)
    dossier = RACINE / chemin
    _, signatures = verifier_paire(dossier)
    if not signatures:
        return None
    resultat = {"slug": slug}
    try:
        resultat["editions"] = verifier_documents(dossier, signatures)
    except (OSError, IncompleteRead, ValueError, subprocess.SubprocessError) as exc:
        resultat["observation"] = str(exc)
    resultat["controle"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    return resultat


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slugs", nargs="*", help="épreuves du registre à vérifier")
    parser.add_argument("--json", type=Path, required=True, help="fichier des observations")
    args = parser.parse_args()
    sujets = registre()
    if inconnus := set(args.slugs) - sujets.keys():
        parser.error("Épreuves absentes du registre : " + ", ".join(sorted(inconnus)))
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=RACINE, text=True).strip()
    with ThreadPoolExecutor(max_workers=2) as pool:
        controles = [r for r in pool.map(controler, sorted(set(args.slugs) or sujets)) if r]
    preuve = {"revision": revision, "epreuves": controles}
    args.json.write_text(json.dumps(preuve, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    verifiees = sum("editions" in r for r in controles)
    print(f"{verifiees} paires de PDF signés et de Markdown correspondants sur "
          f"{len(controles)} épreuves signées au commit {revision}.")


if __name__ == "__main__":
    main()
