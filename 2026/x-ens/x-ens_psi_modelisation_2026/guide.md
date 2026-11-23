# X-ENS PSI — Modélisation 2026 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

L’épreuve du 17 avril 2026 dure cinq heures, sans calculatrice. Le modèle de référence est un avion régional ATR 72 doté de deux turbopropulseurs. La partie A relie les forces, les débits d’un moteur et les réglages des deux hélices. La partie B étudie une source électrique et les contraintes d’un entraînement électrique en altitude.

| Questions | Grandeur suivie | Support à utiliser |
|---|---|---|
| 1–7 | Travail demandé à l’avion pendant le vol | Données et profils des figures 2 à 5 |
| 8–23 | Air, kérosène, températures et puissances | Étages, débits et courbes des figures 9 à 15 |
| 24–33 | Déplacement du distributeur, pas, poussée | Cinématique et caractéristiques des figures 16 à 22 |
| 34–43 | Tension d’une pile et impédance interne | Mesures, code et circuit des figures 24 à 28 |
| 44–52 | Vitesse de base, tension et tenue électrique | Schéma monophasé et courbe de Paschen |

Un partage possible des 300 minutes réserve 35 minutes à la mission, 75 minutes à la thermodynamique, 55 minutes à la régulation et à la validation, 65 minutes à la pile et 50 minutes à l’entraînement et à l’isolation. Les 20 minutes restantes permettent de reprendre les lectures graphiques, les conversions et les grandeurs rapportées à un seul moteur.

## A1. Besoins énergétiques du vol régional

### Question 1

> [!INDICATION]
> Identifier les solutions d'équilibre de l'équation : ce sont les deux racines de son second membre.

> [!INDICATION]
> Calculer la dérivée de la tangente hyperbolique avant de diviser.

#### Solution

Avec $k=\sqrt{B/A}$, on trouve $u'=B(1-u^2)/k=\omega(1-u^2)$ avec $\omega=\sqrt{AB}$. Puisque $|f_0|<k$, on peut écrire initialement $u=\tanh v$. La dérivation donne $(1-\tanh^2 v)v'=\omega(1-\tanh^2 v)$, donc $v'=\omega$. On obtient sur tout $\mathbb R_+$ la solution
$$
f(t)=\sqrt{B/A}\,\tanh\!\left(\sqrt{AB}\,t+\operatorname{argth}\!\left(f_0\sqrt{A/B}\right)\right).
$$
Elle vérifie l'équation et la condition initiale. L'unicité locale du problème de Cauchy, dont le second membre est polynomial, garantit qu'il s'agit de la solution cherchée.

> [!METHODE]
> La condition initiale à l'intérieur des équilibres justifie la branche réelle de la fonction réciproque.

### Question 2

> [!INDICATION]
> Écrire la résultante des forces tangentiellement à chaque portion de trajectoire.

> [!INDICATION]
> Au début de la montée, repartir de la vitesse de décollage en décalant l'origine du temps.

#### Solution

La masse vaut $M_t=29\,850$ kg. La projection du bilan des forces sur la trajectoire élimine la portance. Posons $F=(T_u)_{\max}-M_tg\sin\theta$ et $V_*=\sqrt{F/K}$. Aux temps de décollage $T_d$ et de fin de montée $T_m$, la vitesse s'écrit par morceaux :

- Roulement, pour $0\le t\le T_d$ : $M_t\dot V=(T_u)_{\max}$, donc $V=(T_u)_{\max}t/M_t$ et $T_d=M_tV_d/(T_u)_{\max}$.
- Montée, pour $T_d\le t<T_m$ : $M_t\dot V=F-KV^2$. Avec $V(T_d)=V_d$, la question 1 donne
$$
V(t)=V_*\tanh\!\left(\frac{\sqrt{KF}}{M_t}(t-T_d)+\operatorname{argth}(V_d/V_*)\right).
$$
La fin de la montée satisfait $H=\sin\theta\int_{T_d}^{T_m}V(t)\,dt$.
- Palier : $V=V_p=153$ m/s par prescription, avec $T_u=KV_p^2/2$.

Les constantes imprimées donnent $T_d=34,2$ s et $V_*=135,7$ m/s. La figure 4 indique $26$ s et une montée vers $153$ m/s. Sans transition supplémentaire ni modification des constantes, la loi de montée et le palier tracé ne se raccordent pas. Pour lire les énergies aux questions 4 et 5, on emploie les durées prescrites sur la figure.

![Figure 1 — La loi de montée calculée plafonne à 135,7 m/s avec les données du tableau. La vitesse de palier prescrite vaut 153 m/s.](figures/q02-vitesse-mission.svg)

> [!PIEGE]
> Contrôler la vitesse limite avant de supposer que la vitesse de croisière peut être atteinte.

### Question 3

> [!INDICATION]
> Pour chaque phase, comparer le coefficient choisi à celui qu'aurait la même vitesse dans l'air réel.

> [!INDICATION]
> Séparer une erreur de force à vitesse donnée et son effet sur l'accélération.

#### Solution

Au roulement, annuler la traînée la sous-estime dès que l'avion avance. À poussée donnée, l'accélération est alors surestimée. En montée, la loi quadratique est plausible, mais conserver le coefficient du sol surestime la traînée à vitesse donnée si la masse volumique décroît avec l'altitude et si la configuration aérodynamique reste fixée. L'accélération est alors sous-estimée. En palier, la division par deux représente la baisse de densité. Pour une atmosphère standard à 6 500 m, le rapport de densités est proche de $0,51$, ce qui donnerait une légère sous-estimation avec un coefficient de traînée constant. Le signe précis dépend de l'atmosphère et de la configuration. Les écarts des phases ont des signes opposés. On ne peut attribuer de signe certain à l'erreur énergétique totale sans pondérer les travaux et connaître la traînée réelle.

> [!METHODE]
> Le travail perdu dépend de toute la trajectoire : la durée d'une phase influe sur son poids dans le bilan global.

### Question 4

> [!INDICATION]
> Recenser les forces qui travaillent dans le référentiel du sol.

> [!INDICATION]
> L'intégrale du travail de traînée s'écrit avec la vitesse multipliée par la force instantanée.

#### Solution

Dans le référentiel terrestre supposé galiléen, la portance et la réaction normale du sol ont un travail nul. Entre le repos et le palier à $H$,
$$
E_{TP}=\tfrac12M_tV_p^2+M_tgH
     +K\int_{T_d}^{T_m}V^3(t)\,dt
     +\tfrac K2 V_p^3(T_p-T_m).
$$
Le membre de droite additionne l'accroissement d'énergie cinétique, le gain d'altitude et les deux travaux à fournir contre la traînée. La traînée de roulement est nulle dans le modèle. Il s'agit d'un travail propulsif utile à l'avion.

> [!PIEGE]
> Une force quadratique en vitesse conduit à une puissance cubique, pas quadratique.

### Question 5

> [!INDICATION]
> Convertir les heures de palier en secondes et toutes les énergies en gigajoules.

> [!INDICATION]
> Construire une borne inférieure de l'intégrale de traînée en ne gardant que la vitesse minimale de la montée.

#### Solution

Avec $T_p-T_m=9\,000$ s, on obtient respectivement $0,349$ GJ d'énergie cinétique, $1,90$ GJ d'énergie potentielle, $0,0027$ GJ contre la traînée en montée (valeur imposée) et $19,66$ GJ contre celle du palier. Le total vaut $21,92$ GJ, dont environ 90 % pour le palier.

La valeur imprimée pour la montée ne peut toutefois pas être l'intégrale annoncée. Sur les $559-26=533$ s de la figure 4, la vitesse est au moins $55$ m/s, donc $K\int V^3\,dt\ge1,22\times55^3\times533=108$ MJ, déjà quarante fois les $2,7$ MJ indiqués. Le total précédent suit la consigne numérique. La précision est également limitée par la masse et le coefficient de traînée supposés constants dans chaque phase, par la transition de vitesse et par l'absence de rendement de conversion.

![Figure 2 — Travaux utiles du profil de vol avec la donnée de montée imposée. Le palier de 2 h 30 représente presque 90 % du total.](figures/q05-bilan-energetique.svg)

> [!METHODE]
> Un simple encadrement peut contrôler une valeur numérique imposée, même sans calculer l'intégrale.

### Question 6

> [!INDICATION]
> Un wattheure représente 3 600 joules. Diviser l'énergie par l'énergie disponible par kilogramme.

> [!INDICATION]
> Reconstituer la masse au décollage après avoir remplacé le carburant.

#### Solution

Un kilogramme de batterie stocke $250\times3\,600=9,0\,10^5$ J. À rendement unité, la première estimation est donc $m_b=21,92\,10^9/(9,0\,10^5)\simeq24\,400$ kg, soit environ $111\,\%$ des $22\,000$ kg de masse à vide. En remplaçant les 450 kg de kérosène, la masse au départ atteindrait déjà environ 53,8 t. Le calcul initial a pourtant été fait pour 29,85 t.

Ce profil régional n'est donc pas réaliste par simple remplacement du carburant avec les batteries considérées. La masse supplémentaire accroît le travail de montée et la portance requise. À géométrie, atmosphère et vitesse fixées, la traînée induite augmente. Un coefficient $K$ global ajusté à la nouvelle configuration et la consommation de mission augmenteraient. Une modification du seul poids ne change pas directement le coefficient de traînée parasite.

> [!PIEGE]
> Distinguer la batterie embarquée de la masse totale. Ajouter la première change l'énergie requise.

### Question 7

> [!INDICATION]
> Tracer l'énergie disponible en fonction de la masse totale en commençant à la masse hors batteries.

> [!INDICATION]
> Comparer les pentes en joules par kilogramme, puis le déficit au point de départ.

#### Solution

La masse hors batteries vaut $M_0=M_v+M_u=29\,400$ kg. À la masse totale $M$, la droite d'énergie disponible vaut $E_b(M)=0,9\,10^6(M-M_0)$ J. Une solution nécessite une intersection avec la courbe des besoins pour $M\ge M_0$.

Sur la branche de pente $0,9\,10^6$ J/kg, un kilogramme de batterie couvre exactement le besoin marginal du kilogramme ajouté, sans combler le déficit initial. Avec l'ordonnée à l'origine imprimée $-22\,10^9$ J, l'écart $E-E_b$ serait constant et égal à $4,46$ GJ. Sur la branche de pente $2\,10^6$ J/kg, chaque kilogramme ajoute $1,1$ MJ de déficit. La droite imprimée $2\,10^6M-1,8\,10^{10}$ donne déjà un déficit à $M_0$. La courbe bleue elle-même est strictement au-dessus de l'énergie disponible au départ et croît plus vite sur la plage accessible. Il n'existe donc pas de solution pour ce profil dans le modèle présenté. L'ordonnée à l'origine imprimée pour la première interpolation ne reproduit pas les ordonnées de la courbe bleue, et le tracé au-delà de 30 t reste exploratoire.

![Figure 3 — L'énergie des batteries disponibles part de zéro pour 29,4 t. Elle reste inférieure aux besoins lus sur la courbe du sujet, y compris sur la partie extrapolée.](figures/q07-energie-et-masse.svg)

> [!METHODE]
> Une pente égale à l'énergie massique ne peut résorber un déficit déjà constitué.

## A2. Thermodynamique du turbopropulseur

### Question 8

> [!INDICATION]
> Partir de la loi de Laplace à quantité de matière fixée.

> [!INDICATION]
> Prendre une différentielle logarithmique puis introduire le signe de la définition de compressibilité.

#### Solution

À quantité fixée, sur une isentrope d'un gaz parfait de $\gamma$ constant, $PV^\gamma$ est constant. La différentiation donne $dV/V=-dP/(\gamma P)$, donc $\chi_s=1/(\gamma P)$, en $\mathrm{Pa}^{-1}$.

> [!PIEGE]
> La compressibilité isotherme et la compressibilité isentropique diffèrent pour un gaz parfait.

### Question 9

> [!INDICATION]
> Éliminer la masse volumique à l'aide de l'équation des gaz parfaits.

> [!INDICATION]
> Remplacer ensuite la compressibilité par le résultat précédent.

#### Solution

L'équation d'état donne $\rho_a=P M_a/(RT)$. Ainsi $V_{\rm son}=(\rho_a\chi_s)^{-1/2}=\sqrt{\gamma RT/M_a}$. La masse molaire est en kg/mol lorsque $R$ est exprimé en unités SI.

> [!METHODE]
> Une vitesse au carré s'exprime en joules par kilogramme. Cette vérification impose la conversion de la masse molaire.

### Question 10

> [!INDICATION]
> Écrire la relation de Mayer en capacités massiques.

> [!INDICATION]
> Éliminer la capacité à volume constant par le coefficient isentropique.

#### Solution

En grandeurs massiques, $c_p-c_v=R/M$ et $\gamma=c_p/c_v$. On obtient $c_p=\gamma R/[(\gamma-1)M]$ en $\mathrm{J\,kg^{-1}\,K^{-1}}$.

> [!PIEGE]
> Le résultat molaire doit être divisé par la masse molaire.

### Question 11

> [!INDICATION]
> Quelle masse traverse la surface d'entrée pendant une seconde ?

> [!INDICATION]
> La condition de vol fournit une vitesse sous la forme d'un rapport à la vitesse locale du son.

#### Solution

Le flux d'une masse volumique uniforme traversant normalement la section $A_e$ est $D_{ma}=\rho_a A_eV_p$. En remplaçant $V_p$ par $\mu_1V_{\rm son}$, on obtient
$$D_{ma}=\rho_a A_e\mu_1\sqrt{\gamma RT_1/M_a}.$$
Il s'agit de l'entrée d'un turbopropulseur.

> [!METHODE]
> Délimiter le système à un moteur permet de traiter ensuite le nombre de moteurs au bon endroit.

### Question 12

> [!INDICATION]
> Dans le diffuseur, le flux ralentit sans échange de chaleur ni travail d'arbre.

> [!INDICATION]
> Relier d'abord l'énergie cinétique perdue à la température, puis convertir le rapport de températures en rapport de pressions.

#### Solution

Le diffuseur est adiabatique, sans travail d'arbre, et sa vitesse de sortie est négligeable. La conservation de $h+V^2/2$ donne $c_p(T_2-T_1)=V_p^2/2$. La relation de Laplace sur la compression isentropique donne ensuite
$$
T_2=T_1\left(1+\tfrac{\gamma-1}{2}\mu_1^2\right),\qquad
P_2=P_1\left(1+\tfrac{\gamma-1}{2}\mu_1^2\right)^{\gamma/(\gamma-1)}.
$$
La stagnation fait croître la température et la pression statiques.

> [!METHODE]
> La température d'arrêt diffère de la température statique en amont.

### Question 13

> [!INDICATION]
> Construire la sortie idéale à la même pression que la sortie réelle.

> [!INDICATION]
> Le compresseur réel exige plus de travail que le compresseur isentropique.

#### Solution

Posons $a=(\gamma-1)/\gamma$. La température idéale est $T_{3s}=T_2r_c^a$. Comme $\eta_c=(T_{3s}-T_2)/(T_3-T_2)$,
$$
T_3=T_2\left(1+\frac{r_c^a-1}{\eta_c}\right),\qquad
P_{\rm comp}=D_{ma}\frac{\gamma R}{(\gamma-1)M_a}T_2
                    \frac{r_c^a-1}{\eta_c}.
$$
La puissance est positive dans ce bilan de l'air. À la température et au Mach du tableau, $T_2=262,5$ K et $T_3\simeq582$ K.

> [!PIEGE]
> Placer le rendement au dénominateur pour la hausse réelle de température.

### Question 14

> [!INDICATION]
> Équilibrer dans l'ordre carbone, hydrogène puis oxygène.

> [!INDICATION]
> Pour chaque mole de dioxygène, compter les quatre moles d'azote qui l'accompagnent.

#### Solution

Pour une mole de carburant, les douze atomes de carbone donnent 12 moles de dioxyde de carbone, les 26 hydrogènes donnent 13 moles d'eau et les 37 atomes d'oxygène nécessaires proviennent de 18,5 moles de dioxygène :
$$
\mathrm{C_{12}H_{26}}+18,5\,\mathrm{O_2}+74\,\mathrm{N_2}
 \longrightarrow12\,\mathrm{CO_2}+13\,\mathrm{H_2O}+74\,\mathrm{N_2}.
$$
Il faut $(18,5\times32+74\times28)=2\,664$ g d'air pour $170$ g de carburant. Donc $\mathrm{AFR}=2\,664/170\simeq15,67$ kg d'air par kg de carburant.

> [!PIEGE]
> Un rapport massique air/carburant inclut l'azote spectateur. Les pourcentages fournis sont molaires.

### Question 15

> [!INDICATION]
> Lire la courbe au Mach demandé et à l'altitude demandée.

> [!INDICATION]
> Construire le débit d'air effectivement stœchiométrique avant d'utiliser le rapport air/carburant.

#### Solution

À 6 500 m, la courbe Mach $0,5$, troisième en partant du haut sur la figure 11, donne $D_{ma}\simeq19$ kg/s. Seuls 20 % du débit d'air réagissent, donc $D_{mf}=0,2D_{ma}/\mathrm{AFR}\simeq0,242$ kg/s **par moteur**. L'annexe utilise $15$ kg/s, que la figure donne à Mach $0,4$ à la même altitude. Cette autre donnée conduirait à $0,191$ kg/s par moteur. Les deux lectures sont conservées pour chiffrer leurs conséquences aux questions 21 et 22.

![Figure 4 — Tranche de la figure 11 à 6 500 m. Le débit de 19 kg/s se lit à Mach 0,5. Les 15 kg/s de l'annexe correspondent à Mach 0,4.](figures/q15-debit-par-moteur.svg)

> [!PIEGE]
> Le débit du moteur et le débit de la fraction d'air réactive sont différents.

### Question 16

> [!INDICATION]
> Appliquer la somme stœchiométrique des enthalpies de formation aux produits, puis aux réactifs.

> [!INDICATION]
> Le dioxygène et le diazote sont pris dans leur état standard, de référence.

#### Solution

La loi de Hess donne, avec les enthalpies molaires fournies et l'eau à l'état gazeux,
$$
\Delta_rH^\circ=12(-392)+13(-237)-(-355)
                 =-7\,430\ \mathrm{kJ/mol}.
$$
La combustion est exothermique. Une mole de dodécane libère $7,43$ MJ, soit $43,7$ MJ par kilogramme pour les valeurs du sujet.

> [!METHODE]
> Le signe de l'enthalpie de réaction donne immédiatement le sens de l'échange thermique.

### Question 17

> [!INDICATION]
> Le nombre de moles de combustible brûlées par seconde est le débit massique divisé par la masse molaire.

> [!INDICATION]
> Égaler la puissance libérée par ces moles à la puissance d'échauffement du flux d'air entier.

#### Solution

Sur toute la chambre, le surplus d'air chauffe lui aussi. Avec $M_f=0,170$ kg/mol et en assimilant la capacité thermique du courant chauffé à celle de l'air comme proposé, le bilan adiabatique stationnaire donne
$$
D_{ma}c_{p,a}(T_4-T_3)=-\frac{D_{mf}}{M_f}\Delta_r H^\circ,\qquad
T_4=T_3-\frac{0,2M_a(\gamma-1)}{\mathrm{AFR}\,M_f\gamma R}\Delta_rH^\circ .
$$
La stœchiométrie impose $\mathrm{AFR}\,M_f=92,5 M_a$. L'élévation vaut donc $-0,2(\gamma-1)\Delta_rH^\circ/(92,5\gamma R)\simeq552$ K, avec l'enthalpie en joules par mole. On obtient $T_4\simeq1\,134$ K.

> [!PIEGE]
> Le pourcentage d'air réactif limite le débit de combustible et les gaz diluants s'échauffent également.

### Question 18

> [!INDICATION]
> Repérer la sortie de la turbine, puis la sortie de la tuyère, avant d'appliquer un rendement.

> [!INDICATION]
> Relier la température idéale à la pression à la sortie du premier organe. La chute restante se transforme en vitesse du jet.

#### Solution

Le débit de gaz brûlés est $D_g=D_{ma}(1+0,2/\mathrm{AFR})$. Notons $a_c=(\gamma_c-1)/\gamma_c$ et $c_{p,g}=\gamma_cR/[(\gamma_c-1)M_g]$, où $M_g$ est la masse molaire moyenne des gaz. Pour la dilution indiquée, une mole de carburant reçoit cinq fois l'air stœchiométrique. Les gaz contiennent $12\,\mathrm{CO_2}$, $13\,\mathrm{H_2O}$, $74\,\mathrm{O_2}$ et $370\,\mathrm{N_2}$, soit $M_g=(0,170+5\times2,664)/469\simeq0,02876$ kg/mol.

Avec $P_5=P_1/\pi_e$, le travail réel de la turbine correspond à la chute $T_4-T_5=\eta_T T_4[1-(P_1/(\pi_eP_4))^{a_c}]$. La puissance d'arbre fournie aux deux charges est
$$P_T=D_g c_{p,g}\eta_T T_4\left[1-\left(\frac{P_1}{\pi_e P_4}\right)^{a_c}\right].$$
Dans la tuyère adiabatique, la chute d'enthalpie statique devient énergie cinétique. En supposant en outre la tuyère isentropique, $T_6=T_5\pi_e^{a_c}$. La puissance totale libérée par la détente des gaz sur les deux étages est alors
$$
\begin{aligned}
P_{\rm tot}&=P_T+D_gc_{p,g}T_5(1-\pi_e^{a_c})\\
 &=D_gc_{p,g}T_4\left[1-\pi_e^{a_c}
 \left\{1-\eta_T\left(1-\left(\frac{P_1}{\pi_e P_4}\right)^{a_c}\right)\right\}\right].
\end{aligned}
$$
Si l'on assimile les deux détentes à une turbine équivalente de rendement global $\eta_T$, on écrit $D_gc_{p,g}\eta_T T_4[1-(P_1/P_4)^{a_c}]$. Cette formule coïncide avec la puissance d'arbre dans l'approximation d'une chute de pression négligeable en tuyère ($\pi_e\simeq1$). Un rendement de turbine seul ne détermine pas les pertes d'une tuyère réelle.

![Figure 5 — La turbine fournit du travail à l'arbre. La tuyère accélère les gaz. Le compresseur et l'hélice se partagent la puissance d'arbre.](figures/q18-detente-et-puissance.svg)

> [!PIEGE]
> La puissance cinétique du jet et la puissance d'arbre sont deux sorties physiques distinctes.

### Question 19

> [!INDICATION]
> Faire le bilan mécanique de l'arbre et identifier la charge entraînée en amont du réducteur.

> [!INDICATION]
> Le rendement de transmission agit sur la puissance restant après le prélèvement du compresseur.

#### Solution

Le compresseur prélève $P_{\rm comp}$. La puissance reçue par l'hélice vaut donc $P_{\rm hélice}=\eta_m(P_T-P_{\rm comp})$ pour un moteur. Si $P_{\rm tot}$ désigne la puissance totale libérée au sens de la question 18, on retranche en plus sa part cinétique de tuyère pour retrouver $P_T$. Dans la convention de la détente équivalente entièrement disponible sur l'arbre, la formule devient $\eta_m(P_{\rm tot}-P_{\rm comp})$. Le rendement aérodynamique de l'hélice intervient ultérieurement pour passer à la puissance de propulsion.

> [!METHODE]
> Suivre séparément les pertes aérodynamiques et les pertes mécaniques évite de les compter deux fois.

### Question 20

> [!INDICATION]
> Localiser d'abord la fin de combustion et le début de la détente sur le plan température-entropie.

> [!INDICATION]
> Distinguer entropie échangée par chaleur sortante et entropie créée par les irréversibilités.

#### Solution

À carburant et conditions d'entrée fixés :

- Une fuite de chaleur vers l'extérieur réduit l'enthalpie de sortie par rapport à l'étage adiabatique délivrant le même travail. Le point de sortie descend dans le diagramme $T,s$. L'entropie du fluide vérifie $\Delta s=\int\delta q/T_{\rm paroi}+s_{\rm créée}$, donc un transfert de chaleur sortant ne fixe pas à lui seul le sens de son déplacement horizontal.
- Une combustion incomplète libère moins d'énergie. Sur l'isobare $3\to4$, le point 4 s'arrête à une température plus basse et, dans le modèle à composition fixée, à une entropie plus faible que le point idéal. La détente débute plus bas.
- Les pertes de charge abaissent la pression totale disponible pour la détente. La combustion cesse notamment de suivre une unique isobare. Un écoulement adiabatique dissipatif produit de l'entropie et déplace la trajectoire vers les entropies croissantes à température totale donnée. Le travail disponible sur l'arbre décroît.

> [!PIEGE]
> Un échange thermique vers l'extérieur ne donne pas à lui seul le signe du changement d'entropie du fluide.

### Question 21

> [!INDICATION]
> À partir d'une mole de carburant, calculer la masse de dioxyde de carbone formée.

> [!INDICATION]
> Appliquer le facteur massique au débit total de carburant des deux moteurs.

#### Solution

Pour $170$ g de carburant on produit $12\times44=528$ g de $\mathrm{CO_2}$, soit $3,106$ kg par kilogramme de carburant. Les deux turbopropulseurs émettent donc ensemble $2\times0,242\times3,106\simeq1,50$ kg/s de $\mathrm{CO_2}$ en croisière selon la figure 11. Avec le débit d'air retenu par l'annexe, on retrouve $2\times0,19\times3,106\simeq1,18$ kg/s.

> [!METHODE]
> L'oxygène prélevé dans l'air explique que la masse des émissions puisse dépasser celle du combustible.

### Question 22

> [!INDICATION]
> Combien de secondes faut-il pour parcourir 100 km à la vitesse de palier ?

> [!INDICATION]
> Convertir le débit de l'avion en masse, puis en litres, et enfin rapporter le volume au nombre de passagers.

#### Solution

À 550 km/h, parcourir 100 km prend $100\times3\,600/550\simeq655$ s. Avec la lecture à Mach $0,5$ de la figure 11, les deux moteurs brûlent ensemble $2\times0,2425\times655\simeq318$ kg. Pour 78 passagers et avec une masse volumique de $0,75$ kg/L, cela donne **environ 5,4 L par passager pour 100 km**, soit environ $126\,\%$ de plus que la valeur constructeur de $2,4$ L.

Avec le débit arrondi de $0,19$ kg/s par moteur retenu par l'annexe, le même calcul donne $249$ kg et **4,25 L par passager pour 100 km**, soit environ $77\,\%$ de plus que la valeur constructeur. Le résultat de $2,1$ L suggéré par les opérations de l'annexe utilise $0,19\times655$ pour un seul moteur. Ce comptage est incompatible avec le facteur deux de la question 21. Le modèle à fraction d'air réactive fixée ne valide donc pas quantitativement la consommation de l'avion.

> [!PIEGE]
> Le calcul avec un seul turbopropulseur donne un résultat voisin de la donnée commerciale mais porte sur un système différent.

### Question 23

> [!INDICATION]
> Lire à 6 500 m les deux puissances pour chacun de trois Mach successifs.

> [!INDICATION]
> Le signe de la différence de puissance détermine celui de l'accélération en palier.

#### Solution

À 6 500 m, la comparaison doit se faire pour un même Mach. Sur les figures 14 et 15 on lit, à la précision graphique, environ $1,8$ MW disponibles contre $1,1$ MW résistants à Mach $0,4$, $2,2$ MW contre $2,15$ MW à Mach $0,5$, puis environ $2,8$ MW contre $3,6$ MW à Mach $0,6$. Les deux puissances décroissent avec l'altitude pour chaque Mach. À altitude fixée, la puissance résistante croît plus vite avec la vitesse que la puissance disponible. Comme $M_tV\dot V=P_{\rm prop}-P_{\rm rés}$ en palier, un excédent accélère l'avion et un déficit le ralentit. Leur croisement voisin de Mach $0,5$ rend compte d'une vitesse de croisière stable au réglage étudié.

![Figure 6 — Lectures approchées sur les figures 14 et 15 à la même altitude. L'excédent de puissance à Mach 0,4 devient un déficit à Mach 0,6.](figures/q23-puissances-en-croisiere.svg)

> [!METHODE]
> Des graphiques distincts peuvent avoir des échelles verticales différentes. Comparer des nombres avec unités.

## A3. Régulateur centrifuge du pas d'hélice

### Question 24

> [!INDICATION]
> Former le rapport poids/force centrifuge.

> [!INDICATION]
> Imaginer comment l'inclinaison de l'avion modifie la contribution de la pesanteur aux efforts.

#### Solution

L'effort de pesanteur représente environ $1,5/100=1,5\,\%$ de l'effort centrifuge. La position du régulateur est donc essentiellement sensible à la vitesse de rotation et peu sensible à l'orientation de la pesanteur lors d'un changement d'assiette. Cette approximation convient autour du régime considéré. À très basse vitesse, la force centrifuge, proportionnelle à $\omega_1^2$, s'effondre.

> [!METHODE]
> Une hiérarchie de forces autour d'un point de fonctionnement peut cesser de valoir au démarrage.

### Question 25

> [!INDICATION]
> Exprimer l'altitude du contact par les deux chemins disponibles.

> [!INDICATION]
> Projeter le vecteur de direction locale de la masselotte sur l'axe vertical avant de linéariser.

#### Solution

Par fermeture géométrique, l'altitude de $A_3$ calculée par $O_2$ est $z-c$, et par $B_3$ elle est $-a-b_3\sin\beta_3$. Ainsi
$$\sin\beta_3=(c-a-z)/b_3,\qquad \beta_3\simeq(c-a-z)/b_3.$$
L'origine de $z$ étant définie par le ressort à vide, elle n'impose pas $\beta_3=0$. En linéarisant, $\ddot\beta_3=-\ddot z/b_3$.

> [!PIEGE]
> La position du ressort à vide fixe une origine de déplacement, pas nécessairement une origine d'angle.

### Question 26

> [!INDICATION]
> Au pivot à axe parfait, le moment suivant l'axe de pivotement est nul.

> [!INDICATION]
> Écrire le moment cinétique relatif au pivot avec l'inertie transportée et compléter par l'accélération du pivot.

#### Solution

Notons $m=M_3$, $\beta=\beta_3$, $J=A_3+ma_3^2$ et $D=C_3-B_3-ma_3^2$ (ici $A_3,B_3,C_3$ désignent les composantes de l'inertie). Le moment du pivot parfait sur son axe est nul. Au point de contact, le bras $-b_3\vec j_3$ et l'effort $-Z_{23}\vec k$ donnent un moment axial $b_3 Z_{23}\cos\beta$.

Pour calculer le moment dynamique au pivot mobile, on utilise l'inertie transportée au pivot, de diagonale $(J,B_3+ma_3^2,C_3)$. La vitesse angulaire est $\dot\beta\vec i_1+\omega_1(\sin\beta\,\vec j_3+\cos\beta\,\vec k_3)$. La dérivée galiléenne du moment cinétique relatif au pivot projetée sur $\vec i_1$ est $J\ddot\beta+D\omega_1^2\sin\beta\cos\beta$ (terme gyroscopique). Il faut ajouter le moment d'entraînement $m\overrightarrow{B_3G_3}\mathbin{\times}\vec a_{B_3}$, avec $\vec a_{B_3}=-b\omega_1^2\vec j_1$. Le théorème demandé s'écrit donc
$$
b_3 Z_{23}\cos\beta
= J\ddot\beta+D\omega_1^2\sin\beta\cos\beta
     +ma_3b\omega_1^2\cos\beta.
$$
Au premier ordre, $b_3Z_{23}=J\ddot\beta+D\omega_1^2\beta+ma_3b\omega_1^2$.

![Figure 7 — Coupe de la masselotte dans le plan perpendiculaire au pivot. Le distributeur exerce au contact A₃ un effort vertical descendant sur la masselotte.](figures/q26-masselotte.svg)

> [!PIEGE]
> Le pivot tourne autour de l'arbre et possède une accélération dans le repère galiléen.

### Question 27

> [!INDICATION]
> Isoler le distributeur et projeter sur l'axe de la glissière.

> [!INDICATION]
> La symétrie impose deux actions de contact de même intensité.

#### Solution

Les deux contacts symétriques exercent chacun $+Z_{23}\vec k$ sur la pièce 2. La glissière parfaite ne transmet pas d'effort selon son axe et le poids a été négligé. Ainsi $M_2\ddot z=2Z_{23}-k_Rz$.

> [!PIEGE]
> Le distributeur reçoit la force opposée à celle qu'il exerce sur chaque masselotte.

### Question 28

> [!INDICATION]
> Remplacer l'effort de contact dans le bilan du distributeur par le moment calculé au pivot.

> [!INDICATION]
> Introduire ensuite la fermeture géométrique pour ne conserver que le déplacement, son accélération et les constantes.

#### Solution

On substitue dans le bilan précédent $b_3Z_{23}=-J\ddot z/b_3+D\omega_1^2(c-a-z)/b_3+M_3a_3b\omega_1^2$. Après regroupement, $K_1\ddot z+K_2z=K_3$ avec
$$
\begin{aligned}
K_1&=M_2+\frac{2J}{b_3^2},\\
K_2&=k_R+\frac{2D\omega_1^2}{b_3^2},\\
K_3&=\frac{2M_3a_3b\omega_1^2}{b_3}
      +\frac{2D\omega_1^2(c-a)}{b_3^2}.
\end{aligned}
$$
Ici $J=A_3+M_3a_3^2$, $D=C_3-B_3-M_3a_3^2$. Les trois termes sont des forces dans cette normalisation. Une multiplication des trois coefficients par une même constante donne la même équation.

> [!METHODE]
> Les coefficients d'inertie, de raideur et d'effort se contrôlent en vérifiant l'homogénéité de chaque terme.

### Question 29

> [!INDICATION]
> Soustraire la solution statique à l'équation pour isoler l'évolution libre.

> [!INDICATION]
> Chercher un terme proportionnel à la vitesse de déplacement.

#### Solution

Lorsque $K_1,K_2>0$, en posant $\xi=z-K_3/K_2$ on trouve $\ddot\xi+(K_2/K_1)\xi=0$. Le modèle sans frottement prédit des oscillations libres d'amplitude constante et une résonance idéale sans borne. Il ne décrit donc ni le temps d'établissement ni l'amortissement réel du régulateur. Les petits angles et le régime $\omega_1$ constant limitent également l'application aux grands transitoires.

> [!METHODE]
> Une oscillation libre de durée infinie signale l'absence de dissipation dans le modèle.

### Question 30

> [!INDICATION]
> Transformer la pulsation propre en cycles par seconde.

> [!INDICATION]
> Suivre le prélèvement de mouvement du réducteur de régulateur sur la figure 19.

#### Solution

À partir de l'équation numérique, $\omega_0=\sqrt{7\,080/0,0542}\simeq361$ rad/s et $f_0=\omega_0/(2\pi)\simeq57,5$ Hz. La turbine tourne à $18\,000/60=300$ Hz. Le réducteur 1 donne $300/15=20$ Hz à l'hélice. La prise du réducteur 2 est en aval du premier sur la figure 19, donc le régulateur tourne à $0,8\times20=16$ Hz, soit environ $101$ rad/s, en accord avec la valeur annoncée. Aucune des trois fréquences fondamentales ne coïncide avec $57,5$ Hz. Les excitations réelles peuvent inclure des harmoniques (par exemple $3\times20=60$ Hz, proche) et des modes structuraux. Le schéma seul n'en précise pas les amplitudes.

> [!PIEGE]
> Une comparaison directe entre rad/s, tours/minute et hertz n'a pas de sens.

## A4. Validation au point de croisière

### Question 31

> [!INDICATION]
> Au réglage demandé, relever le déplacement sur la première caractéristique.

> [!INDICATION]
> Reporter ce déplacement sur la deuxième courbe puis l'angle obtenu sur la troisième.

#### Solution

À $70\,\%$, le déplacement d'équilibre vaut $14,5/7\,080=2,05$ mm, en accord avec la figure 20. La figure 21 donne un pas de l'ordre de $45,5$ à $46^\circ$. La figure 22 indique alors une poussée totale proche de **14 à 15 kN** pour les deux hélices. L'échelle assez raide justifie de ne pas sur-préciser la dernière lecture.

> [!PIEGE]
> La figure de poussée additionne déjà les deux hélices.

### Question 32

> [!INDICATION]
> La puissance aérodynamique est le produit de la force longitudinale par la vitesse.

> [!INDICATION]
> Comparer la lecture graphique et l'estimation directe avec la même vitesse en mètres par seconde.

#### Solution

La loi de palier donne $F_{\rm rés}=KV_p^2/2=1,22\times153^2/2\simeq14,3$ kN. La figure 15 donne environ $2,15$ MW à Mach $0,5$ et 6 500 m, soit $F_{\rm rés}=P_{\rm rés}/V_p\simeq14,1$ kN. Ces estimations sont compatibles avec la poussée lue en question 31 et avec l'équilibre en palier, à quelques pour cent près. L'accord porte sur ce point de fonctionnement. Il ne valide pas les hypothèses de consommation ni la réponse transitoire.

> [!METHODE]
> L'accord de grandeurs mécaniques en un point ne valide pas tous les paramètres du modèle thermodynamique.

### Question 33

> [!INDICATION]
> Placer le mécanisme dans le repère du moyeu et identifier l'axe de pivotement d'une pale.

> [!INDICATION]
> Choisir une transformation rotation–translation, puis une biellette commandant toutes les pales par une même bague.

#### Solution

Fixons le stator d'un servomoteur au moyeu tournant. Son rotor entraîne une vis de pas $p$ en pivot dans le moyeu. Un écrou guidé en translation dans ce moyeu est empêché de tourner. Son avance axiale vaut $z=p\varphi/(2\pi)$ pour une rotation relative $\varphi$ de la vis. Une chape et une biellette relient cet écrou au levier excentré du pied de chaque pale. La pale pivote autour de son axe radial, ce qui change le pas. Toutes les biellettes sont entraînées par la même bague pour synchroniser les pales. Un capteur de position autorise l'asservissement et des butées bornent la course. Le schéma représente une pale et les liaisons dans le repère du moyeu.

![Figure 8 — Dans le moyeu, une vis tourne et l'écrou est guidé en translation. Une biellette et une manivelle font pivoter la pale autour de son axe radial.](figures/q33-pas-electromecanique.svg)

> [!METHODE]
> Une vis impose une translation de l'écrou uniquement si un guidage empêche sa rotation relative au moyeu.

## B1. Pile à combustible à membrane échangeuse de protons

### Question 34

> [!INDICATION]
> Commencer par conserver les atomes d’hydrogène.

> [!INDICATION]
> Utiliser ensuite les atomes d’oxygène et contrôler la charge.

#### Solution

Quatre protons apportent quatre atomes d’hydrogène, d’où deux molécules d’eau à droite. Il faut alors une molécule de dioxygène à gauche. La demi-équation cathodique s’écrit

$$\mathrm{O_2+4H^++4e^-\longrightarrow 2H_2O}.$$

Les charges se compensent et les deux coefficients demandés sont $a=1$ et $b=2$.

> [!METHODE]
> Une demi-équation doit conserver simultanément les éléments et la charge électrique.

### Question 35

> [!INDICATION]
> À quelle quantité d’eau correspond la grandeur molaire tabulée ?

> [!INDICATION]
> Compter les électrons avec la même normalisation que l’enthalpie libre.

#### Solution

Pour une mole d’eau formée, la réaction est $\mathrm{H_2+\tfrac12 O_2\longrightarrow H_2O}$ et deux moles d’électrons sont transférées. Avec la valeur $-237{,}1\,\mathrm{kJ\,mol^{-1}}$ rapportée à une mole d’eau, on obtient

$$E_{\rm eq}^0=-\frac{\Delta_rG^0}{n\mathcal F}=\frac{237{,}1\times10^3}{2\times96\,485}\,\mathrm V\simeq1{,}23\,\mathrm V.$$

Il y a une ambiguïté de normalisation dans le sujet. Pour l’équation globale **doublée** qu’il affiche, on doit doubler ensemble la grandeur de réaction ($-474{,}2\,\mathrm{kJ}$ par mole d’avancement) et le nombre d’électrons ($n=4$). Lire littéralement $-237{,}1\,\mathrm{kJ}$ par mole d’avancement de l’équation doublée conduirait à $0{,}61\,\mathrm V$, inférieur même à la tension mesurée aux faibles courants de la figure 25. La tension standard cohérente de la cellule est $1{,}23\,\mathrm V$.

> [!PIEGE]
> Doubler une équation de réaction double sa grandeur de réaction et le nombre d’électrons transférés. Le quotient qui donne la tension est invariant.

### Question 36

> [!INDICATION]
> Développer le polynôme pour une seule valeur de la densité de courant.

> [!INDICATION]
> Regrouper les puissances dans une ligne afin que chaque colonne corresponde à un coefficient.

#### Solution

Notons $J_i=J_{\rm PEMFC}[i]$ et $p=(p_0,\ldots,p_K)^{\mathsf T}$. La mesure $i$ donne $\widetilde U_i=p_0+p_1J_i+\cdots+p_KJ_i^K=r[i]^{\mathsf T}p$ avec $r[i]^{\mathsf T}=(1,J_i,J_i^2,\ldots,J_i^K)$. Chaque composante $r_k[i]$ est $J_i^k$, en convenant que le terme constant vaut toujours un, même à courant nul.

> [!METHODE]
> La dépendance peut être non linéaire en courant tout en restant linéaire par rapport aux coefficients recherchés.

### Question 37

> [!INDICATION]
> Faire écrire à chaque mesure une équation de même forme qu’en Q36.

> [!INDICATION]
> Compter séparément les indices de mesure et les indices de puissance.

#### Solution

En empilant les mesures d’indices $0$ à $G$, on construit une matrice $R$ de taille $(G+1)\times(K+1)$, avec $R_{ik}=J_i^k$. On a donc

$$\widetilde U=Rp,\qquad R=\begin{pmatrix}1&J_0&\cdots&J_0^K\\1&J_1&\cdots&J_1^K\\\vdots&\vdots&&\vdots\\1&J_G&\cdots&J_G^K\end{pmatrix}.$$

![Figure 9 — Trois mesures pour un polynôme de degré deux. Une ligne décrit un courant mesuré et une colonne suit une puissance de ce courant dans les trois mesures.](figures/q37-regresseurs.svg)

> [!PIEGE]
> Avec des indices qui commencent à zéro, la dernière mesure est la ligne G et la dernière puissance la colonne K.

### Question 38

> [!INDICATION]
> Quelle est la première colonne, quelle que soit la valeur de J ?

> [!INDICATION]
> Pour passer à la puissance suivante, réutiliser la colonne déjà calculée.

#### Solution

Dans la fonction de la figure 26, on peut remplir chaque colonne par multiplication de la précédente par le vecteur des densités mesurées. Le nom `POLYNOME_TAILLE` est celui de la signature du sujet et vaut $K+1$.

```python
MAT_REG_CONST = np.ones((len(D_COURANT), POLYNOME_TAILLE), dtype=float)
for k in range(1, POLYNOME_TAILLE):
    MAT_REG_CONST[:, k] = MAT_REG_CONST[:, k - 1] * D_COURANT
return MAT_REG_CONST
```

Il y a $K$ multiplications de vecteurs de longueur $G+1$, soit $K(G+1)$ multiplications scalaires. Avec l’initialisation, le coût en temps est $\Theta((G+1)(K+1))$, ainsi que la taille de la matrice renvoyée. L’initialisation à un traite aussi le polynôme constant.

> [!METHODE]
> Une multiplication vectorisée de longueur G + 1 effectue bien G + 1 multiplications scalaires.

### Question 39

> [!INDICATION]
> Développer le carré de la norme du résidu et regrouper les termes linéaires.

> [!INDICATION]
> Au minimum, une petite variation de n’importe quel coefficient n’a aucun effet au premier ordre.

#### Solution

Notons $U=(U_0,\ldots,U_G)^{\mathsf T}$ le vecteur mesuré. Pour inclure les $G+1$ mesures annoncées, on somme dès l’indice zéro. En développant le carré de la norme,

$$S(p)=(U-Rp)^{\mathsf T}(U-Rp)=U^{\mathsf T}U-2p^{\mathsf T}R^{\mathsf T}U+p^{\mathsf T}R^{\mathsf T}Rp.$$

Sa dérivée par rapport au vecteur $p$ est $2R^{\mathsf T}(Rp-U)$. Ainsi $\boxed{R^{\mathsf T}Rp=R^{\mathsf T}U}$. Ce point est un minimum car, pour tout $h$, le terme linéaire y est nul et $S(p+h)=S(p)+\|Rh\|^2$. Le minimum est unique si les colonnes de $R$ sont indépendantes, notamment pour au moins $K+1$ densités distinctes.

> [!PIEGE]
> L’inversibilité de la matrice normale requiert une hypothèse de rang. L’équation normale elle-même reste valable sans cette hypothèse.

### Question 40

> [!INDICATION]
> Transformer la densité de courant en courant total avec la surface active.

> [!INDICATION]
> Comparer la caractéristique affine à une chute de tension interne proportionnelle au courant.

#### Solution

Pour $K=1$, la loi ajustée est $U=p_0+p_1J$. Si $S$ désigne la surface active, $J=I/S$, où $I$ est le courant débité par la cellule. On reconnaît $U=E-rI$, avec $E=p_0$ et $r=-p_1/S$. La caractéristique décroissante donne $p_1<0$, donc $r>0$. Le modèle correspond à une source idéale de tension $E$ en série avec $r$. Si $J$ est exprimée en $\mathrm{A\,cm^{-2}}$, il faut exprimer $S$ en $\mathrm{cm^2}$.

> [!PIEGE]
> La pente en volts par densité de courant doit être divisée par la surface active pour devenir une résistance.

### Question 41

> [!INDICATION]
> Regarder les faibles densités de courant et la qualité du modèle dans la zone de fonctionnement.

> [!INDICATION]
> Séparer la qualité de l’ajustement aux mesures et celle de prédictions sur de nouvelles mesures.

#### Solution

Sur la figure 27, la droite suit la décroissance globale mais sous-estime nettement la tension près de $J=0$ (environ $0{,}95\,\mathrm V$ contre une mesure proche de $1{,}06\,\mathrm V$). Le modèle de degré sept suit mieux le coude initial et les changements de pente aux deux extrémités. On peut comparer l’erreur quadratique moyenne et la plus grande erreur absolue, puis contrôler les résidus dans chaque zone de courant, en particulier dans la zone d’exploitation visée.

Le modèle de degré sept contient huit paramètres, contre deux pour la droite. Son erreur d’ajustement ne peut qu’être inférieure ou égale sur les données qui ont servi au calcul. Des mesures indépendantes permettent de juger son pouvoir prédictif. Il faut aussi vérifier la décroissance, la plausibilité des extrapolations et le coût de simulation. La droite se traduit immédiatement en circuit à deux paramètres.

> [!METHODE]
> Un ajustement global peut masquer de grands écarts localisés près du courant nul.

### Question 42

> [!INDICATION]
> Entre quels deux nœuds le condensateur est-il branché ?

> [!INDICATION]
> Faire varier le courant à tension de source fixée. Vérifier les limites condensateur ouvert puis court-circuité.

#### Solution

Posons $R_s=R_a+R_c$, $R_0=R_i+R_s$ et $\tau=R_sC$. Sur la figure 28, le condensateur est en parallèle sur **l’ensemble** $R_a+R_c$. En régime de Laplace, son association avec ces résistances a pour impédance $R_s/(1+p\tau)$. La loi des mailles pour un courant $I_L$ débité vers la charge donne $V_L(p)=E_{\rm eq}/p-[R_i+R_s/(1+p\tau)]I_L(p)$ si la source constante est appliquée dès $t=0$ et que la tension initiale du condensateur est nulle.

À $E_{\rm eq}$ fixé, la fonction de transfert entre les **variations** de courant et de tension est donc

$$H(p)=\frac{\delta V_L(p)}{\delta I_L(p)}=-R_0\frac{1+p/\omega_z}{1+p/\omega_p},\qquad \omega_p=\frac1{R_sC},\quad \omega_z=\frac{R_0}{R_iR_sC}.$$

Une augmentation du courant abaisse la tension de sortie, ce qui explique le signe. À basse fréquence on retrouve $-R_0$ (condensateur ouvert) et à haute fréquence $-R_i$ (branche $R_s$ court-circuitée).

![Figure 10 — Impédance interne vue depuis les bornes de la cellule lorsque la source constante est neutralisée. À basse fréquence le courant traverse toutes les résistances. À haute fréquence le condensateur dérive la branche Ra + Rc.](figures/q42-impedance-cellule.svg)

> [!PIEGE]
> Pour une source constante non nulle, le rapport direct entre la tension absolue et le courant contient une contribution indépendante de l’entrée.

### Question 43

> [!INDICATION]
> Classer les deux pulsations avant de faire la somme des pentes.

> [!INDICATION]
> Inclure le signe de la fonction de transfert dans la phase et vérifier ses deux limites.

#### Solution

Comme $\omega_z/\omega_p=R_0/R_i>1$, le pôle agit avant le zéro. En rapportant le module à $1\,\Omega$ pour l’exprimer en décibels, les trois asymptotes sont

$$G_{\rm dB}\simeq\begin{cases}20\log_{10}(R_0/1\,\Omega),&\omega<\omega_p,\\20\log_{10}(R_0/1\,\Omega)-20\log_{10}(\omega/\omega_p),&\omega_p<\omega<\omega_z,\\20\log_{10}(R_i/1\,\Omega),&\omega>\omega_z.\end{cases}$$

Pour le signe négatif de Q42, une phase continue est $\phi=180^\circ+\arctan(\omega/\omega_z)-\arctan(\omega/\omega_p)$, les deux angles étant exprimés en degrés. Elle part de $180^\circ$, diminue, puis revient à $180^\circ$ (on peut soustraire $360^\circ$ à toute la courbe). Pour tracer la phase asymptotique usuelle, chaque arctangente est nulle jusqu’à un dixième de sa pulsation de coupure, monte de $45^\circ$ par décade jusqu’au décuple, puis reste à $90^\circ$. On **soustrait** cette rampe pour le pôle et on **ajoute** celle du zéro. Les deux transitions peuvent se recouvrir, car le rapport de leurs pulsations reste inconnu.

![Figure 11 — Exemple de tracé lorsque Ri vaut 2 Ω, Ra + Rc vaut 18 Ω et le rapport des pulsations de cassure vaut 10. Traits pleins pour les asymptotes et pointillés pour la réponse exacte.](figures/q43-bode-cellule.svg)

> [!METHODE]
> Les contributions de phase s’ajoutent en degrés, même lorsque leurs intervalles de transition se recouvrent.

## B2. Puissance massique et tension de la machine électrique

### Question 44

> [!INDICATION]
> Rappeler le produit couple-vitesse.

> [!INDICATION]
> Diviser par la masse et fixer le facteur limité thermiquement.

#### Solution

La puissance mécanique de rotation est $P=\Gamma\Omega$. Au point de base, avec le couple maximal, $P_b=\Gamma_{\max}\Omega_b$, d’où $P_b/M=(\Gamma_{\max}/M)\Omega_b$. À technologie de refroidissement et couple massique admissible donnés, accroître $\Omega_b$ augmente la puissance délivrée par kilogramme. Le plafond de couple massique vient ici de la capacité à évacuer la chaleur dissipée.

> [!METHODE]
> Une vitesse donnée en radians par seconde multipliée par un couple en newtons-mètres donne directement une puissance en watts.

### Question 45

> [!INDICATION]
> Repérer le sens de la chute de tension inductive quand le courant va de gauche à droite.

> [!INDICATION]
> Utiliser la convention de signe choisie pour le flux lié et remplacer une dérivée par la multiplication par la pulsation complexe.

#### Solution

Avec la référence de tension de la figure 29, $e$ est la **chute** de tension interne correspondant à la force contre-électromotrice. En orientant le flux lié $\phi_t$ selon la convention passive, $e(t)=\mathrm d\phi_t/\mathrm dt$. La force électromotrice induite comptée dans le sens de circulation du courant a le signe opposé, $-\mathrm d\phi_t/\mathrm dt$. Le flux $\phi_t$ est ici celui à courant nul, le flux inductif dû au courant étant compté dans $L_c$.

En suivant le courant de gauche à droite dans $L_c$, la loi des mailles est $v(t)=L_c\,\mathrm di/\mathrm dt+e(t)$. Pour des signaux sinusoïdaux avec la convention $e^{j\omega t}$,

$$\underline V(\omega)=j\omega L_c\underline I(\omega)+\underline E(\omega),\qquad \underline E=j\omega\underline\Phi_t.$$

> [!PIEGE]
> Le flux à courant nul et le flux propre de la phase décrivent deux termes distincts dans la tension totale.

### Question 46

> [!INDICATION]
> Quelle est la direction du terme inductif dans le plan complexe ?

> [!INDICATION]
> À flux fixé, relier l’amplitude de la force contre-électromotrice à la pulsation.

#### Solution

Comme $\underline E$ et $\underline I$ sont en phase, le terme inductif $j\omega_bL_c\underline I$ est en quadrature avec $\underline E$. Pour un flux rotorique sinusoïdal d’amplitude $\widehat\Phi_t$ fixe, Q45 donne $\widehat E=\omega_b\widehat\Phi_t$. La relation de Pythagore donne alors

$$\widehat V=\sqrt{\widehat E^2+(\omega_b L_c\widehat I)^2}=\omega_b\sqrt{\widehat\Phi_t^2+(L_c\widehat I)^2}.$$

À courant maximal et flux fixés, avec $\omega_b=p\Omega_b$, l’amplitude de tension requise augmente proportionnellement à la vitesse de base. Le gain de puissance massique de Q44 s’accompagne donc d’une tension d’alimentation plus grande et de contraintes accrues sur les isolants.

![Figure 12 — Diagramme de Fresnel avec le courant pris pour référence de phase. La tension inductive et la force contre-électromotrice forment les côtés perpendiculaires du triangle des tensions.](figures/q46-tensions-en-quadrature.svg)

> [!METHODE]
> Des amplitudes en quadrature s’additionnent par Pythagore.

## B3. Champ électrique et décharges entre conducteurs

### Question 47

> [!INDICATION]
> Choisir un cylindre de Gauss coaxial et expliciter l’hypothèse sur la longueur du fil.

> [!INDICATION]
> Calculer le flux à travers la surface latérale puis la charge d’un tronçon.

#### Solution

On assimile le conducteur à un cylindre très long devant les distances transverses étudiées, de charge totale par unité de longueur $\lambda=q\pi R^2$. L’hypothèse d’invariance suivant son axe néglige les effets de bord aux extrémités de la longueur $H$. Le champ est radial et de norme constante sur la surface latérale d’un cylindre de Gauss coaxial, de rayon $r\ge R$ et de longueur $h$. Le flux est nul à travers ses bases. Avec la permittivité du vide $\varepsilon_0$ pour l’air, $E_r\,2\pi rh=q\pi R^2 h/\varepsilon_0$, donc

$$\vec E(r)=\frac{qR^2}{2\varepsilon_0 r}\,\vec e_r,\qquad r\ge R.$$

Le champ est sortant si $q>0$. Pour un conducteur fini, cette expression vaut dans la région où les effets de bord sont négligeables.

> [!PIEGE]
> Le rayon de la surface d’intégration et celui du conducteur interviennent à des endroits différents.

### Question 48

> [!INDICATION]
> Repérer les positions des deux axes à partir des graduations portées sur les surfaces.

> [!INDICATION]
> Entre les deux conducteurs, dessiner le sens du champ d’une charge positive puis d’une charge négative.

#### Solution

La figure 31 place l’origine à la **surface** du conducteur positif, et $L$ à celle du conducteur négatif. Les axes des deux cylindres sont donc en $-R$ et $L+R$. Entre les deux surfaces, les distances aux axes sont $x+R$ et $L+R-x$. Les deux champs pointent vers le conducteur négatif. Avec $q>0$ pour la charge volumique du premier, leur superposition donne

$$\vec E(x)=\frac{qR^2}{2\varepsilon_0}\left(\frac1{R+x}+\frac1{R+L-x}\right)\vec u_x,\qquad 0\le x\le L.$$

On applique ici le modèle du sujet qui superpose les distributions cylindriques prescrites. Le profil est symétrique autour de $L/2$.

![Figure 13 — L’axe du cylindre positif est en −R et celui du cylindre négatif en L + R. Au point d’abscisse x entre les deux surfaces, les deux champs s’additionnent dans le même sens.](figures/q48-champs-entre-conducteurs.svg)

> [!METHODE]
> Une vérification de symétrie consiste à échanger les deux distances par le changement de variable x en L moins x.

### Question 49

> [!INDICATION]
> Quelle est la relation entre une variation de potentiel et la circulation du champ ?

> [!INDICATION]
> Sur le segment, les deux champs ont une composante positive.

#### Solution

Comme $\vec E=-\nabla V$, la circulation dans le sens des $x$ croissants est égale à la chute de potentiel du conducteur positif au conducteur négatif :

$$V(0)-V(L)=\int_0^L\vec E(x)\cdot\vec u_x\,\mathrm dx=\frac{qR^2}{2\varepsilon_0}\int_0^L\left(\frac1{R+x}+\frac1{R+L-x}\right)\mathrm dx.$$

L’expression est positive. Si l’on évalue l’intégrale, les deux termes donnent chacun $\ln((R+L)/R)$, d’où $V(0)-V(L)=(qR^2/\varepsilon_0)\ln(1+L/R)$.

> [!PIEGE]
> Inverser l’ordre des potentiels change le signe de la différence trouvée.

### Question 50

> [!INDICATION]
> Le graphique utilise un produit pression-distance dans une unité précisée sur l’axe.

> [!INDICATION]
> Placer les deux produits sur l’abscisse logarithmique puis remonter à la courbe.

#### Solution

L’abscisse de la figure 32 est le produit de la pression **en bars** par la distance **en millimètres**. Avec $d=0{,}1\,\mathrm{mm}$, on obtient $p d=0{,}1013\,\mathrm{bar\,mm}$ au sol et $p d=0{,}0264\,\mathrm{bar\,mm}$ à l’altitude considérée, en utilisant les pressions fournies. Sur ces axes logarithmiques, la figure donne environ $1{,}0\times10^3\,\mathrm V$ au sol et $5\times10^2\,\mathrm V$ à $6\,500\,\mathrm m$. Ce sont des lectures approchées de la courbe de claquage de l’air.

> [!METHODE]
> Sur une échelle logarithmique, le milieu d’une décade correspond à la moyenne géométrique de ses extrémités.

### Question 51

> [!INDICATION]
> Comparer 150 V aux deux seuils graphiques.

> [!INDICATION]
> Comparer ensuite la marge disponible à pression réduite et au sol.

#### Solution

Dans les conditions modélisées, $150\,\mathrm V$ reste en dessous des deux seuils. La tension de claquage du film d’air autour des conducteurs est cependant environ deux fois plus faible en altitude sur la branche de la figure considérée. Augmenter la tension d’alimentation pour atteindre de plus grandes puissances massiques réduit la marge disponible. Il faut alors tenir compte de la tension réellement appliquée entre spires voisines et dimensionner l’isolation pour les pressions, espacements et tensions de crête rencontrés.

> [!PIEGE]
> La courbe de Paschen a un minimum. Le sens de variation observé ici dépend de la branche sur laquelle se trouvent les deux situations.

## Conclusion

### Question 52

> [!INDICATION]
> Identifier une contrainte d’énergie et une contrainte de puissance distinctes.

> [!INDICATION]
> Relier le choix de la vitesse de rotation à une contrainte de fiabilité de l’isolation.

#### Solution

1. **Énergie embarquée et masse.** Le kérosène fournit environ $11{,}9\,\mathrm{kWh\,kg^{-1}}$ d’énergie chimique contre $0{,}10$ à $0{,}25\,\mathrm{kWh\,kg^{-1}}$ pour les batteries citées. Même en tenant compte des rendements de conversion, le stockage électrique pèse fortement sur la masse disponible pour les passagers et sur l’autonomie. L’hybridation se juge à l’échelle du vol régional complet.
2. **Puissance selon la phase de vol.** Le décollage demande un pic de puissance, la croisière une alimentation soutenue et l’approche comporte des variations rapides. Une pile à combustible pour une puissance relativement régulière et un stockage tampon pour les pointes permettent de répartir les sollicitations. Il faut dimensionner l’ensemble avec les profils de mission et leurs durées.
3. **Masse et fiabilité de l’entraînement.** Augmenter la vitesse de rotation améliore la puissance massique de la machine, mais exige une tension plus élevée. En altitude, la marge au claquage peut diminuer. Les gains de masse doivent donc être compatibles avec l’évacuation des pertes et la tenue des isolants sur tout le vol.

> [!METHODE]
> Une conclusion de dimensionnement gagne à relier chaque contrainte au résultat physique qui l’explique.

## Bilan

Sur un profil de vol, intégrer les puissances fournit des travaux et permet de comparer des sources d’énergie de masses différentes. Dans le moteur, suivre le débit d’un seul turbopropulseur jusqu’au dernier calcul évite les erreurs de comptage. Dans le régulateur, une géométrie, un bilan d’efforts et une loi de conversion du déplacement en angle suffisent à prédire un point d’équilibre à confronter à la traînée.

La partie électrique fait varier trois échelles. La caractéristique stationnaire donne la tension en fonction du courant, le circuit dynamique détermine l’effet d’une perturbation et l’isolant doit supporter la tension entre conducteurs à la pression de vol. Les seuils et les rendements nécessaires à la conception dépendent donc du régime retenu et de la grandeur effectivement mesurée.
