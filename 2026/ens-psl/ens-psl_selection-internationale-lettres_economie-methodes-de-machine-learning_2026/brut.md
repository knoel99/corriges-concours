# ENS-PSL · Sélection internationale Lettres 2026 · Économie — méthodes de machine learning · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

**Rédaction** · GPT-6.2 Astra Ultra · vitesse non renseignée · 24 novembre 2026

**Révision (tour 1)** · GPT-6.2 Astra Ultra · vitesse non renseignée · 26 novembre 2026

**Couverture vérifiée.** Le rapport du jury donne page 2 l’écrit individuel du candidat 2. Son oral distinct a pour intitulé « Apports de la révolution de la crédibilité à l’évaluation des politiques publiques ». Les deux copies vérifient la différence entre prédire un résultat et identifier un effet causal. Elles explicitent la formule du modèle partiellement linéaire, l’hypothèse de recouvrement et les limites du partage d’échantillon. Le ciblage de l’aide au Togo fournit un résultat empirique dont la population et la règle de comparaison sont précisées.

**Sujet individuel écrit.** Le recours aux méthodes de machine learning améliore-t-il nécessairement la crédibilité des résultats en économie empirique ?

## Introduction

Une administration peut prédire avec précision quelles personnes resteront longtemps au chômage. Si elle propose une formation aux seules personnes ainsi repérées et observe ensuite qu’elles retrouvent moins souvent un emploi que les autres, que faut-il conclure de la formation ? Le score peut être excellent et la comparaison profondément biaisée. Les méthodes de *machine learning* apprennent dans les données une relation entre variables, souvent en minimisant une erreur de prédiction hors échantillon. La crédibilité d’un résultat empirique dépend de la proposition qu’il prétend établir. Prévoir une durée, mesurer l’effet d’une politique et décider à qui l’offrir correspondent à trois questions distinctes. L’apprentissage peut rendre chacune mieux traitable à condition de respecter son critère propre de validation.

## I. Pour une question prédictive, l’apprentissage flexible peut améliorer une preuve qui reste empirique

Si la cible est le nombre d’inscriptions mensuelles à une formation, de nombreuses variables peuvent être pertinentes. Une régression linéaire simple impose à l’effet de chacune une forme étroite. Une pénalisation peut sélectionner ou rétrécir des coefficients, un arbre peut représenter des interactions, une forêt peut réduire la variance en combinant des arbres. Mullainathan et Spiess (2017) insistent sur l’intérêt de ce savoir-faire pour des problèmes économiques qui contiennent une véritable tâche de prédiction. L’argument en faveur d’une méthode se vérifie sur des observations qu’elle n’a pas utilisées pour choisir sa spécification, face à un modèle simple et avec une métrique liée à l’usage.

Une prévision pour l’année suivante se teste en avançant dans le temps. Mélanger au hasard des lignes relatives aux mêmes individus ou employer des informations collectées après l’entrée en formation peut produire une performance illusoire. Une erreur moyenne plus faible peut encore cacher de fortes erreurs chez les jeunes sans diplôme. Examiner la calibration et les erreurs par groupe intéresse une administration qui répartit des places. La variable à prédire elle-même mérite examen. Le nombre d’inscriptions reflète la demande mais aussi les places disponibles et l’information transmise par les agents. Une prédiction fidèle à cette mesure peut reconduire une pénurie.

Un essai de comparaison des méthodes de ciblage donne du contenu à ce test. Au Togo, Aiken et ses coauteurs (2022) étudient un dispositif qui s’appuie sur des enquêtes de niveau de vie et sur les usages du téléphone mobile pour sélectionner des abonnés susceptibles de recevoir des transferts. Selon le ciblage géographique de référence, le classement appris réduit de 4 à 21 % la proportion de personnes pauvres écartées. Face à une méthode qui disposerait d’un registre social exhaustif, hypothétique dans ce contexte, cette proportion augmente de 9 à 35 %. Ces variations relatives se rapportent à des règles de sélection différentes. L’exercice évalue la capacité à atteindre les ménages visés. Il ne mesure pas de combien le transfert changerait leur niveau de vie. L’absence de téléphone ou la difficulté à s’enregistrer pose en outre une question d’accès, même si le classement des abonnés est précis.

## II. Une bonne prédiction du résultat observé ne donne pas le résultat contrefactuel

Soient $D$ l’entrée en formation et $Y(1),Y(0)$ les revenus potentiels avec ou sans formation. Chaque personne ne révèle que $Y=DY(1)+(1-D)Y(0)$. Un excellent ajustement de $E[Y\mid D,X]$ reproduit la sélection existante. Si les conseillers orientent les cas difficiles vers la formation selon un diagnostic absent de $X$, l’écart ajusté entre participants et non-participants mêle effet du programme et différences initiales.

Un exemple chiffré suffit. Un groupe fragile gagnerait 10 sans formation et reçoit la formation, qui lui rapporte 2. Un groupe favorisé gagnerait 20 sans formation et ne la reçoit pas. Les revenus observés sont 12 et 20. Un prédicteur qui connaît le statut du dossier peut prévoir ces revenus exactement, alors que l’écart brut de −8 donne même le mauvais signe. Sans personnes comparables ayant reçu les deux décisions, l’abondance de variables ne crée pas de comparaison. Ajouter des variables mesurées après le traitement, telles qu’une certification obtenue grâce au programme, peut même éliminer une partie de son effet.

![Figure 1 — Exemple hypothétique. Les revenus effectivement observés apparaissent sur une diagonale. L’effet sur le groupe fragile requiert de connaître les deux revenus de sa ligne.](figures/resultats-potentiels.svg)

La crédibilité causale vient d’un dispositif et de ses hypothèses. Une loterie de places permet d’estimer l’effet de l’offre par comparaison des groupes assignés. Une discontinuité peut identifier un effet local de part et d’autre d’un seuil si les résultats potentiels sont continus et que le seuil n’est pas manipulé. Avec des données observationnelles, une comparaison conditionnelle exige notamment que les facteurs communs pertinents soient observés et que le traitement soit possible de part et d’autre pour les valeurs de $X$ considérées. Aucun algorithme de prédiction ne démontre à lui seul ces conditions. Un échantillon plus large peut rendre un résultat biaisé plus précis.

## III. Une fois la comparaison justifiée, le machine learning peut améliorer l’estimation et l’usage du résultat

Dans le modèle partiellement linéaire $Y=\theta D+g(X)+U$, supposons $E[U\mid D,X]=0$ et assez de variation du traitement après conditionnement. Estimer d’abord $m(X)=E[D\mid X]$ et $\ell(X)=E[Y\mid X]$ permet de comparer les variations de $D-m(X)$ et de $Y-\ell(X)$. Chernozhukov et ses coauteurs (2018) combinent un score orthogonal, peu sensible au premier ordre aux petites erreurs de ces fonctions auxiliaires, avec un partage croisé de l’échantillon. Chaque observation reçoit des prédictions produites sur d’autres observations, puis les contributions sont regroupées. On limite ainsi le surajustement et les biais de régularisation qui pollueraient une substitution naïve. Obtenir une inférence valide exige néanmoins des vitesses de convergence suffisantes, un recouvrement adéquat et des erreurs-types adaptées à la dépendance des données.

Le rôle de l’identification se lit directement dans le coefficient. Posons $V=D-m(X)$. Comme $Y-\ell(X)=\theta V+U$ et $E[VU]=0$, on obtient
$$\theta=\frac{E[V(Y-\ell(X))]}{E[V^2]}.$$
Si le statut de formation est entièrement déterminé par les caractéristiques observées, $E[V^2]=0$. Même des prédictions parfaites des deux fonctions auxiliaires laisseraient le coefficient indéterminé. Lorsque la variation résiduelle est très faible, le dénominateur annonce également une estimation instable.

Dans une expérience de formation, le traitement peut être attribué aléatoirement et ses effets différer entre personnes. Un arbre cherchant les sous-groupes au bénéfice maximal peut découvrir, par chance, une différence spectaculaire. Athey et Imbens (2016) proposent de séparer la construction de la partition et l’estimation des effets dans ses feuilles. Cette estimation « honnête » a un coût en taille effective et améliore l’interprétation des intervalles. Avant d’allouer des places, il faut encore connaître le coût des traitements, la politique de comparaison et les effets d’une extension du programme. Un effet local sur l’emploi peut se réduire si tous les diplômés arrivent sur le même marché.

La reproductibilité intervient à toutes ces étapes. Rendre traçables l’origine des données, la définition des résultats, les découpages et l’ajustement des hyperparamètres permet de comprendre ce qui a réellement été testé. Pour un système en service, une réévaluation après changement de conjoncture est nécessaire. Choisir parmi des centaines de spécifications celle qui raconte l’histoire la plus convaincante, puis présenter son intervalle comme si elle était prévue à l’avance, déplace le problème de sélection au lieu de le résoudre.

## Conclusion

L’apprentissage statistique améliore certaines mesures, des prévisions et l’estimation de composantes auxiliaires difficiles. Il devient un gain de crédibilité quand la cible, le dispositif d’identification, la validation et les incertitudes sont explicités ensemble. Pour juger un résultat, la première question reste ce que les données permettent de comparer. La deuxième est de savoir avec quelle précision et pour quelle population la méthode réalise cette comparaison.

## Sources

[Rapport du jury ENS-PSL, sujet individuel écrit du candidat 2, p. 2](https://www.ens.psl.eu/sites/default/files/rapport_sil_economie_2026.pdf#page=2)

- [Mullainathan et Spiess (2017), apprentissage et économétrie appliquée](https://doi.org/10.1257/jep.31.2.87)
- [Chernozhukov et al. (2018), apprentissage doublement débiaisé](https://doi.org/10.1111/ectj.12097)
- [Athey et Imbens (2016), effets de traitement hétérogènes](https://doi.org/10.1073/pnas.1510489113)
- [Aiken et al. (2022), ciblage de l’aide au Togo](https://doi.org/10.1038/s41586-022-04484-9)
