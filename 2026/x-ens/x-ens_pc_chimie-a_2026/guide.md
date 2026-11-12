# X-ENS PC — Chimie A 2026 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

**Thème.** Le sujet, intitulé « Eau et chimie : caractériser, traiter et prévenir la pollution organique », s'articule autour de la baignabilité de la Seine puis de la synthèse totale d'un antibiotique polyénique, l'énacyloxine IIa. Il comporte deux problèmes indépendants et 59 questions, pour 4 heures sans calculatrice. Les données (potentiels, p$K_a$, table IR, table des groupes protecteurs, intervalles de constantes de couplage) occupent les quatre dernières pages : il faut les consulter systématiquement.

**Problème 1 (Q1–34), chimie générale et analytique, cinétique.**

- *Partie I (Q1–19)* : mesure de la demande chimique en oxygène (DCO) par le dichromate. On part de l'atomistique et de la structure de Lewis du dichromate, on exploite des diagrammes de distribution (spéciation chromate/hydrogénochromate/dichromate), puis on construit pas à pas la formule de la DCO à partir d'un titrage en retour par le sel de Mohr, avec témoins négatif et positif, et on l'applique à un effluent dilué.
- *Partie II (Q20–22)* : la demande biologique en oxygène (DBO), courte partie de cinétique du premier ordre.
- *Partie III (Q23–34)* : oxydation hydrothermale en eau supercritique. Diagramme de phases, puis un schéma de réactions parallèles et successives (COT → CO$_2$, COT → CO → CO$_2$) : dégénérescence de l'ordre, intégration, exploitation de droites, lois d'Arrhenius, et lecture critique de courbes.

**Problème 2 (Q35–59), chimie organique.** On construit le fragment B de l'énacyloxine IIa : couplage aldolique avec le fragment C et stéréochimie (Q35–38) ; partie Est, de l'épibromhydrine à l'aldéhyde **10** (Williamson, ouverture d'époxydes, alcynure, Lindlar, époxydation, acétonide, DDQ, IR, organomagnésien, Q39–47) ; RMN du proton de **5** (Q48–49) ; formation d'un allène et couplage pallado-catalysé allène–alcyne, dont il faut lire le cycle catalytique (Q50–56) ; fin de la synthèse (Q57–59).

**Notions du programme mobilisées.** Configuration électronique, Lewis et mésomérie, nombres d'oxydation, diagrammes de distribution, constante d'équilibre et principe de modération, demi-équations rédox et formule de Nernst, titrage en retour, cinétique formelle (ordre 1, réactions successives, Arrhenius), diagramme $(P,T)$ ; en chimie organique : énolates et aldolisation, S$_\text{N}$2, époxydes, alcynures, hydrogénation, acétals, oxydations et réductions ménagées, organomagnésiens, groupes protecteurs, RMN et IR, stéréodescripteurs, notions de catalyse organométallique.

**Difficulté et longueur.** Le problème 1 est long mais très guidé, avec beaucoup de points accessibles (Q1, Q4, Q8, Q9, Q13, Q14, Q17, Q19–22, Q27, Q28). Il demande des lectures de graphes soigneuses et des calculs sans calculatrice. Le problème 2 est plus exigeant : il faut suivre des structures sur plusieurs pages et vérifier la compatibilité des réactifs avec tous les groupes présents. Le rapport 2026 ne publie ni statistiques ni taux de réussite. Il nomme une seule difficulté, en Q9 (l'équivalence entre électrons échangés et dioxygène), et attend un raisonnement clair dans Q16, question en plusieurs étapes. En chimie organique, il insiste sur des conditions opératoires complètes (réactifs, solvant, température) et sur des mécanismes fléchés (Q35, Q45, Q47, Q58). À notre estimation, Q40–41 (stéréochimie de l'ouverture d'époxyde), Q52 (choix du groupe protecteur), Q55 (noms des étapes) et Q57 (séquence de synthèse) sont les plus discriminantes du problème 2.

**Questions abordables à ne pas laisser passer.** Q1, Q4, Q8, Q9, Q13 (équations et nombres d'oxydation), Q16–17 et Q19–22 (applications numériques directes), Q27–28 (cinétique formelle), Q37–39 (stéréochimie et Williamson), Q43, Q45, Q47 (réactifs classiques), Q48–49 (RMN).

**Gestion du temps.** Environ deux heures par problème. Les deux problèmes étant indépendants, commencer par celui où l'on se sent le plus à l'aise ; dans le problème 2, ne pas rester bloqué sur une structure : les questions de réactifs et de mécanisme restent souvent faisables même avec une structure incertaine.

*Mode d'emploi* : chercher chaque question seul, lire la première indication en cas de blocage, réessayer, puis la seconde, et seulement ensuite la solution.

## Problème 1, partie I — Mesures de la pollution organique d'une eau par une méthode chimique (Q1–19)

On construit la mesure de la DCO pas à pas : structure et degré d'oxydation du chrome, spéciation des chromates (Q1–7), puis stœchiométrie rédox, titrage en retour, témoins et exploitation numérique (Q8–19). Outils : atomistique, Lewis, diagrammes de distribution, constante d'équilibre, nombres d'oxydation, titrage.

### Question 1

> [!INDICATION]
> Remplir 1s, 2s, 2p, 3s, 3p, 4s puis 3d, sans corriger par la stabilité des demi-couches.

#### Solution

La règle de Klechkowski remplit les sous-couches par $n+\ell$ croissant, puis par $n$ croissant à $n+\ell$ égal. Pour $Z=24$ :

$$\boxed{\mathrm{Cr} : 1s^2\,2s^2\,2p^6\,3s^2\,3p^6\,4s^2\,3d^4}$$

On signale que la configuration réelle est $[\mathrm{Ar}]\,4s^1\,3d^5$ (exception liée à la sous-couche $d$ à demi remplie). La question demande toutefois l'application stricte de la règle.

> [!PIEGE]
> Ne pas « corriger » spontanément en $4s^1\,3d^5$ : la question porte sur la règle, pas sur la configuration réelle. On peut signaler l'exception en une phrase, sans en faire la réponse.

> [!JURY]
> Rapport 2026 : « Question de cours ; appliquer la règle de Klechkowski. » La réponse attendue est la configuration que donne la règle, écrite en entier.

### Question 2

> [!INDICATION]
> La formule de Lewis dessinée est-elle la seule possible ? Pensez aux formes mésomères.

> [!INDICATION]
> Comparez, pour chaque type de liaison Cr–O, l'ordre de liaison moyen une fois la charge délocalisée sur les oxygènes terminaux d'un même chrome.

#### Solution

Dans la formule de Lewis de la figure 1, chaque chrome porte trois oxygènes terminaux : deux liés par une double liaison, et un lié par une simple liaison et chargé $-$. Les deux chromes sont reliés par un oxygène pontant, lié à chacun par une simple liaison.

Cette formule n'est qu'une **forme mésomère**. Sur chaque motif CrO$_3$, on écrit trois formes équivalentes en plaçant la simple liaison et la charge $-$ successivement sur chacun des trois oxygènes terminaux. Les six liaisons Cr–O terminales sont donc équivalentes, d'ordre moyen $(2+2+1)/3=5/3$.

Les deux liaisons Cr–O vers l'oxygène pontant restent simples (ordre 1). L'oxygène pontant, déjà engagé dans deux liaisons, ne peut participer à la délocalisation sans porter une charge positive, ce qui ne donnerait que des formes très minoritaires.

Une liaison est d'autant plus courte que son ordre est élevé, d'où :

$$\boxed{\text{2 longueurs : } d(\mathrm{Cr{-}O_{terminal}}) < d(\mathrm{Cr{-}O_{pontant}})}$$

(À titre indicatif, les valeurs expérimentales sont d'environ 1,63 Å et 1,79 Å.)

> [!METHODE]
> Avant de comparer des longueurs de liaison, écrire toutes les formes mésomères équivalentes et calculer l'ordre de liaison moyen de chaque type de liaison. Une formule de Lewis unique localise artificiellement charges et doubles liaisons.

> [!PIEGE]
> Lire la formule dessinée au pied de la lettre conduit à trois longueurs distinctes. C'est l'erreur commise dans la copie IA source.

> [!JURY]
> Rapport 2026 : « Structure de Lewis attendue. » La justification passe par les formules de Lewis (formes mésomères) et l'ordre de liaison qui en découle, pas par une simple affirmation sur les longueurs.

### Question 3

> [!INDICATION]
> Charge formelle = électrons de valence − électrons non liants − nombre de liaisons.

> [!INDICATION]
> L'indication sur les nombres d'oxydation des deux chromes fixe la répartition des deux charges entre les deux motifs CrO$_3$.

#### Solution

La charge formelle d'un atome vaut (électrons de valence) − (électrons non liants) − (nombre de liaisons). L'oxygène a 6 électrons de valence. Dans la formule de la figure 1 :

- O doublement lié (4 atomes) : $6-4-2=0$ ;
- O pontant : $6-4-2=0$ ;
- O terminal simplement lié (2 atomes, un par chrome) : $6-6-1=-1$.

Chaque chrome est alors de charge formelle nulle ($6-0-6$). Le fait que les deux chromes aient le même nombre d'oxydation impose que les deux charges négatives se répartissent à raison d'**une par motif CrO$_3$**. Le total vaut bien $-2$. Compte tenu de la mésomérie (question 2), chaque oxygène terminal porte en moyenne une charge de $-1/3$ ; l'oxygène pontant reste neutre.

> [!METHODE]
> Toujours vérifier que la somme des charges formelles redonne la charge globale de l'ion.

> [!JURY]
> Rapport 2026 : « Calcul des charges formelles et délocalisation. » Le jury attend le calcul atome par atome, puis la conséquence de la mésomérie sur la répartition de la charge.

### Question 4

> [!INDICATION]
> Fixer O à −II et H à +I, puis écrire la conservation de la charge pour chaque espèce.

#### Solution

Avec $\mathrm{n.o.}(\mathrm{O})=-\mathrm{II}$ et $\mathrm{n.o.}(\mathrm{H})=+\mathrm{I}$ :

- $\mathrm{CrO_4^{2-}}$ : $x+4(-2)=-2$, donc $x=+6$ ;
- $\mathrm{HCrO_4^{-}}$ : $1+x+4(-2)=-1$, donc $x=+6$ ;
- $\mathrm{Cr_2O_7^{2-}}$ : $2x+7(-2)=-2$, donc $x=+6$.

$$\boxed{\text{Le chrome est au degré }+\mathrm{VI}\text{ dans les trois espèces}}$$

Les échanges entre elles sont donc des réactions acido-basiques ou de condensation, et non des oxydoréductions.

### Question 5

> [!INDICATION]
> Traduire « majoritaire » par un rapport de concentrations ≥ 10, et relier ce rapport au p$K_a$ apparent lu sur la figure.

> [!INDICATION]
> Vérifier sur les deux figures, et ne pas oublier le dimère.

#### Solution

$\mathrm{CrO_4^{2-}}$ est majoritaire s'il est au moins dix fois plus concentré que $\mathrm{HCrO_4^-}$ et que $\mathrm{Cr_2O_7^{2-}}$.

Ordre de grandeur : le croisement des courbes de $\mathrm{CrO_4^{2-}}$ et de $\mathrm{HCrO_4^-}$ donne un p$K_a$ apparent voisin de 6. Le rapport des concentrations vaut

$$\frac{[\mathrm{CrO_4^{2-}}]}{[\mathrm{HCrO_4^-}]}=10^{\,\mathrm{pH}-\mathrm{p}K_a},$$

et il atteint 10 pour pH ≈ p$K_a$ + 1 ≈ 7.

Lecture quantitative des deux figures à pH 7 (concentrations en mmol/L) :

| Figure | $[\mathrm{CrO_4^{2-}}]$ | $[\mathrm{HCrO_4^-}]$ | $[\mathrm{Cr_2O_7^{2-}}]$ | Rapport chromate / hydrogénochromate |
|---|---|---|---|---|
| 2A (8 mmol/L) | ≈ 7,3 | ≈ 0,6 | ≈ 0 | ≈ 12 |
| 2B (40 mmol/L) | ≈ 35 | ≈ 3 | ≈ 1 | ≈ 12 |

Le dimère est alors au moins trente fois moins concentré que le chromate. À pH 6,5, le rapport chromate / hydrogénochromate ne vaut encore qu'environ 3 : le critère n'est pas rempli.

$$\boxed{\mathrm{CrO_4^{2-}}\text{ majoritaire pour pH} \gtrsim 7}$$

> [!PIEGE]
> Lire le pH au croisement des courbes ne suffit pas : au croisement, les deux espèces sont en quantités égales. Le critère « dix fois plus » décale le seuil d'une unité de pH.

> [!JURY]
> Rapport 2026 : « La lecture quantitative du diagramme de distribution était attendue. » Il faut donner les concentrations lues et le rapport obtenu, et non un pH seul.

### Question 6

> [!INDICATION]
> Équilibrer la condensation avec de l'eau ; le chrome reste au degré +VI.

> [!INDICATION]
> Pour $K^\circ$, lire deux concentrations à pH 3 et contrôler par le bilan de chrome. Pour l'entropie, compter les solutés.

#### Solution

Condensation :

$$\boxed{2\,\mathrm{HCrO_4^-}\;=\;\mathrm{Cr_2O_7^{2-}}+\mathrm{H_2O}}$$

Quotient de réaction : l'eau, solvant, a une activité égale à 1 et n'y figure pas ; les solutés sont supposés idéaux.

$$Q=\frac{[\mathrm{Cr_2O_7^{2-}}]\,c^\circ}{[\mathrm{HCrO_4^-}]^2}$$

À l'équilibre, $Q=K^\circ$. La constante est « apparente » parce qu'elle est estimée avec des concentrations lues sur la figure, dans le milieu de la mesure, et non avec des activités.

Sur la figure 2B à pH 3 : $[\mathrm{HCrO_4^-}]\approx10$ mmol/L et $[\mathrm{Cr_2O_7^{2-}}]\approx15$ mmol/L (bilan en chrome : $10+2\times15=40$ ✓). D'où

$$\boxed{K^\circ\approx\frac{1{,}5\times10^{-2}}{(1{,}0\times10^{-2})^2}\approx1{,}5\times10^{2}}$$

Contrôle sur la figure 2A ($\approx3{,}8$ et $\approx2{,}2$ mmol/L) : $K^\circ\approx1{,}5\times10^2$.

Signe de $\Delta_rS^\circ$ : la réaction remplace deux particules de soluté par une seule, car la molécule d'eau formée se confond avec le solvant. De plus, l'ion dichromate, doublement chargé, ordonne fortement l'eau qui l'entoure. Le désordre diminue :

$$\boxed{\Delta_rS^\circ<0}$$

> [!METHODE]
> Pour une constante lue sur un diagramme de distribution, choisir un pH où les deux espèces concernées sont bien mesurables et contrôler la lecture par la conservation de la matière (ici du chrome).

> [!PIEGE]
> L'eau, solvant, n'apparaît pas dans la constante d'équilibre. Le terme $c^\circ$ est indispensable pour que $K^\circ$ soit sans dimension.

> [!JURY]
> Rapport 2026 : « Quotient réactionnel et signe de l’entropie devaient être justifiés. » On écrit le quotient (eau exclue, avec $c^\circ$) et l'on argumente le signe par le nombre de particules de soluté.

### Question 7

> [!INDICATION]
> Écrire la conservation du chrome et la loi d'action de masse : quelle est la dépendance du dimère en fonction du monomère ?

#### Solution

À pH ≤ 3, $\mathrm{CrO_4^{2-}}$ est négligeable. La conservation du chrome et la loi d'action de masse donnent :

$$\begin{aligned}
C_{\text{tot}}&=[\mathrm{HCrO_4^-}]+2\,[\mathrm{Cr_2O_7^{2-}}]\\
[\mathrm{Cr_2O_7^{2-}}]&=\frac{K^\circ\,[\mathrm{HCrO_4^-}]^2}{c^\circ}
\end{aligned}$$

Principe de modération : partons d'un état d'équilibre et multiplions toutes les concentrations par $\lambda>1$ (solution plus concentrée). Le quotient de réaction devient

$$Q=\frac{\lambda\,[\mathrm{Cr_2O_7^{2-}}]\,c^\circ}{\lambda^2\,[\mathrm{HCrO_4^-}]^2}=\frac{K^\circ}{\lambda}<K^\circ.$$

Le système évolue donc dans le sens direct, celui de la condensation, qui diminue le nombre de particules de soluté : il modère la hausse de concentration. Quand $C_{\text{tot}}$ augmente, $[\mathrm{Cr_2O_7^{2-}}]$ augmente, et sa part relative aussi.

Vérification : de 2A à 2B ($C_{\text{tot}}\times5$), $[\mathrm{HCrO_4^-}]$ passe de ≈ 4 à ≈ 10 mmol/L (facteur 2,5) et $[\mathrm{Cr_2O_7^{2-}}]$ de ≈ 2 à ≈ 15 mmol/L (facteur ≈ 7). La fraction du chrome sous forme de dimère passe de ≈ 50 % à ≈ 75 %.

![Figure 1 — Part du chrome sous forme Cr₂O₇²⁻ et HCrO₄⁻ à pH ≤ 3 en fonction de Ctot, calculée avec K° = 1,5·10² : environ 50 % (figure 2A), 75 % (figure 2B), 82 % dans les tubes de la DCO](figures/q07-q11-dimerisation-chrome.svg)

$$\boxed{[\mathrm{Cr_2O_7^{2-}}]\text{ croît plus vite que }C_{\text{tot}}\text{ : la dimérisation est favorisée par la concentration}}$$

> [!METHODE]
> Un équilibre de dimérisation est d'ordre 2 en monomère : le dimère est favorisé aux fortes concentrations, défavorisé par dilution. C'est le même raisonnement que pour la dissociation d'un électrolyte faible.

> [!JURY]
> Rapport 2026 : « Utilisation du principe de modération. » La comparaison du quotient de réaction à $K^\circ$ après la perturbation en est la forme rigoureuse.

### Question 8

> [!INDICATION]
> Chrome de +VI à +III, deux chromes : combien d'électrons ? Équilibrer O par H$_2$O et les charges par H$^+$.

#### Solution

$$\boxed{\mathrm{Cr_2O_7^{2-}}+14\,\mathrm{H^+}+6\,e^-=2\,\mathrm{Cr^{3+}}+7\,\mathrm{H_2O}}$$

### Question 9

> [!INDICATION]
> Comparer les électrons échangés par une mole de dichromate et par une mole de dioxygène.

#### Solution

Une mole de $\mathrm{K_2Cr_2O_7}$ capte 6 mol d'électrons (question 8) : elle représente 6 équivalents. Le dioxygène capte 4 électrons par molécule :

$$\mathrm{O_2}+4\,\mathrm{H^+}+4\,e^-=2\,\mathrm{H_2O}$$

L'équivalent-gramme du dioxygène vaut donc $32/4=8$ g. Une mole de dichromate correspond à $6\times8=48$ g de dioxygène, soit $1{,}5$ mol de $\mathrm{O_2}$ :

$$\boxed{1\text{ mol de }\mathrm{K_2Cr_2O_7}\equiv48\,000\text{ mg de }\mathrm{O_2}}$$

> [!METHODE]
> La DCO est une conversion « électrons échangés → masse de O$_2$ » : on raisonne toujours sur le nombre d'électrons, quel que soit l'oxydant réellement utilisé.

> [!JURY]
> Rapport 2026 : « La difficulté tenait à l’équivalence entre électrons échangés et dioxygène. » C'est la seule difficulté que le jury nomme dans la partie I : 6 électrons par dichromate, 4 par dioxygène.

### Question 10

> [!INDICATION]
> Le dichromate est introduit en excès : que titre-t-on réellement ?

> [!INDICATION]
> Quel est le rôle du témoin négatif dans le calcul de la quantité consommée ?

#### Solution

C'est un **titrage en retour**. On introduit une quantité connue et excédentaire de dichromate. Après deux heures à reflux en milieu sulfurique concentré, catalysé par Ag$^+$ (HgSO$_4$ complexe les chlorures, qui seraient sinon oxydés), la matière organique est oxydée en CO$_2$ et consomme une partie du dichromate. On titre l'excès restant par Fe$^{2+}$. La différence avec le témoin négatif (dichromate initial) donne le dichromate consommé, donc le nombre d'électrons cédés par la matière organique. On le convertit en masse de O$_2$ équivalente (question 9).

> [!METHODE]
> Titrage en retour : réactif en excès connu, réaction avec l'analyte, puis dosage de l'excès. Le témoin donne la quantité initiale effectivement disponible.

> [!JURY]
> Rapport 2026 : « Il fallait reconnaître un dosage en retour. » Nommer la méthode d'abord, puis la décrire.

### Question 11

> [!INDICATION]
> Calculer la concentration en chrome de la solution introduite et la comparer à la figure 2B.

> [!INDICATION]
> La condensation fait-elle intervenir H$^+$ ? Et, pour un dosage rédox, la forme du chrome +VI importe-t-elle ?

#### Solution

La solution introduite contient $C_t=42$ mmol/L de $\mathrm{K_2Cr_2O_7}$, soit 84 mmol/L de chrome, plus que dans la figure 2B. Elle est acide, puis très fortement acidifiée dans le tube par $\mathrm{H_2SO_4}$ : $\mathrm{CrO_4^{2-}}$ est absent.

D'après la question 7, la part du dimère augmente avec la concentration. Avec $K^\circ\approx150$, on résout $C_{\text{tot}}=h+2K^\circ h^2/c^\circ$ pour $h=[\mathrm{HCrO_4^-}]$. On trouve environ 82 % du chrome sous forme $\mathrm{Cr_2O_7^{2-}}$ et 18 % sous forme $\mathrm{HCrO_4^-}$, soit un rapport des concentrations voisin de 2,3. Le pH n'y change rien, car la condensation ne fait pas intervenir H$^+$.

Une fois les 5 mL de solution dilués dans les 30 mL du tube, le chrome total tombe à 14 mmol/L et la part du dimère à environ 60 % : l'écart à « tout dimère » s'accroît encore.

Au sens strict (critère « 10 fois »), le dimère n'est donc pas la seule forme. L'approximation est pourtant **pertinente pour la DCO** : $\mathrm{HCrO_4^-}$ et $\mathrm{Cr_2O_7^{2-}}$ contiennent du chrome +VI (question 4), réduit en Cr$^{3+}$ avec 3 électrons par atome de chrome dans les deux cas. Le pouvoir oxydant de la solution ne dépend que de la quantité totale de chrome, et compter « $C_t$ en $\mathrm{Cr_2O_7^{2-}}$ » donne le bon nombre d'électrons.

> [!PIEGE]
> Invoquer le pH pour déplacer la dimérisation : l'équation $2\,\mathrm{HCrO_4^-}=\mathrm{Cr_2O_7^{2-}}+\mathrm{H_2O}$ ne contient pas H$^+$. Le pH ne joue que sur l'équilibre avec $\mathrm{CrO_4^{2-}}$.

### Question 12

> [!INDICATION]
> Compter les électrons cédés par l'hydrogénophtalate oxydé en CO$_2$ via le nombre d'oxydation moyen du carbone.

> [!INDICATION]
> Convertir ces électrons en moles de O$_2$ (4 électrons par O$_2$).

#### Solution

L'hydrogénophtalate $\mathrm{C_8H_5O_4^-}$ est oxydé en CO$_2$. Le nombre d'oxydation moyen $x$ du carbone vérifie :

$$\begin{aligned}
8x+5\times(+1)+4\times(-2)&=-1\\
x&=+\tfrac14
\end{aligned}$$

Chaque carbone, porté au degré +IV dans CO$_2$, cède $4-\tfrac14=\tfrac{15}{4}$ électrons. La molécule en cède $8\times\tfrac{15}{4}=30$. Cela équivaut à $30/4=7{,}5$ mol de O$_2$ par mole :

$$2\,\mathrm{C_8H_5O_4^-}+15\,\mathrm{O_2}\rightarrow16\,\mathrm{CO_2}+4\,\mathrm{H_2O}+2\,\mathrm{HO^-}.$$

$$\begin{aligned}
\mathrm{DCO_{th}}&=7{,}5\,C_h\,M(\mathrm{O_2})\\
&=7{,}5\times2{,}1\times10^{-3}\times32\\
&=0{,}504\ \mathrm{g\,L^{-1}}
\end{aligned}$$

$$\boxed{\mathrm{DCO_{th}}\approx5{,}0\times10^{2}\ \mathrm{mg\,L^{-1}}\text{ de }\mathrm{O_2}}$$

> [!METHODE]
> Pour une oxydation totale en CO$_2$, le nombre d'électrons cédés se calcule directement par le nombre d'oxydation moyen du carbone : $n_e=n_C\,(4-\bar x)$.

### Question 13

> [!INDICATION]
> Combiner la demi-équation de Q8 avec six fois le couple Fe$^{3+}$/Fe$^{2+}$.

#### Solution

$$\boxed{\mathrm{Cr_2O_7^{2-}}+6\,\mathrm{Fe^{2+}}+14\,\mathrm{H^+}\rightarrow2\,\mathrm{Cr^{3+}}+6\,\mathrm{Fe^{3+}}+7\,\mathrm{H_2O}}$$

> [!JURY]
> Rapport 2026 : « Equation de titrage en milieu acide. » On équilibre avec H$^+$ et H$_2$O, jamais avec HO$^-$, et l'on vérifie charges et éléments.

### Question 14

> [!INDICATION]
> Égalité des potentiels à l'équilibre ; $\log K = n\Delta E^\circ/0{,}06$.

> [!INDICATION]
> Utiliser les couleurs données en fin d'énoncé pour l'indicateur.

#### Solution

À l'équilibre, les potentiels des deux couples sont égaux. Pour 6 électrons échangés :

$$\begin{aligned}
\log K^\circ&=\frac{6\,(E^\circ_{\mathrm{Cr_2O_7^{2-}/Cr^{3+}}}-E^\circ_{\mathrm{Fe^{3+}/Fe^{2+}}})}{0{,}06}\\
&=\frac{6\times(1{,}33-0{,}77)}{0{,}06}\\
&=56
\end{aligned}$$

$$\boxed{K^\circ=10^{56}\gg10^4\text{ : réaction totale}}$$

Repérage de l'équivalence : l'indicateur est le complexe fer–orthophénanthroline (ferroïne). Avant l'équivalence, le dichromate est en excès et tout le fer est à l'état +III : le complexe est bleu pâle (sur fond vert dû à Cr$^{3+}$). Dès la première goutte de Fe$^{2+}$ en excès, le complexe ferreux se forme et la solution vire au **rouge sang**. Le virage marque l'équivalence.

> [!PIEGE]
> Oublier le nombre d'électrons échangés dans $\log K^\circ=n\,\Delta E^\circ/0{,}06$. Avec $n=1$, on trouverait $10^{9{,}3}$, conclusion identique mais calcul faux.

### Question 15

> [!INDICATION]
> Que contient le témoin, et que mesure donc $V_0$ ? Qu'est-ce qui affecte de la même façon le témoin et l'essai ?

#### Solution

Le témoin négatif est l'**essai à blanc** : de l'eau distillée qui subit exactement le même traitement que les échantillons, mais ne contient pas de matière organique. Son volume équivalent $V_0$ mesure le dichromate réellement disponible dans un tube après chauffage. Il sert de référence pour calculer le dichromate consommé ($V_0-V_m$), et il corrige les consommations parasites (impuretés oxydables des réactifs ou de l'eau, éventuelle évolution du dichromate au reflux).

> [!JURY]
> Rapport 2026 : « Le rôle de l’essai à blanc devait être identifié. » Dire ce qu'il mesure ($V_0$) et ce qu'il corrige.

### Question 16

> [!INDICATION]
> Quantité de dichromate consommée = (Fe$^{2+}$ du témoin − Fe$^{2+}$ de l'essai)/6.

> [!INDICATION]
> Convertir en masse de O$_2$ (Q9) puis diviser par le volume de prise d'essai, attention aux mL.

#### Solution

Étape 1, dichromate consommé. Le témoin indique par $V_0$ le dichromate disponible sans matière organique, l'essai indique par $V_m$ le dichromate restant. La différence $V_0-V_m$ (en mL) correspond donc au Fe$^{2+}$ que le dichromate consommé aurait oxydé.

Étape 2, stœchiométrie. D'après l'équation de titrage (Q13), 6 Fe$^{2+}$ réagissent avec 1 Cr$_2$O$_7^{2-}$ :

$$n_{\text{cons}}=\frac{C_{\text{Mohr}}(V_0-V_m)\times10^{-3}}{6}\ \text{mol}$$

Étape 3, masse de O$_2$ équivalente (Q9) :

$$\begin{aligned}
m_{\mathrm{O_2}}&=48\,000\,n_{\text{cons}}\ \text{mg}\\
&=8\,C_{\text{Mohr}}(V_0-V_m)\ \text{mg}
\end{aligned}$$

Étape 4, on rapporte au volume de la prise d'essai, $V_{\text{sol}}\times10^{-3}$ L :

$$\boxed{\mathrm{DCO}=8\,000\,C_{\text{Mohr}}\,\frac{V_0-V_m}{V_{\text{sol}}}\ \ (\mathrm{mg\,L^{-1}})}$$

> [!PIEGE]
> Les volumes sont en mL et la DCO en mg/L : les puissances de dix se compensent partiellement. Faire une analyse dimensionnelle avant l'application numérique.

> [!JURY]
> Rapport 2026 : « Question en plusieurs étapes : un raisonnement clair était attendu. » Annoncer chaque étape : différence de volumes, stœchiométrie, masse de O$_2$, rapport au volume.

### Question 17

> [!INDICATION]
> Appliquer la formule de Q16 avec $V_m=12{,}2$ mL et comparer à Q12.

#### Solution

$$\begin{aligned}
\mathrm{DCO}(S_{\text{pos}})&=8\,000\times0{,}05\times\frac{24{,}5-12{,}2}{10}\\
&=492\ \mathrm{mg\,L^{-1}}
\end{aligned}$$

Comparaison quantitative avec la DCO théorique de la question 12 :

$$\frac{\mathrm{DCO_{mes}}}{\mathrm{DCO_{th}}}=\frac{492}{504}\approx0{,}976$$

Avec la valeur arrondie de 500 mg/L, le rapport vaut 0,984.

$$\boxed{\text{DCO mesurée} \approx 98\,\%\text{ de la DCO théorique} \geq 95\,\%\text{ : l'expérience est validée}}$$

> [!METHODE]
> Un témoin positif de composition connue valide toute la chaîne de mesure (réactifs, chauffage, titrage). On compare le résultat au critère d'acceptation fixé par la norme.

> [!JURY]
> Rapport 2026 : « Comparaison quantitative attendue. » Donner le rapport chiffré à la valeur théorique et le confronter au seuil de 95 %.

### Question 18

> [!INDICATION]
> Pour $S_0$, que signifie un volume équivalent presque nul ? Pour $S_3$, comparer $V_0-V_m$ à la précision d'une burette.

#### Solution

- $S_0$ (non diluée) : $V_{\text{eq}}=0{,}2$ mL, donc presque tout le dichromate a été consommé. Il n'était plus en excès et la matière organique n'a peut-être pas été entièrement oxydée. On ne lit qu'une borne inférieure de la DCO ($8\,000\times0{,}05\times24{,}3/10=972$ mg/L, sous-estimée).
- $S_3$ (dilution 50) : $V_0-V_m=0{,}2$ mL, de l'ordre de l'incertitude de lecture de la burette (environ 0,05 à 0,1 mL). L'incertitude relative est énorme, amplifiée par le facteur 50 (on trouverait 400 mg/L).

Pour un échantillon inconnu, la DCO n'est pas connue a priori. Une gamme de dilutions garantit qu'au moins une mesure tombe dans le domaine exploitable : dichromate encore en excès, mais consommation nettement mesurable. Les dilutions extrêmes encadrent le résultat.

> [!METHODE]
> Une mesure par différence n'est exploitable que si la différence est grande devant l'incertitude de lecture, et si le réactif titré reste en excès. D'où le choix d'une gamme de dilutions.

### Question 19

> [!INDICATION]
> N'exploiter que les dilutions fiables et multiplier par le facteur de dilution.

#### Solution

On multiplie la DCO de chaque dilution par son facteur de dilution :

- $S_1$ (×2) : $400\times(24{,}5-11{,}8)/10=508$ mg/L, soit $1\,016$ mg/L ;
- $S_2$ (×10) : $400\times(24{,}5-22{,}0)/10=100$ mg/L, soit $1\,000$ mg/L.

$$\boxed{\mathrm{DCO}\approx1{,}0\times10^{3}\ \mathrm{mg\,L^{-1}}\text{ de }\mathrm{O_2}}$$

## Problème 1, partie II — Suivi biologique par autoépuration (Q20–22)

Courte partie de cinétique du premier ordre : exploiter un témoin et un facteur de dilution, intégrer une équation différentielle linéaire, utiliser $k_T\times5=1$.

### Question 20

> [!INDICATION]
> Retrancher la consommation du témoin, puis tenir compte de la dilution des eaux usées dans le flacon.

#### Solution

Consommation dans le témoin : $9-8=1$ mg/L (respiration propre des bactéries). Consommation dans l'essai : $9-2=7$ mg/L. La consommation due aux eaux usées vaut $7-1=6$ mg/L dans le flacon de 300 mL, qui en contient 10 mL (dilution 30) :

$$\boxed{\mathrm{DBO_5}=(7-1)\times\frac{300}{10}=1{,}8\times10^{2}\ \mathrm{mg\,L^{-1}}}$$

(En ne retranchant la consommation du témoin que pour les 290 mL d'eau distillée, on obtient 181 mg/L, identique à deux chiffres.)

> [!PIEGE]
> Oublier le témoin : la respiration endogène des micro-organismes consomme aussi du dioxygène. Oublier la dilution conduit à une DBO trente fois trop faible.

> [!JURY]
> Rapport 2026 : « Le bilan en dioxygène devait intégrer le témoin et la dilution. »

### Question 21

> [!INDICATION]
> Changer de variable $y=[\mathrm{O_2}]-[\mathrm{O_2}]_\infty$ : l'équation devient du premier ordre homogène.

> [!INDICATION]
> La DBO est le dioxygène consommé depuis l'instant initial.

#### Solution

En posant $y=[\mathrm{O_2}]-[\mathrm{O_2}]_\infty$, l'équation devient $\mathrm{d}y/\mathrm{d}t=-k_T\ln(10)\,y$. Elle s'intègre en :

$$\begin{aligned}
y(t)&=y_0\,e^{-k_T\ln(10)\,t}\\
&=y_0\,10^{-k_Tt}
\end{aligned}$$

D'où, avec $y_0=[\mathrm{O_2}]_0-[\mathrm{O_2}]_\infty$ :

$$\boxed{[\mathrm{O_2}](t)=[\mathrm{O_2}]_\infty+\big([\mathrm{O_2}]_0-[\mathrm{O_2}]_\infty\big)\,10^{-k_Tt}}$$

$$\boxed{\mathrm{DBO}_t=[\mathrm{O_2}]_0-[\mathrm{O_2}](t)=\big([\mathrm{O_2}]_0-[\mathrm{O_2}]_\infty\big)\big(1-10^{-k_Tt}\big)}$$

Limites asymptotiques :

- à $t=0$ : $[\mathrm{O_2}]=[\mathrm{O_2}]_0$ et $\mathrm{DBO}_0=0$ ;
- quand $t\to\infty$ : $[\mathrm{O_2}]\to[\mathrm{O_2}]_\infty$ et $\mathrm{DBO}_t\to\mathrm{DBO}_\infty$.

Le palier vaut $\mathrm{DBO}_\infty=[\mathrm{O_2}]_0-[\mathrm{O_2}]_\infty$.

Représentations (figure 2) : $[\mathrm{O_2}]$ décroît exponentiellement vers l'asymptote horizontale $[\mathrm{O_2}]_\infty$. $\mathrm{DBO}_t$ croît de 0 vers le palier $\mathrm{DBO}_\infty$. Les deux courbes sont symétriques, puisque $[\mathrm{O_2}]+\mathrm{DBO}_t=[\mathrm{O_2}]_0$.

La tangente à l'origine coupe l'asymptote en $\tau=1/(k_T\ln10)\approx2{,}2$ jours, temps caractéristique. À $t=5$ jours, $10^{-k_Tt}=0{,}1$ : 90 % du palier est atteint.

![Figure 2 — Cinétique d'ordre 1 (kT = 0,2 j⁻¹) : la concentration en O₂ décroît vers son asymptote, DBOt croît vers DBO∞ ; la tangente à l'origine coupe l'asymptote en τ ≈ 2,2 j, et DBO₅ = 0,9 DBO∞](figures/q21-cinetique-dbo.svg)

> [!METHODE]
> Une équation $\mathrm{d}y/\mathrm{d}t=-k(y-y_\infty)$ se résout en posant $u=y-y_\infty$. Ici le facteur $\ln 10$ vient de l'écriture en base 10.

> [!JURY]
> Rapport 2026 : « L’intégration du modèle cinétique et ses limites asymptotiques étaient attendues. » Les valeurs à $t=0$ et quand $t\to\infty$ doivent figurer sur les courbes.

### Question 22

> [!INDICATION]
> Que vaut $10^{-k_T\times5}$ avec $k_T=0{,}2$ j$^{-1}$ ?

#### Solution

$$\begin{aligned}
\mathrm{DBO}_5&=\mathrm{DBO}_\infty\,(1-10^{-0{,}2\times5})\\
&=0{,}9\,\mathrm{DBO}_\infty
\end{aligned}$$

$$\boxed{\mathrm{DBO}_\infty=\frac{180}{0{,}9}=2{,}0\times10^{2}\ \mathrm{mg\,L^{-1}}}$$

## Problème 1, partie III — Oxydation hydrothermale en conditions supercritiques (Q23–34)

Diagramme de phases, puis cinétique de réactions parallèles et successives (dégénérescence d'ordre, intégration, exploitation graphique, Arrhenius) et lecture critique de courbes modèle/expérience.

### Question 23

> [!INDICATION]
> Trois domaines, trois courbes, deux points remarquables ; une particularité de pente pour l'eau.

#### Solution

![Figure 3 — Diagramme (P, T) de l'eau, non à l'échelle : fusion de pente négative, vaporisation arrêtée au point critique C, zone supercritique T > Tc et P > Pc hachurée](figures/q23-diagramme-phases-eau.svg)

- Trois courbes concourantes au **point triple** $T$ (0,01 °C ; 6 mbar) : la sublimation (solide/vapeur), la vaporisation (liquide/vapeur), qui s'arrête au **point critique** $C$ (374 °C ; 221 bar), et la fusion (solide/liquide), de pente **négative** pour l'eau.
- Le domaine supercritique, à hachurer, est la région $T>T_c$ et $P>P_c$.

> [!PIEGE]
> Pour l'eau, la courbe de fusion a une pente négative (la glace est moins dense que le liquide). Un diagramme « générique » à pente positive est faux pour l'eau.

> [!JURY]
> Rapport 2026 : « Le diagramme devait comporter domaines, courbes et points remarquables (point triple, point critique). »

### Question 24

> [!INDICATION]
> Quel est le nombre d'oxydation maximal du carbone ?

#### Solution

Dans CO$_2$, le carbone est au degré d'oxydation +IV, le maximum possible pour un élément à 4 électrons de valence : CO$_2$ ne peut plus être oxydé. C'est en outre une molécule très stable (deux liaisons C=O fortes, enthalpie de formation très négative). La minéralisation de la matière organique s'arrête donc à CO$_2$ (et H$_2$O).

> [!PIEGE]
> Dire que CO$_2$ « s'échappe » : dans l'eau supercritique, les gaz sont totalement miscibles au fluide. L'argument doit être thermodynamique (degré d'oxydation maximal, grande stabilité).

### Question 25

> [!INDICATION]
> Quelle concentration reste quasi constante au cours de la réaction ?

#### Solution

Chaque étape a une vitesse de la forme $v_i=k_i\,[\mathrm{org}]^a[\mathrm{O_2}]^b$.

Au-delà du point critique, l'eau, la matière organique et le dioxygène forment une **seule phase homogène** (énoncé : ils sont « complètement miscibles »). Il n'y a plus de transfert gaz–liquide limitant : la concentration en dioxygène dissous est fixée par la quantité introduite. Le dioxygène étant en outre en large excès, sa concentration reste pratiquement constante au cours de l'oxydation.

On l'intègre dans une constante apparente $k'_i=k_i[\mathrm{O_2}]_0^b$ : c'est la **dégénérescence de l'ordre**. Les $k'_i$ dépendent alors de la quantité de O$_2$ introduite.

> [!METHODE]
> Dégénérescence de l'ordre : un réactif en large excès voit sa concentration rester quasi constante. On l'absorbe dans une constante apparente, qui dépend donc des conditions initiales.

> [!PIEGE]
> S'en tenir à « le dioxygène est en excès » : l'énoncé insiste sur la miscibilité totale en milieu supercritique, qui supprime toute limitation par le transfert gaz–liquide.

> [!JURY]
> Rapport 2026 : « Concentration en dioxygène dissous constante (condition supercritique). »

### Question 26

> [!INDICATION]
> Regarder les données spectroscopiques fournies en fin d'énoncé.

#### Solution

La **spectroscopie infrarouge** convient : d'après les données, CO absorbe à 2 140 cm$^{-1}$ et CO$_2$ à 2 350 cm$^{-1}$. Ces bandes sont bien séparées et l'absorbance est proportionnelle à la concentration (loi de Beer-Lambert, après étalonnage). On peut suivre l'effluent par prélèvements, ou en ligne avec une cellule adaptée. La chromatographie en phase gazeuse sur des prélèvements détendus est une alternative.

> [!JURY]
> Rapport 2026 : « Spectroscopie infrarouge. » C'est la technique attendue ; citer les nombres d'onde des données justifie qu'elle distingue CO et CO$_2$.

### Question 27

> [!INDICATION]
> Écrire la vitesse de chaque acte (ordre 1 apparent), puis faire le bilan apparition − disparition pour chaque espèce.

#### Solution

Les trois actes sont d'ordre 1 apparent, de vitesses $k'_1C_{\mathrm{COT}}$, $k'_2C_{\mathrm{COT}}$ et $k'_3C_{\mathrm{CO}}$. Le bilan apparition moins disparition de chaque espèce donne :

$$\boxed{\begin{aligned}
\frac{\mathrm{d}C_{\mathrm{COT}}}{\mathrm{d}t}&=-(k'_1+k'_2)\,C_{\mathrm{COT}}\\
\frac{\mathrm{d}C_{\mathrm{CO}}}{\mathrm{d}t}&=k'_2\,C_{\mathrm{COT}}-k'_3\,C_{\mathrm{CO}}\\
\frac{\mathrm{d}C_{\mathrm{CO_2}}}{\mathrm{d}t}&=k'_1\,C_{\mathrm{COT}}+k'_3\,C_{\mathrm{CO}}
\end{aligned}}$$

### Question 28

> [!INDICATION]
> La première équation s'intègre directement ; reporter dans la deuxième.

> [!INDICATION]
> Équation linéaire à second membre exponentiel : solution particulière de même forme exponentielle, puis condition initiale $C_{\mathrm{CO}}(0)=0$.

#### Solution

La première équation s'intègre en $C_{\mathrm{COT}}=C_{\mathrm{COT},0}\,e^{-(k'_1+k'_2)t}$. On reporte dans la deuxième :

$$\frac{\mathrm{d}C_{\mathrm{CO}}}{\mathrm{d}t}+k'_3C_{\mathrm{CO}}=k'_2C_{\mathrm{COT},0}\,e^{-(k'_1+k'_2)t}.$$

Une solution particulière s'écrit $\mu\,e^{-(k'_1+k'_2)t}$. En la reportant, on obtient $\mu\,(k'_3-k'_1-k'_2)=k'_2C_{\mathrm{COT},0}$.

La solution générale vaut $C_{\mathrm{CO}}=\lambda e^{-k'_3t}+\mu e^{-(k'_1+k'_2)t}$. La condition $C_{\mathrm{CO}}(0)=0$ impose $\lambda=-\mu$, d'où :

$$\boxed{C_{\mathrm{CO}}=\frac{k'_2C_{\mathrm{COT},0}}{k'_1+k'_2-k'_3}\left(e^{-k'_3t}-e^{-(k'_1+k'_2)t}\right)}\qquad(k'_1+k'_2\neq k'_3)$$

> [!METHODE]
> Réactions successives $A\to B\to C$ : la solution est une différence de deux exponentielles. Vérifier $C_{\mathrm{CO}}(0)=0$ et le signe positif pour tout $t>0$, quel que soit l'ordre des constantes.

### Question 29

> [!INDICATION]
> Que représente la pente de $\ln(C/C_0)$ en fonction de $t$ ?

> [!INDICATION]
> La droite passe-t-elle par l'origine ? Combien de points la déterminent ?

#### Solution

D'après Q28, $\ln(C_{\mathrm{COT}}/C_{\mathrm{COT},0})=-(k'_1+k'_2)t$. La pente de la figure 4 donne seulement la somme :

$$\boxed{k'_1+k'_2\approx0{,}15\ \mathrm{s^{-1}}\ \text{à }450\ \text{°C}}$$

Les constantes $k'_1$ et $k'_2$ ne sont pas accessibles séparément par le seul suivi du COT. L'ordonnée à l'origine ($-0{,}11$ au lieu de 0) montre que le modèle n'est pas suivi aux temps courts (mise en température et en pression, temps mort, incertitude sur $C_{\mathrm{COT},0}$). Pour fiabiliser l'estimation : ajouter des points (en particulier entre 0 et 6 s), élargir l'intervalle de temps, répéter les mesures et évaluer l'incertitude sur la pente. Il ne faut pas se contenter de 4 points.

> [!PIEGE]
> Forcer la droite à passer par l'origine pour « corriger » l'ordonnée $-0{,}11$ : on masque alors un écart réel au modèle au lieu de le discuter.

### Question 30

> [!INDICATION]
> Comment rendre l'étape 3 seule responsable de l'évolution de CO ?

#### Solution

On étudie l'étape 3 isolément : on réalise l'oxydation hydrothermale à 450 °C, dans les mêmes conditions (même excès de O$_2$, même pression), d'une solution contenant **du monoxyde de carbone seul**, sans matière organique. Alors $C_{\mathrm{CO}}=C_{\mathrm{CO},0}\,e^{-k'_3t}$. On suit CO par IR, à 2 140 cm⁻¹. La pente de $\ln(C_{\mathrm{CO}}/C_{\mathrm{CO},0})$ en fonction du temps vaut $-k'_3$.

### Question 31

> [!INDICATION]
> Trois inconnues : il faut trois informations indépendantes. Penser aux pentes initiales de CO et CO$_2$.

#### Solution

- La figure 4 donne $S=k'_1+k'_2$.
- L'expérience de Q30 donne $k'_3$.
- Dans l'expérience complète, le suivi de CO (ou de CO$_2$) donne $k'_2$. On peut ajuster la loi de Q28, où $k'_2$ est la seule inconnue, ou utiliser les pentes initiales : $(\mathrm{d}C_{\mathrm{CO}}/\mathrm{d}t)_0=k'_2C_{\mathrm{COT},0}$ et $(\mathrm{d}C_{\mathrm{CO_2}}/\mathrm{d}t)_0=k'_1C_{\mathrm{COT},0}$.
- On en déduit $k'_1=S-k'_2$.

> [!METHODE]
> Pentes initiales : à $t=0$, seuls les actes qui consomment le réactif de départ contribuent. Elles permettent de séparer des constantes de réactions parallèles.

### Question 32

> [!INDICATION]
> La pente vaut $-E_a/(1000R)$ puisque l'abscisse est $1000/T$.

> [!INDICATION]
> Pour attribuer les droites aux étapes 1 et 2, comparer les vitesses initiales de formation de CO et de CO$_2$ sur la figure 6.

#### Solution

Loi d'Arrhenius, avec $k$ en s⁻¹ et $T$ en kelvins : $\ln k=\ln A-\dfrac{E_a}{R}\dfrac1T$.

L'abscisse de la figure 5 est $x=1000/T$, en K$^{-1}$. La pente vaut donc $-E_a/(1000\,R)$ et s'exprime en milliers de kelvins.

- Droite supérieure (points pleins), $y=-11{,}10\,x+13{,}05$ : $E_a=11{,}10\times10^3\times8{,}314\ \mathrm{J\,mol^{-1}}$, soit 92 kJ/mol.
- Droite inférieure (points creux), $y=-10{,}31\,x+11{,}23$ : $E_a\approx86$ kJ/mol.

Attribution : à 450 °C, soit 723 K, $x=1{,}383$. Les deux droites donnent alors 0,100 et 0,048 s$^{-1}$, de somme 0,148 s$^{-1}$, en accord avec la figure 4.

Sur la figure 6, CO se forme initialement plus vite que CO$_2$. Les pentes initiales valent $k'_2C_0$ et $k'_1C_0$, donc $k'_2>k'_1$ : la droite supérieure est celle de l'étape 2.

$$\boxed{\begin{aligned}
E_{a2}&\approx92\ \mathrm{kJ\,mol^{-1}}\\
E_{a1}&\approx86\ \mathrm{kJ\,mol^{-1}}
\end{aligned}}$$

Commentaire : les deux valeurs sont proches et modérées, typiques d'actes chimiques radicalaires (bien au-dessus d'un contrôle par la diffusion, de quelques kJ/mol). Le rapport $k'_2/k'_1$ varie donc peu avec $T$. L'ajustement de la série creuse est moins bon ($r^2=0{,}964$), et son estimation est moins fiable.

> [!METHODE]
> Avec une abscisse $1000/T$, la pente vaut $-E_a/(1000R)$ : ne pas oublier le facteur 1000. On vérifie la cohérence avec une valeur déjà connue (ici, la somme à 450 °C).

> [!JURY]
> Rapport 2026 : « Arrhénius : attention aux unités. » Facteur 1000 de l'abscisse, $T$ en kelvins, $R$ en J·K⁻¹·mol⁻¹, résultat en kJ·mol⁻¹.

### Question 33

> [!INDICATION]
> Si les trois $E_a$ étaient égales, comment les courbes se transformeraient-elles avec $T$ ?

> [!INDICATION]
> Suivre l'évolution du maximum de CO et de sa disparition entre 400 et 500 °C.

#### Solution

Si les trois étapes avaient la même énergie d'activation, élever $T$ multiplierait les trois constantes par le même facteur : les courbes se déduiraient les unes des autres par une simple contraction de l'axe des temps, et la hauteur du maximum de CO resterait la même. Or, sur la figure 6, à 400 °C et 425 °C, CO s'accumule sans maximum net sur 20 s (≈ 0,35–0,4 à 20 s). Dès 450 °C, CO passe par un maximum de plus en plus précoce et de plus en plus bas relativement au COT consommé, et il a presque disparu à 20 s à 500 °C, où CO$_2$ tend vers 1. Le rapport $k'_3/(k'_1+k'_2)$ augmente donc avec $T$, ce qui impose :

$$\boxed{E_{a3}>E_{a1}\ \text{et}\ E_{a3}>E_{a2}}$$

L'oxydation de CO est l'étape limitante de la minéralisation à basse température.

> [!METHODE]
> Une constante d'Arrhenius plus « sensible » à la température est celle de plus grande énergie d'activation. Comparer des rapports de constantes, et non les constantes elles-mêmes.

### Question 34

> [!INDICATION]
> Traduire « complète » par un seuil (par exemple 99 %) et utiliser $k'_1+k'_2$ en fonction de $T$, ou lire la figure 6.

> [!INDICATION]
> Comparer l'ordre de grandeur des durées avec celui de la DBO.

#### Solution

Avec les lois d'Arrhenius de Q32, on calcule $k'_1+k'_2$, puis la fraction de COT restant à 20 s, $e^{-20\,(k'_1+k'_2)}$ :

| $T$ (°C) | 400 | 425 | 450 | 475 | 500 |
|---|---|---|---|---|---|
| $k'_1+k'_2$ (s$^{-1}$) | 0,049 | 0,087 | 0,148 | 0,25 | 0,39 |
| COT restant à 20 s | 0,38 | 0,18 | 0,05 | 0,007 | 0,000 4 |

C'est bien ce que montre la figure 6. Une disparition à 99 % en 20 s exige

$$k'_1+k'_2\geq\frac{\ln 100}{20}\approx0{,}23\ \mathrm{s^{-1}},$$

valeur atteinte vers 470–475 °C. Pour une minéralisation complète (CO lui aussi oxydé, CO$_2$ ≈ 1 à 20 s), la figure 6 indique plutôt 500 °C.

$$\boxed{T\approx475\text{–}500\ \text{°C}}$$

Conclusion : l'oxydation hydrothermale détruit la matière organique en quelques secondes, contre plusieurs jours pour l'autoépuration biologique (DBO), soit un gain d'un facteur de l'ordre de $10^4$. Elle traite aussi la fraction non biodégradable ($\mathrm{DCO}/\mathrm{DBO_5}\approx5{,}5$ ici). Le prix à payer est élevé : plus de 221 bar et environ 500 °C, d'où un coût énergétique important et des matériaux résistant à la corrosion. Le procédé est réservé aux effluents industriels concentrés ou réfractaires.

> [!PIEGE]
> Confondre la disparition du COT et la minéralisation complète : le CO intermédiaire n'est pas encore du CO$_2$.

## Problème 2, partie A — Assemblage des fragments B et C, stéréochimie (Q35–38)

Aldolisation croisée dirigée, mécanisme, dénombrement de stéréoisomères et descripteurs CIP.

### Question 35

> [!INDICATION]
> Identifier les fonctions en C15–C16 (fragment B) et en C17 (fragment C).

> [!INDICATION]
> Réaction de formation de liaison C–C entre un énolate et un aldéhyde : quelles conditions la rendent dirigée ?

#### Solution

Le fragment B se termine par une méthylcétone $\mathrm{C_{15}(=O){-}C_{16}H_3}$, et le fragment C commence par l'aldéhyde $\mathrm{C_{17}HO}$. La liaison $\mathrm{C_{16}{-}C_{17}}$ se forme par **aldolisation croisée dirigée** :

1. LDA (1 équivalent), THF anhydre, −78 °C, sous argon : formation quantitative de l'énolate cinétique de la méthylcétone. La déprotonation a lieu sur le CH$_3$, le côté le moins encombré, l'autre position α étant le CH du dioxolane.
2. Addition lente de l'aldéhyde (fragment C) à −78 °C.
3. Hydrolyse douce par NH$_4$Cl aqueux saturé.

Précautions :
- milieu anhydre et atmosphère inerte (base et énolate sont détruits par l'eau) ;
- déprotonation complète de la cétone avant l'introduction de l'aldéhyde, pour éviter l'autocondensation ;
- basse température pour éviter la crotonisation de l'aldol, la rétro-aldolisation et surtout l'épimérisation de l'α-chloroaldéhyde (H en C18 acide) ou l'élimination de HCl ;
- compatibilité avec les protections : d'après la table, l'éther TBS résiste au LDA ; il n'est coupé qu'en milieu acide (pH ≤ 2), basique (pH > 12) ou par TBAF. L'acétonide, un acétal, est stable en milieu basique. On proscrit donc tout traitement acide, qui ouvrirait l'acétonide et couperait le TBS, et toute base aqueuse forte, qui couperait le TBS et saponifierait l'ester. D'où l'hydrolyse par NH$_4$Cl, faiblement acide ;
- éviter tout excès de LDA, qui pourrait déprotoner d'autres positions (méthyle allylique du polyène) ; le LDA, encombré, n'attaque pas l'ester éthylique à −78 °C ;
- le nouveau centre C17 n'est pas contrôlé par cette méthode, et un mélange de diastéréoisomères est possible.

> [!METHODE]
> Aldolisation croisée dirigée : on forme quantitativement l'énolate d'un seul partenaire (base forte encombrée, basse température), puis on ajoute l'électrophile.

> [!PIEGE]
> Utiliser une base faible en milieu protique (soude, éthanol) : on obtient un mélange d'autocondensations et de crotonisations.

> [!PIEGE]
> Terminer par une hydrolyse acide « classique » (HCl dilué) : elle ouvrirait l'acétonide et, à pH ≤ 2, couperait l'éther TBS.

> [!JURY]
> Rapport 2026 : « La formation de la liaison C–C devait rester compatible avec les protections. » Chaque réactif, y compris celui de l'hydrolyse, se justifie face au TBS, à l'acétonide et à l'ester.

### Question 36

> [!INDICATION]
> Trois étapes : déprotonation, addition nucléophile, hydrolyse. Écrire les formes mésomères de l'énolate.

#### Solution

On note $\mathrm{R^B{-}CO{-}CH_3}$ le fragment B et $\mathrm{R^C{-}CHO}$ le fragment C.

1. Déprotonation : le doublet de l'azote de $i\mathrm{Pr_2N^-}$ arrache un H du méthyle. Le doublet C–H forme la double liaison C=C et le doublet π du C=O passe sur l'oxygène. On obtient l'énolate $\mathrm{R^B{-}C(O^-){=}CH_2}\leftrightarrow\mathrm{R^B{-}C(=O){-}CH_2^-}$ (+ $i\mathrm{Pr_2NH}$).
2. Addition nucléophile : le doublet π C=C de l'énolate attaque le carbone de l'aldéhyde, et le doublet π C=O de l'aldéhyde passe sur son oxygène. Il se forme la liaison $\mathrm{C_{16}{-}C_{17}}$ et l'alcoolate $\mathrm{R^B{-}CO{-}CH_2{-}CH(O^-){-}R^C}$ (Li$^+$).
3. Hydrolyse : l'alcoolate est protoné par NH$_4^+$, ce qui donne la β-hydroxycétone $\mathrm{R^B{-}CO{-}CH_2{-}CH(OH){-}R^C}$.

> [!JURY]
> Rapport 2026, appréciations globales : « Un mécanisme doit faire apparaître les flèches courbes représentant les déplacements de doublets d’électrons, ainsi que les charges et les doublets non liants utiles. » Écrire les deux formes de l'énolate et faire partir chaque flèche d'un doublet.

### Question 37

> [!INDICATION]
> Compter les carbones asymétriques et les doubles liaisons stéréogènes, puis vérifier l'absence de symétrie.

#### Solution

Le fragment C s'écrit $\mathrm{OHC{-}CHCl{-}CH(OTBS){-}CH{=}CH{-}CH_2{-}CH_3}$ (C17 à C23). Il comporte deux carbones asymétriques (C18 et C19) et une double liaison C20=C21 stéréogène (chaque carbone porte H et un groupe différent). Il n'a aucun élément de symétrie.

$$\boxed{2^3=8\text{ stéréoisomères de configuration}}$$

> [!PIEGE]
> Oublier la double liaison C20=C21 dans le décompte : elle est stéréogène et double le nombre de stéréoisomères.

### Question 38

> [!INDICATION]
> Classer les substituants par CIP (duplication du C=O de l'aldéhyde, rôle du Cl).

> [!INDICATION]
> Repérer la position de H (avant ou arrière) à partir des liaisons hachurée et grasse.

#### Solution

Règles CIP : on classe les atomes directement liés au centre par numéro atomique décroissant. En cas d'égalité, on compare les ensembles des atomes du rang suivant, une double liaison étant dupliquée.

- **C18** : $\mathrm{Cl}>\mathrm{C_{17}}\,(\mathrm{O,O,H})>\mathrm{C_{19}}\,(\mathrm{O,C,H})>\mathrm{H}$. Sur la figure 7, C18 est un sommet haut du zigzag : Cl est vers le haut en liaison hachurée, donc H pointe vers l'observateur. Le sens Cl → C17 (en bas à gauche) → C19 (en bas à droite) est antihoraire, et on l'inverse puisque H est à l'avant : **R**.
- **C19** : $\mathrm{OTBS}>\mathrm{C_{18}}\,(\mathrm{Cl,C,H})>\mathrm{C_{20}}\,(\mathrm{C,C,H})>\mathrm{H}$. OTBS est vers le bas en liaison grasse, donc H est à l'arrière. Le sens O → C18 (en haut à gauche) → C20 (en haut à droite) est horaire : **R**.

$$\boxed{\text{C18 : }R,\qquad\text{C19 : }R\qquad(\text{double liaison C20=C21 }E)}$$

> [!METHODE]
> Quand H est vers l'observateur, on lit le sens de rotation des trois autres substituants et on l'inverse.

> [!PIEGE]
> Pour classer C17 (aldéhyde), dupliquer l'oxygène de la double liaison : (O, O, H) l'emporte sur (O, C, H).

> [!JURY]
> Rapport 2026 : « L’attribution R/S devait être justifiée par les règles CIP. » Écrire le classement des quatre substituants et la position du dernier avant de conclure.

## Problème 2, partie B — Synthèse de la partie Est du fragment B (Q39–47)

Williamson et ouverture d'époxydes (chimio- et stéréosélectivité), alcynures, hydrogénation de Lindlar, époxydation, acétonide, exploitation d'une formule brute et d'un spectre IR, organomagnésiens.

### Question 39

> [!INDICATION]
> Rôle de NaH, puis nature de la substitution sur C–Br.

#### Solution

**1** est l'épibromhydrine énantiopure. Il y a deux étapes.

1. Déprotonation de l'alcool par l'ion hydrure : $\mathrm{PMB{-}OH}+\mathrm{H^-}\rightarrow\mathrm{PMB{-}O^-}+\mathrm{H_2}\uparrow$. Elle est totale (p$K_a$ 35 contre ~16) et irréversible (dégagement gazeux).
2. S$_\text{N}$2 : un doublet de l'alcoolate attaque le carbone du $\mathrm{CH_2Br}$ en anti de la liaison C–Br, et Br$^-$ part. On obtient **2**, $\mathrm{PMBO{-}CH_2}$-oxirane, en conservant le centre stéréogène, qui n'est pas touché.

> [!METHODE]
> Synthèse de Williamson : alcoolate (formé par une base dont l'acide conjugué est bien plus faible) + halogénure primaire, en S$_\text{N}$2.

### Question 40

> [!INDICATION]
> **1** possède un autre site électrophile. Suivre l'alcoolate formé après une attaque sur ce site.

> [!INDICATION]
> Comparer les substituants du centre stéréogène dans le produit obtenu et dans **2**.

#### Solution

L'alcoolate peut aussi attaquer le $\mathrm{CH_2}$ du cycle époxyde, le carbone le moins encombré. On obtient l'alcoolate $\mathrm{PMBO{-}CH_2{-}CH(O^-){-}CH_2Br}$, qui se referme par S$_\text{N}$2 intramoléculaire sur le $\mathrm{CH_2Br}$. Le nouvel époxyde a la même constitution que **2**, mais le centre stéréogène a vu ses substituants échanger leurs rôles : l'ancien $\mathrm{CH_2}$ du cycle porte maintenant l'OPMB, et l'ancien $\mathrm{CH_2Br}$ est dans le cycle.

$$\boxed{\text{produit secondaire : l'énantiomère de }\mathbf{2}}$$

(On peut aussi citer le 1,3-bis(PMBO)propan-2-ol, issu d'une seconde ouverture par PMBO$^-$.)

> [!METHODE]
> Pour suivre un centre stéréogène dans une séquence ouverture–refermeture, nommer chaque substituant de l'atome et regarder lequel joue quel rôle à la fin.

### Question 41

> [!INDICATION]
> Comparer les groupes partants et l'encombrement des deux sites électrophiles.

> [!INDICATION]
> Quelle voie conserve la configuration du centre stéréogène ?

#### Solution

**2** est très majoritaire parce que la substitution directe sur le $\mathrm{CH_2Br}$ est nettement plus rapide que l'ouverture de l'époxyde :
- le carbone est primaire, exocyclique et peu encombré ;
- Br$^-$ est un excellent nucléofuge (base faible, polarisable), alors que l'ouverture de l'époxyde non activé (milieu basique, sans acide de Lewis) libère un alcoolate, mauvais nucléofuge, malgré la tension du cycle.

La voie directe conserve la configuration du centre stéréogène, et l'excès énantiomérique de **1** se retrouve dans **2**. L'autre voie, minoritaire, conduit à *ent*-**2** et abaisse l'excès énantiomérique.

> [!PIEGE]
> Affirmer que les deux voies « convergent vers **2** » : l'une conduit à l'énantiomère. C'est l'erreur de la copie IA source.

### Question 42

> [!INDICATION]
> Comparer les p$K_a$ donnés ; quel est le rôle du TMS ?

> [!INDICATION]
> Où l'alcynure attaque-t-il l'époxyde ? À quoi sert le lavage acide, et jusqu'où peut-on acidifier ?

#### Solution

1. $n$-HxLi déprotone le triméthylsilylacétylène : p$K_a$ ≈ 25 contre 40 pour l'hexane, réaction totale. Le sous-produit est l'hexane, liquide et inerte ($n$-HxLi est moins dangereux que $n$-BuLi, qui libère du butane gazeux). Le groupe TMS bloque l'autre extrémité de l'alcyne : il empêche une seconde déprotonation et un double couplage.
2. L'alcynure de lithium, nucléophile, ouvre l'époxyde de **2** par S$_\text{N}$2 sur le carbone le moins substitué ($\mathrm{CH_2}$). Le centre stéréogène n'est pas touché, et sa configuration est conservée.
3. Le milieu doit être anhydre et aprotique (THF, sous atmosphère inerte, à basse température). On peut activer l'époxyde par un acide de Lewis (BF$_3$·OEt$_2$).
4. Le lavage par $\mathrm{H_2O}$/H$^+$ protone l'alcoolate pour libérer l'alcool **3**. Il doit rester doux, car le PMB n'est stable que pour pH > 1.

> [!JURY]
> Le rapport 2025 précise que la justification de l'emploi d'un solvant ou d'une molécule ne peut se faire sans représentation chimique. Écrire l'équation de déprotonation et la structure de l'alcynure.

### Question 43

> [!INDICATION]
> Alcyne → alcène Z : quelle hydrogénation s'arrête à l'alcène, et avec quelle stéréochimie ?

> [!INDICATION]
> Vérifier dans la table que le PMB supporte les conditions choisies.

#### Solution

Hydrogénation partielle syn de l'alcyne en alcène Z :

$$\boxed{\mathrm{H_2}\ (1\ \text{bar, 1 équiv.}),\ \text{catalyseur de Lindlar (Pd/CaCO}_3\text{ désactivé par Pb, quinoléine), AcOEt ou MeOH, 25 °C}}$$

D'après la table, l'éther PMB ne craint pas $\mathrm{H_2}$/Pd.

> [!PIEGE]
> H$_2$ et Pd/C sans désactivation conduirait à l'alcane, et la réduction par Na/NH$_3$ à l'alcène $E$.

### Question 44

> [!INDICATION]
> Quel réactif électrophile transforme une double liaison C=C en cycle à trois chaînons ?

> [!INDICATION]
> L'addition est stéréospécifique : que devient la relation cis de l'alcène $Z$ ?

#### Solution

Le m-CPBA époxyde la double liaison C=C. **6** est $\mathrm{CH_3{-}CH{-}CH{-}CH(OH){-}CH_2{-}OPMB}$, où les deux CH centraux appartiennent à un cycle époxyde (oxirane), dont les deux substituants $\mathrm{CH_3}$ et $\mathrm{CH(OH)CH_2OPMB}$ sont en cis.

> [!METHODE]
> L'époxydation par un peracide est stéréospécifique syn : la relation cis/trans des substituants de l'alcène se retrouve dans l'époxyde.

### Question 45

> [!INDICATION]
> Un diol vicinal + une cétone ou son acétal, en catalyse acide : quel groupe protecteur cyclique obtient-on ?

> [!INDICATION]
> Mécanisme : passer par un ion oxocarbénium, deux fois. La réaction est équilibrée : comment la déplacer ?

#### Solution

**7** → **8** : protection du diol vicinal en acétonide.

$$\boxed{\text{2,2-diméthoxypropane (ou acétone), APTS en quantité catalytique, CH}_2\text{Cl}_2\text{ ou acétone anhydre, 25 °C}}$$

On élimine le méthanol ou l'eau formés (tamis moléculaire), car la réaction est équilibrée. La catalyse acide reste douce : le PMB est stable à pH > 1.

Mécanisme (catalyse acide, étapes toutes renversables), écrit avec le 2,2-diméthoxypropane :
1. Activation : un doublet non liant d'un oxygène méthoxy capte H$^+$. Le méthanol part avec le doublet de la liaison C–O, et un doublet non liant de l'autre méthoxy forme la double liaison C=O$^+$. On obtient l'ion oxocarbénium $\mathrm{(CH_3)_2C{=}O^+{-}CH_3}$, stabilisé par mésomérie.
2. Addition nucléophile : un doublet non liant d'un OH du diol attaque le carbone de l'oxocarbénium, et le doublet π revient sur l'oxygène. La perte de H$^+$ donne un acétal mixte.
3. Protonation du second méthoxy et départ de MeOH : nouvel oxocarbénium, porté cette fois par l'oxygène du diol.
4. Attaque intramoléculaire du second OH (cycle à 5 chaînons, favorisé), puis perte de H$^+$ : on obtient l'acétonide **8**, et l'acide catalyseur est régénéré.

Avec l'acétone, la séquence est la même : protonation du C=O, addition d'un OH, prototropie, départ d'eau qui donne l'oxocarbénium, cyclisation, déprotonation. On élimine alors l'eau formée.

> [!METHODE]
> Protection d'un 1,2-diol en acétonide : 2,2-diméthoxypropane, catalyse acide, élimination du méthanol. On la retire en milieu acide aqueux.

> [!JURY]
> Rapport 2026 : « Catalyse acide, conditions opératoires, et mécanisme d’acétalisation étaient attendus. » Les trois éléments sont notés : nommer l'acide, donner solvant et température, écrire le mécanisme fléché.

### Question 46

> [!INDICATION]
> Que fait le DDQ sur un éther PMB ? Que fait le DMP sur un alcool primaire ?

> [!INDICATION]
> Comparer les formules brutes de **9** et **10**, puis exploiter les deux informations IR (bande intense et absence de bande au-delà de 3 000 cm$^{-1}$).

#### Solution

Premier temps, DDQ dans $\mathrm{CH_2Cl_2}$/H$_2$O tamponné à pH 7,4 : déprotection sélective de l'éther PMB. Elle libère l'alcool primaire $\mathrm{{-}CH_2OH}$, de formule $\mathrm{C_{13}H_{21}ClO_3}$.

Second temps, DMP/NaHCO$_3$ : oxydation ménagée de l'alcool primaire en aldéhyde.

Contrôle par la formule : **10** = $\mathrm{C_{13}H_{19}ClO_3}$, soit l'alcool moins 2 H. Contrôle par l'IR : une bande intense à 1 690 cm$^{-1}$ correspond au C=O d'aldéhyde (plage 1 650–1 730 cm$^{-1}$). L'absence de bande au-dessus de 3 000 cm$^{-1}$ signifie qu'il n'y a ni O–H (oxydation complète de l'alcool) ni H aromatique (groupe PMB bien éliminé).

$$\boxed{\mathbf{10} : \mathrm{CH_2{=}CH{-}CH_2{-}CH{=}C(Cl){-}CH(CH_3){-}}\text{[dioxolane 2,2-diméthyle]}\mathrm{{-}CHO}}$$

C'est **9** où $\mathrm{CH_2OPMB}$ est remplacé par CHO, sur le carbone du cycle acétonide, avec les mêmes stéréocentres. L'aldéhyde n'est pas conjugué.

> [!JURY]
> Le rapport 2025 signale que l'analyse du spectre IR a souvent été incomplète. Il faut exploiter la bande présente et l'absence de bande : chacune élimine une hypothèse.

> [!PIEGE]
> Une bande à 1 690 cm$^{-1}$ n'implique pas une conjugaison : rester dans les plages données par l'énoncé et vérifier la structure.

### Question 47

> [!INDICATION]
> Ajouter un carbone sur un aldéhyde pour former un alcool secondaire : quel nucléophile carboné ?

> [!INDICATION]
> Quelle fonction de la molécule interdit une hydrolyse franchement acide ?

#### Solution

Addition d'un organomagnésien méthylé sur l'aldéhyde.

Préparation de l'organomagnésien, juste avant l'emploi : on ajoute goutte à goutte l'iodométhane (ou le bromométhane, en solution) sur des copeaux de magnésium, dans l'éther diéthylique ou le THF **anhydres**. La verrerie est séchée à l'étuve et le montage (ampoule de coulée, réfrigérant, garde à CaCl$_2$) est placé sous argon. Un cristal de diiode amorce la réaction, exothermique, que l'on entretient à reflux doux. L'eau, le dioxygène et le dioxyde de carbone détruisent l'organomagnésien : on les exclut tout au long.

Addition sur **10** puis hydrolyse :

$$\boxed{\begin{aligned}
&1)\ \mathrm{CH_3MgI}\ \text{ou}\ \mathrm{CH_3MgBr},\ \text{Et}_2\text{O ou THF anhydre, sous argon},\ -78\to0\ \text{°C}\\
&2)\ \mathrm{NH_4Cl}\ \text{aq.}
\end{aligned}}$$

L'acétonide et le chlorure vinylique ne réagissent pas avec l'organomagnésien, et **10** ne porte plus aucun H acide.

L'hydrolyse doit rester douce, car l'acétonide est un acétal sensible aux acides. Le nouveau centre est obtenu en mélange d'épimères (liaison ondulée de **11**), sans conséquence puisqu'il sera ensuite oxydé en cétone.

> [!PIEGE]
> Un organomagnésien est aussi une base : il n'est compatible ici que parce qu'il ne reste aucun H acide (OH libre) dans **10**.

> [!JURY]
> Rapport 2026 : « Conditions opératoires pour la préparation d’un organométallique. » Le jury attend la préparation elle-même (halogénure, magnésium, solvant anhydre, atmosphère inerte), pas seulement le nom du réactif.

## Problème 2, partie C — RMN du proton de la molécule 5 (Q48–49)

Constantes de couplage (vicinal, allylique, cis/trans) et attribution complète d'un spectre.

### Question 48

> [!INDICATION]
> Identifier H2 et H3 par leurs couplages avec le méthyle ($^3J$ ou $^4J$).

> [!INDICATION]
> Comparer la constante commune aux deux signaux aux intervalles cis et trans de la table.

#### Solution

**5** : $\mathrm{C^1H_3{-}C^2H{=}C^3H{-}C^4H(OH){-}C^5H_2{-}O{-}C^6H_2{-}Ar}$.
- Signal $c$ (5,65 ppm) : doublet ($J=11{,}0$ Hz) de quadruplets ($J=7{,}0$ Hz). Le couplage $^3J=7$ Hz avec les 3 H du méthyle voisin désigne **H2**.
- Signal $d$ (5,37 ppm) : doublet ($J=11{,}0$ Hz) de quadruplets ($J=1{,}8$ Hz). Le petit couplage allylique $^4J$ avec le méthyle à travers la double liaison désigne **H3**.

La constante commune $J=11{,}0$ Hz est le couplage $^3J$ entre H2 et H3. Elle tombe dans l'intervalle cis (6–11 Hz) et hors de l'intervalle trans (12–17 Hz) :

$$\boxed{\text{H2 et H3 sont cis : alcène }Z}$$

> [!METHODE]
> Une constante de couplage commune à deux signaux identifie les deux protons couplés. La valeur de $^3J$ entre protons vinyliques distingue cis et trans.

### Question 49

> [!INDICATION]
> Numéroter la molécule, puis classer les protons par environnement (aromatiques, vinyliques, O–CH, O–CH$_2$, OCH$_3$, OH, CH$_3$).

> [!INDICATION]
> Vérifier l'intégration totale par la formule brute.

#### Solution

| Signal | δ (ppm) | Intégration | Multiplicité | Attribution |
|---|---|---|---|---|
| a | 7,30–7,25 | 2 H | m | H8 et H12 (aromatiques, côté CH$_2$) |
| b | 6,91–6,86 | 2 H | m | H9 et H11 (aromatiques en ortho de OCH$_3$, blindés par l'effet donneur) |
| c | 5,65 | 1 H | m (dq) | H2 |
| d | 5,37 | 1 H | m (dq) | H3 |
| e | 4,69 | 1 H | m | H4 (CH–OH, allylique) |
| f | 4,52 | 2 H | s | H6 (O–CH$_2$–Ar, sans voisin) |
| g | 3,81 | 3 H | s | H13 (Ar–O–CH$_3$) |
| h, i | 3,44 ; 3,35 | 1 H + 1 H | m | H5 (diastéréotopes, donnés) |
| j | 2,61 | 1 H | s large | O–H (échangeable) |
| k | 1,68 | 3 H | m (dd) | H1 (CH$_3$ vinylique, $^3J=7{,}0$ et $^4J=1{,}8$ Hz) |

Total : 18 H, conforme à C$_{13}$H$_{18}$O$_3$.

> [!JURY]
> Rapport 2026 : « Analyse RMN : merci de garder les mêmes notations que l’énoncé. » Désigner les signaux par les lettres a à k et les protons par les numéros 1 à 13 de la figure 10. Le rapport 2025 demandait déjà un tableau (déplacement, intégration, multiplicité) et la vérification de l'intégration totale.

## Problème 2, partie D — Allène et couplage pallado-catalysé (Q50–56)

Sélectivité de l'époxydation, réduction, choix raisonné d'un groupe protecteur, lecture d'un cycle catalytique (bilan, carbocations, noms des étapes, stéréosélectivité).

### Question 50

> [!INDICATION]
> Le m-CPBA est un électrophile : quelle double liaison est la plus riche en électrons et la plus accessible ?

> [!INDICATION]
> Quel est l'effet électronique d'un chlore porté par la double liaison ?

#### Solution

La partie Est porte une double liaison terminale monosubstituée $\mathrm{CH_2{=}CH{-}}$ et une double liaison trisubstituée portant un chlore. Le m-CPBA est un électrophile, qui réagit d'autant plus vite que la double liaison est riche en électrons (HO haute). L'effet inductif attracteur du chlore appauvrit la double liaison chlorée, qui est en outre plus encombrée.

$$\boxed{\text{C'est la double liaison terminale qui est époxydée}}$$

L'époxyde terminal est ensuite ouvert par l'alcynure de TMS, comme pour **2** → **3**, ce qui donne **12**.

> [!METHODE]
> Chimiosélectivité d'une époxydation : la double liaison la plus substituée par des donneurs et la moins appauvrie par des attracteurs réagit la première, à encombrement comparable.

### Question 51

> [!INDICATION]
> Cétone → alcool secondaire, en présence d'un allène, d'un acétonide et d'un TBS : quel hydrure doux ?

> [!INDICATION]
> Le carbone réduit garde-t-il son caractère stéréogène jusqu'à la fin de la synthèse ?

#### Solution

Réduction 1,2 de la cétone conjuguée à l'allène en alcool secondaire :

$$\boxed{\mathrm{NaBH_4}\ (\text{+ CeCl}_3\text{ pour garantir l'addition 1,2}),\ \mathrm{MeOH},\ 0\ \text{°C, puis hydrolyse douce}}$$

Les conditions sont neutres et compatibles avec l'acétonide, le TBS, le chlorure vinylique et l'allène. Le cérium (conditions de Luche) dépasse le programme. NaBH$_4$ seul à basse température convient en première approche. La configuration du carbinol formé importe peu, car ce carbone devient trigonal lors de la déshydratation **17** → **18**. Un réducteur chiral (type CBS) permettrait néanmoins de la contrôler.

> [!PIEGE]
> Proposer LiAlH$_4$ sans précaution : réducteur plus fort, moins sélectif. Signaler explicitement tout réactif hors programme (CeCl$_3$, CBS).

### Question 52

> [!INDICATION]
> Faire la liste de toutes les conditions que P doit traverser jusqu'à **17**, y compris celles que vous proposerez en Q57.

> [!INDICATION]
> P doit aussi s'ôter sans toucher au TBS : parcourir la table ligne par ligne. Quel groupe a disparu de la molécule au passage **9** → **10** ?

#### Solution

Le groupe P doit résister au couplage de la figure 12 (Pd(OAc)$_2$, phosphine, CuCl, NEt$_3$, THF, 40 °C) et aux étapes de la question 57 (hydrure d'aluminium, réactifs basiques). Il doit aussi pouvoir être ôté sélectivement en présence de l'éther TBS de l'autre alcool. D'après la table :
- Ac et CHO sont coupés par les organométalliques, les hydrures et les bases fortes ;
- TMS est trop labile (acide pH ≤ 6, base, TBAF) ;
- Bn s'ôte par H$_2$/Pd/C, ce qui hydrogénerait aussi les insaturations.

$$\boxed{P=\mathrm{PMB}\ :\ \mathrm{PMBCl,\ NaH,\ THF,\ 20\ °C,\ 12\ h}}$$

Le PMB est stable aux bases, aux organométalliques et aux conditions de couplage. Le DDQ (CH$_2$Cl$_2$/H$_2$O tamponné à pH 7) le coupe sélectivement, sans toucher au TBS, qui ne réagit pas au DDQ. Réciproquement, le TBS s'ôte au TBAF sans toucher au PMB.

> [!METHODE]
> Choisir un groupe protecteur, c'est vérifier une matrice : chaque étape à venir × chaque groupe candidat, plus l'orthogonalité avec les autres protections présentes.

> [!PIEGE]
> Choisir l'acétate parce qu'il « se pose et s'ôte facilement » : il ne résiste ni aux hydrures ni aux organolithiens, utilisés ensuite. C'est l'erreur de la copie IA source.

### Question 53

> [!INDICATION]
> Faire la somme des étapes du cycle : quels réactifs entrent, quel produit sort ?

#### Solution

Le cycle réalise l'**hydroalcynylation** de l'allène : $\mathrm{R^1{-}C{\equiv}C{-}H}+\mathrm{H_2C{=}C{=}CH{-}R^2}\rightarrow\mathrm{R^1{-}C{\equiv}C{-}C(CH_3){=}CH{-}R^2}$ (1,3-ényne). Ici :

$$\boxed{\mathbf{15}+\mathrm{HC{\equiv}C{-}CH_2OH}\xrightarrow{\ \mathrm{Pd(OAc)_2,\ (4\text{-}MeOPh)_3P,\ CuCl,\ NEt_3}\ }\mathbf{16}}$$

> [!METHODE]
> Le bilan d'un cycle catalytique s'obtient en sommant les étapes : le catalyseur et les intermédiaires s'éliminent.

### Question 54

> [!INDICATION]
> Sur quel carbone de l'allène le proton se fixe-t-il dans le cycle ? Quelles sont les deux autres positions possibles ?

> [!INDICATION]
> Un cation peut-il être délocalisé si sa lacune est orthogonale au système π voisin ?

#### Solution

Dans le cycle, le proton se fixe sur le CH$_2$ terminal de l'allène. Il en résulte le cation vinylique $\mathrm{CH_3{-}C^+{=}CH{-}R^2}$, lié ensuite au palladium. Autres carbocations possibles :
- protonation sur l'autre carbone terminal (celui qui porte R$^2$) : cation vinylique $\mathrm{CH_2{=}C^+{-}CH_2{-}R^2}$ ;
- protonation sur le carbone central : cation $\mathrm{^+CH_2{-}CH{=}CH{-}R^2}\leftrightarrow\mathrm{CH_2{=}CH{-}C^+H{-}R^2}$. C'est un cation allylique, stabilisé par mésomérie une fois le CH$_2$ tourné de 90° ; juste après la protonation, la lacune est orthogonale au système π restant.

Les cations vinyliques (lacune sur un carbone sp, non délocalisée) sont très instables. La régiosélectivité observée est imposée par la coordination au métal, et non par la stabilité intrinsèque du cation.

> [!PIEGE]
> Un cation formé sur le carbone central d'un allène n'est pas allylique tout de suite : la lacune est d'abord orthogonale à la double liaison restante.

### Question 55

> [!INDICATION]
> Suivre le degré d'oxydation du palladium en comptant ses ligands anioniques (acétate, alcynyle, vinyle) avant et après chaque étape.

> [!INDICATION]
> Quelle étape forme la liaison C–C et libère le produit ?

#### Solution

- **Étape 4** : le centre palladié anionique capte le cation vinylique et forme la liaison σ Pd–C(vinyle). Le palladium gagne un ligand anionique et son degré d'oxydation formel augmente de deux unités : c'est une **addition oxydante** formelle. Avec l'étape 3, elle revient à une hydropalladation de l'allène (insertion dans une liaison Pd–H).
- **Étape 5** : **élimination réductrice**. La liaison C(sp)–C(sp$^2$) entre l'alcynyle et le vinyle se forme, l'ényne est libérée et le palladium revient au degré +II (complexe de départ).

> [!JURY]
> Le rapport 2025 rappelle que les réactions portent des noms spécifiques qu'il convient de maîtriser. Les étapes élémentaires des cycles catalytiques (addition oxydante, insertion, élimination réductrice, transmétallation) font partie de ce vocabulaire.

> [!METHODE]
> Pour nommer une étape, compter le degré d'oxydation et le nombre de ligands du métal avant et après.

### Question 56

> [!INDICATION]
> À quelle étape la géométrie de la double liaison trisubstituée est-elle fixée ?

> [!INDICATION]
> Comparer les deux approches possibles du palladium sur le cation vinylique : laquelle rapproche deux groupes volumineux ?

#### Solution

L'étape 4 fixe la géométrie de la double liaison trisubstituée $\mathrm{(CH_3)(Pd)C{=}CH{-}R^2}$ : le palladium peut se lier au cation vinylique (linéaire) du côté opposé à R$^2$ ou du même côté.
- Majoritaire : Pd (puis l'alcynyle après l'élimination réductrice) en trans de R$^2$, ce qui donne l'ényne $E$ de **16**.
- Minoritaire : Pd et R² du même côté, d'où l'ényne $\mathrm{R^1C{\equiv}C{-}C(CH_3){=}CH{-}R^2}$ avec l'alcynyle et R² en cis (isomère $Z$).

Le diastéréoisomère minoritaire est défavorisé par la gêne stérique entre la chaîne R$^2$, volumineuse, et le fragment Pd(L)(alcynyl–CuCl), qui porte la phosphine encombrante $(4\text{-MeOPh})_3$P. L'état de transition correspondant est plus haut en énergie (contrôle cinétique).

> [!METHODE]
> Une stéréosélectivité sous contrôle cinétique s'explique par la comparaison des encombrements dans les deux approches possibles.

> [!JURY]
> Rapport 2026 : « La diastéréosélectivité devait être interprétée par des considérations de gêne stérique. »

## Problème 2, partie E — Achèvement du fragment B (Q57–59)

Planifier de courtes séquences en vérifiant la compatibilité de chaque réactif avec toutes les fonctions présentes (acétonide, TBS, PMB, polyène).

### Question 57

> [!INDICATION]
> Comparer **16** et **17** : que deviennent l'alcyne, l'alcool primaire et le groupe P ?

> [!INDICATION]
> Allonger une chaîne de deux carbones en créant un ester α,β-insaturé $E$ : passer par un aldéhyde et un ylure stabilisé. Vérifier chaque réactif face à P, TBS et acétonide.

#### Solution

**16** → **17** : l'alcyne devient une double liaison $E$, la chaîne gagne un motif $\mathrm{CH{=}CH{-}CO_2Et}$ et l'alcool secondaire est libéré. Avec $P=\mathrm{PMB}$ :

1. Réduction trans de l'alcool propargylique en alcool allylique $E$ : Red-Al (ou LiAlH$_4$), THF, 0 °C, puis hydrolyse douce (NH$_4$Cl). L'hydroxyle oriente l'hydroaluminium (réaction hors programme). Le Lindlar donnerait l'isomère $Z$.
2. Oxydation ménagée de l'alcool allylique primaire en diénal : MnO₂, CH₂Cl₂, 25 °C (ou DMP, NaHCO₃).
3. Réaction de Wittig avec l'ylure stabilisé $\mathrm{Ph_3P{=}CH{-}CO_2Et}$, toluène, 25–80 °C : on obtient le triénoate d'éthyle de configuration $E$ (ylure stabilisé, donc $E$-sélectif).
4. Déprotection du PMB : DDQ, CH$_2$Cl$_2$/H$_2$O tamponné à pH 7, 0 °C. On obtient **17** sans toucher au TBS ni à l'acétonide.

> [!METHODE]
> Planifier une séquence : écrire les intermédiaires, puis relire chaque réactif face à toutes les fonctions présentes (groupes protecteurs, acétal, insaturations).

> [!PIEGE]
> Une hydrogénation de Lindlar donnerait l'alcène $Z$, alors que **17** porte une double liaison $E$.

> [!JURY]
> Rapport 2026, appréciations globales : « En chimie organique, des conditions opératoires précises sont attendues, précisant en particulier les réactifs, le solvant et la température. » Chaque étape de la séquence doit les donner.

### Question 58

> [!INDICATION]
> Quelle petite molécule perd-on entre **17** et **18** ? Quelle conjugaison apparaît ?

> [!INDICATION]
> Pourquoi éviter une catalyse acide à chaud ? Comment transformer OH en bon groupe partant ?

#### Solution

**17** → **18** est une **β-élimination (déshydratation)** de l'alcool secondaire allylique. Elle crée une double liaison conjuguée qui relie les deux systèmes π : le pentaénoate est entièrement conjugué jusqu'au chlorure vinylique.

Précautions : préserver l'acétal (acétonide) et l'ester, ainsi que le TBS et le polyène.
- Pas d'acide fort ni de chaleur (déshydratation E1 classique) : l'acétonide serait hydrolysé, le TBS coupé (pH ≤ 2), et le polyène pourrait s'isomériser ou se polymériser via un carbocation allylique.
- Pas de base aqueuse forte (soude, potasse) : elle saponifierait l'ester éthylique et couperait le TBS (pH > 12).
- On active donc l'alcool en bon groupe partant, puis on élimine en E2, en milieu anhydre, avec une base organique non nucléophile qui n'attaque pas l'ester : MsCl, Et$_3$N, CH$_2$Cl$_2$, 0 °C, puis DBU ;
- Contrôler la stéréochimie : la double liaison $E$ attendue est favorisée thermodynamiquement par la conjugaison.
- Travailler sous atmosphère inerte et à l'abri de la lumière : le polyène est sensible à l'oxydation et à la photo-isomérisation.

> [!PIEGE]
> Une déshydratation E1 en milieu acide chaud couperait l'acétonide et le TBS et isomériserait le polyène. À l'inverse, une base aqueuse forte saponifierait l'ester.

> [!JURY]
> Rapport 2026 : « La déshydratation devait préserver les fonctions acétal et ester. »

### Question 59

> [!INDICATION]
> Comparer **18** et le fragment B : quel groupe protecteur doit partir et quelle fonction doit apparaître ?

> [!INDICATION]
> Choisir des conditions qui ne touchent ni à l'acétonide ni au polyène.

#### Solution

**18** → fragment B : le motif $\mathrm{CH(OTBS){-}CH_3}$ devient la méthylcétone.

1. Déprotection du TBS : TBAF, THF, 25 °C. On obtient l'alcool secondaire, sans toucher à l'acétonide, à l'ester ni au polyène (on évite le milieu acide, qui ouvrirait l'acétonide).
2. Oxydation ménagée de l'alcool secondaire en cétone : DMP, NaHCO$_3$, CH$_2$Cl$_2$, 25 °C (ou oxydation de Swern). Les conditions sont neutres et ne touchent pas aux doubles liaisons.

$$\boxed{\mathbf{18}\xrightarrow{\ \mathrm{TBAF,\ THF}\ }\text{alcool}\xrightarrow{\ \mathrm{DMP,\ NaHCO_3,\ CH_2Cl_2}\ }\text{fragment B}}$$

> [!JURY]
> Le rapport 2025 indique que les dernières questions, très rarement abordées, ont été valorisées lorsque les raisonnements étaient cohérents et correctement justifiés. Une séquence courte et bien argumentée rapporte des points même en fin d'épreuve.

## Bilan

**Méthodes à retenir.**

- *Mésomérie et longueurs de liaison* : écrire toutes les formes équivalentes avant de comparer des liaisons (Q2, Q3).
- *Diagrammes de distribution* : un croisement donne un p$K_a$ (ou une constante) apparent ; « majoritaire » se traduit par un facteur 10 ; contrôler toute lecture par la conservation de la matière (Q5–7).
- *Dosages par différence* : titrage en retour, rôle des témoins négatif et positif, domaine de validité d'une mesure (excès de réactif, différence grande devant l'incertitude), gamme de dilutions (Q10–19).
- *Conversion rédox → masse de O$_2$* : tout repose sur le nombre d'électrons échangés (Q9, Q12, Q16).
- *Cinétique formelle* : dégénérescence de l'ordre, réactions parallèles et successives, pentes initiales pour séparer des constantes, linéarisation d'Arrhenius avec l'abscisse $1000/T$ (Q25–34).
- *Synthèse organique* : aldolisation dirigée (LDA, −78 °C), Williamson et ouverture S$_\text{N}$2 des époxydes au carbone le moins encombré, suivi d'un centre stéréogène dans une séquence ouverture–refermeture, Lindlar, époxydation syn, acétonide, couple DDQ/PMB, choix raisonné d'un groupe protecteur à l'aide d'une table (Q35–59).
- *Lecture d'un cycle catalytique* : bilan par sommation, degré d'oxydation du métal à chaque étape, vocabulaire (addition oxydante, élimination réductrice), origine de la stéréosélectivité (Q53–56).

**Prérequis à revoir.** Règle de Klechkowski et ses exceptions ; nombres d'oxydation et demi-équations ; formule de Nernst et constante d'une réaction rédox ; résolution d'une équation différentielle linéaire d'ordre 1 à second membre exponentiel ; règles CIP (duplication des doubles liaisons) ; tables de constantes de couplage et de nombres d'onde IR.

**Questions classiques transposables.** La DCO (Q9–19) est un modèle de titrage en retour qu'on retrouve dans tous les dosages indirects (dosage de la vitamine C, du dioxygène dissous par la méthode de Winkler). Le schéma $A\to B\to C$ avec réaction parallèle (Q27–33) est le cadre standard de la cinétique des intermédiaires réactionnels. Les questions Q40–41 sur l'épibromhydrine illustrent un piège récurrent : deux sites électrophiles sur la même molécule et des conséquences stéréochimiques opposées. Le choix d'un groupe protecteur (Q52) et la planification d'une courte séquence (Q57) se travaillent de la même façon dans tout problème de synthèse : lister les fonctions présentes, puis vérifier chaque réactif face à chacune.

**Ce que le rapport 2026 met en avant.** Des équations équilibrées, des grandeurs définies et des unités indiquées ; en chimie organique, des conditions opératoires complètes (réactifs, solvant, température) et des mécanismes fléchés avec charges et doublets. Il signale la difficulté de Q9, attend des lectures et des comparaisons quantitatives (Q5, Q17), la justification par les règles CIP (Q38) et la compatibilité de chaque étape avec les protections présentes (Q35, Q58).

**Erreurs de la copie IA source corrigées ici.** Trois longueurs de liaison au lieu de deux (Q2) ; convergence supposée des deux voies vers **2** au lieu de son énantiomère (Q40–41) ; groupe protecteur acétate incompatible avec la suite (Q52), d'où une séquence incohérente (Q57). Le détail figure dans la revue.
