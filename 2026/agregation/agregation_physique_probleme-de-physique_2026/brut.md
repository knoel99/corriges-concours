# Agrégation Physique — Problème de physique 2026 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Problème de physique « Marée thermique atmosphérique » (agrégation externe de physique-chimie, option physique, session 2026) : épreuve de 6 heures, calculatrice autorisée, documents interdits. Soixante-six questions en quatre parties : I. stratification de la troposphère (Q1–Q25) ; II. déformation de l'atmosphère (Q26–Q38) ; III. couple de marée (Q39–Q52) ; IV. évolution de l'amplitude du couple de marée (Q53–Q66). On néglige l'inclinaison de l'axe terrestre : le Soleil reste dans le plan équatorial.

## Partie I — Stratification de la troposphère

### Question 1

L'air sec est composé à ≈ 78 % de $N_2$ ($M=28$), ≈ 21 % de $O_2$ ($M=32$) et ≈ 1 % d'argon ($M=40$) en fractions molaires :

$$
\mathcal M_{\text{air}}\approx 0{,}78\times28+0{,}21\times32+0{,}01\times40 = 28{,}96\ \text{g·mol}^{-1}\approx \boxed{29\ \text{g·mol}^{-1}.}
$$

### Question 2

$P_0 V=\dfrac{m}{\mathcal M_{\text{air}}}RT_0$, soit avec $\rho_0=m/V$ et $R_{\text{air}}=R/\mathcal M_{\text{air}}$ :

$$
\begin{aligned}
\boxed{P_0=\rho_0\,R_{\text{air}}\,T_0},\qquad R_{\text{air}} \\
&= \frac{8{,}314}{0{,}029}\approx \boxed{287\ \text{J·K}^{-1}\text{·kg}^{-1}.}
\end{aligned}
$$

### Question 3

L'air est quasi exclusivement diatomique ($N_2,O_2$). À température ambiante, seuls les degrés de translation (3) et de rotation (2) sont excités, les modes de vibration étant « gelés ». D'où $c_v=\tfrac52 R_{\text{air}}$, $c_p=\tfrac72 R_{\text{air}}$ et

$$
\begin{aligned}
\gamma \\
&= \frac{c_p}{c_v} \\
&= \frac{7}{5} \\
&= \boxed{1{,}4.}
\end{aligned}
$$

### Question 4

Déplacée en $z+\mathrm dz$, la parcelle (densité $\rho'=\rho+\mathrm d\rho$ avec $\rho=\rho_0(z)$) subit son **poids** $\rho' V\vec g$ (vers le bas) et la **poussée d'Archimède** $\rho_0(z+\mathrm dz)V\,(-\vec g)=(\rho_0+\mathrm d\rho_0)V(-\vec g)$ (vers le haut). La résultante verticale (comptée vers le haut) vaut $\big[(\rho_0+\mathrm d\rho_0)-\rho'\big]Vg$. Pour que la force soit **restaurante** (vers le bas lorsqu'on monte), il faut la parcelle plus dense que l'air ambiant :

$$
\rho'>\rho_0+\mathrm d\rho_0\ \Longleftrightarrow\ \boxed{\mathrm d\rho>\mathrm d\rho_0.}
$$

### Question 5

La transformation est **adiabatique réversible** pour un **gaz parfait** : $P\rho^{-\gamma}=\text{cste}$ (car $PV^\gamma=\text{cste}$ et $V\propto 1/\rho$). Donc $\dfrac{P}{\rho^\gamma}=\dfrac{P'}{\rho'^\gamma}$ :

$$
\boxed{\rho'=\rho\left(\frac{P'}{P}\right)^{1/\gamma}.}
$$

### Question 6

$\rho'=\rho\Big(1+\dfrac{\mathrm dP_0}{P_0}\Big)^{1/\gamma}\approx\rho\Big(1+\dfrac{1}{\gamma}\dfrac{\mathrm dP_0}{P_0}\Big)$. Avec $\rho=\rho_0$ :

$$
\boxed{\mathrm d\rho=\rho'-\rho=\frac{\rho_0}{\gamma}\,\frac{\mathrm dP_0}{P_0}.}
$$

### Question 7

De $P_0=\rho_0 R_{\text{air}}T_0$ : $\ln P_0=\ln\rho_0+\ln R_{\text{air}}+\ln T_0$, d'où

$$
\begin{aligned}
\frac{\mathrm dP_0}{P_0} \\
&= \frac{\mathrm d\rho_0}{\rho_0}+\frac{\mathrm dT_0}{T_0}\ \\
&\Longrightarrow \ \boxed{\frac{\mathrm d\rho_0}{\rho_0}=\frac{\mathrm dP_0}{P_0}-\frac{\mathrm dT_0}{T_0}.}
\end{aligned}
$$

### Question 8

$\mathrm d\rho-\mathrm d\rho_0=\dfrac{\rho_0}{\gamma}\dfrac{\mathrm dP_0}{P_0}-\rho_0\Big(\dfrac{\mathrm dP_0}{P_0}-\dfrac{\mathrm dT_0}{T_0}\Big)>0$. En divisant par $\rho_0$ puis en multipliant par $T_0$ :

$$
\Big(\frac1\gamma-1\Big)\frac{T_0}{P_0}\mathrm dP_0+\mathrm dT_0>0.
$$

Avec $\mathrm dP_0=\frac{\mathrm dP_0}{\mathrm dz}\mathrm dz$, $\mathrm dT_0=\frac{\mathrm dT_0}{\mathrm dz}\mathrm dz$ :

$$
\boxed{\left[\Big(\frac1\gamma-1\Big)\frac{T_0}{P_0}\frac{\mathrm dP_0}{\mathrm dz}+\frac{\mathrm dT_0}{\mathrm dz}\right]\mathrm dz>0.}
$$

### Question 9

On prend $\mathrm dz>0$. Comme $\gamma>1$, $\big(\tfrac1\gamma-1\big)=-\tfrac{\gamma-1}{\gamma}<0$. Posons $\frac{\mathrm dP_0}{\mathrm dz}=-\big|\frac{\mathrm dP_0}{\mathrm dz}\big|$ et $\frac{\mathrm dT_0}{\mathrm dz}=-\big|\frac{\mathrm dT_0}{\mathrm dz}\big|$. Le premier terme devient

$$
\Big(\tfrac1\gamma-1\Big)\frac{T_0}{P_0}\frac{\mathrm dP_0}{\mathrm dz}=\frac{\gamma-1}{\gamma}\frac{T_0}{P_0}\Big|\frac{\mathrm dP_0}{\mathrm dz}\Big|>0.
$$

La condition s'écrit $\frac{\gamma-1}{\gamma}\frac{T_0}{P_0}\big|\frac{\mathrm dP_0}{\mathrm dz}\big|-\big|\frac{\mathrm dT_0}{\mathrm dz}\big|>0$, soit

$$
\boxed{\Big|\frac{\mathrm dT_0}{\mathrm dz}\Big|<\frac{\gamma-1}{\gamma}\,\frac{T_0}{P_0}\,\Big|\frac{\mathrm dP_0}{\mathrm dz}\Big|.}
$$

### Question 10

Pour une atmosphère isotherme, $|\mathrm dT_0/\mathrm dz|=0$ est strictement inférieur à la borne (strictement positive) de la question 9. La condition de stabilité est donc satisfaite : **une atmosphère isotherme est stablement stratifiée.**

### I.1 — Atmosphère à stratification neutre

### Question 11

$\big(\tfrac1\gamma-1\big)\dfrac{\mathrm dP_0}{P_0}+\dfrac{\mathrm dT_0}{T_0}=0$, d'où

$$
\begin{aligned}
\frac{\mathrm dT_0}{T_0} \\
&= \Big(1-\frac1\gamma\Big)\frac{\mathrm dP_0}{P_0} \\
&= \kappa\frac{\mathrm dP_0}{P_0},\qquad \boxed{\kappa=\frac{\gamma-1}{\gamma}=\frac{0{,}4}{1{,}4}=0{,}286\approx0{,}29.}
\end{aligned}
$$

### Question 12

L'équilibre hydrostatique donne $\mathrm dP_0=-\rho_0\,g\,\mathrm dz$, soit

$$
\boxed{\mathrm dP_0=-\rho_0\,g\,\mathrm dz.}
$$

### Question 13

$\dfrac{\mathrm dT_0}{\mathrm dz}=\kappa\dfrac{T_0}{P_0}\dfrac{\mathrm dP_0}{\mathrm dz}=\kappa\dfrac{T_0}{P_0}(-\rho_0 g)$. Or $\dfrac{T_0}{P_0}=\dfrac{1}{\rho_0 R_{\text{air}}}$, donc

$$
\begin{aligned}
\mu_{\text{sec}}&=\Big(\frac{\mathrm dT_0}{\mathrm dz}\Big)_{z=0}=-\frac{\kappa g}{R_{\text{air}}}\\
&=-\frac{0{,}286\times9{,}81}{287}\approx-9{,}8\times10^{-3}\ \text{K·m}^{-1}=-9{,}8\ \text{K·km}^{-1}.
\end{aligned}
$$

### Question 14

Sur la figure 2, $T$ passe de $\approx +15\,^\circ$C (sol) à $\approx -57\,^\circ$C vers $11$ km :

$$
\Big(\frac{\mathrm dT_0}{\mathrm dz}\Big)_{\text{ISO}}\approx\frac{-57-15}{11}\approx-6{,}5\ \text{K·km}^{-1}.
$$

La valeur adiabatique sèche ($-9{,}8$ K·km⁻¹) est nettement **plus raide** que le profil observé ($-6{,}5$ K·km⁻¹). L'écart suggère un effet modérateur (libération de chaleur latente par l'humidité).

### I.2 — Air humide

### Question 15

Quand la parcelle s'élève, sa température **diminue** (Q13). La vapeur d'eau atteint la saturation et se **condense** : passage vapeur → liquide (condensation/liquéfaction).

### Question 16

La condensation **libère** de la chaleur latente : elle est **exothermique** pour la parcelle. Ce chauffage interne atténue le refroidissement adiabatique : la présence d'humidité **réduit la valeur absolue** du gradient de température au sol ($|\mu_{\text{sat}}|<|\mu_{\text{sec}}|$).

### Question 17

ÉTAT 1 (basses $T$) : **solide** ; ÉTAT 2 (hautes $P$, $T$ modérées) : **liquide** ; ÉTAT 3 (basses $P$, hautes $T$) : **vapeur (gaz)**. Point **A** : **point triple** (coexistence des trois phases) ; point **B** : **point critique**. Transformations : solide↔liquide = **fusion/solidification** ; liquide↔vapeur = **vaporisation/liquéfaction** ; solide↔vapeur = **sublimation/condensation (solide)**.

### Question 18

La courbe de pression de vapeur saturante est la branche **liquide–vapeur** reliant le point triple A au point critique B. Lecture à $T=15\,^\circ$C : $\boxed{P_{\text{sat}}(15\,^\circ\text{C})\approx 1{,}7\ \text{kPa}.}$

### I.3 — Gradient adiabatique humide

### Question 19

La pression partielle de vapeur à saturation est $P_{\text{sat}}$, celle d'air sec $\approx P$. En moles : $\dfrac{n_{\text{vap}}}{n_{\text{sec}}}=\dfrac{P_{\text{sat}}}{P-P_{\text{sat}}}\approx\dfrac{P_{\text{sat}}}{P}$. En masses :

$$
\begin{aligned}
r_{\text{sat}} \\
&= \frac{m_{\text{vap}}}{m_{\text{sec}}} \\
&= \frac{n_{\text{vap}}\mathcal M_{H_2O}}{n_{\text{sec}}\mathcal M_{\text{air}}} \\
&= \boxed{\frac{\mathcal M_{H_2O}}{\mathcal M_{\text{air}}}\frac{P_{\text{sat}}}{P}},\qquad \frac{\mathcal M_{H_2O}}{\mathcal M_{\text{air}}} \\
&= \frac{18}{29}\approx0{,}62.
\end{aligned}
$$

### Question 20

$r_{\text{sat}}=0{,}62\times\dfrac{1{,}7\times10^{3}}{1{,}01\times10^{5}}\approx\boxed{1{,}0\times10^{-2}.}$ Comme $m_{\text{vap}}/m_{\text{sec}}\approx 0{,}01\ll1$, la masse de vapeur est négligeable : $m_{\text{sec}}\approx m$.

### Question 21

On considère l'air sec comme système recevant la chaleur latente. Son enthalpie massique vérifie, pour un gaz parfait, $\mathrm dh=c_p\,\mathrm dT$. Le premier principe sous forme réversible s'écrit $\mathrm dh=\delta q+v\,\mathrm dP$, avec :
- la chaleur reçue par condensation $\delta q=-\Delta h_v\,\mathrm dr_{\text{sat}}$ ($\mathrm dr_{\text{sat}}<0$ libère de la chaleur, $\delta q>0$) ;
- $v\,\mathrm dP=\dfrac{1}{\rho_0}\mathrm dP_0=-g\,\mathrm dz$ (hydrostatique, Q12), la parcelle restant à l'équilibre de pression.

En égalant : $c_p\,\mathrm dT=-\Delta h_v\,\mathrm dr_{\text{sat}}-g\,\mathrm dz$, soit

$$
\boxed{c_p\,\mathrm dT+\Delta h_v\,\mathrm dr_{\text{sat}}+g\,\mathrm dz=0.}
$$

### Question 22

$\mathrm dr_{\text{sat}}=\big(\tfrac{\partial r_{\text{sat}}}{\partial T}\big)_P\mathrm dT+\big(\tfrac{\partial r_{\text{sat}}}{\partial P}\big)_T\mathrm dP$ avec $\mathrm dP=-\rho_0 g\,\mathrm dz$. En reportant dans Q21 :

$$
\mathrm dT\Big[c_p+\Delta h_v\Big(\tfrac{\partial r_{\text{sat}}}{\partial T}\Big)_P\Big]+\mathrm dz\,g\Big[1-\rho_0\Delta h_v\Big(\tfrac{\partial r_{\text{sat}}}{\partial P}\Big)_T\Big]=0,
$$

d'où

$$
\boxed{\mu_{\text{sat}}=\frac{\mathrm dT_0}{\mathrm dz}\Big|_0=-\frac{g}{c_p}\,\frac{1-\rho_0\Delta h_v\big(\tfrac{\partial r_{\text{sat}}}{\partial P}\big)_T}{1+\tfrac{\Delta h_v}{c_p}\big(\tfrac{\partial r_{\text{sat}}}{\partial T}\big)_P}.}
$$

### Question 23

Si $r_{\text{sat}}$ est constant, $\big(\tfrac{\partial r_{\text{sat}}}{\partial T}\big)_P=\big(\tfrac{\partial r_{\text{sat}}}{\partial P}\big)_T=0$, donc $\mu_{\text{sat}}=-g/c_p$. Or $R_{\text{air}}=c_p-c_v=c_p\kappa$ (puisque $\kappa=\tfrac{\gamma-1}{\gamma}=1-\tfrac{c_v}{c_p}$),
d'où $\mu_{\text{sec}}=-\dfrac{\kappa g}{R_{\text{air}}}=-\dfrac{\kappa g}{c_p\kappa}=-\dfrac{g}{c_p}$. Donc $\boxed{\mu_{\text{sat}}=\mu_{\text{sec}}.}$

**Justification physique** : si $r_{\text{sat}}$ est constant, il n'y a **pas de condensation** (teneur en eau figée), donc pas de chaleur latente libérée : la parcelle se comporte comme de l'air sec.

### Question 24

$\big(\tfrac{\partial r_{\text{sat}}}{\partial P}\big)_T=-\dfrac{r_{\text{sat}}}{P}$ et, avec $\dfrac{\mathrm dP_{\text{sat}}}{\mathrm dT}=P_{\text{sat}}\dfrac{A\,T_{\text{ref}}}{T^2}$, $\big(\tfrac{\partial r_{\text{sat}}}{\partial T}\big)_P=r_{\text{sat}}\dfrac{A\,T_{\text{ref}}}{T^2}$. En reportant dans (7), avec $\rho_0/P=1/(R_{\text{air}}T_0)$ et $-g/c_p=\mu_{\text{sec}}$ :

$$
\boxed{\mu_{\text{sat}}=\mu_{\text{sec}}\,\frac{1+\dfrac{\Delta h_v\,r_{\text{sat}}}{R_{\text{air}}T_0}}{1+\dfrac{\Delta h_v\,r_{\text{sat}}\,A\,T_{\text{ref}}}{c_p\,T_0^{2}}}.}
$$

### Question 25

$\mu_{\text{sat}}=-\dfrac{\kappa_{\text{sat}}\,g}{R_{\text{air}}}=-\dfrac{0{,}16\times9{,}81}{287}\approx\boxed{-5{,}5\ \text{K·km}^{-1}.}$
Comparaison : sec $-9{,}8$ K·km⁻¹, saturé $-5{,}5$ K·km⁻¹, observé (ISO) $-6{,}5$ K·km⁻¹. Le modèle **saturé** ($|\text{écart}|\approx1{,}0$) est plus proche de l'observation que le sec ($|\text{écart}|\approx3{,}3$).

## Partie II — Déformation de l'atmosphère

### II.1 — Décomposition du flux solaire reçu

### Question 26

Sur la face **éclairée**, la surface $\mathrm d\vec S$ fait l'angle $\alpha$ avec la direction du Soleil : le flux reçu par unité de surface terrestre est $F_S\cos\alpha$. Sur la face dans l'**ombre**, aucun flux :

$$
\boxed{F(\alpha)=\begin{cases}F_S\cos\alpha & |\alpha|\le\pi/2\\[2pt] 0 & \pi/2<|\alpha|\le\pi.\end{cases}}
$$

### Question 27

*Schéma attendu : arche $F_S\cos\alpha$ (maximum $F_S$ en $\alpha=0$) entre $-\pi/2$ et $\pi/2$,
nulle ailleurs ; **points anguleux** en $\alpha=\pm\pi/2$ où la courbe rejoint $0$.*

### Question 28

$F(-\alpha)=F(\alpha)$ : $F$ est **paire** (le flux ne dépend que de $|\alpha|$, et $\cos$ est pair). Le développement d'une fonction paire ne contient que des cosinus : les coefficients de $\sin(n\alpha)$ sont nuls.

### Question 29

$\hat F_n=\dfrac1\pi\displaystyle\int_{-\pi}^{\pi}F\cos(n\alpha)\mathrm d\alpha=\dfrac2\pi\int_0^\pi F\cos(n\alpha)\mathrm d\alpha$ (intégrande pair). Comme $F=0$ pour $\alpha>\pi/2$ :

$$
\boxed{\hat F_n=\frac{2F_S}{\pi}\int_0^{\pi/2}\cos\alpha\,\cos(n\alpha)\,\mathrm d\alpha.}
$$

### Question 30

$\hat F_1=\dfrac{2F_S}{\pi}\displaystyle\int_0^{\pi/2}\cos^2\alpha\,\mathrm d\alpha=\dfrac{2F_S}{\pi}\cdot\dfrac\pi4=\boxed{\dfrac{F_S}{2}.}$

### Question 31

$\cos\alpha\cos(n\alpha)=\tfrac12[\cos((n{+}1)\alpha)+\cos((n{-}1)\alpha)]$, et $\int_0^{\pi/2}\cos(m\alpha)\mathrm d\alpha=\dfrac{\sin(m\pi/2)}{m}$. D'où pour $n\ge2$ :

$$
\hat F_n=\frac{F_S}{\pi}\left[\frac{\sin\frac{(n+1)\pi}{2}}{n+1}+\frac{\sin\frac{(n-1)\pi}{2}}{n-1}\right].
$$

Pour $n=2p+1$ impair : $n\pm1$ pairs, $\sin(k\pi)=0\Rightarrow \hat F_{2p+1}=0$. Pour $n=2p$ : $\sin\frac{(2p+1)\pi}{2}=(-1)^p$, $\sin\frac{(2p-1)\pi}{2}=(-1)^{p+1}$, d'où

$$
\begin{aligned}
\hat F_{2p} \\
&= \frac{F_S}{\pi}(-1)^p\Big[\frac1{2p+1}-\frac1{2p-1}\Big] \\
&= \frac{F_S}{\pi}(-1)^p\frac{-2}{4p^2-1} \\
&= \boxed{\frac{(-1)^{p+1}}{4p^2-1}\frac{2}{\pi}F_S.}
\end{aligned}
$$

### Question 32

Les harmoniques impaires ($n\ge3$) sont **nulles** ($\hat F_{2p+1}=0$). Les harmoniques paires décroissent comme $\dfrac{1}{4p^2-1}\sim \dfrac1{p^2}$ : $\hat F_4=\dfrac{2F_S}{15\pi}\approx0{,}04\,F_S$, négligeable devant $\hat F_1=F_S/2$. Seuls les termes $n=0,1,2$ sont significatifs.

### Question 33

$\hat F_2=\dfrac{2F_S}{3\pi}$ ($p=1$), $\hat F_1=\dfrac{F_S}{2}$ :

$$
\boxed{\frac{\hat F_2}{\hat F_1}=\frac{2/(3\pi)}{1/2}=\frac{4}{3\pi}\approx0{,}42.}
$$

### Question 34

Le **forçage** diurne domine le forçage semi-diurne ($\hat F_2/\hat F_1\approx0{,}42<1$). Pourtant, sur la figure 5, la **réponse** en pression semi-diurne (12 h) est d'amplitude supérieure ou égale à la réponse diurne (24 h). La composante semi-diurne est donc **bien plus amplifiée** que la diurne : l'atmosphère, oscillateur forcé, a sa **période propre proche de 12 h** (résonance au voisinage de la période semi-diurne).

### II.2 — Redistribution de masse

### Question 35

$\mathrm dP=-\rho g\,\mathrm dz\Rightarrow \rho\,\mathrm dz=-\mathrm dP/g$. En intégrant de $z=0$ ($P=P_s$) à $z\to\infty$ ($P\to0$) :

$$
\begin{aligned}
\Sigma(t) \\
&= \int_0^\infty\rho\,\mathrm dz \\
&= \int_{P_s}^{0}\Big(-\frac{\mathrm dP}{g}\Big) \\
&= \boxed{\frac{P_s(t)}{g}.}
\end{aligned}
$$

### Question 36

Par Q35, $\Sigma=P_s/g$ : les variations ont les mêmes phases que celles de la pression. La figure 5 donne une amplitude diurne d'environ $0,3$ mbar et semi-diurne d'environ $1,0$ mbar, d'où
$$\hat\Sigma_1\simeq3\ \mathrm{kg\,m^{-2}},\qquad \hat\Sigma_2\simeq10\ \mathrm{kg\,m^{-2}}.$$
Le maximum de la composante diurne se situe vers $\alpha_1\simeq-100°$ (lecture à une dizaine de degrés près). Les maxima semi-diurnes sont vers $-30°$ et $150°$, avec un minimum vers $60°$ :
$$\boxed{\alpha_2\simeq-30°\pmod{180°}.}$$
Ces valeurs sont des lectures graphiques, non des mesures exactes.

### Question 37

Représentation : Terre vue du pôle Nord, Soleil selon $\alpha=0$, rotation dans le sens trigonométrique ; deux excès de masse diamétralement opposés aux angles $\alpha_2\simeq-30°$ et $\alpha_2+180°\simeq150°$.

Le couple gravitationnel solaire tend à aligner l'axe de ces deux renflements sur la direction Soleil–Terre. Au voisinage de $\alpha_2=-30°$, il fait croître cet angle vers zéro, donc agit dans le sens de rotation. **La marée thermique atmosphérique accélère la rotation terrestre.**

### Question 38

$\hat\Sigma_2/\hat\Sigma_1\approx10/3\approx3{,}3$. Par ailleurs

$$
\frac{m_T}{R_T^2}=\frac{5{,}972\times10^{24}}{(6{,}371\times10^{6})^2}\approx1{,}5\times10^{11}\ \text{kg·m}^{-2}\gg\hat\Sigma_2\approx10\ \text{kg·m}^{-2}.
$$

Donc $\hat\Sigma_2\approx3{,}3\,\hat\Sigma_1\ll m_T/R_T^2$.

**$\hat\Sigma_2\approx3{,}3\,\hat\Sigma_1\ll m_T/R_T^2\approx1{,}5\times10^{11}$ kg·m$^{-2}$.**

## Partie III — Couple de marée

### III.1 — Développement multipolaire

### Question 39

$\mathrm dU=-\dfrac{\mathcal G m_S\,\mathrm dm}{|\vec r_S-\vec r_M|}$, d'où

$$
\boxed{U=-\mathcal G m_S\int_{m_T}\frac{\mathrm dm}{|\vec r_S-\vec r_M|}.}
$$

### Question 40

$\dfrac1{|\vec r_S-\vec r_M|}=\dfrac1{r_S}\Big[1-\dfrac{2\vec r_M\cdot\vec r_S}{r_S^2}+\dfrac{r_M^2}{r_S^2}\Big]^{-1/2}$. Avec $(1+u)^{-1/2}\approx1-\tfrac u2+\tfrac{3}{8}u^2$ :

$$
\frac1{|\vec r_S-\vec r_M|}=\frac1{r_S}\Big[1+\frac{\vec r_M\cdot\vec r_S}{r_S^2}+\frac12\Big(3\big(\tfrac{\vec r_M\cdot\vec r_S}{r_S^2}\big)^2-\frac{r_M^2}{r_S^2}\Big)\Big].
$$

En reportant dans $U$ on obtient $U\approx U_0+U_1+U_2$ avec les expressions (11).

**Développement limité à l'ordre 2 en $r_M/r_S$ : $U\approx U_0+U_1+U_2$ (expressions (11)).**

### Question 41

$U_0=-\dfrac{\mathcal G m_S}{r_S}\displaystyle\int\mathrm dm=\boxed{-\dfrac{\mathcal G m_S m_T}{r_S}}$ : interaction de **deux masses ponctuelles** $m_S$ et $m_T$ (toute la masse concentrée au centre $G$).
$U_1=-\dfrac{\mathcal G m_S}{r_S^3}\vec r_S\cdot\displaystyle\int\vec r_M\,\mathrm dm$. Or $\int\vec r_M\,\mathrm dm=m_T\,\overrightarrow{GG}=\vec0$ car l'origine est le **barycentre**. Donc $\boxed{U_1=0}$ : le terme dipolaire est nul par choix du centre de masse.

### Question 42

Pour une distribution sphérique, tous les moments d'inertie par rapport à un axe passant par le centre sont égaux : $I_\parallel=I_\perp$. La formule de MacCullagh donne $U_2=\dfrac{\mathcal G m_S(I_\parallel-I_\perp)}{2r_S^3}(3\cos^2\beta-1)=0$. Un corps sphérique n'a pas de moment quadrupolaire.

**Pour une distribution sphérique, $U_2=0$ : pas de moment quadrupolaire.**

### Question 43

Pour une rotation d'angle $\mathrm d\beta$ autour de $\vec u_Z$, le travail du couple $\Gamma_{\text{atm}}$ (porté par $\vec u_Z$) est

$$
\boxed{\delta W=\Gamma_{\text{atm}}\,\mathrm d\beta.}
$$

### Question 44

L'interaction étant conservative, $\delta W=-\mathrm dU$, donc $\Gamma_{\text{atm}}=-\dfrac{\mathrm dU}{\mathrm d\beta}$. Pour $U=U_2$ :

$$
\begin{aligned}
\frac{\mathrm dU_2}{\mathrm d\beta} \\
&= \frac{\mathcal G m_S(I_\parallel-I_\perp)}{2r_S^3}\cdot(-3\sin2\beta)\ \\
&\Rightarrow \ \boxed{\Gamma_{\text{atm}}=\frac{3\mathcal G m_S(I_\parallel-I_\perp)}{2r_S^3}\sin2\beta.}
\end{aligned}
$$

### III.2 — Terme dipolaire

### Question 45

Masse totale inchangée ($+\delta m_1-\delta m_1=0$). Le barycentre de la sphère est $O$ ; les anomalies en $(\pm R_T,0,0)$ donnent

$$
\vec r_G=\frac{\delta m_1(R_T,0,0)+(-\delta m_1)(-R_T,0,0)}{m_T}=\boxed{\frac{2\delta m_1 R_T}{m_T}\,\vec u_X.}
$$

### Question 46

a) $I_\parallel$ (axe $\vec u_X$) : les anomalies, situées **sur** l'axe $\vec u_X$, sont à distance nulle de cet axe. Donc $\boxed{I_\parallel=I_0.}$

b) $I'_\perp$ (axe $\perp\vec u_X$ passant par $O$) : les anomalies sont à distance $R_T$ de cet axe ; $+\delta m_1$
apporte $+\delta m_1 R_T^2$, $-\delta m_1$ apporte $-\delta m_1 R_T^2$ : $\boxed{I'_\perp=I_0.}$

c) $I_\perp$ (axe $\perp\vec u_X$ passant par $G$) : Huygens $I'_\perp=I_\perp+m_T d^2$ avec $d=|OG|=\dfrac{2\delta m_1 R_T}{m_T}$ :

$$
\boxed{I_\perp=I_0-\frac{4\delta m_1^2 R_T^2}{m_T}.}
$$

### III.3 — Terme quadrupolaire

### Question 47

Les deux anomalies $+\delta m_2$ en $(\pm R_T,0,0)$ se compensent en position, l'anneau $-2\delta m_2$ est centré en $O$, masse totale ajoutée $=\delta m_2+\delta m_2-2\delta m_2=0$. Donc $\boxed{G=O.}$

### Question 48

a) $I_\parallel$ (axe $\vec u_X$) : les masses $+\delta m_2$ sont sur l'axe (contribution nulle) ; l'anneau (plan $\perp\vec u_X$, rayon $R_T$)
a toute sa masse à $R_T$ de l'axe : contribution $-2\delta m_2 R_T^2$. $\boxed{I_\parallel=I_0-2\delta m_2 R_T^2.}$ L'anneau (masse négative) **abaisse** $I_\parallel$.

b) Moment d'un cercle de masse $\delta m$, rayon $R$, par rapport à un diamètre : moment par rapport à l'axe $\perp$ (centre) $=\delta m R^2$ ; par le théorème des axes perpendiculaires $\delta m R^2=I_{\text{diam},1}+I_{\text{diam},2}=2I_{\text{diam}}$, donc $\boxed{I_{\text{diam}}=\tfrac12\delta m R^2.}$

c) $I_\perp$ (axe $\vec u_Y$ par $G=O$) : sphère $I_0$ ; les deux $+\delta m_2$
à distance $R_T$ : $+2\delta m_2 R_T^2$ ; anneau par rapport à un de ses diamètres : $\tfrac12(-2\delta m_2)R_T^2=-\delta m_2 R_T^2$. D'où

$$
\begin{aligned}
I_\perp&=I_0+\delta m_2 R_T^2,\\
I_\parallel-I_\perp&=-3\delta m_2 R_T^2.
\end{aligned}
$$

### III.4 — Amplitude du couple

### Question 49

Dipôle : $(I_\parallel-I_\perp)_{\text{dip}}=\dfrac{4\delta m_1^2 R_T^2}{m_T}$ (ordre 2 en $\delta m_1$). Quadrupôle : $(I_\parallel-I_\perp)_{\text{quad}}=-3\delta m_2 R_T^2$ (ordre 1). Avec $\delta m_{1,2}\sim\hat\Sigma_{1,2}R_T^2$ :

$$
\frac{|(I_\parallel-I_\perp)_{\text{dip}}|}{|(I_\parallel-I_\perp)_{\text{quad}}|}\sim\frac{\hat\Sigma_1^2 R_T^6/m_T}{\hat\Sigma_2 R_T^4}=\frac{\hat\Sigma_1}{\hat\Sigma_2}\cdot\frac{\hat\Sigma_1 R_T^2}{m_T}\ll1
$$

car $\hat\Sigma_1 R_T^2/m_T\ll1$ (Q38). La contribution dipolaire à $U_2$ est **négligeable**. On garde donc la seule redistribution quadrupolaire avec $\beta=\alpha_2$.

### Question 50

Avec $\delta m_2=\tfrac{16\pi}{45}\hat\Sigma_2 R_T^2$ :

$$
\boxed{U_2=-\frac{8\pi}{15}\frac{\mathcal G m_S\hat\Sigma_2 R_T^4}{r_S^3}\big(3\cos^2\beta-1\big),}
$$

et (Q44)

$$
\begin{aligned}
\Gamma_{\text{atm}}&=-\frac{8\pi}{5}\frac{\mathcal G m_S\hat\Sigma_2 R_T^4}{r_S^3}\sin2\beta,\\
&\qquad\beta=\alpha_2.
\end{aligned}
$$

### Question 51

D'après Q50,
$$\Gamma_{\mathrm{atm}}=-\frac{8\pi}{5}\frac{\mathcal Gm_S\hat\Sigma_2R_T^4}{r_S^3}\sin(2\alpha_2).$$
Avec $\hat\Sigma_2\simeq10\ \mathrm{kg\,m^{-2}}$, $\alpha_2\simeq-30°$, $\mathcal Gm_S\simeq1,33\times10^{20}\ \mathrm{m^3s^{-2}}$, $R_T\simeq6,371\times10^6$ m et $r_S\simeq1,50\times10^{11}$ m,
$$K=\frac{\mathcal Gm_S\hat\Sigma_2R_T^4}{r_S^3}\simeq6,5\times10^{14}\ \mathrm{N\,m},$$
$$\boxed{\Gamma_{\mathrm{atm}}\simeq+2,8\times10^{15}\ \mathrm{N\,m}.}$$
Le signe positif confirme l'accélération de la rotation. Ce couple vaut environ $6\%$ du module du couple océanique actuel $-4,5\times10^{16}$ N m : le bilan actuel reste freinant.

### Question 52

Le couple océanique supposé au Précambrien est
$$\Gamma'_{\mathrm{océan}}=\frac{-4,5\times10^{16}}4=-1,125\times10^{16}\ \mathrm{N\,m}.$$
Son annulation nécessite donc un couple atmosphérique positif de même module. Avec l'estimation Q51,
$$\boxed{\eta_{\mathrm{nécessaire}}=\frac{1,125\times10^{16}}{2,8\times10^{15}}\simeq4.}$$
L'incertitude de lecture de la phase et des amplitudes limite la précision de cette estimation.

## Partie IV — Évolution de l'amplitude du couple de marée

### Question 53

Le forçage est maximal pour $t=0$, $\varphi=0$. La réponse
$$\delta P=A\delta F_2\cos(\omega t+2\varphi+\psi)$$
est maximale à $t=0$ lorsque $2\varphi_0+\psi=0$ modulo $2\pi$. Ainsi
$$\boxed{\varphi_0=-\psi/2\pmod{180°}.}$$
La correspondance $\varphi_0=\alpha_2\simeq-30°$ donne
$$\boxed{\psi_0\simeq+60°.}$$

### Question 54

Posons $X=\omega/\omega_L$.
- $\mathcal T_1(\omega)=-\dfrac{A_0}{\varepsilon+iX}$ : **filtre passe-bas du premier ordre** (gain statique $-A_0/\varepsilon$, avec **inversion de signe**), de pulsation de coupure $\omega_c=\varepsilon\omega_L=\omega_R$.
- $\mathcal T_2(\omega)=\dfrac{A_0}{\varepsilon\kappa+i(X-1/X)}$ : **filtre passe-bande du second ordre**, résonant en $\omega_L$ ; gain maximal $A_0/(\varepsilon\kappa)$ à la résonance ; **facteur de qualité** $Q=1/(\varepsilon\kappa)$.

### Question 55

*Schéma attendu : $\mathcal T_1$ (passe-bas) : gain $20\log(A_0/\varepsilon)$ plat jusqu'à $\omega_R=\varepsilon\omega_L$, puis pente $-20$ dB/décade ; **phase** décalée de $180^\circ$
(gain négatif) : $\psi_1=180^\circ-\arctan(X/\varepsilon)$, de $180^\circ$ (BF) à $90^\circ$ (HF), passant par $135^\circ$ en $\omega_R$.*
*Schéma attendu : $\mathcal T_2$ (passe-bande) : gain maximal $20\log(A_0/\varepsilon\kappa)$ en $\omega_L$, pentes $+20$ et $-20$
dB/décade de part et d'autre ; **phase** de $+90^\circ$ (BF) à $-90^\circ$ (HF), nulle à la résonance $\omega_L$ ; transition d'autant plus raide que $Q=1/\varepsilon\kappa$ est grand.*

### Question 56

$\mathcal T_1=-\dfrac{A_0(\varepsilon-iX)}{\varepsilon^2+X^2}\Rightarrow \text{Im}\,\mathcal T_1=\dfrac{A_0 X}{\varepsilon^2+X^2}$. $\mathcal T_2=\dfrac{A_0(\varepsilon\kappa-i(X-1/X))}{(\varepsilon\kappa)^2+(X-1/X)^2}\Rightarrow \text{Im}\,\mathcal T_2=-\dfrac{A_0(X-1/X)}{(\varepsilon\kappa)^2+(X-1/X)^2}$. D'où

$$
\boxed{\text{Im}\,\mathcal T=\frac{A_0\,\omega/\omega_L}{\varepsilon^2+(\omega/\omega_L)^2}-\frac{A_0\big(\omega/\omega_L-\omega_L/\omega\big)}{(\varepsilon\kappa)^2+\big(\omega/\omega_L-\omega_L/\omega\big)^2}.}
$$

### Question 57

$\text{Im}\,\mathcal T_1=\dfrac{A_0 X}{\varepsilon^2+X^2}$ : extremum pour $X=\varepsilon$, valeur $\boxed{\dfrac{A_0}{2\varepsilon}}$ en $\omega=\varepsilon\omega_L=\omega_R$ (maximum).
$\text{Im}\,\mathcal T_2=-\dfrac{A_0 Y}{(\varepsilon\kappa)^2+Y^2}$ ($Y=X-1/X$) : extrema pour $Y=\pm\varepsilon\kappa$, valeurs $\mp\dfrac{A_0}{2\varepsilon\kappa}$. Près de $\omega_L$,
$X=1+u\Rightarrow Y\approx2u$, donc $u=\pm\varepsilon\kappa/2$ :

$$
\begin{aligned}
\text{Im}\,\mathcal T_2^{\max}&=+\frac{A_0}{2\varepsilon\kappa}\ \text{en}\ \omega\approx\omega_L\big(1-\tfrac{\varepsilon\kappa}{2}\big),\\
\text{Im}\,\mathcal T_2^{\min}&=-\frac{A_0}{2\varepsilon\kappa}\ \text{en}\ \omega\approx\omega_L\big(1+\tfrac{\varepsilon\kappa}{2}\big).
\end{aligned}
$$

### Question 58

Le couple est proportionnel à $\operatorname{Im}\mathcal T$, somme des deux termes de Q56. Le tracé comporte un pic positif large vers $\omega_R$, puis, près de $\omega_L$, une contribution dispersive plus étroite : maximum positif juste au-dessous de $\omega_L$, minimum négatif juste au-dessus.

À la pulsation propre, le deuxième terme s'annule, mais le premier subsiste :
$$\operatorname{Im}\mathcal T(\omega_L)=\frac{A_0}{1+\varepsilon^2}>0.$$
Le graphe complet ne passe donc pas exactement par zéro en $\omega_L$. Il s'en approche si l'on néglige le premier filtre devant l'amplitude de la contribution résonante. **L'annulation exacte en $\omega_L$ ne vaudra qu'après l'approximation introduite après Q60.**

### Question 59

$\omega_0=\dfrac{2\pi}{12\ \text{h}}=\dfrac{2\pi}{43200}=1{,}45\times10^{-4}\ \text{rad·s}^{-1}$, donc

$$
\boxed{X_0=\frac{1{,}45\times10^{-4}}{1{,}51\times10^{-4}}\approx0{,}96.}
$$

### Question 60

Le rapport exact des modules est
$$\left|\frac{\mathcal T_1}{\mathcal T_2}\right|=\frac{\sqrt{(\varepsilon\kappa)^2+(X-1/X)^2}}{\sqrt{\varepsilon^2+X^2}},\qquad X=\frac\omega{\omega_L}.$$
Près de la résonance, $|X-1/X|\ll1$ et $\varepsilon\kappa\ll1$, tandis que le dénominateur est d'ordre un : $\mathcal T_1$ est donc petit devant $\mathcal T_2$.

À la pulsation actuelle $X_0\simeq0,963$ et avec $\varepsilon\kappa\simeq0,043$ déterminé en Q62, ce rapport est de l'ordre de $0,09$. Négliger $\mathcal T_1$ constitue une approximation à environ dix pour cent sur le module de la réponse dans ces conditions ; ce rapport n'est pas égal à $\varepsilon\kappa$, expression valable exactement en $X=1$ si $\varepsilon\ll1$.

### Question 61

À $\omega=\omega_L$, $X=1$ et $X-1/X=0$, donc $\text{Im}\,\mathcal T_2=0$. Par conséquent

$$
\boxed{\Gamma_{\text{atm}}(\omega_L)=0.}
$$

Le **gain** $|\mathcal T_2|$ est maximal en $\omega_L$, mais c'est la **partie imaginaire** — qui fixe le couple — qui s'y annule ; le couple est extrémal légèrement **hors** résonance.

### Question 62

Pour $\mathcal T\simeq\mathcal T_2$ et $\varepsilon\kappa>0$,
$$\psi_0=-\arctan\!\left(\frac{X_0-1/X_0}{\varepsilon\kappa}\right).$$
On en déduit
$$\boxed{\varepsilon=\frac{X_0-1/X_0}{\kappa\tan(-\psi_0)}.}$$
Avec $X_0=2\pi/(43200\times1,51\times10^{-4})\simeq0,963$, $\kappa=0,16$ et $\psi_0\simeq60°$,
$$\varepsilon\kappa\simeq\frac{-0,075}{-\sqrt3}\simeq0,043,$$
$$\boxed{\varepsilon\simeq0,27.}$$
La valeur est inférieure à un mais pas extrêmement petite. Les résultats utilisant un développement limité en $\varepsilon\kappa\simeq0,043$ restent mieux contrôlés que ceux qui supposeraient sans vérification $\varepsilon$ négligeable.

### Question 63

L'équilibre impose $\Gamma_{\text{atm}}(\omega)=|\Gamma_{\text{océan}}|>0$ : la droite horizontale coupe le **pic positif** de $\Gamma_{\text{atm}}$ en deux points (branche montante et branche descendante). La dynamique $I\,\dot\omega=\Gamma_{\text{atm}}(\omega)+\Gamma_{\text{océan}}$ est **stable** si une perturbation $\delta\omega>0$ génère un couple restaurant ($<0$),
c'est-à-dire $\mathrm d\Gamma_{\text{atm}}/\mathrm d\omega<0$. Le point d'équilibre **stable** est donc celui situé sur la **branche descendante** du pic positif, entre $\omega_L(1-\varepsilon\kappa/2)$ et $\omega_L$.

### Question 64

Le maximum positif du terme résonant est situé vers
$$X_{\max}\simeq1-\frac{\varepsilon\kappa}{2}\simeq0,978.$$
La valeur actuelle $X_0\simeq0,963$ est inférieure à $X_{\max}$ : le point actuel est sur la **branche montante positive**. Il n'est pas un point d'équilibre stable avec un couple océanique constant, lequel requiert une pente atmosphérique négative.

### Question 65

Dans l'approximation $\mathcal T\simeq\mathcal T_2$, le maximum vaut $A_0/(2\varepsilon\kappa)$, tandis que la valeur actuelle est
$$\operatorname{Im}\mathcal T_2(X_0)=\frac{A_0(1/X_0-X_0)}{(\varepsilon\kappa)^2+(X_0-1/X_0)^2}.$$
Le facteur d'amplification est donc
$$\boxed{\eta=\frac{(\varepsilon\kappa)^2+(X_0-1/X_0)^2}{2\varepsilon\kappa(1/X_0-X_0)}.}$$
Avec $\varepsilon\kappa\simeq0,043$ et $1/X_0-X_0\simeq0,075$, on obtient
$$\boxed{\eta\simeq1,15.}$$
Contrôle : la relation de phase donne $1/X_0-X_0=(\varepsilon\kappa)\tan\psi_0$ ; l'expression se réduit à $\eta=1/\sin(2\psi_0)$, soit $2/\sqrt3$ pour $\psi_0=60°$.

### Question 66

Dans les hypothèses du modèle, il faudrait amplifier le couple atmosphérique actuel d'un facteur voisin de $4$ pour équilibrer la marée océanique précambrienne supposée. Le maximum résonant accessible ne fournit qu'un facteur d'environ $1,15$ :
$$\eta_{\max}\simeq1,15<\eta_{\mathrm{nécessaire}}\simeq4.$$
**Le blocage n'est donc pas possible avec ces paramètres et ces hypothèses.** Cette conclusion concerne le modèle de l'énoncé ; elle n'est pas une exclusion générale de tous les scénarios géophysiques précambriens.

