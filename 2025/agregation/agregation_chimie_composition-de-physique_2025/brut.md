# Agrégation Chimie — Composition de physique 2025 · Corrigé brut
*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Sujet : « Autour des matériaux piézoélectriques » (épreuve B, session 2025, durée 5 heures, calculatrice autorisée). Les 60 questions sont traitées dans la numérotation du sujet.

## Partie I — Une application du quartz fondu

### Q1

Une **image réelle** d'un point-objet est l'intersection effective des rayons émergents : les rayons convergent physiquement en ce point, qui peut être recueilli sur un écran. Une **image virtuelle** est l'intersection des prolongements des rayons émergents : aucun rayon ne passe réellement par ce point, qui ne peut être recueilli sur un écran mais seulement observé à travers le système.

Sur la figure 1, les rayons issus de la photographie convergent effectivement après la sphère de quartz : l'image observée est **réelle**, renversée et réduite.

### Q2

Le système (sphère homogène) possède une symétrie de révolution autour de tout axe passant par son centre $C$. Le plan défini par le point-objet $A$ et $C$ (plan méridien) contient donc l'axe optique. En un dioptre sphérique, la normale est radiale, donc contenue dans ce plan ; les lois de Snell-Descartes laissent le rayon réfracté dans le plan d'incidence. Tout rayon issu de $A$ reste ainsi dans le plan méridien : une coupe plane suffit.

Un rayon issu de $A$ et dirigé vers le point $S$ passe par le centre $C$ (droite $AS$ diamétrale).

Il atteint chaque dioptre selon la direction radiale, c'est-à-dire selon la normale : l'incidence est normale, donc $i = 0$ et $r = 0$ : le rayon n'est **pas dévié**, il poursuit en ligne droite suivant $AS$.

### Q3

Un système est **rigoureusement stigmatique** pour le couple $(A,A')$ si tout rayon issu de $A$ émerge en passant (réellement ou en prolongement) par un unique point $A'$.

L'image $A'$ est alors l'intersection du rayon non dévié (la droite $AS$, passant par $C$) et du rayon émergent correspondant au rayon incident passant par $I_1$ : on construit $A'$ comme ce point d'intersection sur la figure a.

### Q4

Pour le rayon frappant la sphère en $I_1'$ puis $I_2'$, on trace en chaque point d'incidence la **normale au dioptre** (direction radiale passant par $C$).

On applique ensuite les lois de Snell-Descartes à l'entrée ($\sin i = n\sin r$) et à la sortie ($n\sin r' = \sin i'$). Le rayon émergent, prolongé, coupe la droite $AC$ en un point $A''$.

Un tracé exact donne $A'' \neq A'$ : le point image dépend du rayon choisi. Le système n'est donc **pas rigoureusement stigmatique** pour $A$, ce qui contredit l'hypothèse faite en Q3.

### Q5

Les **conditions de Gauss** (approximation de Gauss) sont réalisées pour des rayons **paraxiaux** : peu inclinés sur l'axe optique (angles faibles, $\sin\alpha \approx \tan\alpha \approx \alpha$) et peu écartés de l'axe. Dans ce cadre, un système centré est approximativement stigmatique et aplanétique.

## Partie II — Une utilisation domestique de l'effet piézoélectrique

### Q6

Dans le diagramme de Clapeyron $(p,v)$ du butane : à gauche de la courbe de saturation (faibles volumes massiques), le butane est **liquide** ; à droite (grands volumes massiques), il est **gazeux** ; sous la cloche délimitée par la courbe de saturation, il est en **équilibre liquide-vapeur**. La courbe de saturation (binodale) est le lieu des états de début et de fin de changement d'état ; son sommet est le **point critique** $\mathcal{C}$, à $T_c = 425\ \text{K}$, soit $151{,}85\ ^\circ\text{C}$.

Pour $T > T_c = 425\ \text{K}$, il n'y a plus de distinction liquide/gaz : le butane est un **fluide supercritique**.

### Q7

**Hypothèses du gaz parfait** : molécules ponctuelles (volume propre négligeable), sans interaction à distance hormis les chocs élastiques, en agitation thermique désordonnée (chaos moléculaire). **Équation d'état** :

$$
pV = nRT,
$$

soit, par unité de masse, $p\,v = \dfrac{RT}{M}$.

Sur une isotherme, le gaz parfait impose $p\,v = \text{cste}$ : en échelles logarithmiques, une droite de pente $-1$. Cette portion n'est atteinte qu'aux **grands volumes massiques** (faibles pressions), loin de la cloche de saturation, où les interactions sont négligeables. Partout ailleurs, le diagramme d'un gaz réel ne peut pas être celui d'un gaz parfait puisqu'il montre le butane sous différents états physiques.

### Q8

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

### Q9

Le réservoir est indilatable et la masse qu'il contient est fixée : le volume massique moyen $v = V/m$ est constant, donc le point représentatif se déplace sur une **verticale** ($v = \text{cste}$) du diagramme $(p,v)$, vers les pressions croissantes quand $T$ augmente.

Comme $v_A$ est nettement supérieur au volume massique critique, le point est du côté « riche en vapeur ». En montant à $v$ fixé, on croise les isotitres vers des titres en vapeur $x$ **croissants** : la proportion de liquide **diminue** (le liquide se vaporise), jusqu'à disparition complète du liquide.

### Q10

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

## Partie III — Effet piézoélectrique et ultrasons

### Q11

L'**approximation acoustique** (linéarisation) consiste à supposer que toutes les perturbations apportées par l'onde sont des infiniment petits du premier ordre par rapport à l'état d'équilibre : $|\mu_1| \ll \mu_0$, $|p_1| \ll p_0$, et le champ de vitesse $\vec v_1$, **nul en l'absence d'onde**, est lui-même du premier ordre, ainsi que ses dérivées. On ne conserve dans les équations que les termes d'ordre 1.

### Q12

La conservation de la masse s'écrit

$$
\frac{\partial\mu}{\partial t} + \operatorname{div}(\mu\vec v) = 0.
$$

Avec $\mu = \mu_0 + \mu_1$ et $\vec v = \vec v_1$, au premier ordre ($\mu_0$ uniforme et stationnaire, le produit $\mu_1\vec v_1$ étant d'ordre 2) :

$$
\boxed{\frac{\partial\mu_1}{\partial t} + \mu_0\operatorname{div}\vec v_1 = 0}.
$$

### Q13

Une **particule de fluide** est un système de taille **mésoscopique** : grande devant l'échelle moléculaire (elle contient un très grand nombre de molécules, ce qui donne un sens aux grandeurs moyennes) et petite devant l'échelle macroscopique (les grandeurs y sont localement uniformes). C'est un **système fermé** : on suit toujours le même ensemble de molécules au cours du mouvement.

### Q14

On applique la deuxième loi de Newton à une particule de fluide de volume $\mathrm d\tau$ et de masse $\mu\,\mathrm d\tau$, en ne retenant que les forces de pression, de résultante $-\overrightarrow{\operatorname{grad}}\,p\ \mathrm d\tau$ :

$$
\mu\,\vec a = -\overrightarrow{\operatorname{grad}}\,p.
$$

L'accélération lagrangienne $\vec a = \dfrac{\partial\vec v}{\partial t} + (\vec v\cdot\overrightarrow{\operatorname{grad}})\vec v$ se réduit au premier ordre à $\dfrac{\partial\vec v_1}{\partial t}$ (le terme convectif est d'ordre 2), et l'on remplace $\mu$ par $\mu_0$ et $p$ par $p_1$ dans le gradient :

$$
\boxed{\mu_0\frac{\partial\vec v_1}{\partial t} = -\overrightarrow{\operatorname{grad}}\,p_1}.
$$

Comme $p_1$ ne dépend que de $x$, $\overrightarrow{\operatorname{grad}}\,p_1 = \dfrac{\partial p_1}{\partial x}\vec e_x$ : le champ de vitesse $\vec v_1$ est **colinéaire à $\vec e_x$**, l'onde est **longitudinale**.

### Q15

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

### Q16

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

### Q17

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

### Q18

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

### Q19

Dans la solution $p_1(x,t) = \tfrac12[f(x-ct) + f(x+ct)]$, le terme en $x-ct$ représente une **onde progressive** se propageant vers les $x$ croissants à la célérité $c$ sans déformation ; le terme en $x+ct$ représente une onde progressive se propageant vers les $x$ décroissants.

À l'instant $t$, le profil $f(x-ct)$ est le profil initial translaté de $ct$ : c'est le **retard de propagation** dû au temps de trajet $x/c$. La perturbation $p_1$ est une superposition de deux ondes progressives, et non une onde progressive unique.

### Q20

Avec $g = 0$, $p_1(x,t) = \tfrac12[f(x-ct)+f(x+ct)]$ et $c = 300\ \text{m}\cdot\text{s}^{-1}$. À $t = 1\ \text{s}$, on a $ct = 300\ \text{m}$.

Le profil est alors la somme de deux triangles d'amplitude moitié ($500\ \text{Pa}$), images du profil initial, centrés respectivement en $x = -300\ \text{m}$ et $x = +300\ \text{m}$ (figure c).

Si le triangle initial a pour demi-largeur $100\ \text{m}$, les deux triangles ont pour bases respectives $[-400\ \text{m}, -200\ \text{m}]$ et $[200\ \text{m}, 400\ \text{m}]$.

### Q21

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

### Q22

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

### Q23

Ligne 14 du script Python : `c_MC = lambda_MC * f_MC`.

**Méthode de Monte-Carlo** : $\lambda$ et $f$ sont tirées selon des lois uniformes (type B rectangulaire de demi-largeur $\sqrt3\,u$, soit les bornes $\lambda \pm \sqrt3\,u_\lambda$ et $f \pm \sqrt3\,u_f$).

Pour chacun des $N$ tirages, on calcule $c = \lambda f$ ; la moyenne de l'échantillon estime $c$ et l'écart-type expérimental (avec `ddof=1`) estime $u(c)$. La figure 6 donne :

$$
\boxed{c = (339 \pm 13)\ \text{m}\cdot\text{s}^{-1}}.
$$

### Q24

La durée mesurée `Duree` (en µs) correspond à l'**aller-retour** de l'onde acoustique entre l'émetteur et la cible : la distance est $d = \dfrac{c\,T}{2}$. Avec $c = 347\ \text{m}\cdot\text{s}^{-1} = 0{,}0347\ \text{cm}\cdot\mu\text{s}^{-1}$, la ligne 36 du script C s'écrit :

```c
Distance = Duree * 0.0347 / 2;
```

### Q25

Le module bascule « Echo » lorsque la tension aux bornes du récepteur dépasse un seuil d'environ $10\ \text{mV}$ (dizaine de millivolts), lu sur l'**échelle de droite** de la figure 9. La salve reçue croissant progressivement, le seuil est franchi **après** le début réel de l'écho ($t \approx 2{,}4\ \text{ms}$), avec un retard $\Delta t \sim 1\times10^{-4}\ \text{s}$. L'erreur systématique sur la distance, qui est **surestimée** (durée allongée), vaut

$$
\boxed{\Delta d = \frac{c\,\Delta t}{2} \approx \frac{347\times10^{-4}}{2} \approx 1{,}7\times10^{-2}\ \text{m} \approx 2\ \text{cm}}.
$$

### Q26

L'émetteur est **directement excité** par le signal créneau de 5 V (conversion électro-mécanique interne au transducteur), tandis que le récepteur ne capte qu'une fraction de l'énergie acoustique : l'onde **diverge géométriquement** (la puissance se répartit sur un front d'onde de plus en plus grand, donc une puissance surfacique décroissante) et subit une **double conversion** peu efficace (acoustique → mécanique → électrique au récepteur). Ce sont ces deux effets, plus que l'absorption dans l'air, qui expliquent l'amplitude beaucoup plus faible du signal reçu.

## Partie IV — Oscillateur à quartz

### Q27

Pour un ALI idéal fonctionnant en régime linéaire, la relation entrée-sortie du montage inverseur est

$$
v_{\mathcal A} = -\frac{R'}{R}\,u_{\mathcal A}.
$$

Cette relation n'est valable que tant que la sortie n'est pas saturée, c'est-à-dire $|v_{\mathcal A}| \le V_{\text{sat}}$, soit $|u_{\mathcal A}| \le \dfrac{R}{R'}V_{\text{sat}}$. Au-delà, l'ALI **sature** : $v_{\mathcal A} = \pm V_{\text{sat}}$. La caractéristique est donc la droite de pente $-R'/R$ passant par l'origine entre les points $\left(\pm\frac{R}{R'}V_{\text{sat}},\ \mp V_{\text{sat}}\right)$, prolongée par les deux paliers horizontaux $v_{\mathcal A} = \pm V_{\text{sat}}$.

### Q28

**Théorème du diviseur de tension.** Deux dipôles d'impédances $\underline{Z}_1$ et $\underline{Z}_2$ sont en série, soumis à la tension totale $\underline{u}$ et parcourus par le même courant $\underline{i}$.

La tension aux bornes de $\underline{Z}_2$ est $\underline{u}_2 = \underline{Z}_2\,\underline{i}$. Comme $\underline{u} = (\underline{Z}_1+\underline{Z}_2)\,\underline{i}$, on obtient

$$
\boxed{\underline{u}_2 = \frac{\underline{Z}_2}{\underline{Z}_1+\underline{Z}_2}\,\underline{u}}.
$$

**Condition d'utilisation** : aucun courant n'est dérivé au nœud intermédiaire (branche non chargée, dite « sortie ouverte » pour l'étage aval).

### Q29

Le bloc $\mathcal B$ est un diviseur constitué de $R''$ et de $R$ en série. En **sortie ouverte** (aucun courant prélevé en sortie, donc même courant dans $R''$ et $R$), la tension de sortie, prise aux bornes de $R$, vaut :

$$
\boxed{v_{\mathcal B} = \frac{R}{R+R''}\,u_{\mathcal B}}.
$$

### Q30

Le bloc $\mathcal C$ est un **montage suiveur** (ALI idéal en rétroaction totale) : $v_{\mathcal C} = u_{\mathcal C}$. Son intérêt est l'**adaptation d'impédance** : impédance d'entrée infinie (il ne charge pas l'étage précédent, qui reste effectivement en sortie ouverte) et impédance de sortie nulle, ce qui permet la **mise en cascade** des quadripôles sans modifier leurs relations entrée-sortie. Comme $u_{\mathcal C} = v_{\mathcal B}$ :

$$
v_{\mathcal C} = \frac{R}{R+R''}\,u_{\mathcal B}.
$$

### Q31

La sortie du bloc $\mathcal A$ alimente le bloc $\mathcal B$ : $u_{\mathcal B} = v_{\mathcal A}$ ; grâce au suiveur $\mathcal C$, le bloc $\mathcal B$ est bien en sortie ouverte.

En **régime linéaire** de $\mathcal A$ ($v_{\mathcal A} = -\dfrac{R'}{R}u_{\mathcal A}$) :

$$
\boxed{v_{\mathcal C} = \frac{R}{R+R''}\,v_{\mathcal A} = -\frac{R'}{R+R''}\,u_{\mathcal A}}.
$$

En **régime de saturation** ($v_{\mathcal A} = \pm V_{\text{sat}}$) :

$$
v_{\mathcal C} = \pm\frac{R}{R+R''}\,V_{\text{sat}}.
$$

### Q32

Le quartz est modélisé par la capacité $C_p$ en parallèle avec la branche série $(R_s, C_s, L_s)$. L'impédance de la branche série est

$$
\underline{Z}_s = R_s + jL_s\omega + \frac{1}{jC_s\omega} = \frac{1 + jR_sC_s\omega + (j\omega)^2L_sC_s}{jC_s\omega}.
$$

L'impédance équivalente, association en parallèle avec $\dfrac{1}{jC_p\omega}$, vaut $\underline{Z} = \dfrac{\underline{Z}_s}{1 + jC_p\omega\,\underline{Z}_s}$, soit après développement :

$$
\boxed{\underline{Z} = \frac{1 + jR_sC_s\omega + (j\omega)^2L_sC_s}{j(C_s+C_p)\omega + (j\omega)^2R_sC_sC_p + (j\omega)^3L_sC_sC_p}}.
$$

*Homogénéité* : au dénominateur, chaque terme est de la forme $C\omega$ (ou un produit de tels termes), c'est-à-dire une admittance ; numérateur et dénominateur sont homogènes et $\underline{Z}$ est bien une impédance.

### Q33

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

### Q34

Lecture graphique de la courbe de résonance $V_{\mathcal D}(f)$ :
- le sommet est en $f_0 \approx 32\,768\ \text{Hz}$, soit $\omega_0 = 2\pi f_0 \approx 2{,}06\times10^{5}\ \text{rad}\cdot\text{s}^{-1}$ ;
- le gain à la résonance vaut $|H_0| = \dfrac{V_{\mathcal D,\max}}{U_{\mathcal D}} = \dfrac{4{,}3}{0{,}20} \approx 22$ ;
- la bande passante à $-3\ \text{dB}$ (tension $\dfrac{V_{\mathcal D,\max}}{\sqrt2} \approx 3{,}0\ \text{V}$) a pour largeur $\Delta f \approx 1{,}5\ \text{Hz}$, d'où

$$
\boxed{Q = \frac{f_0}{\Delta f} \approx \frac{32\,768}{1{,}5} \approx 2\times10^{4}}.
$$

Ce facteur de qualité gigantesque traduit la très grande finesse de résonance du quartz, qui assure l'excellente stabilité en fréquence de l'oscillateur (base de temps des montres).

### Q35

De la fonction de transfert $\underline{H}_{\mathcal D} = \dfrac{\underline{V}_{\mathcal D}}{\underline{U}_{\mathcal D}}$ :

$$
\left(1 + \frac{j\omega}{Q\omega_0} + \frac{(j\omega)^2}{\omega_0^2}\right)\underline{V}_{\mathcal D} = H_0\frac{j\omega}{Q\omega_0}\,\underline{U}_{\mathcal D}.
$$

En régime sinusoïdal forcé, l'opérateur $j\omega$ correspond à $\dfrac{\mathrm d}{\mathrm dt}$ ; en multipliant par $\omega_0^2$, on obtient l'équation différentielle :

$$
\boxed{\frac{\mathrm d^2 v_{\mathcal D}}{\mathrm dt^2} + \frac{\omega_0}{Q}\frac{\mathrm d v_{\mathcal D}}{\mathrm dt} + \omega_0^2\,v_{\mathcal D} = \frac{H_0\,\omega_0}{Q}\frac{\mathrm d u_{\mathcal D}}{\mathrm dt}}.
$$

### Q36

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

### Q37

Sur la figure e (voie C1 : $5\ \text{V}/\text{div}$ pour $v_{\mathcal A}$ ; voie C2 : $200\ \text{mV}/\text{div}$ pour $v_{\mathcal D}$ ; base de temps $10\ \mu\text{s}/\text{div}$), $v_{\mathcal A}$ est un créneau saturé : la lecture donne

$$
V_{\text{sat}} \approx 14\ \text{V},
$$

proche de la tension d'alimentation $V_{cc} = 15\ \text{V}$. La période des oscillations couvre environ $3{,}05$ divisions, soit $T \approx 30{,}5\ \mu\text{s}$, d'où

$$
\boxed{f = \frac{1}{T} \approx 3{,}3\times10^{4}\ \text{Hz} \approx 32{,}8\ \text{kHz}},
$$

cohérent avec la fréquence propre $f_0$ mesurée en Q34.

### Q38

Lorsque l'ALI $\mathcal A$ est **saturé** ($v_{\mathcal A} = \pm V_{\text{sat}}$), $v_{\mathcal D}$ obéit à l'équation homogène de l'oscillateur amorti ; lors des brèves phases **linéaires** de basculement, elle obéit à l'équation à amortissement négatif. $v_{\mathcal D}$ est donc une fonction **continue définie par morceaux**, solution alternativement de l'une ou de l'autre équation différentielle : elle **n'est pas sinusoïdale**. Elle paraît quasi sinusoïdale parce que le facteur de qualité très élevé du filtre $\mathcal D$ ne laisse passer qu'une composante quasi monochromatique.

Le caractère **non linéaire** du montage (saturation de $\mathcal A$) est essentiel : c'est lui qui assure l'**apport extérieur d'énergie** (fournie par l'alimentation $\pm V_{cc}$) compensant les pertes et stabilisant l'amplitude des oscillations — ce qui distingue un oscillateur auto-entretenu du simple régime libre amorti d'un oscillateur.

## Partie V — Relations électro-mécaniques d'un matériau piézoélectrique

### V.1 — Le condensateur plan

### Q39

L'équation de Maxwell-Gauss s'écrit $\operatorname{div}\vec E = \dfrac{\rho}{\varepsilon_0}$. Intégrons-la sur un volume $\mathcal V$ délimité par une surface **fermée** $\mathcal S$ :

$$
\iiint_{\mathcal V}\operatorname{div}\vec E\,\mathrm d\tau = \iiint_{\mathcal V}\frac{\rho}{\varepsilon_0}\,\mathrm d\tau = \frac{Q_{\text{int}}}{\varepsilon_0}.
$$

Par le théorème d'Ostrogradski (Green-Ostrogradski), avec le vecteur surface $\overrightarrow{\mathrm dS}$ orienté vers l'**extérieur** du volume :

$$
\boxed{\oiint_{\mathcal S}\vec E\cdot\overrightarrow{\mathrm dS} = \frac{Q_{\text{int}}}{\varepsilon_0}}.
$$

### Q40

La distribution $\mathcal D_{\sigma_0}$ — plan $\Pi_0 = (O,\vec e_y,\vec e_z)$ uniformément chargé en surface avec la densité $\sigma_0$ — est **invariante par translation** selon $\vec e_y$ et $\vec e_z$.

Le champ $\vec E$ ne dépend donc que de $x_M$.

Tout plan contenant $\vec e_x$ est un plan de **symétrie** de la distribution. En particulier :
- le plan $(M,\vec e_x,\vec e_y)$ contient $\vec E(M)$, donc $E_z = 0$ ;
- le plan $(M,\vec e_x,\vec e_z)$ contient $\vec E(M)$, donc $E_y = 0$.

Ainsi :

$$
\boxed{\vec E_{\mathcal D_{\sigma_0}}(M) = E_{\mathcal D_{\sigma_0}}(x_M)\,\vec e_x}.
$$

### Q41

Un **plan d'anti-symétrie** d'une distribution de charges est un plan tel que la symétrie par rapport à ce plan transforme la distribution en son **opposée** (elle change le signe de toutes les densités de charge). Pour $\mathcal D_{\sigma_0}$, de densité $\sigma_0$ uniforme et de signe constant, aucune symétrie plane ne peut inverser le signe des charges : $\mathcal D_{\sigma_0}$ ne possède donc **aucun plan d'anti-symétrie** (le plan $\Pi_0$ est au contraire un plan de symétrie de la distribution).

### Q42

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

### Q43

On applique le théorème de Gauss à un cylindre (« boîte à chaussures ») d'axe $\vec e_x$, de section $S$, symétrique par rapport à $\Pi_0$, dont les faces sont en $\pm x_M$.

On raisonne pour $x_M > 0$. Le flux sort par les deux faces (champ $\pm\vec e_x$, imparité : $E(-x_M) = -E(x_M)$) et le flux latéral est nul ($\vec E \perp \overrightarrow{\mathrm dS}$). La charge intérieure vaut $\sigma_0 S$, d'où

$$
2\,E(x_M)\,S = \frac{\sigma_0 S}{\varepsilon_0},
$$

soit $E(x_M) = \dfrac{\sigma_0}{2\varepsilon_0}$ pour $x_M > 0$, et, par imparité, $E(x_M) = -\dfrac{\sigma_0}{2\varepsilon_0}$ pour $x_M < 0$. Finalement, pour tout point $M$ de l'espace :

$$
\boxed{\vec E_{\mathcal D_{\sigma_0}}(M) = \frac{\sigma_0}{2\varepsilon_0}\operatorname{sgn}(x_M)\,\vec e_x}.
$$

### Q44

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

### Q45

En régime stationnaire, le champ électrostatique dérive d'un **potentiel** $V$ défini par $\vec E = -\overrightarrow{\operatorname{grad}}\,V$, de circulation nulle : $\oint\vec E\cdot\overrightarrow{\mathrm d\ell} = 0$, ce qui est la **loi des mailles** (la somme algébrique des tensions le long d'une maille est nulle). En **régime variable**, l'équation de Maxwell-Faraday $\operatorname{rot}\vec E = -\dfrac{\partial\vec B}{\partial t}$ donne

$$
\oint\vec E\cdot\overrightarrow{\mathrm d\ell} = -\frac{\mathrm d\Phi_B}{\mathrm dt},
$$

la loi des mailles est alors modifiée par une **force électromotrice d'induction** $e = -\dfrac{\mathrm d\Phi_B}{\mathrm dt}$. Dans le cadre de l'ARQS, ce phénomène d'induction est négligé.

### Q46

Le champ est uniforme entre les armatures : $\vec E = -\dfrac{\sigma}{\varepsilon_0}\vec e_x$, et $\overrightarrow{\mathrm d\ell} = \mathrm dx\,\vec e_x$ le long du chemin $\mathcal C$ de $O$ vers $A$ :

$$
\int_{\mathcal C,\,O\to A}\vec E\cdot\overrightarrow{\mathrm d\ell} = \int_0^{L_x}\left(-\frac{\sigma}{\varepsilon_0}\right)\mathrm dx = -\frac{\sigma L_x}{\varepsilon_0}.
$$

Or $\displaystyle\int_O^A\vec E\cdot\overrightarrow{\mathrm d\ell} = V_O - V_A = -(V_A - V_O)$, donc la tension $v = V_A - V_O$ vaut :

$$
\boxed{v = V_A - V_O = \frac{\sigma L_x}{\varepsilon_0}}.
$$

### Q47

La **capacité** $C$ d'un condensateur est définie par la relation $q = C\,v$, où $q$ est la charge de l'armature portée au potentiel le plus élevé et $v$ la tension entre les armatures. Ici $q = \sigma S$ et $v = \dfrac{\sigma L_x}{\varepsilon_0}$, d'où

$$
C = \frac{q}{v} = \frac{\sigma S}{\sigma L_x/\varepsilon_0}
$$

soit

$$
\boxed{C = \frac{\varepsilon_0 S}{L_x}}.
$$

### Q48

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

### Q49

D'après $C = \dfrac{\varepsilon_0\varepsilon_r S}{L_x}$, on augmente la capacité en :
1. **augmentant la surface $S$** des armatures (limité par l'encombrement ; réalisé par enroulement des feuilles dans les condensateurs bobinés) ;
2. **diminuant la distance $L_x$** entre armatures (limité par le champ disruptif du diélectrique, qui provoque le claquage) ;
3. **augmentant la permittivité relative $\varepsilon_r$** du diélectrique intercalé (solution la plus efficace ; on emploie des céramiques de forte permittivité).

Ordres de grandeur usuels : de quelques **nanofarads** à quelques **microfarads** ; les **supercondensateurs**, à très grande surface développée (électrodes poreuses), atteignent des capacités de l'ordre du **farad**.

### Q50

L'**intensité** $i$ du courant électrique est le débit de charge à travers une section orientée de la surface : pendant la durée $\mathrm dt$, une charge $\delta q$ traverse la section (comptée positivement si elle traverse dans le sens choisi pour $i$), et

$$
\boxed{i = \frac{\delta q}{\mathrm dt}}.
$$

### Q51

**Bilan de charge** sur l'armature $\Pi_A$ (système = armature de charge $q$), en convention récepteur. Pendant $\mathrm dt$, la charge $\delta q = i\,\mathrm dt$ apportée par le fil (orienté dans le sens de $i$) s'accumule sur l'armature, qui ne laisse passer aucune charge vers l'autre armature : la variation de la charge d'état vaut $\mathrm dq = \delta q$. D'où

$$
\boxed{i = \frac{\mathrm dq}{\mathrm dt}}.
$$

L'orientation de $i$ (vers $\Pi_A$) est cohérente avec le sens d'accumulation de la charge dans ce bilan en convention récepteur.

### Q52

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

### Q53

Pour $t > 0$, $i(t) = \dfrac{U}{R}e^{-t/\tau} > 0$ et décroît.

Des charges **positives** circulent dans le sens de $i$ et s'accumulent sur l'armature $\Pi_A$ (sa charge $q = \sigma S > 0$ croît).

Tandis que l'armature $\Pi_0$ se charge négativement par influence totale. Physiquement, ce sont les **électrons** qui se déplacent en sens inverse de $i$, quittant $\Pi_A$. Lorsque $q \to CU$, le courant tend vers 0 : le mouvement cesse.

### V.2 — Chaîne de ressorts et polarisation piézoélectrique

### Q54

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

### Q55

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

### Q56

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

### Q57

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

### Q58

Le volume mésoscopique $\mathrm d\tau_M$ contient $N$ mailles sur une longueur $Na$ selon $\vec e_x$. Pour être mésoscopique, cette longueur doit être très grande devant la maille $a$ et très petite devant l'échelle macroscopique de variation des champs (ici la longueur $L$ du système, ou la longueur d'onde de la déformation) : le critère s'écrit

$$
\boxed{1 \ll N \quad\text{et}\quad Na \ll L} \qquad\text{(soit } 1 \ll N \ll N_x = L/a\text{)}.
$$

### Q59

Le moment dipolaire élémentaire contenu dans $\mathrm d\tau_M$ est la somme des moments des $N$ mailles :

$$
\overrightarrow{\mathrm dp_M} = \sum_{N\ \text{mailles}} \vec p_i.
$$

Le premier terme de Q57 donne $N$ fois $\dfrac{2\delta^2 E}{k_a+k_b}$. Dans le second, la somme $\sum\big(\widetilde{x_{A_i}} - \widetilde{x_{A_{i-1}}}\big)$ est **télescopique** : il reste $\widetilde{x_{A_{j+N}}} - \widetilde{x_{A_j}}$.

Or le champ de déplacement vérifie $\widetilde{x_{A_j}} = u(x)$ et $\widetilde{x_{A_{j+N}}} = u(x+\mathrm dx)$ (les points $A_j$ et $A_{j+N}$ sont en $x$ et $x+\mathrm dx$). D'où

$$
\boxed{\overrightarrow{\mathrm dp_M} = \left[\frac{2N\delta^2 E}{k_a+k_b} + \frac{\delta(k_b-k_a)}{k_a+k_b}\big(u(x+\mathrm dx) - u(x)\big)\right]\vec e_x}.
$$

### Q60

Le volume mésoscopique vaut $\mathrm d\tau_M = (Na)\,a^2 = Na^3$ et $\mathrm dx = Na$. Au premier ordre, $u(x+\mathrm dx) - u(x) = \dfrac{\mathrm du}{\mathrm dx}\,\mathrm dx = \dfrac{\mathrm du}{\mathrm dx}\,Na$. La polarisation $\vec P = \dfrac{\overrightarrow{\mathrm dp_M}}{\mathrm d\tau_M}$ vaut donc :

$$
\begin{aligned}
\vec P(M) &= \left[\frac{2N\delta^2 E}{(k_a+k_b)Na^3} + \frac{\delta(k_b-k_a)}{k_a+k_b}\cdot\frac{\frac{\mathrm du}{\mathrm dx}Na}{Na^3}\right]\vec e_x \\
&= \boxed{\left[\frac{2\delta^2}{(k_a+k_b)a^3}\,E + \frac{\delta(k_b-k_a)}{(k_a+k_b)a^2}\,\frac{\mathrm du}{\mathrm dx}\right]\vec e_x}.
\end{aligned}
$$

Le premier terme, proportionnel à $E$, existe dans tout **diélectrique**. Le second, proportionnel à $(k_b-k_a)\dfrac{\mathrm du}{\mathrm dx}$, s'annule si $k_a = k_b$ : c'est la **signature de l'effet piézoélectrique**, c'est-à-dire l'apparition d'une polarisation sous l'effet d'une déformation, même en l'absence de champ électrique appliqué.
