#!/usr/bin/env python3
"""État des rédactions et relectures Astra Ultra dans les deux éditions X/ENS."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
import sys
import time
import unicodedata
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

RACINE = Path(__file__).resolve().parents[1]
REGISTRE = RACINE / "campagnes/x-ens/epreuves.tsv"
SITE = "https://sujet-corriges.ai"
PHASES = {
    "redaction": "Rédaction",
    "relecture_corrige": "Révision",
    "revision": "Révision",
}
BANQUES = {
    "x",
    "x-ens",
    "ens",
    "ens-de-lyon",
    "ens-rennes",
    "ens-paris-saclay",
    "ens-psl",
    "bel",
}
SLUG = re.compile(r"[a-z0-9-]+_[a-z0-9-]+_[a-z0-9-]+_\d{4}")
LIGNE_SIGNATURE = re.compile(r"^\*\*[^*\n]+\*\* · .+$")


DATE_SIGNATURE = re.compile(
    r" · (?:\d{4}-\d{2}-\d{2}|\d{1,2} (?:janvier|février|mars|avril|mai|juin|juillet|"
    r"août|septembre|octobre|novembre|décembre) \d{4})$"
)


def registre() -> dict[str, str]:
    with REGISTRE.open(encoding="utf-8") as fichier:
        lignes = list(csv.DictReader(fichier, delimiter="\t"))
    sujets = {r["slug"]: r["modalite"] for r in lignes}
    if len(sujets) != len(lignes) or any(not SLUG.fullmatch(s) for s in sujets):
        raise ValueError("Identifiants du registre invalides ou en double.")
    if any(
        r["modalite"] not in {"écrit", "oral", "pratique"}
        or urlsplit(r["source"]).scheme != "https"
        for r in lignes
    ):
        raise ValueError(
            "Chaque épreuve requiert une modalité et un lien HTTPS vers son sujet."
        )
    return sujets


def entete(markdown: str) -> set[str]:
    """Lire le bloc de signatures de tête, à l’exclusion du corps et des exemples."""
    lignes = iter(l.strip() for l in markdown.splitlines() if l.strip())
    titre = next(lignes, "")
    if not titre.startswith("# "):
        return set()
    ligne = next(lignes, "")
    resultats = set()
    while ligne:
        if LIGNE_SIGNATURE.fullmatch(ligne):
            resultats.add(DATE_SIGNATURE.sub("", ligne))
        elif "Corrigé rédigé par IA" not in ligne:
            break
        ligne = next(lignes, "")
    return resultats


def signatures_qualifiantes(meta: dict) -> set[str]:
    signatures = set()
    for entree in meta.get("contributions", []):
        role = PHASES.get(entree.get("phase"))
        modele = str(entree.get("modele") or "").casefold()
        if not role or modele not in {"gpt-6.2-astra", "gpt-6.2 astra"}:
            continue
        if str(entree.get("effort") or "").casefold() != "ultra":
            continue
        if entree.get("tour") is not None:
            role += f" (tour {entree['tour']})"
        vitesse = entree.get("vitesse")
        if vitesse and vitesse.lower() in {"standard", "ultrafast", "fast"}:
            vitesse = vitesse.lower()
        fin = f" {vitesse}" if vitesse else " · vitesse non renseignée"
        signatures.add(f"**{role}** · GPT-6.2 Astra Ultra{fin}")
    return signatures


@lru_cache(maxsize=1)
def editions_retirees() -> dict[str, list[tuple[str, str]]]:
    """Empreintes des éditions invalidées par une rectification documentée."""
    chemin = RACINE / "campagnes/x-ens/rectifications.tsv"
    editions: dict[str, list[tuple[str, str]]] = {}
    with chemin.open(encoding="utf-8") as fichier:
        for ligne in csv.DictReader(fichier, delimiter="\t"):
            editions.setdefault(ligne["slug"], []).extend(
                (nom, ligne[nom]) for nom in ("brut", "guide")
            )
    return editions


def verifier_paire(dossier: Path) -> tuple[str, set[str]]:
    fichiers = [dossier / f for f in ("meta.json", "brut.md", "guide.md")]
    if not all(f.is_file() for f in fichiers):
        return "paire absente ou incomplète", set()
    for nom, empreinte in editions_retirees().get(dossier.name, []):
        if (
            hashlib.sha256((dossier / f"{nom}.md").read_bytes()).hexdigest()
            == empreinte
        ):
            return "édition retirée du bilan après contrôle du sujet", set()
    meta = json.loads(fichiers[0].read_text(encoding="utf-8"))
    signatures = signatures_qualifiantes(meta)
    if not signatures:
        return "intervention Astra Ultra à effectuer ou documenter", set()
    if SLUG.fullmatch(dossier.name):
        # La publication du site construit la clé des textes et PDF à partir de la matière.
        matiere = str(meta.get("epreuve", {}).get("matiere", ""))
        ascii_matiere = (
            unicodedata.normalize("NFKD", matiere).encode("ascii", "ignore").decode()
        )
        segment = re.sub(r"[^\w.-]+", "-", ascii_matiere.lower()).strip("-")
        if segment != dossier.name.split("_")[2]:
            return "identité de matière à corriger pour publier sur la fiche", set()
    for md in fichiers[1:]:
        if not signatures <= entete(md.read_text(encoding="utf-8")):
            return "signature à vérifier dans les deux éditions", set()
    couverture = meta.get("couverture")
    if isinstance(couverture, dict) and couverture.get("statut") == "partiel":
        return "signature présente, corrigé partiel", signatures
    return "signature présente", signatures


def fiche_site(slug: str) -> str:
    banque, voie, epreuve = slug.split("_", 2)
    filieres = voie.split("-")
    if len(filieres) > 1 and set(filieres) <= {
        "mp",
        "mpi",
        "pc",
        "psi",
        "pt",
        "tsi",
        "tpc",
        "tb",
        "bcpst",
        "ats",
        "ect",
        "ecg",
    }:
        voie = filieres[0]
    return f"{banque}_{voie}_{epreuve}"


class SourceHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.blocs = []
        self.dans_pre = False

    def handle_starttag(self, tag, attrs):
        if tag == "pre":
            self.dans_pre = True
            self.blocs.append([])

    def handle_endtag(self, tag):
        if tag == "pre":
            self.dans_pre = False

    def handle_data(self, texte):
        if self.dans_pre:
            self.blocs[-1].append(texte)


class LectureHTML(HTMLParser):
    """Texte du corrigé effectivement affiché et lien PDF proposé au lecteur."""

    def __init__(self, nature: str):
        super().__init__()
        self.nature = nature
        self.dans_article = False
        self.paragraphe = None
        self.paragraphes = []
        self.documents = set()

    def handle_starttag(self, tag, attrs):
        attributs = dict(attrs)
        if tag == "article" and "copie-prose" in attributs.get("class", "").split():
            self.dans_article = True
        if tag == "p" and self.dans_article:
            classes = (attributs.get("class") or "").split()
            self.paragraphe = None if "document__titre" in classes else []
        if tag == "a":
            lien = attributs.get("href") or ""
            if re.fullmatch(
                rf"/api/catalog/documents/corriges/[a-z0-9_-]+/{self.nature}\.pdf", lien
            ):
                self.documents.add(lien)

    def handle_data(self, texte):
        if self.paragraphe is not None:
            self.paragraphe.append(texte)

    def handle_endtag(self, tag):
        if tag == "p" and self.paragraphe is not None:
            self.paragraphes.append(" ".join("".join(self.paragraphe).split()))
            self.paragraphe = None
        if tag == "article":
            self.dans_article = False

    def signatures(self):
        entetes = set()
        for texte in self.paragraphes:
            if " · " in texte:
                entetes.add(DATE_SIGNATURE.sub("", texte))
            elif "Corrigé rédigé par IA" not in texte:
                break
        return entetes


def telecharger(url: str) -> bytes:
    requete = Request(url, headers={"User-Agent": "Verification-corriges-X-ENS/1.0"})
    for tentative in range(3):
        try:
            with urlopen(requete, timeout=25) as reponse:
                return reponse.read()
        except (TimeoutError, URLError) as exc:
            if (
                tentative == 2
                or isinstance(exc, HTTPError)
                and exc.code not in {429, 500, 502, 503, 504}
            ):
                raise
            time.sleep(2**tentative)


def site_verifie(dossier: Path, fiche: str, signatures: set[str]) -> bool:
    libelles = {s.replace("**", "") for s in signatures}
    for nature in ("brut", "guide"):
        url = f"{SITE}/epreuves/{fiche}?doc=corrige&mode={nature}"
        lecture = LectureHTML(nature)
        lecture.feed(telecharger(url).decode())
        if not libelles <= lecture.signatures() or len(lecture.documents) != 1:
            return False
        source = SourceHTML()
        source.feed(telecharger(url + "&vue=source").decode())
        attendu = (dossier / f"{nature}.md").read_text(encoding="utf-8").strip()
        if not any(
            "".join(bloc)
            .strip()
            .replace(f"](/figures/corriges/{dossier.name}/", "](figures/")
            == attendu
            for bloc in source.blocs
        ):
            return False
        pdf = telecharger(SITE + lecture.documents.pop())
        if not pdf.startswith(b"%PDF-"):
            return False
        sortie = subprocess.run(
            ["pdftotext", "-layout", "-", "-"],
            input=pdf,
            capture_output=True,
            check=True,
        )
        texte = " ".join(sortie.stdout.decode().split("\f", 1)[0].split())
        if not all(libelle in texte for libelle in libelles):
            return False
    return True


def slugs_modifies(base: str) -> set[str]:
    diff = subprocess.check_output(
        ["git", "diff", "--name-only", "--no-renames", "-z", f"{base}...HEAD"],
        cwd=RACINE,
    )
    sujets = set()
    for nom in diff.decode().split("\0"):
        morceaux = Path(nom).parts
        if (
            len(morceaux) >= 4
            and SLUG.fullmatch(morceaux[2])
            and morceaux[:2] == (morceaux[2][-4:], morceaux[2].split("_")[0])
        ):
            sujets.add(morceaux[2])
    return sujets


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "slugs", nargs="*", help="limiter le rapport aux épreuves indiquées"
    )
    parser.add_argument("--depuis", help="contrôler les épreuves modifiées dans une PR")
    parser.add_argument(
        "--site",
        action="store_true",
        help="vérifier les deux HTML et PDF en production",
    )
    parser.add_argument("--tsv", type=Path, help="écrire le rapport par épreuve")
    parser.add_argument(
        "--exiger", action="store_true", help="échouer si une épreuve reste à couvrir"
    )
    args = parser.parse_args()
    perimetre = registre()
    selection = set(args.slugs) if args.slugs else set(perimetre)
    if args.depuis:
        selection = {
            s
            for s in slugs_modifies(args.depuis)
            if s in perimetre or s.split("_")[0] in BANQUES
        }
    elif not selection <= perimetre.keys():
        parser.error(
            "Épreuve(s) absente(s) du registre : "
            + ", ".join(sorted(selection - perimetre.keys()))
        )

    def ligne(slug):
        banque = slug.split("_", 1)[0]
        dossier = RACINE / slug[-4:] / banque / slug
        local, signatures = verifier_paire(dossier)
        fiche = fiche_site(slug)
        site = "non vérifié"
        if signatures and args.site:
            try:
                site = (
                    "vérifié"
                    if site_verifie(dossier, fiche, signatures)
                    else "trace à vérifier"
                )
            except (OSError, ValueError, subprocess.SubprocessError) as exc:
                site = f"contrôle impossible ({exc})"
        return (
            slug,
            perimetre.get(slug, "à inventorier"),
            local,
            site,
            f"{SITE}/epreuves/{fiche}?doc=corrige&mode=guide",
        )

    with ThreadPoolExecutor(max_workers=4) as pages:
        bilan = list(pages.map(ligne, sorted(selection)))
    for (modalite, local, site), n in sorted(
        Counter((r[1], r[2], r[3]) for r in bilan).items()
    ):
        print(f"{n:4}  {modalite} — {local} — site {site}")
    if args.tsv:
        with args.tsv.open("w", newline="", encoding="utf-8") as fichier:
            tab = csv.writer(fichier, delimiter="\t", lineterminator="\n")
            tab.writerow(("slug", "modalite", "github", "site", "fiche"))
            tab.writerows(bilan)
    acceptes = {"signature présente"}
    if args.depuis:
        # Une PR peut publier les parties effectivement traitées, signalées dans le bilan global.
        acceptes.add("signature présente, corrigé partiel")
    incompletes = [
        r
        for r in bilan
        if r[1] == "à inventorier"
        or r[2] not in acceptes
        or (args.site and r[3] != "vérifié")
    ]
    if args.depuis or args.slugs:
        for slug, modalite, local, site, _ in incompletes:
            print(f"{slug} ({modalite}) : {local} — site {site}")
    return int(bool(incompletes) and args.exiger)


if __name__ == "__main__":
    sys.exit(main())
