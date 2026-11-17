# Agrégation Physique — Problème de physique 2025 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Épreuve de 6 heures (session 2025, concours externe, section physique-chimie, option physique), sujet « Manipulation de macromolécules uniques » : 66 questions en trois parties — **A.** fonctionnement du dispositif de pinces magnétiques (champ de deux aimants, bille superparamagnétique, mesure de force par fluctuations thermiques puis par analyse de Fourier, mesure de position par diffraction) ; **B.** élasticité entropique de l'ADN (chaîne librement jointe 1D puis 3D, approche thermodynamique) ; **C.** modélisation de l'ADN comme longue tige flexible (traction, flexion, longueur de persistance, retour sur le « modèle du ver »). Principales données de l'énoncé : $L = 16{,}5\ \mu\text{m}$, diamètre de l'ADN $2{,}0$ nm, montée de $0{,}34$ nm par paire de bases, $K \simeq 350\ \text{kJ}\cdot\text{m}^{-3}$, $\ln(\tau_{\text{mes}}/\tau_0) \simeq 20$, $m_{\text{sat}} \simeq 10^{-12}\ \text{A}\cdot\text{m}^2$, $\Delta B = 0{,}5$ T sur $\Delta z = 5$ mm, diamètre de la bille $1\ \mu$m, $\eta = 1{,}0\times10^{-3}$ Pa·s, $a = 10\ \mu$m, $\lambda \simeq 650$ nm, pixels de $10\ \mu$m, $k = (7{,}70 \pm 0{,}40)\times10^{-6}\ \text{pN}\cdot\text{nm}^{-1}$ (ajustement de la Figure 7).

---

## Partie A — Fonctionnement du dispositif

**A.1. Piégeage de la bille magnétique**

### A.1.1. Création du champ magnétique

### Question 1

Un dipôle magnétique permanent de moment $\vec M$ placé dans un champ $\vec B$ a pour énergie potentielle

$$
E_p = -\vec M\cdot\vec B.
$$

Le couple qui aligne le dipôle sur le champ est $\vec\Gamma = \vec M\times\vec B$ ; la force s'obtient à $\vec M$ fixé par $\vec F = -\vec\nabla E_p$ :

$$
\boxed{\vec F = \vec\nabla(\vec M\cdot\vec B).}
$$

La force est donc non nulle **uniquement si le champ est non uniforme** : un champ uniforme ne produit qu'un couple.

### Question 2

Schéma : axe horizontal $\vec e_x$ portant les deux aimants, de moments $\vec M_1 = \vec M_2 = M\vec e_x$, placés en $x = -d/2$ et $x = +d/2$ ; $O$ est le milieu ; axe vertical $\vec e_z$.

Rappel du champ créé par un dipôle $\vec M$ en un point situé au vecteur $\vec r$ (de la source vers le point) :

$$
\vec B(\vec r) = \frac{\mu_0}{4\pi}\,\frac{3(\vec M\cdot\vec r)\,\vec r - r^2\,\vec M}{r^5}.
$$

Pour le dipôle 1, $\vec r_1 = \overrightarrow{P_1O} = \tfrac d2\vec e_x$ :

$$
\vec B_1(O) = \frac{\mu_0}{4\pi}\,\frac{2M}{(d/2)^3}\,\vec e_x.
$$

Pour le dipôle 2, $\vec r_2 = -\tfrac d2\vec e_x$ : la composante selon $\vec e_x$ est identique. En sommant :

$$
\boxed{\vec B(O) = \frac{\mu_0}{4\pi}\,\frac{32\,M}{d^3}\,\vec e_x = \frac{8\mu_0 M}{\pi d^3}\,\vec e_x.}
$$

### Question 3

Soit $P = (0,z)$. On pose $\rho = \sqrt{(d/2)^2 + z^2}$ ; $\vec r_{1,2} = (\pm\tfrac d2, z)$ et $\vec M\cdot\vec r_{1,2} = \pm M\tfrac d2$. La composante selon $\vec e_x$ est la même pour les deux dipôles ; les composantes selon $\vec e_z$, proportionnelles à $\pm\tfrac{Md}{2}z$, se compensent par symétrie. Il reste

$$
\boxed{\vec B(P) = \frac{\mu_0 M}{2\pi}\,\frac{\tfrac{d^2}{2} - z^2}{\big((\tfrac d2)^2 + z^2\big)^{5/2}}\,\vec e_x.}
$$

On vérifie qu'en $z = 0$ on retrouve le résultat de la question 2. Le champ s'annule lorsque $\tfrac{d^2}{2} - z^2 = 0$, soit

$$
\boxed{z = \pm\frac{d}{\sqrt2}.}
$$

### A.1.2. Bille superparamagnétique

### Question 4

Un milieu magnétique est (i) **linéaire** si son aimantation $\vec M$ dépend linéairement de l'excitation $\vec H$ ; (ii) **homogène** si ses propriétés magnétiques sont identiques en tout point ; (iii) **isotrope** si elles sont identiques dans toutes les directions. La relation constitutive générale s'écrit

$$
\boxed{\vec B = \mu_0(\vec H + \vec M)},
$$

où $\vec B$ est le champ magnétique (tesla), $\vec H$ l'excitation magnétique (A·m⁻¹) et $\vec M$ l'aimantation, moment magnétique volumique (A·m⁻¹). $\vec H$ et $\vec M$ ont la même unité ; $\vec B$ n'a pas la même.

### Question 5

En l'absence d'aimantation permanente, on linéarise au premier ordre : $\vec M = \chi_m\vec H$, avec $\chi_m$ sans dimension (susceptibilité magnétique). Alors

$$
\vec B = \mu_0(\vec H + \chi_m\vec H) = \mu_0(1+\chi_m)\vec H,
$$

soit

$$
\boxed{\mu = \mu_0(1+\chi_m).}
$$

### Question 6

- Courbe **(A)**, pente **négative** ($\chi_m < 0$) : matériau **diamagnétique** — aimantation induite opposée au champ, $|\chi_m| \sim 10^{-5}$.
- Courbe **(B)**, droite de pente **positive** : matériau **paramagnétique** — moments alignés par le champ, $\chi_m > 0$ faible.
- Courbe **(C)**, saturation et **cycle d'hystérésis** : matériau **ferromagnétique** — aimantation rémanente, domaines de Weiss.

### Question 7

Si $\tau_{\text{mes}} \gg \tau$, le moment de la nanoparticule bascule de nombreuses fois entre ses deux directions pendant la durée de mesure. En champ nul, les deux orientations ont la même énergie (Boltzmann) et sont équiprobables : la **moyenne temporelle de l'aimantation est nulle**. C'est le **superparamagnétisme**, par analogie avec le paramagnétisme : comme pour un paramagnétique, il n'y a **aucune aimantation rémanente** en champ nul ; la différence est que le « moment » qui fluctue est le moment géant du mono-domaine ferromagnétique (d'où le « super »).

### Question 8

Le blocage apparaît lorsque $\tau_{\text{mes}} = \tau$. Avec la loi d'Arrhenius $\tau = \tau_0\exp\!\big(\tfrac{Kv}{k_BT}\big)$ :

$$
\tau_{\text{mes}} = \tau_0\exp\!\Big(\frac{Kv}{k_BT_B}\Big)\ \Rightarrow\ \boxed{T_B = \frac{Kv}{k_B\,\ln(\tau_{\text{mes}}/\tau_0)}.}
$$

La particule est **bloquée** (moment figé) si $T < T_B$, c'est-à-dire si $\tau > \tau_{\text{mes}}$ : à basse température le retournement est trop lent devant le temps de mesure.

### Question 9

On impose $T_B \geq T \simeq 300$ K, soit

$$
v \geq \frac{k_BT\,\ln(\tau_{\text{mes}}/\tau_0)}{K} = \frac{1{,}38\times10^{-23}\times300\times20}{350\times10^{3}} \approx 2{,}4\times10^{-25}\ \text{m}^3.
$$

Pour une nanoparticule sphérique de diamètre $D = (6v/\pi)^{1/3}$ :

$$
\boxed{D \approx 7{,}6\ \text{nm}}
$$

(soit un côté $a \approx 6$ nm pour un cube). Les nanoparticules doivent mesurer **quelques nanomètres**, cohérent avec le caractère mono-domaine.

### A.1.3. Force magnétique sur la bille

### Question 10

Schéma attendu : courbe $m(B)$ impaire, linéaire à l'origine ($m = \alpha B$), saturant à $\pm m_{\text{sat}}$ à fort champ, **sans hystérésis**.

La bille se comporte comme un **paramagnétique saturable** : réponse linéaire à faible champ (comme la courbe B), saturation à fort champ (comme un ferromagnétique, courbe C), mais **sans rémanence ni hystérésis** — signature du superparamagnétisme.

### Question 11

À saturation, $\vec m_{\text{sat}}$ est constant et aligné sur $\vec B$. L'énergie magnétique vaut $E_p = -\tfrac12\vec m_{\text{sat}}\cdot\vec B$ (le facteur $\tfrac12$ vient de la construction progressive de l'aimantation), d'où

$$
\vec F = -\vec\nabla E_p = \frac12\vec\nabla(\vec m_{\text{sat}}\cdot\vec B) = \frac12\,m_{\text{sat}}\,\vec\nabla B.
$$

En ordre de grandeur, $\|\vec\nabla B\| \sim \dfrac{\Delta B}{\Delta z} = \dfrac{0{,}5}{5\times10^{-3}} = 100\ \text{T}\cdot\text{m}^{-1}$ :

$$
F \approx \frac12\,m_{\text{sat}}\,\frac{\Delta B}{\Delta z} = \frac12\times10^{-12}\times100 = \boxed{5\times10^{-11}\ \text{N} \approx 50\ \text{pN}.}
$$

## A.2. Mesures de force

### A.2.1. Modèle de pendule inversé

### Question 12

Schéma : ancrage en $O$ (en bas), bille en haut, fil de longueur $L$ faisant l'angle $\beta$ avec la verticale ; force magnétique $\vec F = F\vec e_z$ vers le haut ; tension $\vec F_t = -F_t\vec e_r$ dirigée de la bille vers $O$ ($F_t \geq 0$, un fil ne peut que tirer) ; poids négligé.

À l'équilibre : $\vec F + \vec F_t = \vec 0$, soit $F\vec e_z = F_t\vec e_r$. Deux vecteurs colinéaires de même sens imposent $\vec e_r = \vec e_z$, d'où

$$
\boxed{\beta = 0,}
$$

la bille est à la verticale de l'ancrage. L'énergie potentielle $E_p = -FL\cos\beta$ est **minimale** en $\beta = 0$ : l'équilibre est **stable**.

### Question 13

La bille décrit un cercle de rayon $L$ : $\vec a = -L\dot\beta^2\vec e_r + L\ddot\beta\,\vec e_\theta$, avec $\vec e_z = \cos\beta\,\vec e_r - \sin\beta\,\vec e_\theta$. Le PFD $m\vec a = F\vec e_z - F_t\vec e_r$ se projette sur $(\vec e_r, \vec e_\theta)$ :

$$
\text{(}\vec e_\theta\text{) : }\ mL\ddot\beta = -F\sin\beta\ \Rightarrow\ \boxed{mL\ddot\beta + F\sin\beta = 0,}
$$

$$
\text{(}\vec e_r\text{) : }\ -mL\dot\beta^2 = F\cos\beta - F_t\ \Rightarrow\ \boxed{F_t = F\cos\beta + mL\dot\beta^2.}
$$

Le signe **+** devant $F\sin\beta$ est un rappel vers $\beta = 0$.

### Question 14

Avec $z = L\cos\beta$ : $E_p = -Fz = -FL\cos\beta$ et $E_c = \tfrac12 mL^2\dot\beta^2$, d'où

$$
E_m(\beta,\dot\beta) = \frac12 mL^2\dot\beta^2 - FL\cos\beta.
$$

La tension est portée par $\vec e_r$ et la vitesse $\vec v = L\dot\beta\,\vec e_\theta$ est tangente : $\vec F_t\cdot\vec v = 0$, **la tension ne travaille pas**. L'énergie magnétique étant conservative, $E_m$ se conserve :

$$
\frac{dE_m}{dt} = mL^2\dot\beta\ddot\beta + FL\sin\beta\,\dot\beta = 0\ \Rightarrow\ mL\ddot\beta + F\sin\beta = 0,
$$

identique à la question 13.

### Question 15

Pour $\beta \ll 1$, $\sin\beta = \beta + O(\beta^3) \approx \beta$. L'équation devient

$$
\ddot\beta + \frac{F}{mL}\,\beta = 0,
$$

équation de l'**oscillateur harmonique**, de pulsation propre

$$
\boxed{\omega_0 = \sqrt{\frac{F}{mL}}.}
$$

### Question 16

Dans l'expérience réelle, la bille est immergée dans un solvant à la température $T$ : elle subit en permanence les chocs des molécules du solvant. C'est l'**agitation thermique (mouvement brownien)** qui excite aléatoirement l'oscillateur, tandis que la **viscosité** du solvant l'amortit. L'angle $\beta$ oscille ainsi autour de $\beta = 0$ : on a un **oscillateur harmonique amorti, forcé par un bruit thermique** (équation de Langevin).

### A.2.2. Fluctuations thermiques

### Question 17

$E_p(\beta) = -FL\cos\beta \approx -FL + \tfrac12 FL\beta^2$ au voisinage de $\beta = 0$. Pour $\beta \ll 1$, $x = L\sin\beta \approx L\beta$, donc $\beta \approx x/L$ :

$$
\boxed{E_p(x) \approx -FL + \frac12\,\frac{F}{L}\,x^2.}
$$

C'est un potentiel **parabolique** : le mouvement horizontal est gouverné par une force de rappel élastique de raideur $k = F/L$, comme un ressort.

### Question 18

Le degré de liberté $x$ a une énergie potentielle quadratique $\tfrac12 kx^2$ avec $k = F/L$. Le théorème d'**équipartition** lui attribue une énergie moyenne $\tfrac12 k_BT$ :

$$
\frac12 k\,\langle x^2\rangle = \frac12 k_BT\ \Rightarrow\ \frac12\frac FL\langle x^2\rangle = \frac12 k_BT,
$$

d'où

$$
\boxed{F = \frac{L\,k_BT}{\langle x^2\rangle}.}
$$

Ici $\langle x\rangle = 0$ : la variance du déplacement vaut $\langle x^2\rangle$, c'est-à-dire le **carré de l'écart-type** lu sur la largeur de la gaussienne ajustant l'histogramme $\mathcal P(x)$.

### Question 19

L'histogramme de la Figure 5 a un écart-type $\sqrt{\langle x^2\rangle} \approx 0{,}15\ \mu\text{m} = 1{,}5\times10^{-7}$ m, soit $\langle x^2\rangle \approx 2{,}3\times10^{-14}\ \text{m}^2$. Avec $L \simeq 16{,}5\ \mu$m et $k_BT \simeq 4{,}1\times10^{-21}$ J :

$$
F = \frac{16{,}5\times10^{-6}\times4{,}1\times10^{-21}}{2{,}3\times10^{-14}} \approx \boxed{3\ \text{pN}}
$$

(quelques pN ; toute valeur de l'ordre du pN cohérente avec la lecture graphique est acceptable).

### Question 20

À l'équilibre thermique, la probabilité de présence suit la statistique de Boltzmann :

$$
\mathcal P(x) \propto e^{-E_p(x)/k_BT} = e^{-\frac{Fx^2}{2Lk_BT}}.
$$

Le potentiel étant **quadratique** en $x$ (Q17), $\mathcal P(x)$ est une **gaussienne** centrée en 0, de variance $\langle x^2\rangle = Lk_BT/F$ : l'ajustement gaussien de l'histogramme est justifié.

### A.2.3. Analyse de Fourier

### Question 21

Dans l'équation de Langevin $m\ddot x = -\gamma\dot x - \tfrac FL x + \xi(t)$ :
- $m\ddot x$ : terme d'**inertie** de la bille ;
- $-\gamma\dot x$ : **frottement visqueux** du solvant (traînée de Stokes) ;
- $-\tfrac FL x$ : **force de rappel élastique** de raideur $k = F/L$ (Q17) ;
- $\xi(t)$ : **force aléatoire** modélisant le bruit thermique (chocs browniens).

### Question 22

Sans le terme d'inertie : $\gamma\dot x + \tfrac FL x = \xi$. Par transformée de Fourier, $\mathrm{TF}[\dot x] = i\omega X(\omega)$ :

$$
\Big(i\gamma\omega + \frac FL\Big)X(\omega) = \Xi(\omega)\ \Rightarrow\ \boxed{X(\omega) = \frac{\Xi(\omega)}{\frac FL + i\gamma\omega}.}
$$

### Question 23

$$
S_{xx}(\omega) = |X(\omega)|^2 = \frac{|\Xi(\omega)|^2}{(F/L)^2 + \gamma^2\omega^2} = \frac{1}{(F/L)^2}\,\frac{S_{\xi\xi}(\omega)}{1 + \big(\tfrac{\gamma L}{F}\big)^2\omega^2}.
$$

Par identification avec la forme (3) :

$$
\boxed{A = \frac{L^2}{F^2},\qquad \omega_c = \frac{F}{\gamma L}.}
$$

### Question 24

Le bruit thermique étant blanc, $S_{\xi\xi} = 2\gamma k_BT$ est constant :

$$
\boxed{S_{xx}(\omega) = \frac{2\gamma k_BT\,L^2/F^2}{1 + (\omega/\omega_c)^2},\qquad \omega_c = \frac{F}{\gamma L}.}
$$

C'est une **lorentzienne** : plateau $S_{xx}(0) = 2\gamma k_BT L^2/F^2$ aux basses fréquences, puis décroissance en $\omega^{-2}$ au-delà de $\omega_c$.

### Question 25

Loi de Stokes avec le **rayon** $r = 0{,}5\ \mu\text{m} = 5\times10^{-7}$ m (et non le diamètre) :

$$
\gamma = 6\pi\eta r = 6\pi\times1{,}0\times10^{-3}\times5\times10^{-7} \approx \boxed{9{,}4\times10^{-9}\ \text{N}\cdot\text{s}\cdot\text{m}^{-1}.}
$$

### Question 26

La densité spectrale de la Figure 6 présente un plateau puis un coude : on lit $f_c \approx 1$ Hz. Avec $\omega_c = 2\pi f_c$ et $\omega_c = F/(\gamma L)$ (Q23) :

$$
F = \gamma L\,\omega_c = \gamma L\,2\pi f_c = 9{,}4\times10^{-9}\times16{,}5\times10^{-6}\times2\pi\times1 \approx \boxed{1\ \text{pN}.}
$$

Ordre de grandeur **cohérent** avec la méthode directe de la question 19 (quelques pN) ; la méthode fréquentielle est plus précise car elle s'affranchit des vibrations externes.

## A.3. Mesures de position

### A.3.1. Position horizontale

### Question 27

La **diffraction de Fraunhofer** (champ lointain) s'applique lorsque source et écran sont « à l'infini » (ou dans les plans focaux d'une lentille) : l'amplitude diffractée est alors la transformée de Fourier spatiale de la pupille. Condition de champ lointain : $z \gg a^2/\lambda$ (nombre de Fresnel $\ll 1$).

Pour une pupille **circulaire** de rayon $a$, on observe une **tache d'Airy** : disque central brillant cerné d'**anneaux concentriques** alternativement sombres et clairs, d'intensité décroissante ; le premier anneau sombre est en $\theta_1 \simeq 1{,}22\,\lambda/a$.

### Question 28

La bille opaque est l'**écran complémentaire** d'une ouverture circulaire de même rayon. Par le **théorème de Babinet**, les figures de diffraction de deux écrans complémentaires sont identiques partout **sauf** dans la direction de l'onde non diffractée :
- hors de l'axe, on retrouve la même structure d'**anneaux d'Airy** (mêmes positions) ;
- au centre persiste le faisceau transmis non diffracté, et sur l'axe apparaît un point brillant, la **tache d'Arago-Poisson** ; les contrastes sont inversés par rapport au fond éclairé.

### Question 29

La lentille de focale $f'$ forme la figure de diffraction dans son plan focal image : la direction $\theta_1$ se projette à la distance $r_1 = f'\tan\theta_1 \approx f'\theta_1$ (petits angles). Le **diamètre** du premier anneau sombre vaut donc

$$
\boxed{d_1 = 2f'\theta_1 = \frac{2{,}44\,\lambda f'}{a}.}
$$

### Question 30

Critère d'échantillonnage (Nyquist) : il faut que le disque central de la tache d'Airy s'étale sur au moins deux pixels, $d_1 \gtrsim 2p = 20\ \mu$m. Avec $a = 10\ \mu$m et $\lambda \approx 650$ nm :

$$
f' \gtrsim \frac{d_1\,a}{2{,}44\,\lambda} = \frac{20\times10^{-6}\times10\times10^{-6}}{2{,}44\times650\times10^{-9}} \approx \boxed{1{,}3\times10^{-4}\ \text{m}.}
$$

Il faut une focale d'au moins ≈ 0,1 mm ; en pratique on choisira une focale sensiblement plus grande, qui sur-échantillonne et garantit la résolution.

### A.3.2. Position verticale

### Question 31

**Objectif** : ajuster un modèle $f(x,\vec p)$ à un nuage de mesures $\{(x_i,y_i)\}$. **Principe** : minimiser la somme des carrés des résidus

$$
\boxed{S(\vec p) = \sum_i \big[y_i - f(x_i,\vec p)\big]^2,}
$$

la minimisation portant sur les **paramètres $\vec p$** du modèle (on annule $\partial S/\partial p_k$). Ici, on compare le profil radial mesuré à chaque profil de référence.

### Question 32

La grandeur ajustée est la **position verticale $z$ de la bille** (distance au plan focal) : on cherche le profil de référence, donc le $z$, qui minimise $S$ par rapport au profil mesuré.

### Question 33

Les deux emplacements reçoivent la somme des carrés des résidus pour la valeur courante de `A` :
```python
quantite_prec = sum((ydata - func(xdata, A))**2)
# ...
quantite_actu = sum((ydata - func(xdata, A))**2)
```
La boucle incrémente `A` de `step` tant que $S$ varie de plus que `tolerance`.

**Effet de `step`** : un pas **trop grand** rend l'optimisation rapide mais grossière (on risque de « sauter » par-dessus le minimum) ; un pas **trop petit** donne une grande précision mais une convergence lente et peut provoquer un arrêt prématuré dans une zone plate (faux minimum local).

---

## Partie B — Élasticité de l'ADN

**B.1. Un comportement élastique**

### Question 34

Sur l'agrandissement de la Figure 7, l'extension croît approximativement **linéairement** avec la force aux faibles forces ($f \lesssim 0{,}2$ pN, extensions $z$ jusqu'à ≈ 8–10 µm) : c'est la signature d'un régime **élastique** (loi de Hooke). La raideur est l'ordre de grandeur de la pente :

$$
k \sim \frac{\Delta f}{\Delta z} \approx \frac{0{,}1\times10^{-12}\ \text{N}}{5\times10^{-6}\ \text{m}} \approx \boxed{2\times10^{-8}\ \text{N}\cdot\text{m}^{-1}}
$$

(quelques $10^{-8}$ S.I.).

### Question 35

Le régime élastique s'étend jusqu'à des extensions $z \approx 8$–$10\ \mu$m, soit **environ la moitié** de la longueur étirée $L = 16{,}5\ \mu$m : l'ADN se comporte élastiquement **bien avant d'être complètement étiré**. L'élasticité ne provient donc pas de l'étirement des liaisons chimiques du squelette (qui n'interviendrait qu'au voisinage immédiat de $L$), mais du **dépliement d'une conformation enroulée** : un modèle de chaîne de polymère (élasticité entropique) est nécessaire.

**B.2. Élasticité entropique**

### Question 36

L'extension globale est $z = \sum_{i=1}^N z_i$ avec $z_i = \pm\ell$. À force nulle, les deux orientations sont équiprobables : $\langle z_i\rangle = 0$, donc

$$
\boxed{\langle z\rangle = 0.}
$$

Pour la variance, les orientations étant **indépendantes**, les termes croisés $i\neq j$ s'annulent ($\langle z_iz_j\rangle = \langle z_i\rangle\langle z_j\rangle = 0$) et il reste $\langle z_i^2\rangle = \ell^2$ :

$$
\langle z^2\rangle = N\ell^2 = (N\ell)\,\ell = \boxed{\ell L.}
$$

### Question 37

La marche aléatoire 1D donne $\langle x^2\rangle = 2Dt = N\,\delta x^2$ (avec $D = \delta x^2/(2\delta t)$ et $t = N\delta t$). La chaîne librement jointe donne $\langle z^2\rangle = N\ell^2$. Même forme $N \times (\text{pas})^2$, avec la correspondance :

$$
\boxed{\langle z^2\rangle \leftrightarrow \langle x^2\rangle,\quad N\ \text{monomères} \leftrightarrow N\ \text{pas},\quad \ell \leftrightarrow \delta x.}
$$

La configuration du polymère est une marche aléatoire 1D dont les « pas » sont les monomères.

### Question 38

Pour une force $f$ constante, le travail de traction de 0 à $z$ est $W = \int_0^z f\,dz' = fz$. L'énergie potentielle associée (dont dérive la force, $f = -\partial U/\partial z$) est donc

$$
\boxed{U = -f\,z.}
$$

Par monomère : $u_i = -fz_i = \mp f\ell$.

### Question 39

Chaque monomère est un système à deux niveaux d'énergies $\mp f\ell$. Avec $u = f\ell/k_BT$, la statistique de Boltzmann donne

$$
p_+ = \frac{e^{u}}{e^{u}+e^{-u}},\qquad p_- = \frac{e^{-u}}{e^{u}+e^{-u}},
$$

et l'orientation moyenne vaut

$$
\langle z_i\rangle = \ell\,p_+ - \ell\,p_- = \ell\,\frac{e^u - e^{-u}}{e^u + e^{-u}} = \boxed{\ell\tanh\!\Big(\frac{f\ell}{k_BT}\Big).}
$$

### Question 40

Les $N$ monomères étant indépendants :

$$
\boxed{\langle z\rangle = N\langle z_i\rangle = N\ell\tanh\!\Big(\frac{f\ell}{k_BT}\Big) = L\tanh\!\Big(\frac{f\ell}{k_BT}\Big).}
$$

Schéma attendu : courbe impaire $\langle z\rangle/L = \tanh(f\ell/k_BT)$, de pente 1 à l'origine, tendant vers l'asymptote horizontale $+1$ (axes légendés).

### Question 41

- **Grandes forces** ($f\ell/k_BT \gg 1$) : $\tanh \to 1$, donc $\langle z\rangle \to L = N\ell$ : la chaîne est complètement étirée. Ce n'est réaliste que jusqu'à l'étirement complet : le modèle 1D sature à $L$ et ne décrit pas le sur-étirement des liaisons au-delà.
- **Petites forces** ($f\ell/k_BT \ll 1$) : $\tanh u \approx u$, donc $\langle z\rangle \approx L\,\dfrac{f\ell}{k_BT} = \dfrac{N\ell^2 f}{k_BT}$ : réponse **linéaire** (élastique) en force.

### Question 42

À l'équilibre, la molécule exerce sur l'opérateur une force opposée à la traction. Dans le régime linéaire (Q41), $f = \dfrac{k_BT}{N\ell^2}\langle z\rangle$, donc

$$
\boxed{\vec f_{\text{ADN}} = -\frac{k_BT}{N\ell^2}\,\langle z\rangle\,\vec e_z.}
$$

Cette force de rappel est **proportionnelle à $T$** et ne provient d'aucune variation d'énergie interne ($U = 0$) : elle traduit la tendance du système vers l'état le plus désordonné (le plus probable). C'est l'élasticité **entropique**.

### Question 43

De $f = \dfrac{k_BT}{N\ell^2}\langle z\rangle = k^{1D}_{\text{ADN}}\langle z\rangle$ :

$$
\boxed{k^{1D}_{\text{ADN}} = \frac{k_BT}{N\ell^2} = \frac{k_BT}{L\ell}.}
$$

Homogénéité : $[k_BT] = \text{J} = \text{N}\cdot\text{m}$ et $[L\ell] = \text{m}^2$, donc $[k] = \text{N}\cdot\text{m}^{-1}$ : c'est bien une raideur.

### Modèle 3D

### Question 44

On repère l'orientation de chaque monomère $\vec r_i$ par ses **coordonnées sphériques** $(\theta_i,\phi_i)$, l'axe polaire étant celui de la force $\vec f = f\vec e_z$. La projection sur $\vec e_z$ vaut $\ell\cos\theta_i$ et l'énergie $u_i = -\vec f\cdot\vec r_i = -f\ell\cos\theta_i$. Le poids de Boltzmann de l'état du système étant $\propto \exp\!\big(\tfrac{f\ell}{k_BT}\sum_i\cos\theta_i\big)$, la moyenne de $z = \sum_i\ell\cos\theta_i$ s'obtient en intégrant sur toutes les orientations (élément d'angle solide $\sin\theta_i\,d\theta_i\,d\phi_i$), normalisée par $Z$ : c'est exactement l'équation (5).

### Question 45

L'exponentielle d'une somme se factorise et les variables $(\theta_i,\phi_i)$ sont indépendantes :

$$
Z = \prod_{i=1}^N \int_0^{2\pi}\!d\phi_i\int_0^\pi\!\sin\theta_i\,d\theta_i\,e^{\frac{f\ell\cos\theta_i}{k_BT}},
$$

soit

$$
\boxed{Z = \Big(\int_0^{2\pi}\!d\phi\int_0^\pi\!\sin\theta\,d\theta\,e^{\frac{f\ell\cos\theta}{k_BT}}\Big)^{\!N}.}
$$

### Question 46

Posons $u = f\ell/k_BT$. Avec $c = \cos\theta$ :

$$
\int_0^\pi \sin\theta\,e^{u\cos\theta}d\theta = \int_{-1}^{1} e^{uc}dc = \frac{e^u - e^{-u}}{u} = \frac{2\sinh u}{u},
$$

donc $Z = \big(\tfrac{4\pi\sinh u}{u}\big)^N$ et $\ln Z = N[\ln(4\pi) + \ln\sinh u - \ln u]$. Comme $\langle z\rangle = k_BT\,\partial\ln Z/\partial f$ et $\partial u/\partial f = \ell/k_BT$ :

$$
\langle z\rangle = k_BT\cdot N\Big(\coth u - \frac1u\Big)\frac{\ell}{k_BT},
$$

soit

$$
\boxed{\langle z\rangle = N\ell\Big[\coth\!\Big(\frac{f\ell}{k_BT}\Big) - \frac{k_BT}{f\ell}\Big].}
$$

On reconnaît la **fonction de Langevin** $\mathcal L(u) = \coth u - 1/u$.

### Question 47

- **Grande force** ($u \gg 1$) : $\coth u \to 1$ et $1/u \to 0$, donc $\langle z\rangle \to N\ell = L$ : même saturation qu'en 1D.
- **Petite force** ($u \ll 1$) : avec $\coth u = \tfrac1u + \tfrac u3 + O(u^3)$, on a $\coth u - \tfrac1u \approx \tfrac u3$, d'où

$$
\langle z\rangle \approx N\ell\,\frac u3 = \frac{N\ell^2 f}{3k_BT} = \frac{L\ell\,f}{3k_BT}.
$$

Soit $f = \dfrac{3k_BT}{L\ell}\langle z\rangle$, et la raideur 3D :

$$
\boxed{k^{3D}_{\text{ADN}} = \frac{3k_BT}{L\ell}.}
$$

La chaîne 3D est **trois fois plus raide** que la chaîne 1D : seule la fraction $1/3$ des fluctuations d'orientation contribue à l'axe $z$.

**B.3. Élasticité entropique : thermodynamique**

### Question 48

- Force nulle : chaque monomère a 2 orientations indépendantes, donc $\Omega_{f=0} = 2^N$.
- Force élevée : tous les monomères alignés, $\Omega = 1$.

Avec $S = k_B\ln\Omega$ : $S_{f=0} = Nk_B\ln2$ et $S_{f\gg f_0} = 0$. Application numérique ($N = 100$) :

$$
S_{f=0} = 100\times1{,}38\times10^{-23}\times\ln2 \approx \boxed{9{,}6\times10^{-22}\ \text{J}\cdot\text{K}^{-1}},\qquad S_{f\gg f_0} = 0.
$$

### Question 49

- **Énergie interne nulle** : dans ce modèle, les monomères sont articulés librement, sans interaction ni énergie de courbure — aucune configuration ne coûte d'énergie, donc $U = 0$ (hors énergie cinétique).
- **Énergie libre** : $\mathcal F = U - TS = -TS = -TS_0 + \dfrac{3k_BT}{2N\ell^2}z^2$.
- **Force conjuguée** de l'extension, à $T$ fixée : $f = \big(\partial\mathcal F/\partial z\big)_T = \dfrac{3k_BT}{N\ell^2}z = \dfrac{3k_BT}{L\ell}z$.
- **Comparaison** : loi linéaire de raideur

$$
\boxed{k = \frac{3k_BT}{L\ell} = k^{3D}_{\text{ADN}},}
$$

**identique** au résultat de la question 47 : les approches statistique (B.2) et thermodynamique (B.3) sont cohérentes. L'origine est bien entropique ($\mathcal F = -TS$, $U = 0$).

---

## Partie C — Modélisation de l'ADN comme une longue tige flexible

**C.1. Ajustement avec le « modèle du ver »**

### Question 50

Pour $z/L \ll 1$, $(1 - z/L)^{-2} \approx 1 + 2\tfrac zL$. Le crochet de la loi (11) devient

$$
\frac zL - \frac14 + \frac14\Big(1 + 2\frac zL\Big) = \frac zL + \frac z{2L} = \frac{3z}{2L},
$$

d'où

$$
f \approx \frac{2k_BT}{\ell}\cdot\frac{3z}{2L} = \frac{3k_BT}{L\ell}\,z,
$$

comportement élastique de raideur $k = \dfrac{3k_BT}{L\ell} = k^{3D}_{\text{ADN}}$ (équation 9) : le « modèle du ver » redonne bien l'élasticité entropique à faible force.

### Question 51

On inverse $k = 3k_BT/(L\ell)$. Avec $k_BT \simeq 4{,}1$ pN·nm (à 300 K) et $L = 16{,}5\ \mu$m $= 1{,}65\times10^4$ nm :

$$
\ell = \frac{3k_BT}{L\,k} = \frac{3\times4{,}1}{1{,}65\times10^4\times7{,}70\times10^{-6}} \approx \boxed{98\ \text{nm}.}
$$

**Incertitude** : $\dfrac{\Delta\ell}{\ell} = \dfrac{\Delta k}{k} = \dfrac{0{,}40}{7{,}70} \approx 5{,}2\ \%$, soit $\Delta\ell \approx 5$ nm : $\ell = (98 \pm 5)$ nm $\approx 100$ nm.

D'après la Figure 1, la montée est de $0{,}34$ nm par paire de bases, donc

$$
n_\ell = \frac{\ell}{0{,}34} \approx \frac{98}{0{,}34} \approx \boxed{290\ \text{paires de bases}}
$$

(ordre de grandeur ~300).

**C.2. L'ADN comme une tige élastique : traction**

### Question 52

$\sigma = Y\varepsilon$ avec $\sigma$ une contrainte (Pa) et $\varepsilon$ sans dimension : le module de Young $Y$ s'exprime en **pascals** (Pa = N·m⁻²). Or $\text{N}\cdot\text{m}^{-2} = \text{J}\cdot\text{m}^{-3}$ : $Y$ a la dimension d'une **énergie par unité de volume**. Microscopiquement, $Y$ mesure la raideur des liaisons interatomiques multipliée par leur densité : c'est l'ordre de grandeur de l'énergie de cohésion stockée par unité de volume lors de la déformation.

### Question 53

Énergie de liaison $\sim 1$ eV $= 1{,}6\times10^{-19}$ J ; densité $\sim 1$ liaison par Å³ $= 10^{-30}$ m³ :

$$
Y \sim \frac{1{,}6\times10^{-19}}{10^{-30}} = \boxed{1{,}6\times10^{11}\ \text{Pa} \approx 160\ \text{GPa}.}
$$

Cohérent avec les solides durs du Tableau 1 (acier 200 GPa, cuivre 117 GPa, diamant ≈ 1000 GPa).

### Question 54

Loi de Hooke : $f = \dfrac{YA}{L}\Delta L$ avec $A = \pi r^2$. L'énergie d'étirement est le travail de cette force **intégré** de 0 à $\Delta L$ (la force croît avec l'allongement) :

$$
E_{\text{étirem}} = \int_0^{\Delta L} \frac{YA}{L}x\,dx = \boxed{\frac{\pi r^2 Y}{2L}\,\Delta L^2.}
$$

Par unité de volume ($V = AL$) : $e_{\text{étirem}} = \dfrac{Y}{2}\big(\tfrac{\Delta L}{L}\big)^2$, d'où

$$
\boxed{\alpha = \frac Y2.}
$$

**C.3. Flexion et longueur de persistance**

### C.3.1. Énergie de courbure

### Question 55

La section droite est un disque de rayon $r$. À la hauteur $z$ ($-r \le z \le r$), la largeur est la corde du cercle :

$$
\boxed{w(z) = 2\sqrt{r^2 - z^2}.}
$$

La tranche entre $z$ et $z+dz$, de longueur $L$, a pour volume

$$
\boxed{dv(z) = w(z)\,L\,dz = 2L\sqrt{r^2-z^2}\,dz.}
$$

### Question 56

La fibre neutre (au centre) a pour longueur $L = R\theta$. La fibre à la hauteur $z$ a un rayon de courbure $R+z$, donc une longueur $L(z) = (R+z)\theta = L(1 + z/R)$. Son allongement est

$$
\boxed{\Delta L(z) = L(z) - L = \frac{Lz}{R}}\quad\Rightarrow\quad \frac{\Delta L(z)}{L} = \frac zR.
$$

La déformation locale $\varepsilon(z) = z/R$ varie linéairement avec la distance à l'axe neutre.

### Question 57

La densité d'énergie locale (Q54) est $e_{\text{étirem}}(z) = \dfrac Y2\big(\tfrac{z}{R}\big)^2$. En intégrant sur le volume :

$$
E_{\text{flexion}} = \int_{-r}^{r} \frac Y2\frac{z^2}{R^2}\,2L\sqrt{r^2-z^2}\,dz = \frac{YL}{R^2}\int_{-r}^{r} z^2\sqrt{r^2-z^2}\,dz.
$$

Avec $z = rx$, l'intégrale vaut $r^4\int_{-1}^1 x^2\sqrt{1-x^2}\,dx = r^4\cdot\dfrac\pi8$ (donnée du préambule), d'où

$$
E_{\text{flexion}} = \frac{YL}{R^2}\cdot\frac{\pi r^4}{8} = \frac12\,\frac{\pi r^4 Y}{4}\cdot\frac{L}{R^2},
$$

soit la forme (12) avec

$$
\boxed{B = \kappa Y,\qquad \kappa = \frac{\pi r^4}{4}.}
$$

### Question 58

La Figure 1 donne un diamètre de $2{,}0$ nm, soit $r = 1{,}0$ nm $= 10^{-9}$ m :

$$
\kappa = \frac{\pi r^4}{4} = \frac{\pi\times10^{-36}}{4} \approx \boxed{0{,}78\times10^{-36}\ \text{S.I.}}
$$

(en accord avec l'énoncé ; prendre le **rayon**, pas le diamètre).

### Question 59

La rigidité de flexion $B = \dfrac{\pi r^4}{4}Y$ varie comme la **puissance quatrième** du rayon : si le diamètre (donc $r$) double, $B$ est multiplié par $2^4 = \boxed{16}$ — la tige devient 16 fois plus rigide.

### Question 60

Par unité de longueur : $e_{\text{flexion}} = \dfrac{E_{\text{flexion}}}{L} = \dfrac{B}{2R^2}$. Avec $\theta = L/R$ (donc $1/R = \theta/L$) :

$$
\boxed{e_{\text{flexion}} = \frac{B}{2R^2} = \frac B2\,\frac{\theta^2}{L^2}.}
$$

### C.3.2. Fluctuations thermiques

### Question 61

L'énergie de courbure totale s'écrit $E_{\text{flexion}} = \dfrac12\dfrac{B}{R^2}L = \dfrac{B}{2L}\theta^2$ : c'est une énergie **quadratique** en $\theta$, un degré de liberté « harmonique ». Le théorème d'**équipartition** lui attribue $\tfrac12 k_BT$ :

$$
\frac{B}{2L}\langle\theta^2\rangle = \frac12 k_BT\ \Rightarrow\ \boxed{\langle\theta^2\rangle = \frac{k_BT\,L}{B}.}
$$

Les fluctuations atteignent $\langle\theta^2\rangle = 1\ \text{rad}^2$ pour $L = L_P$ tel que $k_BT L_P/B = 1$, soit la **longueur de persistance**

$$
\boxed{L_P = \frac{B}{k_BT}.}
$$

**C.4. Retour sur le « modèle du ver » et comparaison avec le modèle articulé**

### Question 62

Schéma attendu : $\langle\vec t(s)\cdot\vec t(s')\rangle = e^{-|s-s'|/L_P}$ en fonction de $|s-s'|$, décroissance exponentielle depuis 1 en 0, atteignant $1/e$ en $|s-s'| = L_P$. La longueur de persistance $L_P$ est la distance curviligne sur laquelle la tangente « perd la mémoire » de son orientation.

### Question 63

Le vecteur tangent est la dérivée de la position par rapport à l'abscisse curviligne : $\vec t(u) = \dfrac{d\vec r(u)}{du}$. En intégrant de $s$ à $s+L$ :

$$
\boxed{\vec R(L) = \vec r(s+L) - \vec r(s) = \int_s^{s+L}\vec t(u)\,du.}
$$

### Question 64

Avec $a = 1/L_P$ et la symétrie $s \leftrightarrow s'$ :

$$
\langle R^2(L)\rangle = \int_0^L\!\!\int_0^L e^{-a|s-s'|}\,ds\,ds' = 2\int_0^L ds\int_0^s ds'\,e^{-a(s-s')}.
$$

L'intégrale interne vaut $\tfrac1a(1 - e^{-as})$, d'où

$$
\langle R^2(L)\rangle = \frac2a\int_0^L(1-e^{-as})ds = \frac{2L}{a} - \frac{2}{a^2}\big(1-e^{-aL}\big),
$$

soit, avec $a = 1/L_P$ :

$$
\boxed{\langle R^2(L)\rangle = 2LL_P\Big[1 - \frac{L_P}{L}\big(1 - e^{-L/L_P}\big)\Big].}
$$

### Question 65

- **$L \ll L_P$** (tige rigide) : avec $1 - e^{-L/L_P} \approx \tfrac{L}{L_P} - \tfrac{L^2}{2L_P^2} + \tfrac{L^3}{6L_P^3}$, le crochet vaut $\tfrac{L}{2L_P} - \tfrac{L^2}{6L_P^2}$, d'où $\langle R^2\rangle \approx L^2(1 - \tfrac{L}{3L_P}) \approx L^2$ : la corde se comporte comme une **tige rigide** ($\sqrt{\langle R^2\rangle} \approx L$).
- **$L \gg L_P$** (pelote) : $e^{-L/L_P} \to 0$ et $L_P/L \to 0$, donc

$$
\boxed{\langle R^2\rangle \approx 2LL_P.}
$$

La corde forme une **pelote statistique**, avec $\langle R^2\rangle \propto L$ (comportement de marche aléatoire).

### Question 66

- **Détermination de $\ell$** : à grand $L$, le modèle du ver donne $\langle R^2\rangle = 2LL_P$, et la chaîne librement jointe (Q36) donne $\langle z^2\rangle = \ell L$. L'équivalence impose

$$
\ell L = 2LL_P\ \Rightarrow\ \boxed{\ell = 2L_P.}
$$

- **Interprétation** : le segment rigide du modèle articulé (longueur de Kuhn) vaut **deux longueurs de persistance** ; au-delà de $2L_P$, la corde « oublie » son orientation et se comporte comme un maillon indépendant. Les deux modèles sont équivalents pour $L \gg L_P$.
- **Application numérique** : avec $\ell \simeq 100$ nm, $L_P = \ell/2 = 50$ nm. Alors

$$
B = L_P\,k_BT = 5\times10^{-8}\times4{,}1\times10^{-21} \approx \boxed{2{,}1\times10^{-28}\ \text{J}\cdot\text{m}},
$$

$$
Y = \frac{B}{\kappa} = \frac{2{,}1\times10^{-28}}{0{,}78\times10^{-36}} \approx \boxed{2{,}7\times10^{8}\ \text{Pa} \approx 0{,}3\ \text{GPa}.}
$$

Cette valeur (~0,1–1 GPa) situe la rigidité de l'ADN **au niveau des plastiques** (Tableau 1 : plastiques 0,2–5 GPa), très en dessous des solides durs (métaux, diamant).
