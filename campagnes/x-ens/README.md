# Relectures Polytechnique et ENS

Le registre recense les sujets identifiés de Polytechnique, de l’ENS-PSL, de l’ENS de Lyon, de l’ENS Paris-Saclay et de l’ENS Rennes. Chaque ligne donne l’identifiant du corrigé, la modalité et le lien vers le sujet. Une épreuve partagée entre plusieurs écoles ou filières compte une fois. Les écrits et les oraux disposent de totaux distincts. L’identification des archives se poursuit. [Registre des sujets](epreuves.tsv)

Pour entrer dans le total des corrigés vérifiés, une épreuve doit réunir les éléments suivants.

- Une session **GPT-6.2 Astra Ultra** a rédigé ou relu sur le fond le corrigé brut et le corrigé guidé en les confrontant au sujet et, s’il existe, au rapport correspondant.
- Le journal de l’épreuve décrit l’intervention et sa portée. Les deux éditions reprennent sa signature, avec la vitesse enregistrée ou la mention « vitesse non renseignée ». Les rédactions et révisions antérieures conservent leurs propres signatures. [Format des signatures](../../CONTRIBUTING.md#signer-une-rédaction-ou-une-révision-par-ia)
- Les deux textes disponibles sur le site correspondent aux sources GitHub. La première page de chacun des deux PDF porte la signature attendue.

## Lire le bilan

Depuis la racine du dépôt, cette commande écrit une ligne par épreuve avec son état dans Git, son état sur le site et le lien vers la fiche. Le contrôle des PDF utilise `pdftotext` (paquet `poppler-utils`). L’option `--site` interroge les éditions en ligne des paires portant une signature qualifiante.

```sh
python3 scripts/couverture_astra.py --site --tsv bilan-x-ens.tsv
```

Pour contrôler une livraison précise, ajoutez les identifiants des épreuves et `--exiger`. Le contrôle compare les fichiers, les signatures et les éditions en ligne. Le détail de la relecture de fond se trouve dans le journal et le diff de chaque correction.

Si seules certaines questions sont traitées, renseignez `couverture.statut` avec `partiel` dans `meta.json` et précisez les questions couvertes et les limites dans le corrigé. Le bilan affiche ces paires séparément. Lorsqu’une nouvelle archive est identifiée, ajoutez son sujet au registre.
