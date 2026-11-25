# Essai local de publication des corrigés

Le 25/11/2026 à 15 h 22 UTC, les 1598 paires signées de la révision `1ac04eac` ont fourni les deux textes attendus et leurs signatures dans le service de lecture du site. Le journal de chaque fiche renvoie au bon dossier GitHub, reprend les interventions qualifiantes et indique le caractère partiel quand il est déclaré. [Résultats par épreuve](prepublication-lecteurs.tsv) · [Version des corrigés](https://github.com/knoel99/corriges-concours/tree/1ac04eacf26dc42377dfaa0cc1b17b9698b517fe) · [Version du site](https://github.com/knoel99/prepa/tree/a573d94d2e8b7292a4ef159e1313c2f9aafd0162)

Le contrôle couvre 1875 fiches de filière pour 1598 épreuves signées. Les épreuves communes sont aussi vérifiées sous chaque filière de leur notice éditoriale. [Contrôles des 277 fiches supplémentaires](prepublication-lecteurs-autres-filieres.tsv)

L’essai utilise une base SQLite temporaire et les fichiers locaux des révisions Git. La conversion du dépôt public et le plan de publication du site produisent les clés du stockage. La synchronisation charge d’abord le contenu de `54fe93cd`, puis celui de la branche de travail. Pour chaque édition, le service qui alimente le lecteur doit restituer exactement le Markdown attendu après la réécriture des chemins d’illustrations. Le contrôle vérifie aussi la présence de chaque SVG référencé. Si une édition ne référence aucun SVG, la colonne de disponibilité est positive et le classeur des épreuves indique zéro illustration pour cette édition.

Le 25 novembre 2026, les deux lecteurs et les quatre téléchargements ont aussi été vérifiés sur les 134 fiches de filière de 45 épreuves communes déjà en production à la révision `54fe93cd`. [Adresses et empreintes des fichiers](production-filieres-54fe93cd.tsv)

Les contrôles sur sujet-corriges.ai portent leur propre date. Le relevé en production distingue les deux lecteurs HTML, les textes Markdown téléchargeables et les PDF signés. [Contrôles des lecteurs en production](lecteurs-a-verifier-54fe93cd.tsv) · [Téléchargements vérifiés](fichiers-telechargeables.tsv) · [Téléchargements complémentaires](fichiers-complementaires-54fe93cd.tsv)
