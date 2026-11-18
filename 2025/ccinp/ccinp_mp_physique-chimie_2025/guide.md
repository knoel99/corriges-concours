# CCINP MP — Physique-chimie 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

L'épreuve dure quatre heures sans calculatrice. Les 30 premières questions décrivent le stockage et le guidage des électrons dans le synchrotron SOLEIL, puis le rayonnement qu’ils émettent et la mesure interférométrique des longueurs d’onde. Les 14 dernières questions étudient le plomb, la solution d’acide sulfurique et le fonctionnement d’une batterie automobile.

Les bilans de mécanique et de chimie permettent de démarrer directement en Q1, Q6, Q31 et Q33. Les deux lectures optiques de Q29–Q30 et les courbes intensité-potentiel de Q39–Q41 demandent de revenir aux axes et aux unités. Gardez les valeurs intermédiaires avant l’arrondi final. La plupart des résultats demandent un chiffre significatif et Q40 en demande deux.

## Problème I — Le synchrotron SOLEIL

### Partie I — Généralités

### Question 1

> [!INDICATION]
> Écrivez la force sur une charge négative, puis comparez-la à l'opposé du gradient de l'énergie potentielle.

#### Solution

Le champ électrostatique est $\vec E=-\operatorname{grad}V$. La force sur l’électron est $\vec F=-e\vec E=e\operatorname{grad}V$. Comme $\vec F=-\operatorname{grad}E_p$, on obtient **$E_p=-eV$ à une constante près**.

> [!JURY]
> Le rapport attend la relation entre le champ et le potentiel, puis l'identification du signe de l'énergie potentielle de l'électron.

### Question 2

> [!INDICATION]
> Utilisez la conservation de l'énergie mécanique. Repérez le signe du potentiel final par rapport au potentiel initial.

#### Solution

La force électrostatique est conservative. Avec une vitesse initiale nulle, la conservation de l’énergie mécanique donne $E_c=e(V_f-V_i)$. Ainsi
$$
\boxed{V_f-V_i=\frac{E_c}{e}\simeq 1\times10^3\ \mathrm V.}
$$

### Question 3

> [!INDICATION]
> Calculez le rapport qui résulterait de l'expression classique et comparez la vitesse obtenue à la vitesse de la lumière.

#### Solution

L’expression classique impliquerait
$$
\frac vc=\sqrt{\frac{2E_c}{m_ec^2}}
\simeq \sqrt{\frac{2\times10^5}{5{,}1\times10^2}}.
$$
Elle donnerait **$v\simeq6\times10^9\ \mathrm{m\,s^{-1}}$**, soit environ vingt fois $c$. Ce résultat exclut l’emploi de la mécanique classique.

### Question 4

> [!INDICATION]
> Isolez le facteur de Lorentz dans la relation donnée. Utilisez la masse au repos dans l'unité qui évite une conversion en joules.

#### Solution

La relation relativiste donne
$$
\boxed{\gamma=1+\frac{E_c}{m_ec^2}\simeq2\times10^2.}
$$
Le rapport est calculé en exprimant $E_c$ et $m_ec^2$ en keV.

### Question 5

> [!INDICATION]
> Sur une période de révolution, comptez combien d'électrons traversent une section. Revenez ensuite à la définition de l'intensité.

#### Solution

Chaque électron traverse une section de l’anneau une fois par période $T=2\pi R/c$. En valeur absolue, la charge traversant la section en une période est $Ne$. Donc $i=Ne/T$, d’où
$$
\boxed{N=\frac{2\pi R i}{e c}\simeq3\times10^{12}\ \text{électrons}.}
$$

### Question 6

> [!INDICATION]
> Traitez le gaz résiduel comme un gaz parfait et convertissez la pression en pascals.

#### Solution

À cette très faible pression, le dihydrogène est assimilé à un gaz parfait. Avec $n$ le nombre de molécules par unité de volume, $PV=(nV/N_A)RT$. Comme $P=6\times10^{-8}\ \mathrm{Pa}$,
$$
n=\frac{PN_A}{RT}=\frac{6\times10^{-8}\times6{,}0\times10^{23}}{8{,}3\times298}
\simeq\boxed{1\times10^{13}\ \mathrm{m^{-3}}}.
$$
La valeur avant arrondi est $1{,}46\times10^{13}\ \mathrm{m^{-3}}$.

> [!JURY]
> Utilisez le nombre de molécules par unité de volume. La pression donnée en bar doit être convertie en pascals.

### Question 7

> [!INDICATION]
> Isolez la dimension de $\sigma$ en utilisant le fait que $N$ est un effectif.

#### Solution

L'effectif $N$ et sa variation sont sans dimension. Puisque $[n]=L^{-3}$ et $[\mathrm dx]=L$, on a $[\sigma]=1/(L^{-3}L)=L^2$. La section efficace a donc la dimension d'une aire et s'exprime en $\mathrm{m^2}$.

### Question 8

> [!INDICATION]
> Reliez la distance parcourue au temps, puis traduisez une diminution de $37\,\%$ en fraction restante.

#### Solution

À la vitesse $c$, on a $\mathrm dx=c\,\mathrm dt$. L'intégration de $\mathrm dN/N=-\sigma nc\,\mathrm dt$ avec $N(0)=N_0$ donne $N(t)=N_0\exp(-\sigma nc\,t)$. Comme $N(\tau)=0{,}63N_0$,
$$
\boxed{\tau=\frac{-\ln(0{,}63)}{\sigma nc}=\frac{0{,}46}{\sigma nc}.}
$$

### Question 9

> [!INDICATION]
> Convertissez les centimètres carrés et gardez la valeur non arrondie de $n$. Identifiez le mécanisme qui peut compenser les pertes.

#### Solution

La conversion donne $\sigma=2{,}0\times10^{-27}\ \mathrm{m^2}$. Avec la formule de Q8 et $n=1{,}46\times10^{13}\ \mathrm{m^{-3}}$, on obtient $5{,}3\times10^4\ \mathrm s$, soit **$5\times10^4\ \mathrm s$** à un chiffre significatif, de l'ordre d'une quinzaine d'heures. Puisque le courant à vitesse et géométrie fixées est proportionnel à $N$, des injections régulières d'électrons depuis le booster compensent les pertes et maintiennent le courant près de sa consigne.

### Partie II — Éléments magnétiques

### Question 10

> [!INDICATION]
> Identifiez l'instrument qui mesure une composante du champ magnétique. Précisez la position et l'orientation de sa sonde.

#### Solution

On utilise **un teslamètre et sa sonde**. On place la sonde au point étudié, on règle le zéro en l’absence du champ à mesurer, puis on l’oriente pour mesurer la composante suivant son axe sensible. Avec une sonde monoaxe, trois mesures suivant des axes orthogonaux donnent le vecteur champ.

### Question 11

> [!INDICATION]
> Calculez la puissance de la force magnétique pour décider si la norme de la vitesse varie.

> [!INDICATION]
> Projetez le principe fondamental sur la normale à la trajectoire. Reliez ensuite pulsation, rayon et vitesse.

#### Solution

La force $\vec F=-e\vec v\times\vec B$ est orthogonale à la vitesse. Son travail est nul et la norme de la vitesse reste $v_0$. Elle est également orthogonale au champ, de sorte que la vitesse, initialement perpendiculaire à celui-ci, le reste. L’accélération normale vaut $v_0^2/R_B$ et la force a pour norme $e v_0B_0$. Ainsi
$$
\begin{aligned}
B_0&=\boxed{\frac{m_ev_0}{eR_B}=\frac{p}{eR_B}},\\
\omega_B&=\boxed{\frac{v_0}{R_B}=\frac{eB_0}{m_e}}.
\end{aligned}
$$

### Question 12

> [!INDICATION]
> Combinez la relation entre rayon et quantité de mouvement avec l'approximation ultrarelativiste.

#### Solution

Dans le régime ultrarelativiste, l’énergie totale est assimilable à $E_c$ dans la relation $p\simeq E/c$. On obtient
$$
\boxed{B_0\simeq \frac{E_c/e}{cR_B}\simeq2\ \mathrm T.}
$$
On a utilisé $E_c/e=2{,}7\times10^9\ \mathrm V$.

### Question 13

> [!INDICATION]
> Pour chaque réflexion, demandez si les flèches de courant sont conservées ou inversées. Appliquez la règle appropriée pour un champ axial.

> [!INDICATION]
> Sur chaque axe, repérez les deux faces de bobines les plus proches et déterminez leur polarité avec la main droite.

#### Solution

Le champ magnétique est un vecteur axial. Dans un plan de symétrie des courants, il est normal au plan. Dans un plan d’antisymétrie des courants, il appartient au plan.

Le plan $xOy$ est plan d’antisymétrie des courants. Chaque bobine est alors réfléchie sur elle-même en inversant le courant orienté. Donc $\vec B$ appartient à $xOy$ en tout point de ce plan.

Les plans $xOz$ et $yOz$ sont des plans de symétrie des courants.

On le vérifie en réfléchissant les bobines de la figure 2b et en suivant le sens de leurs courants.

Ainsi, sur $Ox$, le champ est dirigé suivant $Oy$ et, sur $Oy$, il est dirigé suivant $Ox$.

À l’origine, les deux contraintes s’appliquent simultanément, d’où **$\vec B(O)=\vec 0$**.

Par la règle de la main droite, les faces tournées vers l’origine des bobines du haut à gauche et du bas à droite sont des pôles nord. Les deux autres sont des pôles sud. Du côté $x>0$, la bobine du bas est nord et celle du haut sud, ce qui oriente le champ suivant $+\vec e_y$. Du côté $y>0$, le nord est à gauche et le sud à droite, ce qui oriente le champ suivant $+\vec e_x$. Les sens sont inversés sur les demi-axes négatifs par symétrie.

### Question 14

> [!INDICATION]
> Écrivez les deux équations locales, en distinguant la zone au voisinage de l'origine de l'intérieur des bobines.

> [!INDICATION]
> Calculez les dérivées croisées puis utilisez la valeur du champ en O.

#### Solution

En régime stationnaire, les équations locales sont $\operatorname{div}\vec B=0$ et $\operatorname{rot}\vec B=\mu_0\vec j$. Au voisinage de l’origine, hors des bobines, $\vec j=\vec0$. Dans le champ proposé, la divergence est nulle. La seule composante éventuellement non nulle du rotationnel est $\partial_x B_y-\partial_y B_x=K-K=0$. Comme $\vec B(O)=K'(\vec e_x+\vec e_y)=\vec0$ par Q13, **$K'=0$**.

### Question 15

> [!INDICATION]
> Calculez d'abord le champ de chaque côté de l'origine sur l'axe étudié. Déduisez le sens de la force à partir du produit vectoriel et du signe de la charge.

#### Solution

Sur $Oy$, $\vec B=Ky\vec e_x$, d’où
$$
\vec F=-e v_0 \vec e_z\times (Ky\vec e_x)=-e v_0 K y\,\vec e_y .
$$
En $A$, le champ pointe vers $+x$ et la force vers $-y$. En $B$, le champ pointe vers $-x$ et la force vers $+y$.

![Figure 1 — Sur Oy, le champ change de sens entre A et B et les deux forces pointent vers l’axe central.](figures/q15-focalisation.svg)

**Les forces sont dirigées vers le centre du faisceau en $y$.**

### Question 16

> [!INDICATION]
> Recommencez le produit vectoriel dans l'autre plan. Cherchez ensuite une rotation du quadrupôle qui échange les deux directions transverses.

#### Solution

Sur $Ox$, $\vec B=Kx\vec e_y$, donc $\vec F=e v_0 Kx\vec e_x$. Elle éloigne chaque électron de l’axe en $x$. Un second quadrupôle tourné de $90^\circ$ autour de l’axe du faisceau échange les plans focalisant et défocalisant. **Une succession de quadrupôles alternés, de forces et d’espacements ajustés, permet de confiner le faisceau dans les deux plans.**

### Partie III — Rayonnement

### Question 17

> [!INDICATION]
> Distinguez ce qui dépend de la direction d'observation de ce qui décrit l'évolution du champ électrique dans le temps.

#### Solution

Un rayonnement est **anisotrope** si sa puissance surfacique dépend de la direction d’observation. Il est **polarisé** si les variations temporelles de la direction de son champ électrique transverse présentent une organisation déterminée, par exemple une direction fixe pour une polarisation rectiligne.

### Question 18

> [!INDICATION]
> Choisissez le plan qui contient l'axe du dipôle et le point d'observation.

> [!INDICATION]
> Comparez les règles de transformation d'un vecteur polaire et d'un vecteur axial. Utilisez ensuite l'invariance par rotation.

#### Solution

Tout plan méridien passant par $Oz$ est plan de symétrie de la distribution de charges et de courants. Le champ électrique, vecteur polaire, est dans ce plan. Le champ magnétique, vecteur axial, est normal à ce plan. Au point considéré, cela donne **$E_\varphi=B_r=B_\theta=0$**. L’invariance de la distribution par rotation autour de $Oz$ rend les composantes dans la base sphérique indépendantes de $\varphi$.

### Question 19

> [!INDICATION]
> Dérivez deux fois la position, puis sommez les positions pondérées par les charges.

> [!INDICATION]
> Distinguez la norme instantanée d'un vecteur sinusoïdal et son amplitude.

#### Solution

En dérivant deux fois la position de l’électron, on obtient $\vec a(t)=-l\omega^2\cos(\omega t)\vec e_z$. Le moment dipolaire est la somme des positions pondérées par les charges. Ici,
$$
\vec p(t)=-el\cos(\omega t)\,\vec e_z.
$$
Son amplitude est $p_0=el$. Dans l’expression demandée, $a=l\omega^2$ désigne l’amplitude de l’accélération. La norme instantanée vaut $a|\cos(\omega t)|$. **$p_0=ea/\omega^2$.**

### Question 20

> [!INDICATION]
> Repérez les longueurs caractéristiques du rayonnement. Interprétez la différence entre l'heure d'émission et l'heure de réception.

#### Solution

La zone de rayonnement se situe loin de la source et à une distance grande devant la longueur d’onde $\lambda=2\pi c/\omega$.

Le champ en $1/r$ y domine les termes proches.

Le terme $r/c$ est le temps nécessaire pour parcourir la distance $r$ à la vitesse $c$ dans le vide.

**Le champ observé à l’instant $t$ dépend de la source à l’instant retardé $t-r/c$.**

### Question 21

> [!INDICATION]
> Calculez le produit vectoriel de la direction de propagation avec le champ électrique.

> [!INDICATION]
> Pour les unités, commencez par celle du coefficient du champ électrique, puis vérifiez séparément l'effet du facteur supplémentaire dans le champ magnétique.

#### Solution

Les champs sont transverses et, puisque $\vec e_r\times\vec e_\theta=\vec e_\varphi$, ils vérifient
$$
\boxed{\vec B=\frac{\vec e_r\times\vec E}{c}.}
$$
Sur une petite région loin de la source, la direction radiale et l’amplitude varient peu. Cette relation et la phase retardée donnent la structure locale d’une onde plane progressive dans la direction $\vec e_r$. Le champ électrique oscille parallèlement à $\vec e_\theta$, donc la polarisation est rectiligne.

Pour vérifier les unités, on part de
$$
\begin{aligned}
[\mu_0]&=\mathrm{kg\,m\,s^{-2}\,A^{-2}},\\
[p_0]&=\mathrm{A\,s\,m},\\
[\omega]&=\mathrm{s^{-1}}.
\end{aligned}
$$
Le facteur $\mu_0p_0\omega^2/r$ a donc l’unité $\mathrm{kg\,m\,s^{-3}\,A^{-1}}$, soit $\mathrm{V\,m^{-1}}$. Le facteur supplémentaire $1/c$ dans $\vec B$ donne $\mathrm{kg\,s^{-2}\,A^{-1}}$, soit le tesla.

### Question 22

> [!INDICATION]
> Utilisez le produit vectoriel des deux champs. Après moyenne temporelle, examinez la dépendance angulaire.

#### Solution

Le vecteur de Poynting vaut $\vec\Pi=\vec E\times\vec B/\mu_0$. Avec la relation de Q21,
$$
\vec\Pi(r,\theta,t)=
\frac{\mu_0 p_0^2\omega^4}{16\pi^2cr^2}\sin^2\theta
\cos^2\!\bigl(\omega(t-r/c)\bigr)\vec e_r.
$$
La moyenne de $\cos^2$ vaut $1/2$. À distance fixée, la puissance surfacique moyenne est maximale pour $\theta=\pi/2$, dans toutes les directions perpendiculaires à l’axe du dipôle. Avec $p_0=ea/\omega^2$ et $\mu_0\varepsilon_0c^2=1$,
$$
\boxed{\|\langle\vec\Pi\rangle\|_{\max}
=\frac{e^2a^2}{32\pi^2\varepsilon_0 c^3 r^2}.}
$$

### Partie IV — Directivité du rayonnement synchrotron

### Question 23

> [!INDICATION]
> Repérez la direction qui rend le dénominateur le plus petit. Comparez les deux maxima à distance et accélération comparables.

#### Solution

Dans la formule relativiste, $1-(v/c)\cos\theta$ est minimal quand $\cos\theta=1$. Le maximum est donc dans la direction et le sens de la vitesse. À distance et amplitude d’accélération comparables, **le rapport des maxima relativiste et dipolaire est $(1-v/c)^{-4}$**. Il est très supérieur à $1$ lorsque $v$ est proche de $c$. Le rayonnement est fortement concentré vers l’avant.

### Question 24

> [!INDICATION]
> Additionnez le vecteur de vitesse du référentiel et celui de la particule émise transversalement.

> [!INDICATION]
> Associez le demi-plan avant au cône transformé. Le cas où la vitesse de la source est la plus grande demande d'examiner aussi les directions initialement vers l'arrière.

#### Solution

Avec la composition galiléenne, $\vec v'_p=\vec v_p+v\vec e_x$. Pour une émission à $\theta=\pi/2$, $\vec v_p=v_p\vec e_y$. Par conséquent,
$$
\begin{aligned}
\vec v'_p&=\boxed{v\vec e_x+v_p\vec e_y},\\
\theta'&=\boxed{\arctan(v_p/v)}.
\end{aligned}
$$

![Figure 2 — Composition galiléenne pour une émission transverse. Les deux composantes donnent la vitesse mesurée et son angle avec Ox.](figures/q24-vitesses.svg)

Les particules émises dans le demi-plan avant sont dans ce cône après composition.

En effet, leur composante suivant $x$ est au moins $v$ et la composante transverse a un module au plus $v_p$.

**Cela représente au moins la moitié des particules, et exactement la moitié si $v_p\geq v$**, cas pertinent pour la comparaison avec les photons.

Dans ce cas, la direction du vecteur somme parcourt les angles dans le même ordre que la direction initiale, car l’origine est à l’intérieur du cercle des extrémités de $\vec v'_p$ ou sur son bord.

Pour $v_p<v$, posons $\rho=v/v_p>1$.

Pour une émission dans le demi-plan arrière, posons $u=-\cos\theta>0$.

La condition d’appartenance au cône devient $\rho\sqrt{1-u^2}\leq\rho-u$.

En élevant au carré les membres positifs, elle équivaut à $u\geq2\rho/(1+\rho^2)$.

La proportion totale est alors
$$
\boxed{\frac12+\frac1\pi\arccos\left(\frac{2\rho}{1+\rho^2}\right).}
$$

> [!PIEGE]
> L'image du demi-plan avant entre dans le cône. L'égalité avec une moitié de toutes les particules utilise une hypothèse sur les vitesses dans le modèle galiléen.

### Question 25

> [!INDICATION]
> Comparez la norme du vecteur galiléen à la propriété relativiste de la vitesse de la lumière.

#### Solution

Dans le vide, la vitesse d’un photon a pour norme $c$ dans tout référentiel inertiel. La composition galiléenne donnerait pour un photon émis transversalement la norme $\sqrt{c^2+v^2}>c$. **La transformation relativiste des vitesses est indispensable.**

### Question 26

> [!INDICATION]
> Insérez d'abord les composantes de départ correspondant à une émission transverse.

> [!INDICATION]
> Examinez le rapport transverse sur parallèle et justifiez l'approximation de petit angle.

#### Solution

Pour un photon, $v_p=c$. À l’émission transverse, les formules données donnent $v'_{p\parallel}=v$ et $v'_{p\perp}=c/\gamma$. La transformation conserve l’ordre des directions : en divisant la composante parallèle par $c$, on trouve $\cos\theta_{\mathcal R'}=(\cos\theta+v/c)/(1+(v/c)\cos\theta)$, croissante en $\cos\theta$. Ainsi, la direction transverse délimite bien l’image du demi-plan avant.

Comme $v\simeq c$ et $\gamma\gg1$,
$$
\tan\theta'=\frac{c}{\gamma v}\simeq\frac1\gamma.
$$
Le petit angle vérifie donc **$\theta'\simeq1/\gamma\simeq2\times10^{-5}\ \mathrm{rad}$**. La moitié du rayonnement est concentrée dans un cône très étroit.

### Partie V — Principe de la spectrométrie d’absorption

### Question 27

> [!INDICATION]
> Placez la séparatrice, les miroirs, puis la lentille et son foyer image.

> [!INDICATION]
> Suivez au moins deux rayons parallèles dans les deux bras, à l'aller et au retour vers le même port.

#### Solution

La séparatrice à $45^\circ$ partage le faisceau collimaté en deux faisceaux parallèles dans deux bras orthogonaux. Après réflexion à incidence normale sur les miroirs, une partie de chaque faisceau revient vers le port de sortie. Une lentille convergente rassemble ces deux faisceaux au foyer image $F'$, où se trouve la photodiode.

![Figure 3 — Michelson réglé en lame d’air. Deux faisceaux parallèles suivent les bras orthogonaux, se recombinent vers la lentille et atteignent la photodiode placée au foyer image.](figures/q27-michelson.svg)

### Question 28

> [!INDICATION]
> Reliez l'épaisseur traversée à la différence de marche aller-retour.

> [!INDICATION]
> Dans la somme de deux ondes, comparez les intensités dans les deux bras pour savoir quand les minima peuvent s'annuler.

#### Solution

En incidence normale, la différence de marche vaut $\delta=2d$. Pour deux faisceaux de même intensité qui se superposent avec la même polarisation,
$$
\boxed{I(F')=\frac{I_{\max}}2
 \left[1+\cos\left(\frac{4\pi d}{\lambda_m}\right)\right].}
$$
Le contraste est maximal lorsque les deux faisceaux recombinés ont la même intensité. Dans un Michelson idéal, chacun subit une réflexion et une transmission à la même séparatrice, et les miroirs ont des réflectivités égales. Cette symétrie équilibre les voies.

### Question 29

> [!INDICATION]
> Mesurez plusieurs périodes entre deux maxima éloignés et divisez par leur nombre.

> [!INDICATION]
> Évaluez l'incertitude sur chacun des deux temps lus, puis propagez-la jusqu'à la longueur d'onde.

#### Solution

Avec $d=v_0t$, la période de l’interférogramme vaut $T_m=\lambda_m/(2v_0)$. Sur la figure 5, vingt périodes séparent le maximum à l’origine du maximum situé vers $7{,}7\ \mathrm s$. Cette lecture donne environ $0{,}39\ \mathrm s$ par période avant arrondi. D’où
$$
\boxed{\lambda_m=2v_0T_m\simeq5\times10^{-7}\ \mathrm m.}
$$
Pour estimer l’incertitude de lecture, prenons une demi-largeur de $0{,}1\ \mathrm s$ sur la position de chaque maximum extrême, indépendante et à distribution uniforme. En l’absence d’incertitude indiquée sur $v_0$,
$$
u(\lambda_m)=\frac{2v_0}{20}\sqrt{2}\,
\frac{0{,}1\ \mathrm s}{\sqrt3}.
$$
On trouve **$u(\lambda_m)\simeq6\times10^{-9}\ \mathrm m$** avec cette convention de lecture.

> [!JURY]
> Une mesure sur plusieurs périodes réduit l'effet de la lecture de chaque extrémité. L'estimation finale doit préciser la résolution adoptée.

### Question 30

> [!INDICATION]
> Lisez la durée de décroissance de l'enveloppe, puis convertissez-la en différence de marche.

> [!INDICATION]
> Reliez cette différence de marche au temps de cohérence et utilisez la variation de la relation entre fréquence et longueur d'onde.

#### Solution

Sur la figure 6b, l’amplitude de l’enveloppe autour du niveau moyen est de l’ordre de la moitié de sa valeur initiale après environ $30\ \mathrm s$. Si $t_{\mathrm{env}}$ désigne cette durée de balayage, la différence de marche correspondante est
$$
\boxed{L_c\simeq2v_0 t_{\mathrm{env}}\simeq4\times10^{-5}\ \mathrm m.}
$$
Le temps de cohérence physique vaut $\tau_c\simeq L_c/c$, et diffère du temps de balayage. Avec $\nu=c/\lambda$, pour une bande étroite, $\Delta\nu\simeq(c/\lambda_m^2)\Delta\lambda$. En utilisant $\Delta\nu\,\tau_c\simeq1$ et la lecture de Q29 avant arrondi,
$$
\boxed{\Delta\lambda\simeq\frac{\lambda_m^2}{L_c}\simeq7\times10^{-9}\ \mathrm m.}
$$

## Problème 2 — La batterie au plomb

### Question 31

> [!INDICATION]
> Utilisez le numéro atomique, le nombre de masse et la neutralité électrique de l'atome.

#### Solution

Le numéro atomique $Z=82$ donne **82 protons**. Le noyau contient $A=207$ nucléons, donc $207-82=\mathbf{125}$ **neutrons**. L'atome est neutre et possède **82 électrons**.

### Question 32

> [!INDICATION]
> Écrivez une équation pour la somme des proportions et une pour la moyenne pondérée des masses.

#### Solution

Deux isotopes d’un même élément ont **le même nombre de protons et des nombres de neutrons différents**. Les pourcentages totalisent $100$ et la masse molaire moyenne est la moyenne pondérée des masses molaires isotopiques. En assimilant ces dernières à leur nombre de masse en $\mathrm{g\,mol^{-1}}$, on obtient
$$
\boxed{\begin{cases}
x+y+22+52=100,\\
204 x+206 y+207\times22+208\times52=100\times207{,}2.
\end{cases}}
$$

> [!JURY]
> Le rapport relève deux oublis fréquents, la définition du mot isotope et l'équation qui utilise les nombres de masse.

### Question 33

> [!INDICATION]
> Pondérez chaque site par le nombre de mailles qui le partagent, puis convertissez le paramètre de maille avant de le mettre au cube.

#### Solution

La maille conventionnelle comporte huit sites aux sommets et six sites au centre des faces. Chaque sommet est commun à huit mailles et chaque face à deux mailles. Cela représente $8/8+6/2=4$ atomes par maille.

![Figure 4 — Maille cubique à faces centrées du plomb. Les sites sont aux huit sommets et au centre des six faces.](figures/q33-cfc.svg)

Une maille a une masse $4M_{\mathrm{Pb}}/N_A$ et un volume $a^3$. Avec $a=5{,}0\times10^{-10}\ \mathrm m$ et $M_{\mathrm{Pb}}=0{,}207\ \mathrm{kg\,mol^{-1}}$,
$$
\rho=\frac{4M_{\mathrm{Pb}}}{N_Aa^3}\simeq1{,}1\times10^4\ \mathrm{kg\,m^{-3}}
\simeq\boxed{1\times10^4\ \mathrm{kg\,m^{-3}}}
$$
à un chiffre significatif.

### Question 34

> [!INDICATION]
> Raisonnez sur un kilogramme de solution et estimez son volume à partir des volumes des deux constituants.

#### Solution

Dans $1{,}00\ \mathrm{kg}$ de solution, on a $0{,}33\ \mathrm{kg}$ de $\mathrm{H_2SO_4}$ et $0{,}67\ \mathrm{kg}$ d'eau. La quantité d'acide vaut $0{,}33/0{,}098\simeq3{,}37\ \mathrm{mol}$.

En supposant les volumes additifs et en prenant les masses volumiques $1{,}8$ et $1{,}0\ \mathrm{kg\,L^{-1}}$, on estime
$$
V\simeq\frac{0{,}33}{1{,}8}+\frac{0{,}67}{1{,}0}=0{,}853\ \mathrm L,\qquad
C\simeq\frac{3{,}37}{0{,}853}\simeq\boxed{4\ \mathrm{mol\,L^{-1}}}.
$$
L'additivité des volumes est une approximation pour un mélange aussi concentré.

> [!JURY]
> Le jury relève que le volume d'eau seul ne suffit pas dans une solution aussi concentrée.

### Question 35

> [!INDICATION]
> Écrivez un bilan qui libère deux ions oxonium par molécule d'acide dans le modèle proposé.

#### Solution

Dans le modèle des deux acidités fortes,
$$
\mathrm{H_2SO_4}(aq)+2\mathrm{H_2O}(l)\longrightarrow
2\mathrm{H_3O^+}(aq)+\mathrm{SO_4^{2-}}(aq).
$$
Ainsi $[\mathrm{H_3O^+}]\simeq2C=8\ \mathrm{mol\,L^{-1}}$ et $\mathrm{pH}\simeq-\log_{10}(8)=\boxed{-0{,}9}$. Un pH négatif est possible et traduit ici la forte acidité. L'approximation des activités par les concentrations et celle de deux acidités fortes limitent la portée quantitative de la valeur obtenue.

### Question 36

> [!INDICATION]
> Écrivez le quotient de la réaction de dissolution et imposez l'égalité au produit de solubilité lorsque le solide apparaît.

#### Solution

Pour $\mathrm{PbSO_4}(s)\rightleftharpoons\mathrm{Pb^{2+}}(aq)+\mathrm{SO_4^{2-}}(aq)$, à la saturation, dans l'approximation des activités du sujet,
$$
K_s=\frac{[\mathrm{Pb^{2+}}][\mathrm{SO_4^{2-}}]}{(C^0)^2}.
$$
Avec $[\mathrm{SO_4^{2-}}]\simeq4\ \mathrm{mol\,L^{-1}}$, le seuil est **$[\mathrm{Pb^{2+}}]_{\rm sat}\simeq4\times10^{-9}\ \mathrm{mol\,L^{-1}}$**. Au-delà de ce seuil en plomb(II) apporté, l'excédent précipite sous forme de $\mathrm{PbSO_4}(s)$. Dès que la quantité apportée excède nettement le seuil, le solide est la forme prépondérante et la concentration dissoute reste voisine du seuil tant que le sulfate est en large excès.

### Question 37

> [!INDICATION]
> Équilibrez les atomes puis les charges en milieu acide. Dans le bilan, éliminez les électrons échangés entre les deux électrodes.

#### Solution

Pendant la décharge, le plomb est oxydé à l’anode et le dioxyde de plomb est réduit à la cathode.
$$
\begin{aligned}
\text{Anode}\quad&
\mathrm{Pb}(s)+\mathrm{SO_4^{2-}}(aq)
\longrightarrow \mathrm{PbSO_4}(s)+2e^-,\\
\text{Cathode}\quad&
\mathrm{PbO_2}(s)+\mathrm{SO_4^{2-}}(aq)+4\mathrm{H^+}(aq)+2e^-
\longrightarrow\mathrm{PbSO_4}(s)+2\mathrm{H_2O}(l).
\end{aligned}
$$
Les électrons se simplifient dans le bilan.
$$
\boxed{\begin{aligned}
\mathrm{Pb}(s)+\mathrm{PbO_2}(s)+2\mathrm{SO_4^{2-}}(aq)+4\mathrm{H^+}(aq)
&\longrightarrow 2\mathrm{PbSO_4}(s)+2\mathrm{H_2O}(l).
\end{aligned}}
$$

À la recharge, le générateur impose la transformation inverse. Le bilan devient
$$
\boxed{2\mathrm{PbSO_4}(s)+2\mathrm{H_2O}(l)\longrightarrow
\mathrm{Pb}(s)+\mathrm{PbO_2}(s)+2\mathrm{SO_4^{2-}}(aq)+4\mathrm{H^+}(aq).}
$$

> [!JURY]
> Le jury invite à identifier l'anode avec l'oxydation et la cathode avec la réduction avant de sommer les demi-équations.

### Question 38

> [!INDICATION]
> Appliquez la loi de Nernst dans le sens réduction pour les deux couples, puis soustrayez les potentiels.

> [!INDICATION]
> Repérez où intervient la combinaison de concentrations fournie. Déterminez l'association qui additionne les tensions.

#### Solution

Posons $s=[\mathrm{SO_4^{2-}}]/C^0$ et $a=[\mathrm{H^+}]/C^0$. L’activité des solides purs et celle de l’eau solvant sont prises égales à $1$. La loi de Nernst pour les deux couples, écrits dans le sens de la réduction, donne
$$
\begin{aligned}
E_1&=E_1^\circ-\frac{RT}{2F}\ln s,\\
E_2&=E_2^\circ+\frac{RT}{2F}\ln(sa^4).
\end{aligned}
$$
La fém est donc
$$
\begin{aligned}
e&=E_2-E_1\\
&=E_2^\circ-E_1^\circ+\frac{RT}{F}\ln(sa^2).
\end{aligned}
$$
Avec $sa^2=100$, le terme logarithmique vaut $2(RT/F)\ln10$. On trouve **$e\simeq2\ \mathrm V$ à un chiffre significatif**. Avant arrondi, $e\simeq2{,}16\ \mathrm V$ et $12/e\simeq5{,}6$. Il faut **six éléments en série** pour une batterie de tension nominale $12\ \mathrm V$.

> [!JURY]
> Les potentiels standards seuls ne donnent pas la force électromotrice. La loi de Nernst tient compte de la composition de l'électrolyte.

### Question 39

> [!INDICATION]
> Distinguez les branches anodiques et cathodiques grâce au signe du courant, puis rattachez chaque branche au couple de son domaine de potentiel.

#### Solution

Les courants positifs correspondent à des oxydations, les courants négatifs à des réductions.

- **(1)** Oxydation du plomb $\mathrm{Pb}$ en $\mathrm{PbSO_4}$ à l'électrode négative.
- **(2)** Oxydation de $\mathrm{PbSO_4}$ en $\mathrm{PbO_2}$ à l'électrode positive.
- **(3)** Oxydation de l'eau en dioxygène, via $2\mathrm{H_2O}\to\mathrm{O_2}+4\mathrm{H^+}+4e^-$.
- **(4)** Réduction des ions $\mathrm{H^+}$ en dihydrogène, via $2\mathrm{H^+}+2e^-\to\mathrm{H_2}$.
- **(5)** Réduction de $\mathrm{PbSO_4}$ en plomb $\mathrm{Pb}$ à l'électrode négative.
- **(6)** Réduction de $\mathrm{PbO_2}$ en $\mathrm{PbSO_4}$ à l'électrode positive.

### Question 40

> [!INDICATION]
> Repérez les branches actives à la décharge avec leur signe de courant, puis lisez l'écart horizontal des potentiels.

#### Solution

En décharge, la branche (1) est lue à $+I_0$ et la branche (6) à $-I_0$. La figure 8 donne environ $E_-\simeq-0{,}20\ \mathrm V$ et $E_+\simeq1{,}5\ \mathrm V$. Il reste donc environ $1{,}7\ \mathrm V$ par élément. Les six éléments sont en série et leurs tensions s'additionnent. La tension disponible est **$U_{\mathrm d}\simeq1{,}0\times10^1\ \mathrm V$** à deux chiffres significatifs.

### Question 41

> [!INDICATION]
> Inversez les transformations des électrodes pour la recharge. Reliez les branches en pointillés aux effets d'une tension trop forte.

#### Solution

La recharge impose $+I_0$ sur la branche (2) et $-I_0$ sur la branche (5). Sur la figure 8, on lit environ $E_+\simeq1{,}9\ \mathrm V$ et $E_-\simeq-0{,}55\ \mathrm V$. La tension du générateur vaut
$$
U_{\mathrm g}=6(E_+-E_-)\simeq 6(1{,}9+0{,}55)\ \mathrm V=14{,}7\ \mathrm V.
$$
Avec ces lectures, on donne **$1\times 10^1\ \mathrm V$** au chiffre significatif demandé.

Une tension plus élevée favorise l'électrolyse de l'eau aux branches (3) et (4), qui dégage du dioxygène et du dihydrogène. Dans une batterie scellée, l'accumulation des gaz augmente la pression et peut endommager ou rompre l'enveloppe.

### Question 42

> [!INDICATION]
> Convertissez la charge extraite en coulombs puis comptez les électrons par atome de plomb oxydé.

> [!INDICATION]
> Distinguez la masse consommée dans un élément et celle consommée dans l'ensemble des éléments en série.

#### Solution

À mi-décharge, la charge extraite vaut $Q_{\mathrm d}=20\ \mathrm{A\,h}=20\times3600\ \mathrm C$. La réaction anodique libère deux électrons par atome de plomb. Dans chaque élément, la masse oxydée vaut
$$
\boxed{m_{\mathrm{Pb,él}}=\frac{M(\mathrm{Pb})Q_{\mathrm d}}{2F}
\simeq8\times10^{-2}\ \mathrm{kg}.}
$$
La même charge traverse chaque élément en série. Dans les six éléments de la batterie, la masse totale de plomb oxydée vaut donc **$6m_{\mathrm{Pb,él}}\simeq5\times10^{-1}\ \mathrm{kg}$**, en multipliant avant arrondi.

### Question 43

> [!INDICATION]
> Lisez les deux grandeurs électriques portées sur la batterie. Associez-les pour obtenir une énergie en wattheures avant de diviser par la masse.

#### Solution

La figure 7 indique $12\ \mathrm V$ et $40\ \mathrm{A\,h}$. En assimilant la tension à sa valeur nominale au cours de la décharge, l’énergie est estimée par $UQ$. Ainsi,
$$
\boxed{w=\frac{UQ}{m}
\simeq 5\times10^1\ \mathrm{W\,h\,kg^{-1}}.}
$$
Le calcul en $\mathrm{W\,h}$ utilise directement la capacité en $\mathrm{A\,h}$.

### Question 44

> [!INDICATION]
> Équilibrez la demi-équation en milieu acide, puis identifiez le mode où l'électrode positive est le siège d'une oxydation.

#### Solution

Le plomb passe du degré d'oxydation $0$ à $+\mathrm{IV}$. En milieu acide, l'équation s'écrit
$$
\boxed{\mathrm{Pb}(s)+2\mathrm{H_2O}(l)\longrightarrow
\mathrm{PbO_2}(s)+4\mathrm{H^+}(aq)+4e^-.}
$$
Cette oxydation a lieu lors de la **recharge**, où l'électrode positive joue le rôle d'anode.

## Bilan des méthodes

- Dans l’anneau, la force magnétique agit sur la direction de la vitesse. La perte d’électrons est proportionnelle à leur effectif et conduit à une décroissance exponentielle sans réinjection.
- Dans le Michelson, le déplacement du miroir fixe la différence de marche. La période des oscillations donne la longueur d’onde centrale, tandis que la décroissance de l’enveloppe donne un ordre de grandeur de la longueur de cohérence.
- Dans une batterie, l’oxydation se produit à l’anode. À la recharge, les rôles des électrodes s’inversent. Le même courant traverse les éléments en série, mais le potentiel de chaque électrode varie avec le courant qui la traverse.

FIN
