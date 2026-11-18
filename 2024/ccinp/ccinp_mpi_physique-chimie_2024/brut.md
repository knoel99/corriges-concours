# CCINP MPI — Physique-chimie 2024 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Partie I — Les besoins en eau du pin maritime (ou pin des Landes)

### Question 1

**a)** Dans un conducteur ohmique de conductivité $\sigma$, la loi d’Ohm locale donne $\vec j=\sigma\vec E=-\sigma\nabla V$.

Le potentiel hydrique $\psi$ joue le rôle de $V$, et $\vec j_M$ celui de $\vec j$. Dans la relation $\vec j_M=-\gamma\nabla\psi$, **la conductivité hydraulique est $\gamma=K/(\rho_e g)$**.

**b)** Comme $I=\iint_S\vec j\cdot\mathrm d\vec S$, le flux de $\vec j_M$ à travers la surface orientée joue le rôle de **l’intensité électrique $I$**.

### Question 2

**a)** En orientant le débit de $A$ vers $B$, on définit **$R_H=(\psi_A-\psi_B)/D$**.

**b)** Le potentiel hydrique s’exprime en $\mathrm{Pa}=\mathrm{kg\,m^{-1}\,s^{-2}}$ et le débit en $\mathrm{kg\,s^{-1}}$. Ainsi **$[R_H]=\mathrm{m^{-1}\,s^{-1}}$**.

### Question 3

Le long d’une racine, de l’extrémité côté sol vers le point $O$, la loi de Darcy donne $-\nabla\psi=\vec j_M/\gamma_r$. En régime stationnaire, le débit $D_r$ est le même à travers toute section droite de la racine. Dans le modèle cylindrique homogène, sa densité de courant axiale vaut $D_r/s_r$. La circulation donne

$$
\psi_S-\psi_O=\int_{S}^{O}(-\nabla\psi)\cdot\mathrm d\vec\ell
=\frac{D_r l_r}{\gamma_r s_r}.
$$

Les $N$ racines ont les mêmes potentiels aux deux extrémités, et leurs débits s’additionnent. **Elles sont en parallèle**, donc

$$
\boxed{\begin{gathered}
R_r=\frac{l_r}{\gamma_r s_r}\\
R_N=\frac{R_r}{N}.
\end{gathered}}
$$

### Question 4

En régime stationnaire, sans accumulation ni branchement extérieur à la chaîne, le débit total sortant des racines traverse successivement le tronc, les feuilles et l’interface. Le **même débit** traverse donc les quatre résistances, qui sont en série. La résistance de l’arbre vaut $R_p=R_N+R_t+R_f$.

![Circuit hydraulique équivalent avec débit commun du sol vers l’atmosphère](figures/q04-circuit.svg)

### Question 5

La figure 2 donne $\psi_S=-0{,}05\,\mathrm{MPa}$, $\psi_F=-1{,}5\,\mathrm{MPa}$ aux feuilles du sommet, et $\psi_A=-100\,\mathrm{MPa}$ en atmosphère. Dans l’arbre et dans l’interface, le même débit vaut respectivement $(\psi_S-\psi_F)/R_p$ et $(\psi_F-\psi_A)/R_a$. Donc

$$
\boxed{R_a=R_p\frac{\psi_F-\psi_A}{\psi_S-\psi_F}
\simeq6{,}8\times 10^{10}\,\mathrm{m^{-1}\,s^{-1}}.}
$$

### Question 6

Avec $D=(\psi_S-\psi_F)/R_p=1{,}45\times10^{-3}\,\mathrm{kg\,s^{-1}}$ conservé pendant les douze heures d’exposition et un débit nocturne négligé, la masse évapo-transpirée est

$$
\boxed{m=D\,\Delta t\simeq63\,\mathrm{kg}\ \text{par pin et par jour}.}
$$

### Question 7

La plage de $15$ à $25\,\mathrm{t}$ par hectare et par jour correspond, en divisant par $300$, à **$50$ à $83\,\mathrm{kg}$ par pin et par jour**.

Les $63\,\mathrm{kg}$ calculés en Q6 sont dans cet intervalle. Réciproquement, le modèle donne environ $19\,\mathrm{t\,ha^{-1}\,j^{-1}}$.

## Partie II — Gemmage en forêt landaise et distillation de la résine de pin

### Question 8

Dans le diagramme $(T,p)$, $T$ est en abscisse et $p$ en ordonnée. Les courbes de sublimation, fusion et vaporisation se rejoignent au **point triple**. La vaporisation s’arrête au **point critique**, au-delà duquel la distinction liquide–gaz disparaît. Pour l’eau, la courbe de fusion de la glace ordinaire a une pente négative.

![Diagramme de phases schématique de l’eau pure avec point triple et point critique](figures/q08-phases.svg)

### Question 9

Le pinène a pour masse molaire $M_p=136\,\mathrm{g\,mol^{-1}}$. À l’équilibre, sa pression partielle vaut $p_p=430\,\mathrm{Pa}$. Le gaz parfait donne la concentration massique

$$
\boxed{\frac{m_p}{V}=\frac{M_p p_p}{RT}\simeq24\,\mathrm{g\,m^{-3}}.}
$$

La valeur est presque cinq fois la limite de $5\,\mathrm{g\,m^{-3}}$. **Le local saturé est dangereux selon le critère de l’énoncé.**

### Question 10

À l’ébullition du corps pur, la pression de vapeur saturante égale la pression extérieure. Sur la figure 5, l’horizontale $1\,\mathrm{bar}$ coupe $p_p(T)$ à **$T\simeq430\,\mathrm K$, soit $157\,^\circ\mathrm C$**.

### Question 11

En présence des deux liquides non miscibles, l’ébullition vérifie $p_e(T)+p_p(T)=1\,\mathrm{bar}$. L’intersection de la courbe somme avec cette horizontale donne **$T_{\mathrm{éb}}\simeq368\,\mathrm K$, soit $95\,^\circ\mathrm C$**. Cette température est inférieure à celle d’ébullition du pinène seul.

### Question 12

À cette abscisse, les courbes donnent environ **$p_e\simeq0{,}85\,\mathrm{bar}$** et **$p_p\simeq0{,}15\,\mathrm{bar}$**. Leur somme est cohérente avec $1\,\mathrm{bar}$ à la précision graphique.

### Question 13

À même température et dans le même volume gazeux, le rapport des quantités de matière est $n_e/n_p=p_e/p_p$. Pour un condensat qui recueille ces quantités sans perte,

$$
\boxed{\frac{m_e}{m_p}=\frac{M_e p_e}{M_p p_p}\simeq0{,}75.}
$$

Il faut **vaporiser environ $0{,}75\,\mathrm{kg}$ d’eau** pour obtenir $1\,\mathrm{kg}$ de pinène, dans ce modèle.

## Partie III — La marche du berger landais sur échasses

## III.1 — Étude de la phase d’oscillation gauche

### Question 14

Dans le référentiel du buste supposé galiléen, on étudie la jambe gauche autour de l’axe fixe $F_g y$. La liaison pivot idéale a un moment axial nul. La direction de la jambe orientée du pied vers la hanche fait l’angle $\theta$ avec la verticale ascendante, positif dans le sens de la figure 7b. On écrit donc $\overrightarrow{F_gG_{jg}}=-\Delta(\sin\theta\,\vec u_x+\cos\theta\,\vec u_z)$ et $\vec P=-m_jg\,\vec u_z$. Le moment du poids projeté sur $\vec u_y$ vaut $-m_jg\Delta\sin\theta$. Le théorème du moment cinétique projeté donne

$$
\boxed{J_F\ddot\theta=-m_jg\Delta\sin\theta.}
$$

### Question 15

La position d’équilibre stable correspond à la jambe suspendue verticalement, soit $\theta=0$ dans la convention de Q14. Pour de petits écarts, $\sin\theta\simeq\theta$. La jambe décrit une oscillation harmonique de pulsation $\omega_{\mathrm{os}}$. Elle passe d’une extrémité de l’oscillation à l’autre pendant une demi-période. Ainsi

$$
\boxed{\begin{gathered}
\omega_{\mathrm{os}}=\sqrt{\frac{m_jg\Delta}{J_F}}\\
\tau_{\mathrm{os}}=\frac{\pi}{\omega_{\mathrm{os}}}.
\end{gathered}}
$$

## III.2 — Étude de la phase de double contact

### Question 16

L’énergie cinétique de rotation de la jambe droite gagne $\tfrac12 J_O\Omega(\tau_{\mathrm{dc}})^2$ car sa vitesse angulaire initiale est nulle. La jambe gauche gagne autant par hypothèse. La translation quasi uniforme du buste donne une variation cinétique négligeable. Ses variations d’énergie potentielle valent $m_bgh$, tandis que celles des jambes sont négligées. On en déduit

$$
\boxed{\Delta E=J_O\Omega(\tau_{\mathrm{dc}})^2+m_bgh.}
$$

## III.3 — Coût énergétique et pas optimal de la marche ordinaire

### Question 17

Dans le référentiel galiléen du sol, la variation d’énergie mécanique d’un système est égale à la somme des travaux des forces dont l’énergie potentielle n’est pas déjà comptabilisée, y compris le travail interne pertinent pour un système articulé. Les réactions du sol aux contacts fixes ne travaillent pas. Le poids est pris en compte dans l’énergie potentielle. En négligeant les pertes, il reste le travail moteur des muscles, soit $P\tau_{\mathrm{dc}}$ pour une puissance quasi constante. **On obtient $P=\Delta E/\tau_{\mathrm{dc}}$.**

### Question 18

On remplace dans Q16 $\Omega(\tau_{\mathrm{dc}})^2$ par $m_jg\Delta/J_F$ et $h$ par $p^2/(2l_j)$. Avec $1/\tau_{\mathrm{dc}}=V_{\mathrm{dc}}/p$, la relation de Q17 donne

$$
\boxed{P=gV_{\mathrm{dc}}\left(
\frac{J_O}{J_F}\frac{m_j\Delta}{p}
+\frac{m_b p}{2l_j}\right).}
$$

### Question 19

À vitesse $V_{\mathrm{dc}}$ fixée, la puissance est proportionnelle à $A/p+Bp$ pour $p>0$, avec $A=(J_O/J_F)m_j\Delta>0$ et $B=m_b/(2l_j)>0$.

Sa dérivée vaut $-A/p^2+B$, négative puis positive de part et d’autre de $\sqrt{A/B}$. L’unique minimum est donc atteint pour

$$
\boxed{p_{\mathrm{opt}}=\sqrt{\frac{2l_jJ_Om_j\Delta}{J_Fm_b}}.}
$$

### Question 20

Pour une jambe uniforme, $\Delta=l_j/2$ et $J_O=J_F$. Ainsi **$p_{\mathrm{opt}}=l_j\sqrt{m_j/m_b}\simeq0{,}41\,\mathrm m$**.

## III.4 — Pas optimal avec des échasses

### Question 21

**a)** La tige supplémentaire étant sans masse, $m_j$, $m_b$, $\Delta$ et $J_F$ sont inchangés.

Le pivot au sol passe de $O$ à $E$, d’où le remplacement de $J_O$ par $J_E^*$. La longueur utilisée dans la relation géométrique de hauteur passe de $l_j$ à $l_j+l^*$.

**b)** En appliquant Q19,

$$
\boxed{p_{\mathrm{opt}}^*
=\sqrt{\frac{2(l_j+l^*)J_E^*m_j\Delta}{J_Fm_b}}.}
$$

$$
\boxed{\frac{p_{\mathrm{opt}}^*}{p_{\mathrm{opt}}}
=\sqrt{\frac{J_E^*}{J_O}\left(1+\frac{l^*}{l_j}\right)}.}
$$

### Question 22

**a)** Posons $r=l^*/l_j$. Le tableau donne $J_E^*/J_O=1+3r+3r^2$, donc **$p_{\mathrm{opt}}^*/p_{\mathrm{opt}}=\sqrt{(1+r)(1+3r+3r^2)}$**.

**b)** Pour $r=1$, le rapport vaut **$\sqrt{14}\simeq3{,}74$**.

**c)** En phase oscillante, la rotation est toujours autour du pivot fémoral. Comme $\Delta$, $m_j$ et $J_F$ sont inchangés, **$\omega_{\mathrm{os}}$ et $\tau_{\mathrm{os}}$ sont inchangées**.

**d)** Avec la proportionnalité donnée, le rapport des vitesses vaut le rapport des pas, soit **$V^*/V\simeq3{,}74$** dans ce cas. Le modèle prévoit une augmentation marquée de la vitesse. Une telle estimation est à nuancer, notamment parce que $p_{\mathrm{opt}}^*\simeq1{,}53\,\mathrm m$ pour une jambe équivalente de $2\,\mathrm m$, ce qui éloigne la géométrie du régime asymptotique des très petits angles.

## Partie IV — La préparation du pastis landais

### Question 23

On additionne la dissociation acide de $\mathrm{H_2P_2O_7^{2-}}$ de constante $K_{a1}$, la protonation de $\mathrm{HCO_3^-}$ en $\mathrm{CO_{2,aq}}$ et eau de constante $1/K_{a3}$.

On ajoute ensuite le dégazage de $\mathrm{CO_{2,aq}}$ de constante $1/K_s$. Les constantes se multiplient.

$$
\boxed{K_1=\frac{K_{a1}}{K_{a3}K_s}\simeq14.}
$$

### Question 24

Les masses molaires des deux sels sont $M_d=222\,\mathrm{g\,mol^{-1}}$ et $M_b=84\,\mathrm{g\,mol^{-1}}$. La stœchiométrie impose $m_d/M_d=m_b/M_b$. La somme $m_d+m_b$ vaut $11\,\mathrm g$ après retrait de l’amidon. Les deux masses sont donc

$$
\boxed{m_d=11\,\mathrm g\,\frac{M_d}{M_d+M_b}\simeq8{,}0\,\mathrm g,\qquad
m_b\simeq3{,}0\,\mathrm g.}
$$

### Question 25

La quantité produite est $n_{\mathrm{CO_2}}=(m_d+m_b)/(M_d+M_b)\simeq3{,}59\times10^{-2}\,\mathrm{mol}$ puisque la réaction est totale et la préparation stœchiométrique. Sous $p=1\,\mathrm{bar}$ à $T=443\,\mathrm K$, le volume est

$$
\boxed{V=\frac{n_{\mathrm{CO_2}}RT}{p}\simeq1{,}32\,\mathrm L.}
$$

### Question 26

**a)** À pH croissant, les espèces phosphorées prédominantes sont successivement $\mathrm{H_2P_2O_7^{2-}}$ (courbe 1), $\mathrm{HP_2O_7^{3-}}$ (2) et $\mathrm{P_2O_7^{4-}}$ (3). La droite décroissante 4 vérifie $\log_{10}([\mathrm{H_3O^+}]/c^\circ)=-\mathrm{pH}$. La droite croissante 5 vérifie $\log_{10}([\mathrm{OH^-}]/c^\circ)=\mathrm{pH}-14$.

**b)** Le plateau de la courbe 1 en milieu acide, où la première espèce représente pratiquement tout le phosphore sous forme diphosphate, est vers $-0{,}45$. On en tire **$C_p\simeq0{,}35$ à $0{,}36\,\mathrm{mol\,L^{-1}}$**.

**c)** Au point $P$, les concentrations de l’acide et de sa base conjuguée du premier couple sont égales, donc $\mathrm{pH}_P=pK_{a1}=6{,}7$. Au point $Q$, la même propriété pour le second couple donne **$\mathrm{pH}_Q=pK_{a2}=9{,}3$**.

### Question 27

Après la réaction totale et le dégazage, l’espèce introduite dans l’équilibre (a) est $\mathrm{HP_2O_7^{3-}}$. La réaction (a) forme les deux autres espèces phosphorées en quantités égales. Le pH se lit donc à l’intersection des courbes 1 et 3, vers **$\mathrm{pH}\simeq8{,}0$**. En effet, l’égalité des concentrations extrêmes donne aussi $\mathrm{pH}=(pK_{a1}+pK_{a2})/2$ en combinant les deux lois d’action des masses.

## Partie V — Système d’arrosage automatique d’un green de golf

### Question 28

$$
\begin{array}{ccc}
\text{Entrée 1} & \text{Entrée 2} & \text{NAND} \\ \hline
0 & 0 & 1 \\
0 & 1 & 1 \\
1 & 0 & 1 \\
1 & 1 & 0 \\
\end{array}
$$

Avec les entrées reliées, $\overline{x\land x}=\overline x$. **La porte devient un inverseur.**

### Question 29

Au nœud de potentiel $u_2$, le courant d’entrée des portes et le prélèvement de l’étage suivant sont négligés.

Le courant venant de $u_1$ par $R$ est $(u_1-u_2)/R$. Il entre dans la borne de $C$ au potentiel $u_2$ puis ressort au potentiel $u$.

Avec cette convention, il vaut $C\,\mathrm du_c/\mathrm dt$, où $u_c=u_2-u$. En remplaçant $u_2$ par $u+u_c$, on obtient l’équation avec la constante de temps $\tau=RC$.

$$
\boxed{\tau\frac{\mathrm du_c}{\mathrm dt}+u_c=u_1-u.}
$$

La porte 2 inverse le niveau de $u_2$ et fournit $u_1$. La porte 1 inverse à son tour $u_1$ et fournit $u$.

### Question 30

**a)** Lorsque $u_1=V_a$, la porte 1 fournit **$u(0^+)=0$** et maintient $u=0$. L’équation de Q29 a pour second membre $V_a$. Avec $u_c(0)=0$, on obtient, sur $[0,t_b[$,

$$
\boxed{u_c(t)=u_2(t)=V_a(1-e^{-t/\tau}).}
$$

**b)** La porte 2 bascule dès que son entrée $u_2$ atteint $V_b$. Donc

$$
\boxed{t_b=\tau\ln\!\left(\frac{V_a}{V_a-V_b}\right).}
$$

### Question 31

**a)** À la montée de $u_2$ jusqu’au seuil, la porte 2 donne $u_1=0$, puis la porte 1 donne $u=V_a$.

La tension $u_c$ est continue et vaut encore $V_b$ à la commutation. L’entrée $u_2$ saute à $V_a+V_b$, ce qui maintient la porte 2 dans son nouvel état. L’équation devient **$\tau\dot u_c+u_c=-V_a$**.

**b)** En prenant l’origine du temps de cette phase en $t_b$,

$$
\boxed{\begin{aligned}
u_c(t)&=-V_a+(V_a+V_b)e^{-(t-t_b)/\tau},\\
u_2(t)&=(V_a+V_b)e^{-(t-t_b)/\tau}.
\end{aligned}}
$$

**c)** Au basculement suivant, $u_2(t_b'^{-})=V_b$. Donc

$$
\boxed{t_b'-t_b=\tau\ln\!\left(\frac{V_a+V_b}{V_b}\right).}
$$

### Question 32

**a)** À $t_b'$, la porte 2 repasse à $u_1=V_a$ et la porte 1 à $u=0$.

La tension du condensateur reste à $u_c(t_b')=V_b-V_a$, donc $u_2$ saute de $V_b$ à $V_b-V_a$, en dessous du seuil.

L’équation redevient $\tau\dot u_c+u_c=V_a$, avec la nouvelle condition initiale. On obtient

$$
\boxed{u_c(t)=u_2(t)=V_a+(V_b-2V_a)e^{-(t-t_b')/\tau}.}
$$

**b)** En imposant $u_2(t_b''^{-})=V_b$,

$$
\boxed{t_b''-t_b'=\tau\ln\!\left(\frac{2V_a-V_b}{V_a-V_b}\right).}
$$

### Question 33

La tension $u$ est en créneaux et $u_c$ est continue.

La tension $u_2=u+u_c$ suit donc la même courbure exponentielle que $u_c$ entre les basculements, mais saute de $+V_a$ ou $-V_a$ à chaque changement d’état de $u$.

Le seuil $V_b$ est atteint juste avant chaque saut de $u_2$.

![Chronogrammes de u, de la tension u_c aux bornes de C et de l’entrée u₂](figures/q33-chronogrammes.svg)

### Question 34

**a)** Dès $t_b$, les deux phases se répètent. La période est la somme de leurs durées.

$$
\boxed{T=RC\ln\!\left(\frac{(V_a+V_b)(2V_a-V_b)}
{V_b(V_a-V_b)}\right).}
$$

**b)** On a $RC=2{,}00\,\mathrm{ms}$, d’où **$T\simeq4{,}71\,\mathrm{ms}$**.

**c)** L’étage 1 génère le signal périodique qui excite le capteur. C’est un **oscillateur de relaxation**, ou multivibrateur astable.

### Question 35

**a)** L’entrée de la porte 3 ne prélève pas de courant dans le modèle. Le courant dans la série $R_h,C_h$ est donc nul. La chute dans $R_h$ est nulle et l’écart de potentiel aux bornes de $C_h$ reste constant. Ainsi **$u_h(t)=u_2(t)+k$**.

**b)** Le signal **B** présente les variations exponentielles et sauts de $u_2$ avec un décalage, donc représente $u_h$. Le signal **C** est la sortie de l’inverseur, donc $u_i$. Le signal **A** varie plus lentement autour d’un niveau, donc représente $u_{rd}$.

**c)** En figure 10a, le niveau A reste sous $3{,}5\,\mathrm V$. En figure 10b, il est d’environ $4\,\mathrm V$, au-dessus du seuil. **L’arrosage a lieu dans le cas 10b, pour $C_h=700\,\mathrm{pF}$.** Puisque l’arrosage correspond au sol le plus sec, **$C_h$ augmente avec l’humidité** dans ce montage.

**d)** En figure 10a, lorsque B dépasse $V_b$, C est bas. Le reste du temps, C est haut. Cela explique les impulsions basses courtes de la sortie. Quand la diode conduit vers cette sortie basse, elle abaisse rapidement A. Quand elle se bloque, le réseau $R_d,C_d$ fait remonter A plus lentement vers $V_a$. En figure 10b, B atteint tout juste le voisinage de $V_b$ et ne le dépasse que très brièvement. C reste donc haut presque tout le temps, avec de brèves chutes sur le graphe. Le filtrage maintient A au-dessus du seuil d’arrosage. Le modèle logique idéal décrit les états hors de ces transitoires, tandis que le graphe montre des chutes qui ne descendent pas jusqu’au niveau bas idéal.

## Partie VI — Bronzage sur les plages de la Côte d’Argent et protection solaire

### Question 36

Avec les volumes finaux assimilés aux volumes d’eau donnés, $M(\mathrm{I_2})=254\,\mathrm{g\,mol^{-1}}$ et $M(\mathrm{Na_2S_2O_3})=158\,\mathrm{g\,mol^{-1}}$. La dissolution libère un ion thiosulfate par unité de sel. On trouve

$$
\boxed{\begin{aligned}
C_i&=\frac{m_i}{M(\mathrm{I_2})V_i^{\mathrm{préparation}}}
\simeq4{,}92\times10^{-2}\,\mathrm{mol\,L^{-1}},\\
C_t&=\frac{m_t}{M(\mathrm{Na_2S_2O_3})V_t^{\mathrm{préparation}}}
\simeq9{,}49\times10^{-2}\,\mathrm{mol\,L^{-1}}.
\end{aligned}}
$$

### Question 37

L’acide ascorbique cède deux électrons pour former $\mathrm{C_6H_6O_6}$ et deux protons. Le diiode accepte ces deux électrons. Avant le dosage, le bilan est donc

$$
\boxed{\mathrm{C_6H_8O_6+I_2\longrightarrow C_6H_6O_6+2I^-+2H^+}.}
$$

Au dosage, deux ions thiosulfate cèdent ensemble deux électrons pour former un ion tétrathionate. D’où

$$
\boxed{\mathrm{I_2+2S_2O_3^{2-}\longrightarrow2I^-+S_4O_6^{2-}}.}
$$

### Question 38

Il y avait initialement $C_iV_i$ moles de diiode dans l’erlenmeyer. La première réaction consomme une mole de diiode par mole d’acide ascorbique. À l’équivalence du dosage en retour, la quantité de diiode restant vaut $C_tV_t/2$. Ainsi

$$
\boxed{n_a=C_iV_i-\frac{C_tV_t}2\simeq5{,}55\times10^{-4}\,\mathrm{mol}.}
$$

### Question 39

Le prélèvement de $20{,}0\,\mathrm{mL}$ représente le cinquième de la solution préparée à partir de $500\,\mathrm{mg}$ de poudre, soit une masse équivalente de $100\,\mathrm{mg}$. La masse molaire de l’acide ascorbique vaut $176\,\mathrm{g\,mol^{-1}}$. La pureté est donc

$$
\boxed{w=\frac{n_a M(\mathrm{C_6H_8O_6})}
{(20{,}0/100)\,m_{\mathrm{poudre}}}
\simeq0{,}978,\quad\text{soit }97{,}8\,\%.}
$$

FIN
