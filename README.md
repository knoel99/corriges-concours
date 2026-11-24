# Corrigés de concours

Corrigés rédigés par IA des épreuves écrites des concours d'entrée aux grandes écoles
(session 2026 : X / X-ENS, Mines-Ponts, Centrale-Supélec, CCINP, e3a-Polytech, Banque PT,
ATS, G2E, Agro-Véto). Les mêmes corrigés se lisent en ligne, avec le sujet et le rapport du
jury, sur [Sujets et corrigés.ai](https://sujet-corriges.ai/epreuves).

> **Ces corrigés ne sont pas officiels.** Ils ont été rédigés par une IA, puis relus et révisés
> par IA à l'aide du rapport du jury quand il était paru. Ils peuvent contenir des erreurs :
> signalez-les (issue) ou corrigez-les (pull request).

## Contenu

Chaque épreuve a son dossier `<année>/<banque>/<slug>/` :

| Fichier | Contenu |
|---|---|
| `brut.md` | **Corrigé brut** : les réponses complètes, question par question |
| `guide.md` | **Corrigé guidé** : présentation, indications graduées, solution, méthode, pièges, bilan |
| `figures/` | Figures en SVG |
| `meta.json` | Épreuve, nombre de questions, liste des figures |

La liste complète est dans [INDEX.md](INDEX.md). Le Markdown est la **seule source** : les maths sont
en LaTeX (`$…$`, `$$…$$`), rendues par KaTeX sur le site. Les encadrés
`> [!INDICATION]`, `> [!METHODE]`, `> [!PIEGE]` et `> [!JURY]` sont des alertes.

Le suivi Polytechnique et ENS donne, par sujet et par matière, la source et la procédure de vérification de la rédaction ou relecture par GPT-6.2 Astra Ultra sur GitHub et sur le site. [Suivi X et ENS](campagnes/x-ens/)

## PDF et LaTeX

Les PDF ne sont pas versionnés : ils se téléchargent sur la fiche de chaque épreuve du site, où
ils sont recompilés depuis ce dépôt à chaque publication. Pour les produire chez soi
(pandoc, latexmk, lualatex et rsvg-convert requis) :

```bash
python3 scripts/exporter/exporter.py --pdf                 # tous les corrigés
python3 scripts/exporter/exporter.py --pdf <slug> [...]    # quelques épreuves
```

Le `.tex` et le `.pdf` sont écrits à côté du Markdown, et ignorés par git. La compilation est
incrémentale : une épreuve inchangée n'est pas recompilée, et une modification de l'exporteur ne
recompile en PDF que les documents dont le `.tex` produit change.

Les **sujets** et les **rapports de jury** ne sont pas dans ce dépôt : ils appartiennent aux
banques de concours. Chaque fiche du site renvoie vers le document officiel.

## Contribuer

Voir [CONTRIBUTING.md](CONTRIBUTING.md). En bref : fork, modification du `.md`, `python3
scripts/verifier.py`, pull request. La CI compile le PDF des épreuves modifiées et le joint au
run ; après fusion, le site republie la correction.

## Licences

- Corrigés, figures et documents : [CC BY 4.0](LICENSE). Citez « Corrigés de concours,
  sujet-corriges.ai » avec un lien vers ce dépôt.
- Scripts (`scripts/`, `tests/`) : [MIT](LICENSE-CODE).

Les courtes citations des rapports de jury qu'on trouve dans les encadrés `[!JURY]` restent la
propriété de leurs auteurs ; elles sont reproduites au titre du droit de courte citation.
