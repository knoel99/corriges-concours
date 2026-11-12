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
| `brut.md` · `brut.pdf` | **Corrigé brut** : les réponses complètes, question par question |
| `guide.md` · `guide.pdf` | **Corrigé guidé** : présentation, indications graduées, solution, méthode, pièges, bilan |
| `brut.tex` · `guide.tex` | Source LaTeX des PDF (générée depuis le Markdown) |
| `figures/` | Figures en SVG (et PDF pour LaTeX) |
| `meta.json` | Épreuve, nombre de questions, liste des figures |

La liste complète est dans [INDEX.md](INDEX.md). Le Markdown est la source : les maths sont
en LaTeX (`$…$`, `$$…$$`), rendues par KaTeX sur le site. Les encadrés
`> [!INDICATION]`, `> [!METHODE]`, `> [!PIEGE]` et `> [!JURY]` sont des alertes.

Les **sujets** et les **rapports de jury** ne sont pas dans ce dépôt : ils appartiennent aux
banques de concours. Chaque fiche du site renvoie vers le document officiel.

## Contribuer

Voir [CONTRIBUTING.md](CONTRIBUTING.md). En bref : fork, modification du `.md`, `python3
scripts/verifier.py`, pull request. Les PDF et `.tex` sont régénérés par le mainteneur.

## Licences

- Corrigés, figures et documents : [CC BY 4.0](LICENSE). Citez « Corrigés de concours,
  sujet-corriges.ai » avec un lien vers ce dépôt.
- Scripts (`scripts/`) : [MIT](LICENSE-CODE).

Les courtes citations des rapports de jury qu'on trouve dans les encadrés `[!JURY]` restent la
propriété de leurs auteurs ; elles sont reproduites au titre du droit de courte citation.
