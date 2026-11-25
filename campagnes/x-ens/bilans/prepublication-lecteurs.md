# Essai local de publication des corrigés

Le 25/11/2026 à 16 h 09 UTC, les 1689 paires signées de la révision `9da7aa08` ont fourni les deux textes attendus et leurs signatures dans le service de lecture du site. Le journal de chaque fiche renvoie au bon dossier GitHub, reprend les interventions qualifiantes et indique le caractère partiel quand il est déclaré. [Résultats par épreuve](prepublication-lecteurs.tsv) · [Version des corrigés](https://github.com/knoel99/corriges-concours/tree/9da7aa08d3d44e4e2397357b7a0e4c2e39501074) · [Version du site](https://github.com/knoel99/prepa/tree/3a94037e6d8d02588ffd7273875b59c15bc1cb9a)

Le contrôle couvre 2074 fiches de filière pour 1689 épreuves signées. Les épreuves communes sont aussi vérifiées sous chaque filière de leur notice éditoriale. [Contrôles des 385 fiches supplémentaires](prepublication-lecteurs-autres-filieres.tsv)

L’essai utilise une base SQLite temporaire et les fichiers locaux des révisions Git. La conversion du dépôt public et le plan de publication du site produisent les clés du stockage. La synchronisation charge d’abord le contenu de `54fe93cd`, puis celui de la branche de travail. Pour chaque édition, le service qui alimente le lecteur doit restituer exactement le Markdown attendu après la réécriture des chemins d’illustrations. Le contrôle vérifie aussi la présence de chaque SVG référencé. Si une édition ne référence aucun SVG, la colonne de disponibilité est positive et le classeur des épreuves indique zéro illustration pour cette édition.

Une compilation locale indépendante des 74 PDF de français et de langues MP-PC de 2011 à 2014 a produit 202 pages. Pour chacune des deux éditions, la première page porte la signature attendue et LaTeX inclut les schémas. [Pages, empreintes et révisions des 37 épreuves](pdf-francais-langues-mp-pc-2011-2014.tsv)

Pour les dix écrits d’option informatique de l’X en MP de 2000 à 2009, les 20 PDF compilés ont été recoupés avec les empreintes du convertisseur, les arbres Git des rédactions et les journaux LaTeX. Les signatures et les figures des deux éditions ont été vérifiées. Les PDF totalisent 119 pages. [Contrôles des dix écrits](pdf-option-informatique-mp-2000-2009.tsv)

Les 200 fiches MP et PC des 100 compositions de 2005 à 2008 ont également été interrogées via l’API locale du site. Pour chaque fiche, le sujet et son numéro de page, le rapport quand il existe, les documents complémentaires et la provenance affichée concordent avec le registre. [Sources par fiche](sources-fiches-mp-pc-2005-2008.tsv) · [Version du catalogue contrôlée](https://github.com/knoel99/prepa/tree/d63723b)

Les 32 fiches de filière des 16 compositions de l’X–ESPCI en 2009 et 2010 ont été contrôlées de la même manière. Le catalogue précise que l’ESPCI recrutait en PC. [Sources par fiche en 2009 et 2010](sources-fiches-x-espci-2009-2010.tsv)

Pour 40 compositions de français et de langues en MP-PC-PSI de 2015 à 2021, les 80 PDF compilés totalisent 261 pages. Le contrôle compare les arbres Git et les empreintes de conversion, relit les signatures en première page et vérifie que les schémas sont incorporés dans les deux éditions. [Détail par épreuve](pdf-francais-langues-mp-pc-psi-2015-2021.tsv)

Pour les 28 compositions de français, d’anglais et d’arabe de 2005 à 2008, les 56 PDF totalisent 152 pages. La signature et les illustrations ont été vérifiées dans chaque PDF, avec les empreintes des fichiers de rédaction et de conversion. [Contrôles des 28 compositions](pdf-francais-anglais-arabe-mp-pc-2005-2008.tsv)

Le 25 novembre 2026, les deux lecteurs et les quatre téléchargements ont aussi été vérifiés sur les 134 fiches de filière de 45 épreuves communes déjà en production à la révision `54fe93cd`. [Adresses et empreintes des fichiers](production-filieres-54fe93cd.tsv)

Les contrôles sur sujet-corriges.ai portent leur propre date. Le relevé en production distingue les deux lecteurs HTML, les textes Markdown téléchargeables et les PDF signés. [Contrôles des lecteurs en production](lecteurs-a-verifier-54fe93cd.tsv) · [Téléchargements vérifiés](fichiers-telechargeables.tsv) · [Téléchargements complémentaires](fichiers-complementaires-54fe93cd.tsv)
