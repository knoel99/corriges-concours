# CAPES Physique — Épreuve disciplinaire appliquée (bac+5) 2026 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Épreuve écrite disciplinaire appliquée du CAPES externe et du CAFEP (section physique-chimie), session 2026 : 5 heures, calculatrice autorisée, tout ouvrage et tout matériel électronique interdits. Dossier en trois parties et 67 questions : partie 1 « La vitesse en physique-chimie » (Q1–Q32), partie 2 « L'électricité : histoire, concepts et modèles » (Q33–Q50), partie 3 « La pile, siège d'une évolution spontanée » (Q51–Q67).

**Signalement d'énoncé.** À la question 15, la formule imprimée correspond au cas d'une source en mouvement vers un observateur immobile, alors que la situation décrite est l'inverse (observateur en mouvement vers une source immobile) ; le rapport du jury 2026 le confirme. La démonstration publiée ci-dessous établit la formule correcte pour la situation de l'énoncé.

## Partie 1 — La vitesse en physique-chimie

### Q1. Identification du graphique

Le **graphique C** convient. La **courbe en trait plein** (droite passant par l'origine, pente constante) décrit le **cycliste** à vitesse constante. La **courbe en pointillés** (parabole partant de l'origine avec une tangente horizontale, donc vitesse initiale nulle) décrit la **voiture** qui accélère depuis l'arrêt : elle croise la droite peu avant $t = 5$ s et atteint 100 m légèrement avant le cycliste, qui perd donc de peu.

### Q2. Deux coups de pouce

1. « Trace à la main l'allure de la courbe position–temps d'un objet qui avance à **vitesse constante** : quelle forme obtiens-tu ? »
2. « La voiture **part de l'arrêt** : quelle doit être la pente (donc la vitesse) de sa courbe au départ ? Repère ensuite le graphique où la courbe en pointillés rattrape la droite **juste avant la fin**. »

### Q3. Deux plus-values du tableur

1. Le tableur **automatise les calculs répétitifs** (vitesses successives, conversions) sur un grand nombre de points, sans erreur de calcul.
2. Il permet de **tracer et modifier instantanément les représentations graphiques** ($d(t)$, $v(t)$), facilitant l'analyse et la comparaison.

### Q4. Deux points du programme de cycle 4

L'analyse des graphiques $d(t)$ et $v(t)$ d'Usain Bolt permet d'aborder :
- « Caractériser le mouvement d'un objet » : **mouvement dont la vitesse varie au cours du temps** (phase d'accélération puis phase quasi uniforme) ;
- « Utiliser la relation liant vitesse, distance et durée dans le cas d'un mouvement uniforme » (sur la phase finale à vitesse quasi constante), avec **vitesse : direction, sens et valeur**.

### Q5. Trois questions (doc 1-C.2, cycle 4)

1. « Décrire le mouvement de Felix Baumgartner pendant les 30 premières secondes (nature et évolution de la vitesse). » *(mouvement rectiligne dont la vitesse varie)*
2. « Calculer la valeur de la vitesse moyenne entre $t=0$ et $t=40$ s, puis la **convertir en km·h⁻¹**. » *(relation vitesse–distance–durée, conversions)*
3. « Identifier la phase pendant laquelle le mouvement est quasiment **uniforme** et justifier à l'aide du tableau de valeurs. »

### Q6. Correction de la copie DR-1

- *Ex. 1, Q2.* « circulaire constant » → écrire **« circulaire uniforme »** ; « la balle est verticale et accéléré » → **« mouvement rectiligne (vertical) et accéléré »** (une trajectoire est rectiligne, pas « verticale et accéléré »).
- *Ex. 2, Q2.* « linéaire et ralenti » → **« rectiligne et ralenti (décéléré) »** (« linéaire » n'est pas le terme adapté).
- *Ex. 2, Q3.* Erreur : la **durée** de la section F est $\Delta t = 7{,}55 - 3{,}95 = 3{,}6$ s, et non 7,55 s (l'élève a lu l'instant de passage, pas la durée).
- *Ex. 2, Q4.* Conséquence : $v = \dfrac{d}{\Delta t} = \dfrac{5}{3{,}6} = 1{,}4\ \text{m·s}^{-1} = 5{,}0\ \text{km·h}^{-1}$ (et non $5/7{,}55$).

*Commentaire formatif à l'élève* : « Attention à bien distinguer un **instant** d'une **durée** : la durée d'une section se calcule par différence des instants de passage. »

### Q7. Vecteurs déplacement et vitesse

Avec les positions repérées sur l'axe $(O,\vec{i})$ :
- Vecteur déplacement (seconde) : $\overrightarrow{M_0M_2} = (x_2 - x_0)\,\vec{i}$.
- Vecteur vitesse moyenne entre $M_0$ et $M_2$ (seconde) : $\vec{v}_{\text{moy}} = \dfrac{\overrightarrow{M_0M_2}}{2\,\Delta t} = \dfrac{x_2 - x_0}{2\,\Delta t}\,\vec{i}$.
- Vecteur vitesse en $M_2$ (terminale) : $\vec{v}(M_2) = \left.\dfrac{\mathrm{d}\overrightarrow{OM}}{\mathrm{d}t}\right|_{M_2} \approx \dfrac{\overrightarrow{M_1M_3}}{2\,\Delta t} = \dfrac{x_3 - x_1}{2\,\Delta t}\,\vec{i}$.

### Q8. Lignes de code (annexe 1-D)

- Ligne 6 : `vx = (x[i+1] - x[i]) / dt`
- Ligne 14 : `dt = 0.3`

### Q9. Valeur affichée $v_1$

Pour $i=1$ : $v_x = \dfrac{x_2 - x_1}{\Delta t} = \dfrac{6{,}3 - 3{,}1}{0{,}3} = 10{,}67\ \text{m·s}^{-1}$, arrondi à $10{,}7$. Le programme affiche :
> `Au point M1, la vitesse vaut 10.7 m/s`

### Q10. Vitesse trop grande pour Galilée

La lumière parcourt l'aller-retour $2d = 2\times 1800 = 3{,}6\times10^{3}$ m. Avec $c \approx 3{,}0\times10^{8}\ \text{m·s}^{-1}$ :

$$
\begin{aligned}
\Delta t \\
&= \frac{2d}{c} \\
&= \frac{3{,}6\times10^{3}}{3{,}0\times10^{8}} \\
&= 1{,}2\times10^{-5}\ \text{s} \\
&= 12\ \mu\text{s}.
\end{aligned}
$$

Cette durée est **totalement négligeable** devant le temps de réaction humain ($\sim 0{,}1$–$0{,}2$ s) et la résolution d'une clepsydre : Galilée ne pouvait mesurer qu'un temps dominé par les réactions des deux opérateurs, d'où l'impossibilité de mesurer $c$.

### Q11. Vitesse / célérité

La **vitesse** désigne le déplacement d'un objet matériel (transport de matière) ; la **célérité** désigne la **vitesse de propagation d'une onde** (perturbation qui se propage **sans transport de matière**). On parle ainsi de la *célérité* de la lumière ou du son, et de la *vitesse* d'un coureur.

### Q12. Lois de Kepler et contradiction

Pour un astre en orbite autour d'un corps attracteur :
1. **Loi des orbites** : la trajectoire est une **ellipse** dont le corps attracteur occupe un foyer.
2. **Loi des aires** : le rayon vecteur balaie des aires égales pendant des durées égales.
3. **Loi des périodes** : $\dfrac{T^2}{a^3} = \text{constante}$ ($a$ = demi-grand axe).

Les lois de Kepler (ici appliquées à Io autour de Jupiter) impliquent une période **constante**. Or Römer observe une **variation apparente** de la période de Io selon la position de la Terre : c'est en **contradiction avec la loi des périodes** (3ᵉ loi). La résolution est que ce n'est pas la période réelle qui change, mais la durée de trajet de la lumière.

### Q13. Première valeur de $c$ (Huygens)

$EH = 2\times 1{,}5\times10^{8}\ \text{km} = 3{,}0\times10^{11}\ \text{m}$ ; $\Delta t = 22\ \text{min} = 1{,}32\times10^{3}\ \text{s}$.

$$
\begin{aligned}
c \\
&= \frac{EH}{\Delta t} \\
&= \frac{3{,}0\times10^{11}}{1{,}32\times10^{3}} \\
&= 2{,}3\times10^{8}\ \text{m·s}^{-1}.
\end{aligned}
$$

**Source d'erreur principale** : la **mesure de la durée** (22 min), surestimée par Römer (la valeur réelle est voisine de 16 min), bien plus incertaine que la distance. C'est elle qui explique l'écart avec $2{,}998\times10^{8}\ \text{m·s}^{-1}$.

### Q14. Phénomène

Il s'agit de l'**effet Doppler** (Doppler-Fizeau pour les ondes lumineuses), énoncé au milieu du XIXᵉ siècle.

### Q15. Démonstration de la fréquence perçue

La source immobile émet des fronts d'onde séparés de la longueur d'onde $\lambda = \dfrac{c}{f}$. L'observateur se déplace à la vitesse $v$ **vers** la source : la vitesse relative des fronts d'onde par rapport à l'observateur est $c + v$. Il reçoit donc les fronts à la fréquence

$$
\begin{aligned}
f' \\
&= \frac{c+v}{\lambda} \\
&= \frac{c+v}{c/f} \\
&= f\,\frac{c+v}{c}.
\end{aligned}
$$

*(La formule de l'énoncé, $f' = \dfrac{cf}{c-v}$, correspondrait à une source mobile vers un observateur fixe.)*

### Q16. Valeur de $c$ à partir de Römer

Avec $f = 1/T$ et l'observateur se rapprochant : $T' = T\,\dfrac{c}{c+v}$, d'où une diminution

$$
\begin{aligned}
\Delta T \\
&= T - T' \\
&= T\,\frac{v}{c+v} \approx T\,\frac{v}{c}\quad \\
&\Longrightarrow\quad c \approx \frac{T\,v}{\Delta T}.
\end{aligned}
$$

$T = 1{,}769\ \text{j} = 1{,}53\times10^{5}\ \text{s}$, $v = 3{,}0\times10^{4}\ \text{m·s}^{-1}$, $\Delta T = 15\ \text{s}$ :

$$
c \approx \frac{1{,}53\times10^{5}\times 3{,}0\times10^{4}}{15} = 3{,}1\times10^{8}\ \text{m·s}^{-1}.
$$

Valeur en très bon accord avec $c = 2{,}998\times10^{8}\ \text{m·s}^{-1}$.

### Q17. Expérience de Foucault ; incertitude

La relation fournie donne

$$
\begin{aligned}
c&=\frac{16\pi Df}{\theta}\\
&=\frac{16\pi\times20{,}0\times375}{1{,}263\times10^{-3}}\\
&=2{,}984886\times10^8\ \mathrm{m\,s^{-1}}.
\end{aligned}
$$

En supposant les grandeurs d'entrée indépendantes, la propagation des incertitudes donne

$$
\frac{u(c)}c
=\sqrt{\left(\frac{0{,}2}{20{,}0}\right)^2
+\left(\frac3{375}\right)^2
+\left(\frac{0{,}009}{1{,}263}\right)^2}
=1{,}47\times10^{-2}.
$$

Ainsi $u(c)=4{,}37\times10^6\ \mathrm{m\,s^{-1}}$, soit, avec deux chiffres significatifs pour l'incertitude,

$$
\boxed{c=(2{,}985\pm0{,}044)\times10^8\ \mathrm{m\,s^{-1}}.}
$$

### Q18. Autre expérience de Foucault

Le **pendule de Foucault** (installé sous la coupole du Panthéon en 1851) met en évidence la **rotation de la Terre sur elle-même**. On peut aussi citer le **gyroscope** qu'il a inventé, ou les **courants de Foucault** (freinage et chauffage par induction).

### Q19. Compatibilité de la mesure

On calcule l'écart normalisé en conservant les valeurs non arrondies de Q17 :

$$
z=\frac{|2{,}984886\times10^8-2{,}99792458\times10^8|}{4{,}3744\times10^6}
\approx0{,}30.
$$

**$z<2$ : la mesure est compatible avec la valeur de référence.** L'incertitude relative caractérise sa précision ; l'écart normalisé permet ici d'apprécier la compatibilité.

### Q20. Extrait d'activité (annexe 1-G)

1. *Sécurité* : l'éthanoate d'éthyle est **très inflammable** (H225) → travailler loin de toute flamme, sous ventilation ; **irritant pour les yeux** (H319) et pouvant provoquer somnolence/vertiges (H336) → port de **lunettes, gants, blouse**, manipulation sous hotte ou en salle aérée.
2. *Verrerie* : **éprouvette graduée** (ou pipette jaugée de 20,0 mL) pour la solution d'hydroxyde de sodium, **bécher de 200 mL**, **éprouvette graduée** pour les 80 mL d'eau distillée, **petite éprouvette graduée (2 mL)** pour l'éthanoate d'éthyle.
3. *Choix du pH-mètre* : la réaction **consomme les ions HO⁻** ; la concentration $[\text{HO}^-]$ diminue. Via le produit ionique de l'eau $K_e = [\text{H}_3\text{O}^+][\text{HO}^-]$, $[\text{H}_3\text{O}^+]$ augmente et le **pH diminue** : une grandeur mesurable en continu permet donc de suivre l'avancement.

### Q21. Ligne 10 (annexe 1-H)

Comme $\text{pH} = \text{p}K_e + \log[\text{HO}^-]$, on a $[\text{HO}^-] = 10^{\,\text{pH}-\text{p}K_e}$. En Python (opération vectorisée sur le tableau `pH`) :
```python
C_HO = 10**(pH - pKe)
```

### Q22. Commentaires de lignes

- Ligne 15 `plt.grid()` : *affiche le quadrillage du graphique.*
- Ligne 16 `plt.xlabel(...)` : *légende l'axe des abscisses (temps en min).*
- Ligne 19 `plt.axis(xmin=0,xmax=10)` : *fixe les bornes de l'axe des abscisses.*
- Ligne 21 `plt.show()` : *affiche la figure à l'écran.*

### Q23. Décroissance du pH

La transformation consomme les ions $\text{HO}^-$ : $[\text{HO}^-]$ **décroît** au cours du temps. Par $K_e = [\text{H}_3\text{O}^+][\text{HO}^-] = \text{cte}$, $[\text{H}_3\text{O}^+]$ **augmente**, donc $\text{pH} = -\log[\text{H}_3\text{O}^+]$ **diminue**, ce qui explique l'allure décroissante.

### Q24. Document ressource sur $t_{1/2}$

> **Temps de demi-réaction $t_{1/2}$** : durée au bout de laquelle la concentration du **réactif limitant** a atteint la **moitié** de sa valeur initiale (transformation totale).
> **Méthode graphique** : sur la courbe $[\text{HO}^-](t)$, repérer la valeur initiale $[\text{HO}^-]_0$ ; tracer l'ordonnée $[\text{HO}^-]_0/2$ ; lire l'abscisse du point de la courbe correspondant : c'est $t_{1/2}$. *(Penser à légender les axes et leurs unités.)*

### Q25. Réactif limitant et $t_{1/2}$

$n(\text{HO}^-) = C\cdot V = 2{,}5\times10^{-2}\times 20{,}0\times10^{-3} = 5{,}0\times10^{-4}\ \text{mol}$.
Pour l'éthanoate d'éthyle : masse volumique $\rho = d\cdot\rho_{\text{eau}} = 0{,}902\times1{,}00\ \text{g·mL}^{-1}$, donc $m = \rho\cdot V = 0{,}902\times 2{,}0 = 1{,}8\ \text{g}$, et

$$
\begin{aligned}
n(\text{ester}) \\
&= \frac{m}{M} \\
&= \frac{1{,}8}{88{,}1} \\
&= 2{,}0\times10^{-2}\ \text{mol}.
\end{aligned}
$$

La réaction est mole à mole : $n(\text{ester}) \gg n(\text{HO}^-)$, donc **$\text{HO}^-$ est le réactif limitant**.
Sur la courbe $[\text{HO}^-](t)$ (annexe 1-I), $[\text{HO}^-]_0 = 5{,}0\times10^{-3}\ \text{mol·L}^{-1}$ ; la moitié, $2{,}5\times10^{-3}\ \text{mol·L}^{-1}$, est atteinte vers $t_{1/2} \approx 60\ \text{s}$.

### Q26. Moyenne et incertitude-type (annexe 1-J)

Pour $N=12$ valeurs :

$$
\begin{aligned}
\overline{t_{1/2}} \\
&= \frac{1}{12}\sum t_i \\
&= \frac{716}{12} \\
&= 59{,}7\ \text{s}.
\end{aligned}
$$

Écart-type expérimental : $s = \sqrt{\dfrac{1}{N-1}\sum (t_i-\overline{t})^2} = \sqrt{\dfrac{166{,}5}{11}} = 3{,}9\ \text{s}$.

$$
\begin{aligned}
u(t_{1/2}) \\
&= \frac{s}{\sqrt{N}} \\
&= \frac{3{,}9}{\sqrt{12}} \\
&= 1{,}1\ \text{s}.
\end{aligned}
$$

Soit $t_{1/2} = (59{,}7 \pm 1{,}1)\ \text{s}$.

### Q27. Nom de la méthode

C'est la **méthode de la dégénérescence de l'ordre** (ou méthode de l'isolement / de l'excès) : l'éthanoate d'éthyle, en large excès, voit sa concentration quasi constante ; la loi de vitesse devient d'ordre 1 apparent par rapport à $\text{HO}^-$.

### Q28. Relation $\ln[\text{HO}^-]$–$t$

Vitesse de disparition : $v = -\dfrac{\mathrm{d}[\text{HO}^-]}{\mathrm{d}t}$. Loi d'ordre 1 : $v = k_{\text{app}}[\text{HO}^-]$. D'où

$$
\begin{aligned}
\frac{\mathrm{d}[\text{HO}^-]}{[\text{HO}^-]} \\
&= -k_{\text{app}}\,\mathrm{d}t \; \\
&\Longrightarrow\; \ln[\text{HO}^-] \\
&= -k_{\text{app}}\,t + \ln[\text{HO}^-]_0.
\end{aligned}
$$

### Q29. Conclusion et $k_{\text{app}}$

La courbe $\ln[\text{HO}^-] = f(t)$ (annexe 1-K) est une **droite** (coefficient de corrélation $0{,}994$) : l'évolution suit bien une **loi de vitesse d'ordre 1** par rapport à $\text{HO}^-$. Le coefficient directeur vaut $a = -k_{\text{app}} = -0{,}608\ \text{min}^{-1}$, donc

$$
\begin{aligned}
k_{\text{app}} \\
&= 0{,}608\ \text{min}^{-1} \\
&= \frac{0{,}608}{60} \\
&= 1{,}0\times10^{-2}\ \text{s}^{-1}.
\end{aligned}
$$

### Q30. Loi de vitesse et dépendance en $T$

L'ordre partiel étant 1 par rapport à chaque réactif :

$$
v = k\,[\text{ester}]\,[\text{HO}^-] \quad (\text{ordre global } 2).
$$

La constante de vitesse $k$ dépend de la température par la **loi d'Arrhenius** :

$$
k = A\,\exp\!\left(-\frac{E_a}{R\,T}\right),
$$

avec $A$ le facteur préexponentiel, $E_a$ l'**énergie d'activation** (J·mol⁻¹), $R$ la **constante des gaz parfaits** (8,314 J·K⁻¹·mol⁻¹) et $T$ la température (K).

### Q31. Schémas de Lewis

L'éthanoate d'éthyle a pour connectivité $\mathrm{CH_3-C(=O)-O-CH_2-CH_3}$. Les deux atomes d'oxygène portent chacun **deux doublets non liants** ; le carbone carbonylé est lié à trois voisins et respecte l'octet.

L'ion hydroxyde possède une liaison simple H–O, une charge formelle $-1$ sur l'oxygène et **trois doublets non liants** sur cet oxygène. Une représentation textuelle des doublets est :

```text
      —
H — O⁻ |
      —
```

Les trois traits non liants autour de O représentent les six électrons non engagés dans la liaison O–H. Le carbone carbonylé de l'ester est électrophile ; un doublet non liant de l'oxygène de HO⁻ peut l'attaquer.

### Q32. Mécanisme réactionnel

1. **Addition nucléophile.** Une flèche courbe part d'un doublet non liant de l'oxygène de $\mathrm{HO^-}$ vers le carbone du groupe carbonyle ; simultanément, une flèche part de la liaison $\pi$ C=O vers son oxygène. On obtient l'intermédiaire tétraédrique $\mathrm{CH_3-C(OH)(O^-)-OCH_2CH_3}$.
2. **Élimination.** Un doublet de l'oxygène chargé négativement reforme la liaison C=O ; la liaison entre le carbone acyle et l'oxygène du groupe éthoxy se rompt vers cet oxygène. Les produits de cette étape sont $\mathrm{CH_3COOH}$ et $\mathrm{CH_3CH_2O^-}$.
3. **Réaction acide-base.** Un doublet de l'éthanolate se dirige vers le proton du groupe carboxyle ; la liaison O–H de l'acide se rabat sur son oxygène. Il se forme $\mathrm{CH_3COO^-}$ et $\mathrm{CH_3CH_2OH}$. Cette dernière étape favorise le bilan global de saponification.

Les charges sont conservées à chaque étape. L'éthanolate n'est pas à qualifier de bon nucléofuge sans réserve : son départ ici accompagne la reformation du carbonyle, puis le transfert de proton déplace le bilan vers les produits.

## Partie 2 — L'électricité : histoire, concepts et modèles

### Q33. Électrostatique vs électrocinétique

L'**électrostatique** étudie les **charges électriques au repos** et les interactions (loi de Coulomb) et champs qu'elles créent. L'**électrocinétique** étudie les **charges en mouvement** (courant électrique) dans les circuits et les lois qui les gouvernent (lois d'Ohm, de Kirchhoff). La distinction tient donc au caractère **statique ou mobile** des charges.

### Q34. Interprétation microscopique (ballon)

Le frottement sur la laine **arrache des électrons** à la laine, chargeant le ballon **négativement** (excès d'électrons). Approché du plafond (isolant électriquement neutre), le ballon chargé provoque, par **influence**, une **polarisation** locale : les charges du plafond se redistribuent, la face proche se chargeant positivement (charges opposées au ballon). Ces charges opposées s'**attirent** (interaction coulombienne attractive), maintenant le ballon « collé ».

### Q35. Molécules d'eau et champ électrique

La molécule d'eau est **polaire** : du fait de sa **géométrie coudée** et de la plus grande **électronégativité** de l'oxygène par rapport à l'hydrogène, le barycentre des charges positives ne coïncide pas avec celui des charges négatives → la molécule porte un **moment dipolaire permanent**. Un champ électrique **oriente** ces dipôles et exerce une force sur eux (plus intense côté champ fort) : le filet d'eau est dévié vers l'objet électrisé.

### Q36. Risques électrostatiques

Les tensions électrostatiques peuvent être élevées, mais la quantité de charge accumulée et l'énergie stockée lors des expériences décrites sont faibles. Au contact, la charge se transfère pendant un temps très bref et la tension chute rapidement : la source ne maintient pas un courant dans le corps.

Le danger dépend de l'intensité, de la durée et du trajet du courant. **Une décharge peut présenter un pic de courant sans fournir un courant durable** ; sa faible charge et sa brièveté expliquent ici le risque limité. Une tension élevée ne suffit donc pas, à elle seule, à caractériser le danger.

### Q37. Transfert de charge dans l'électroscope (correction B-2)

La tige de PVC négative repousse les **électrons mobiles** de l'électroscope vers les feuilles : le plateau présente un déficit local d'électrons et les feuilles un excès ; elles se repoussent et s'écartent. L'électroscope reste globalement neutre tant qu'il n'y a pas de contact avec la Terre.

En touchant le plateau avec le doigt tout en maintenant la tige proche, on relie l'électroscope à la Terre ; une partie des électrons repoussés quitte alors l'électroscope. On retire **d'abord le doigt**, puis la tige. L'électroscope isolé conserve un déficit d'électrons, donc une **charge globale positive**. Les charges positives des noyaux ne se sont pas déplacées : c'est le départ d'électrons qui explique cette charge.

### Q38. Orientation du champ magnétique

Le faisceau se déplace vers la droite et, en présence du seul champ électrique, dévie vers le haut sur le schéma 2-B.2. Comme les particules sont chargées négativement, $\vec E$ est dirigé vers le bas ; la force électrique est dirigée vers le haut.

Pour redresser le faisceau, la force magnétique doit être dirigée vers le bas. Choisissons $\vec e_x$ vers la droite, $\vec e_y$ vers le haut et $\vec e_z$ vers le lecteur. Avec $\vec v=v\vec e_x$ et **$\vec B=-B\vec e_z$ entrant dans le plan de la figure**,

$$
\vec v\wedge\vec B=vB\vec e_y,
$$

et $q\vec v\wedge\vec B$ est dirigé vers le bas puisque $q<0$. Les forces se compensent lorsque $vB=E$, soit $\vec E+\vec v\wedge\vec B=\vec0$.

### Q39. Vitesse du rayonnement cathodique

À l'équilibre (1ʳᵉ loi de Newton, mouvement rectiligne uniforme), les composantes électrique et magnétique se compensent : $\lvert q\rvert E = \lvert q\rvert vB$, d'où

$$
\begin{aligned}
v \\
&= \frac{E}{B} \\
&= \frac{15\times10^{3}}{0{,}72\times10^{-3}} \\
&= 2{,}1\times10^{7}\ \text{m·s}^{-1}.
\end{aligned}
$$

### Q40. Nature des rayons cathodiques

$\dfrac{v}{c} = \dfrac{2{,}1\times10^{7}}{3{,}0\times10^{8}} \approx 0{,}07$, soit **7 % de la célérité de la lumière**, nettement inférieur à $c$. Un rayonnement **électromagnétique** se propagerait à $c$. Cette valeur bien plus faible prouve que les rayons cathodiques sont de nature **corpusculaire** (particules matérielles).

### Q41. Inconvénient des « questions à tiroir »

Les questions dépendantes exposent l'élève à un **effet d'enchaînement des erreurs** : une erreur à une question compromet toutes les suivantes, même si la méthode est correcte, et peut bloquer l'élève. *Exemple* : si un élève se trompe dans l'expression de l'accélération $\vec{a}$ (question a), toutes les expressions de $\vec{v}$, $\vec{r}$, puis le rapport $q/m$ (questions b à e) seront fausses, sans qu'il puisse valoriser la suite du raisonnement.

### Q42. Circuit illustrant l'unicité du courant

On réalise un circuit **série** avec la pile, l'interrupteur et les **deux ampoules identiques (3,5 V – 150 mA)**. On observe que les deux ampoules brillent avec le **même éclat**, et qu'en **inversant leur position** dans le circuit, leur éclat ne change pas. Puisqu'une ampoule « avant » ne brille pas plus qu'une ampoule « après », le courant n'est **pas consommé** : il est **identique en tout point** d'une boucle série. Cela réfute la conception d'un « courant qui s'use ».

### Q43. « Payer l'électricité »

Le courant électrique (déplacement de charges) est bien **restitué** au réseau : ce n'est pas lui qui est « consommé ». Ce que l'on paie, c'est l'**énergie électrique** transportée par ce courant et **convertie** dans nos appareils en d'autres formes (chaleur, lumière, mouvement). Le courant est le **support** du transfert d'énergie ; c'est l'**énergie**, et non le courant, qui est consommée. *(D'ailleurs le réseau domestique fonctionne en courant alternatif : les électrons oscillent sur place sans être « consommés ».)*

### Q44. Densité volumique de charges mobiles

Chaque atome libère un électron ; le nombre d'électrons par unité de volume est $n = \dfrac{\rho\,N_A}{M}$ (atomes par m³), d'où

$$
\boxed{\;\rho_e = n\,e = \frac{\rho\,N_A\,e}{M}\;}
$$

*Vérification dimensionnelle* : $\dfrac{[\text{kg·m}^{-3}][\text{mol}^{-1}][\text{C}]}{[\text{kg·mol}^{-1}]} = [\text{C·m}^{-3}]$.

### Q45. Volume traversé

Pendant $\Delta t$, les électrons parcourent $v_D\,\Delta t$ à travers la section $S$ :

$$
V = S\,v_D\,\Delta t.
$$

### Q46. Vitesse de dérive

La charge mobile traversant $S$ pendant $\Delta t$ est $Q = \rho_e\,V = \rho_e\,S\,v_D\,\Delta t$, et l'intensité $I = \dfrac{Q}{\Delta t} = \rho_e\,S\,v_D$. Donc

$$
v_D = \frac{I}{\rho_e\,S} = \frac{M\,I}{\rho\,S\,N_A\,e}.
$$

### Q47. Application numérique

$\rho_e = \dfrac{\rho\,N_A\,e}{M} = \dfrac{8{,}96\times 6{,}02\times10^{23}\times 1{,}60\times10^{-19}}{63{,}5} = 1{,}36\times10^{4}\ \text{C·cm}^{-3} = 1{,}36\times10^{10}\ \text{C·m}^{-3}$.
Avec $S = 1{,}5\ \text{mm}^2 = 1{,}5\times10^{-6}\ \text{m}^2$ et $I = 1{,}0\ \text{A}$ :

$$
v_D = \frac{I}{\rho_e\,S} = \frac{1{,}0}{1{,}36\times10^{10}\times 1{,}5\times10^{-6}} \approx 5\times10^{-5}\ \text{m·s}^{-1}.
$$

Soit $v_D \approx 0{,}05\ \text{mm·s}^{-1}$, vitesse **extrêmement faible** (sub-millimétrique par seconde).

### Q48. Vitesse de propagation du signal

Le signal électrique est une **onde électromagnétique** se propageant dans le conducteur à une vitesse $v_S$ voisine de la **célérité de la lumière** dans ce milieu, soit $v_S \sim 2\times10^{8}\ \text{m·s}^{-1}$ (quelques $10^{8}\ \text{m·s}^{-1}$).

### Q49. Différence $v_D$ / $v_S$

La **vitesse de dérive** $v_D$ (quelques $10^{-5}\ \text{m·s}^{-1}$) est la vitesse **moyenne de déplacement d'ensemble** des électrons : accélérés par le champ, ils « se cognent » sans cesse sur le réseau de cations, ce qui les ralentit fortement. La **vitesse du signal** $v_S$ (quelques $10^{8}\ \text{m·s}^{-1}$) est la vitesse de propagation de la **perturbation électromagnétique** (l'« ordre de se mettre en mouvement »), qui se transmet quasi instantanément à **tous** les électrons du fil. Ce sont deux grandeurs physiques **distinctes** et sans lien direct : l'une décrit le déplacement lent des porteurs, l'autre la propagation rapide de l'information.

### Q50. Séquence pédagogique (enseignement scientifique, terminale, 6 h)

**Contextualisation.** Deux siècles d'électrification : des premières piles aux panneaux solaires et aux alternateurs des centrales, l'électricité est produite par **conversion d'énergie** sans combustion, enjeu de la transition écologique.

**Problématique.** *« À partir de quels phénomènes physiques peut-on produire de l'énergie électrique sans combustion, et comment les premières découvertes historiques éclairent-elles ces procédés ? »*

**Évaluation diagnostique (QCM, 3 questions).**
1. L'unité d'énergie est : a) le watt ; **b) le joule** ; c) le volt.
2. Un alternateur convertit : a) l'énergie électrique en chimique ; **b) l'énergie mécanique en électrique** ; c) l'énergie lumineuse en thermique.
3. Une pile fournit de l'énergie électrique à partir : **a) d'une transformation chimique** ; b) de la lumière ; c) d'un aimant tournant.

**Les six séances (thèmes).**
1. Formes et conversions de l'énergie ; énergie, puissance, durée.
2. L'**induction électromagnétique** (Faraday, Lenz) ; l'alternateur.
3. L'**effet photovoltaïque** (Edmond Becquerel, 1839) ; semi-conducteurs et spectre solaire.
4. La **conversion électrochimique** (Volta, Daniell, Leclanché) ; piles et accumulateurs.
5. Chaînes de conversion et rendement d'un système ; incidences environnementales.
6. Synthèse, retour à la problématique, évaluation sommative.

**Détail d'une séance (séance 2 — induction, 1 h).**
- *Activité de l'enseignant* : rappel historique (expérience de Faraday, 1831) ; mise à disposition d'un **aimant, d'une bobine et d'un galvanomètre/interface d'acquisition**.
- *Activité de l'élève* : **reproduire l'expérience historique** — déplacer l'aimant dans la bobine, observer l'apparition d'une tension induite ; faire varier la vitesse ; relier qualitativement vitesse de variation du flux et tension.
- *Modalités* : travail en îlots, acquisition numérique de $u(t)$.
- *Institutionnalisation* : un alternateur = source de champ magnétique + conducteur en mouvement relatif ; conversion énergie mécanique → électrique, rendement proche de 1.
- *Trace écrite* : schéma annoté de l'alternateur ; phrase reliant rotation du rotor et fréquence du courant.

**Évaluation sommative (5 questions, dont une tâche complexe).** Verbes d'action :
1. **Reconnaître** les éléments d'un alternateur sur un schéma.
2. **Relier** vitesse de rotation du rotor et fréquence.
3. **Définir** le rendement d'un alternateur.
4. **Comparer** le spectre d'absorption d'un semi-conducteur au spectre solaire pour juger de son usage photovoltaïque.
5. **Tâche complexe** : « À partir des documents fournis (ressource primaire, rendements, données de production), proposer et justifier une chaîne de conversions permettant d'alimenter une habitation en électricité sans combustion, et estimer l'énergie disponible. » *(résolution autonome, sans guidage pas-à-pas)*

---

## Partie 3 — La pile, siège d'une évolution spontanée

### Q51. Aides au branchement des appareils

- **Voltmètre** : « Branche-le **en dérivation** aux bornes de la pile (une électrode sur la borne **V**, l'autre sur la borne **COM**). Sélectionne le calibre tension continue le plus adapté. Si la valeur affichée est négative, **inverse les deux bornes** pour obtenir une valeur positive. »
- **Ampèremètre** : « Branche-le **en série** dans le circuit (borne **mA** côté circuit, borne **COM** côté retour). Choisis un calibre courant adapté, en partant du plus grand. »

### Q52. Remarque sur l'écriture des résultats

Les résultats $E = 1{,}1$ et $I = 0{,}024$ sont écrits **sans unité**. Il faut écrire $E = 1{,}1\ \text{V}$ et $I = 0{,}024\ \text{A}$ (soit $24\ \text{mA}$), et veiller à la cohérence des **chiffres significatifs**.

### Q53. Imposer une tension à vide positive

1. Cela **fixe un sens de branchement commun** à tous les groupes, ce qui **facilite la correction collective** et la comparaison des résultats.
2. Cela aide les élèves à **identifier sans ambiguïté la polarité** de la pile (borne + = électrode reliée à la borne V du voltmètre), structurant l'exploitation ultérieure (anode/cathode).

### Q54. Correction-type des 5 questions (annexe 3-B)

1–2. **Schéma de la pile Daniell** (tracé à la règle) : demi-pile Zn/Zn²⁺ et demi-pile Cu/Cu²⁺ reliées par un pont salin ; circuit extérieur comportant un **conducteur ohmique (27 Ω) en série avec un ampèremètre**. Polarité : **Cu = borne +**, **Zn = borne −** (car $E = 1{,}1\ \text{V}>0$ avec Cu sur V). **Courant** extérieur : de + vers − (de Cu vers Zn) ; **électrons** : de Zn vers Cu dans les fils ; **ions** dans le pont salin : les **anions** migrent vers le compartiment de l'anode (Zn), les **cations** vers celui de la cathode (Cu).

Schéma attendu : deux béchers (Zn²⁺ / Cu²⁺) reliés par un pont salin ; électrodes Zn (−) et Cu (+) ; circuit extérieur R + ampèremètre ; flèches i, e⁻ et ions.

3. **Demi-équations** (d'après la polarité) :
   - Anode (Zn, oxydation) : $\text{Zn}(s) \rightarrow \text{Zn}^{2+}(aq) + 2e^-$.
   - Cathode (Cu, réduction) : $\text{Cu}^{2+}(aq) + 2e^- \rightarrow \text{Cu}(s)$.
4. **Équation de fonctionnement** : $\text{Zn}(s) + \text{Cu}^{2+}(aq) \rightarrow \text{Zn}^{2+}(aq) + \text{Cu}(s)$.
5. **Rôle du pont salin** : assurer la **neutralité électrique** des deux compartiments par migration des ions, **fermer le circuit** et permettre le fonctionnement continu de la pile.

### Q55. Schéma de la pile au citron

Schéma attendu : un **citron** dans lequel sont plantées une **plaque de zinc** et une **plaque de cuivre**, reliées par des fils et pinces crocodiles à une **DEL** ; la borne + de la DEL (anode, patte longue) reliée à la plaque de **cuivre** (pôle +), la borne − à la plaque de **zinc** (pôle −).

Le **citron** (jus acide) joue le rôle d'électrolyte ; il ne faut pas le remplacer par le symbole d'une pile. Le sens de branchement de la DEL doit respecter la polarité imposée par les deux métaux.

### Q56. Réactions électrochimiques de la pile au citron

Avec $E°(\text{Zn}^{2+}/\text{Zn}) = -0{,}76\ \text{V} < E°(\text{H}^+/\text{H}_2) = 0{,}00\ \text{V}$, le zinc (réducteur le plus fort) s'oxyde et les ions $\text{H}^+$ du jus acide se réduisent sur le cuivre :
- Anode (−), zinc : $\text{Zn}(s) \rightarrow \text{Zn}^{2+}(aq) + 2e^-$.
- Cathode (+), cuivre : $2\,\text{H}^+(aq) + 2e^- \rightarrow \text{H}_2(g)$.

Équation globale : $\text{Zn}(s) + 2\,\text{H}^+(aq) \rightarrow \text{Zn}^{2+}(aq) + \text{H}_2(g)$.

### Q57. La DEL ne s'allume pas

La **tension délivrée par une seule pile au citron** (≈ 0,9–1 V) est **inférieure à la tension seuil de la DEL** (≈ 1,8–2 V) ; de plus, la **résistance interne élevée** de la pile limite fortement l'intensité. La DEL ne peut donc s'allumer : il faudrait **associer plusieurs piles en série** pour dépasser le seuil.

### Q58. Conseil pour la question de Grand Oral

La question « Qu'est-ce qu'une pile à hydrogène ? » est trop **descriptive et fermée** (elle appelle une simple définition). Conseiller de la **problématiser** et de la **relier au projet technologique** de l'élève, par exemple : *« En quoi la pile à hydrogène peut-elle constituer une alternative aux piles conventionnelles pour une application de cuisine moléculaire ? »*

### Q59. Quatre questions supplémentaires (STL SPCL)

1. **Déterminer le nombre d'oxydation** de l'élément cuivre (resp. zinc) dans $\text{Cu}^{2+}$, $\text{Cu}(s)$, $\text{Zn}^{2+}$, $\text{Zn}(s)$ et identifier oxydant et réducteur.
2. **À l'aide de la relation de Nernst**, exprimer le potentiel de chaque demi-pile en fonction des concentrations, puis **prévoir l'influence d'une dilution** de la solution de sulfate de cuivre sur la tension.
3. **Calculer la constante d'équilibre** de la réaction de fonctionnement à partir des potentiels standards, et **prévoir le sens d'évolution spontanée**.
4. **Déterminer la quantité d'électricité** maximale disponible dans la pile à partir des quantités de matière initiales.

### Q60. Schéma du dispositif de titrage potentiométrique

Schéma attendu : bécher contenant la solution S (Fe²⁺ acidifiée), **électrode de platine (mesure)** et **électrode au calomel saturée ECS (référence, reliée à COM)**, toutes deux **reliées à un voltmètre** ; **burette** de permanganate de potassium ; **agitateur magnétique**.

### Q61. Électrode au calomel saturée

L'**ECS** est constituée de mercure $\text{Hg}(\ell)$ en contact avec du calomel solide $\text{Hg}_2\text{Cl}_2(s)$, l'ensemble plongeant dans une **solution saturée de chlorure de potassium** (KCl). Le couple mis en jeu est $\text{Hg}_2\text{Cl}_2(s)/\text{Hg}(\ell)$ :

$$
\text{Hg}_2\text{Cl}_2(s) + 2e^- \rightarrow 2\,\text{Hg}(\ell) + 2\,\text{Cl}^-.
$$

La loi de Nernst donne $E = E°(\text{Hg}_2\text{Cl}_2/\text{Hg}) - \dfrac{0{,}06}{2}\log[\text{Cl}^-]^2 = E° - 0{,}06\log[\text{Cl}^-]$. La solution de KCl étant **saturée**, $[\text{Cl}^-]$ est **constante** (fixée par la solubilité) : le potentiel de l'ECS est donc **fixe et reproductible** ($E(\text{ECS}) = 0{,}24\ \text{V}$), ce qui en fait une **électrode de référence**.

### Q62. Potentiels standards par la courbe (annexe 3-E)

Le volume équivalent, lu au maximum de $\dfrac{\mathrm{d}e}{\mathrm{d}V}$, vaut $V_{\text{éq}} = 9{,}0\ \text{mL}$.
- À la **demi-équivalence** ($V = V_{\text{éq}}/2 = 4{,}5\ \text{mL}$), $[\text{Fe}^{3+}] = [\text{Fe}^{2+}]$ : $E = E°(\text{Fe}^{3+}/\text{Fe}^{2+})$. La lecture $e \approx 0{,}53\ \text{V}$ donne

$$
E°(\text{Fe}^{3+}/\text{Fe}^{2+}) = e + E(\text{ECS}) = 0{,}53 + 0{,}24 \approx 0{,}77\ \text{V}.
$$

- À la **double équivalence** ($V = 2V_{\text{éq}} = 18\ \text{mL}$), l'excès de permanganate égale la quantité de $\text{Mn}^{2+}$ formé ($[\text{MnO}_4^-] = [\text{Mn}^{2+}]$) : $E \approx E°(\text{MnO}_4^-/\text{Mn}^{2+})$. La lecture $e \approx 1{,}27\ \text{V}$ donne

$$
E°(\text{MnO}_4^-/\text{Mn}^{2+}) = 1{,}27 + 0{,}24 \approx 1{,}5\ \text{V}.
$$

### Q63. Équation de titrage et concentration en Fe²⁺

Réaction support (milieu acide) :

$$
\text{MnO}_4^-(aq) + 5\,\text{Fe}^{2+}(aq) + 8\,\text{H}^+(aq) \rightarrow \text{Mn}^{2+}(aq) + 5\,\text{Fe}^{3+}(aq) + 4\,\text{H}_2\text{O}(\ell).
$$

À l'équivalence : $n(\text{MnO}_4^-)_{\text{versé}} = \dfrac{n(\text{Fe}^{2+})}{5}$, soit $C_{\text{MnO}_4^-}\,V_{\text{éq}} = \dfrac{C_S\,V}{5}$ :

$$
\begin{aligned}
C_S \\
&= \frac{5\,C_{\text{MnO}_4^-}\,V_{\text{éq}}}{V} \\
&= \frac{5\times 2{,}0\times10^{-2}\times 9{,}0}{20{,}0} \\
&= 4{,}5\times10^{-2}\ \text{mol·L}^{-1}.
\end{aligned}
$$

La solution commerciale ayant été **diluée 10 fois**, sa concentration en Fe²⁺ est

$$
C_{\text{commerciale}} = 10\times C_S = 0{,}45\ \text{mol·L}^{-1}.
$$

### Q64. Annotation de la copie DR-2

- **Erreur majeure (conversion)** : l'élève écrit $\Delta t = \dfrac{1930}{0{,}20} = 9650\ \text{s}$ en prenant $I = 0{,}20\ \text{A}$. Or $I = 20\ \text{mA} = 0{,}020\ \text{A}$. Le résultat correct est

$$
\begin{aligned}
\Delta t \\
&= \frac{Q}{I} \\
&= \frac{1930}{0{,}020} \\
&= 9{,}65\times10^{4}\ \text{s} \approx 26{,}8\ \text{h}.
\end{aligned}
$$

*Conseil 1* : « Convertis les mA en A avec soin : $20\ \text{mA} = 0{,}020\ \text{A}$ ; vérifie l'homogénéité avant tout calcul. »
- **Notation** : l'élève note « $m$ » la quantité de matière ($m = 0{,}100\times0{,}1 = 0{,}01$). *Conseil 2* : « Réserve $m$ à une masse et $n$ à une quantité de matière : écris $n(\text{Cu}^{2+}) = C\cdot V = 1{,}00\times10^{-2}\ \text{mol}$. »
- **Chiffres significatifs** : les données ont 3 chiffres significatifs. *Conseil 3* : « Donne le résultat avec un nombre cohérent de chiffres significatifs : $\Delta t \approx 2{,}7\times10^{1}\ \text{h}$. »
- **Analyse critique** : *Conseil 4* : « Vérifie la vraisemblance : une pile alimentant un appareil pendant seulement 2,7 h paraît faible ; le facteur 10 sur l'intensité est la cause. » *(La démarche — réactif limitant Cu²⁺, puis $n(e^-) = 2\,n(\text{Cu}^{2+})$, $Q = n(e^-)\mathcal{F}$, $\Delta t = Q/I$ — est correcte.)*

### Q65. Énoncé guidé (deux questions intermédiaires)

1. « Identifier le **réactif limitant** de la transformation en comparant les quantités de matière initiales de $\text{Cu}^{2+}$ et de Zn, et en déduire la **quantité maximale d'électrons** échangés. »
2. « Exprimer puis calculer la **quantité d'électricité** $Q$ disponible ($Q = n(e^-)\times\mathcal{F}$), puis la **durée maximale** de fonctionnement à partir de $\Delta t = \dfrac{Q}{I}$ (attention aux unités de $I$). »

### Q66. Grille d'évaluation — Analyser/Raisonner

| Indicateur de réussite **observable** | Non atteint | Partiellement | Atteint |
|---|---|---|---|
| Identifier la nécessité de rechercher le **réactif limitant** (comparaison des $n$ initiaux) | | | |
| Choisir la relation pertinente $n(e^-) = 2\,n(\text{Cu}^{2+})$ et la loi $Q = n(e^-)\,\mathcal{F}$ | | | |
| Mettre en œuvre la stratégie $\Delta t = \dfrac{Q}{I}$ avec unités cohérentes et contrôle de vraisemblance | | | |

### Q67. Séquence pédagogique (terminale STL PCM, 3 × 2 h)

**Contextualisation.** La pile, de la grenouille de Galvani à la pile Volta, convertit de l'énergie chimique en énergie électrique utilisable au quotidien (piles, accumulateurs).

**Problématique.** *« Comment une transformation d'oxydo-réduction permet-elle de produire un courant électrique, et quelle quantité d'électricité une pile peut-elle fournir ? »*

**Séance 1 (2 h) — Oxydo-réduction : les outils.**
- *Objectifs/contenus* : nombre d'oxydation ; oxydant/réducteur ; couple redox ; écriture de demi-équations et d'équations en milieu acide.
- *Activité* : exercices d'application et activité documentaire (oxydants/réducteurs usuels).
- *Institutionnalisation / trace écrite* : définitions, méthode d'ajustement des demi-équations.

**Séance 2 (2 h) — La pile : constitution et fonctionnement.**
- *Objectifs/contenus* : demi-pile, pile, pont salin ; anode/cathode ; polarité, sens du courant, des électrons et des ions.
- *Activité expérimentale* (annexe 3-B) : **réaliser la pile Daniell**, mesurer la tension à vide, identifier anode et cathode.
- *Trace écrite* : schéma annoté, équation de fonctionnement, rôle du pont salin.

**Séance 3 (2 h) — Quantité d'électricité.**
- *Objectifs/contenus* : déterminer la quantité d'électricité disponible à partir des quantités de matière initiales.
- *Activité* : **résolution de problème** (document réponse DR-2 réaménagé), avec énoncé différencié (version guidée / version ouverte).
- *Trace écrite* : $Q = n(e^-)\,\mathcal{F}$, $\Delta t = Q/I$ ; retour à la problématique.

**Évaluation formative (QCM, 4 questions couvrant les capacités exigibles).**
1. Dans $\text{MnO}_4^-$, le nombre d'oxydation du manganèse est : a) +2 ; **b) +7** ; c) −1.
2. L'oxydation se produit : **a) à l'anode** ; b) à la cathode.
3. Dans le circuit extérieur d'une pile, le courant circule : **a) du pôle + vers le pôle −** ; b) l'inverse.
4. La quantité d'électricité fournie par une pile se calcule par : a) $Q = U\times I$ ; **b) $Q = n(e^-)\times\mathcal{F}$** ; c) $Q = I/\Delta t$.
