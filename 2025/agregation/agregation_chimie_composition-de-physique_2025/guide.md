# Agrégation Chimie — Composition de physique 2025 · Corrigé guidé
*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Sujet : « Autour des matériaux piézoélectriques » (épreuve B, session 2025, durée 5 heures). Mode d’emploi recommandé : chercher seul, lire l’indication en cas de blocage, réessayer, puis voir la solution.

## Présentation du sujet

Épreuve de composition de physique de 5 heures (session 2025), calculatrice autorisée, aucun autre document. Le sujet, « Autour des matériaux piézoélectriques », comporte **60 questions** réparties en cinq parties largement indépendantes :

- **Partie I** (Q1–Q5) : optique géométrique d'une sphère de quartz fondu formant l'image d'une photographie ;
- **Partie II** (Q6–Q10) : thermodynamique du butane dans un allume-gaz (diagramme de Clapeyron, gaz parfait, bilan énergétique de l'étincelle) ;
- **Partie III** (Q11–Q26) : émission et réception d'ultrasons par des transducteurs piézoélectriques (acoustique linéaire, célérité du son, ondes progressives, expérience de mesure avec incertitudes et scripts Python/C) ;
- **Partie IV** (Q27–Q38) : oscillateur à quartz à amplificateurs linéaires intégrés (ALI) ;
- **Partie V** (Q39–Q60) : du condensateur plan (V.1) à la polarisation piézoélectrique modélisée par une chaîne de ressorts (V.2).

Notions du programme mobilisées : optique géométrique (Snell-Descartes, stigmatisme, conditions de Gauss), thermodynamique des fluides (diagramme de Clapeyron, gaz parfait, loi de Laplace), acoustique linéaire et ondes, électrocinétique en régime transitoire et sinusoïdal forcé (ALI, impédances complexes, filtres), électrostatique (Gauss, symétries, énergie), mécanique du solide (ressorts, moment dipolaire). D'après le rapport du jury, 39 questions sur 60 relèvent d'un socle fondamental (repérées par une étoile dans l'énoncé).

Gestion du temps : les parties I, II et V.1 sont très abordables et bien rémunérées (nombreuses questions fondamentales) ; en partie IV, ne pas oublier le régime saturé de l'ALI (Q31, Q36, Q38) ; la fin de la partie V (Q55–Q60) est plus discriminante mais se traite par des sommes télescopiques. Partout, schémas, analyse dimensionnelle et résultats encadrés sont valorisés.

## Partie I — Une application du quartz fondu

Une sphère de quartz fondu forme l'image d'une photographie : après les définitions (Q1), on établit les propriétés de symétrie du système (Q2) qui mènent au stigmatisme rigoureux (Q3), dont on montre la limite hors des conditions de Gauss (Q4–Q5). Outils : lois de Snell-Descartes, symétrie de révolution, définitions du stigmatisme.

### Question 1

> [!INDICATION]
> Repérer sur la figure 1 si les rayons émergents convergent réellement, ou seulement en prolongement.

> [!INDICATION]
> Définir image réelle et image virtuelle à partir de l'intersection effective ou des prolongements des rayons émergents.

#### Solution

Une **image réelle** d'un point-objet est l'intersection effective des rayons émergents : les rayons convergent physiquement en ce point, qui peut être recueilli sur un écran. Une **image virtuelle** est l'intersection des prolongements des rayons émergents : aucun rayon ne passe réellement par ce point, qui ne peut être recueilli sur un écran mais seulement observé à travers le système.

Sur la figure 1, les rayons issus de la photographie convergent effectivement après la sphère de quartz : l'image observée est **réelle**, renversée et réduite.

> [!JURY]
> « Les notions d’images réelles et virtuelles sont souvent définies de façon peu précise et des confusions apparaissent sur le rôle des plans focaux ou des foyers » (rapport 2025, Q1).

### Question 2

> [!INDICATION]
> Montrer que tout rayon issu de A reste dans le plan (A, C) : invoquer la symétrie de révolution et les lois de Snell-Descartes.

> [!INDICATION]
> Quel rayon atteint les deux dioptres selon la normale ? Quelle est sa direction après la sphère ?

#### Solution

Le système (sphère homogène) possède une symétrie de révolution autour de tout axe passant par son centre $C$. Le plan défini par le point-objet $A$ et $C$ (plan méridien) contient donc l'axe optique. En un dioptre sphérique, la normale est radiale, donc contenue dans ce plan ; les lois de Snell-Descartes laissent le rayon réfracté dans le plan d'incidence. Tout rayon issu de $A$ reste ainsi dans le plan méridien : une coupe plane suffit.

Un rayon issu de $A$ et dirigé vers le point $S$ passe par le centre $C$ (droite $AS$ diamétrale).

Il atteint chaque dioptre selon la direction radiale, c'est-à-dire selon la normale : l'incidence est normale, donc $i = 0$ et $r = 0$ : le rayon n'est **pas dévié**, il poursuit en ligne droite suivant $AS$.

### Question 3

> [!INDICATION]
> Définir le stigmatisme rigoureux pour le couple (A, A').

> [!INDICATION]
> Construire A' à partir de deux rayons émergents particuliers, dont le rayon non dévié de Q2.

#### Solution

Un système est **rigoureusement stigmatique** pour le couple $(A,A')$ si tout rayon issu de $A$ émerge en passant (réellement ou en prolongement) par un unique point $A'$.

L'image $A'$ est alors l'intersection du rayon non dévié (la droite $AS$, passant par $C$) et du rayon émergent correspondant au rayon incident passant par $I_1$ : on construit $A'$ comme ce point d'intersection sur la figure a.

### Question 4

> [!INDICATION]
> Tracer la normale (direction radiale) en chaque point d'incidence avant d'appliquer Snell-Descartes.

> [!INDICATION]
> Comparer la position du point obtenu pour le rayon I1'I2' avec celle de A' de Q3.

#### Solution

Pour le rayon frappant la sphère en $I_1'$ puis $I_2'$, on trace en chaque point d'incidence la **normale au dioptre** (direction radiale passant par $C$).

On applique ensuite les lois de Snell-Descartes à l'entrée ($\sin i = n\sin r$) et à la sortie ($n\sin r' = \sin i'$). Le rayon émergent, prolongé, coupe la droite $AC$ en un point $A''$.

Un tracé exact donne $A'' \neq A'$ : le point image dépend du rayon choisi. Le système n'est donc **pas rigoureusement stigmatique** pour $A$, ce qui contredit l'hypothèse faite en Q3.

> [!JURY]
> « Il est cependant nécessaire de tracer la normale au dioptre lorsque l’on trace des rayons de lumière réfractés afin d’expliciter la référence par rapport à laquelle les angles sont mesurés » (rapport 2025, Q4).

### Question 5

> [!INDICATION]
> Quelles sont les deux conditions (angle, écartement à l'axe) qui définissent un rayon paraxial ?

> [!INDICATION]
> Dans ce cadre, quelles propriétés le système centré possède-t-il approximativement ?

#### Solution

Les **conditions de Gauss** (approximation de Gauss) sont réalisées pour des rayons **paraxiaux** : peu inclinés sur l'axe optique (angles faibles, $\sin\alpha \approx \tan\alpha \approx \alpha$) et peu écartés de l'axe. Dans ce cadre, un système centré est approximativement stigmatique et aplanétique.

> [!PIEGE]
> Ne pas employer « paraxial » sans les deux conditions : faible inclinaison sur l'axe et faible écartement à l'axe.

## Partie II — Une utilisation domestique de l'effet piézoélectrique

Un allume-gaz contient du butane liquéfié : on lit son diagramme de Clapeyron (Q6–Q9) et l'on modélise l'étincelle par un bilan d'énergie avec analyse critique (Q10). Outils : courbe de saturation, modèle du gaz parfait, méthode de résolution de problème.

### Question 6

> [!INDICATION]
> Localiser liquide, gaz et équilibre liquide-vapeur sur le plan (p, v), par rapport à la courbe de saturation.

> [!INDICATION]
> Que devient un corps pur au-dessus de la température critique ?

#### Solution

Dans le diagramme de Clapeyron $(p,v)$ du butane : à gauche de la courbe de saturation (faibles volumes massiques), le butane est **liquide** ; à droite (grands volumes massiques), il est **gazeux** ; sous la cloche délimitée par la courbe de saturation, il est en **équilibre liquide-vapeur**. La courbe de saturation (binodale) est le lieu des états de début et de fin de changement d'état ; son sommet est le **point critique** $\mathcal{C}$, à $T_c = 425\ \text{K}$, soit $151{,}85\ ^\circ\text{C}$.

Pour $T > T_c = 425\ \text{K}$, il n'y a plus de distinction liquide/gaz : le butane est un **fluide supercritique**.

> [!JURY]
> « certaines copies ont su évoquer la notion d’état supercritique » (rapport 2025, Q6).

### Question 7

> [!INDICATION]
> Rappeler les hypothèses et l'équation d'état du modèle du gaz parfait.

> [!INDICATION]
> À quoi ressemble une isotherme de gaz parfait en échelles logarithmiques, et où se situe cette portion sur le diagramme réel ?

#### Solution

**Hypothèses du gaz parfait** : molécules ponctuelles (volume propre négligeable), sans interaction à distance hormis les chocs élastiques, en agitation thermique désordonnée (chaos moléculaire). **Équation d'état** :

$$
pV = nRT,
$$

soit, par unité de masse, $p\,v = \dfrac{RT}{M}$.

Sur une isotherme, le gaz parfait impose $p\,v = \text{cste}$ : en échelles logarithmiques, une droite de pente $-1$. Cette portion n'est atteinte qu'aux **grands volumes massiques** (faibles pressions), loin de la cloche de saturation, où les interactions sont négligeables. Partout ailleurs, le diagramme d'un gaz réel ne peut pas être celui d'un gaz parfait puisqu'il montre le butane sous différents états physiques.

> [!JURY]
> « le diagramme ne pouvait pas être celui d’un gaz parfait puisqu’il montrait le butane sous différents états physiques » (rapport 2025, Q7).

### Question 8

> [!INDICATION]
> Convertir 32 °C en kelvins et relier le pourcentage de liquide en masse au titre en vapeur.

> [!INDICATION]
> Lire p_A et v_A sur le diagramme (attention à l'axe logarithmique), puis appliquer m = V/v au réservoir.

#### Solution

À $T = 32\ ^\circ\text{C} = 305{,}15\ \text{K}$ avec 70 % de liquide en masse, le titre en vapeur vaut $x = 0{,}30$. Le point $A$ est à l'intersection de l'isotherme $305\ \text{K}$ (à l'intérieur de la cloche) et de l'isotitre $0{,}3$. On y lit la pression de vapeur saturante :

$$
\boxed{p_A \approx 3\times10^{5}\ \text{Pa} \approx 3\ \text{bar}}.
$$

Le volume massique au point $A$ se lit sur l'axe logarithmique : $v_A \approx 4{,}5\times10^{-2}\ \text{m}^3\cdot\text{kg}^{-1}$. Le réservoir a pour volume

$$
\begin{aligned}
V &= 4\ \text{cm} \times 1\ \text{cm} \times 1\ \text{cm} \\
&= 4\ \text{cm}^3 = 4\times10^{-6}\ \text{m}^3.
\end{aligned}
$$

d'où la masse de butane contenue :

$$
\boxed{m = \frac{V}{v_A} \approx \frac{4\times10^{-6}}{4{,}5\times10^{-2}} \approx 9\times10^{-5}\ \text{kg} \approx 0{,}09\ \text{g}}.
$$

*Vérification* : la masse de liquide $m_\ell = 0{,}7\,m \approx 0{,}063\ \text{g}$ occupe, avec $\rho_\ell \approx 0{,}58\ \text{g}\cdot\text{cm}^{-3}$, un volume d'environ $0{,}1\ \text{cm}^3$, soit une petite fraction du réservoir : le reste est de la vapeur, ce qui est cohérent.

> [!PIEGE]
> La lecture sur un axe logarithmique est source d’erreurs grossières : faire un contrôle de vraisemblance (ordre de grandeur du volume de liquide).

> [!JURY]
> « des fragilités apparaissent lors de la lecture des coordonnées selon un axe logarithmique » (rapport 2025, Q8).

### Question 9

> [!INDICATION]
> Quelle grandeur est fixée par un réservoir indilatable contenant une masse fixée ? Traduction sur le diagramme (p, v).

> [!INDICATION]
> En montant à v fixé, dans quel sens évolue le titre en vapeur lu sur les courbes isotitres ?

#### Solution

Le réservoir est indilatable et la masse qu'il contient est fixée : le volume massique moyen $v = V/m$ est constant, donc le point représentatif se déplace sur une **verticale** ($v = \text{cste}$) du diagramme $(p,v)$, vers les pressions croissantes quand $T$ augmente.

Comme $v_A$ est nettement supérieur au volume massique critique, le point est du côté « riche en vapeur ». En montant à $v$ fixé, on croise les isotitres vers des titres en vapeur $x$ **croissants** : la proportion de liquide **diminue** (le liquide se vaporise), jusqu'à disparition complète du liquide.

### Question 10

> [!INDICATION]
> Modéliser l'allume-gaz par un ressort de raideur k comprimé d'une longueur x : quelle énergie est disponible ?

> [!INDICATION]
> Estimer k par un ordre de grandeur (force, course), puis comparer l'énergie stockée à l'énergie minimale d'inflammation.

#### Solution

**Modèle.** Au relâchement, l'énergie élastique emmagasinée dans le ressort comprimé d'une longueur $x$,

$$
E_{\text{él}} = \frac12 k x^2,
$$

est transférée au marteau puis au cristal de quartz, qui la restitue sous forme d'énergie électrique capable de produire une étincelle. L'allumage du gaz exige que l'énergie délivrée atteigne au moins l'énergie minimale d'inflammation du butane, $E_{\text{EMI}} = 0{,}25\ \text{mJ}$ ; en pratique, la tension disruptive de l'air impose une énergie bien supérieure.

**Ordres de grandeur.** Un « effort non négligeable » sur la gâchette correspond à une force $F \sim 50\ \text{N}$ sur une course $x \sim 5\ \text{mm}$, d'où

$$
k \sim \frac{F}{x} \sim \frac{50}{5\times10^{-3}} \sim 10^{4}\ \text{N}\cdot\text{m}^{-1}.
$$

L'énergie stockée vaut alors

$$
E_{\text{él}} \sim \frac12\,k x^2 \approx \frac12\times10^{4}\times(5\times10^{-3})^2 \approx 0{,}1\ \text{J},
$$

soit environ $4\times10^{2}$ fois l'EMI : **cohérent** avec la production fiable d'une étincelle malgré les pertes. On retient

$$
\boxed{k \sim 10^{3}\text{--}10^{4}\ \text{N}\cdot\text{m}^{-1}}.
$$

> [!JURY]
> « la conclusion numérique d’une résolution de problème s’accompagne d’une analyse critique des résultats » (rapport 2025, Q10).

## Partie III — Effet piézoélectrique et ultrasons

Des transducteurs piézoélectriques émettent et reçoivent des ultrasons : on établit l'équation de propagation (Q11–Q20), puis on exploite une expérience de mesure (Q21–Q26) avec incertitudes-type et lecture de scripts. Outils : acoustique linéaire, loi de Laplace, ondes progressives, propagation d'incertitudes, Monte-Carlo.

### Question 11

> [!INDICATION]
> Quelles grandeurs sont perturbées par le passage de l'onde, et à quelle condition les linéarise-t-on ?

> [!INDICATION]
> Quel statut a le champ de vitesse dans l'approximation acoustique ?

#### Solution

L'**approximation acoustique** (linéarisation) consiste à supposer que toutes les perturbations apportées par l'onde sont des infiniment petits du premier ordre par rapport à l'état d'équilibre : $|\mu_1| \ll \mu_0$, $|p_1| \ll p_0$, et le champ de vitesse $\vec v_1$, **nul en l'absence d'onde**, est lui-même du premier ordre, ainsi que ses dérivées. On ne conserve dans les équations que les termes d'ordre 1.

> [!JURY]
> « Les conditions de l’approximation acoustique sont bien connues à l’exception de celle concernant le champ de vitesse » (rapport 2025, Q11).

### Question 12

> [!INDICATION]
> Partir de l'équation de conservation de la masse et ne garder que les termes du premier ordre.

> [!INDICATION]
> Quel produit est d'ordre 2 et disparaît ?

#### Solution

La conservation de la masse s'écrit

$$
\frac{\partial\mu}{\partial t} + \operatorname{div}(\mu\vec v) = 0.
$$

Avec $\mu = \mu_0 + \mu_1$ et $\vec v = \vec v_1$, au premier ordre ($\mu_0$ uniforme et stationnaire, le produit $\mu_1\vec v_1$ étant d'ordre 2) :

$$
\boxed{\frac{\partial\mu_1}{\partial t} + \mu_0\operatorname{div}\vec v_1 = 0}.
$$

### Question 13

> [!INDICATION]
> Entre quelles deux échelles se situe la taille d'une particule de fluide ?

> [!INDICATION]
> Suit-on un système fermé ou ouvert lorsqu'on suit une particule de fluide ?

#### Solution

Une **particule de fluide** est un système de taille **mésoscopique** : grande devant l'échelle moléculaire (elle contient un très grand nombre de molécules, ce qui donne un sens aux grandeurs moyennes) et petite devant l'échelle macroscopique (les grandeurs y sont localement uniformes). C'est un **système fermé** : on suit toujours le même ensemble de molécules au cours du mouvement.

> [!JURY]
> « une particule de fluide est nécessairement de taille mésoscopique et constitue un système fermé » (rapport 2025, Q12 à Q16).

### Question 14

> [!INDICATION]
> Appliquer la deuxième loi de Newton à une particule de fluide, forces de pression seules : écrire la résultante des forces de pression.

> [!INDICATION]
> Linéariser l'accélération lagrangienne au premier ordre.

#### Solution

On applique la deuxième loi de Newton à une particule de fluide de volume $\mathrm d\tau$ et de masse $\mu\,\mathrm d\tau$, en ne retenant que les forces de pression, de résultante $-\overrightarrow{\operatorname{grad}}\,p\ \mathrm d\tau$ :

$$
\mu\,\vec a = -\overrightarrow{\operatorname{grad}}\,p.
$$

L'accélération lagrangienne $\vec a = \dfrac{\partial\vec v}{\partial t} + (\vec v\cdot\overrightarrow{\operatorname{grad}})\vec v$ se réduit au premier ordre à $\dfrac{\partial\vec v_1}{\partial t}$ (le terme convectif est d'ordre 2), et l'on remplace $\mu$ par $\mu_0$ et $p$ par $p_1$ dans le gradient :

$$
\boxed{\mu_0\frac{\partial\vec v_1}{\partial t} = -\overrightarrow{\operatorname{grad}}\,p_1}.
$$

Comme $p_1$ ne dépend que de $x$, $\overrightarrow{\operatorname{grad}}\,p_1 = \dfrac{\partial p_1}{\partial x}\vec e_x$ : le champ de vitesse $\vec v_1$ est **colinéaire à $\vec e_x$**, l'onde est **longitudinale**.

### Question 15

> [!INDICATION]
> Écrire le développement limité de μ(p, s) au voisinage de (p0, s), à l'ordre 1 en p1.

> [!INDICATION]
> Introduire le coefficient de compressibilité isentropique χS.

#### Solution

Le développement limité de $\mu(p,s)$ au voisinage de $(p_0,s)$ donne

$$
\mu(p_0+p_1,s) = \mu(p_0,s) + p_1\left(\frac{\partial\mu}{\partial p}\right)_s(p_0,s).
$$

Or $\mu(p_0,s) = \mu_0$, donc $\mu_1 = p_1\left(\dfrac{\partial\mu}{\partial p}\right)_s$. Avec le coefficient de compressibilité isentropique

$$
\chi_S = \frac{1}{\mu}\left(\frac{\partial\mu}{\partial p}\right)_s \approx \frac{1}{\mu_0}\left(\frac{\partial\mu}{\partial p}\right)_s,
$$

on obtient

$$
\boxed{\mu_1 = \mu_0\,\chi_S\,p_1}.
$$

### Question 16

> [!INDICATION]
> Dériver par rapport au temps la relation de conservation linéarisée, et combiner avec l'équation de la dynamique.

> [!INDICATION]
> Identifier la célérité c et vérifier son homogénéité.

#### Solution

En dérivant par rapport au temps la relation de Q12 et en utilisant Q14 :

$$
\begin{aligned}
\frac{\partial^2\mu_1}{\partial t^2} &= -\mu_0\operatorname{div}\frac{\partial\vec v_1}{\partial t} \\
&= \operatorname{div}(\overrightarrow{\operatorname{grad}}\,p_1) = \Delta p_1.
\end{aligned}
$$

Avec Q15, $\dfrac{\partial^2\mu_1}{\partial t^2} = \mu_0\chi_S\dfrac{\partial^2 p_1}{\partial t^2}$, d'où l'**équation de d'Alembert**

$$
\boxed{c^2\,\Delta p_1 = \frac{\partial^2 p_1}{\partial t^2}}
$$

avec la célérité

$$
\boxed{c = \frac{1}{\sqrt{\chi_S\mu_0}}}.
$$

*Homogénéité* : $[\chi_S] = \text{Pa}^{-1}$ et $[\mu_0] = \text{kg}\cdot\text{m}^{-3}$, donc $[\chi_S\mu_0] = \text{s}^2\cdot\text{m}^{-2}$ et $[c] = \text{m}\cdot\text{s}^{-1}$.

> [!METHODE]
> Pour obtenir l’équation de propagation, dériver la conservation de la masse linéarisée par rapport au temps et éliminer v1 à l’aide de l’équation de la dynamique ; l’équation de d’Alembert porte sur p1.

### Question 17

> [!INDICATION]
> Écrire le premier principe pour un corps pur monophasé, puis pour un gaz parfait en transformation isentropique.

> [!INDICATION]
> Utiliser l'équation d'état, Cp − CV = nR et γ = Cp/CV pour aboutir à la loi de Laplace en masse volumique.

#### Solution

Pour un corps pur monophasé, le premier principe s'écrit $\mathrm dU = T\,\mathrm dS - p\,\mathrm dV$. Pour un gaz parfait, la première loi de Joule donne $\mathrm dU = C_V\,\mathrm dT$ ; en transformation **isentropique** ($\mathrm dS = 0$) :

$$
C_V\,\mathrm dT = -p\,\mathrm dV.
$$

L'équation d'état $pV = nRT$ donne $\mathrm dT = \dfrac{1}{nR}(p\,\mathrm dV + V\,\mathrm dp)$. En reportant :

$$
\frac{C_V}{nR}(p\,\mathrm dV + V\,\mathrm dp) = -p\,\mathrm dV.
$$

Avec $C_p - C_V = nR$ et $\gamma = C_p/C_V$, il vient $C_p\,p\,\mathrm dV + C_V\,V\,\mathrm dp = 0$, soit

$$
\gamma\frac{\mathrm dV}{V} + \frac{\mathrm dp}{p} = 0.
$$

Par intégration, $pV^{\gamma} = \text{cste}$. La masse étant fixée, $V \propto 1/\mu$, d'où la **loi de Laplace** :

$$
\boxed{\frac{p}{\mu^{\gamma}} = \text{cste}}.
$$

> [!JURY]
> « Le jury attend une connaissance parfaite de l’écriture des principes de la thermodynamique et une compréhension profonde des notations utilisées » (rapport 2025, Q17 et Q18).

### Question 18

> [!INDICATION]
> Calculer χS pour un gaz parfait à partir de la loi de Laplace.

> [!INDICATION]
> En déduire c, puis faire l'application numérique pour l'air.

#### Solution

Le long d'une isentropique, $p\,\mu^{-\gamma} = \text{cste}$, donc $\mu \propto p^{1/\gamma}$ et

$$
\left(\frac{\partial\mu}{\partial p}\right)_S = \frac{\mu}{\gamma p},
$$

d'où

$$
\chi_S = \frac{1}{\mu}\left(\frac{\partial\mu}{\partial p}\right)_S = \frac{1}{\gamma p}.
$$

La célérité du son vaut donc, avec $\mu_0 = pM/(RT)$ :

$$
\begin{aligned}
c^2 &= \frac{1}{\mu_0\chi_S} = \frac{\gamma p}{\mu_0} \\
&= \frac{\gamma RT}{M},
\end{aligned}
$$

soit

$$
\boxed{c = \sqrt{\frac{\gamma RT}{M}}}.
$$

*Application numérique* (air : $T = 300{,}15\ \text{K}$, $M = 29{,}0\times10^{-3}\ \text{kg}\cdot\text{mol}^{-1}$, $\gamma = 1{,}40$, $R = 8{,}314\ \text{J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$) :

$$
\boxed{c = \sqrt{\frac{1{,}40\times8{,}314\times300{,}15}{29{,}0\times10^{-3}}} \approx 347\ \text{m}\cdot\text{s}^{-1}}.
$$

### Question 19

> [!INDICATION]
> Dans f(x−ct) et f(x+ct), quel terme se propage vers les x croissants ?

> [!INDICATION]
> Relier la translation du profil au retard de propagation.

#### Solution

Dans la solution $p_1(x,t) = \tfrac12[f(x-ct) + f(x+ct)]$, le terme en $x-ct$ représente une **onde progressive** se propageant vers les $x$ croissants à la célérité $c$ sans déformation ; le terme en $x+ct$ représente une onde progressive se propageant vers les $x$ décroissants.

À l'instant $t$, le profil $f(x-ct)$ est le profil initial translaté de $ct$ : c'est le **retard de propagation** dû au temps de trajet $x/c$. La perturbation $p_1$ est une superposition de deux ondes progressives, et non une onde progressive unique.

> [!JURY]
> « toutes les ondes ne sont pas des ondes progressives » (rapport 2025, Q19) : ici p1 est une superposition de deux ondes progressives.

### Question 20

> [!INDICATION]
> Appliquer la solution de d'Alembert avec g = 0 à t = 1 s : où sont centrés les deux profils et quelle est leur amplitude ?

#### Solution

Avec $g = 0$, $p_1(x,t) = \tfrac12[f(x-ct)+f(x+ct)]$ et $c = 300\ \text{m}\cdot\text{s}^{-1}$. À $t = 1\ \text{s}$, on a $ct = 300\ \text{m}$.

Le profil est alors la somme de deux triangles d'amplitude moitié ($500\ \text{Pa}$), images du profil initial, centrés respectivement en $x = -300\ \text{m}$ et $x = +300\ \text{m}$ (figure c).

Si le triangle initial a pour demi-largeur $100\ \text{m}$, les deux triangles ont pour bases respectives $[-400\ \text{m}, -200\ \text{m}]$ et $[200\ \text{m}, 400\ \text{m}]$.

### Question 21

> [!INDICATION]
> Combien de longueurs d'onde séparent les deux positions de B ? En déduire λ.

> [!INDICATION]
> Quelle incertitude-type B pour une lecture sur instrument gradué ? Comment se propage-t-elle sur une différence, puis sur λ ?

#### Solution

Entre la position de $B$ en figure 4 et celle en figure 5, on a observé dix mises en phase successives : la différence des abscisses vaut $10\lambda$. Lectures : $x_{B,4} \approx 147\ \text{mm}$ et $x_{B,5} \approx 233\ \text{mm}$, soit $d = x_{B,5} - x_{B,4} \approx 86\ \text{mm}$, d'où

$$
\boxed{\lambda = \frac{d}{10} \approx 8{,}6\ \text{mm}}.
$$

*Incertitude-type B* (instrument gradué, loi rectangulaire de demi-largeur $\delta/2$, avec une graduation $\delta = 1\ \text{mm}$) : $u(x) = \dfrac{\delta}{2\sqrt3} \approx 0{,}3\ \text{mm}$. Pour une différence de deux lectures indépendantes :

$$
u(d) = \sqrt{u(x_{B,4})^2 + u(x_{B,5})^2} = \sqrt2\,u(x) \approx 0{,}4\ \text{mm},
$$

et donc

$$
\boxed{u(\lambda) = \frac{u(d)}{10} \approx 0{,}04\ \text{mm}}.
$$

> [!METHODE]
> Incertitude-type B d’une lecture sur instrument gradué : loi rectangulaire de demi-largeur une demi-graduation, u = δ/(2√3) pour un pas de graduation δ ; pour des grandeurs indépendantes, les incertitudes se combinent quadratiquement.

### Question 22

> [!INDICATION]
> Exprimer c en fonction de λ et f, et propager les incertitudes relatives.

> [!INDICATION]
> Comparer à la valeur du modèle par l'écart normalisé : quelle conclusion si z < 2 ?

#### Solution

La célérité est $c = \lambda f$, avec $f = 39{,}988\times10^{3}\ \text{Hz}$ :

$$
\boxed{c = 8{,}6\times10^{-3}\times39{,}988\times10^{3} \approx 344\ \text{m}\cdot\text{s}^{-1}}.
$$

Propagation des incertitudes sur un produit de grandeurs indépendantes :

$$
\frac{u(c)}{c} = \sqrt{\left(\frac{u(\lambda)}{\lambda}\right)^2 + \left(\frac{u(f)}{f}\right)^2} = \sqrt{\left(\frac{0{,}04}{8{,}6}\right)^2 + \left(\frac{5}{39\,988}\right)^2} \approx 4{,}7\times10^{-3},
$$

terme dominé par $\lambda$, d'où $u(c) \approx 1{,}6\ \text{m}\cdot\text{s}^{-1}$ et

$$
c = (344 \pm 2)\ \text{m}\cdot\text{s}^{-1}.
$$

*Compatibilité avec le modèle* $c_{\text{mod}} = 347\ \text{m}\cdot\text{s}^{-1}$ (Q18), par l'écart normalisé :

$$
z = \frac{|c - c_{\text{mod}}|}{u(c)} \approx \frac{3}{1{,}6} \approx 1{,}9 < 2.
$$

Les deux valeurs sont **compatibles**.

> [!JURY]
> « L’estimation d’incertitudes-type, le calcul de propagation d’incertitudes, l’utilisation de la méthode de Monte-Carlo et celle de l’écart normalisé sont autant de savoir-faire qui ont significativement progressé dans les copies » (rapport 2025, Q21 à Q23).

### Question 23

> [!INDICATION]
> Quelle ligne du script Python calcule la célérité d'un tirage ?

> [!INDICATION]
> Comment la méthode de Monte-Carlo estime-t-elle c et u(c) à partir de tirages uniformes de λ et f ?

#### Solution

Ligne 14 du script Python : `c_MC = lambda_MC * f_MC`.

**Méthode de Monte-Carlo** : $\lambda$ et $f$ sont tirées selon des lois uniformes (type B rectangulaire de demi-largeur $\sqrt3\,u$, soit les bornes $\lambda \pm \sqrt3\,u_\lambda$ et $f \pm \sqrt3\,u_f$).

Pour chacun des $N$ tirages, on calcule $c = \lambda f$ ; la moyenne de l'échantillon estime $c$ et l'écart-type expérimental (avec `ddof=1`) estime $u(c)$. La figure 6 donne :

$$
\boxed{c = (339 \pm 13)\ \text{m}\cdot\text{s}^{-1}}.
$$

### Question 24

> [!INDICATION]
> La durée mesurée correspond-elle à un aller simple ou à un aller-retour ?

> [!INDICATION]
> Compléter la ligne 36 du script C, avec c exprimée en cm·µs⁻¹.

#### Solution

La durée mesurée `Duree` (en µs) correspond à l'**aller-retour** de l'onde acoustique entre l'émetteur et la cible : la distance est $d = \dfrac{c\,T}{2}$. Avec $c = 347\ \text{m}\cdot\text{s}^{-1} = 0{,}0347\ \text{cm}\cdot\mu\text{s}^{-1}$, la ligne 36 du script C s'écrit :

```c
Distance = Duree * 0.0347 / 2;
```

### Question 25

> [!INDICATION]
> Sur quelle échelle en ordonnée se lit le seuil de basculement du module « Echo » ?

> [!INDICATION]
> Le seuil est-il franchi au début réel de l'écho ? En déduire l'erreur systématique sur la distance.

#### Solution

Le module bascule « Echo » lorsque la tension aux bornes du récepteur dépasse un seuil d'environ $10\ \text{mV}$ (dizaine de millivolts), lu sur l'**échelle de droite** de la figure 9. La salve reçue croissant progressivement, le seuil est franchi **après** le début réel de l'écho ($t \approx 2{,}4\ \text{ms}$), avec un retard $\Delta t \sim 1\times10^{-4}\ \text{s}$. L'erreur systématique sur la distance, qui est **surestimée** (durée allongée), vaut

$$
\boxed{\Delta d = \frac{c\,\Delta t}{2} \approx \frac{347\times10^{-4}}{2} \approx 1{,}7\times10^{-2}\ \text{m} \approx 2\ \text{cm}}.
$$

> [!JURY]
> « la double échelle en ordonnée a parfois été oubliée » (rapport 2025, Q25).

### Question 26

> [!INDICATION]
> Comparer l'excitation de l'émetteur (directe) et le signal reçu au récepteur.

> [!INDICATION]
> Plutôt que l'absorption, quels effets géométriques (divergence) et de conversion expliquent la différence d'amplitude ?

#### Solution

L'émetteur est **directement excité** par le signal créneau de 5 V (conversion électro-mécanique interne au transducteur), tandis que le récepteur ne capte qu'une fraction de l'énergie acoustique : l'onde **diverge géométriquement** (la puissance se répartit sur un front d'onde de plus en plus grand, donc une puissance surfacique décroissante) et subit une **double conversion** peu efficace (acoustique → mécanique → électrique au récepteur). Ce sont ces deux effets, plus que l'absorption dans l'air, qui expliquent l'amplitude beaucoup plus faible du signal reçu.

> [!JURY]
> « Le phénomène d’absorption n’est probablement pas la cause principale » à évoquer pour justifier les différences d’amplitude (rapport 2025, Q26).

## Partie IV — Oscillateur à quartz

Un oscillateur à quartz stabilise la fréquence d'une montre : blocs à ALI en cascade (Q27–Q31), modèle électrique du quartz et filtre passe-bande (Q32–Q35), condition d'oscillation auto-entretenue (Q36) et signaux observés à l'oscilloscope (Q37–Q38). Outils : diviseur de tension, montage suiveur, impédances complexes, équations différentielles.

### Question 27

> [!INDICATION]
> Écrire la relation entrée-sortie du montage inverseur à ALI idéal en régime linéaire.

> [!INDICATION]
> Ajouter les paliers de saturation et la condition de validité du régime linéaire.

#### Solution

Pour un ALI idéal fonctionnant en régime linéaire, la relation entrée-sortie du montage inverseur est

$$
v_{\mathcal A} = -\frac{R'}{R}\,u_{\mathcal A}.
$$

Cette relation n'est valable que tant que la sortie n'est pas saturée, c'est-à-dire $|v_{\mathcal A}| \le V_{\text{sat}}$, soit $|u_{\mathcal A}| \le \dfrac{R}{R'}V_{\text{sat}}$. Au-delà, l'ALI **sature** : $v_{\mathcal A} = \pm V_{\text{sat}}$. La caractéristique est donc la droite de pente $-R'/R$ passant par l'origine entre les points $\left(\pm\frac{R}{R'}V_{\text{sat}},\ \mp V_{\text{sat}}\right)$, prolongée par les deux paliers horizontaux $v_{\mathcal A} = \pm V_{\text{sat}}$.

> [!JURY]
> « L’ALI est un composant non linéaire : lorsqu’il ne fonctionne pas en régime linéaire, il sature » (rapport 2025, Q27).

### Question 28

> [!INDICATION]
> Écrire le diviseur de tension pour deux impédances en série parcourues par le même courant.

> [!INDICATION]
> Quelle condition sur le courant dérivé au nœud intermédiaire ?

#### Solution

**Théorème du diviseur de tension.** Deux dipôles d'impédances $\underline{Z}_1$ et $\underline{Z}_2$ sont en série, soumis à la tension totale $\underline{u}$ et parcourus par le même courant $\underline{i}$.

La tension aux bornes de $\underline{Z}_2$ est $\underline{u}_2 = \underline{Z}_2\,\underline{i}$. Comme $\underline{u} = (\underline{Z}_1+\underline{Z}_2)\,\underline{i}$, on obtient

$$
\boxed{\underline{u}_2 = \frac{\underline{Z}_2}{\underline{Z}_1+\underline{Z}_2}\,\underline{u}}.
$$

**Condition d'utilisation** : aucun courant n'est dérivé au nœud intermédiaire (branche non chargée, dite « sortie ouverte » pour l'étage aval).

> [!JURY]
> « Le jury attend néanmoins que les conditions d’utilisation soient clairement explicitées » (rapport 2025, Q28).

### Question 29

> [!INDICATION]
> Appliquer le diviseur de tension au bloc B, en précisant ce que signifie « sortie ouverte ».

#### Solution

Le bloc $\mathcal B$ est un diviseur constitué de $R''$ et de $R$ en série. En **sortie ouverte** (aucun courant prélevé en sortie, donc même courant dans $R''$ et $R$), la tension de sortie, prise aux bornes de $R$, vaut :

$$
\boxed{v_{\mathcal B} = \frac{R}{R+R''}\,u_{\mathcal B}}.
$$

> [!JURY]
> « Le jury a particulièrement apprécié les copies où la notion de sortie ouverte est clairement définie » (rapport 2025, Q29).

### Question 30

> [!INDICATION]
> Quel montage à ALI réalise v_C = u_C ?

> [!INDICATION]
> Pourquoi ce montage permet-il de mettre les quadripôles en cascade sans les charger ?

#### Solution

Le bloc $\mathcal C$ est un **montage suiveur** (ALI idéal en rétroaction totale) : $v_{\mathcal C} = u_{\mathcal C}$. Son intérêt est l'**adaptation d'impédance** : impédance d'entrée infinie (il ne charge pas l'étage précédent, qui reste effectivement en sortie ouverte) et impédance de sortie nulle, ce qui permet la **mise en cascade** des quadripôles sans modifier leurs relations entrée-sortie. Comme $u_{\mathcal C} = v_{\mathcal B}$ :

$$
v_{\mathcal C} = \frac{R}{R+R''}\,u_{\mathcal B}.
$$

### Question 31

> [!INDICATION]
> Enchaîner A → B → C en utilisant le suiveur pour garder B en sortie ouverte.

> [!INDICATION]
> Traiter séparément le régime linéaire et le régime de saturation de A.

#### Solution

La sortie du bloc $\mathcal A$ alimente le bloc $\mathcal B$ : $u_{\mathcal B} = v_{\mathcal A}$ ; grâce au suiveur $\mathcal C$, le bloc $\mathcal B$ est bien en sortie ouverte.

En **régime linéaire** de $\mathcal A$ ($v_{\mathcal A} = -\dfrac{R'}{R}u_{\mathcal A}$) :

$$
\boxed{v_{\mathcal C} = \frac{R}{R+R''}\,v_{\mathcal A} = -\frac{R'}{R+R''}\,u_{\mathcal A}}.
$$

En **régime de saturation** ($v_{\mathcal A} = \pm V_{\text{sat}}$) :

$$
v_{\mathcal C} = \pm\frac{R}{R+R''}\,V_{\text{sat}}.
$$

> [!PIEGE]
> Ne pas se limiter au régime linéaire : le régime de saturation de l’ALI se traite explicitement et change la valeur de v_C.

### Question 32

> [!INDICATION]
> Écrire l'impédance de la branche série (Rs, Cs, Ls), puis celle de l'association parallèle avec Cp.

> [!INDICATION]
> Vérifier l'homogénéité du résultat obtenu.

#### Solution

Le quartz est modélisé par la capacité $C_p$ en parallèle avec la branche série $(R_s, C_s, L_s)$. L'impédance de la branche série est

$$
\underline{Z}_s = R_s + jL_s\omega + \frac{1}{jC_s\omega} = \frac{1 + jR_sC_s\omega + (j\omega)^2L_sC_s}{jC_s\omega}.
$$

L'impédance équivalente, association en parallèle avec $\dfrac{1}{jC_p\omega}$, vaut $\underline{Z} = \dfrac{\underline{Z}_s}{1 + jC_p\omega\,\underline{Z}_s}$, soit après développement :

$$
\boxed{\underline{Z} = \frac{1 + jR_sC_s\omega + (j\omega)^2L_sC_s}{j(C_s+C_p)\omega + (j\omega)^2R_sC_sC_p + (j\omega)^3L_sC_sC_p}}.
$$

*Homogénéité* : au dénominateur, chaque terme est de la forme $C\omega$ (ou un produit de tels termes), c'est-à-dire une admittance ; numérateur et dénominateur sont homogènes et $\underline{Z}$ est bien une impédance.

> [!JURY]
> « un résultat manifestement non homogène et repéré comme tel sur une copie est valorisé » (rapport 2025, Q32) : l’analyse dimensionnelle détecte les erreurs de calcul.

### Question 33

> [!INDICATION]
> Exprimer la fonction de transfert du bloc D (amplificateur inverseur d'impédance d'entrée Z).

> [!INDICATION]
> Identifier ω0, Q et H0 avec la forme canonique du passe-bande du second ordre.

#### Solution

Le bloc $\mathcal D$ est un amplificateur inverseur à ALI : impédance d'entrée $\underline{Z}$ (le quartz), rétroaction $R$, donc $\underline{H}_{\mathcal D} = \dfrac{\underline{V}_{\mathcal D}}{\underline{U}_{\mathcal D}} = -\dfrac{R}{\underline{Z}}$. En ne retenant dans $\underline{Z}$ que la branche série (rôle dominant au voisinage de la résonance série), $\underline{Z} \approx \dfrac{1 + jR_sC_s\omega + L_sC_s(j\omega)^2}{jC_s\omega}$ :

$$
\underline{H}_{\mathcal D} = -\frac{R\,jC_s\omega}{1 + jR_sC_s\omega + L_sC_s(j\omega)^2}.
$$

Par identification avec la forme canonique du passe-bande du second ordre,

$$
\underline{H}_{\mathcal D} = \frac{H_0\,\dfrac{j\omega}{Q\omega_0}}{1 + \dfrac{j\omega}{Q\omega_0} + \dfrac{(j\omega)^2}{\omega_0^2}},
$$

on obtient :

$$
\begin{aligned}
\omega_0^2 &= \frac{1}{L_sC_s} &&\Rightarrow& \boxed{\omega_0 = \frac{1}{\sqrt{L_sC_s}}}, \\
\frac{1}{Q\omega_0} &= R_sC_s &&\Rightarrow& \boxed{Q = \frac{1}{R_s}\sqrt{\frac{L_s}{C_s}}}, \\
H_0\,R_sC_s &= -R\,C_s &&\Rightarrow& \boxed{H_0 = -\frac{R}{R_s}}.
\end{aligned}
$$

Le numérateur en $j\omega$ et le dénominateur d'ordre 2 caractérisent un **filtre passe-bande** du second ordre ; $H_0$ est le gain (algébrique) à la résonance $\omega = \omega_0$.

> [!PIEGE]
> L’identification de H0 (signe et valeur) est l’étape la plus délicate : reprendre le numérateur complet, pas seulement le terme en jω.

> [!JURY]
> « L’obtention des expressions des caractéristiques du filtre est généralement bien menée à l’exception de celle de H0 » (rapport 2025, Q33).

### Question 34

> [!INDICATION]
> Lire f0 au sommet de la courbe, |H0| comme un rapport d'amplitudes, et Q = f0/Δf à −3 dB.

> [!INDICATION]
> Quelle largeur de bande passante lit-on sur la courbe de résonance ?

#### Solution

Lecture graphique de la courbe de résonance $V_{\mathcal D}(f)$ :
- le sommet est en $f_0 \approx 32\,768\ \text{Hz}$, soit $\omega_0 = 2\pi f_0 \approx 2{,}06\times10^{5}\ \text{rad}\cdot\text{s}^{-1}$ ;
- le gain à la résonance vaut $|H_0| = \dfrac{V_{\mathcal D,\max}}{U_{\mathcal D}} = \dfrac{4{,}3}{0{,}20} \approx 22$ ;
- la bande passante à $-3\ \text{dB}$ (tension $\dfrac{V_{\mathcal D,\max}}{\sqrt2} \approx 3{,}0\ \text{V}$) a pour largeur $\Delta f \approx 1{,}5\ \text{Hz}$, d'où

$$
\boxed{Q = \frac{f_0}{\Delta f} \approx \frac{32\,768}{1{,}5} \approx 2\times10^{4}}.
$$

Ce facteur de qualité gigantesque traduit la très grande finesse de résonance du quartz, qui assure l'excellente stabilité en fréquence de l'oscillateur (base de temps des montres).

> [!JURY]
> « Le facteur de qualité n’est pas toujours associé à la largeur de la bande passante » (rapport 2025, Q34) : Q = f0/Δf à −3 dB.

### Question 35

> [!INDICATION]
> Repartir de la fonction de transfert et passer de jω à d/dt.

> [!INDICATION]
> Quelle équation différentielle relie v_D et u_D ?

#### Solution

De la fonction de transfert $\underline{H}_{\mathcal D} = \dfrac{\underline{V}_{\mathcal D}}{\underline{U}_{\mathcal D}}$ :

$$
\left(1 + \frac{j\omega}{Q\omega_0} + \frac{(j\omega)^2}{\omega_0^2}\right)\underline{V}_{\mathcal D} = H_0\frac{j\omega}{Q\omega_0}\,\underline{U}_{\mathcal D}.
$$

En régime sinusoïdal forcé, l'opérateur $j\omega$ correspond à $\dfrac{\mathrm d}{\mathrm dt}$ ; en multipliant par $\omega_0^2$, on obtient l'équation différentielle :

$$
\boxed{\frac{\mathrm d^2 v_{\mathcal D}}{\mathrm dt^2} + \frac{\omega_0}{Q}\frac{\mathrm d v_{\mathcal D}}{\mathrm dt} + \omega_0^2\,v_{\mathcal D} = \frac{H_0\,\omega_0}{Q}\frac{\mathrm d u_{\mathcal D}}{\mathrm dt}}.
$$

> [!JURY]
> « Le passage d’une équation algébrique portant sur des grandeurs complexes (aspect fréquentiel) à une équation différentielle (aspect temporel), lorsqu’il est explicite, a été valorisé par le jury » (rapport 2025, Q35).

### Question 36

> [!INDICATION]
> Reboucler le montage et écrire l'équation différentielle en régime linéaire.

> [!INDICATION]
> Quelle condition sur le coefficient d'amortissement fait démarrer les oscillations ? Quel composant règle le seuil ?

#### Solution

En rebouclant le montage ($u_{\mathcal D}$ remplacé par $v_{\mathcal C} = K u_{\mathcal A}$), l'équation de fonctionnement en régime linéaire devient

$$
\frac{\mathrm d^2 v_{\mathcal D}}{\mathrm dt^2} + \frac{\omega_0}{Q}(1-KH_0)\frac{\mathrm d v_{\mathcal D}}{\mathrm dt} + \omega_0^2\,v_{\mathcal D} = 0.
$$

Les oscillations démarrent (amplitude croissante à partir du bruit) si le coefficient d'amortissement est **négatif** :

$$
1 - KH_0 < 0 \quad\Longleftrightarrow\quad \boxed{KH_0 > 1}.
$$

Ici $K = -\dfrac{R'}{R+R''} < 0$ et $H_0 = -\dfrac{R}{R_s} < 0$, donc $KH_0 = \dfrac{R'R}{(R+R'')R_s} > 0$.

La condition s'écrit $\dfrac{R'R}{(R+R'')R_s} > 1$. C'est précisément le rôle du **potentiomètre** $R'$ (réglable de 0 à 470 kΩ) : ajuster $R'$ pour franchir le seuil $KH_0 = 1$ et déclencher les oscillations auto-entretenues.

> [!PIEGE]
> Attention aux signes : K et H0 sont tous deux négatifs, donc KH0 > 0 ; la condition de démarrage porte sur KH0, pas sur K ou H0 séparément.

> [!JURY]
> « Quelques candidats ont évoqué le signe des coefficients de l’équation différentielle en lien avec la stabilité du régime linéaire de fonctionnement » (rapport 2025, Q36).

### Question 37

> [!INDICATION]
> Lire Vsat sur la voie C1 et la période sur la base de temps de la figure e.

> [!INDICATION]
> En déduire la fréquence des oscillations.

#### Solution

Sur la figure e (voie C1 : $5\ \text{V}/\text{div}$ pour $v_{\mathcal A}$ ; voie C2 : $200\ \text{mV}/\text{div}$ pour $v_{\mathcal D}$ ; base de temps $10\ \mu\text{s}/\text{div}$), $v_{\mathcal A}$ est un créneau saturé : la lecture donne

$$
V_{\text{sat}} \approx 14\ \text{V},
$$

proche de la tension d'alimentation $V_{cc} = 15\ \text{V}$. La période des oscillations couvre environ $3{,}05$ divisions, soit $T \approx 30{,}5\ \mu\text{s}$, d'où

$$
\boxed{f = \frac{1}{T} \approx 3{,}3\times10^{4}\ \text{Hz} \approx 32{,}8\ \text{kHz}},
$$

cohérent avec la fréquence propre $f_0$ mesurée en Q34.

### Question 38

> [!INDICATION]
> Dans quels intervalles v_D obéit-elle à l'équation amortie, et dans lesquels à l'équation à amortissement négatif ?

> [!INDICATION]
> Pourquoi v_D n'est-elle pas sinusoïdale, et quel rôle joue la saturation de A (apport d'énergie) ?

#### Solution

Lorsque l'ALI $\mathcal A$ est **saturé** ($v_{\mathcal A} = \pm V_{\text{sat}}$), $v_{\mathcal D}$ obéit à l'équation homogène de l'oscillateur amorti ; lors des brèves phases **linéaires** de basculement, elle obéit à l'équation à amortissement négatif. $v_{\mathcal D}$ est donc une fonction **continue définie par morceaux**, solution alternativement de l'une ou de l'autre équation différentielle : elle **n'est pas sinusoïdale**. Elle paraît quasi sinusoïdale parce que le facteur de qualité très élevé du filtre $\mathcal D$ ne laisse passer qu'une composante quasi monochromatique.

Le caractère **non linéaire** du montage (saturation de $\mathcal A$) est essentiel : c'est lui qui assure l'**apport extérieur d'énergie** (fournie par l'alimentation $\pm V_{cc}$) compensant les pertes et stabilisant l'amplitude des oscillations — ce qui distingue un oscillateur auto-entretenu du simple régime libre amorti d'un oscillateur.

> [!JURY]
> « La tension vD n’est pas sinusoïdale mais une fonction continue définie par morceaux, solution alternativement de l’une ou l’autre des équations différentielles données dans l’énoncé » (rapport 2025, Q38) ; le nécessaire apport extérieur d’énergie, assuré par la saturation de l’ALI, distingue l’oscillateur auto-entretenu du régime libre amorti.

## Partie V — Relations électro-mécaniques d'un matériau piézoélectrique

La polarisation piézoélectrique se comprend à partir de systèmes simples : le condensateur plan (V.1, Q39–Q53), puis une chaîne de ressorts ionique (V.2, Q54–Q60). Outils : théorème de Gauss et symétries, énergie électrostatique, bilan de charge, mécanique des ressorts.

### V.1 — Le condensateur plan

### Question 39

> [!INDICATION]
> Partir de l'équation de Maxwell-Gauss et l'intégrer sur un volume fermé.

> [!INDICATION]
> Appliquer le théorème d'Ostrogradski en orientant le vecteur surface vers l'extérieur.

#### Solution

L'équation de Maxwell-Gauss s'écrit $\operatorname{div}\vec E = \dfrac{\rho}{\varepsilon_0}$. Intégrons-la sur un volume $\mathcal V$ délimité par une surface **fermée** $\mathcal S$ :

$$
\iiint_{\mathcal V}\operatorname{div}\vec E\,\mathrm d\tau = \iiint_{\mathcal V}\frac{\rho}{\varepsilon_0}\,\mathrm d\tau = \frac{Q_{\text{int}}}{\varepsilon_0}.
$$

Par le théorème d'Ostrogradski (Green-Ostrogradski), avec le vecteur surface $\overrightarrow{\mathrm dS}$ orienté vers l'**extérieur** du volume :

$$
\boxed{\oiint_{\mathcal S}\vec E\cdot\overrightarrow{\mathrm dS} = \frac{Q_{\text{int}}}{\varepsilon_0}}.
$$

> [!JURY]
> « utilisé rigoureusement le théorème d’Ostrogradski en indiquant clairement le domaine d’intégration ainsi qu’en orientant le vecteur surface vers l’extérieur du volume » (rapport 2025, Q39).

### Question 40

> [!INDICATION]
> Quelles invariances par translation la distribution possède-t-elle ?

> [!INDICATION]
> Quels plans de symétrie en déduire pour le champ ? Quelles composantes de E s'annulent ?

#### Solution

La distribution $\mathcal D_{\sigma_0}$ — plan $\Pi_0 = (O,\vec e_y,\vec e_z)$ uniformément chargé en surface avec la densité $\sigma_0$ — est **invariante par translation** selon $\vec e_y$ et $\vec e_z$.

Le champ $\vec E$ ne dépend donc que de $x_M$.

Tout plan contenant $\vec e_x$ est un plan de **symétrie** de la distribution. En particulier :
- le plan $(M,\vec e_x,\vec e_y)$ contient $\vec E(M)$, donc $E_z = 0$ ;
- le plan $(M,\vec e_x,\vec e_z)$ contient $\vec E(M)$, donc $E_y = 0$.

Ainsi :

$$
\boxed{\vec E_{\mathcal D_{\sigma_0}}(M) = E_{\mathcal D_{\sigma_0}}(x_M)\,\vec e_x}.
$$

### Question 41

> [!INDICATION]
> Rappeler la définition d'un plan d'anti-symétrie d'une distribution de charges.

> [!INDICATION]
> Une distribution uniforme de signe constant possède-t-elle un tel plan ?

#### Solution

Un **plan d'anti-symétrie** d'une distribution de charges est un plan tel que la symétrie par rapport à ce plan transforme la distribution en son **opposée** (elle change le signe de toutes les densités de charge). Pour $\mathcal D_{\sigma_0}$, de densité $\sigma_0$ uniforme et de signe constant, aucune symétrie plane ne peut inverser le signe des charges : $\mathcal D_{\sigma_0}$ ne possède donc **aucun plan d'anti-symétrie** (le plan $\Pi_0$ est au contraire un plan de symétrie de la distribution).

> [!PIEGE]
> Ne pas confondre plan d’anti-symétrie d’une distribution (qui change le signe des charges) et plan de symétrie du champ.

> [!JURY]
> « les candidats confondent souvent plan d’anti-symétrie d’une distribution et plan de symétrie du champ » (rapport 2025, Q41).

### Question 42

> [!INDICATION]
> Exploiter la symétrie du plan Π0 avec la relation propre aux champs polaires.

> [!INDICATION]
> En déduire la parité de la fonction E(x_M).

#### Solution

Le plan $\Pi_0$ (plan $x=0$) est un plan de symétrie de $\mathcal D_{\sigma_0}$. Pour un champ **polaire** (comme le champ électrostatique), la symétrie par rapport à $\Pi_0$ donne :

pour $M$ d'abscisse $x_M$ et son symétrique $\mathcal S_{\Pi_0}(M)$ d'abscisse $-x_M$, on a

$$
\mathcal S_{\Pi_0}\!\big(\vec E_{\mathcal D_{\sigma_0}}(M)\big) = \vec E_{\mathcal D_{\sigma_0}}\!\big(\mathcal S_{\Pi_0}(M)\big).
$$

La symétrie par rapport au plan $x=0$ change $\vec e_x$ en $-\vec e_x$ : le membre de gauche vaut $-E(x_M)\vec e_x$, le membre de droite $E(-x_M)\vec e_x$. D'où

$$
-E(x_M) = E(-x_M),
$$

soit :

$$
\boxed{x_M \mapsto E_{\mathcal D_{\sigma_0}}(x_M) \text{ est une fonction impaire}}.
$$

> [!JURY]
> « la relation exploitant le caractère polaire du champ électrostatique a été globalement très mal traitée » (rapport 2025, Q42) : écrire la relation de symétrie S(E(M)) = E(S(M)) avec le bon signe pour un vecteur polaire.

### Question 43

> [!INDICATION]
> Choisir une surface de Gauss cylindrique traversant Π0, et raisonner pour x_M > 0.

> [!INDICATION]
> Calculer le flux et la charge intérieure, puis conclure pour tout M par imparité.

#### Solution

On applique le théorème de Gauss à un cylindre (« boîte à chaussures ») d'axe $\vec e_x$, de section $S$, symétrique par rapport à $\Pi_0$, dont les faces sont en $\pm x_M$.

On raisonne pour $x_M > 0$. Le flux sort par les deux faces (champ $\pm\vec e_x$, imparité : $E(-x_M) = -E(x_M)$) et le flux latéral est nul ($\vec E \perp \overrightarrow{\mathrm dS}$). La charge intérieure vaut $\sigma_0 S$, d'où

$$
2\,E(x_M)\,S = \frac{\sigma_0 S}{\varepsilon_0},
$$

soit $E(x_M) = \dfrac{\sigma_0}{2\varepsilon_0}$ pour $x_M > 0$, et, par imparité, $E(x_M) = -\dfrac{\sigma_0}{2\varepsilon_0}$ pour $x_M < 0$. Finalement, pour tout point $M$ de l'espace :

$$
\boxed{\vec E_{\mathcal D_{\sigma_0}}(M) = \frac{\sigma_0}{2\varepsilon_0}\operatorname{sgn}(x_M)\,\vec e_x}.
$$

> [!JURY]
> « il est en outre important de préciser que xM > 0 dans le raisonnement » (rapport 2025, Q43) : expliciter la surface de Gauss et le signe du flux.

### Question 44

> [!INDICATION]
> Invoquer la linéarité des équations de Maxwell pour superposer les champs des deux plans.

> [!INDICATION]
> Tracer E0, EA et leur somme ; quelles valeurs entre les armatures et à l'extérieur ?

#### Solution

Les équations de Maxwell étant **linéaires**, le champ créé par l'ensemble des deux plans chargés est la **somme** (superposition) des champs créés par chacun. Avec $\sigma_0 = -\sigma$ pour le plan $\Pi_0$ ($x=0$) et $\sigma_A = +\sigma$ pour le plan $\Pi_A$ ($x = L_x$) :

$$
\begin{aligned}
E_0(x) &= -\frac{\sigma}{2\varepsilon_0}\operatorname{sgn}(x), \\
E_A(x) &= +\frac{\sigma}{2\varepsilon_0}\operatorname{sgn}(x-L_x).
\end{aligned}
$$

- $E_0$ est une « marche » descendante en $x=0$ (valeur $-\sigma/(2\varepsilon_0)$ pour $x>0$) ;
- $E_A$ est une « marche » montante en $x=L_x$ (valeur $+\sigma/(2\varepsilon_0)$ pour $x>L_x$) ;
- leur somme $E = E_0 + E_A$ est **nulle à l'extérieur** des armatures et constante entre les armatures :

$$
\boxed{\vec E = -\frac{\sigma}{\varepsilon_0}\,\vec e_x \quad\text{dans l'espace inter-armature}\ (0 < x < L_x)}.
$$

> [!PIEGE]
> Tracer séparément E0 et EA (marches de signes opposés) avant de sommer : le champ est nul à l’extérieur et constant entre les armatures.

> [!JURY]
> « les graphes demandés se sont régulièrement avérés faux ou incohérents » (rapport 2025, Q44).

### Question 45

> [!INDICATION]
> Définir le potentiel électrostatique en régime stationnaire et en déduire la loi des mailles.

> [!INDICATION]
> Que devient la circulation de E en régime variable (équation de Maxwell-Faraday) ?

#### Solution

En régime stationnaire, le champ électrostatique dérive d'un **potentiel** $V$ défini par $\vec E = -\overrightarrow{\operatorname{grad}}\,V$, de circulation nulle : $\oint\vec E\cdot\overrightarrow{\mathrm d\ell} = 0$, ce qui est la **loi des mailles** (la somme algébrique des tensions le long d'une maille est nulle). En **régime variable**, l'équation de Maxwell-Faraday $\operatorname{rot}\vec E = -\dfrac{\partial\vec B}{\partial t}$ donne

$$
\oint\vec E\cdot\overrightarrow{\mathrm d\ell} = -\frac{\mathrm d\Phi_B}{\mathrm dt},
$$

la loi des mailles est alors modifiée par une **force électromotrice d'induction** $e = -\dfrac{\mathrm d\Phi_B}{\mathrm dt}$. Dans le cadre de l'ARQS, ce phénomène d'induction est négligé.

### Question 46

> [!INDICATION]
> Calculer la circulation du champ uniforme E le long du chemin C de O vers A.

> [!INDICATION]
> Relier cette intégrale à V_O − V_A, puis conclure pour v = V_A − V_O.

#### Solution

Le champ est uniforme entre les armatures : $\vec E = -\dfrac{\sigma}{\varepsilon_0}\vec e_x$, et $\overrightarrow{\mathrm d\ell} = \mathrm dx\,\vec e_x$ le long du chemin $\mathcal C$ de $O$ vers $A$ :

$$
\int_{\mathcal C,\,O\to A}\vec E\cdot\overrightarrow{\mathrm d\ell} = \int_0^{L_x}\left(-\frac{\sigma}{\varepsilon_0}\right)\mathrm dx = -\frac{\sigma L_x}{\varepsilon_0}.
$$

Or $\displaystyle\int_O^A\vec E\cdot\overrightarrow{\mathrm d\ell} = V_O - V_A = -(V_A - V_O)$, donc la tension $v = V_A - V_O$ vaut :

$$
\boxed{v = V_A - V_O = \frac{\sigma L_x}{\varepsilon_0}}.
$$

### Question 47

> [!INDICATION]
> Rappeler la définition de la capacité : relation entre charge d'une armature et tension.

> [!INDICATION]
> Exprimer q et v en fonction de σ, S, Lx, puis conclure.

#### Solution

La **capacité** $C$ d'un condensateur est définie par la relation $q = C\,v$, où $q$ est la charge de l'armature portée au potentiel le plus élevé et $v$ la tension entre les armatures. Ici $q = \sigma S$ et $v = \dfrac{\sigma L_x}{\varepsilon_0}$, d'où

$$
C = \frac{q}{v} = \frac{\sigma S}{\sigma L_x/\varepsilon_0}
$$

soit

$$
\boxed{C = \frac{\varepsilon_0 S}{L_x}}.
$$

> [!JURY]
> « Une explication qualitative n’est pas suffisante » (rapport 2025, Q47) : définir C par la relation q = C v.

### Question 48

> [!INDICATION]
> Partir de la densité volumique d'énergie électrique et intégrer sur le volume inter-armature.

> [!INDICATION]
> Exprimer le résultat en fonction de C et v.

#### Solution

Partons de la **densité volumique d'énergie électrique** $u_e = \dfrac{\varepsilon_0 E^2}{2}$ : l'énergie stockée vaut

$$
\mathcal E_e = \iiint u_e\,\mathrm d\tau = \iiint\frac{\varepsilon_0 E^2}{2}\,\mathrm d\tau.
$$

Le champ $E = \dfrac{\sigma}{\varepsilon_0}$ étant uniforme sur le volume inter-armature $S L_x$ :

$$
\mathcal E_e = \frac{\varepsilon_0}{2}\left(\frac{\sigma}{\varepsilon_0}\right)^2 S L_x = \frac{\sigma^2 S L_x}{2\varepsilon_0}.
$$

Avec $\sigma = \dfrac{\varepsilon_0 v}{L_x}$ et $C = \dfrac{\varepsilon_0 S}{L_x}$ :

$$
\mathcal E_e = \frac{\varepsilon_0^2 v^2}{L_x^2}\cdot\frac{S L_x}{2\varepsilon_0} = \frac{\varepsilon_0 S}{2L_x}\,v^2,
$$

soit

$$
\boxed{\mathcal E_e = \frac12 C v^2}.
$$

> [!JURY]
> « menant un raisonnement ayant comme point de départ la densité volumique d’énergie électrique » (rapport 2025, Q48).

### Question 49

> [!INDICATION]
> À partir de l'expression de C, quelles grandeurs augmenter ou diminuer pour augmenter la capacité ?

> [!INDICATION]
> Quelles limitations physiques rencontre-t-on ? Quelles technologies récentes (supercondensateurs) ?

#### Solution

D'après $C = \dfrac{\varepsilon_0\varepsilon_r S}{L_x}$, on augmente la capacité en :
1. **augmentant la surface $S$** des armatures (limité par l'encombrement ; réalisé par enroulement des feuilles dans les condensateurs bobinés) ;
2. **diminuant la distance $L_x$** entre armatures (limité par le champ disruptif du diélectrique, qui provoque le claquage) ;
3. **augmentant la permittivité relative $\varepsilon_r$** du diélectrique intercalé (solution la plus efficace ; on emploie des céramiques de forte permittivité).

Ordres de grandeur usuels : de quelques **nanofarads** à quelques **microfarads** ; les **supercondensateurs**, à très grande surface développée (électrodes poreuses), atteignent des capacités de l'ordre du **farad**.

> [!JURY]
> « Le jury a valorisé l’évocation de l’existence de supercondensateurs » (rapport 2025, Q49).

### Question 50

> [!INDICATION]
> Définir l'intensité comme un débit de charge à travers une section orientée.

> [!INDICATION]
> Quelle notation pour la charge élémentaire échangée pendant dt ?

#### Solution

L'**intensité** $i$ du courant électrique est le débit de charge à travers une section orientée de la surface : pendant la durée $\mathrm dt$, une charge $\delta q$ traverse la section (comptée positivement si elle traverse dans le sens choisi pour $i$), et

$$
\boxed{i = \frac{\delta q}{\mathrm dt}}.
$$

> [!JURY]
> « La définition de l’intensité du courant électrique est très mal connue » (rapport 2025, Q50) : i est un débit de charge, avec orientation de la surface et notation δq.

### Question 51

> [!INDICATION]
> Faire un bilan de charge sur l'armature ΠA, en convention récepteur.

> [!INDICATION]
> Distinguer la variation d'une grandeur d'état (dq) et la charge échangée (δq).

#### Solution

**Bilan de charge** sur l'armature $\Pi_A$ (système = armature de charge $q$), en convention récepteur. Pendant $\mathrm dt$, la charge $\delta q = i\,\mathrm dt$ apportée par le fil (orienté dans le sens de $i$) s'accumule sur l'armature, qui ne laisse passer aucune charge vers l'autre armature : la variation de la charge d'état vaut $\mathrm dq = \delta q$. D'où

$$
\boxed{i = \frac{\mathrm dq}{\mathrm dt}}.
$$

L'orientation de $i$ (vers $\Pi_A$) est cohérente avec le sens d'accumulation de la charge dans ce bilan en convention récepteur.

> [!JURY]
> « la convention d’orientation des échanges est la convention récepteur pour le système considéré » (rapport 2025, Q51) ; distinguer la variation d’état dq et la cause δq.

### Question 52

> [!INDICATION]
> Écrire la loi des mailles avec q = C u, puis dériver pour obtenir l'équation différentielle sur i.

> [!INDICATION]
> Quelle condition initiale, justifiée par la continuité de la tension aux bornes du condensateur ?

#### Solution

Pour $t > 0$, la loi des mailles s'écrit $U = Ri + \dfrac{q}{C}$ avec $i = \dfrac{\mathrm dq}{\mathrm dt}$. En dérivant ($U$ constante) :

$$
R\frac{\mathrm di}{\mathrm dt} + \frac{i}{C} = 0,
$$

soit $\dfrac{\mathrm di}{\mathrm dt} + \dfrac{i}{RC} = 0$.
**Condition initiale** : la tension aux bornes d'un condensateur est continue (car $i = C\,\dfrac{\mathrm du_C}{\mathrm dt}$ reste finie), donc $u_C(0^+) = u_C(0^-) = 0$ ; la loi des mailles en $t = 0^+$ donne alors $U = R\,i(0^+)$, soit $i(0^+) = \dfrac{U}{R}$. D'où :

$$
\boxed{i(t) = \frac{U}{R}\,e^{-t/\tau}}
$$

avec la constante de temps $\tau = RC$.
Le courant, discontinu en $t=0$ (il passe de 0 à $U/R$), décroît exponentiellement vers 0 (régime transitoire d'une durée de l'ordre de $5\tau$, puis régime établi $i = 0$).

> [!JURY]
> « l’exploitation de la continuité de la tension aux bornes d’un condensateur » (rapport 2025, Q52) a été particulièrement appréciée pour la condition initiale.

### Question 53

> [!INDICATION]
> Quel est le signe de i(t) et son sens de variation ?

> [!INDICATION]
> Décrire le mouvement des charges (positives dans le sens de i, électrons en sens inverse) et la fin de la charge.

#### Solution

Pour $t > 0$, $i(t) = \dfrac{U}{R}e^{-t/\tau} > 0$ et décroît.

Des charges **positives** circulent dans le sens de $i$ et s'accumulent sur l'armature $\Pi_A$ (sa charge $q = \sigma S > 0$ croît).

Tandis que l'armature $\Pi_0$ se charge négativement par influence totale. Physiquement, ce sont les **électrons** qui se déplacent en sens inverse de $i$, quittant $\Pi_A$. Lorsque $q \to CU$, le courant tend vers 0 : le mouvement cesse.

### V.2 — Chaîne de ressorts et polarisation piézoélectrique

### Question 54

> [!INDICATION]
> Écrire le DL de l'énergie d'interaction à l'ordre 2 au voisinage du minimum ℓ0.

> [!INDICATION]
> Relier la dérivée seconde de l'énergie à la raideur d'un ressort (force de rappel).

#### Solution

Au voisinage du minimum $\ell_0$ de l'énergie potentielle d'interaction $\mathcal E_{\text{ion}}$, on a $\mathcal E_{\text{ion}}'(\ell_0) = 0$ et $\mathcal E_{\text{ion}}(\ell_0) = \mathcal E_0$. Le développement limité à l'ordre 2 donne

$$
\mathcal E_{\text{ion}}(\ell) \approx \mathcal E_0 + \frac12\,\mathcal E_{\text{ion}}''(\ell_0)\,(\ell-\ell_0)^2.
$$

La force associée, $F = -\dfrac{\mathrm d\mathcal E_{\text{ion}}}{\mathrm d\ell} \approx -\mathcal E_{\text{ion}}''(\ell_0)(\ell-\ell_0)$, est une **force de rappel de ressort** $F = -k(\ell-\ell_0)$, avec :

$$
\boxed{\text{longueur à vide} = \ell_0}
$$

et

$$
\boxed{k = \mathcal E_{\text{ion}}''(\ell_0) = \left.\frac{\mathrm d^2\mathcal E_{\text{ion}}}{\mathrm d\ell^2}\right|_{\ell_0} > 0}.
$$

($k > 0$ puisque $\ell_0$ est un minimum.)

> [!JURY]
> « Le lien entre l’approximation parabolique de l’énergie potentielle d’interaction entre deux ions et la force de rappel d’un ressort est peu explicité » (rapport 2025, Q54) : F = −dE/dℓ au voisinage du minimum.

### Question 55

> [!INDICATION]
> Exprimer les allongements des deux ressorts attachés à G⊕i en fonction de son abscisse x.

> [!INDICATION]
> Quelle abscisse annule les deux allongements ? Même question pour G⊖i.

#### Solution

Au repos, $A_{i-1}$ est en $ia$ et $A_i$ en $(i+1)a$.

Le barycentre $G_{\oplus i}$, d'abscisse $x$, est relié à $A_{i-1}$ par un ressort de raideur $k_a$ et de longueur à vide $a/2$.

Il est aussi relié à $A_i$ par un ressort de raideur $k_b$ et de longueur à vide $a/2$. Testons $x = \left(i+\tfrac12\right)a$ :
- allongement du ressort gauche : $\left[x - ia\right] - \dfrac a2 = \dfrac a2 - \dfrac a2 = 0$ ;
- allongement du ressort droit : $\left[(i+1)a - x\right] - \dfrac a2 = \dfrac a2 - \dfrac a2 = 0$.

Les deux ressorts sont à leur longueur à vide, donc les forces sont nulles : l'équilibre est réalisé **quelles que soient** $k_a$ et $k_b$. Ainsi

$$
x_{G_{\oplus i},0} = \left(i+\tfrac12\right)a.
$$

Le même raisonnement pour $G_{\ominus i}$ (relié par $k_b$ à $A_{i-1}$ et par $k_a$ à $A_i$) donne $x_{G_{\ominus i},0} = \left(i+\tfrac12\right)a$ : les deux barycentres coïncident au repos, ce qui est compatible avec la neutralité électrique de la maille et des barycentres confondus à l'équilibre.

### Question 56

> [!INDICATION]
> Écrire l'équilibre des forces sur chaque barycentre, en ajoutant la force électrique ±δE.

> [!INDICATION]
> Résoudre pour les écarts x̃ des barycentres à leur position de repos.

#### Solution

En présence du champ $\vec E = E\vec e_x$, la force électrique sur $G_{\oplus i}$ (charge $+\delta$) est $+\delta E\,\vec e_x$.

Celle sur $G_{\ominus i}$ (charge $-\delta$) est $-\delta E\,\vec e_x$.

À l'équilibre mécanique, la résultante des forces (ressorts, dont les résultantes au repos sont nulles, plus force électrique) est nulle, ce qui donne, en notant $\widetilde{x}$ les écarts à la position de repos :

$$
-(k_a+k_b)\widetilde{x_{G_{\oplus i}}} + k_a\widetilde{x_{A_{i-1}}} + k_b\widetilde{x_{A_i}} + \delta E = 0,
$$

$$
-(k_a+k_b)\widetilde{x_{G_{\ominus i}}} + k_b\widetilde{x_{A_{i-1}}} + k_a\widetilde{x_{A_i}} - \delta E = 0,
$$

d'où

$$
\boxed{\widetilde{x_{G_{\oplus i}}} = \frac{\delta E + k_a\widetilde{x_{A_{i-1}}} + k_b\widetilde{x_{A_i}}}{k_a+k_b}}
$$

et

$$
\boxed{\widetilde{x_{G_{\ominus i}}} = \frac{-\delta E + k_b\widetilde{x_{A_{i-1}}} + k_a\widetilde{x_{A_i}}}{k_a+k_b}}.
$$

### Question 57

> [!INDICATION]
> Définir le moment dipolaire de la maille comme la somme des charges pondérées par leur position.

> [!INDICATION]
> Exprimer la différence des positions des barycentres à l'aide de Q56.

#### Solution

Le moment dipolaire de la maille $i$ est la somme des charges pondérées par leur position :

$$
\vec p_i = \big[(+\delta)x_{G_{\oplus i}} + (-\delta)x_{G_{\ominus i}}\big]\vec e_x = \delta\big(x_{G_{\oplus i}} - x_{G_{\ominus i}}\big)\vec e_x.
$$

Les positions de repos étant égales (Q55), $x_{G_{\oplus i}} - x_{G_{\ominus i}} = \widetilde{x_{G_{\oplus i}}} - \widetilde{x_{G_{\ominus i}}}$. Avec Q56 :

$$
\widetilde{x_{G_{\oplus i}}} - \widetilde{x_{G_{\ominus i}}} = \frac{2\delta E + (k_b-k_a)\big(\widetilde{x_{A_i}} - \widetilde{x_{A_{i-1}}}\big)}{k_a+k_b}.
$$

Donc

$$
\boxed{\vec p_i = \left[\frac{2\delta^2 E}{k_a+k_b} + \frac{\delta(k_b-k_a)}{k_a+k_b}\big(\widetilde{x_{A_i}} - \widetilde{x_{A_{i-1}}}\big)\right]\vec e_x}.
$$

### Question 58

> [!INDICATION]
> Quelle longueur contient N mailles du réseau ?

> [!INDICATION]
> Quelles inégalités traduisent le caractère mésoscopique de ce volume ?

#### Solution

Le volume mésoscopique $\mathrm d\tau_M$ contient $N$ mailles sur une longueur $Na$ selon $\vec e_x$. Pour être mésoscopique, cette longueur doit être très grande devant la maille $a$ et très petite devant l'échelle macroscopique de variation des champs (ici la longueur $L$ du système, ou la longueur d'onde de la déformation) : le critère s'écrit

$$
\boxed{1 \ll N \quad\text{et}\quad Na \ll L} \qquad\text{(soit } 1 \ll N \ll N_x = L/a\text{)}.
$$

### Question 59

> [!INDICATION]
> Sommer les moments des N mailles : quelle somme se télescope ?

> [!INDICATION]
> Exprimer x̃(A_{j+N}) − x̃(A_j) à l'aide du champ de déplacement u(x).

#### Solution

Le moment dipolaire élémentaire contenu dans $\mathrm d\tau_M$ est la somme des moments des $N$ mailles :

$$
\overrightarrow{\mathrm dp_M} = \sum_{N\ \text{mailles}} \vec p_i.
$$

Le premier terme de Q57 donne $N$ fois $\dfrac{2\delta^2 E}{k_a+k_b}$. Dans le second, la somme $\sum\big(\widetilde{x_{A_i}} - \widetilde{x_{A_{i-1}}}\big)$ est **télescopique** : il reste $\widetilde{x_{A_{j+N}}} - \widetilde{x_{A_j}}$.

Or le champ de déplacement vérifie $\widetilde{x_{A_j}} = u(x)$ et $\widetilde{x_{A_{j+N}}} = u(x+\mathrm dx)$ (les points $A_j$ et $A_{j+N}$ sont en $x$ et $x+\mathrm dx$). D'où

$$
\boxed{\overrightarrow{\mathrm dp_M} = \left[\frac{2N\delta^2 E}{k_a+k_b} + \frac{\delta(k_b-k_a)}{k_a+k_b}\big(u(x+\mathrm dx) - u(x)\big)\right]\vec e_x}.
$$

> [!METHODE]
> La somme des différences de positions successives est télescopique : il ne reste que les termes extrêmes, exprimés avec le champ de déplacement u(x).

### Question 60

> [!INDICATION]
> Diviser le moment élémentaire par dτ_M = Na³ et développer u(x+dx) − u(x) au premier ordre.

> [!INDICATION]
> Quels termes de la polarisation, proportionnels à E et à du/dx, obtient-on ? Lequel caractérise l'effet piézoélectrique ?

#### Solution

Le volume mésoscopique vaut $\mathrm d\tau_M = (Na)\,a^2 = Na^3$ et $\mathrm dx = Na$. Au premier ordre, $u(x+\mathrm dx) - u(x) = \dfrac{\mathrm du}{\mathrm dx}\,\mathrm dx = \dfrac{\mathrm du}{\mathrm dx}\,Na$. La polarisation $\vec P = \dfrac{\overrightarrow{\mathrm dp_M}}{\mathrm d\tau_M}$ vaut donc :

$$
\begin{aligned}
\vec P(M) &= \left[\frac{2N\delta^2 E}{(k_a+k_b)Na^3} + \frac{\delta(k_b-k_a)}{k_a+k_b}\cdot\frac{\frac{\mathrm du}{\mathrm dx}Na}{Na^3}\right]\vec e_x \\
&= \boxed{\left[\frac{2\delta^2}{(k_a+k_b)a^3}\,E + \frac{\delta(k_b-k_a)}{(k_a+k_b)a^2}\,\frac{\mathrm du}{\mathrm dx}\right]\vec e_x}.
\end{aligned}
$$

Le premier terme, proportionnel à $E$, existe dans tout **diélectrique**. Le second, proportionnel à $(k_b-k_a)\dfrac{\mathrm du}{\mathrm dx}$, s'annule si $k_a = k_b$ : c'est la **signature de l'effet piézoélectrique**, c'est-à-dire l'apparition d'une polarisation sous l'effet d'une déformation, même en l'absence de champ électrique appliqué.

> [!METHODE]
> Passer à la limite mésoscopique : diviser par dτ_M et faire tendre dx vers 0 au premier ordre ; le terme en du/dx, nul si ka = kb, est la signature piézoélectrique.

## Bilan

**Méthodes à retenir.** Linéarisation systématique des équations (acoustique Q11–Q16, mécanique Q54–Q56) ; symétries et invariances puis théorème de Gauss avec une surface bien choisie et orientée (Q40–Q43) ; superposition pour les champs (Q44) ; identification d'une fonction de transfert complexe avec la forme canonique d'un filtre (Q33) ; condition de démarrage d'un oscillateur auto-entretenu (amortissement négatif, Q36) et rôle de la saturation comme apport d'énergie (Q38) ; incertitudes-type B, propagation quadratique et écart normalisé (Q21–Q23).

**Définitions à connaître précisément** (le rapport du jury insiste) : image réelle/virtuelle, stigmatisme rigoureux, conditions de Gauss, particule de fluide (mésoscopique, système fermé), intensité du courant (débit de charge, notations d et δ, convention récepteur), capacité (q = C v).

**Questions classiques transposables** : lecture d'un diagramme (p, v) et évolution à volume fixé (Q6–Q9), célérité du son dans un gaz parfait (Q17–Q18), oscillateur à quartz des montres (partie IV), mesure de distance par écho d'ultrasons (Q24–Q25), condensateur plan et énergie stockée (Q46–Q48), polarisation par déformation (Q57–Q60).
