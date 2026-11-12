# Contribuer

Merci de relire ! Toute correction est bienvenue, d'une coquille à une démonstration fausse.

1. **Signaler** : ouvrez une issue avec le slug de l'épreuve, le numéro de question et ce qui ne
   va pas (idéalement avec la référence au sujet ou au rapport du jury).
2. **Corriger** : forkez le dépôt, modifiez `brut.md` et/ou `guide.md` de l'épreuve (gardez les
   deux cohérents), lancez `python3 scripts/verifier.py <slug>`, puis ouvrez une pull request.
   Ne modifiez ni les `.pdf` ni les `.tex` : ils sont régénérés depuis le Markdown.

Règles de forme :

- suivre la numérotation du sujet et n'employer que des outils au programme de la filière ;
- maths en `$…$` / `$$…$$` (KaTeX) ; pas d'environnement `align`/`equation`, pas de
  `\newcommand`, pas de TikZ ni de HTML (`<svg>`, `<img>`) ;
- une figure = un fichier `figures/<nom>.svg` (sans script ni lien externe), insérée seule dans
  son paragraphe : `![Figure N — légende](figures/<nom>.svg)`, et déclarée dans `meta.json` ;
- ne pas recopier de longs passages des sujets ou des rapports de jury (droits des banques).

En contribuant, vous acceptez que votre contribution soit publiée sous CC BY 4.0 (corrigés) ou
MIT (scripts). Le mainteneur relit et fusionne les pull requests ; les corrections fusionnées
sont reportées sur le site.
