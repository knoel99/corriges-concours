# BCE ECG — Mathématiques 2 appliquées (ESSEC) 2025 · Corrigé guidé

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

## Présentation du sujet

**Cadre.** Épreuve « Mathématiques 2 appliquées » conçue par l'ESSEC (code sujet 287), 4 heures, calculatrice interdite. Un problème d'**arrêt optimal** en quatre parties, 51 questions. D'après le rapport 2025 : 3 495 copies, moyenne 9,7, écart type 5,21 ; barème de 29 % pour la partie 1, 17 % pour la partie 2, 25 % pour la partie 3, 29 % pour la partie 4, dont 10 % d'informatique.

**Le problème.** On observe $n$ réels un par un et l'on doit, au moment où l'on voit un nombre, décider de le garder (définitivement) ou de passer au suivant ; on veut maximiser la probabilité de garder le plus grand. Stratégie étudiée : fixer un seuil $s$ et garder le premier nombre qui dépasse $s$ (le dernier, si aucun ne le dépasse).

- **Partie 1 (15 questions)** : outils. Inégalités $\mathrm e^t\geqslant1+t$, un réel $\alpha\approx0{,}806$, et un **couplage** : une variable de Bernoulli $X$ et une variable de Poisson $Y$ construites à partir de la même uniforme $U$, avec $P(X\neq Y)\leqslant2p^2$.

  Puis l'inégalité de Boole et une distance $\delta$ entre lois.
- **Partie 2 (10 questions)** : inégalité de Hodge et Le Cam $\delta(S_n,T_n)\leqslant4\sum p_k^2$ entre une somme de Bernoulli indépendantes et une loi de Poisson ; application à un nombre de succès qui converge en loi vers $\mathcal P(\ln2)$.
- **Partie 3 (11 questions)** : étude de $g(x)=\mathrm e^{-x}\int_0^x\frac{\mathrm e^t-1}t\,\mathrm dt$, son maximum en $\gamma\in[\ln3,2]$ et son développement $g(x)=\mathrm e^{-x}\sum_{k\geqslant1}\frac{x^k}{k!\,k}$ ; tracé en Python.
- **Partie 4 (15 questions)** : le problème du meilleur choix. Minoration générale par $\frac1{\mathrm e}$, formule exacte de $r_n$, limite $g(\lambda)$ quand $p=\frac\lambda n$, et choix optimal $\lambda=\gamma$.

**Notions mobilisées.** Étude de fonctions, théorème de la bijection, développement limité de $\mathrm e^x$ à l'ordre 2, fonctions de classe $\mathcal C^1$, intégrale fonction de sa borne, comparaison série-intégrale, série exponentielle et séries géométriques ; loi uniforme, loi de Poisson, loi de Bernoulli et binomiale, indépendance, lemme des coalitions, stabilité de la loi de Poisson, inégalité de Markov, convergence en loi, probabilité conditionnelle ; Python (dichotomie, boucles `while`, `rd.random`, tracés).

**Difficulté.** Sujet long, dense et bien guidé. Le rapport 2025 précise que « Pour avoir une très bonne note, la résolution d'environ 50% des questions suffit en général. » Il insiste sur la lecture préalable des hypothèses de chaque partie : par exemple, $p<\alpha$ dans les questions 3 et 9, $p_k\neq1$ dans la partie 4.

**Questions à ne pas laisser passer.** 1, 2. a), 2. b), 3. b), 4, 5. a), 7, 8, 11. b), 11. c), 12, 13. a), 13. b), 14. c), 17. a), 18. a), 18. b). Le rapport liste comme les plus pondérées : 3.a, 3.d, 3.e, 8, 12, 13.c, 13.d, 15.a, 17.b, 19.a, 19.e.

**Gestion du temps.** Environ 1 h 10 pour la partie 1, 35 minutes pour la partie 2, 1 h pour la partie 3 et 1 h 15 pour la partie 4. La partie 3 est indépendante des deux premières : on peut la traiter tôt.

---

## Partie 1 — Des résultats généraux

On prépare les outils : deux inégalités de convexité, un réel $\alpha$, une construction simultanée de $X\hookrightarrow\mathcal B(p)$ et $Y\hookrightarrow\mathcal P(p)$ qui coïncident avec grande probabilité, l'inégalité de Boole et la « distance » $\delta$.

### Question 1.

> [!INDICATION]
> Étudier $t\mapsto\mathrm e^t-1-t$.

> [!INDICATION]
> Pour la seconde inégalité, appliquer la première à un réel bien choisi.

#### Solution

$\varphi(t)=\mathrm e^t-1-t$ a pour dérivée $\mathrm e^t-1$, du signe de $t$ : minimum $\varphi(0)=0$, donc $\mathrm e^t\geqslant1+t$.

Pour $t>-1$, avec $u=\ln(1+t)$ : $1+t=\mathrm e^u\geqslant1+\ln(1+t)$, donc $\ln(1+t)\leqslant t$.

> [!METHODE]
> On peut aussi invoquer la convexité de $\exp$ (au-dessus de sa tangente en $0$) et la concavité de $\ln$ (en dessous de sa tangente en $1$).

### Question 2. a)

> [!INDICATION]
> Dériver, puis appliquer le théorème de la bijection sur $[0,1]$.

#### Solution

$f'(t)=-t\,\mathrm e^{-t}-1<0$ : $f$ est strictement décroissante. $f(0)=1>0$ et $f(1)=\frac2{\mathrm e}-1<0$.

Par le théorème de la bijection, $f$ s'annule en un unique $\alpha\in\,]0,1[$, et $f(t)>0\iff t<\alpha$ par stricte décroissance.

> [!PIEGE]
> L'équivalence $f(t)>0\iff t<\alpha$ demande les deux sens ; la stricte décroissance les donne d'un coup ($f(t)>f(\alpha)\iff t<\alpha$). Le rapport 2025 relève dans trop de copies « pas de différences entre condition nécessaire, suffisante, équivalence ».

### Question 2. b)

> [!INDICATION]
> Dichotomie : garder un intervalle $[a,b]$ contenant $\alpha$, avec $f(a)>0\geqslant f(b)$, et le couper en deux jusqu'à ce que sa longueur soit au plus $10^{-3}$.

#### Solution

```python
def f(t):
    return (1+t)*np.exp(-t) - t

a = 0
b = 1
while b - a > 10**(-3):
    c = (a + b)/2
    if f(c) > 0:
        a = c
    else:
        b = c
print(a)
```

Exécuté : $0{,}8057$, pour $\alpha\approx0{,}8065$.

> [!JURY]
> Le rapport 2025 regrette que « quelques candidats continuent inlassablement à croire que l'ordinateur va s'adapter à leur langage, alors que, c'est le contraire » : syntaxe exacte (`np.exp`, `**`, indentation), et une sortie (`print` ou `return`).

### Question 2. c)

> [!INDICATION]
> Étudier $t\mapsto1+2t-\mathrm e^t$ sur $[0,1]$ : elle croît puis décroît.

> [!INDICATION]
> Pour $\alpha$, minorer $f$ grâce à $\mathrm e^{-t}\geqslant\frac1{1+2t}$, puis évaluer en $\frac1{\sqrt2}$.

#### Solution

$\psi(t)=1+2t-\mathrm e^t$ croît sur $[0,\ln2]$ et décroît sur $[\ln2,1]$. Son minimum est donc atteint en une borne.

Or $\psi(0)=0$ et $\psi(1)=3-\mathrm e>0$, donc $\psi\geqslant0$ sur $[0,1]$.

Alors $f(t)\geqslant\frac{1+t}{1+2t}-t=\frac{1-2t^2}{1+2t}$, qui est nul en $\frac1{\sqrt2}$. Donc $f\left(\frac1{\sqrt2}\right)\geqslant0$, ce qui exclut $\frac1{\sqrt2}>\alpha$ : $\alpha\geqslant\frac1{\sqrt2}$.

### Question 3. a)

> [!INDICATION]
> Calculer les sommes partielles $c_k=\sum_{i\leqslant k}\frac{p^i}{i!}\mathrm e^{-p}$ de proche en proche, en mettant à jour le terme courant ($\times\frac pk$).

> [!INDICATION]
> On s'arrête au premier $k$ tel que $x\leqslant c_k$.

#### Solution

```python
def minimum(x, p):
    k = 0
    terme = np.exp(-p)
    S = terme
    while x > S:
        k = k + 1
        terme = terme * p / k
        S = S + terme
    return k

def simulY(p):
    return minimum(rd.random(), p)
```

> [!JURY]
> Question 3 a) parmi les plus pondérées (rapport 2025).

### Question 3. b)

> [!INDICATION]
> Écrire $[Y=k]$ comme un événement de la forme $[a<U\leqslant b]$.

#### Solution

Avec $c_{-1}=0$ : $[Y=k]=[c_{k-1}<U\leqslant c_k]$ par croissance de $(c_k)$, donc $P(Y=k)=c_k-c_{k-1}=\frac{p^k}{k!}\mathrm e^{-p}$ : $Y\hookrightarrow\mathcal P(p)$.

> [!METHODE]
> C'est la **méthode d'inversion** pour une loi discrète : on découpe $[0,1[$ en intervalles de longueurs $P(Y=k)$ et l'on regarde dans lequel tombe $U$.

### Question 3. c)

> [!INDICATION]
> Que vaut $c_1$ ? Comparer avec $\beta+p$.

#### Solution

$c_1=(1+p)\mathrm e^{-p}=\beta+p$. Si $Y=k\geqslant2$, $U>c_{k-1}\geqslant c_1=\beta+p$, donc $X=0$. Ainsi $[Y=k]\subset[X=0]$ et $P([X=0]\cap[Y=k])=P(Y=k)$.

### Question 3. d)

> [!INDICATION]
> Situer $\beta$ par rapport à $c_0=\mathrm e^{-p}$ ; faire un dessin de $[0,1[$ avec les points $\beta$, $c_0$, $\beta+p=c_1$.

> [!INDICATION]
> Chaque probabilité conjointe s'obtient comme la probabilité que $U$ tombe dans un intervalle, ou par différence.

#### Solution

On a $0<\beta<c_0<c_1=\beta+p\leqslant1$ :

- $[Y=1]=[c_0<U\leqslant c_1]\subset[\beta<U\leqslant\beta+p]=[X=1]$, donc $[X=0]\cap[Y=1]=\varnothing$ et $P([X=1]\cap[Y=1])=P(Y=1)=p\,\mathrm e^{-p}$ ;
- $[X=0]\cap[Y=0]=[U\leqslant\beta]$, de probabilité $\beta$ ;
- $P([X=1]\cap[Y=0])=c_0-\beta=p(1-\mathrm e^{-p})$.

Contrôle par simulation, avec $p=0{,}3$ et $2\cdot10^5$ tirages : les fréquences observées sont $0{,}2216$, $0{,}6638$ et $0{,}0782$.

Les valeurs théoriques sont $0{,}2222$, $0{,}6631$ et $0{,}0778$.

> [!JURY]
> Question 3 d) parmi les plus pondérées. Le rapport 2025 signale de « nombreux mélanges d'objets (événement, probabilité) » : on écrit $[X=0]\cap[Y=1]=\varnothing$ (événements) et $P(\dots)=0$ (nombres), pas l'inverse.

### Question 3. e)

> [!INDICATION]
> $[X=Y]$ est la réunion de deux des événements de 3. d).

> [!INDICATION]
> Pour la majoration, la question 1 en $t=-p$.

#### Solution

$P(X\neq Y)=1-\beta-p\,\mathrm e^{-p}=1+p-(1+2p)\mathrm e^{-p}$. Avec $\mathrm e^{-p}\geqslant1-p$ :

$$\begin{aligned}
P(X\neq Y)&\leqslant1+p-(1+2p)(1-p)\\
&=2p^2 .
\end{aligned}$$

> [!METHODE]
> Couplage : pour comparer deux lois, on construit deux variables de ces lois sur le même espace, aussi souvent égales que possible ; $P(X\neq Y)$ contrôle alors l'écart entre les lois (question 5).

### Question 4. a)

> [!INDICATION]
> Que signifie $T(\omega)\geqslant1$ ?

#### Solution

$T(\omega)$ compte les $B_i$ contenant $\omega$ ; $T(\omega)\geqslant1$ si et seulement si $\omega\in\bigcup B_i$. Les événements sont égaux, donc leurs probabilités aussi.

### Question 4. b)

> [!INDICATION]
> Une inégalité qui majore $P(Z\geqslant a)$ à l'aide de $E(Z)$, pour $Z$ positive.

#### Solution

Inégalité de Markov : si $Z\geqslant0$ admet une espérance, $P(Z\geqslant a)\leqslant\frac{E(Z)}a$ pour tout $a>0$.

Avec $Z=T$, $a=1$ et $E(T)=\sum P(B_i)$ (linéarité, $E(\mathbf 1_B)=P(B)$), on obtient l'inégalité de Boole.

> [!PIEGE]
> L'énoncé demande d'**énoncer précisément** l'inégalité : hypothèses (variable positive, espérance finie, $a>0$) comprises.

### Question 5. a)

> [!INDICATION]
> Majorer le terme général par une somme de deux termes de séries convergentes.

#### Solution

$|P(X=k)-P(Y=k)|\leqslant P(X=k)+P(Y=k)$, terme général d'une série convergente (de somme $2$) ; par comparaison de séries à termes positifs, la série converge.

### Question 5. b)

> [!INDICATION]
> Découper $[X=k]$ selon que $Y=k$ ou non.

#### Solution

$P(X=k)=P([X=k]\cap[Y=k])+P([X=k]\cap[Y\neq k])$ et $P([X=k]\cap[Y=k])\leqslant P(Y=k)$, d'où $P(X=k)-P(Y=k)\leqslant P([X=k]\cap[Y\neq k])$ ; le membre de gauche est la valeur absolue.

### Question 5. c)

> [!INDICATION]
> Deux cas, et la symétrie des rôles de $X$ et $Y$.

#### Solution

Si $P(X=k)\geqslant P(Y=k)$, 5. b) donne la majoration par le premier terme. Sinon, 5. b) avec $X$ et $Y$ échangés la donne par le second. Dans tous les cas, la somme des deux majore.

### Question 5. d)

> [!INDICATION]
> Sommer sur $k$ et reconnaître $P(X\neq Y)$ dans chacune des deux sommes.

#### Solution

Les $[X=k]\cap[Y\neq k]$ sont incompatibles et de réunion $[X\neq Y]$ ; de même pour $[X\neq k]\cap[Y=k]$. Donc $\delta(X,Y)\leqslant2P(X\neq Y)\leqslant2$.

> [!METHODE]
> Inégalité de couplage : $\delta(X,Y)\leqslant2P(X\neq Y)$. La distance entre deux lois est contrôlée par n'importe quel couplage.

---

## Partie 2 — Une inégalité d'après Hodge et Le Cam

On applique le couplage de la partie 1 à chaque $k$, et l'on somme avec l'inégalité de Boole. L'énoncé renvoie à « la question 2 de la partie 1 » pour la définition de $X$ et $Y$ : il s'agit de la question 3.

### Question 6.

> [!INDICATION]
> Majorer $\delta(S_n,T_n)$ sans calcul, puis minorer $4\sum p_k^2$ grâce à 2. c).

#### Solution

$\delta(S_n,T_n)\leqslant2$ (5. d)) et, si $p_k\geqslant\alpha\geqslant\frac1{\sqrt2}$, $4\sum p_i^2\geqslant4p_k^2\geqslant2$.

### Question 7.

> [!INDICATION]
> De quelles variables $X_k$ et $Y_k$ sont-elles fonctions ?

#### Solution

$X_k$ et $Y_k$ sont des fonctions de $U_k$ seule ; les $U_k$ étant indépendantes, le lemme des coalitions conclut.

### Question 8.

> [!INDICATION]
> Stabilité de la loi de Poisson ; loi de chaque $X_k$.

> [!INDICATION]
> Pour la limite, un résultat du cours sur $\mathcal B\left(n,\frac\lambda n\right)$.

#### Solution

$T_n\hookrightarrow\mathcal P(\lambda)$ par stabilité. $X_k\hookrightarrow\mathcal B(p_k)$ car $P(\beta_k<U_k\leqslant\beta_k+p_k)=p_k$ (avec $0<\beta_k$ et $\beta_k+p_k\leqslant1$).

Si $p_k=\frac\lambda n$ pour tout $k$, $S_n\hookrightarrow\mathcal B\left(n,\frac\lambda n\right)$, et $(S_n)$ converge en loi vers la loi $\mathcal P(\lambda)$.

> [!JURY]
> Question 8 parmi les plus pondérées (rapport 2025). Les trois réponses doivent être justifiées : indépendance (7), loi de chaque terme, résultat de cours invoqué.

### Question 9. a)

> [!INDICATION]
> Contraposée.

#### Solution

Si tous les $X_k(\omega)$ égalent les $Y_k(\omega)$, les sommes sont égales. Par contraposée, $[S_n\neq T_n]\subset\bigcup_k[X_k\neq Y_k]$.

### Question 9. b)

> [!INDICATION]
> Enchaîner 5. d), 9. a), 4. b) et 3. e) : vérifier que les hypothèses de 3. e) sont satisfaites.

#### Solution

$$\begin{aligned}
\delta(S_n,T_n)&\leqslant2P(S_n\neq T_n)\leqslant2\sum_{k=1}^nP(X_k\neq Y_k)\\
&\leqslant4\sum_{k=1}^np_k^2 .
\end{aligned}$$

La question 3. e) s'applique car $p_k<\alpha$.

> [!JURY]
> Le rapport 2025 : « Quand on utilise une question précédente, il faut l'invoquer précisément en citant son numéro (et pas « d'après une question précédente ») ». Ici, quatre questions sont mobilisées : on les cite toutes.

### Question 10.

> [!INDICATION]
> Identifier les lois de $S_n$ et $T_n$ (question 8), puis comparer la somme demandée à $\delta(S_n,T_n)$.

#### Solution

$S_n\hookrightarrow\mathcal B(n,\frac\lambda n)$, $T_n\hookrightarrow\mathcal P(\lambda)$. La somme demandée est formée des termes d'indices $0$ à $n$ de la série $\delta(S_n,T_n)$, qui est à termes positifs. Elle est donc au plus égale à $\delta(S_n,T_n)$, et par 9. b) :

$$\begin{aligned}
\delta(S_n,T_n)&\leqslant4\sum_{k=1}^n\left(\frac\lambda n\right)^2\\
&=\frac{4\lambda^2}n .
\end{aligned}$$

> [!METHODE]
> Cette inégalité quantifie l'approximation de la loi binomiale par la loi de Poisson : l'erreur totale est en $O\left(\frac1n\right)$. Contrôle numérique pour $\lambda=1{,}3$ et $n=50$ : somme $\approx0{,}014$ pour une borne $0{,}135$.

### Question 11. a)

> [!INDICATION]
> Se placer dans le cadre de la partie 2 avec $p_k=\frac1{n+k}$ : vérifier $p_k<\alpha$ et identifier $\lambda$.

> [!INDICATION]
> Majorer $\sum_k\frac1{(n+k)^2}$ grossièrement.

#### Solution

$p_k\leqslant\frac13<\alpha$, $\lambda=s_n$, et la loi de $S_n$ est celle de $\sum X_k$. Par 9. b) :

$$\delta(S_n,T_n)\leqslant4\sum_{k=1}^n\frac1{(n+k)^2}\leqslant\frac{4n}{(n+1)^2}\leqslant\frac4n .$$

Chaque terme $\left|P(S_n=k)-\frac{s_n^k}{k!}\mathrm e^{-s_n}\right|$ est au plus $\delta(S_n,T_n)$.

### Question 11. b)

> [!INDICATION]
> Encadrer $\frac1{n+t}$ par sa valeur en $k$ sur les intervalles $[k,k+1]$ et $[k-1,k]$.

#### Solution

Par décroissance de $t\mapsto\frac1{n+t}$ : $\frac1{n+t}\leqslant\frac1{n+k}$ sur $[k,k+1]$ et $\frac1{n+t}\geqslant\frac1{n+k}$ sur $[k-1,k]$ ; on intègre sur ces intervalles de longueur $1$.

### Question 11. c)

> [!INDICATION]
> Sommer, puis calculer les intégrales avec un logarithme.

> [!INDICATION]
> La relation de Chasles recolle les intégrales sur $[k,k+1]$ et sur $[k-1,k]$.

#### Solution

$\ln\frac{2n+1}{n+1}\leqslant s_n\leqslant\ln2$ ; le minorant tend vers $\ln2$ : $s_n\to\ln2$.

### Question 11. d)

> [!INDICATION]
> Inégalité triangulaire entre $P(S_n=k)$, $\frac{s_n^k}{k!}\mathrm e^{-s_n}$ et $\frac{(\ln2)^k}{k!}\mathrm e^{-\ln2}$.

#### Solution

$|P(S_n=k)-P(S=k)|\leqslant\frac4n+\left|\frac{s_n^k}{k!}\mathrm e^{-s_n}-\frac{(\ln2)^k}{k!}\mathrm e^{-\ln2}\right|\to0$ par continuité. Les variables sont à valeurs entières : $S_n$ converge en loi vers $S\hookrightarrow\mathcal P(\ln2)$.

> [!METHODE]
> Pour des variables à valeurs dans $\mathbb Z$, la convergence en loi se vérifie sur les $P(S_n=k)$, $k$ fixé ; une majoration uniforme en $k$ (ici $\frac4n$) suffit largement.

---

## Partie 3 — Étude du maximum d'une fonction

Analyse pure : régularité de $h$, signe de $g'$ grâce à une intégrale, encadrement de $\gamma$, puis développement en série de $g$.

### Question 12.

> [!INDICATION]
> Le seul point délicat est $0$ : continuité, dérivabilité, puis continuité de la dérivée.

> [!INDICATION]
> Utiliser le développement limité de $\mathrm e^x$ à l'ordre 2 en $0$.

#### Solution

Sur $]0,+\infty[$, $h$ est $\mathcal C^1$ et $h'(x)=\frac{(x-1)\mathrm e^x+1}{x^2}$. Avec $\mathrm e^x=1+x+\frac{x^2}2+x^2\varepsilon(x)$ :

- $h(x)=1+\frac x2+x\varepsilon(x)\to1$ : continuité en $0$ ;
- $\frac{h(x)-1}{x}=\frac12+\varepsilon(x)\to\frac12$ : $h'(0)=\frac12$ ;
- $h'(x)=\frac12+\frac x2+(x-1)\varepsilon(x)\to\frac12$ : $h'$ est continue en $0$.

$h$ est donc $\mathcal C^1$ sur $\mathbb{R}^+$.

> [!PIEGE]
> Montrer que $h'(x)$ a une limite en $0$ ne suffit pas à lui seul : il faut aussi la dérivabilité en $0$ (taux d'accroissement) et l'égalité de la limite avec $h'(0)$. Le rapport 2025 salue d'ailleurs « le soin pris par de très nombreux candidats à prouver la régularité d'une fonction avant de la dériver ou de l'intégrer ».

> [!JURY]
> Question 12 parmi les plus pondérées (rapport 2025).

### Question 13. a)

> [!INDICATION]
> Dériver le produit ; exprimer $h(x)$ à l'aide de $h(0)$ et d'une intégrale de $h'$.

#### Solution

$g'(x)=\mathrm e^{-x}\left(h(x)-\int_0^xh\right)$ et $h(x)=1+\int_0^xh'$ ($h$ est $\mathcal C^1$), d'où $g'(x)=\mathrm e^{-x}\left(1-\int_0^x(h-h')\right)$.

### Question 13. b)

> [!INDICATION]
> Réduire au même dénominateur $t^2$.

#### Solution

$h(t)-h'(t)=\frac{t(\mathrm e^t-1)-(t-1)\mathrm e^t-1}{t^2}=\frac{\mathrm e^t-1-t}{t^2}$.

### Question 13. c)

> [!INDICATION]
> Minorer $\mathrm e^t-1-t$ par un multiple de $t^2$ (étude de fonction).

> [!INDICATION]
> Ne pas oublier $t=0$, où l'on connaît $h(0)$ et $h'(0)$.

#### Solution

$\chi(t)=\mathrm e^t-1-t-\frac{t^2}2$ est nulle en $0$, de dérivée $\mathrm e^t-1-t\geqslant0$ (question 1) : $\chi\geqslant0$ sur $\mathbb R^+$.

Avec 13. b), $h(t)-h'(t)=\frac{\mathrm e^t-1-t}{t^2}\geqslant\frac12$ pour $t>0$ ; et en $0$, $h(0)-h'(0)=1-\frac12=\frac12$.

Donc $h-h'\geqslant\frac12>0$ sur $\mathbb R^+$, et par croissance de l'intégrale, $\int_0^x(h-h')\geqslant\frac x2\to+\infty$.

> [!METHODE]
> Pour montrer qu'une intégrale $\int_0^x\varphi$ tend vers $+\infty$, il suffit de minorer $\varphi$ par une constante strictement positive : c'est ce que fournit l'inégalité $\mathrm e^t\geqslant1+t+\frac{t^2}2$, qui resservira en 14. a).

> [!JURY]
> Question 13 c) parmi les plus pondérées (rapport 2025).

### Question 13. d)

> [!INDICATION]
> Le signe de $g'(x)$ est celui de $1-\int_0^x(h-h')$ : étudier cette fonction de $x$.

#### Solution

$G(x)=\int_0^x(h-h')$ est continue, strictement croissante, $G(0)=0$, $G\to+\infty$ : elle prend la valeur $1$ en un unique $\gamma>0$.

| $x$ | $0$ | | $\gamma$ | | $+\infty$ |
|---|---|---|---|---|---|
| $g'(x)$ | | $+$ | $0$ | $-$ | |
| $g$ | $0$ | croissante | $g(\gamma)$ | décroissante | |

$g$ atteint son maximum en $\gamma$ et seulement en $\gamma$.

> [!JURY]
> Question 13 d) parmi les plus pondérées (rapport 2025) : $\gamma$ doit apparaître dans le tableau, et l'unicité doit être justifiée (stricte monotonie de $G$).

### Question 14. a)

> [!INDICATION]
> La minoration vient de 13. c). Pour la majoration, étudier $t\mapsto\frac{t^2}2\mathrm e^t-\mathrm e^t+1+t$ en dérivant deux fois.

#### Solution

$\omega(t)=\frac{t^2}2\mathrm e^t-\mathrm e^t+1+t$ : $\omega''(t)=\left(2t+\frac{t^2}2\right)\mathrm e^t\geqslant0$, $\omega'(0)=0$, $\omega(0)=0$, donc $\omega'\geqslant0$ puis $\omega\geqslant0$.

D'où $\mathrm e^t-1-t\leqslant\frac{t^2}2\mathrm e^t$.

> [!METHODE]
> Pour comparer deux fonctions qui coïncident à l'ordre 1 en $0$, on dérive deux fois leur différence : signe de la dérivée seconde, puis dérivée nulle en $0$, puis fonction nulle en $0$.

### Question 14. b)

> [!INDICATION]
> Intégrer l'encadrement de 14. a) sur $[0,x]$, puis l'injecter dans 13. a).

#### Solution

$\frac x2\leqslant\int_0^x(h-h')\leqslant\frac{\mathrm e^x-1}2$, d'où $\mathrm e^{-x}\frac{3-\mathrm e^x}2\leqslant g'(x)\leqslant\mathrm e^{-x}\left(1-\frac x2\right)$.

### Question 14. c)

> [!INDICATION]
> Évaluer les deux bornes en des points où elles s'annulent.

#### Solution

$g'(\ln3)\geqslant0$ donc $\ln3\leqslant\gamma$ ; $g'(2)\leqslant0$ donc $\gamma\leqslant2$ (signe de $g'$ de part et d'autre de $\gamma$).

### Question 15. a)

> [!INDICATION]
> Pour $k\geqslant n+1$, comparer $\frac{x^k}{k!}$ à $\frac{x^n}{n!}\left(\frac{x}{n+1}\right)^{k-n}$.

> [!INDICATION]
> Sommer la série géométrique obtenue et utiliser $x\leqslant n$.

#### Solution

$\frac{x^k}{k!}=\frac{x^n}{n!}\cdot\frac{x^{k-n}}{(n+1)\cdots k}\leqslant\frac{x^n}{n!}\left(\frac x{n+1}\right)^{k-n}$. La série géométrique de raison $q=\frac x{n+1}<1$ vaut $\frac{x}{n+1-x}\leqslant x$, car $n+1-x\geqslant1$. D'où

$$\sum_{k=0}^n\frac{x^k}{k!}\leqslant\mathrm e^x\leqslant\sum_{k=0}^n\frac{x^k}{k!}+\frac{x^{n+1}}{n!}.$$

En retranchant $1$ et en divisant par $x>0$, on obtient l'encadrement de $h$ ; en $x=0$, les trois membres valent $1$.

> [!JURY]
> Question 15 a) parmi les plus pondérées (rapport 2025). Il s'agit d'une triple inégalité : chacune doit être justifiée.

### Question 15. b)

> [!INDICATION]
> Intégrer sur $[0,x]$, multiplier par $\mathrm e^{-x}$ ; pour la série, faire tendre $n$ vers $+\infty$ à $x$ fixé.

#### Solution

On intègre 15. a) sur $[0,x]$, avec $\int_0^x\frac{t^{k-1}}{k!}\,\mathrm dt=\frac{x^k}{k!\,k}$ et $\int_0^x\frac{t^n}{n!}\,\mathrm dt=\frac{x^{n+1}}{(n+1)!}$, puis on multiplie par $\mathrm e^{-x}$.

À $x$ fixé et $n\geqslant\max(1,x)$, l'écart entre $g(x)$ et la somme partielle $\mathrm e^{-x}\sum_{k=1}^n\frac{x^k}{k!\,k}$ est au plus $\mathrm e^{-x}\frac{x^{n+1}}{(n+1)!}$, qui tend vers $0$ (terme général de la série exponentielle).

Donc la série converge et $g(x)=\mathrm e^{-x}\sum_{k\geqslant1}\frac{x^k}{k!\,k}$.

> [!PIEGE]
> L'encadrement n'est valable que pour $x\in[0,n]$ : on fixe d'abord $x$, puis on prend $n\geqslant x$. Le rapport 2025 note que les quantificateurs « sont souvent négligés ou ignorés » : ici, leur ordre est essentiel.

### Question 16.

> [!INDICATION]
> Repérer ce que représentent `s` et `d` : une somme partielle de 15. b) et le majorant de l'erreur.

> [!INDICATION]
> Au passage de $n$ à $n+1$, comment obtenir le nouveau terme et le nouveau majorant à partir de `d` ?

#### Solution

```python
X = np.linspace(np.log(3), 2, 100)
Y = []
for x in X:
    n = 2; s = x + x**2/4; d = x**3/6
    while d * np.exp(-x) > 0.0001:
        n = n + 1
        s = s + d/n
        d = d*x/(n+1)
    Y.append(s*np.exp(-x))
plt.plot(X, Y)
plt.grid()
plt.show()
```

`s` vaut $\sum_{k=1}^n\frac{x^k}{k!\,k}$ et `d` vaut $\frac{x^{n+1}}{(n+1)!}$. Exécuté : écart à $g$ inférieur à $1{,}5\cdot10^{-5}$, maximum $\approx0{,}5173$ vers $x\approx1{,}50$, comme sur le graphique de l'énoncé.

---

## Partie 4 — Le problème du meilleur choix

On minore d'abord la probabilité de succès par $\frac1{\mathrm e}$ en général, puis, pour des $X_k$ de même loi, on calcule $r_n$ exactement en conditionnant par l'ensemble des indices qui dépassent le seuil.

### Question 17. a)

> [!INDICATION]
> Montrer une inclusion d'événements.

> [!INDICATION]
> Si un seul $X_k$ dépasse $s$, lequel la stratégie retient-elle, et est-ce le plus grand ?

#### Solution

Si un seul $X_{k_0}$ dépasse $s$, la stratégie le retient ($a_{n,s}=k_0$) et c'est le maximum : $[K_{n,s}=1]\subset[Y_{n,s}=Z_n]$.

### Question 17. b)

> [!INDICATION]
> $[K_{n,s}=1]$ : un indice au-dessus du seuil, tous les autres en dessous ; réunion disjointe sur l'indice.

#### Solution

$\theta=\prod_k(1-p_k)>0$, et

$$\begin{aligned}
P(K_{n,s}=1)&=\sum_{k=1}^np_k\prod_{i\neq k}(1-p_i)\\
&=\theta\sum_{k=1}^n\frac{p_k}{1-p_k}.
\end{aligned}$$

> [!JURY]
> Question 17 b) parmi les plus pondérées (rapport 2025). L'hypothèse $p_k\neq1$ sert ici, pour diviser par $1-p_k$.

### Question 17. c)

> [!INDICATION]
> Comparer $-\ln(1-p_k)$ et $\frac{p_k}{1-p_k}$ grâce à la question 1.

#### Solution

$-\ln(1-p_k)=\ln\left(1+\frac{p_k}{1-p_k}\right)\leqslant\frac{p_k}{1-p_k}$ ; en sommant, $-\ln\theta\leqslant\sum\frac{p_k}{1-p_k}$, puis on multiplie par $\theta>0$.

### Question 17. d)

> [!INDICATION]
> Pour quelle valeur de $\theta$ la quantité $-\theta\ln\theta$ vaut-elle $\frac1{\mathrm e}$ ?

> [!INDICATION]
> $\theta=F_n(s)$ : théorème des valeurs intermédiaires.

#### Solution

La fonction $\theta\mapsto-\theta\ln\theta$ vaut $\frac1{\mathrm e}$ en $\theta=\frac1{\mathrm e}$ (c'est d'ailleurs son maximum sur $]0,1]$).

$F_n$ est continue, de limites $0$ et $1$ : par le théorème des valeurs intermédiaires, il existe $s$ avec $F_n(s)=\frac1{\mathrm e}$.

Pour ce $s$, aucun $p_k$ ne vaut $1$ : sinon $F_{X_k}(s)=0$ et $F_n(s)=0$.

Alors $P(Y_{n,s}=Z_n)\geqslant\frac1{\mathrm e}$.

> [!METHODE]
> Règle pratique : choisir le seuil tel que la probabilité qu'**aucune** observation ne le dépasse soit $\frac1{\mathrm e}$. On gagne alors au moins une fois sur $\mathrm e$, quelles que soient les lois.

### Question 18. a)

> [!INDICATION]
> Fonction de répartition de la loi uniforme.

#### Solution

$1-F(s)=p\in\,]0,1[$ impose $s\in\,]0,1[$, où $F(s)=s$ : $s=1-p$.

### Question 18. b)

> [!INDICATION]
> Simuler les $n$ variables d'un coup, puis chercher le premier indice qui dépasse $s$, sans dépasser $n$.

#### Solution

```python
def simulCouple(n, p):
    s = 1 - p
    X = rd.random(n)
    Z = np.max(X)
    k = 1
    while k < n and X[k-1] <= s:
        k = k + 1
    Y = X[k-1]
    return (Z, Y)
```

> [!PIEGE]
> L'ordre des tests compte : `k < n and X[k-1] <= s` arrête la boucle à `k = n` même si $X_n\leqslant s$ ; c'est bien la règle « sinon, on garde le dernier ».

### Question 18. c)

> [!INDICATION]
> Fréquence empirique de l'événement $[Y_{10,s}=Z_{10}]$ sur un grand nombre de simulations.

#### Solution

```python
N = 10000
c = 0
for i in range(N):
    Z, Y = simulCouple(10, 0.15)
    if Y == Z:
        c = c + 1
print(c/N)
```

Exécuté avec $N=10^5$ : $0{,}560$, pour $r_{10}\approx0{,}5603$ (formule de 19. e)).

### Question 19. a)

> [!INDICATION]
> Écrire $P_{A_j}(X_i\leqslant x)$ comme un quotient et utiliser l'indépendance des $X_l$ sous $P$.

> [!INDICATION]
> Pour l'indépendance sous $P_{A_j}$, utiliser la caractérisation par des intervalles.

#### Solution

$P([X_i\leqslant x]\cap A_j)=P(s<X_i\leqslant x)\,p^{k-1}(1-p)^{n-k}$ et $P(A_j)=p^k(1-p)^{n-k}$, d'où la formule. Pour des intervalles $J_i$ :

$$P_{A_j}\left(\bigcap_{i\in I_j}[X_i\in J_i]\right)=\prod_{i\in I_j}\frac{P(X_i\in J_i\cap\,]s,+\infty[)}{p}=\prod_{i\in I_j}P_{A_j}(X_i\in J_i).$$

> [!JURY]
> Question 19 a) parmi les plus pondérées (rapport 2025). Le rapport conseille de prendre le temps d'assimiler les notions nouvelles : ici, conditionner par $A_j$ revient à « tronquer » chaque $X_i$ au-dessus de $s$.

### Question 19. b)

> [!INDICATION]
> $X_r$ est le maximum si et seulement si le maximum des autres lui est inférieur ; utiliser le résultat admis.

> [!INDICATION]
> Une primitive de $(F(t)-F(s))^{k-1}f(t)$ se lit directement.

#### Solution

Avec $W=\max_{i\neq r}X_i$, de fonction de répartition $G^{k-1}$ sous $P_{A_j}$ et indépendante de $X_r$ :

$$\begin{aligned}
P_{A_j}(W\leqslant X_r)&=\frac1{p^k}\int_s^{+\infty}(F(t)-F(s))^{k-1}f(t)\,\mathrm dt\\
&=\frac1{p^k}\cdot\frac{(1-F(s))^k}{k}=\frac1k .
\end{aligned}$$

> [!METHODE]
> Résultat attendu par symétrie : $k$ variables indépendantes de même loi à densité ont chacune la même chance $\frac1k$ d'être la plus grande. Le calcul le confirme.

### Question 19. c)

> [!INDICATION]
> Sur $A_j$, qui est $Y_{n,s}$ et qui est $Z_n$ ?

#### Solution

Les $A_j$ partitionnent $[K_{n,s}=k]$ : l'ensemble des indices où le seuil est dépassé est l'un des $I_j$, et un seul. D'où la somme.

Sur $A_j$, la stratégie retient $Y_{n,s}=X_{\min I_j}$, et le maximum est $Z_n=\max_{i\in I_j}X_i$ puisque les autres valeurs sont sous le seuil. Donc $P_{A_j}(Y_{n,s}=Z_n)=\frac1k$ par 19. b), avec $r=\min I_j$.

> [!METHODE]
> Décomposer selon une partition fine ($A_j$) sur laquelle tout se calcule, puis regrouper : c'est la formule des probabilités totales, appliquée en deux étages ($[K_{n,s}=k]$, puis les $A_j$).

### Question 19. d)

> [!INDICATION]
> Sur $[K_{n,s}=0]$, la stratégie garde $X_n$ ; refaire le raisonnement de 19. a) et 19. b) en conditionnant par « tous en dessous de $s$ ».

#### Solution

Sous $P_{A_0}$, les $X_i$ sont indépendantes de densité $\frac f{1-p}$ sur $]-\infty,s]$ ; $X_n$ est le maximum avec probabilité $\frac1{(1-p)^n}\cdot\frac{F(s)^n}{n}=\frac1n$.

D'où $P([Y_{n,s}=Z_n]\cap[K_{n,s}=0])=\frac1n(1-p)^n$.

### Question 19. e)

> [!INDICATION]
> Probabilités totales avec le système complet $([K_{n,s}=k])_{0\leqslant k\leqslant n}$.

#### Solution

$$r_n=\frac1n(1-p)^n+\sum_{k=1}^n\binom nk\frac{p^k(1-p)^{n-k}}{k}.$$

Vérifié par simulation pour $n\in\{3,7\}$ et $p\in\{0{,}2;\,0{,}5\}$ (écarts inférieurs à $0{,}004$).

> [!JURY]
> Question 19 e) parmi les plus pondérées. Le rapport 2025 met en garde : « Une assertion sans preuve mais avec beaucoup d'aplomb, ou une conclusion incohérente avec les calculs, ne font pas bon effet : le bluff ne paie pas. »

### Question 20. a)

> [!INDICATION]
> Quelle question de la partie 2 contient déjà presque cette inégalité ?

#### Solution

C'est la question 10 : la somme de $k=0$ à $n$ est au plus $\frac{4\lambda^2}n$ ; on retire le terme $k=0$ (positif) et l'on utilise $\frac1k\leqslant1$.

Comme $p=\frac\lambda n$ est une probabilité, $n>\lambda$ ; si $\alpha\leqslant\frac\lambda n<1$, la somme est au plus $2\leqslant4n\alpha^2\leqslant\frac{4\lambda^2}n$.

> [!PIEGE]
> Pour $n\leqslant\lambda$, $p=\frac\lambda n$ n'est plus une probabilité et l'inégalité de l'énoncé est fausse : avec $n=5$ et $\lambda=15$, la somme vaut environ $1\,211$, pour une borne $\frac{4\lambda^2}n=180$.
>
> L'énoncé suppose implicitement $n>\lambda$.

### Question 20. b)

> [!INDICATION]
> Comparer chaque morceau de $r_n$ (19. e)) à sa limite présumée.

#### Solution

Le premier terme vérifie $0\leqslant\frac1n\left(1-\frac\lambda n\right)^n\leqslant\frac1n$, donc tend vers $0$.

Par 20. a), la somme pondérée diffère de $\mathrm e^{-\lambda}\sum_{k=1}^n\frac{\lambda^k}{k!\,k}$ d'au plus $\frac{4\lambda^2}n$, qui tend vers $0$.

Enfin cette somme partielle converge vers la somme de la série (15. b)). D'où $r_n\to\mathrm e^{-\lambda}\sum_{k\geqslant1}\frac{\lambda^k}{k!\,k}$.

> [!METHODE]
> Schéma « à trois epsilons » : on intercale une quantité dont on connaît la limite, et l'on majore chaque écart par une suite qui tend vers $0$.

### Question 21.

> [!INDICATION]
> Reconnaître la limite comme une valeur de la fonction de la partie 3.

#### Solution

La limite vaut $g(\lambda)$ (15. b)), maximale pour $\lambda=\gamma$ et seulement pour cette valeur (13. d)).

On choisit donc $s$ tel que $P(X_k>s)=\frac\gamma n$, soit $F(s)=1-\frac\gamma n$.

La probabilité de retenir le maximum est alors environ $g(\gamma)\approx0{,}517$, avec $\gamma\approx1{,}50$ (graphique de la question 16).

> [!METHODE]
> Interprétation : il faut régler le seuil pour que, **en moyenne**, environ $\gamma\approx1{,}5$ observations le dépassent. On fait mieux que la garantie $\frac1{\mathrm e}\approx0{,}37$ de la question 17, car les lois sont connues et identiques.

---

## Bilan

**Méthodes à retenir.**

- Inégalités de convexité $\mathrm e^t\geqslant1+t$, $\ln(1+t)\leqslant t$, et études de fonctions (dérivée seconde si nécessaire).
- Simulation d'une loi discrète par inversion : $Y=\min\{k : U\leqslant F_Y(k)\}$.
- Couplage et inégalité $\delta(X,Y)\leqslant2P(X\neq Y)$ ; inégalité de Boole par l'inégalité de Markov.
- Approximation binomiale–Poisson quantifiée (Le Cam) : erreur au plus $4\sum p_k^2$.
- Régularité $\mathcal C^1$ en un point problématique par développement limité ; signe d'une dérivée exprimée par une intégrale.
- Encadrement du reste de la série exponentielle par une série géométrique.
- Conditionnement par une partition ($[K=k]$, puis les $A_j$) et symétrie entre variables indépendantes de même loi.
- Lecture critique d'un programme fourni : identifier ce que contient chaque variable avant de compléter les trous (question 16).

**Prérequis à revoir.** Théorème de la bijection ; développement limité de $\mathrm e^x$ à l'ordre 2 ; intégrale fonction de sa borne ; séries exponentielle et géométrique ; loi de Poisson et sa stabilité ; inégalité de Markov ; convergence en loi pour des variables entières ; dichotomie en Python.

**Questions transposables.** Problème du secrétaire (version classique : observer environ $\frac n{\mathrm e}$ candidats puis prendre le premier meilleur que tous les précédents, probabilité de succès $\to\frac1{\mathrm e}$) ; inégalité de Le Cam ; limite en loi d'un nombre de succès de probabilités $\frac1{n+k}$ (lien avec la série harmonique).
