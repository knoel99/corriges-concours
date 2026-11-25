# Contribuer

Merci de relire ! Toute correction est bienvenue, d'une coquille à une démonstration fausse.

Aucun compte sur le site n'est nécessaire : un compte GitHub suffit. La page
[Contribuer](https://sujet-corriges.ai/contribuer) du site renvoie vers les formulaires ci-dessous.

1. **Signaler** : ouvrez une issue avec le formulaire
   [« Signaler une erreur »](https://github.com/knoel99/corriges-concours/issues/new?template=erreur.yml) :
   slug de l'épreuve, lien de la fiche, document (corrigé brut ou guidé), numéro de question et
   ce qui ne va pas (idéalement avec la référence au sujet ou au rapport du jury).
   Pour annoncer que vous rédigez ou relisez le corrigé d'une épreuve, utilisez
   [« Proposer ou réserver un corrigé »](https://github.com/knoel99/corriges-concours/issues/new?template=corrige.yml) :
   la réservation est acquise quand un mainteneur vous assigne l'issue, et le corrigé se dépose
   ensuite par pull request (point 2). Les identifiants des champs (`epreuve`, `lien`,
   `document`, `question`, `intention`, `description`) sont stables et servent au
   pré-remplissage par l'adresse (`…/issues/new?template=erreur.yml&epreuve=<slug>`).
2. **Corriger** :
   - *correction ponctuelle* : le lien « Proposer une correction » de chaque fiche du site ouvre
     `brut.md` ou `guide.md` de l'épreuve dans l'éditeur de GitHub ; GitHub crée le fork et la
     branche, puis propose d'ouvrir la pull request. Gardez les deux corrigés cohérents (une
     erreur du brut se retrouve souvent dans le guidé) ; la CI lance `scripts/verifier.py`.
   - *modification plus large* : forkez le dépôt, modifiez `brut.md` et/ou `guide.md` de
     l'épreuve (gardez les deux cohérents), lancez `python3 scripts/verifier.py <slug>`, puis
     ouvrez une pull request.

   Il n'y a ni `.pdf` ni `.tex` à modifier : ils sont produits depuis le Markdown. La CI de la
   pull request compile le PDF des épreuves touchées (artefact `pdf` du run) ; pour le voir
   avant, `python3 scripts/exporter/exporter.py --pdf <slug>`.

Règles de forme :

- suivre la numérotation du sujet et n'employer que des outils au programme de la filière ;
- maths en `$…$` / `$$…$$` (KaTeX) ; pas d'environnement `align`/`equation`, pas de
  `\newcommand`, pas de TikZ ni de HTML (`<svg>`, `<img>`) ;
- une figure = un fichier `figures/<nom>.svg` (sans script ni lien externe), insérée seule dans
  son paragraphe : `![Figure N — légende](figures/<nom>.svg)`, et déclarée dans `meta.json` ;
- ne pas recopier de longs passages des sujets ou des rapports de jury (droits des banques).

### Signer une rédaction ou une révision par IA

Ajoutez chaque intervention à la fin de `contributions` dans `meta.json`. Conservez les
entrées précédentes. Le journal consigne la phase (`redaction`, `relecture_corrige` ou
`retouches`, par exemple), le modèle et sa déclinaison dans `modele`, l’effort de
raisonnement dans `effort` et le mode de vitesse dans `vitesse`. Renseignez également
`date`, `modifications` et `perimetre` d’après le travail effectué. Un numéro de
`tour` permet de distinguer plusieurs passes.

Dans `brut.md` et `guide.md`, placez la signature après l’avertissement, sur une ligne
par intervention. L’ordre de lecture est modèle, effort, vitesse. Ainsi, la rédaction
Mines-Ponts de chimie PC 2024 donne **Rédaction** · GPT-6.2 Sol High standard.
Les phases `relecture_corrige` et `revision` s’affichent toutes deux sous le libellé
**Révision**. Si le journal indique `"tour": 2`, la signature correspondante peut
par exemple être **Révision (tour 2)** · GPT-6.2 Astra Ultra · vitesse non renseignée.
Conservez la valeur de vitesse enregistrée, y compris la distinction entre `standard`,
`priority` et `ultrafast`. Pour une nouvelle session, relevez les réglages effectifs
au moment de l’intervention. Pour une reprise d’archive, une valeur manquante reste
`null` et apparaît comme « non renseigné » ou « non renseignée ». Si seule la famille
est attestée, précisez-la dans `famille_modele` et laissez `modele` à `null`.

En contribuant, vous acceptez que votre contribution soit publiée sous CC BY 4.0 (corrigés) ou
MIT (scripts). Le mainteneur relit et fusionne les pull requests ; les corrections fusionnées
sont publiées sur le site (Markdown et PDF recompilés) sans autre manipulation.
