# Relectures Polytechnique et ENS

Le registre recense les sujets identifiés de Polytechnique, de l’ENS-PSL, de l’ENS de Lyon, de l’ENS Paris-Saclay et de l’ENS Rennes. Chaque ligne donne l’identifiant du corrigé, la modalité et le lien vers le sujet. Une épreuve partagée entre plusieurs écoles ou filières compte une fois. Le bilan distingue les écrits, les oraux et les projets pratiques. L’identification des archives se poursuit. [Registre des sujets](epreuves.tsv)

Pour entrer dans le total des corrigés vérifiés, une épreuve doit réunir les éléments suivants.

- Une session **GPT-6.2 Astra Ultra** a rédigé ou relu sur le fond le corrigé brut et le corrigé guidé en les confrontant au sujet et, s’il existe, au rapport correspondant.
- Le journal de l’épreuve décrit l’intervention et sa portée. Les deux éditions reprennent sa signature, avec la vitesse enregistrée ou la mention « vitesse non renseignée ». Les rédactions et révisions antérieures conservent leurs propres signatures. [Format des signatures](../../CONTRIBUTING.md#signer-une-rédaction-ou-une-révision-par-ia)
- Les deux textes de l’onglet Markdown correspondent aux fichiers GitHub. La signature apparaît dans le corps de chaque corrigé en vue Lecture et sur la première page du PDF accessible depuis cette même vue.

La colonne « sessions IA » du tableau détaillé reprend les identifiants consignés dans le journal lors de la rédaction ou de la révision. Plusieurs identifiants peuvent figurer sur une même épreuve. La mention « Non renseignée » signale une intervention dont le journal atteste le modèle et l’effort sans nommer la session.

Les sujets d’informatique et de mathématiques-informatique des ENS depuis 2003, ainsi que les compositions B communes depuis 2011, sont distingués par la garde de chaque cahier. En 2010, l’épreuve des trois ENS sur les programmes à compteurs entiers diffère de celle de Polytechnique sur le plus proche ancêtre commun. Le rapport sur les rotations et repliages de mots de 2009 est conservé par l’ENS de Paris. En 2011, la bonne épreuve B sur les permutations est dans la rubrique MP. La banque déclare l’épreuve B supprimée en 2020. Les rapports sont rattachés après lecture de leur en-tête. [Sujets, rapports et empreintes des fichiers](informatique-ecrits-2003-2025.tsv) · [Annales officielles de la banque PC](https://banques-ecoles.fr/cms/filiere-pc/les-annales-et-rapports-des-jurys/)

Les deux concours ont aussi des compositions distinctes avant 2010. Le lycée Faidherbe conserve le cahier de 1997 des ENS de Paris et de Lyon. Les premiers sujets de mathématiques-informatique comprennent les carrés latins, donnés en 2002 au groupe I des filières MP et PC. [Archives antérieures et empreintes des cahiers](informatique-ecrits-1997-2009.tsv)

Pour la modélisation PSI 2016 sur le GPS, le fac-similé de seize pages donne aussi les deux feuilles du document-réponse avec les figures A, B et C. [Cahier officiel et exemplaire avec les feuilles-réponses](modelisation-psi-2016.tsv)

## Lire le bilan

Le bilan daté donne les comptes par matière et les liens vers les preuves pour chaque épreuve. [Dernier bilan sur le site](https://sujet-corriges.ai/couverture-x-ens) · [Recherche par épreuve](https://sujet-corriges.ai/couverture-x-ens/epreuves) · [Relevés datés sur GitHub](bilans/)

Depuis la racine du dépôt, cette commande écrit une ligne par épreuve avec son état dans Git, son état sur le site et le lien vers la fiche. Le contrôle des PDF utilise `pdftotext` (paquet `poppler-utils`). L’option `--site` interroge les éditions en ligne des paires portant une signature qualifiante.

```sh
python3 scripts/couverture_astra.py --site --tsv bilan-x-ens.tsv
```

Pour contrôler une livraison précise, ajoutez les identifiants des épreuves et `--exiger`. Le contrôle compare les fichiers, les signatures et les éditions en ligne. Le détail de la relecture de fond se trouve dans le journal et le diff de chaque correction.

Si seules certaines questions sont traitées, renseignez `couverture.statut` avec `partiel` dans `meta.json` et précisez les questions couvertes et les limites dans le corrigé. Le bilan affiche ces paires séparément. Lorsqu’une nouvelle archive est identifiée, ajoutez son sujet au registre.

Si une vérification du fond invalide une édition déjà signée, sa version exacte est consignée avec le motif et le sujet. Le bilan exclut cette paire tant que le brut ou le guidé contient encore la version retirée. [Rectifications documentées](rectifications.tsv)

Pour 2022 à 2024, le registre identifie 25 écrits de l’X et des ENS en français, langues, informatique, physique et sciences de l’ingénieur. Les 31 pages suivant les gardes des cinq dossiers communs de français et de langues en 2024 ont la même image dans les versions de l’X et de PSI. Pour l’informatique B, le tableau précise les filières concernées et donne aussi le second rapport disponible pour 2023. [Sujets et rapports de 2022 à 2024](ecrits-x-ens-2022-2024.tsv) · [Arrêté sur les banques MP, MPI et PC](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000046503494/) · [Structure de la banque MPI en 2024](https://banques-ecoles.fr/cms/wp-content/uploads/2023/12/24_mpi_structure_bq.pdf)

Pour les écrits scientifiques de 2025, les gardes identifient l’école et les filières de neuf sujets supplémentaires. En français et dans quatre langues, les 36 pages qui suivent les gardes sont identiques dans le sujet de l’X et dans sa version PSI publiée par l’ENS. Chaque épreuve commune compte une fois. [Sujets et rapports de 2025](ecrits-x-ens-2025.tsv)

Pour le concours Droit-économie de Rennes de 2024 et 2025, chaque option écrite renvoie à sa première page dans le fascicule officiel. Le registre distingue les empreintes des fichiers institutionnels et celles des aperçus PDF consultés. Deux rapports de langue orale de 2025 attestent des épreuves dont les articles restent à retrouver. [Écrits et oraux de Rennes](droit-economie-rennes-2024-2025.tsv)

Les options de langue de la banque Centrale-Supélec qui entrent dans l’admissibilité TSI de l’X sont rattachées à leur sujet commun aux cinq filières. Une fiche orale de l’ENS peut regrouper plusieurs planches ou dossiers d’une même discipline. Certains fascicules littéraires de Lyon réunissent plusieurs matières ou options. Leur PDF et son empreinte sont conservés pour identifier chaque sujet avant de l’ajouter au registre. [Fascicules à dépouiller](fascicules-a-depouiller.tsv)

Les fascicules entièrement dépouillés conservent leur empreinte et le nombre de sujets identifiés. Le registre renvoie à la première page de chaque sujet. [Fascicules dépouillés](fascicules-depouilles.tsv)

Certaines épreuves sont attestées par l’ENS alors que le texte ou les pièces distribuées restent à retrouver. Le relevé précise les documents manquants et la référence de l’organisateur. [Documents manquants](documents-manquants.tsv)

Pour les fascicules B/L de Lyon, le relevé distingue les planches intégrales de mathématiques, les intitulés d’exposés, les références de presse et les cartes ou dossiers à retrouver. Les options écrites 2025 présentes aussi dans le recueil de Lyon conservent leur fiche commune. [Pages des sujets et rapports B/L de Lyon](sections-b-l-lyon.tsv)

À l’oral d’espagnol A/L de l’ENS-PSL, le tronc commun est répertorié en un fascicule de 27 références. Pour l’option, le rapport donne séparément cinq passages, deux de Calderón et trois de Saer. Il mentionne successivement quatre et cinq candidats, puis détaille cinq notes et cinq extraits. [Références des oraux d’espagnol](oraux-espagnol-ulm-2026.tsv)

Les oraux de la sélection internationale Lettres de 2016 à 2019 sont identifiés par consigne, y compris lorsque plusieurs candidats recevaient des extraits différents réunis dans le même PDF. Les deux index qui reproduisent le commentaire de Biland en 2016 renvoient à une même épreuve. La page finale du recueil littéraire de 2016 reproduit la consigne de l’écrit sur Modiano. Les feuillets d’histoire de l’art de 2016 et 2018 sont datés au moyen des œuvres et des rapports de session. [Épreuves orales et pages des recueils](ulm-selection-lettres-oraux-2016-2019.tsv)

Pour la sélection internationale Lettres de 2016 à 2019, les sujets et leurs annexes ont été lus ensemble. Les deux feuillets de lettres classiques de 2017 identifient des oraux sur Platon et Sénèque, y compris dans la rubrique « écrits » de l’index. Leurs consignes précisent la durée de l’exposé et de l’entretien. Six écrits du concours normalien étudiant de 2019, 2021 et 2022 complètent le dépouillement. [Sujets, exemplaires et pièces distribuées](ulm-selection-2016-2019-et-cnel-2019-2022.tsv)

La sélection internationale Lettres de 2022 comprend quatorze écrits et onze oraux identifiés. Les deux sujets de droit figurent dans les archives du jury, qui indique dans son rapport que la demande d’audition en droit n’a pas abouti. Le cabinet de porcelaine de Charlottenburg est illustré dans le feuillet d’arts. Le lien du commentaire de film est conservé avec l’état de son support. Pour 2023, les dossiers oraux sur Galien, sur le conseil et sur les signaux de communication ont été retrouvés. [Consignes, annexes et rapports](ulm-selection-lettres-2022-oraux-2023.tsv)

Au concours normalien étudiant de sciences de l’Antiquité, onze fichiers de 2021 correspondent à cinq sujets et quinze fichiers de 2022 à onze sujets. Les consignes, les passages, les annexes et leurs différentes présentations sont réunis par sujet. [Exemplaires et sujets de 2021 et 2022](ulm-cnel-antiquite-2021-2022.tsv)

À Ulm en 2023, onze sujets distincts de sciences de l’Antiquité du concours normalien étudiant et douze écrits de la sélection internationale Lettres ont été rapprochés de leurs documents. Les deux questions d’histoire individuelle sont distinguées. Les exemplaires de Stace et de Valéry qui posent la même question sont regroupés. Les ressources distribuées en géographie et en études cognitives accompagnent les consignes. [Registre des sujets et des pièces](ulm-lettres-cnel-selection-2023.tsv)

Le concours normalien étudiant Lettres de l’ENS-PSL comprend des épreuves propres aux départements. Les sujets identifiés dans les rapports indiquent leur page et les documents restant à retrouver. [Sujets et rapports du CNEL 2026](cnel-lettres-2026.tsv)

En design à Paris-Saclay, le techno-design est un écrit d’admissibilité. L’épreuve pratique d’admission offre trois sujets au choix. Chaque option dispose de son original et de sa propre fiche. [Article 10 du règlement](https://www.enseignementsup-recherche.gouv.fr/fr/bo/2025/Hebdo32/MENS2523783A) · [Sources des projets de design et des oraux de sélection internationale](design-et-selection-internationale-2026.tsv)

Les rapports de sélection internationale Lettres donnent les six intitulés individuels d’économie, le sujet de sciences sociales et les écrits et oraux d’études classiques. Les jurys de droit, de géographie et de linguistique indiquent que leurs dossiers de candidature n’ont donné lieu à aucune admissibilité en 2026. [Sujets reproduits dans les rapports](selection-internationale-jurys-2026.tsv) · [Rapports officiels 2026](https://www.ens.psl.eu/une-formation-d-exception/admission-concours/international/concours-selection-internationale-0)

L’ENS Paris-Saclay utilise les admissibilités HEC Paris, ESSEC ou ESCP pour son concours Économie-gestion option II (ECG). Onze sujets communs et dix-huit options ELVi sont rattachés à leurs fiches BCE. La brochure identifie les écoles utilisatrices, les concepteurs et les langues ouvertes en ECG. La synthèse, également accessible en ECT, figure une fois sous ECG. [Épreuves BCE retenues](admissibilite-saclay-ecg-2026.tsv) · [Brochure BCE, parcours et coefficients](https://www.concours-bce.com/sites/default/files/2025-11/2026_Brochure_BCE_2026_web_VF.pdf#page=8) · [Notice des ENS](https://ens-paris-saclay.fr/sites/default/files/CONCOURS/CONCOURS_2026/2026_Notice_interENS.pdf)

Les annales orales A/L de Lyon donnent des listes par série, des sujets accompagnés de planches et une sélection de textes espagnols. Le tableau identifie les quinze fascicules, les cinq épreuves de cinéma, les trois sujets d’histoire des arts et les deux exercices distincts d’écriture musicale. [Fascicules et pages des sujets de Lyon](oraux-lettres-lyon-2026.tsv)

À Ulm, 70 fascicules d’oraux A/L de 2026 ont été contrôlés sur les originaux. Un même fichier lié depuis plusieurs dates ne compte qu’une fois. Le registre signale les désaccords entre dates ou commissions et les passages dont seules les références ont été publiées. [Sources des oraux A/L à Ulm](oraux-lettres-ulm-2026.tsv)

Pour le concours design de Cachan puis de Paris-Saclay, le registre distingue les écrits d’admissibilité, les projets pratiques et les sujets connus par le seul rapport du jury. En 2015, l’expression graphique, chromatique ou volumique est un écrit. En 2020, les candidats choisissaient leur champ d’intervention à partir du même dossier sur la fontaine à l’Albien. [Sources du design de 2015 à 2025](design-archives.tsv)

Les gardes de vingt-quatre compositions de mathématiques des ENS de 2003 à 2014 permettent de distinguer les épreuves communes à deux écoles, les compositions MPI 1 et MPI 2 et les mathématiques C et D. Le relevé contient également les deux rapports des correcteurs de mathématiques A et B de 2013, ainsi que le corrigé de référence publié par l’ENS pour MPI 1 en 2007. [Sujets, rapports, empreintes et écoles](mathematiques-ens-2003-2014.tsv)

Les gardes des vingt-deux compositions de mathématiques de Polytechnique de 2000 à 2010 donnent l’école, la filière MP, le numéro et la durée. Les deux compositions de 2010 sont désormais rattachées à l’X. Les rapports des correcteurs sont documentés, y compris les rapports B de 2011 et de 2012 et les rapports A et B de 2015. [Compositions et rapports de Polytechnique](mathematiques-polytechnique-2000-2015.tsv)

Le sujet de sciences industrielles en PSI de 2015 comporte trois feuilles-réponses. Elles figurent aux pages PDF 30 à 32 du cahier et sont également accessibles en fichier séparé. Le rapport du jury porte la session 2015 en première page. [Cahier, feuilles et rapport](sciences-industrielles-psi-2015.tsv)

Le rapport de grec A/L de 2026 reproduit un billet d’Aristophane avec ses coupures et ses notes. L’exemple complète les feuilles où figure l’auteur. La date du passage reste indéterminée et le décompte des fascicules est conservé. [Exemples de billets publiés par les jurys](exemples-de-billets-du-jury.tsv)

En 1999, Ulm et Lyon ont donné un sujet d’informatique de quatre heures sur les automates cellulaires. La même année, Lyon et Cachan ont consacré leur composition de mathématiques-informatique aux polynômes creux, en trois heures. Les deux cahiers originaux figurent dans les archives de Stéphane Gonnord. [Cahiers et empreintes](informatique-ecrits-1997-2009.tsv)

Pour Rennes, les deux sessions 2022 et 2023 réunissent huit écrits en économie, droit civil, droit commercial et droit public. Chaque épreuve est associée à son sujet et à son rapport. Le relevé distingue les empreintes de la collecte institutionnelle et celles des fichiers lus en aperçu. [Seize documents du concours Droit-économie](rennes-droit-economie-2022-2023.tsv)

Les archives de l’UPS donnent les trois compositions d’informatique de Polytechnique de 1997 à 1999 et le cahier de 1998 commun aux ENS d’Ulm et de Lyon, groupes C/S, M et I. Elles conservent aussi deux cahiers ENS déjà recensés et six corrigés pédagogiques attribués à leurs auteurs. Le registre indique la longueur et l’empreinte de chacun des douze fichiers. [Pièces et auteurs](informatique-ups-1997-1999.tsv) · [Archives de l’UPS](https://prepas.org/index.php?module=Sujets)

L’ENS Paris-Saclay publie aussi les annales de son ancien concours d’entrée en deuxième année. Les treize pages de l’index de 2017 à 2024 contiennent 140 liens vers 137 adresses distinctes. Deux cahiers de PSI de 2017 étaient déjà recensés et deux notices de français de 2023 renvoient au même fichier. Six épreuves de 2023 et 2024 ont été rapprochées de leur sujet. Pour les deux oraux d’anglais de 2024, l’école donne les consignes et les références des six extraits adaptés. [Index, documents et rattachements](cycle-master-paris-saclay.tsv) · [Annales du concours de deuxième année](https://ens-paris-saclay.fr/admission/voie-eleve-concours/concours-cycle-master/annales-2nd-concours)

Pour Rennes, les options de droit commercial, de droit public et de mathématiques appliquées de 2020 et 2021 figurent dans des fascicules communs. Chaque fiche ouvre la première page de son option. Les sujets de mathématiques de 2022 et 2023 sont des fichiers distincts. Les douze fiches ajoutées associent le sujet à son rapport et distinguent l’empreinte de la collecte de celle de l’aperçu consulté. [Sujets, pages des options et rapports de Rennes](rennes-droit-economie-2020-2023.tsv)
