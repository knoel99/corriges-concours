# Agrégation Chimie — Composition de chimie 2026 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Sujet : « Chimie à la surface de microgouttelettes d'eau atmosphériques » (64 questions, 5 heures).

**Signalements d'énoncé.** La constante des gaz parfaits imprimée dans les données ($R = 8{,}413\ \mathrm{J\cdot K^{-1}\cdot mol^{-1}}$) est une coquille : on utilise la valeur exacte $R = 8{,}314\ \mathrm{J\cdot K^{-1}\cdot mol^{-1}}$. Le produit ionique de l'eau est donné à 20 °C ($pK_e = 14{,}0$) ; les questions se plaçant à 25 °C se traitent avec $pK_e = 14{,}0$.

## A — Effets isotopiques sur les propriétés acide-base de l'eau

### A.1 — pH d'une solution aqueuse

### Question 1 (*)

Pour une solution aqueuse diluée,

$$

\begin{aligned}
\mathrm{pH} & = -\log a(\mathrm{H_3O^+})\\
& \simeq -\log\!\left(\frac{[\mathrm{H_3O^+}]}{c°}\right),\qquad c°\\
& = 1\ \text{mol·L}^{-1},
\end{aligned}

$$

l'approximation valant en solution diluée où le coefficient d'activité $\gamma \approx 1$. $\boxed{\mathrm{pH}=-\log([\mathrm{H_3O^+}]/c°)}$

### Question 2 (*)

Dans l'eau pure, électroneutralité : $[\mathrm{H_3O^+}]=[\mathrm{OH^-}]$. Avec $K_e=[\mathrm{H_3O^+}][\mathrm{OH^-}]/c°^2=10^{-14}$,

$$

\begin{aligned}
[\mathrm{H_3O^+}] & = [\mathrm{OH^-}]\\
& = c°\sqrt{K_e}\\
& = 1{,}0\times10^{-7}\ \text{mol·L}^{-1}.
\end{aligned}

$$

Concentration de l'eau : $[\mathrm{H_2O}]=\dfrac{\rho}{M}=\dfrac{1000}{18}=55{,}5\ \text{mol·L}^{-1}$.
**Hypothèse** retenue : la part d'eau dissociée est négligeable, de sorte que $[\mathrm{H_2O}]\approx$ cte. **Vérification** : $10^{-7}\ll 55{,}5$ (facteur $\sim10^{8}$).

### Question 3

*Contextualisation* : l'acide éthanoïque est le constituant acide du vinaigre ; on cherche à contrôler le « degré » annoncé d'un vinaigre commercial. *Problématisation* : « Comment déterminer, par un titrage, la concentration (donc le degré) en acide éthanoïque d'un vinaigre, et confronter le résultat à l'étiquetage réglementaire ? » Le titrage acido-basique en est la démarche expérimentale de résolution.

### Question 4

De $[\mathrm{H_3O^+}]=c°\,10^{-\mathrm{pH}}$, on tire $\ln([\mathrm{H_3O^+}]/c°)=-\ln(10)\,\mathrm{pH}$, d'où

$$
\frac{u([\mathrm{H_3O^+}])}{[\mathrm{H_3O^+}]}=\ln(10)\;u(\mathrm{pH}).
$$

Une incertitude-type raisonnable sur la lecture d'un pH-mètre est $u(\mathrm{pH})\approx 0{,}05$. Alors

$$

\begin{aligned}
\frac{u([\mathrm{H_3O^+}])}{[\mathrm{H_3O^+}]} & \approx 2{,}30\times 0{,}05\\
& \approx 0{,}12\\
& = 12\%\ (>10\%).
\end{aligned}

$$

**Conclusion** : la détermination de $[\mathrm{H_3O^+}]$ (et donc de la concentration) *via* une courbe d'étalonnage pH–$[\mathrm{H_3O^+}]$ est entachée d'une incertitude relative supérieure à 10 % ; l'échelle logarithmique du pH **amplifie** fortement toute erreur de lecture : la méthode proposée par l'élève est peu précise.

### Question 5 (*)

Schéma attendu : burette contenant la soude (0,10 mol·L⁻¹) au-dessus d'un bécher ; dans le bécher, les 20 mL de $S_0$ + 250 mL d'eau distillée ; cellule conductimétrique (deux électrodes planes parallèles) plongée dans la solution et reliée au **conductimètre** ; **barreau aimanté** + agitateur magnétique. Légendes : burette graduée (NaOH), bécher, solution à titrer, cellule/électrodes, conductimètre, agitation magnétique.

### Question 6 (*)

Le conductimètre mesure la **conductance** $G$ (en siemens), reliée à la **conductivité** $\sigma$ par $G=\sigma/K_{\text{cell}}$ ($K_{\text{cell}}$ : constante de cellule). La conductivité est reliée aux concentrations par la loi de Kohlrausch :

$$
\sigma=\sum_i \lambda_i\,[i],
$$

où $\lambda_i$ est la conductivité ionique molaire de l'ion $i$ (sommation sur tous les ions).

### Question 7 (*)

On repère l'équivalence par l'**intersection de deux droites** $\sigma=f(V)$, c'est-à-dire par une rupture de pente. La position du point équivalent ne dépend pas de la valeur absolue de $\sigma$ (ni de $K_{\text{cell}}$) : **l'étalonnage du conductimètre n'est pas nécessaire** ici.

### Question 8 (*)

Réaction support : $\mathrm{CH_3COOH} + \mathrm{HO^-} \longrightarrow \mathrm{CH_3COO^-} + \mathrm{H_2O}$ (quantitative).
- **Avant l'équivalence** : chaque ajout de NaOH consomme l'acide (peu dissocié, peu conducteur) et introduit $\mathrm{Na^+}$ ($\lambda=5{,}0$) et $\mathrm{CH_3COO^-}$ ($\lambda=4{,}1$). La conductivité **croît faiblement** (pente $\propto 5{,}0+4{,}1=9{,}1$).
- **Après l'équivalence** : on ajoute $\mathrm{Na^+}$ ($5{,}0$) et surtout $\mathrm{OH^-}$ ($\lambda=19{,}8$, très mobile). La conductivité **croît fortement** (pente $\propto 5{,}0+19{,}8=24{,}8$).
On observe donc **deux droites croissantes** de pentes différentes, se coupant à l'équivalence. Le grand volume d'eau ajouté (250 mL) rend la **dilution** quasi constante lors des ajouts, ce qui justifie le caractère **linéaire** des portions. $\mathrm{Na^+}$, spectateur mais présent à chaque ajout, n'est pas négligeable.

Schéma attendu : $\sigma=f(V_{\text{NaOH}})$, deux segments croissants, faible pente puis forte pente, intersection en $V_e=13{,}7$ mL.

### Question 9 (*)

Pour un **acide faible dilué**, le saut de pH à l'équivalence est faible et étalé (effet tampon autour de l'équivalence), ce qui rend la méthode pH-métrique (dérivée) imprécise. La méthode **conductimétrique** exploite une **régression linéaire sur de nombreux points** encadrant l'équivalence, dont l'intersection est bien définie : elle est ici **plus précise et plus robuste**. L'opinion des élèves (« le pH-métrique est plus précis ») est donc **invalidée** dans ce cas (acide faible, solution diluée).

### A.2 — Propriétés comparées de l'eau lourde et de l'eau normale

### Question 10 (*)

Deux **isotopes** d'un élément sont des nucléides de même numéro atomique $Z$ (même nombre de protons, donc même élément) mais de nombres de neutrons différents (donc de nombres de masse $A$ différents). H ($^1$H) et D ($^2$H) en sont un exemple.

### Question 11 (*)

La réactivité chimique est gouvernée par la **structure électronique**. Or deux isotopes ont même $Z$, donc même nombre d'électrons et même configuration électronique : le cortège électronique et les surfaces d'énergie potentielle sont identiques. Les noyaux ne diffèrent que par leur **masse** : seuls les effets dépendant de la masse (vibrations, effets cinétiques isotopiques) se manifestent, et faiblement. La réactivité est donc peu modifiée.

### Question 12

À 20 °C, $\rho(\mathrm{D_2O})=1{,}11>\rho(\mathrm{H_2O})=1{,}00\ \text{kg·L}^{-1}$ : un glaçon de D₂O, plus dense que l'eau légère liquide, **coule** (tandis qu'un glaçon de H₂O flotte). Le système **n'est pas à l'équilibre thermodynamique** : à température ambiante, la glace fond (transformation irréversible), il existe des gradients de température, et le mélange isotopique D₂O/H₂O n'est pas réalisé — les critères d'équilibre (thermique, mécanique, chimique) ne sont pas satisfaits.

### Question 13 (*)

Le volume molaire $V_m$ est le volume occupé par une mole ; la masse d'une mole est la masse molaire $M$ (grandeur tabulée). D'où

$$
\boxed{\rho=\frac{M}{V_m}}.
$$

### Question 14 (*)

Schéma de Lewis : l'atome d'oxygène porte **2 liaisons O–H** et **2 doublets non liants** (molécule coudée). Dans les phases condensées, chaque molécule peut former **4 liaisons hydrogène idéales** : 2 en tant que **donneur** (par les 2 liaisons O–H) et 2 en tant qu'**accepteur** (par les 2 doublets non liants) — arrangement tétraédrique.

Schéma attendu : H–O–H coudé, 2 doublets libres sur O ; 4 liaisons H pointillées vers 4 molécules voisines, géométrie tétraédrique.

### Question 15

Chaque molécule participe à 4 liaisons H, chacune partagée par 2 molécules : **2 liaisons H par molécule**. En attribuant l'enthalpie de vaporisation à la rupture de ces liaisons,

$$
\Delta_{\text{vap}}H° = 2\,E(\text{liaison H}).
$$

- $\mathrm{H_2O}$ : $E=\dfrac{40{,}66}{2}=20{,}3\ \text{kJ·mol}^{-1}$.
- $\mathrm{D_2O}$ : $E=\dfrac{41{,}52}{2}=20{,}8\ \text{kJ·mol}^{-1}$.

**Comparaison** : la liaison « deutérée » O–D···O est légèrement **plus forte** ($\sim +0{,}4\ \text{kJ·mol}^{-1}$), cohérent avec la température d'ébullition plus élevée de D₂O. (La formation de la liaison étant exothermique, on peut écrire $\Delta_{\text{form}}H°(\text{liaison H})\approx -20\ \text{kJ·mol}^{-1}$.)

### Question 16

$\rho(\mathrm{H_2O})=1{,}00$, $M=18\Rightarrow V_m=18{,}0\ \text{cm}^3\text{·mol}^{-1}$ ; $\rho(\mathrm{D_2O})=1{,}11$, $M=20\Rightarrow V_m=20/1{,}11=18{,}0\ \text{cm}^3\text{·mol}^{-1}$. Les **volumes molaires sont identiques** : la structure (longueurs des liaisons H) n'est pas modifiée par la deutération (structure électronique inchangée). La différence de masse volumique de la glace deutérée provient donc **essentiellement de la différence de masse molaire** ($20/18=1{,}11$), et non d'un changement de compacité.

### A.3 — Étude spectroscopique de H₂O et D₂O

### Question 17

Trois modes :
- **élongation symétrique** $\nu_1$ (les deux O–H s'allongent en phase) ;
- **cisaillement / déformation angulaire** $\nu_2$ (variation de l'angle H–O–H) ;
- **élongation antisymétrique** $\nu_3$ (une O–H s'allonge, l'autre se raccourcit).

Schéma attendu : les 3 modes avec flèches de déplacement des atomes.

### Question 18

Un mode est **actif en IR s'il s'accompagne d'une variation du moment dipolaire** de la molécule. L'eau étant coudée et polaire, les trois modes ($\nu_1,\nu_2,\nu_3$) modifient le moment dipolaire : **les trois modes sont actifs en IR**.

### Question 19 (*)

- $R\ll R_e$ : l'énergie croît très fortement — **répulsion** à courte distance (répulsion internucléaire et principe de Pauli entre cortèges électroniques).
- $R\gg R_e$ : l'énergie tend vers une **asymptote** ($E_p\to$ cte) — la liaison se rompt, les atomes se séparent sans interagir.
- $R_e$ : **longueur de liaison d'équilibre** (position du minimum de $E_p$).
- $D_e$ : **énergie de dissociation** (profondeur du puits, du minimum à l'asymptote).

### Question 20

Au voisinage de $R_e$, où $E_p'(R_e)=0$, le développement de Taylor donne

$$

\begin{aligned}
E_p(R) & \approx E_p(R_e)+\tfrac12\,k\,(R-R_e)^2,\qquad k\\
& = E_p''(R_e)>0.
\end{aligned}

$$

C'est une **parabole** tangente au fond du puits de Morse. L'approximation harmonique est valable pour des **oscillations de faible amplitude** (R proche de $R_e$, niveaux vibrationnels bas) ; elle devient fausse loin de $R_e$ (anharmonicité, dissociation).

Schéma attendu : courbe de Morse avec la parabole superposée au fond du puits.

### Question 21

Dans l'approximation de Born-Oppenheimer, $E_p(R)$ est l'énergie électronique à géométrie fixée : elle ne dépend que des **charges nucléaires et des électrons**, identiques pour H et D. La substitution isotopique ne change que la **masse** des noyaux, pas le potentiel $E_p(R)$ (donc ni $k$, ni $R_e$, ni $D_e$).

### Question 22 (*)

Pour un oscillateur harmonique (vibration d'une liaison), la force de rappel est proportionnelle à l'écart à l'équilibre :

$$

\begin{aligned}
F & = -k\,(R-R_e),\qquad E_p\\
& = \tfrac12 k (R-R_e)^2,
\end{aligned}

$$

$k$ étant la **constante de force** de la liaison. La pulsation propre est $\omega=\sqrt{k/\mu}$, avec $\mu$ la **masse réduite**. (À distinguer de la loi d'élasticité d'un ressort macroscopique, même si la forme est identique.)

### Question 23 (*)

Pour l'oscillateur harmonique quantique, les niveaux sont **équidistants** :

$$

\begin{aligned}
E_n & = \hbar\omega\left(n+\tfrac12\right),\qquad n\\
& = 0,1,2,\dots
\end{aligned}

$$

avec une **énergie de point zéro** $E_0=\tfrac12\hbar\omega$. $E_0,E_1,E_2,E_3$ se représentent par des segments horizontaux dans le puits parabolique, régulièrement espacés de $\hbar\omega$ (le premier à $\tfrac12\hbar\omega$ au-dessus du minimum).

Schéma attendu : parabole avec 4 niveaux horizontaux équidistants, $E_0$ au-dessus du fond.

### Question 24

Avec $\omega=2\pi c\bar\nu$, on a $\hbar\omega=hc\bar\nu$. Pour l'élongation O–H ($\bar\nu\approx 3400\ \text{cm}^{-1}=3{,}4\times10^{5}\ \text{m}^{-1}$) :

$$

\begin{aligned}
N_A\hbar\omega & = N_A h c\bar\nu\\
& = 6{,}022\times10^{23}\times6{,}626\times10^{-34}\times3{,}00\times10^{8}\times3{,}4\times10^{5}\\
& \approx 4{,}1\times10^{4}\ \text{J·mol}^{-1}\\
& = 40{,}7\ \text{kJ·mol}^{-1}.
\end{aligned}

$$

À 25 °C : $RT=8{,}314\times298=2{,}48\ \text{kJ·mol}^{-1}$.
Ainsi $N_A\hbar\omega\approx 16\times RT$, soit $N_A\hbar\omega\gg RT$. **Conclusion** : le quantum vibrationnel est très supérieur à l'énergie d'agitation thermique ; la vibration d'élongation ne peut **pas** être décrite classiquement : elle doit être traitée comme une **vibration quantique à niveaux discrets**. À température ambiante, les molécules peuplent quasi exclusivement le niveau fondamental $n=0$.

### Question 25

$\omega=\sqrt{k/\mu}$, $k$ inchangé par substitution isotopique (Q21). Avec $\mu_{OH}=\dfrac{m_O m_H}{m_O+m_H}$ et $m_O\gg m_H$, $\mu_{OH}\approx m_H$ ; de même $\mu_{OD}\approx m_D$. Donc

$$

\begin{aligned}
r & = \frac{\omega_{OH}}{\omega_{OD}}\\
& = \sqrt{\frac{\mu_{OD}}{\mu_{OH}}}\\
& \approx \sqrt{\frac{m_D}{m_H}}\\
& = \sqrt{\frac{2{,}0}{1{,}0}}\\
& = \boxed{\sqrt2}.
\end{aligned}

$$

### Question 26

Sur la figure 2, la bande d'élongation O–H de H₂O est vers $\bar\nu\approx 3400\ \text{cm}^{-1}$, celle d'élongation O–D de D₂O vers $\bar\nu\approx 2500\ \text{cm}^{-1}$. Le rapport mesuré vaut

$$
\frac{\bar\nu_{OH}}{\bar\nu_{OD}}=\frac{3400}{2500}\approx 1{,}36,
$$

à comparer à $\sqrt2=1{,}41$. L'écart (≈ 4 %) est faible : l'approximation $m_{H,D}\ll m_O$ (et le modèle harmonique) est **validée** de façon satisfaisante, l'écart résiduel provenant de l'anharmonicité et du fait que $\mu_{OH}\neq m_H$ exactement.

### A.4 — Interprétation des propriétés acide-base de H₂O et D₂O

### Question 27 (*)

Autoprotolyse : $2\,\mathrm{H_2O}=\mathrm{H_3O^+}+\mathrm{HO^-}$. L'enthalpie libre standard de réaction est la combinaison des potentiels chimiques (enthalpies libres molaires) standard :

$$
\Delta_rG°_H=\mu°(\mathrm{H_3O^+})+\mu°(\mathrm{HO^-})-2\,\mu°(\mathrm{H_2O}).
$$

### Question 28 (*)

La loi d'action de masse à l'équilibre donne $\Delta_rG°=-RT\ln K$. Ici $K=K_e$, donc

$$
\Delta_rG°_H=-RT\ln K_e.
$$

Avec $\ln K_e=-pK_e\ln 10$ :

$$
\boxed{\Delta_rG°_H=RT\ln(10)\,pK_e}.
$$

### Question 29

On pose $\Delta E_0(i)=E_0(\text{O–H})-E_0(\text{O–D})>0$ dans l'espèce $i$, abaissement d'énergie de point zéro par liaison deutérée. L'enthalpie libre standard d'une espèce deutérée s'écrit $G°_D(i)=G°_H(i)-n_i\,\Delta E_0(i)$, où $n_i$ est le nombre de liaisons O–H : $n(\mathrm{H_3O^+})=3$, $n(\mathrm{HO^-})=1$,
$n(\mathrm{H_2O})=2$. Alors

$$
\Delta_rG°_D=G°_D(\mathrm{D_3O^+})+G°_D(\mathrm{DO^-})-2G°_D(\mathrm{D_2O})
$$

$$
=\big[G°_H(\mathrm{H_3O^+})-3\Delta E_0(\mathrm{H_3O^+})\big]+\big[G°_H(\mathrm{HO^-})-\Delta E_0(\mathrm{HO^-})\big]-2\big[G°_H(\mathrm{H_2O})-2\Delta E_0(\mathrm{H_2O})\big]
$$

$$
\boxed{\Delta_rG°_D=\Delta_rG°_H-3\,\Delta E_0(\mathrm{H_3O^+})-\Delta E_0(\mathrm{HO^-})+4\,\Delta E_0(\mathrm{H_2O})}.
$$

### Question 30

Par liaison, $\Delta E_0=\tfrac12\hbar\omega_{OH}-\tfrac12\hbar\omega_{OD}=\tfrac12\hbar\omega_{OH}\big(1-\tfrac1r\big)$. Or $\hbar\omega_{OH}=hc\,\bar\nu$, donc

$$
\boxed{\Delta E_0(\mathrm{H_3O^+})=\tfrac12\,h\,c\,\bar\nu(\mathrm{H_3O^+})\left(1-\frac1r\right)=\tfrac12\,h\,c\,\bar\nu(\mathrm{H_3O^+})\left(1-\frac1{\sqrt2}\right)}.
$$

### Question 31

Facteur molaire par m⁻¹ : $\tfrac12 N_A hc\big(1-\tfrac1{\sqrt2}\big)$. Avec $N_A hc=0{,}1196\ \text{J·m·mol}^{-1}$ et $1-\tfrac1{\sqrt2}=0{,}293$ :

$$
\Delta E_0(i)=0{,}1196\times0{,}1465\times\bar\nu(i)\ [\text{m}^{-1}]\ \text{J·mol}^{-1}.
$$

Numériquement :
- $\mathrm{H_2O}$ ($3400\ \text{cm}^{-1}$) : $\Delta E_0=5{,}96\ \text{kJ·mol}^{-1}$ ;
- $\mathrm{H_3O^+}$ ($3000\ \text{cm}^{-1}$) : $\Delta E_0=5{,}26\ \text{kJ·mol}^{-1}$ ;
- $\mathrm{HO^-}$ ($3625\ \text{cm}^{-1}$) : $\Delta E_0=6{,}35\ \text{kJ·mol}^{-1}$.

Correction : $-3(5{,}26)-6{,}35+4(5{,}96)=+1{,}71\ \text{kJ·mol}^{-1}$.
$\Delta_rG°_H=RT\ln(10)\,pK_e=5{,}70\times14=79{,}9\ \text{kJ·mol}^{-1}$, d'où

$$

\begin{aligned}
\Delta_rG°_D & = 79{,}9+1{,}7\\
& = 81{,}6\ \text{kJ·mol}^{-1},\qquad pK_e^D\\
& = \frac{\Delta_rG°_D}{RT\ln 10}\\
& = \frac{81{,}6}{5{,}70}\\
& = 14{,}3.
\end{aligned}

$$

Soit $K_e^D=10^{-14{,}3}\approx 5\times10^{-15}$. Eau lourde neutre : $[\mathrm{D_3O^+}]=[\mathrm{DO^-}]$, donc

$$
pD=\tfrac12\,pK_e^D=\boxed{7{,}15}.
$$

### Question 32

Valeur expérimentale (table 1, 25 °C) : $pD=7{,}43$ ; valeur calculée : $7{,}15$. Le modèle reproduit **qualitativement** le sens de l'effet isotopique ($pD>pH=7$ : D₂O est **moins autoprotolysée** que H₂O, car l'abaissement d'énergie de point zéro stabilise davantage les réactifs deutérés), mais le **sous-estime** d'environ 0,3 unité. Les écarts proviennent des approximations : modèle purement vibrationnel (point zéro) négligeant les modes de déformation et l'anharmonicité, approximation $r=\sqrt2$, confusion enthalpie libre/énergie, et données à 20 °C/25 °C.

---

## B — Réactions de solutés dans une goutte

### B.1 — Étude des microréacteurs utilisés

### Question 33

Dans le microtube scellé, les valeurs de $\log(RAF)$ sont voisines de 0 : la cinétique y est quasi identique à celle du cœur de la solution. Ce microréacteur joue le rôle d'**expérience témoin** : milieu confiné mais sans grande interface libre ni évaporation. Il montre que l'accélération observée dans les microgouttes et les films minces **ne résulte pas d'un simple effet de confinement** (ni d'une concentration par évaporation), mais bien d'un **effet interfacial** (surface libre).

### Question 34

- **(a) Microgoutte** sphérique, diamètre $8\ \mu$m ($r=4\ \mu$m) : toute la surface est libre.

$$

\begin{aligned}
\frac{S}{V} & = \frac{4\pi r^2}{\tfrac43\pi r^3}\\
& = \frac3r\\
& = \frac{3}{4}\\
& = 0{,}75\ \mu\text{m}^{-1}.
\end{aligned}

$$

- **(b) Film mince** d'épaisseur $e=6{,}5\ \mu$m : seule la face supérieure (aire $A$) est une surface libre.

$$

\begin{aligned}
\frac{S_{\text{libre}}}{V} & = \frac{A}{A\,e}\\
& = \frac1e\\
& = \frac{1}{6{,}5}\\
& = 0{,}15\ \mu\text{m}^{-1}.
\end{aligned}

$$

### Question 35

La microgoutte ($S/V=0{,}75\ \mu\text{m}^{-1}$) présente une surface spécifique libre $\sim5$ fois plus grande que le film ($0{,}15\ \mu\text{m}^{-1}$). Les facteurs d'accélération suivent la même hiérarchie ($\log RAF$ microgouttes $>$ films $>$ bulk/tube scellé). L'accélération croît donc avec la **surface spécifique libre** : la réaction est **accélérée à l'interface**, et d'autant plus que la part d'interface est grande.

### B.2 — Addition d'aza-Michael

### Question 36 (*)

- **A** : $\mathrm{CH_2{=}CH{-}CO{-}NH_2}$ = **prop-2-énamide** (acrylamide). Fonctions : **amide** et **alcène** (liaison C=C ; énone-amide conjugué).
- **B** : $\mathrm{H_2N{-}(CH_2)_3{-}N(C_4H_9)_2}$ = **$N,N$-dibutylpropane-1,3-diamine** ($M=186\ \text{g·mol}^{-1}$). Fonctions : **amine primaire** et **amine tertiaire**.

### Question 37 (*)

Le réactif B porte des fonctions amine, dont le doublet non liant de l'azote confère **deux types de réactivité** : caractère **nucléophile** (attaque d'un site électrophile) et caractère **basique** (capture d'un proton, base de Brønsted).

### Question 38 (*)

A est une **énone conjuguée** (amide α,β-insaturé) : la conjugaison C=C–C=O appauvrit en électrons le **carbone β** (CH₂= terminal). A peut donc réagir avec le nucléophile B (amine primaire) : l'amine attaque le **carbone β** (addition de type 1,4 / Michael). Les **sites électrophiles** de A sont le carbone β (visé en addition conjuguée) et, secondairement, le carbone du carbonyle.

### Question 39

On compare les deux interactions frontalières possibles :
- HO(B)/BV(A) : $|{-}6{,}45-({-}1{,}24)|=5{,}21\ \text{eV}$ ;
- HO(A)/BV(B) : $|{-}7{,}11-0{,}87|=7{,}98\ \text{eV}$.
L'écart le plus faible est HO(B)/BV(A) : c'est l'**interaction dominante** (B nucléophile par sa HO, A électrophile par sa BV). La **régiosélectivité** est ensuite fixée par le recouvrement : l'attaque s'effectue là où le **coefficient de la BV de A est le plus grand**, c'est-à-dire sur le **carbone β** (CH₂= terminal, visible sur la représentation de la BV de A). Le contrôle orbitalaire prédit donc l'addition 1,4.

### Question 40 (*)

1. **Protonation** de A sur l'**oxygène** du carbonyle : $\mathrm{A+H^+}\rightleftharpoons \mathrm{AH^+}$, formant un cation stabilisé par mésomérie (accepteur de Michael activé, plus électrophile). *(flèche : doublet de O vers H⁺.)*
2. **Addition** de l'amine (doublet de N) sur le carbone β de $\mathrm{AH^+}$ : formation de la liaison C–N et déplacement de la double liaison vers l'énol/iminium : $\mathrm{AH^+ + B\to IR}$. *(flèches : doublet de N → Cβ ; liaison C=C → Cα.)*
3. **Prototropie** : $\mathrm{IR\to P+H^+}$ — déprotonation de l'azote puis tautomérie énol → amide, régénérant $\mathrm{H^+}$ et donnant le produit $\mathrm{P}=\mathrm{H_2N{-}CO{-}CH_2{-}CH_2{-}NH{-}(CH_2)_3{-}N(C_4H_9)_2}$.

Schéma attendu : enchaînement avec flèches courbes partant toutes d'un **doublet** (et non d'une charge).

### Question 41

Le profil $E_p$ = f(c.r.) présente : un **pré-équilibre rapide** de protonation (faible barrière, minimum $\mathrm{AH^+}$), puis l'**étape cinétiquement déterminante** d'addition (barrière la plus haute, minimum $\mathrm{IR}$), enfin une **étape rapide** de prototropie menant à $\mathrm{P}$.

Schéma attendu : profil à **trois** bosses, barrière centrale la plus haute, intermédiaires $\mathrm{AH^+}$ et $\mathrm{IR}$.

### Question 42

L'étape déterminante est l'étape 2, $\mathrm{AH^+ + B\to IR}$, **bimoléculaire**. Avec le pré-équilibre rapide de l'étape 1 ($[\mathrm{AH^+}]=K_1[\mathrm{A}][\mathrm{H^+}]$) :

$$
v=k_2[\mathrm{AH^+}][\mathrm{B}]=k_2K_1[\mathrm{A}][\mathrm{H^+}][\mathrm{B}].
$$

À $[\mathrm{H^+}]$ fixé (assistance acide à l'interface), $v\propto[\mathrm{A}][\mathrm{B}]$ : la réaction est d'**ordre global 2** vis-à-vis des réactifs, ce qui justifie l'hypothèse d'une **réaction bimoléculaire**.

### B.3 — Étude cinétique expérimentale

### Question 43 (*)

**Principe** : les molécules sont **ionisées** (ici par électronébulisation, formation d'ions $\mathrm{[M+H]^+}$ par protonation), **accélérées**, puis **séparées selon leur rapport masse/charge $m/z$** (champ magnétique/électrique ou temps de vol) et détectées ; l'abondance relative est portée en ordonnée.
**Pics** :
- $m/z=187$ : réactif $\mathrm{B}$ protoné, $\mathrm{[B+H]^+}$, $M(\mathrm{B})=186$, donc $m=187$, $z=1$ ;
- $m/z=258$ : produit $\mathrm{P}$ protoné, $\mathrm{[P+H]^+}$, $M(\mathrm{P})=186+71=257$, donc $m=258$, $z=1$.
(Le produit résulte de l'addition de l'acrylamide $A$, $M=71$, sur $B$.)

### Question 44 (*)

Les deux réactifs sont introduits à la même concentration $[\mathrm{SM}]_0$ et se consomment selon une stœchiométrie 1:1 ; donc à tout instant $[\mathrm{A}]=[\mathrm{B}]=[\mathrm{SM}]$. La réaction étant d'ordre 2 (Q42), $v=k[\mathrm{A}][\mathrm{B}]=k[\mathrm{SM}]^2$, d'où

$$

\begin{aligned}
\frac{d[\mathrm{SM}]}{dt}+k\,[\mathrm{SM}]^2 &= 0,\\
&\qquad(\alpha=2).
\end{aligned}

$$

### Question 45

L'intégration de Q44 donne $\dfrac{1}{[\mathrm{SM}]}=\dfrac{1}{[\mathrm{SM}]_0}+kt$. Conservation : $[\mathrm{P}]=[\mathrm{SM}]_0-[\mathrm{SM}]$, donc

$$
\frac{[\mathrm{P}]}{[\mathrm{SM}]}=\frac{[\mathrm{SM}]_0}{[\mathrm{SM}]}-1=[\mathrm{SM}]_0\,k\,t.
$$

Le rapport $[\mathrm{P}]/[\mathrm{SM}]$ est donc **linéaire en $t$**, de pente $k[\mathrm{SM}]_0$. Les figures 7a, 7b, 7c (droites) **confirment l'ordre 2**.

### Question 46

Trois sources d'incertitude sur la pente de la droite $\ln k=f(1/T)$ (fig. 7d) :
1. le **nombre insuffisant de points** (trois seulement) ;
2. l'incertitude sur la **température** $T$ (donc sur $1/T$) ;
3. l'incertitude sur chaque **constante $k$**, elle-même issue des pentes des droites 7a–c (mesures de $[\mathrm{P}]/[\mathrm{SM}]$ par spectrométrie de masse, calibration interne).

### Question 47 (*)

La droite $\ln k=f(1/T)$ correspond à la **loi d'Arrhenius** :

$$

\begin{aligned}
k & = A\,\exp\!\left(-\frac{E_a}{RT}\right)\\\
& \Longrightarrow \ \ln k\\
& = \ln A-\frac{E_a}{R}\cdot\frac1T,
\end{aligned}

$$

de pente $-E_a/R$.

### Question 48

La pente est $-5{,}68\times10^{3}\ \text{K}$ (négative), soit $E_{a,\text{app}}=-\text{pente}\times R=5{,}68\times10^{3}\times8{,}314\approx 47\ \text{kJ·mol}^{-1}>0$. Comme $k_{\text{obs}}=K_1k_2$ (pré-équilibre), $\dfrac{d\ln k_{\text{obs}}}{d(1/T)}=-\dfrac{\Delta_rH_1°+E_{a,2}}{R}$. La pente **négative** (donc $E_{a,\text{app}}>0$) signifie $\Delta_rH_1°+E_{a,2}>0$ : l'énergie d'activation de l'étape **bimoléculaire** déterminante
($E_{a,2}$) domine, et la vitesse **croît avec la température**.

### Question 49

D'après Q45, $\dfrac{[\mathrm{P}]}{[\mathrm{SM}]}=k\,[\mathrm{SM}]_0\,t$. En comparant microréacteur et solution au **même instant $t$** et à la **même concentration initiale** :

$$
RAF=\frac{k_{\text{micro}}}{k_{\text{sol}}}=\frac{\big([\mathrm{P}]/[\mathrm{SM}]\big)_{\text{micro}}}{\big([\mathrm{P}]/[\mathrm{SM}]\big)_{\text{sol}}}.
$$

### Question 50

Dans un solvant polaire protique (eau, méthanol), la **solvatation stabilise** (abaisse l'énergie) les espèces, d'autant plus qu'elles portent une **charge localisée** : les ions $\mathrm{A^+}$ et $\mathrm{B}$ sont fortement solvatés (interactions ion-dipôle, liaisons H). Les espèces neutres le sont moins. Le **complexe activé** $\mathrm{[A{-}B]^+}$ porte la même charge globale mais **répartie / diffuse** sur un édifice plus grand : il est **moins stabilisé** par la solvatation que les réactifs à charges localisées.

### Question 51

En **solution** (bulk), la solvatation complète stabilise fortement les réactifs ioniques (charges localisées), davantage que le complexe activé (charge diffuse) : l'état initial est abaissé relativement à l'état de transition → **barrière d'activation plus élevée**. À l'**interface**, la solvatation est réduite (moins de molécules de solvant) : les réactifs sont moins stabilisés, l'écart à l'état de transition diminue → **barrière plus basse**. On attribue donc :
- le profil de **plus faible** énergie d'activation → **interface** ;
- le profil de **plus haute** énergie d'activation → **solution**.

### Question 52

La barrière d'activation étant **plus faible à l'interface**, la constante de vitesse $k=A\exp(-E_a/RT)$ y est **plus grande** : la **vitesse de réaction est accrue à l'interface** ($RAF>1$), conformément aux observations.

---

## C — Évolution de l'acidité dans une goutte

### Question 53 (*)

Cœur de la goutte, comportement idéal, référence « soluté infiniment dilué » :

$$
\mu_{\mathrm{Sol}}=\mu°_{\mathrm{Sol}}(T,\mathrm{H^+})+RT\ln\!\left(\frac{[\mathrm{H^+}]_{\mathrm{sol}}}{c°}\right).
$$

### Question 54 (*)

À l'interface, même référence mais solution non idéale :

$$
\mu_i=\mu°_{\mathrm{Sol}}(T,\mathrm{H^+})+RT\ln a_i=\mu°_{\mathrm{Sol}}(T,\mathrm{H^+})+RT\ln\!\left(\gamma_{i,\mathrm{H^+}}\,\frac{[\mathrm{H^+}]_i}{c°}\right).
$$

### Question 55

À l'équilibre, $\mu_i=\mu_{\mathrm{Sol}}$, d'où

$$
\gamma_{i,\mathrm{H^+}}\,[\mathrm{H^+}]_i=[\mathrm{H^+}]_{\mathrm{sol}}.
$$

Comme le pH est défini à partir de l'**activité** et que $a_i=a_{\mathrm{sol}}$ à l'équilibre, le **pH ne diffère pas** entre interface et cœur (même activité). En revanche, les **concentrations** peuvent différer.

### Question 56

De Q55 :

$$
\boxed{[\mathrm{H^+}]_i=\frac{[\mathrm{H^+}]_{\mathrm{sol}}}{\gamma_{i,\mathrm{H^+}}}}.
$$

### Question 57 (*)

Avec un standard de référence $\mu_i°(T,\mathrm{H^+})$ propre à l'interface (solution y supposée idéale) :

$$
\mu_i=\mu_i°(T,\mathrm{H^+})+RT\ln\!\left(\frac{[\mathrm{H^+}]_i}{c°}\right).
$$

En identifiant avec l'expression de Q54 :

$$
\mu_i°(T,\mathrm{H^+})+RT\ln\frac{[\mathrm{H^+}]_i}{c°}=\mu°_{\mathrm{Sol}}(T,\mathrm{H^+})+RT\ln\frac{\gamma_{i,\mathrm{H^+}}[\mathrm{H^+}]_i}{c°}
$$

$$
\boxed{\mu_i°(T,\mathrm{H^+})-\mu°_{\mathrm{Sol}}(T,\mathrm{H^+})=RT\ln\gamma_{i,\mathrm{H^+}}}.
$$

### Question 58 (*)

Pour $\mathrm{H^+(c\oe ur)=H^+(interface)}$ :

$$
\Delta_rG°=\Delta_fG°(\mathrm{H^+_i})-\Delta_fG°(\mathrm{H^+_{sol}}).
$$

### Question 59

Les potentiels standard sont les enthalpies libres standard de formation. D'après Q57-Q58, $RT\ln\gamma_{i,\mathrm{H^+}}=\mu_i°-\mu°_{\mathrm{Sol}}=\Delta_fG°(\mathrm{H^+_i})-\Delta_fG°(\mathrm{H^+_{sol}})$, donc

$$
\boxed{\gamma_{i,\mathrm{H^+}}=\exp\!\left(\frac{\Delta_fG°(\mathrm{H^+_i})-\Delta_fG°(\mathrm{H^+_{sol}})}{RT}\right)}.
$$

### Question 60

$\Delta_fG°(\mathrm{H^+_i})-\Delta_fG°(\mathrm{H^+_{sol}})=-5{,}9\ \text{kJ·mol}^{-1}<0$ : l'ion hydronium est **plus stable à l'interface**. $\Delta_fG°(\mathrm{OH^-_i})-\Delta_fG°(\mathrm{OH^-_{sol}})=+11{,}3\ \text{kJ·mol}^{-1}>0$ : l'ion hydroxyde est **moins stable à l'interface**. L'interface **enrichit en $\mathrm{H_3O^+}$** et **appauvrit en $\mathrm{OH^-}$** : l'espèce **majoritaire à l'interface est $\mathrm{H_3O^+}$** (interface plus acide).

### Question 61

Quatre équations :
1. **Électroneutralité globale** (goutte d'eau pure, neutre au total) :

$$
[\mathrm{H^+}]_{\mathrm{sol}}V_C+[\mathrm{H^+}]_iV_i=[\mathrm{OH^-}]_{\mathrm{sol}}V_C+[\mathrm{OH^-}]_iV_i,
$$

où $V_C$ est le **volume du cœur** et $V_i$ le **volume de l'interface**.
2. Équilibre de $\mathrm{H^+}$ (Q56) : $[\mathrm{H^+}]_{\mathrm{sol}}=[\mathrm{H^+}]_i\,\gamma_{i,\mathrm{H^+}}$.
3. Équilibre de $\mathrm{OH^-}$ : $[\mathrm{OH^-}]_{\mathrm{sol}}=[\mathrm{OH^-}]_i\,\gamma_{i,\mathrm{OH^-}}$.
4. Autoprotolyse (cœur idéal) : $K_e\,c°^2=[\mathrm{H^+}]_{\mathrm{sol}}\,[\mathrm{OH^-}]_{\mathrm{sol}}$.

### Question 62

Cœur sphérique de rayon $R-d$, interface = coquille d'épaisseur $d$ :

$$

\begin{aligned}
V_C & = \frac43\pi(R-d)^3,\qquad V_i\\
& = \frac43\pi\big[R^3-(R-d)^3\big].
\end{aligned}

$$

### Question 63

Coefficients ($RT=8{,}314\times298=2477{,}6\ \text{J·mol}^{-1}$) :

$$

\begin{aligned}
\gamma_{i,\mathrm{H^+}} & = \exp\!\left(\frac{-5900}{2477{,}6}\right)\\
& = e^{-2{,}38}\\
& = 0{,}0924,\qquad \gamma_{i,\mathrm{OH^-}}\\
& = \exp\!\left(\frac{+11300}{2477{,}6}\right)\\
& = e^{4{,}56}\\
& = 95{,}7.
\end{aligned}

$$

Géométrie ($R=10$ nm, $d=0{,}5$ nm, $R-d=9{,}5$ nm ; on raisonne en unités de $(\text{nm})^3$) : $V_C\propto 9{,}5^3=857{,}4$, $V_i\propto 10^3-9{,}5^3=142{,}6$.
En substituant (2),(3) dans (1) : $[\mathrm{H^+}]_{\mathrm{sol}}\big(V_C+\tfrac{V_i}{\gamma_{i,\mathrm{H^+}}}\big)=[\mathrm{OH^-}]_{\mathrm{sol}}\big(V_C+\tfrac{V_i}{\gamma_{i,\mathrm{OH^-}}}\big)$, soit

$$

\begin{aligned}
[\mathrm{H^+}]_{\mathrm{sol}}\times 2401 & = [\mathrm{OH^-}]_{\mathrm{sol}}\times 858{,}9\\\
& \Rightarrow \ [\mathrm{OH^-}]_{\mathrm{sol}}\\
& = 2{,}80\,[\mathrm{H^+}]_{\mathrm{sol}}.
\end{aligned}

$$

Avec (4), $[\mathrm{H^+}]_{\mathrm{sol}}^2\times 2{,}80=10^{-14}\Rightarrow[\mathrm{H^+}]_{\mathrm{sol}}=5{,}98\times10^{-8}\ \text{mol·L}^{-1}$. Alors

$$

\begin{aligned}
[\mathrm{H^+}]_i & = \frac{[\mathrm{H^+}]_{\mathrm{sol}}}{\gamma_{i,\mathrm{H^+}}}\\
& = \frac{5{,}98\times10^{-8}}{0{,}0924}\\
& = 6{,}5\times10^{-7}\ \text{mol·L}^{-1}.
\end{aligned}

$$

pH d'une solution idéale à cette concentration : $-\log(6{,}5\times10^{-7})=\boxed{6{,}2}$.

### Question 64

La première étude (partie B) attribuait l'accélération à une **solvatation réduite** à l'interface, abaissant l'énergie d'activation de l'étape bimoléculaire. Le second modèle (partie C) montre que l'interface est **nettement plus acide** ($[\mathrm{H^+}]_i\approx 6{,}5\times10^{-7}$, pH ≈ 6,2, contre ≈ 7 au cœur) : l'enrichissement local en $\mathrm{H_3O^+}$ fournit une **catalyse acide** — précisément le proton requis par le mécanisme acido-catalysé de l'aza-Michael (Q40). Les deux effets se **complètent** : désolvatation du complexe activé **et** surconcentration en hydronium concourent à accélérer les réactions à la surface des microgouttes.
