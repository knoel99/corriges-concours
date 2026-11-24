# Relectures Polytechnique et ENS

Le registre recense les sujets identifiés de Polytechnique, de l’ENS-PSL, de l’ENS de Lyon, de l’ENS Paris-Saclay et de l’ENS Rennes. Chaque ligne donne l’identifiant du corrigé, la modalité et le lien vers le sujet. Une épreuve partagée entre plusieurs écoles ou filières compte une fois. Les écrits et les oraux disposent de totaux distincts. L’identification des archives se poursuit. [Registre des sujets](epreuves.tsv)

Pour entrer dans le total des corrigés vérifiés, une épreuve doit réunir les éléments suivants.

- Une session **GPT-6.2 Astra Ultra** a rédigé ou relu sur le fond le corrigé brut et le corrigé guidé en les confrontant au sujet et, s’il existe, au rapport correspondant.
- Le journal de l’épreuve décrit l’intervention et sa portée. Les deux éditions reprennent sa signature, avec la vitesse enregistrée ou la mention « vitesse non renseignée ». Les rédactions et révisions antérieures conservent leurs propres signatures. [Format des signatures](../../CONTRIBUTING.md#signer-une-rédaction-ou-une-révision-par-ia)
- Les deux textes de l’onglet Markdown correspondent aux fichiers GitHub. La signature apparaît dans le corps de chaque corrigé en vue Lecture et sur la première page du PDF accessible depuis cette même vue.

## Lire le bilan

Le bilan daté donne les comptes par matière et les liens vers les preuves pour chaque épreuve. [Bilan du 24 novembre 2026](bilans/2026-11-24.md) · [Tableau détaillé](bilans/2026-11-24.tsv)

Depuis la racine du dépôt, cette commande écrit une ligne par épreuve avec son état dans Git, son état sur le site et le lien vers la fiche. Le contrôle des PDF utilise `pdftotext` (paquet `poppler-utils`). L’option `--site` interroge les éditions en ligne des paires portant une signature qualifiante.

```sh
python3 scripts/couverture_astra.py --site --tsv bilan-x-ens.tsv
```

Pour contrôler une livraison précise, ajoutez les identifiants des épreuves et `--exiger`. Le contrôle compare les fichiers, les signatures et les éditions en ligne. Le détail de la relecture de fond se trouve dans le journal et le diff de chaque correction.

Si seules certaines questions sont traitées, renseignez `couverture.statut` avec `partiel` dans `meta.json` et précisez les questions couvertes et les limites dans le corrigé. Le bilan affiche ces paires séparément. Lorsqu’une nouvelle archive est identifiée, ajoutez son sujet au registre.

Si une vérification du fond invalide une édition déjà signée, sa version exacte est consignée avec le motif et le sujet. Le bilan exclut cette paire tant que le brut ou le guidé contient encore la version retirée. [Rectifications documentées](rectifications.tsv)

Les options de langue de la banque Centrale-Supélec qui entrent dans l’admissibilité TSI de l’X sont rattachées à leur sujet commun aux cinq filières. Une fiche orale de l’ENS peut regrouper plusieurs planches ou dossiers d’une même discipline. Certains fascicules littéraires de Lyon réunissent plusieurs matières ou options. Leur PDF et son empreinte sont conservés pour identifier chaque sujet avant de l’ajouter au registre. [Fascicules à dépouiller](fascicules-a-depouiller.tsv)

Les fascicules entièrement dépouillés conservent leur empreinte et le nombre de sujets identifiés. Le registre renvoie à la première page de chaque sujet. [Fascicules dépouillés](fascicules-depouilles.tsv)

Certaines épreuves sont attestées par l’ENS alors que le texte ou les pièces distribuées restent à retrouver. Le relevé précise les documents manquants et la référence de l’organisateur. [Documents manquants](documents-manquants.tsv)

Pour les fascicules B/L de Lyon, le relevé distingue les planches intégrales de mathématiques, les intitulés d’exposés, les références de presse et les cartes ou dossiers à retrouver. Les options écrites 2025 présentes aussi dans le recueil de Lyon conservent leur fiche commune. [Pages des sujets et rapports B/L de Lyon](sections-b-l-lyon.tsv)
