# BCE ECT — Mathématiques T (conception ESCP) 2025 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Épreuve de 4 heures, sans document ni calculatrice (règle graduée seule autorisée). Trois exercices indépendants, 65 questions.

## Exercice 1

### Partie I) Division de la population en deux classes d'âge

**1.(a)** Calcul de $A^2$ :
$$A^2=\begin{pmatrix}\frac49+\frac19&\frac23+\frac23\\\frac2{27}+\frac2{27}&\frac19+\frac49\end{pmatrix}=\begin{pmatrix}\frac59&\frac43\\\frac4{27}&\frac59\end{pmatrix}.$$
Puis
$$A^2-\frac43A+\frac13I_2=\begin{pmatrix}\frac59-\frac89+\frac39&\frac43-\frac43\\\frac4{27}-\frac4{27}&\frac59-\frac89+\frac39\end{pmatrix}=\begin{pmatrix}0&0\\0&0\end{pmatrix}.$$
Le polynôme $X^2-\frac43X+\frac13$ est donc un polynôme annulateur de $A$.

**1.(b)** $X^2-\frac43X+\frac13=(X-1)\left(X-\frac13\right)$ (somme des racines $\frac43$, produit $\frac13$).

Toute valeur propre de $A$ est racine d'un polynôme annulateur : les valeurs propres possibles de $A$ sont **$1$ et $\frac13$**.

**1.(c)**
$$A\begin{pmatrix}3\\1\end{pmatrix}=\begin{pmatrix}2+1\\\frac13+\frac23\end{pmatrix}=\begin{pmatrix}3\\1\end{pmatrix},\qquad A\begin{pmatrix}3\\-1\end{pmatrix}=\begin{pmatrix}2-1\\\frac13-\frac23\end{pmatrix}=\frac13\begin{pmatrix}3\\-1\end{pmatrix}.$$
Ces deux vecteurs sont non nuls : $1$ et $\frac13$ sont valeurs propres de $A$. Avec la question 1.(b),
$$\boxed{\mathrm{Sp}(A)=\left\{1,\ \frac13\right\}}$$

**2.(a)**
$$PQ=\begin{pmatrix}3+3&9-9\\1-1&3+3\end{pmatrix}=6I_2.$$

**2.(b)** $P\left(\frac16Q\right)=I_2$ : $P$ est inversible et
$$\boxed{P^{-1}=\frac16Q=\frac16\begin{pmatrix}1&3\\1&-3\end{pmatrix}}$$

**2.(c)**
$$AP=\begin{pmatrix}3&1\\1&-\frac13\end{pmatrix},\qquad PD=\begin{pmatrix}3&1\\1&-\frac13\end{pmatrix}.$$
Donc $AP=PD$, et en multipliant à droite par $P^{-1}$, $A=PDP^{-1}$, soit $D=P^{-1}AP$ avec $D$ diagonale et $P$ inversible :

**$A$ est diagonalisable**.

**2.(d)** Pour $n=0$ : $PD^0P^{-1}=PP^{-1}=I_2=A^0$. Si $A^n=PD^nP^{-1}$ pour un $n\in\mathbb N$, alors
$$\begin{aligned}
A^{n+1}&=A^nA\\
&=PD^nP^{-1}PDP^{-1}\\
&=PD^{n+1}P^{-1}.
\end{aligned}$$
Par récurrence, $A^n=PD^nP^{-1}$ pour tout $n\in\mathbb N$.

**2.(e)** $D$ est diagonale : $D^n=\begin{pmatrix}1&0\\0&\left(\frac13\right)^n\end{pmatrix}$. Avec $P^{-1}=\frac16Q$ :
$$\begin{aligned}
A^n&=\frac16\begin{pmatrix}3&3\left(\frac13\right)^n\\1&-\left(\frac13\right)^n\end{pmatrix}\begin{pmatrix}1&3\\1&-3\end{pmatrix}\\
&=\frac16\begin{pmatrix}3+3\left(\frac13\right)^n&9-9\left(\frac13\right)^n\\1-\left(\frac13\right)^n&3+3\left(\frac13\right)^n\end{pmatrix}.
\end{aligned}$$
Comme $3\left(\frac13\right)^n=\left(\frac13\right)^{n-1}$ et $9\left(\frac13\right)^n=\left(\frac13\right)^{n-2}$, on obtient la formule de l'énoncé :
$$A^n=\frac16\begin{pmatrix}3+\left(\frac13\right)^{n-1}&9-\left(\frac13\right)^{n-2}\\1-\left(\frac13\right)^n&3+\left(\frac13\right)^{n-1}\end{pmatrix}.$$

**3.(a)** D'après le système (1), pour tout $n\in\mathbb N$ :
$$X_{n+1}=\begin{pmatrix}\frac23u_n+v_n\\\frac19u_n+\frac23v_n\end{pmatrix}=AX_n.$$

**3.(b)** Récurrence : $X_0=I_2X_0=A^0X_0$ ; si $X_n=A^nX_0$, alors $X_{n+1}=AX_n=A\,A^nX_0=A^{n+1}X_0$. Donc $X_n=A^nX_0$ pour tout $n\in\mathbb N$.

**3.(c)** Avec la question 2.(e), pour tout $n\in\mathbb N$ :
$$\boxed{\begin{aligned}u_n&=\frac16\left[\left(3+\left(\tfrac13\right)^{n-1}\right)u_0+\left(9-\left(\tfrac13\right)^{n-2}\right)v_0\right]\\v_n&=\frac16\left[\left(1-\left(\tfrac13\right)^{n}\right)u_0+\left(3+\left(\tfrac13\right)^{n-1}\right)v_0\right]\end{aligned}}$$

**3.(d)** Comme $0<\frac13<1$, $\left(\frac13\right)^n$, $\left(\frac13\right)^{n-1}$ et $\left(\frac13\right)^{n-2}$ tendent vers $0$. Donc
$$\begin{aligned}
\lim_{n\to+\infty}u_n&=\frac{3u_0+9v_0}6=\frac{u_0+3v_0}2,\\
\lim_{n\to+\infty}v_n&=\frac{u_0+3v_0}6.
\end{aligned}$$
Ces deux limites sont des réels strictement positifs ($u_0>0$, $v_0>0$) : chaque population tend vers un effectif fini non nul. Il n'y a ni extinction ni explosion : **la population survit**, avec à terme trois fois plus d'enfants que d'adultes.

**4.(a)** Dans un enclos, on ne trouve qu'une seule catégorie d'une seule espèce : chaque enclos correspond à une seule ligne de la table. L'attribut **`Enclos`** peut donc servir de clé primaire. `Espèce` ne convient pas (une espèce occupe au moins deux lignes, enfants et adultes), ni `Categorie`.

**4.(b)**
```sql
SELECT DISTINCT Type FROM ALIMENTATION;
```

**4.(c)**
```sql
SELECT Espèce FROM ANIMAUX
WHERE Categorie = 'adulte' AND Effectif >= 6;
```

**4.(d)** Le tarif est dans ALIMENTATION et l'effectif dans ANIMAUX : on fait une jointure sur l'espèce.
```sql
SELECT ANIMAUX.Espèce, ANIMAUX.Effectif
FROM ANIMAUX INNER JOIN ALIMENTATION ON ANIMAUX.Espèce = ALIMENTATION.Espèce
WHERE ALIMENTATION.Tarif < 15;
```

### Partie II) Croissance à taux fixe et croissance logistique

**5.(a)** Pour tout $n\in\mathbb N$, $w_{n+1}=w_n+rw_n=(1+r)w_n$ : $(w_n)$ est géométrique de raison $1+r$, et
$$\boxed{w_n=(1+r)^nw_0}$$

**5.(b)** La population ne peut pas perdre plus que son effectif entre deux instants : $w_{n+1}=(1+r)w_n$ doit rester positif ou nul, ce qui impose $1+r\geqslant0$, c'est-à-dire $r\geqslant-1$ (une baisse d'au plus $100\,\%$).

**5.(c)**

- Si $r\in[-1,0[$ : $0\leqslant1+r<1$, donc $(1+r)^n\to0$ et $w_n\to0$ :
  **extinction** (pour $r=-1$, $w_n=0$ dès $n=1$).
- Si $r=0$ : $w_n=w_0$ pour tout $n$ : la population est constante, **survie**.
- Si $r>0$ : $1+r>1$, donc $(1+r)^n\to+\infty$ et $w_n\to+\infty$ : **explosion**.

Le modèle n'est pas toujours réaliste : une croissance illimitée est impossible dans un milieu aux ressources finies, et le taux de variation ne reste pas constant quand la population devient grande. C'est l'objet du modèle logistique.

**6.(a)i.** Pour $x\in\mathbb R$ :
$$\begin{aligned}
&f(x)=0\\
\iff{}&\alpha x\left(1-\frac x\beta\right)=0\\
\iff{}&x=0\ \text{ou}\ x=\beta,
\end{aligned}$$
car $\alpha\neq0$. Les solutions sont $\boxed{0\text{ et }\beta}$.

**6.(a)ii.** $f(x)=\alpha x-\frac\alpha\beta x^2$ est un trinôme de coefficient dominant $-\frac\alpha\beta<0$, dérivable, de dérivée $f'(x)=\alpha\left(1-\frac{2x}\beta\right)$, positive sur $\left[0,\frac\beta2\right]$ et négative sur $\left[\frac\beta2,+\infty\right[$. Son maximum vaut $f\left(\frac\beta2\right)=\frac{\alpha\beta}4$.

En $+\infty$, $f(x)=x\left(\alpha-\frac\alpha\beta x\right)\to-\infty$.

| $x$ | $0$ | | $\frac\beta2$ | | $\beta$ | | $+\infty$ |
|---|---|---|---|---|---|---|---|
| $f'(x)$ | | $+$ | $0$ | $-$ | | $-$ | |
| $f$ | $0$ | ↗ | $\frac{\alpha\beta}4$ | ↘ | $0$ | ↘ | $-\infty$ |

**6.(b)i.** $g(x)=x\left(1+\alpha-\frac\alpha\beta x\right)$.

- $g(x)=0\iff x=0$ ou $x=\frac{(1+\alpha)\beta}\alpha$.
- $g(x)=x\iff f(x)=0\iff x=0$ ou $x=\beta$.
- $g(x)=\beta\iff\frac\alpha\beta x^2-(1+\alpha)x+\beta=0\iff x^2-\frac{(1+\alpha)\beta}\alpha x+\frac{\beta^2}\alpha=0$. Le réel $\beta$ est racine : $\beta^2-\frac{(1+\alpha)\beta^2}\alpha+\frac{\beta^2}\alpha=\beta^2\left(1-\frac1\alpha-1+\frac1\alpha\right)=0$. Le produit des racines vaut $\frac{\beta^2}\alpha$, donc l'autre racine est $\frac\beta\alpha$.

$$\boxed{\begin{aligned}g(x)=0&\iff x\in\left\{0,\ \tfrac{(\alpha+1)\beta}\alpha\right\}\\g(x)=x&\iff x\in\{0,\ \beta\}\\g(x)=\beta&\iff x\in\left\{\beta,\ \tfrac\beta\alpha\right\}\end{aligned}}$$

**6.(b)ii.** Comme $\beta>0$ et $\alpha>0$ :

- $\beta<\frac{(\alpha+1)\beta}{2\alpha}\iff2\alpha<\alpha+1\iff\alpha<1$, vrai ;
- $\frac{(\alpha+1)\beta}{2\alpha}<\frac\beta\alpha\iff\alpha+1<2\iff\alpha<1$, vrai ;
- $\frac\beta\alpha<\frac{(\alpha+1)\beta}\alpha\iff1<\alpha+1\iff\alpha>0$, vrai.

**6.(b)iii.** $g$ est un trinôme, $g'(x)=1+\alpha-\frac{2\alpha}\beta x$, qui s'annule en $x^*=\frac{(\alpha+1)\beta}{2\alpha}$ : $g$ est croissante sur $[0,x^*]$ et décroissante sur $[x^*,+\infty[$, de maximum
$$g(x^*)=x^*\left(1+\alpha-\frac{1+\alpha}2\right)=\frac{(\alpha+1)^2\beta}{4\alpha}.$$
En $+\infty$, $g(x)\to-\infty$ (coefficient dominant $-\frac\alpha\beta$). Avec l'ordre établi en 6.(b)ii :

| x | 0 | | β | | x* | | $\frac\beta\alpha$ | | $\frac{(\alpha+1)\beta}\alpha$ | | +∞ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $g$ | 0 | ↗ | β | ↗ | $\frac{(\alpha+1)^2\beta}{4\alpha}$ | ↘ | β | ↘ | 0 | ↘ | −∞ |

**6.(c)i.** Montrons par récurrence que $w_n\in\,]0,\beta]$ pour tout $n\in\mathbb N$, ce qui donne $w_n\in[0,\beta]$ pour tout $n\in\mathbb N^*$. C'est vrai pour $n=0$.

Si $w_n\in\,]0,\beta]$ : sur $[0,\beta]\subset[0,x^*]$, $g$ est strictement croissante, donc
$$g(0)<g(w_n)\leqslant g(\beta),$$
c'est-à-dire $0<w_{n+1}\leqslant\beta$.

**6.(c)ii.** Pour tout $n$, $w_n\in[0,\beta]$, et d'après le tableau de 6.(a)ii, $f\geqslant0$ sur $[0,\beta]$ : $f(w_n)\geqslant0$. Donc $w_{n+1}-w_n=f(w_n)\geqslant0$ :

**$(w_n)$ est croissante**.

**6.(c)iii.** $(w_n)$ est croissante et majorée par $\beta$ : par le théorème de la limite monotone, elle converge vers un réel $\ell$.

**6.(c)iv.** $(w_n)$ est croissante, donc $w_n\geqslant w_0$ pour tout $n$ ; par passage à la limite dans l'inégalité, $\ell\geqslant w_0$.

**6.(c)v.** $w_{n+1}=g(w_n)$ avec $w_n\to\ell$ : $g(w_n)=w_n+\alpha w_n-\frac\alpha\beta w_n^2$ tend vers $\ell+\alpha\ell-\frac\alpha\beta\ell^2=g(\ell)$ par opérations sur les limites (sommes et produits), et $w_{n+1}\to\ell$ ; par unicité de la limite, $\ell=g(\ell)$.

D'après 6.(b)i, $\ell\in\{0,\beta\}$. Comme $\ell\geqslant w_0>0$,
$$\boxed{\ell=\beta}$$
La population croît et se stabilise au niveau $\beta$ (capacité d'accueil du milieu) : **survie**.

**6.(d)i.** D'après 6.(b)iii, $g(x^*)=\frac{(\alpha+1)^2\beta}{4\alpha}$, et
$$\frac{(\alpha+1)^2\beta}{4\alpha}<\frac\beta\alpha\iff(\alpha+1)^2<4\iff\alpha+1<2,$$
vrai car $0<\alpha<1$.

Montrons par récurrence que $w_n\in\left[\beta,\frac\beta\alpha\right]$. C'est vrai pour $n=0$. Supposons $w_n\in\left[\beta,\frac\beta\alpha\right]$.

Sur cet intervalle, $g$ croît de $g(\beta)=\beta$ à $g(x^*)$ puis décroît jusqu'à $g\left(\frac\beta\alpha\right)=\beta$. Donc
$$\beta\leqslant g(w_n)\leqslant g(x^*)<\frac\beta\alpha,$$
et $w_{n+1}\in\left[\beta,\frac\beta\alpha\right]$.

**6.(d)ii.** Pour tout $n$, $w_n\geqslant\beta$, et $f\leqslant0$ sur $[\beta,+\infty[$ (question 6.(a)ii). Donc $w_{n+1}-w_n=f(w_n)\leqslant0$ : **$(w_n)$ est décroissante**.

**6.(d)iii.** $(w_n)$ est décroissante et minorée par $\beta$ : elle converge vers un réel $\ell\geqslant\beta$. Comme en 6.(c)v (opérations sur les limites et unicité de la limite), $\ell=g(\ell)$, donc $\ell\in\{0,\beta\}$, d'où $\boxed{\ell=\beta}$.

La population, trop nombreuse au départ, décroît et se stabilise au niveau $\beta$.

**6.(e)i.** Sur $\left[\frac\beta\alpha,\frac{(\alpha+1)\beta}\alpha\right]\subset[x^*,+\infty[$, $g$ est strictement décroissante, avec $g\left(\frac\beta\alpha\right)=\beta$ et $g\left(\frac{(\alpha+1)\beta}\alpha\right)=0$. Pour $w_0\in\left[\frac\beta\alpha,\frac{(\alpha+1)\beta}\alpha\right[$ :
$$0=g\left(\tfrac{(\alpha+1)\beta}\alpha\right)<g(w_0)\leqslant g\left(\tfrac\beta\alpha\right)=\beta,$$
donc $w_1\in\,]0,\beta]$.

**6.(e)ii.** La suite $(w_{n+1})_{n\in\mathbb N}$ vérifie la même relation de récurrence, avec un premier terme $w_1\in\,]0,\beta]$. D'après l'étude 6.(c), elle converge vers $\beta$. Donc $(w_n)$ converge et $\boxed{\lim w_n=\beta}$.

**6.(f)** Non. Si $w_0=\frac{(\alpha+1)\beta}\alpha$, alors $w_1=g(w_0)=0$, puis $w_n=0$ pour tout $n\geqslant1$ : la population s'éteint dès le premier instant.

Si $w_0>\frac{(\alpha+1)\beta}\alpha$, alors $w_1=g(w_0)<0$ : la « population » devient négative, ce qui n'a pas de sens (et $f$, $g$ ne sont définies que sur $\mathbb R^+$). Le modèle logistique n'est pertinent que pour $w_0<\frac{(\alpha+1)\beta}\alpha$.

## Exercice 2

On note qu'en position $0$ le pion avance toujours (toute bille est $>0$) et qu'en position $n$ il recule toujours (toute bille est $\leqslant n$).

**1.(a)**
```python
import numpy as np
import numpy.random as rd
def deplacement_pion(n,k):
        position = np.zeros(k+1)
        for j in range(0,k):
                bille = rd.randint(1,n+1)
                if position[j] < bille:
                        position[j+1] = position[j]+1
                else:
                        position[j+1] = position[j]-1
        return(position)
```
(`rd.randint(1,n+1)` tire un entier uniforme dans $[\![1,n]\!]$.)

**1.(b)**
```python
position = deplacement_pion(20,10)
print(position[10])
```

**1.(c)** `Test(10,100,1000)` simule $1000$ fois, de façon indépendante, $100$ déplacements avec $n=10$, et renvoie la moyenne des $1000$ positions finales obtenues.

C'est une moyenne empirique de $1000$ réalisations de $X_{100}$ : d'après la loi faible des grands nombres, $5{,}054$ est une **estimation de $E(X_{100})$**. Elle suggère que la position moyenne du pion après $100$ déplacements est proche de $5=\frac n2$, le milieu de l'axe (ce que confirme la question 9).

**2.** Initialement le pion est en $0$ ; toute bille a un numéro $\geqslant1>0$, donc il avance : $X_1=1$ est certaine.
$$\boxed{\begin{aligned}P(X_1=1)&=1\\E(X_1)&=1\end{aligned}}$$

**3.** En position $1$, le pion avance si la bille est $>1$ ($n-1$ billes sur $n$) et recule si la bille est $1$. Donc $X_2(\Omega)=\{0,2\}$ et
$$\begin{aligned}P(X_2=2)&=\frac{n-1}n\\P(X_2=0)&=\frac1n\end{aligned}.$$
$$\boxed{E(X_2)=2\cdot\frac{n-1}n=\frac{2(n-1)}n}$$

**4.** Montrons par récurrence que $X_k(\Omega)\subset[\![0,n]\!]$ pour tout $k\in\mathbb N$. C'est vrai pour $X_0=0$.

Supposons que $X_k$ prend ses valeurs dans $[\![0,n]\!]$.

- Lorsque $X_k=0$, le pion avance et $X_{k+1}=1$.
- Lorsque $X_k=n$, il recule et $X_{k+1}=n-1$.
- Lorsque $1\leqslant X_k\leqslant n-1$, $X_{k+1}=X_k\pm1\in[\![0,n]\!]$.

Donc $X_{k+1}(\Omega)\subset[\![0,n]\!]$.

**5.** Le pion ne peut arriver en $0$ que depuis la position $1$, en reculant, c'est-à-dire en tirant la bille $1$. Le tirage de l'étape $k+1$ est indépendant des précédents, donc
$$\begin{aligned}
P(X_{k+1}=0) &= P\big((X_k=1)\cap(\text{bille }1\text{ à l'étape }k+1)\big)\\
&= \frac1n\,P(X_k=1).
\end{aligned}$$
De même, le pion ne peut arriver en $n$ que depuis $n-1$, en avançant, c'est-à-dire en tirant la bille $n$ (seule bille $>n-1$). Donc $P(X_{k+1}=n)=\frac1n\,P(X_k=n-1)$.

**6.(a)** En position $\ell-1$, le pion avance si la bille tirée est strictement supérieure à $\ell-1$, c'est-à-dire parmi $\ell,\dots,n$ : $n-\ell+1$ billes sur $n$. La probabilité est $\boxed{\dfrac{n-\ell+1}n}$.

**6.(b)** En position $\ell+1$, le pion recule si la bille est inférieure ou égale à $\ell+1$ : $\ell+1$ billes sur $n$. La probabilité est $\boxed{\dfrac{\ell+1}n}$.

**6.(c)** Les événements $(X_k=j)$, $j\in[\![0,n]\!]$, forment un système complet (question 4). Le pion arrive en $\ell$ à l'étape $k+1$ si et seulement s'il était en $\ell-1$ et avance, ou s'il était en $\ell+1$ et recule ; ces deux cas sont incompatibles.

Le tirage de l'étape $k+1$ étant indépendant de la position $X_k$, les questions 6.(a) et 6.(b) donnent
$$\begin{aligned}P(X_{k+1}=\ell)={}&\frac{n-\ell+1}n\,P(X_k=\ell-1)\\&+\frac{\ell+1}n\,P(X_k=\ell+1).\end{aligned}$$

**7.** D'après la question 4, $E(X_{k+1})=\sum_{\ell=0}^n\ell\,P(X_{k+1}=\ell)$. Le terme $\ell=0$ est nul ; on utilise 6.(c) pour $1\leqslant\ell\leqslant n-1$ et 5 pour $\ell=n$ :
$$\begin{aligned}E(X_{k+1})={}&\sum_{\ell=1}^{n-1}\ell\,\frac{n-\ell+1}nP(X_k=\ell-1)\\&+\sum_{\ell=1}^{n-1}\ell\,\frac{\ell+1}nP(X_k=\ell+1)\\&+n\cdot\frac1nP(X_k=n-1).\end{aligned}$$
On pose $j=\ell-1$ dans la première somme et $j=\ell+1$ dans la seconde. Le dernier terme est le terme $j=n-1$ de la première somme, car $(j+1)(n-j)=n$ pour $j=n-1$.

On ajoute aussi les termes nuls $j=n$ de la première somme ($(n+1)\cdot0=0$) et $j=0$, $j=1$ de la seconde ($(j-1)j=0$) :
$$\begin{aligned}
E(X_{k+1})&=\sum_{j=0}^n\frac{(j+1)(n-j)}nP(X_k=j)+\sum_{j=0}^n\frac{(j-1)j}nP(X_k=j)\\
&=\sum_{j=0}^n\frac{(j+1)(n-j)+j(j-1)}nP(X_k=j).
\end{aligned}$$
Or $(j+1)(n-j)+j(j-1)=nj+n-2j$, donc $\frac{(j+1)(n-j)+j(j-1)}n=1+\left(1-\frac2n\right)j$. Comme $\sum_jP(X_k=j)=1$ :
$$E(X_{k+1})=1+\left(1-\frac2n\right)E(X_k).$$

**8.(a)** $(E(X_m))_{m\geqslant n}$ est une **suite arithmético-géométrique** : $E(X_{m+1})=\left(1-\frac2n\right)E(X_m)+1$.

**8.(b)** $x=1+\left(1-\frac2n\right)x\iff\frac2nx=1\iff\boxed{x=\frac n2}$

**8.(c)** En soustrayant $x=1+\left(1-\frac2n\right)x$ à la relation de la question 7 :
$$x_{k+1}=\left(1-\frac2n\right)x_k.$$
La suite $(x_k)_{k\geqslant n}$ est géométrique de raison $1-\frac2n$, donc pour tout $k\geqslant n$ :
$$x_k=\left(1-\frac2n\right)^{k-n}x_n=\left(1-\frac2n\right)^{k-n}\left(E(X_n)-\frac n2\right).$$

**8.(d)** Pour tout $k\geqslant n$ :
$$\boxed{E(X_k)=\frac n2+\left(1-\frac2n\right)^{k-n}\left(E(X_n)-\frac n2\right)}$$

**9.** Comme $n\geqslant2$, $0\leqslant1-\frac2n<1$, donc $\left(1-\frac2n\right)^{k-n}\xrightarrow[k\to+\infty]{}0$ (pour $n=2$, ce terme est nul dès $k>n$). Donc
$$\boxed{\lim_{k\to+\infty}E(X_k)=\frac n2}$$
Au bout d'un grand nombre de déplacements, la position moyenne du pion est le milieu de l'axe. C'est cohérent avec la valeur $5{,}054\approx5$ obtenue pour $n=10$ à la question 1.(c).

## Exercice 3

### Partie I) Premier cas particulier : $f_0$ est une fonction puissance sur $[0,1]$

**1.** $f_0$ est positive ($t^\alpha\geqslant0$ sur $[0,1]$), continue sur $\mathbb R$ sauf peut-être en $0$ et en $1$, et
$$\begin{aligned}
\int_{-\infty}^{+\infty}f_0(t)\,dt &= \int_0^1(\alpha+1)t^\alpha\,dt\\
&= \Big[t^{\alpha+1}\Big]_0^1\\
&= 1.
\end{aligned}$$
$f_0$ est une densité de probabilité.

**2.(a)** Sur $]0,1[$, $f_0(t)=(\alpha+1)t^\alpha$ est dérivable et $f_0'(t)=\alpha(\alpha+1)t^{\alpha-1}$.

- En $1^-$ : $f_0'(t)\to\alpha(\alpha+1)$, limite finie.
- En $0^+$, si $\alpha>1$ : $t^{\alpha-1}\to0$ et $f_0'(t)\to0$.
- En $0^+$, si $\alpha=1$ : $f_0'(t)=2$ pour tout $t$.
  La limite est finie dans les deux cas (c'est là que sert $\alpha\geqslant1$).

$f_0$ est donc dérivable sur $[0,1]$ au sens de l'énoncé, avec $f_0'(t)=\alpha(\alpha+1)t^{\alpha-1}$ pour $t\in\,]0,1]$.

En $0$, la dérivée vaut $0$ si $\alpha>1$ et $2$ si $\alpha=1$.

**2.(b)** Montrons par récurrence que $f_n=\alpha^nf_0$ (et donc que $f_n$ est dérivable sur $[0,1]$ au sens de l'énoncé). Pour $n=0$, c'est immédiat.

Si $f_n=\alpha^nf_0$, alors $f_n'=\alpha^nf_0'$ sur $[0,1]$, et pour $t\in[0,1]$ :

- si $t\in\,]0,1]$ : $f_{n+1}(t)=t\,\alpha^n\alpha(\alpha+1)t^{\alpha-1}=\alpha^{n+1}(\alpha+1)t^\alpha=\alpha^{n+1}f_0(t)$ ;
- si $t=0$ : $f_{n+1}(0)=0\cdot f_n'(0)=0=\alpha^{n+1}f_0(0)$.

Hors de $[0,1]$, $f_{n+1}=0=\alpha^{n+1}f_0$. Donc $f_{n+1}=\alpha^{n+1}f_0$ sur $\mathbb R$.

**2.(c)** $\alpha^n>0$. Avec $\boxed{c_n=\dfrac1{\alpha^n}}$, $c_nf_n=f_0$ est une densité de probabilité.

**2.(d)** $X_n$ admet pour densité $c_nf_n=f_0$, qui est aussi une densité de $X_0$. Deux variables à densité de même densité ont la même fonction de répartition : $X_n$ et $X_0$ ont la même loi.

**3.** $F_{X_\alpha}(x)=\int_{-\infty}^xf_0(t)\,dt$.

- Si $x\leqslant0$ : $F_{X_\alpha}(x)=0$.
- Si $x\in\,]0,1]$ : $F_{X_\alpha}(x)=\int_0^x(\alpha+1)t^\alpha\,dt=x^{\alpha+1}$.
- Si $x>1$ : $F_{X_\alpha}(x)=\int_0^1(\alpha+1)t^\alpha\,dt=1$.

**4.** $tf_0(t)$ et $t^2f_0(t)$ sont nulles hors de $[0,1]$ et continues sur $[0,1]$ : les intégrales convergent, $X_\alpha$ admet une espérance et un moment d'ordre 2.
$$\begin{aligned}
E(X_\alpha)&=\int_0^1(\alpha+1)t^{\alpha+1}\,dt=\frac{\alpha+1}{\alpha+2},\\
E(X_\alpha^2)&=\int_0^1(\alpha+1)t^{\alpha+2}\,dt=\frac{\alpha+1}{\alpha+3}.
\end{aligned}$$
Par Koenig-Huygens, et comme $(\alpha+2)^2-(\alpha+1)(\alpha+3)=1$ :
$$\begin{aligned}
V(X_\alpha)&=\frac{\alpha+1}{\alpha+3}-\frac{(\alpha+1)^2}{(\alpha+2)^2}\\
&=\frac{(\alpha+1)\left[(\alpha+2)^2-(\alpha+1)(\alpha+3)\right]}{(\alpha+3)(\alpha+2)^2}\\
&=\frac{\alpha+1}{(\alpha+3)(\alpha+2)^2}.
\end{aligned}$$

### Partie II) Second cas particulier : $f_0$ est une fonction exponentielle sur $[0,1]$

**5.** $\int_0^1e^t\,dt=e-1>0$. Avec $\boxed{c_0=\dfrac1{e-1}}$, $c_0f_0$ est positive, continue sauf en $0$ et $1$, d'intégrale $1$ : c'est une densité de probabilité.

**6.** $tc_0f_0(t)$ est nulle hors de $[0,1]$ et continue sur $[0,1]$ : $X_0$ admet une espérance.

Par intégration par parties ($u(t)=t$, $v(t)=e^t$ ;

$u$, $v$, $u'$, $v'$ continues sur $[0,1]$) :
$$\begin{aligned}
\int_0^1te^t\,dt &= \Big[te^t\Big]_0^1-\int_0^1e^t\,dt\\
&= e-(e-1)\\
&= 1.
\end{aligned}$$
$$\boxed{E(X_0)=\frac1{e-1}}$$

**7.** D'après les résultats admis, $f_n$ est dérivable sur $[0,1]$ et $f_n'$ est continue sur $[0,1]$. Par intégration par parties avec $u(t)=t$ et $v=f_n$ :
$$\begin{aligned}
\int_0^1f_{n+1}(t)\,dt&=\int_0^1tf_n'(t)\,dt\\
&=\Big[tf_n(t)\Big]_0^1-\int_0^1f_n(t)\,dt\\
&=f_n(1)-\int_0^1f_n(t)\,dt.
\end{aligned}$$

**8.** Récurrence. Pour $n=0$ : $f_0(t)=e^t=P_0(t)e^t$ sur $[0,1]$. Supposons $f_n(t)=P_n(t)e^t$ sur $[0,1]$.

Cette fonction est dérivable sur $\mathbb R$, de dérivée $(P_n'(t)+P_n(t))e^t$, continue ; les limites en $0^+$ et $1^-$ de $f_n'$ sont donc les valeurs de cette expression. Pour $t\in[0,1]$ :
$$\begin{aligned}
f_{n+1}(t) &= tf_n'(t)\\
&= t\left(P_n'(t)+P_n(t)\right)e^t\\
&= P_{n+1}(t)e^t.
\end{aligned}$$
Donc $f_n(t)=P_n(t)e^t$ pour tout $n\in\mathbb N$ et tout $t\in[0,1]$.

**9.** Avec la question 8 et la définition de $P_{n+1}$ :
$$\begin{aligned}
f_{n+1}(1)&=P_{n+1}(1)\,e=\left(P_n'(1)+P_n(1)\right)e\\
&=f_n(1)+eP_n'(1).
\end{aligned}$$
Comme $P_n'(1)\geqslant0$ (résultat admis), $f_{n+1}(1)\geqslant f_n(1)$.

**10.** Notons $J_n=\int_0^1f_n(t)\,dt$ et montrons par récurrence que $0<J_n<f_n(1)$.

- $n=0$ : $J_0=e-1$ et $f_0(1)=e$, donc $0<J_0<f_0(1)$.
- Si $0<J_n<f_n(1)$, la question 7 donne $J_{n+1}=f_n(1)-J_n>0$, et $J_{n+1}<f_n(1)\leqslant f_{n+1}(1)$ (question 9).

Donc $0<\int_0^1f_n(t)\,dt<f_n(1)$ pour tout $n\in\mathbb N$.

**11.** Posons
$$\boxed{c_n=\frac1{\int_0^1f_n(t)\,dt}}$$
réel strictement positif d'après la question 10.

La fonction $c_nf_n$ vérifie les trois conditions :

- elle est positive : sur $[0,1]$, $f_n(t)=P_n(t)e^t\geqslant0$ car $P_n\geqslant0$, et elle est nulle ailleurs ;
- elle est continue sur $\mathbb R$ sauf peut-être en $0$ et en $1$, car $f_n$ est continue sur $[0,1]$ ;
- son intégrale vaut $c_n\int_0^1f_n(t)\,dt=1$.

C'est une densité de probabilité.

**FIN**
