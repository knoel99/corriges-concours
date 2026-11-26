# Essai local de publication des corrigés

Le 26/11/2026 à 23 h 58 UTC, les 2355 paires signées de la révision `c95aa02d` ont fourni les deux textes attendus et leurs signatures dans le service de lecture du site. Le journal de chaque fiche renvoie au bon dossier GitHub, reprend les interventions qualifiantes et indique le caractère partiel quand il est déclaré. [Résultats par épreuve](prepublication-lecteurs.tsv) · [Version des corrigés](https://github.com/knoel99/corriges-concours/tree/c95aa02da9c858e422e6ad0937fd170ca4e85a9b) · [Version du site](https://github.com/knoel99/prepa/tree/af2e6c55fbdd1f17963ffaa8da1b6d4941ceac02)

Le contrôle couvre 2829 fiches de filière pour 2355 épreuves signées. Les épreuves communes sont aussi vérifiées sous chaque filière de leur notice éditoriale. [Contrôles des 474 fiches supplémentaires](prepublication-lecteurs-autres-filieres.tsv)

L’essai utilise une base SQLite temporaire et les fichiers locaux des révisions Git. La conversion du dépôt public et le plan de publication du site produisent les clés du stockage. La synchronisation charge d’abord le contenu de `54fe93cd`, puis celui de la branche de travail. Pour chaque édition, le service qui alimente le lecteur doit restituer exactement le Markdown attendu après la réécriture des chemins d’illustrations. Le contrôle vérifie aussi la présence de chaque SVG référencé. Si une édition ne référence aucun SVG, la colonne de disponibilité est positive et le classeur des épreuves indique zéro illustration pour cette édition.

Une compilation locale indépendante des 74 PDF de français et de langues MP-PC de 2011 à 2014 a produit 202 pages. Pour chacune des deux éditions, la première page porte la signature attendue et LaTeX inclut les schémas. [Pages, empreintes et révisions des 37 épreuves](pdf-francais-langues-mp-pc-2011-2014.tsv)

Pour les dix écrits d’option informatique de l’X en MP de 2000 à 2009, les 20 PDF compilés ont été recoupés avec les empreintes du convertisseur, les arbres Git des rédactions et les journaux LaTeX. Les signatures et les figures des deux éditions ont été vérifiées. Les PDF totalisent 119 pages. [Contrôles des dix écrits](pdf-option-informatique-mp-2000-2009.tsv)

Les 200 fiches MP et PC des 100 compositions de 2005 à 2008 ont également été interrogées via l’API locale du site. Pour chaque fiche, le sujet et son numéro de page, le rapport quand il existe, les documents complémentaires et la provenance affichée concordent avec le registre. [Sources par fiche](sources-fiches-mp-pc-2005-2008.tsv) · [Version du catalogue contrôlée](https://github.com/knoel99/prepa/tree/d63723b)

Les 32 fiches de filière des 16 compositions de l’X–ESPCI en 2009 et 2010 ont été contrôlées de la même manière. Le catalogue précise que l’ESPCI recrutait en PC. [Sources par fiche en 2009 et 2010](sources-fiches-x-espci-2009-2010.tsv)

Pour 40 compositions de français et de langues en MP-PC-PSI de 2015 à 2021, les 80 PDF compilés totalisent 261 pages. Le contrôle compare les arbres Git et les empreintes de conversion, relit les signatures en première page et vérifie que les schémas sont incorporés dans les deux éditions. [Détail par épreuve](pdf-francais-langues-mp-pc-psi-2015-2021.tsv)

Pour les 28 compositions de français, d’anglais et d’arabe de 2005 à 2008, les 56 PDF totalisent 152 pages. La signature et les illustrations ont été vérifiées dans chaque PDF, avec les empreintes des fichiers de rédaction et de conversion. [Contrôles des 28 compositions](pdf-francais-anglais-arabe-mp-pc-2005-2008.tsv)

Les 55 fiches de langues A/L de 2023 à 2025 renvoient aux pages des livrets vérifiées dans l’API locale. Pour le thème polonais de 2023, la fiche distingue le rapport de langue complémentaire. [Résultats des 55 fiches](sources-fiches-langues-bel-al-2023-2025.tsv)

Quinze autres écrits de spécialité du même fascicule annuel sont identifiés en philosophie, grec, latin, lettres modernes et histoire. Les fiches locales renvoient aux pages du sujet et du rapport adéquates. Pour le grec 2023, le feuillet imprime trois heures et le rapport du jury indique le passage à quatre heures. [Pages et rubriques contrôlées](sources-fiches-specialites-bel-al-2023-2025.tsv)

Parmi ces quinze écrits de spécialité, 15 disposent de deux PDF intégraux signés et contrôlés, sur 82 pages. [Contrôles des PDF des spécialités](pdf-specialites-bel-al-2023-2025.tsv)

Parmi ces 55 écrits, 54 ont leurs deux PDF signés vérifiés, soit 252 pages. Les sujets et les rubriques du jury ont été rapprochés des références éditoriales et de l’API du site. [Contrôles par édition](pdf-langues-bel-al-2023-2025.tsv)

En Banque PT, les 102 fiches des sessions 2017 à 2025 ont été ouvertes dans l’API locale. Les 306 liens de sujets, de rapports et de coefficients correspondent aux références institutionnelles. [Sources par épreuve](sources-fiches-banque-pt-2017-2025.tsv)

Pour les mathématiques C de Banque PT 2017 à 2019, les éditions brute et guidée traitent chacune les 100 questions et sous-questions. Les six PDF signés totalisent 47 pages et 323 signets. [Résultats par édition et empreintes des sources](pdf-banque-pt-maths-c-2017-2019.tsv)

En Banque PT, les deux éditions de mathématiques A de 2017 à 2019 traitent chacune les 103 questions et sous-questions. Les six PDF totalisent 41 pages et 341 signets. En français A et B de 2017 et 2018, les huit PDF totalisent 19 pages. Les deux résumés comptent 190 mots pour Camus et 180 pour Chalier. [Mathématiques A](pdf-banque-pt-maths-a-2017-2019.tsv) · [Français A et B](pdf-banque-pt-francais-2017-2018.tsv)

Pour les mathématiques de l’X de 1985 à 1989, 30 fiches locales affichent le fac-similé authentifié et la notice annuelle du concours. Deux épreuves communes donnent chacune accès à deux voies. Les deuxièmes compositions M′ 1986 et P′ 1989 ont quatre PDF signés pour 58 questions et sous-questions. [Sources des 30 fiches](sources-fiches-mathematiques-x-1985-1989.tsv) · [Contrôles des quatre PDF](pdf-mathematiques-x-1986-1989.tsv)

Pour les mathématiques A et C de la Banque PT en 2020, 2021 et 2022, les 12 PDF couvrent 229 questions et sous-questions. Les sujets de mathématiques C de 2020 et 2022 comportent une planche A4 imprimable à 100 % avec respectivement 3 et 2 cm par unité sur les deux axes. [Mathématiques A](pdf-banque-pt-maths-a-2020-2022.tsv) · [Mathématiques C](pdf-banque-pt-maths-c-2020-2022.tsv) · [Liens dans les quatre éditions concernées](liens-planches-banque-pt-maths-c-2020-2022.tsv)

Les huit PDF de français A et B de 2019 et 2020 totalisent 18 pages. Les résumés de Larroque et de Braud comptent 190 et 200 mots. Les trois fascicules de langue vivante A de 2017 à 2019 offrent chacun le choix entre l’allemand, l’anglais, l’arabe, l’espagnol et l’italien. Les 15 synthèses et leurs guides couvrent 75 documents. [Français](pdf-banque-pt-francais-2019-2020.tsv) · [Langues vivantes A](pdf-banque-pt-lva-2017-2019.json)

Pour chaque session de Banque PT entre 2017 et 2025, les deux français, la langue vivante A dans les cinq langues, et les mathématiques A et C sont intégralement corrigés. Les 90 PDF signés totalisent 505 pages. Les épreuves de français A et B disposent de 36 PDF, et les 45 synthèses de langues sont réparties dans 18 PDF. [Tableau des 45 épreuves et de leurs deux PDF](couverture-francais-langues-mathematiques-banque-pt-2017-2025.tsv)

En philosophie générale de l’art au concours Design, les deux éditions sont complètes pour dix sessions de 2015 à 2026. Les calendriers attestent aussi les épreuves de 2019 et 2022. Les deux énoncés restent à retrouver. Pour 2023, la fiche renvoie au feuillet de philosophie sur Simondon, après vérification de la garde. [Détail par session](philosophie-de-lart-design-2015-2026.tsv)

Banque PT, informatique et modélisation. Pour les sessions 2017, 2018, 2019, 2020, 2021, 2023, 2024, 2025, les deux PDF couvrent 336 questions. Chaque signet a été vérifié sur la page de réponse. Le sujet 2023 porte sur l’élasticité et le piégeage optique. Le titre de réverbération cité par erreur au début du rapport 2023 correspond au feuillet 2020. [Contrôle de chaque question](questions-informatique-modelisation-banque-pt-2017-2025.tsv) · [Sources officielles et empreintes](sources-informatique-modelisation-banque-pt-2017-2025.tsv)

Les deux compositions de mathématiques A et C de chacune des neuf sessions 2017 à 2025 de la Banque PT sont entièrement traitées. Les 36 PDF couvrent 686 questions et sous-questions, sur 297 pages, avec 2239 signets. Les trois feuilles millimétrées des mathématiques C 2023 et 2024 se téléchargent depuis les corrigés. [Sources et empreintes des 36 éditions](pdf-banque-pt-mathematiques-a-et-c-2017-2025.tsv) · [Échelle des tracés](planches-banque-pt-maths-c-2023-2025.tsv)

Pour les sessions historiques 1985 à 1989 de l’X, 30 compositions ont leurs deux éditions intégrales vérifiées. Les 60 PDF traitent 701 questions et sous-questions, sur 374 pages. [Fac-similés, signatures et signets](pdf-mathematiques-x-1985-1989.tsv)

Pour les 21 dossiers de Médecine-Humanités de 2018 à 2026, l’API locale affiche les sources attendues sur chaque fiche, dont 18 avec un rapport et cinq liens complémentaires. [Vérifications des 21 fiches](sources-fiches-medecine-humanites-2018-2026.tsv)

Les 40 sujets de physique A PC (2011 à 2014 et 2016 à 2021), d’italien (2005 à 2010), d’allemand et de chinois (2005 à 2008) ont fait l’objet d’un contrôle indépendant sur les fichiers compilés. Les 80 PDF portent la signature attendue et totalisent 267 pages. La conversion reproduit les 80 sources LaTeX, avec 150 références aux figures. La physique A PC 2017 reste partielle. [Contrôles par épreuve](pdf-physique-a-pc-italien-allemand-chinois-2026-11-26.tsv)

En physique, économie, gestion, médecine et humanités, littérature, portugais et russe, les 94 PDF des 47 paires ont été contrôlés sur leurs sources Git. Ils totalisent 482 pages et 184 insertions de schémas. [Révisions, pages et empreintes de chaque édition](pdf-physique-economie-humanites-langues-2026-11-26.tsv)

Pour les 12 analyses économiques de Paris-Saclay et 14 sujets de la Sélection internationale Lettres de l’ENS-PSL, les archives ont été relues PDF par PDF. Les 52 fichiers totalisent 179 pages. Les signatures correspondent aux deux éditions et les arbres de rédaction à la branche. [Pages, empreintes et révisions](pdf-analyses-saclay-et-selection-lettres-2026-11-26.tsv)

Les 47 épreuves relues en économie et en sociologie ont fourni 94 PDF signés, totalisant 427 pages. Chaque fichier a été comparé aux octets de l’archive et rattaché à l’arbre Git de la paire relue. [Couverture, signatures des PDF et empreintes](pdf-revues-economie-sociologie-2026-11-26.tsv)

Pour les sept épreuves de langues du concours D-E et l’anglais 2SEP de Rennes en 2026, les signatures, les figures et les empreintes des seize PDF ont été vérifiées sur les fichiers issus de la rédaction. Ils totalisent 76 pages. [Contrôles et empreintes par PDF](pdf-langues-rennes-de-2sep-2026-11-26.tsv)

Les 24 PDF de onze épreuves de la Sélection internationale Lettres et de l’oral d’histoire contemporaine B/L à Lyon totalisent 72 pages. Avec le gabarit corrigé, les 142 signets renvoient aux titres correspondants. [Contrôles et empreintes par PDF](pdf-signets-selection-lettres-et-histoire-lyon-2026-11-26.tsv)

Les quatorze épreuves d’informatique ENS de 1997 à 2010, onze épreuves de lettres et l’oral de grec de Lyon ont été recompilés sur le gabarit aux signets corrigés. Les signatures, les pages et les figures ont été vérifiées dans les deux éditions. [Contrôles et empreintes par PDF](pdf-informatique-ens-1997-2010-et-lettres-2026-11-26.tsv)

Les 26 PDF des treize épreuves de Médecine-Humanités de 2018, 2020 et 2022 totalisent 69 pages. La première page de chaque PDF porte la signature du journal. Chaque empreinte correspond au fichier de l’archive. [Oraux de 2018](pdf-medecine-humanites-2018-2026-11-26.tsv) · [Oraux de 2020](pdf-medecine-humanites-2020-2026-11-26.tsv) · [Écrits de 2022](pdf-medecine-humanites-2022-2026-11-26.tsv)

Un contrôle consolidé relie les 166 PDF de langues anciennes et modernes à leurs sources et aux deux éditions. Ils totalisent 584 pages et 141 schémas distincts par épreuve. La série comprend 81 paires complètes et deux oraux de latin partiels, à Lyon et à Ulm. Les fichiers de Rennes figurent aussi dans leur relevé détaillé. [Empreintes, pages et couverture](pdf-83-epreuves-langues-anciennes-et-modernes-2026-11-26.tsv)

Le 26 novembre, le contrôle sur le site public ne retrouvait pas encore la paire attendue pour le grec oral de Lyon 2026. Le lecteur de « Guerre et humanité » de 2022 répondait HTTP 404. [Résultat des deux sondes](production-grec-lyon-et-medecine-humanites-2026-11-26.tsv)

Les sept épreuves mixtes de mathématiques-informatique de 2002, 2004, 2005, 2006, 2008, 2009 et 2010 disposent de 14 PDF complets et signés, soit 89 pages. Le rapport de 2002 reste introuvable. [Révisions et empreintes](pdf-mathematiques-informatique-ens-2002-2010.tsv)

Les trois compositions françaises et les trois compositions de philosophie de Lyon (2017, 2019 et 2022), ainsi que les cinq oraux de philosophie de la Sélection internationale Lettres de 2018, ont été revus dans les deux éditions. Les 22 PDF totalisent 79 pages et 128 signets contrôlés. [Révisions et empreintes](pdf-signets-philosophie-et-francais-lyon-psl-2026-11-26.tsv)

Les six oraux d’histoire et de littérature ENS-PSL 2018, sur Monteil, Ginzburg, Renan, Cendrars, Djebar et Rolin, comptent douze PDF de 35 pages et 69 signets vérifiés. [Feuillets officiels, commits et empreintes](pdf-signets-oraux-histoire-litterature-psl-2018-2026-11-26.tsv)

Pour sept sessions de sciences industrielles PSI de 2009 à 2017, les 14 PDF signés totalisent 179 pages. La relecture couvre 332 questions et 22 documents-réponses. Pour 2016, les trois feuilles absentes du livret institutionnel ont été vérifiées sur la reproduction renseignée de l’UPSTI. [Révisions, figures et empreintes](pdf-sciences-industrielles-psi-2009-2017.tsv)

Les huit options de langues vivantes B/L de 2025 ont été confrontées à leurs 29 documents. Leurs seize PDF signés totalisent 39 pages. [Feuillets, révisions et empreintes](pdf-bel-bl-huit-langues-2025.tsv)

Les deux épreuves de mathématiques approfondies BCE 2026 et les mathématiques D ENS 2023 totalisent 137 questions et sous-questions. Les six PDF ont été vérifiés sur leurs 100 pages. [Révisions, pagination et empreintes](pdf-bce-approfondies-2026-et-maths-d-2023.tsv)

Les 1488 PDF rassemblés dans ce relevé totalisent 10185 pages. Les empreintes des PDF et de leurs archives correspondent aux éditions signées. Pour chaque édition, le nombre d’objets graphiques effectivement affichés dans le PDF couvre le nombre de schémas SVG distincts référencés par le texte. Le relevé donne leurs pages et distingue objets vectoriels et images matricielles. [Preuves par épreuve et par édition](pdf-maths-physique-et-sociologie-2026-11-26.tsv)

Les 166 questions des quinze épreuves d’informatique PSI–PT de 2002 à 2016 ont été repérées à la fois dans le sujet et dans chacune des deux éditions. Les trente PDF comptent 168 pages, 332 signets de question vérifiés sur leur page et 90 insertions de schémas. [Révisions et empreintes](pdf-informatique-psi-pt-166-questions.tsv)

Pour l’informatique B MP–PC de 2011 à 2016 et l’informatique C MPI de 2023 à 2025, les 180 questions ont été rapprochées du sujet, du journal éditorial et des deux réponses. Les programmes des deux éditions ont été exécutés à nouveau. Les 18 PDF signés totalisent 140 pages et 360 signets de question contrôlés. [Informatique B](pdf-informatique-b-mp-pc-82-questions.tsv) · [Informatique C](pdf-informatique-c-mpi-98-questions.tsv)

Pour les cinq épreuves d’informatique B de 2017, 2019, 2021, 2022 et 2023, les 10 PDF signés totalisent 73 pages et 164 signets de questions vérifiés à destination. [Empreintes et arbres Git](pdf-informatique-b-mp-pc-psi-82-questions.tsv)

Pour les options d’informatique MP de 1998 et 2010, les 4 PDF signés totalisent 29 pages et 52 signets de questions vérifiés à destination. [Empreintes et arbres Git](pdf-informatique-option-mp-1998-2010.tsv)

Le 25 novembre 2026, les deux lecteurs et les quatre téléchargements ont aussi été vérifiés sur les 134 fiches de filière de 45 épreuves communes déjà en production à la révision `54fe93cd`. [Adresses et empreintes des fichiers](production-filieres-54fe93cd.tsv)

Les contrôles sur sujet-corriges.ai portent leur propre date. Le relevé en production distingue les deux lecteurs HTML, les textes Markdown téléchargeables et les PDF signés. [Contrôles des lecteurs en production](lecteurs-a-verifier-54fe93cd.tsv) · [Téléchargements vérifiés](fichiers-telechargeables.tsv) · [Téléchargements complémentaires](fichiers-complementaires-54fe93cd.tsv)
