# CAPES Physique — Épreuve disciplinaire (bac+5) 2026 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

**Nature de l'épreuve.** Épreuve écrite disciplinaire du concours externe, troisième concours et CAFEP (bac+5), section physique-chimie, session 2026 : 5 heures, deux parties d'égale importance rendues sur deux copies séparées. Cette épreuve est la **Partie A : composition de physique**, « La physique au service des œuvres d'art » : l'accélérateur AGLAE du Louvre produit des faisceaux de protons et de particules α pour analyser les œuvres d'art (méthodes RBS et PIXE). La partie I étudie le dispositif expérimental (tube accélérateur électrostatique, guidage magnétique du faisceau, détection des rayons X, détection de l'ionoluminescence par fibre optique) ; la partie II étudie les deux méthodes d'analyse par faisceau d'ions (RBS et expérience de Rutherford, spectres RBS, PIXE et loi de Moseley). 44 questions (Q1–Q44). Calculatrice autorisée (circulaire du 17 juin 2021) ; aucun ouvrage ni matériel électronique.

**Statistiques (rapport 2026).** Moyenne CAPES 7,94/20 (écart-type 3,18 ; note min 1,12, max 19,48) ; barre d'admissibilité CAPES 6,87/20. Épreuve sélective, coefficient 2.

**Consignes transversales du rapport 2026.** « en inscrivant clairement le numéro de chaque question traitée, et en mettant en valeur les résultats obtenus (soulignement ou encadrement) » ; « qu'ils établissent d'abord une expression littérale avant de passer à l'application numérique » ; vérification de « l'homogénéité du résultat » ; « l'invalidité de tout résultat numérique sans unité » ; « le signe est une propriété exclusive des grandeurs scalaires ou des composantes d'un vecteur » ; « lorsque le résultat final est indiqué dans l'énoncé […] Ce type de démarche est lourdement sanctionné » (démonstration rigoureuse exigée pour Q6, Q10, Q24…).

**Gestion du temps.** Sur 5 heures pour la partie A : traiter les questions dans l'ordre de l'énoncé (les sous-parties sont indépendantes mais progressives), garder du temps pour les applications numériques (conversions keV→J, unités SI) et la relecture (homogénéité, unités, chiffres significatifs). Les questions les moins traitées selon le jury : Q21, Q28–Q31, Q37, Q40, Q43 — ce sont des points à grappiller.

## I. Étude du dispositif expérimental

### Q1.

> [!INDICATION]
> L'anion H⁻ est un atome d'hydrogène ayant capté un électron supplémentaire : compter protons, neutrons, électrons.

> [!INDICATION]
> Somme des masses avec les données (défaut de masse négligé) ; combien de chiffres significatifs ?

#### Solution

$$
m_{\text{H}^-}=m_p+2\,m_e=1{,}673\times10^{-27}+2\times9{,}110\times10^{-31}=1{,}6748\times10^{-27}\ \text{kg}
$$

$$
\boxed{m_{\text{H}^-}\approx 1{,}67\times10^{-27}\ \text{kg}}\quad(3\ \text{CS})
$$

> [!JURY]
> Rapport 2026 : « De nombreux candidats confondent chiffres significatifs et décimales. »

### Q2.

> [!INDICATION]
> L'énergie cinétique d'entrée (30 keV) fixe la vitesse : $E_c=\frac12 mv^2$.

> [!INDICATION]
> Convertir les keV en joules ; comparer les deux vitesses par un rapport.

#### Solution

$$
v_{\text{H}^-_{\text{entrée}}}=\sqrt{\frac{2E_{c,\text{entrée}}}{m_{\text{H}^-}}}=\sqrt{\frac{2\times4{,}81\times10^{-15}}{1{,}6748\times10^{-27}}}\approx \boxed{2{,}4\times10^{6}\ \text{m·s}^{-1}}=2{,}4\times10^{3}\ \text{km·s}^{-1}.
$$

Comparaison à $v_{\text{H}^+_{\text{sortie}}}=3{,}0\times10^{4}\ \text{km·s}^{-1}$ :

$$
\frac{v_{\text{H}^+_{\text{sortie}}}}{v_{\text{H}^-_{\text{entrée}}}}=\frac{3{,}0\times10^{4}}{2{,}4\times10^{3}}\approx 13.
$$

Le proton sort environ **13 fois plus vite** qu'il n'entre.

> [!JURY]
> Rapport 2026 : lorsqu'un énoncé demande de comparer deux grandeurs, « le jury attend une comparaison quantitative, idéalement formalisée par le calcul d'un rapport entre les deux grandeurs ».

### Q3.

> [!INDICATION]
> Force électrique $\vec F = q\vec E$ avec $q=-e$ (anion) ; le champ entre armatures uniformes vaut $-\frac{V_E}{D}\vec{u_x}$.

> [!INDICATION]
> L'énoncé demande un vecteur, pas seulement une norme.

#### Solution

$$
\vec{F_{\text{él}}}=q\vec E=(-e)\left(-\frac{V_E}{D}\vec{u_x}\right)=\boxed{\frac{e\,V_E}{D}\,\vec{u_x}}.
$$

### Q4.

> [!INDICATION]
> Bilan complet des forces (poids négligeable devant la force électrique — le quantifier) puis PFD.

> [!INDICATION]
> Trajectoire rectiligne car $\vec v_0$ colinéaire à $\vec a$ constant ; mouvement accéléré si $\vec a\cdot\vec v>0$.

#### Solution

PFD dans le référentiel du laboratoire galiléen :

$$
m\,\vec a=\vec{F_{\text{él}}}\ \Rightarrow\ \vec a=\frac{e\,V_E}{m\,D}\,\vec{u_x}=\text{cte}.
$$

La vitesse initiale $\vec v(0)=v_{\text{entrée}}\vec{u_x}$ est **colinéaire** à $\vec a$ : la trajectoire est donc **rectiligne** selon $(Ox)$ (un vecteur accélération constant ne donne une trajectoire rectiligne que si $\vec v_0$ est nul ou colinéaire à $\vec a$ — ce qui est le cas ici).
Pour que le **mouvement soit accéléré**, il faut $\vec a\cdot\vec v>0$, soit $a_x>0$ : avec $\vec v$ selon $+\vec{u_x}$, cela impose $\dfrac{eV_E}{mD}>0$, donc **$V_E>0$**.

### Q5.

> [!INDICATION]
> Théorème de l'énergie cinétique entre l'entrée et l'électrode centrale ; justifier que la force est constante (champ uniforme, mouvement rectiligne).

> [!INDICATION]
> Préciser le système et les instants.

#### Solution

$$
\Delta E_c=W(\vec{F_{\text{él}}})=\vec{F_{\text{él}}}\cdot(D\,\vec{u_x})=\frac{eV_E}{D}\times D=\boxed{e\,V_E}.
$$

(Le poids, négligé, ne travaille pas non plus car perpendiculaire au déplacement.)

### Q6.

> [!INDICATION]
> Résultat fourni : démontrer rigoureusement. Deux accélérations successives par la même électrode (anion puis proton) : cumuler les travaux.

> [!INDICATION]
> Le proton a pour charge $+e$ et passe du potentiel $V_E$ à 0.

#### Solution

$$
W_2=q\,(V_{\text{départ}}-V_{\text{arrivée}})=(+e)(V_E-0)=e\,V_E.
$$

TEC sur cette portion : $\Delta E_c^{(2)}=e V_E$. D'où, en sortie :

$$
E_{c,\text{sortie}}=\underbrace{(E_{c,\text{entrée}}+eV_E)}_{\text{à l'électrode}}+\underbrace{eV_E}_{W_2}=\boxed{E_{c,\text{entrée}}+2\,e\,V_E}.
$$

> [!JURY]
> Rapport 2026 : la relation est fournie « dans le but de rassurer les candidats » ; « Le jury attend en contrepartie une démonstration très rigoureuse et claire, et toute réponse approximative ou malhonnête est décelée et pénalisée. »

### Q7.

> [!INDICATION]
> $E_{c,\text{sortie}}=\frac12 m_p v_{\text{sortie}}^2$ avec $v_{\text{sortie}}$ donné ; négliger $E_{c,\text{entrée}}$ devant.

> [!INDICATION]
> La valeur de la figure 2 est écrite avec un chiffre significatif : écrire le résultat avec un seul CS.

#### Solution

$$
E_{c,\text{sortie}}=\tfrac12\times1{,}673\times10^{-27}\times(3{,}0\times10^{7})^2=7{,}53\times10^{-13}\ \text{J}.
$$

Comme $E_{c,\text{entrée}}=4{,}81\times10^{-15}\ \text{J}\ll E_{c,\text{sortie}}$ :

$$
V_E=\frac{E_{c,\text{sortie}}-E_{c,\text{entrée}}}{2e}\approx\frac{7{,}53\times10^{-13}}{3{,}204\times10^{-19}}\approx 2{,}3\times10^{6}\ \text{V}.
$$

$$
\boxed{V_E\approx 2\ \text{MV}}\quad(1\ \text{CS}).
$$

Cohérent avec l'indication constructeur « 2MV electrostatic accelerator ».

> [!JURY]
> Rapport 2026 : « La valeur sur la figure 2 étant écrite avec un chiffre significatif, il convient d'écrire le résultat du calcul avec un seul chiffre significatif pour comparer. »

**B. Guidage du faisceau jusqu'à l'objet étudié**

### Q8.

> [!INDICATION]
> Force de Lorentz magnétique $\vec F = q\vec v\wedge\vec B$ : produit vectoriel, pas scalaire.

#### Solution

$$
\boxed{\vec{F_{Lm}}=e\,\vec v\wedge\vec B.}
$$

> [!PIEGE]
> Confusion fréquente entre produit scalaire et produit vectoriel (rapport 2026) : la force de Lorentz magnétique est un produit vectoriel.

### Q9.

> [!INDICATION]
> Puissance $\mathcal P = \vec F\cdot\vec v$ ; le produit mixte $(\vec v\wedge\vec B)\cdot\vec v$ est nul.

#### Solution

$$
\boxed{\mathcal P=0.}
$$

La force magnétique est à tout instant orthogonale à la vitesse.

### Q10.

> [!INDICATION]
> Théorème de la puissance cinétique : $\frac{\mathrm dE_c}{\mathrm dt}=\mathcal P=0$, donc $v=\|\vec v\|$ constante.

> [!INDICATION]
> Résultat fourni : démonstration rigoureuse attendue.

#### Solution

$$
\frac{\mathrm d E_c}{\mathrm d t}=\mathcal P(\vec{F_{Lm}})=0\ \Rightarrow\ E_c=\tfrac12 m v^2=\text{cte}\ \Rightarrow\ \boxed{v=\|\vec v\|=\text{cte}.}
$$

### Q11.

> [!INDICATION]
> Lire le rayon $R=O'M$ sur la figure 4 avec son échelle (1 m par division) — pas le diamètre.

#### Solution

$$
\boxed{R\approx 1\ \text{m}.}
$$

[Figure : lecture sur figure 4 ; on reporte quelques points de l'arc et on mesure $R=O'M_1\approx O'M_2\approx 1$ m.]

### Q12.

> [!INDICATION]
> Coordonnées polaires : $\vec{O'M}=R\vec{u_r}$, $\vec v=R\dot\theta\vec{u_\theta}$, $\vec a=-R\dot\theta^2\vec{u_r}+R\ddot\theta\vec{u_\theta}$.

> [!INDICATION]
> $v$ et $R$ constants donnent $\dot\theta$ constant ; une position ne s'exprime pas par un angle.

#### Solution

$$
\vec{O'M}=R\,\vec{u_r},\qquad \vec v(M)=\frac{\mathrm d\vec{O'M}}{\mathrm dt}=R\,\dot\theta\,\vec{u_\theta},
$$

$$
\vec a(M)=\frac{\mathrm d\vec v}{\mathrm dt}=-R\dot\theta^2\,\vec{u_r}+R\ddot\theta\,\vec{u_\theta}.
$$

Comme $v=R|\dot\theta|$ est constant (Q10) et $R$ constant, $\dot\theta$ est constant, donc $\ddot\theta=0$ :

$$
\boxed{\vec{O'M}=R\,\vec{u_r},\quad \vec v=R\dot\theta\,\vec{u_\theta}=v\,\vec{u_\theta},\quad \vec a=-R\dot\theta^2\,\vec{u_r}=-\frac{v^2}{R}\,\vec{u_r}.}
$$

Sur la figure 5, le proton va de $M_1$ (bas) vers $M_2$ (haut) dans le sens où $\theta$ croît : **$\dot\theta>0$**.

### Q13.

> [!INDICATION]
> PFD en base polaire : la force de Lorentz doit être centripète, ce qui fixe le sens de $\vec B$.

> [!INDICATION]
> Norme $B = m_p v/(eR)$ ; application numérique.

#### Solution

$$
m\vec a=e\,\vec v\wedge\vec B\ \Rightarrow\ -m\frac{v^2}{R}\vec{u_r}=e(v\,\vec{u_\theta})\wedge(B_z\vec{u_z})=e\,v\,B_z\,\vec{u_r}.
$$

Par identification : $e v B_z=-m\dfrac{v^2}{R}$, soit $B_z=-\dfrac{m v}{eR}<0$. Donc $\vec B$ est dirigé selon $-\vec{u_z}$ (perpendiculaire au plan, **entrant dans le plan de la figure**), de norme :

$$
B=\frac{m_p v}{eR}=\frac{1{,}673\times10^{-27}\times3{,}0\times10^{7}}{1{,}602\times10^{-19}\times1}\approx \boxed{0{,}3\ \text{T}.}
$$

> [!PIEGE]
> Ne jamais écrire qu'un vecteur est « > 0 » : le signe est une propriété exclusive des grandeurs scalaires ou des composantes d'un vecteur (rapport 2026).

**C. Système de détection des rayons X**

### Q14.

> [!INDICATION]
> $E=h\nu=hc/\lambda$ croît avec la fréquence : classer par énergie croissante (IR < visible < UV < X < $\gamma$).

#### Solution

$$
\boxed{\text{proche IR}<\text{visible}<\text{proche UV}<\text{rayons X}<\text{rayons }\gamma.}
$$

### Q15.

> [!INDICATION]
> Associer chaque diagramme de bandes (conducteur, semi-conducteur, isolant) à la nature du silicium.

#### Solution

- **Diagramme 1** (bande partiellement remplie, pas de gap) → **conducteur** ;
- **Diagramme 2** (bande de valence pleine, petit $E_{\text{gap}}$) → **semi-conducteur** ;
- **Diagramme 3** (bandes séparées par un grand $E_{\text{gap}}$) → **isolant**.

Le silicium, semi-conducteur, correspond au diagramme 2 : le gap modéré permet, pour une onde d'énergie suffisante, de faire passer des électrons de la bande de valence vers la bande de conduction, d'où un courant.

### Q16.

> [!INDICATION]
> Le courant d'obscurité vient de l'agitation thermique qui peuple la bande de conduction ; abaisser $T$ réduit ce bruit.

#### Solution



Même en l'absence de rayonnement à détecter, l'agitation thermique peut exciter des électrons de la bande de valence vers la bande de conduction du silicium. Les paires électron-trou ainsi créées produisent un courant parasite, ou courant d'obscurité, et des fluctuations qui se superposent au signal utile.

**Abaisser la température réduit ces excitations thermiques et le bruit associé.** Le signal dû aux paires électron-trou créées par les rayons X se distingue alors mieux du fond, ce qui améliore la mesure de leur énergie.

### Q17.

> [!INDICATION]
> Sur le diagramme $(P,T)$ du diazote : extrémité de la courbe de vaporisation et point triple ; domaines solide/liquide/gaz.

#### Solution

- **point n°1** = **point critique** (extrémité de la courbe de vaporisation) ;
- **point n°2** = **point triple**.
Les domaines : **B** (basse $T$, haute $P$) = **solide** ; **A** (domaine central supérieur) = **liquide** ; **C** (haute $T$) = **gaz**.

### Q18.

> [!INDICATION]
> Sur le diagramme de Clapeyron $(P,v)$ : hors dôme = liquide ou vapeur, sous le dôme = mélange diphasé ; pas de solide.

#### Solution

- **D** (petit volume massique, hors dôme à gauche) → **liquide** ;
- **E** (sous le dôme de saturation) → **mélange liquide + vapeur** (équilibre diphasé) ;
- **F** (grand volume massique, hors dôme à droite) → **vapeur (gaz)**.

### Q19.

> [!INDICATION]
> $PV=nRT$ : $n$ est une quantité de matière (mol), unités SI : Pa et m³.

#### Solution

$$
\boxed{PV=nRT}
$$

$P$ pression (**Pa**), $V$ volume (**m³**), $n$ **quantité de matière** (mol), $R=8{,}314\ \text{J·K}^{-1}\text{·mol}^{-1}$, $T$ température thermodynamique (**K**).

### Q20.

> [!INDICATION]
> Volume massique $v=V/m=RT/(MP)$ avec $M(\mathrm{N_2})=28\times10^{-3}$ kg/mol (diazote, pas azote) ; comparer à la figure 10 pour valider le modèle.

#### Solution

$$
v=\frac{V}{m}=\frac{nRT}{nM\,P}\cdot\frac{1}{1}=\frac{RT}{M P}=\frac{8{,}314\times273}{28\times10^{-3}\times10^{5}}\approx \boxed{0{,}81\ \text{m}^3\text{·kg}^{-1}.}
$$

Sur la figure 10, l'isotherme $0\,°$C à $P=1\ \text{bar}$ donne $v\approx 0{,}8\ \text{m}^3\text{·kg}^{-1}$ : l'accord valide le **modèle du gaz parfait** dans ces conditions (faible pression, loin de la saturation).

> [!PIEGE]
> Ne pas confondre volume massique $v$ et masse volumique $\rho$, et dire « diazote » (N₂), pas « azote » (rapport 2026).

### Q21.

> [!INDICATION]
> Volume massique global $v=V/m$, puis théorème des moments avec $v_l$ et $v_v$ lus sur la courbe de saturation à 1 bar.

> [!INDICATION]
> Titre en vapeur $x_v=(v-v_l)/(v_v-v_l)$, puis masses.

#### Solution

Lecture (saturation, $P\approx1\ \text{bar}$) : $v_l\approx 1{,}2\times10^{-3}\ \text{m}^3\text{·kg}^{-1}$ et $v_v\approx 0{,}21\ \text{m}^3\text{·kg}^{-1}$. Titre en vapeur :

$$
x_v=\frac{v-v_l}{v_v-v_l}=\frac{8{,}0\times10^{-3}-1{,}2\times10^{-3}}{0{,}21-1{,}2\times10^{-3}}\approx 0{,}033.
$$

$$
m_v=x_v\,m\approx 0{,}033\times7{,}5\approx \boxed{0{,}24\ \text{kg}},\qquad m_l=m-m_v\approx \boxed{7{,}3\ \text{kg}.}
$$

Le diazote est quasi entièrement liquide : cohérent avec un vase Dewar.

**D. Système de détection de l'ionoluminescence**

### Q22.

> [!INDICATION]
> Guidage par réflexion totale interne ; démontrer la condition $n_c>n_g$ via Snell-Descartes (la réfraction n'existe plus au-delà de l'angle limite).

#### Solution

$$
\boxed{n_c>n_g.}
$$

En effet, seule alors $\sin i_2=\dfrac{n_c}{n_g}\sin i$ peut dépasser 1, interdisant la réfraction.

### Q23.

> [!INDICATION]
> Schéma : angles repérés par rapport à la normale au dioptre (air/cœur puis cœur/gaine).

#### Solution

[Figure : Rayon incident arrivant en $O$ sous l'angle $\theta_0$ (par rapport à l'axe $Oz$). À l'interface air/cœur, réfraction : angle $r$ mesuré par rapport à la **normale** (axe perpendiculaire à l'entrée). Le rayon réfracté se propage dans le cœur et atteint l'interface cœur/gaine sous l'angle d'incidence $i$ (mesuré par rapport à la normale radiale, perpendiculaire à l'axe) ; réflexion totale, puis au moins deux rebonds en zig-zag sur les deux faces cœur/gaine.]

### Q24.

> [!INDICATION]
> Snell à l'entrée ($n_0\sin\theta_0=n_c\sin r$) + réflexion totale ($\sin i \ge n_g/n_c$) avec $i=90°-r$ (angles complémentaires).

> [!INDICATION]
> Cas limite : angle de réfraction dans la gaine = 90°.

#### Solution

Dans le cœur, la normale à l'interface cœur/gaine est perpendiculaire à l'axe ; le rayon faisant l'angle $r$ avec l'axe, son angle d'incidence sur cette interface est $i=90°-r$ (**angles complémentaires**). Le guidage exige la réflexion totale : $i\ge i_{\ell}$ avec $\sin i_\ell=\dfrac{n_g}{n_c}$, soit $\sin i\ge\dfrac{n_g}{n_c}$. Or $\sin i=\sin(90°-r)=\cos r$, donc $\cos r\ge\dfrac{n_g}{n_c}$.
Le cas limite ($\cos r=n_g/n_c$) donne $\sin r=\sqrt{1-(n_g/n_c)^2}$. En reportant dans Snell :

$$
\sin\theta_{0\,\text{max}}=\frac{n_c}{n_0}\sin r=\boxed{\frac{n_c}{n_0}\sqrt{1-\left(\frac{n_g}{n_c}\right)^2}.}
$$

### Q25.

> [!INDICATION]
> Appliquer la formule de Q24 avec $n_c=1{,}460$, $n_g=1{,}455$, $n_0=1{,}00$ ; unité d'angle de la calculatrice (degré/radian).

#### Solution

$$
\left(\frac{n_g}{n_c}\right)^2=\left(\frac{1{,}455}{1{,}460}\right)^2=0{,}9932,\quad \sqrt{1-0{,}9932}=0{,}0827.
$$

$$
\sin\theta_{0\,\text{max}}=1{,}460\times0{,}0827=0{,}121\ \Rightarrow\ \boxed{\theta_{0\,\text{max}}\approx 6{,}9°.}
$$

### Q26.

> [!INDICATION]
> $\vec E=E_0\cos(\omega t-\vec k\cdot\vec r)\vec{u_y}$ : polarisation selon $\vec{u_y}$, propagation selon $\vec{u_\theta}$ (vecteur unitaire).

#### Solution

- Direction de **polarisation** : $\vec{u_y}$ (direction de $\vec E$).
- Direction de **propagation** : $\vec{u_\theta}$ (direction de $\vec k$).
- $\omega$ : **pulsation** (rad·s⁻¹) ; $\vec k$ : **vecteur d'onde** (rad·m⁻¹).

### Q27.

> [!INDICATION]
> Phénomène : interférences (pas diffraction) ; conditions : cohérence (déphasage constant) et même direction de polarisation.

#### Solution

- **cohérentes** : déphasage constant au cours de la propagation (ici de même pulsation : synchrones) ;
- de **même direction de polarisation** (ici toutes deux selon $\vec{u_y}$).

### Q28.

> [!INDICATION]
> Intensité $I(x)=2I_0(1+\cos\Delta\varphi)$ avec $\Delta\varphi$ ne dépendant que de $x$ : franges rectilignes parallèles à $(Oy)$.

#### Solution

$$
I(x)=2I_0\big(1+\cos\Delta\varphi\big),\qquad \Delta\varphi=\frac{4\pi}{\lambda_0}n_c\,x\,\sin\alpha.
$$

Le déphasage **ne dépend que de $x$** (ni de $y$ ni de $z$). Donc $I$ ne dépend que de $x$ : à $x$ fixé, l'intensité est uniforme selon $y$. Les lignes d'égale intensité (franges) sont donc **rectilignes, parallèles à $(Oy)$**.

### Q29.

> [!INDICATION]
> Définir l'interfrange $i$ (distance entre deux franges brillantes consécutives, $\Delta\varphi$ variant de $2\pi$), puis $i=\lambda_0/(2n_c\sin\alpha)$.

#### Solution

$$
\frac{4\pi}{\lambda_0}n_c\,i\,\sin\alpha=2\pi\ \Rightarrow\ \boxed{i=\frac{\lambda_0}{2\,n_c\,\sin\alpha}.}
$$

### Q30.

> [!INDICATION]
> Intensité nulle sur les deux miroirs distants de $2a$ : $2a = m\,i$ avec $m$ entier ; égaler à l'interfrange de Q29.

#### Solution

$$
2a=m\,i\ \Rightarrow\ i=\frac{2a}{m}.
$$

En égalant à $i=\dfrac{\lambda_0}{2n_c\sin\alpha}$ :

$$
\frac{\lambda_0}{2n_c\sin\alpha}=\frac{2a}{m}\ \Rightarrow\ \boxed{\sin\alpha=\frac{m\,\lambda_0}{4\,a\,n_c}},\quad m\in\mathbb N^*.
$$

### Q31.

> [!INDICATION]
> Un mode $m$ est guidé si $\sin\alpha_m \le \sin\alpha_{\max}$ (Q24) ; AN avec $\lambda_0=1310$ nm, $a=4{,}5\ \mu$m, $n_c=1{,}460$ ; conclure sur le caractère monomode.

#### Solution

Avec $\lambda_0=1{,}31\times10^{-6}\ \text{m}$, $a=4{,}5\times10^{-6}\ \text{m}$, $n_c=1{,}460$ :

$$
\sin\alpha_m=\frac{m\,\lambda_0}{4an_c}=m\times\frac{1{,}31\times10^{-6}}{4\times4{,}5\times10^{-6}\times1{,}460}=m\times0{,}0499.
$$

- $m=1$ : $\sin\alpha_1=0{,}050<0{,}083$ → mode **guidé** ;
- $m=2$ : $\sin\alpha_2=0{,}100>0{,}083$ → **non guidé**.
Seul le mode $m=1$ se propage : la fibre SMF28 est bien **monomode** à $\lambda_0=1310\ \text{nm}$, assurant un transport optimal du signal.

## II. Étude de deux méthodes d'analyse par faisceau d'ions

### Q32.

> [!INDICATION]
> Désintégration α du radium 226 : conservation de $Z$ et $A$ ; le fils est le radon $^{222}_{86}$Rn (symbole Rn, pas Ra).

#### Solution

$$
\boxed{^{226}_{\ 88}\text{Ra}\ \longrightarrow\ ^{222}_{\ 86}\text{Rn}+\ ^{4}_{2}\text{He}.}
$$

Le noyau fils est le **radon** Rn ($Z=86$).

> [!PIEGE]
> Symbole du radon : Rn (et non Ra) — erreur relevée par le jury.

### Q33.

> [!INDICATION]
> Loi de Coulomb répulsive entre $+79e$ (or) et $+2e$ (α) : $\vec F = \frac{1}{4\pi\varepsilon_0}\frac{158e^2}{d^2}\vec{u}$ ; origine du vecteur au niveau de la particule α.

#### Solution

$$
\boxed{\vec{F_{\text{Au}/\alpha}}=\frac{1}{4\pi\varepsilon_0}\frac{79e\times2e}{d_{\text{Au},\alpha}^{\,2}}\,\vec{u_{\text{Au},\alpha}}=\frac{79\,e^2}{2\pi\varepsilon_0\,d_{\text{Au},\alpha}^{\,2}}\,\vec{u_{\text{Au},\alpha}}.}
$$

[Figure : particule α à gauche, noyau d'or à droite ; $\vec{F_{\text{Au}/\alpha}}$ d'origine la particule α, dirigée de l'or **vers** la particule (selon $+\vec{u_{\text{Au},\alpha}}$).]

Les deux charges étant de même signe, le coefficient est positif : l'interaction est **répulsive** (force dirigée de l'or vers la particule α).

### Q34.

> [!INDICATION]
> $\vec F=-\frac{\mathrm dE_p}{\mathrm dr}\vec{u_r}$ : intégrer et fixer la constante avec $E_p(\infty)=0$.

#### Solution

$$
\frac{\mathrm dE_{p,\text{él}}}{\mathrm dr}=-\frac{79e^2}{2\pi\varepsilon_0 r^2}\ \Rightarrow\ E_{p,\text{él}}=\frac{79e^2}{2\pi\varepsilon_0\,r}+C.
$$

Condition $E_{p,\text{él}}\to0$ quand $r\to\infty$ : $C=0$, d'où

$$
\boxed{E_{p,\text{él}}=\frac{79\,e^2}{2\pi\varepsilon_0}\cdot\frac1r.}
$$

> [!PIEGE]
> La constante d'intégration doit être posée et justifiée par la référence à l'infini (souvent absente, rapport 2026).

### Q35.

> [!INDICATION]
> $E_{m,\alpha}=E_c+E_{p,\text{él}}$ : sommer les deux expressions.

#### Solution

$$
\boxed{E_{m,\alpha}=E_c+E_{p,\text{él}}=\frac12 m_\alpha v^2+\frac{79\,e^2}{2\pi\varepsilon_0\,r}.}
$$

### Q36.

> [!INDICATION]
> Une seule force, conservative (dérive d'une Ep) : théorème de l'énergie mécanique, $E_{m,\alpha}$ constante.

#### Solution

$$
\boxed{E_{m,\alpha}=E_{c,i}=\text{cte}.}
$$

### Q37.

> [!INDICATION]
> Au point le plus proche ($b=0$), la vitesse s'annule ; conservation de $E_m$ entre l'infini et ce point pour trouver $a_0$ ; comparer à $r_{\text{Au}}$.

#### Solution

$$
E_{c,i}=\frac{79e^2}{2\pi\varepsilon_0\,a_0}\ \Rightarrow\ \boxed{a_0=\frac{79\,e^2}{2\pi\varepsilon_0\,E_{c,i}}.}
$$

AN : $E_{c,i}=5{,}3\ \text{MeV}=8{,}49\times10^{-13}\ \text{J}$ :

$$
a_0=\frac{79\times(1{,}602\times10^{-19})^2}{2\pi\times8{,}854\times10^{-12}\times8{,}49\times10^{-13}}\approx \boxed{4{,}3\times10^{-14}\ \text{m}.}
$$

Comparaison : $a_0\approx 4{,}3\times10^{-14}\ \text{m}$ contre $r_{\text{Au}}=7{,}56\times10^{-15}\ \text{m}$, soit $a_0\approx 5{,}7\,r_{\text{Au}}$. La particule α **ne touche jamais** le noyau : elle est repoussée bien avant, ce qui valide le modèle d'interaction purement coulombienne (pas de contact ni de force nucléaire).

**2. Les spectres RBS**

### Q38.

> [!INDICATION]
> Cible épaisse = marche/plateau (élément en profondeur) ; pic fin = couche mince de surface. Comparer fourreau (plateau d'or = or massif) et statuette (pic d'or = dorure).

#### Solution


Sur la figure 17, le spectre du **fourreau du sabre** présente un front à l'énergie caractéristique de l'or et un signal étendu vers les énergies inférieures, allure d'une **cible épaisse en or** (figure 16). Une simple dorure sur argent ferait aussi apparaître le signal du substrat d'argent sous celui de la couche d'or. Le spectre fourni étaye donc l'identification d'un fourreau en **or massif**, dans l'épaisseur sondée par la méthode.

Le spectre de la **statuette khmère** présente au contraire un signal d'or plus étroit, superposé à un fond provenant d'éléments plus légers : il est compatible avec une **couche d'or superficielle sur un cœur d'un autre matériau**, par exemple un alliage plus léger. Le seul spectre ne suffit pas à préciser sa composition complète.

### Q39.

> [!INDICATION]
> L'énergie rétrodiffusée croît avec la masse de la cible : classer O < Si < K < Fe < Pb par énergie croissante ; pic de Pb (couche mince) sur plateaux du verre.

#### Solution



À énergie incidente et angle de diffusion fixés, le facteur cinématique donné dans l'énoncé augmente avec la masse de l'atome cible. **Les éléments les plus lourds donnent donc les fronts ou pics aux énergies les plus élevées.** Cela explique notamment la succession des fronts de l'oxygène, du silicium, du potassium puis le pic du plomb, beaucoup plus lourd, à droite du spectre.

D'après la figure 16, une couche très mince donne un pic étroit : la faible perte d'énergie des ions à l'aller et au retour explique le **pic du plomb**, attribué sur la figure 18 à une couche d'environ **10 nm**. Pour une cible plus épaisse, les ions rétrodiffusés à différentes profondeurs ne perdent pas la même énergie ; le signal s'étale vers les basses énergies. La matrice du vitrail produit ainsi des **plateaux et des marches**, dont les fronts de haute énergie identifient les éléments présents près de la surface. La couche de silice d'environ **50 nm** indiquée sur la figure contribue également à ces pertes d'énergie.

### Q40.

> [!INDICATION]
> Lire $E_K$ sur la figure 18, puis inverser le facteur cinématique $k=E/E_0$ pour $\theta=150°$, $m=4$ u, $M=39$ u ; trouver $E_0$.

#### Solution

$$
k=\frac{E}{E_0}=\frac{\big[(M^2-m^2\sin^2\theta)^{1/2}+m\cos\theta\big]^2}{(M+m)^2}.
$$

$\sin^2 150°=0{,}25$ : $M^2-m^2\sin^2\theta=1521-4=1517$, $\sqrt{\ }=38{,}9$ ; $m\cos150°=-3{,}46$ ; numérateur $=(38{,}9-3{,}46)^2=1{,}26\times10^{3}$ ; $(M+m)^2=43^2=1849$. Donc $k=0{,}68$.

$$
E_0=\frac{E_K}{k}=\frac{2{,}0}{0{,}68}\approx \boxed{3{,}0\ \text{MeV}.}
$$

Cohérent avec « 3 MeV He beam » de la figure 18.

**B. La méthode PIXE — 1. Principe et 2. Loi de Moseley**

### Q41.

> [!INDICATION]
> Pour $n$ fixé : $\ell\in\{0,\dots,n-1\}$, $m_\ell\in\{-\ell,\dots,+\ell\}$, $m_s=\pm\frac12$.

#### Solution

- **nombre quantique secondaire (azimutal)** $\ell$ : $\ell\in\{0,1,\dots,n-1\}$ ;
- **nombre quantique magnétique** $m_\ell$ : $m_\ell\in\{-\ell,\dots,0,\dots,+\ell\}$ ;
- **nombre quantique de spin** $m_s$ : $m_s=\pm\tfrac12$.

### Q42.

> [!INDICATION]
> Planck-Einstein : $E=h\nu=hc/\lambda$ ; unités (J, Hz, m).

#### Solution

$$
\boxed{E=h\nu=\frac{hc}{\lambda}}
$$

$E$ énergie du photon (**J**), $h=6{,}63\times10^{-34}\ \text{J·s}$ constante de Planck, $\nu$ fréquence (**Hz**), $c$ célérité (m·s⁻¹), $\lambda$ longueur d'onde (**m**).

### Q43.

> [!INDICATION]
> La figure 20 donne $\sqrt\nu$ affine en $Z$ pour la raie Kα ; introduire $E=h\nu$ pour obtenir $E=C_1(Z-\sigma)^2$ ; lire pente et ordonnée à l'origine.

#### Solution

$$
E=\underbrace{h\,a^2}_{C_1}(Z-\sigma)^2=C_1(Z-\sigma)^2.
$$

Exploitation du graphe (droite Kα, par exemple de $(Z=13;\sqrt\nu\approx6{,}0\times10^{8})$ à $(Z=47;\sqrt\nu\approx22\times10^{8})$) :

$$
a=\frac{\Delta\sqrt\nu}{\Delta Z}=\frac{(22-6)\times10^{8}}{47-13}\approx 4{,}9\times10^{7}\ \text{Hz}^{1/2}.
$$

$$
C_1=h\,a^2=6{,}63\times10^{-34}\times(4{,}9\times10^{7})^2\approx \boxed{1{,}6\times10^{-18}\ \text{J}.}
$$

L'ordonnée à l'origine (extrapolation à $\sqrt\nu=0$) donne $\boxed{\sigma\approx 1{,}0}$ (sans dimension), $C_1$ en **joules**.

### Q44.

> [!INDICATION]
> Inverser la loi de Moseley $Z=\sigma+\sqrt{E/C_1}$ ; lire $E_{K\alpha}\approx 8{,}6$ keV sur la figure 21 ; conclure (zinc, pigment moderne = faux).

#### Solution

$$
Z=\sigma+\sqrt{\frac{E_{K\alpha}}{C_1}}=1+\sqrt{\frac{1{,}38\times10^{-15}}{1{,}66\times10^{-18}}}=1+\sqrt{831}=1+28{,}8\approx \boxed{30.}
$$

L'élément est le **zinc** ($Z=30$). La présence de zinc dans le pigment (un pigment moderne, le zinc n'étant pas disponible du temps des « primitifs italiens ») **trahit le faux**.

## Bilan

- **Mécanique (Q1–Q13)** : PFD avec schéma (système, forces, base locale) ; TEC/TPC avec système et instants précisés ; produit vectoriel vs scalaire ; coordonnées polaires ($\vec a=-R\dot\theta^2\vec{u_r}+R\ddot\theta\vec{u_\theta}$) ; force de Lorentz centripète ($B=mv/eR$).
- **Thermodynamique (Q17–Q21)** : diagramme $(P,T)$ (point triple, point critique) vs diagramme de Clapeyron $(P,v)$ ; gaz parfait $PV=nRT$ en unités SI ; théorème des moments pour le titre en vapeur.
- **Ondes et optique (Q14, Q22–Q31)** : spectre électromagnétique classé par énergie ; réflexion totale interne ($n_c>n_g$, ouverture numérique) ; interférences dans un guide d'onde plan (interfrange $i=\lambda_0/(2n_c\sin\alpha)$, quantification $\sin\alpha_m=m\lambda_0/(4an_c)$, fibre monomode SMF28).
- **Physique atomique et nucléaire (Q32–Q44)** : désintégration α ; interaction coulombienne répulsive ($E_{p,\text{él}}=79e^2/(2\pi\varepsilon_0 r)$) ; distance minimale d'approche ($v=0$ au rebroussement) ; spectres RBS (énergie croissante avec la masse cible, pic = couche mince, plateau = massif) ; loi de Moseley $E=C_1(Z-\sigma)^2$ et identification d'un élément par sa raie Kα.
- **Transversal** : expression littérale avant l'AN, homogénéité, unités, chiffres significatifs, résultats encadrés, numérotation claire, vecteurs jamais comparés à zéro — les exigences générales du rapport 2026.
