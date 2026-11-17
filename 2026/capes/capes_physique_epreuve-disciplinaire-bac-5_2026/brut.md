# CAPES Physique — Épreuve disciplinaire (bac+5) 2026 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Session 2026, concours externe, troisième concours et CAFEP, section physique-chimie — **Partie A : composition de physique**, « La physique au service des œuvres d'art » (accélérateur AGLAE du Louvre, méthodes RBS et PIXE). Épreuve écrite disciplinaire : durée 5 heures, deux parties d'égale importance (le candidat rend deux copies séparées) ; calculatrice autorisée (circulaire du 17 juin 2021), tout ouvrage, dictionnaire ou matériel électronique interdit. Cette copie traite la Partie A (44 questions).

## I. Étude du dispositif expérimental
**A. Le tube accélérateur**

### Q1.

$$
m_{\text{H}^-}=m_p+2\,m_e=1{,}673\times10^{-27}+2\times9{,}110\times10^{-31}=1{,}6748\times10^{-27}\ \text{kg}
$$

$$
\boxed{m_{\text{H}^-}\approx 1{,}67\times10^{-27}\ \text{kg}}\quad(3\ \text{CS})
$$

### Q2.

$$
v_{\text{H}^-_{\text{entrée}}}=\sqrt{\frac{2E_{c,\text{entrée}}}{m_{\text{H}^-}}}=\sqrt{\frac{2\times4{,}81\times10^{-15}}{1{,}6748\times10^{-27}}}\approx \boxed{2{,}4\times10^{6}\ \text{m·s}^{-1}}=2{,}4\times10^{3}\ \text{km·s}^{-1}.
$$

Comparaison à $v_{\text{H}^+_{\text{sortie}}}=3{,}0\times10^{4}\ \text{km·s}^{-1}$ :

$$
\frac{v_{\text{H}^+_{\text{sortie}}}}{v_{\text{H}^-_{\text{entrée}}}}=\frac{3{,}0\times10^{4}}{2{,}4\times10^{3}}\approx 13.
$$

Le proton sort environ **13 fois plus vite** qu'il n'entre.

### Q3.

$$
\vec{F_{\text{él}}}=q\vec E=(-e)\left(-\frac{V_E}{D}\vec{u_x}\right)=\boxed{\frac{e\,V_E}{D}\,\vec{u_x}}.
$$

### Q4.

PFD dans le référentiel du laboratoire galiléen :

$$
m\,\vec a=\vec{F_{\text{él}}}\ \Rightarrow\ \vec a=\frac{e\,V_E}{m\,D}\,\vec{u_x}=\text{cte}.
$$

La vitesse initiale $\vec v(0)=v_{\text{entrée}}\vec{u_x}$ est **colinéaire** à $\vec a$ : la trajectoire est donc **rectiligne** selon $(Ox)$ (un vecteur accélération constant ne donne une trajectoire rectiligne que si $\vec v_0$ est nul ou colinéaire à $\vec a$ — ce qui est le cas ici).
Pour que le **mouvement soit accéléré**, il faut $\vec a\cdot\vec v>0$, soit $a_x>0$ : avec $\vec v$ selon $+\vec{u_x}$, cela impose $\dfrac{eV_E}{mD}>0$, donc **$V_E>0$**.

### Q5.

$$
\Delta E_c=W(\vec{F_{\text{él}}})=\vec{F_{\text{él}}}\cdot(D\,\vec{u_x})=\frac{eV_E}{D}\times D=\boxed{e\,V_E}.
$$

(Le poids, négligé, ne travaille pas non plus car perpendiculaire au déplacement.)

### Q6.

$$
W_2=q\,(V_{\text{départ}}-V_{\text{arrivée}})=(+e)(V_E-0)=e\,V_E.
$$

TEC sur cette portion : $\Delta E_c^{(2)}=e V_E$. D'où, en sortie :

$$
E_{c,\text{sortie}}=\underbrace{(E_{c,\text{entrée}}+eV_E)}_{\text{à l'électrode}}+\underbrace{eV_E}_{W_2}=\boxed{E_{c,\text{entrée}}+2\,e\,V_E}.
$$

### Q7.

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

**B. Guidage du faisceau jusqu'à l'objet étudié**

### Q8.

$$
\boxed{\vec{F_{Lm}}=e\,\vec v\wedge\vec B.}
$$

### Q9.

$$
\boxed{\mathcal P=0.}
$$

La force magnétique est à tout instant orthogonale à la vitesse.

### Q10.

$$
\frac{\mathrm d E_c}{\mathrm d t}=\mathcal P(\vec{F_{Lm}})=0\ \Rightarrow\ E_c=\tfrac12 m v^2=\text{cte}\ \Rightarrow\ \boxed{v=\|\vec v\|=\text{cte}.}
$$

### Q11.

$$
\boxed{R\approx 1\ \text{m}.}
$$

[Figure : lecture sur figure 4 ; on reporte quelques points de l'arc et on mesure $R=O'M_1\approx O'M_2\approx 1$ m.]

### Q12.

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

$$
m\vec a=e\,\vec v\wedge\vec B\ \Rightarrow\ -m\frac{v^2}{R}\vec{u_r}=e(v\,\vec{u_\theta})\wedge(B_z\vec{u_z})=e\,v\,B_z\,\vec{u_r}.
$$

Par identification : $e v B_z=-m\dfrac{v^2}{R}$, soit $B_z=-\dfrac{m v}{eR}<0$. Donc $\vec B$ est dirigé selon $-\vec{u_z}$ (perpendiculaire au plan, **entrant dans le plan de la figure**), de norme :

$$
B=\frac{m_p v}{eR}=\frac{1{,}673\times10^{-27}\times3{,}0\times10^{7}}{1{,}602\times10^{-19}\times1}\approx \boxed{0{,}3\ \text{T}.}
$$

**C. Système de détection des rayons X**

### Q14.

$$
\boxed{\text{proche IR}<\text{visible}<\text{proche UV}<\text{rayons X}<\text{rayons }\gamma.}
$$

### Q15.
- **Diagramme 1** (bande partiellement remplie, pas de gap) → **conducteur** ;
- **Diagramme 2** (bande de valence pleine, petit $E_{\text{gap}}$) → **semi-conducteur** ;
- **Diagramme 3** (bandes séparées par un grand $E_{\text{gap}}$) → **isolant**.

Le silicium, semi-conducteur, correspond au diagramme 2 : le gap modéré permet, pour une onde d'énergie suffisante, de faire passer des électrons de la bande de valence vers la bande de conduction, d'où un courant.

### Q16.

Même en l'absence de rayonnement à détecter, l'agitation thermique peut exciter des électrons de la bande de valence vers la bande de conduction du silicium. Les paires électron-trou ainsi créées produisent un courant parasite, ou courant d'obscurité, et des fluctuations qui se superposent au signal utile.

**Abaisser la température réduit ces excitations thermiques et le bruit associé.** Le signal dû aux paires électron-trou créées par les rayons X se distingue alors mieux du fond, ce qui améliore la mesure de leur énergie.

### Q17.
- **point n°1** = **point critique** (extrémité de la courbe de vaporisation) ;
- **point n°2** = **point triple**.
Les domaines : **B** (basse $T$, haute $P$) = **solide** ; **A** (domaine central supérieur) = **liquide** ; **C** (haute $T$) = **gaz**.

### Q18.
- **D** (petit volume massique, hors dôme à gauche) → **liquide** ;
- **E** (sous le dôme de saturation) → **mélange liquide + vapeur** (équilibre diphasé) ;
- **F** (grand volume massique, hors dôme à droite) → **vapeur (gaz)**.

### Q19.

$$
\boxed{PV=nRT}
$$

$P$ pression (**Pa**), $V$ volume (**m³**), $n$ **quantité de matière** (mol), $R=8{,}314\ \text{J·K}^{-1}\text{·mol}^{-1}$, $T$ température thermodynamique (**K**).

### Q20.

$$
v=\frac{V}{m}=\frac{nRT}{nM\,P}\cdot\frac{1}{1}=\frac{RT}{M P}=\frac{8{,}314\times273}{28\times10^{-3}\times10^{5}}\approx \boxed{0{,}81\ \text{m}^3\text{·kg}^{-1}.}
$$

Sur la figure 10, l'isotherme $0\,°$C à $P=1\ \text{bar}$ donne $v\approx 0{,}8\ \text{m}^3\text{·kg}^{-1}$ : l'accord valide le **modèle du gaz parfait** dans ces conditions (faible pression, loin de la saturation).

### Q21.

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

$$
\boxed{n_c>n_g.}
$$

En effet, seule alors $\sin i_2=\dfrac{n_c}{n_g}\sin i$ peut dépasser 1, interdisant la réfraction.

### Q23.

[Figure : Rayon incident arrivant en $O$ sous l'angle $\theta_0$ (par rapport à l'axe $Oz$). À l'interface air/cœur, réfraction : angle $r$ mesuré par rapport à la **normale** (axe perpendiculaire à l'entrée). Le rayon réfracté se propage dans le cœur et atteint l'interface cœur/gaine sous l'angle d'incidence $i$ (mesuré par rapport à la normale radiale, perpendiculaire à l'axe) ; réflexion totale, puis au moins deux rebonds en zig-zag sur les deux faces cœur/gaine.]

### Q24.

Dans le cœur, la normale à l'interface cœur/gaine est perpendiculaire à l'axe ; le rayon faisant l'angle $r$ avec l'axe, son angle d'incidence sur cette interface est $i=90°-r$ (**angles complémentaires**). Le guidage exige la réflexion totale : $i\ge i_{\ell}$ avec $\sin i_\ell=\dfrac{n_g}{n_c}$, soit $\sin i\ge\dfrac{n_g}{n_c}$. Or $\sin i=\sin(90°-r)=\cos r$, donc $\cos r\ge\dfrac{n_g}{n_c}$.
Le cas limite ($\cos r=n_g/n_c$) donne $\sin r=\sqrt{1-(n_g/n_c)^2}$. En reportant dans Snell :

$$
\sin\theta_{0\,\text{max}}=\frac{n_c}{n_0}\sin r=\boxed{\frac{n_c}{n_0}\sqrt{1-\left(\frac{n_g}{n_c}\right)^2}.}
$$

### Q25.

$$
\left(\frac{n_g}{n_c}\right)^2=\left(\frac{1{,}455}{1{,}460}\right)^2=0{,}9932,\quad \sqrt{1-0{,}9932}=0{,}0827.
$$

$$
\sin\theta_{0\,\text{max}}=1{,}460\times0{,}0827=0{,}121\ \Rightarrow\ \boxed{\theta_{0\,\text{max}}\approx 6{,}9°.}
$$

### Q26.
- Direction de **polarisation** : $\vec{u_y}$ (direction de $\vec E$).
- Direction de **propagation** : $\vec{u_\theta}$ (direction de $\vec k$).
- $\omega$ : **pulsation** (rad·s⁻¹) ; $\vec k$ : **vecteur d'onde** (rad·m⁻¹).

### Q27.
- **cohérentes** : déphasage constant au cours de la propagation (ici de même pulsation : synchrones) ;
- de **même direction de polarisation** (ici toutes deux selon $\vec{u_y}$).

### Q28.

$$
I(x)=2I_0\big(1+\cos\Delta\varphi\big),\qquad \Delta\varphi=\frac{4\pi}{\lambda_0}n_c\,x\,\sin\alpha.
$$

Le déphasage **ne dépend que de $x$** (ni de $y$ ni de $z$). Donc $I$ ne dépend que de $x$ : à $x$ fixé, l'intensité est uniforme selon $y$. Les lignes d'égale intensité (franges) sont donc **rectilignes, parallèles à $(Oy)$**.

### Q29.

$$
\frac{4\pi}{\lambda_0}n_c\,i\,\sin\alpha=2\pi\ \Rightarrow\ \boxed{i=\frac{\lambda_0}{2\,n_c\,\sin\alpha}.}
$$

### Q30.

$$
2a=m\,i\ \Rightarrow\ i=\frac{2a}{m}.
$$

En égalant à $i=\dfrac{\lambda_0}{2n_c\sin\alpha}$ :

$$
\frac{\lambda_0}{2n_c\sin\alpha}=\frac{2a}{m}\ \Rightarrow\ \boxed{\sin\alpha=\frac{m\,\lambda_0}{4\,a\,n_c}},\quad m\in\mathbb N^*.
$$

### Q31.

Avec $\lambda_0=1{,}31\times10^{-6}\ \text{m}$, $a=4{,}5\times10^{-6}\ \text{m}$, $n_c=1{,}460$ :

$$
\sin\alpha_m=\frac{m\,\lambda_0}{4an_c}=m\times\frac{1{,}31\times10^{-6}}{4\times4{,}5\times10^{-6}\times1{,}460}=m\times0{,}0499.
$$

- $m=1$ : $\sin\alpha_1=0{,}050<0{,}083$ → mode **guidé** ;
- $m=2$ : $\sin\alpha_2=0{,}100>0{,}083$ → **non guidé**.
Seul le mode $m=1$ se propage : la fibre SMF28 est bien **monomode** à $\lambda_0=1310\ \text{nm}$, assurant un transport optimal du signal.

## II. Étude de deux méthodes d'analyse par faisceau d'ions
**A. La méthode RBS — 1. Expérience de Rutherford**

### Q32.

$$
\boxed{^{226}_{\ 88}\text{Ra}\ \longrightarrow\ ^{222}_{\ 86}\text{Rn}+\ ^{4}_{2}\text{He}.}
$$

Le noyau fils est le **radon** Rn ($Z=86$).

### Q33.

$$
\boxed{\vec{F_{\text{Au}/\alpha}}=\frac{1}{4\pi\varepsilon_0}\frac{79e\times2e}{d_{\text{Au},\alpha}^{\,2}}\,\vec{u_{\text{Au},\alpha}}=\frac{79\,e^2}{2\pi\varepsilon_0\,d_{\text{Au},\alpha}^{\,2}}\,\vec{u_{\text{Au},\alpha}}.}
$$

[Figure : particule α à gauche, noyau d'or à droite ; $\vec{F_{\text{Au}/\alpha}}$ d'origine la particule α, dirigée de l'or **vers** la particule (selon $+\vec{u_{\text{Au},\alpha}}$).]

Les deux charges étant de même signe, le coefficient est positif : l'interaction est **répulsive** (force dirigée de l'or vers la particule α).

### Q34.

$$
\frac{\mathrm dE_{p,\text{él}}}{\mathrm dr}=-\frac{79e^2}{2\pi\varepsilon_0 r^2}\ \Rightarrow\ E_{p,\text{él}}=\frac{79e^2}{2\pi\varepsilon_0\,r}+C.
$$

Condition $E_{p,\text{él}}\to0$ quand $r\to\infty$ : $C=0$, d'où

$$
\boxed{E_{p,\text{él}}=\frac{79\,e^2}{2\pi\varepsilon_0}\cdot\frac1r.}
$$

### Q35.

$$
\boxed{E_{m,\alpha}=E_c+E_{p,\text{él}}=\frac12 m_\alpha v^2+\frac{79\,e^2}{2\pi\varepsilon_0\,r}.}
$$

### Q36.

$$
\boxed{E_{m,\alpha}=E_{c,i}=\text{cte}.}
$$

### Q37.

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

Sur la figure 17, le spectre du **fourreau du sabre** présente un front à l'énergie caractéristique de l'or et un signal étendu vers les énergies inférieures, allure d'une **cible épaisse en or** (figure 16). Une simple dorure sur argent ferait aussi apparaître le signal du substrat d'argent sous celui de la couche d'or. Le spectre fourni étaye donc l'identification d'un fourreau en **or massif**, dans l'épaisseur sondée par la méthode.

Le spectre de la **statuette khmère** présente au contraire un signal d'or plus étroit, superposé à un fond provenant d'éléments plus légers : il est compatible avec une **couche d'or superficielle sur un cœur d'un autre matériau**, par exemple un alliage plus léger. Le seul spectre ne suffit pas à préciser sa composition complète.

### Q39.

À énergie incidente et angle de diffusion fixés, le facteur cinématique donné dans l'énoncé augmente avec la masse de l'atome cible. **Les éléments les plus lourds donnent donc les fronts ou pics aux énergies les plus élevées.** Cela explique notamment la succession des fronts de l'oxygène, du silicium, du potassium puis le pic du plomb, beaucoup plus lourd, à droite du spectre.

D'après la figure 16, une couche très mince donne un pic étroit : la faible perte d'énergie des ions à l'aller et au retour explique le **pic du plomb**, attribué sur la figure 18 à une couche d'environ **10 nm**. Pour une cible plus épaisse, les ions rétrodiffusés à différentes profondeurs ne perdent pas la même énergie ; le signal s'étale vers les basses énergies. La matrice du vitrail produit ainsi des **plateaux et des marches**, dont les fronts de haute énergie identifient les éléments présents près de la surface. La couche de silice d'environ **50 nm** indiquée sur la figure contribue également à ces pertes d'énergie.

### Q40.

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
- **nombre quantique secondaire (azimutal)** $\ell$ : $\ell\in\{0,1,\dots,n-1\}$ ;
- **nombre quantique magnétique** $m_\ell$ : $m_\ell\in\{-\ell,\dots,0,\dots,+\ell\}$ ;
- **nombre quantique de spin** $m_s$ : $m_s=\pm\tfrac12$.

### Q42.

$$
\boxed{E=h\nu=\frac{hc}{\lambda}}
$$

$E$ énergie du photon (**J**), $h=6{,}63\times10^{-34}\ \text{J·s}$ constante de Planck, $\nu$ fréquence (**Hz**), $c$ célérité (m·s⁻¹), $\lambda$ longueur d'onde (**m**).

### Q43.

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

$$
Z=\sigma+\sqrt{\frac{E_{K\alpha}}{C_1}}=1+\sqrt{\frac{1{,}38\times10^{-15}}{1{,}66\times10^{-18}}}=1+\sqrt{831}=1+28{,}8\approx \boxed{30.}
$$

L'élément est le **zinc** ($Z=30$). La présence de zinc dans le pigment (un pigment moderne, le zinc n'étant pas disponible du temps des « primitifs italiens ») **trahit le faux**.
