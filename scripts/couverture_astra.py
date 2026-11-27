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
from http.client import IncompleteRead
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
            "Chaque épreuve requiert une modalité et un lien HTTPS vers sa source."
        )
    return sujets


def exemples_documentes(sujets: dict[str, str]) -> dict[str, str]:
    """Billets vérifiables individuellement, déjà rattachés aux fascicules du décompte."""
    exemples = {}
    source = REGISTRE.with_name("exemples-de-billets-du-jury.tsv")
    with source.open(encoding="utf-8") as fichier:
        for ligne in csv.DictReader(fichier, delimiter="\t"):
            identifiant = ligne["fiche"]
            rattachements = ligne["fascicules_associes"].split("|")
            if (
                not SLUG.fullmatch(identifiant)
                or identifiant in sujets
                or identifiant in exemples
                or any(sujets.get(slug) != "oral" for slug in rattachements)
                or urlsplit(ligne["source"]).scheme != "https"
                or not re.fullmatch(r"[0-9a-f]{64}", ligne["sha256"])
            ):
                raise ValueError(f"Exemple de billet ou rattachement invalide : {identifiant}")
            exemples[identifiant] = "exemple du jury"
    return exemples


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


def est_astra_ultra(entree: dict) -> bool:
    return str(entree.get("modele") or "").casefold() in {
        "gpt-6.2-astra", "gpt-6.2 astra"
    } and str(entree.get("effort") or "").casefold() == "ultra"


def interventions_editoriales(meta: dict) -> list[dict]:
    return [
        e for e in meta.get("contributions", [])
        if e.get("phase") in PHASES or e.get("phase") == "retouches"
        or e.get("modifications") is True
    ]


def signatures_qualifiantes(meta: dict) -> set[str]:
    signatures = set()
    for entree in meta.get("contributions", []):
        role = PHASES.get(entree.get("phase"))
        if not role or not est_astra_ultra(entree):
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


def segment_adresse(libelle: str) -> str:
    ascii_libelle = unicodedata.normalize("NFKD", libelle).encode("ascii", "ignore").decode()
    return re.sub(r"[^\w.-]+", "-", ascii_libelle.lower()).strip("-")


def statut_couverture(couverture: object) -> str:
    """Lire les deux formats historiques et tenir compte des omissions explicites."""
    if isinstance(couverture, dict):
        if couverture.get("questions_non_traitees") or couverture.get("questions_partiellement_traitees"):
            return "partiel"
        couverture = couverture.get("statut")
    if isinstance(couverture, str):
        statut = couverture.strip().casefold()
        if statut in {"partiel", "partielle"}:
            return "partiel"
        if statut in {"complet", "complète", "intégral", "intégrale"}:
            return "complet"
    return "à confirmer"


def verifier_paire(dossier: Path, *, integralite: bool = False) -> tuple[str, set[str]]:
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
    for entree in reversed(interventions_editoriales(meta)):
        if est_astra_ultra(entree) and entree.get("phase") in PHASES:
            break
        if not est_astra_ultra(entree) and entree.get("modifications") is not False:
            return "édition modifiée depuis la dernière rédaction ou révision Astra Ultra", set()
    if SLUG.fullmatch(dossier.name):
        # Les deux lecteurs retrouvent les textes et leur journal par cette adresse.
        banque, _, matiere, annee = dossier.name.split("_")
        epreuve = meta.get("epreuve", {})
        if segment_adresse(str(epreuve.get("matiere", ""))) != matiere:
            return "identité de matière à corriger pour publier sur la fiche", set()
        if filiere := epreuve.get("filiere"):
            adresse = f"{banque}_{segment_adresse(filiere)}_{matiere}_{annee}"
            if not set(fiches_site(dossier.name)) <= set(fiches_site(adresse)):
                return "identité de filière à corriger pour publier sur la fiche", set()
    for md in fichiers[1:]:
        if not signatures <= entete(md.read_text(encoding="utf-8")):
            return "signature à vérifier dans les deux éditions", set()
    couverture = statut_couverture(meta.get("couverture"))
    if couverture == "partiel":
        return "signature présente, corrigé partiel", signatures
    if integralite and couverture != "complet":
        return "signature présente, couverture à confirmer", signatures
    return "signature présente", signatures


def fiches_site(slug: str) -> tuple[str, ...]:
    """Adresses publiques de chacune des voies d’une épreuve commune."""
    banque, voie, epreuve = slug.split("_", 2)
    if voie == "m-prime-p-prime":
        return tuple(f"{banque}_{filiere}_{epreuve}" for filiere in ("m-prime", "p-prime"))
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
        return tuple(f"{banque}_{filiere}_{epreuve}" for filiere in dict.fromkeys(filieres))
    return (slug,)


def fiche_site(slug: str) -> str:
    return fiches_site(slug)[0]


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
        except (TimeoutError, URLError, ConnectionError, IncompleteRead) as exc:
            if (
                tentative == 2
                or isinstance(exc, HTTPError)
                and exc.code not in {429, 500, 502, 503, 504}
            ):
                raise
            time.sleep(2**tentative)


def pdf_signe(pdf: bytes, libelles: set[str]) -> bool:
    if not pdf.startswith(b"%PDF-"):
        return False
    sortie = subprocess.run(
        ["pdftotext", "-f", "1", "-l", "1", "-layout", "-", "-"],
        input=pdf, capture_output=True, check=True,
    )
    texte = " ".join(sortie.stdout.decode().split())
    return all(libelle in texte for libelle in libelles)


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
        if not pdf_signe(pdf, libelles):
            return False
    return True


def texte_hors_signatures(markdown: str) -> str:
    lignes = markdown.strip().splitlines()
    if not lignes or not lignes[0].startswith("# "):
        return markdown
    for i, ligne in enumerate(lignes[1:], 1):
        if ligne.strip() and not LIGNE_SIGNATURE.fullmatch(ligne.strip()) and (
            "Corrigé rédigé par IA" not in ligne
        ):
            return "\n".join([lignes[0], *lignes[i:]])
    return lignes[0]


def edition_attribuee_depuis(dossier: Path, base: str) -> bool:
    """Vérifie qu’une modification du contenu possède sa propre intervention signée."""
    chemin = dossier.relative_to(RACINE).as_posix()
    noms = subprocess.check_output(
        ["git", "diff", "--name-only", "--no-renames", "-z", base, "HEAD", "--",
         f"{chemin}/brut.md", f"{chemin}/guide.md", f"{chemin}/figures"],
        cwd=RACINE,
    ).decode().split("\0")
    fichiers = [nom for nom in noms if nom]
    if not fichiers:
        return True

    def ancien(nom: str) -> str:
        resultat = subprocess.run(
            ["git", "show", f"{base}:{nom}"], cwd=RACINE, capture_output=True
        )
        return resultat.stdout.decode() if resultat.returncode == 0 else ""

    journal = interventions_editoriales(json.loads((dossier / "meta.json").read_text()))
    avant = interventions_editoriales(json.loads(ancien(f"{chemin}/meta.json") or "{}"))

    def objet(entree):
        # Une précision sur le nom du modèle ou sa vitesse ne signe pas un nouveau texte.
        return tuple(entree.get(champ) for champ in ("phase", "date", "tour", "perimetre"))

    if journal:
        derniere = journal[-1]
        objet_courant = objet(derniere)
        occurrences = sum(objet(e) == objet_courant for e in journal)
        anterieures = sum(objet(e) == objet_courant for e in avant)
        if (
            occurrences > anterieures
            and est_astra_ultra(derniere)
            and (derniere.get("agent") or derniere.get("session"))
        ):
            return True
    for nom in fichiers:
        if nom.startswith(f"{chemin}/figures/"):
            return False
        if texte_hors_signatures((RACINE / nom).read_text()) != texte_hors_signatures(ancien(nom)):
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
        help="vérifier les deux lecteurs et PDF en production pour chaque filière",
    )
    parser.add_argument("--tsv", type=Path, help="écrire le rapport par épreuve")
    parser.add_argument(
        "--exiger", action="store_true", help="échouer si une épreuve reste à couvrir"
    )
    parser.add_argument(
        "--integral", action="store_true",
        help="exiger une paire Astra signée et une couverture intégrale documentée pour chaque épreuve",
    )
    args = parser.parse_args()
    perimetre = registre()
    if args.depuis or args.slugs:
        perimetre.update(exemples_documentes(perimetre))
    selection = set(args.slugs) if args.slugs else set(perimetre)
    if args.depuis:
        base = subprocess.check_output(
            ["git", "merge-base", args.depuis, "HEAD"], cwd=RACINE, text=True
        ).strip()
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
        local, signatures = verifier_paire(dossier, integralite=args.integral)
        if args.depuis and signatures and not edition_attribuee_depuis(dossier, base):
            local, signatures = "modification du corrigé sans nouvelle attribution Astra Ultra", set()
        fiche = fiche_site(slug)
        site = "non vérifié"
        if signatures and args.site:
            try:
                meta = json.loads((dossier / "meta.json").read_text(encoding="utf-8"))
                voie = meta.get("epreuve", {}).get("filiere")
                adresse = slug
                if voie:
                    concours, _, epreuve, annee = slug.split("_")
                    adresse = f"{concours}_{segment_adresse(voie)}_{epreuve}_{annee}"
                lacunes = [
                    cible for cible in fiches_site(adresse)
                    if not site_verifie(dossier, cible, signatures)
                ]
                site = "trace à vérifier (" + ", ".join(lacunes) + ")" if lacunes else "vérifié"
            except (OSError, IncompleteRead, ValueError, subprocess.SubprocessError) as exc:
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
    if args.depuis and not args.integral:
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
    return int(bool(incompletes) and (args.exiger or args.integral))


if __name__ == "__main__":
    sys.exit(main())
