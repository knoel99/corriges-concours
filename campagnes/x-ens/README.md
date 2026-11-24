# Relectures Polytechnique et ENS

Le registre recense les sujets identifiés de Polytechnique, de l’ENS-PSL, de l’ENS de Lyon, de l’ENS Paris-Saclay et de l’ENS Rennes. Chaque ligne donne l’identifiant du corrigé, la modalité et le lien vers le sujet. Une épreuve partagée entre plusieurs écoles ou filières compte une fois. Le bilan distingue les écrits, les oraux et les projets pratiques. L’identification des archives se poursuit. [Registre des sujets](epreuves.tsv)

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

Le concours normalien étudiant Lettres de l’ENS-PSL comprend des épreuves propres aux départements. Les sujets identifiés dans les rapports indiquent leur page et les documents restant à retrouver. [Sujets et rapports du CNEL 2026](cnel-lettres-2026.tsv)

En design à Paris-Saclay, le techno-design est un écrit d’admissibilité. L’épreuve pratique d’admission offre trois sujets au choix. Chaque option dispose de son original et de sa propre fiche. [Article 10 du règlement](https://www.enseignementsup-recherche.gouv.fr/fr/bo/2025/Hebdo32/MENS2523783A) · [Sources des projets de design et des oraux de sélection internationale](design-et-selection-internationale-2026.tsv)

Les rapports de sélection internationale Lettres donnent les six intitulés individuels d’économie, le sujet de sciences sociales et les écrits et oraux d’études classiques. Les jurys de droit, de géographie et de linguistique indiquent que leurs dossiers de candidature n’ont donné lieu à aucune admissibilité en 2026. [Sujets reproduits dans les rapports](selection-internationale-jurys-2026.tsv) · [Rapports officiels 2026](https://www.ens.psl.eu/une-formation-d-exception/admission-concours/international/concours-selection-internationale-0)

L’ENS Paris-Saclay utilise les admissibilités HEC Paris, ESSEC ou ESCP pour son concours Économie-gestion option II (ECG). Onze sujets communs et dix-huit options ELVi sont rattachés à leurs fiches BCE. La brochure identifie les écoles utilisatrices, les concepteurs et les langues ouvertes en ECG. La synthèse, également accessible en ECT, figure une fois sous ECG. [Épreuves BCE retenues](admissibilite-saclay-ecg-2026.tsv) · [Brochure BCE, parcours et coefficients](https://www.concours-bce.com/sites/default/files/2025-11/2026_Brochure_BCE_2026_web_VF.pdf#page=8) · [Notice des ENS](https://ens-paris-saclay.fr/sites/default/files/CONCOURS/CONCOURS_2026/2026_Notice_interENS.pdf)
