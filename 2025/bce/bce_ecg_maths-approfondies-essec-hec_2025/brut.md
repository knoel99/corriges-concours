# BCE ECG — Maths approfondies (ESSEC-HEC) 2025 · Corrigé brut

*Corrigé rédigé par IA, non officiel. Signalez toute erreur.*

Épreuve de mathématiques approfondies, conception ESSEC BS – HEC Paris, voie générale, 4 heures, calculatrice interdite. Trois parties, 46 questions (sous-questions comprises).

**Convention.** Dans les parties II et III, on applique la partie I avec $E=\mathcal{M}_{p,1}(\mathbb{R})$ et $F=\mathcal{M}_{n,1}(\mathbb{R})$ munis de leurs produits scalaires canoniques, pour lesquels les bases canoniques sont orthonormales, et avec $u:X\mapsto AX$.

Alors $\ker u=\ker(A)$, $\operatorname{Im}u=\operatorname{Im}(A)$ et, d'après la question 4, $u^*:Y\mapsto {}^tAY$, donc $\operatorname{Im}u^*=\operatorname{Im}({}^tA)$ et $u^*\circ u:X\mapsto MX$.

---

## Partie I : autour de l'adjoint

### 1.

*Unicité.* Si $a_0$ et $a_0'$ conviennent, alors pour tout $x\in E$ :

$$\langle a_0-a_0',x\rangle_E=\ell(x)-\ell(x)=0.$$

Avec $x=a_0-a_0'$, on obtient $\|a_0-a_0'\|^2=0$, donc $a_0=a_0'$.

*Existence.* On pose $a_0=\sum_{i=1}^{p}\ell(e_i)\,e_i$. La base $\mathscr{B}_E$ étant orthonormale, pour tout $j\in\llbracket 1,p\rrbracket$ :

$$\begin{aligned}
\langle a_0,e_j\rangle_E&=\sum_{i=1}^{p}\ell(e_i)\langle e_i,e_j\rangle_E\\
&=\ell(e_j).
\end{aligned}$$

Les applications $\ell$ et $x\mapsto\langle a_0,x\rangle_E$ sont linéaires (bilinéarité du produit scalaire) et coïncident sur la base $\mathscr{B}_E$ : elles sont égales.

**Il existe un unique $a_0\in E$ tel que $\ell(x)=\langle a_0,x\rangle_E$ pour tout $x\in E$.**

### 2.

Soit $y\in F$. L'application $\ell_y:x\mapsto\langle u(x),y\rangle_F$ est une forme linéaire sur $E$ : composée de l'application linéaire $u$ et de la forme linéaire $z\mapsto\langle z,y\rangle_F$.

La question 1 appliquée à $\ell_y$ donne **un unique $z_y\in E$ tel que $\langle u(x),y\rangle_F=\langle z_y,x\rangle_E$ pour tout $x\in E$.**

### 3.

Soient $y,y'\in F$ et $\lambda\in\mathbb{R}$. Pour tout $x\in E$ :

$$\begin{aligned}
\langle u(x),y+\lambda y'\rangle_F&=\langle u(x),y\rangle_F+\lambda\langle u(x),y'\rangle_F\\
&=\langle z_y,x\rangle_E+\lambda\langle z_{y'},x\rangle_E\\
&=\langle z_y+\lambda z_{y'},x\rangle_E.
\end{aligned}$$

Le vecteur $z_y+\lambda z_{y'}$ vérifie la propriété qui caractérise $z_{y+\lambda y'}$ ; par l'unicité de la question 2, $z_{y+\lambda y'}=z_y+\lambda z_{y'}$. **L'application $u^*$ est linéaire.**

### 4.

Les bases étant orthonormales, le coefficient $(i,j)$ de $\operatorname{Mat}_{\mathscr{B}_E,\mathscr{B}_F}(u^*)$ est la $i$-ième coordonnée de $u^*(f_j)$ dans $\mathscr{B}_E$, c'est-à-dire :

$$\langle u^*(f_j),e_i\rangle_E=\langle u(e_i),f_j\rangle_F=A_{j,i}.$$

$$\boxed{\operatorname{Mat}_{\mathscr{B}_E,\mathscr{B}_F}(u^*)={}^tA.}$$

Une matrice et sa transposée ont même rang, donc $\operatorname{rg}(u^*)=\operatorname{rg}({}^tA)=\operatorname{rg}(A)=\operatorname{rg}(u)$.

L'application $u^*:F\to E$ a pour matrice ${}^tA$ dans les bases orthonormales $\mathscr{B}_F$ et $\mathscr{B}_E$.

Le résultat précédent, appliqué à $u^*$, montre que $(u^*)^*:E\to F$ a pour matrice ${}^t({}^tA)=A$ dans $\mathscr{B}_E$ et $\mathscr{B}_F$. Deux applications linéaires de même matrice dans les mêmes bases sont égales : **$(u^*)^*=u$.**

### 5.

*Inclusion.* Soient $x\in\ker(u)$ et $y\in F$ :

$$\langle x,u^*(y)\rangle_E=\langle u(x),y\rangle_F=0.$$

Donc tout vecteur de $\operatorname{Im}(u^*)$ est orthogonal à $\ker(u)$ : $\operatorname{Im}(u^*)\subset\ker(u)^\perp$.

*Dimensions.* Par la question 4 et le théorème du rang :

$$\begin{aligned}
\dim\operatorname{Im}(u^*)&=\operatorname{rg}(u)\\
&=p-\dim\ker(u)\\
&=\dim\ker(u)^\perp.
\end{aligned}$$

**Donc $\operatorname{Im}(u^*)=\ker(u)^\perp$.**

### 6.

Si $u(x)=0$, alors $u^*(u(x))=0$ : $\ker(u)\subset\ker(u^*\circ u)$. Réciproquement, si $u^*(u(x))=0$ :

$$\begin{aligned}
\|u(x)\|_F^2&=\langle u(x),u(x)\rangle_F\\
&=\langle x,u^*(u(x))\rangle_E\\
&=0,
\end{aligned}$$

donc $u(x)=0$. **Ainsi $\ker(u^*\circ u)=\ker(u)$.**

On a $\operatorname{Im}(u^*\circ u)\subset\operatorname{Im}(u^*)$. Par le théorème du rang appliqué à $u^*\circ u$ (endomorphisme de $E$) et à $u$, puis la question 4 :

$$\begin{aligned}
\operatorname{rg}(u^*\circ u)&=p-\dim\ker(u)\\
&=\operatorname{rg}(u)\\
&=\operatorname{rg}(u^*).
\end{aligned}$$

Inclusion et égalité des dimensions donnent **$\operatorname{Im}(u^*\circ u)=\operatorname{Im}(u^*)$.**

### 7.

L'application $w$ est bien définie, car $u^*\circ u(x)\in\operatorname{Im}(u^*)$ pour tout $x$, et linéaire comme restriction de $u^*\circ u$. C'est donc un endomorphisme de $\operatorname{Im}(u^*)$.

Elle est injective : par les questions 5 et 6,

$$\begin{aligned}
\ker(w)&=\ker(u^*\circ u)\cap\operatorname{Im}(u^*)\\
&=\ker(u)\cap\ker(u)^\perp\\
&=\{0\}.
\end{aligned}$$

Un endomorphisme injectif d'un espace de dimension finie est bijectif : **$w$ est un isomorphisme de $\operatorname{Im}(u^*)$.**

*Interprétation matricielle.* Avec $E=\mathbb{R}^p$, $F=\mathbb{R}^n$ et leurs bases canoniques (convention en tête), $u^*\circ u$ a pour matrice $M={}^tAA$ et $\operatorname{Im}(u^*)=\operatorname{Im}({}^tA)$.

**Pour tout $b\in\operatorname{Im}({}^tA)$, en particulier pour $b={}^tAY$ avec $Y\in\mathcal{M}_{n,1}(\mathbb{R})$, l'équation $MX=b$ admet une unique solution $X$ dans $\operatorname{Im}({}^tA)$.**

### 8.

**(a)** Montrons d'abord que $\operatorname{Im}(u)^\perp=\ker(u^*)$. Pour $y\in F$ :

$$\begin{aligned}
y\in\operatorname{Im}(u)^\perp&\iff\forall x\in E,\ \langle u(x),y\rangle_F=0\\
&\iff\forall x\in E,\ \langle x,u^*(y)\rangle_E=0\\
&\iff u^*(y)=0.
\end{aligned}$$

Soit $y\in F$. Comme $\pi$ est le projecteur orthogonal sur $\operatorname{Im}(u)$, $y-\pi(y)\in\operatorname{Im}(u)^\perp=\ker(u^*)$, donc $u^*(\pi(y))=u^*(y)$. Ainsi $u^*\circ\pi=u^*$.

En passant aux matrices dans $\mathscr{B}_F$ et $\mathscr{B}_E$ :

$$\boxed{{}^tAQ={}^tA.}$$

**(b)** Soit $r=\operatorname{rg}(u)=\dim\operatorname{Im}(u)$.

Dans une base de $F$ obtenue en concaténant une base de $\operatorname{Im}(u)$ et une base de $\operatorname{Im}(u)^\perp$, la matrice de $\pi$ est $\begin{pmatrix}I_r&0\\0&0\end{pmatrix}$, de trace $r$.

La trace est invariante par changement de base, donc **$\operatorname{Tr}(Q)=\operatorname{rg}(u)$.**

### 9.

D'après la convention, $M$ est la matrice de $u^*\circ u$ dans la base canonique de $\mathbb{R}^p$. Donc :

$$\begin{aligned}
M\text{ inversible}&\iff\ker(u^*\circ u)=\{0\}\\
&\iff\ker(u)=\{0\}\\
&\iff\operatorname{rg}(A)=p,
\end{aligned}$$

par la question 6 puis le théorème du rang ($\dim E=p$). **$M$ est inversible si et seulement si $\operatorname{rg}(A)=p$.**

### 10.

**(a)** Par la question 9, $M$ est inversible. Posons $P=AM^{-1}\,{}^tA\in\mathcal{M}_n(\mathbb{R})$ et soit $Y\in\mathcal{M}_{n,1}(\mathbb{R})$. D'une part $PY=A\big(M^{-1}\,{}^tAY\big)\in\operatorname{Im}(A)$. D'autre part :

$$\begin{aligned}
{}^tA(Y-PY)&={}^tAY-({}^tAA)M^{-1}\,{}^tAY\\
&={}^tAY-{}^tAY\\
&=0,
\end{aligned}$$

donc $Y-PY\in\ker({}^tA)=\operatorname{Im}(A)^\perp$ (question 8(a)).

Ainsi $Y=PY+(Y-PY)$ avec $PY\in\operatorname{Im}(A)$ et $Y-PY\in\operatorname{Im}(A)^\perp$.

Donc $PY$ est le projeté orthogonal de $Y$ sur $\operatorname{Im}(A)$, c'est-à-dire $QY$.

Ceci pour tout $Y$ :

$$\boxed{Q=A\,M^{-1}\,{}^tA.}$$

**(b)**

```python
def Calcule_Q(A):
    n, p = np.shape(A)
    if al.matrix_rank(A) != p:
        print("Erreur : A n'est pas de rang p")
        return None
    M = np.dot(np.transpose(A), A)
    return np.dot(np.dot(A, al.inv(M)), np.transpose(A))
```


### 11.

Pour tout $X\in\mathcal{M}_{p,1}(\mathbb{R})$ :

$$\begin{aligned}
{}^tXMX&={}^tX\,{}^tA\,AX\\
&={}^t(AX)(AX)\\
&=\|AX\|^2\\
&\geqslant 0.
\end{aligned}$$

---

## Partie II : minimisation d'une fonction quadratique

### 12.

Soient $X,H\in\mathcal{M}_{p,1}(\mathbb{R})$. En développant le carré de la norme :

$$\begin{aligned}
J_0(X+H)-J_0(X)&=\tfrac12\|(AX-Y)+AH\|^2-\tfrac12\|AX-Y\|^2\\
&=\langle AX-Y,AH\rangle+\tfrac12\|AH\|^2\\
&=\langle {}^tA(AX-Y),H\rangle+\tfrac12\,{}^tH\,{}^tAAH\\
&=\langle D(X),H\rangle+\tfrac12\,{}^tHMH,
\end{aligned}$$

car ${}^tA(AX-Y)=MX-{}^tAY=D(X)$. C'est l'identité (2).

### 13.

*Si $D(X)=0$* : pour tout $H$, (2) et la question 11 donnent $J_0(X+H)-J_0(X)=\tfrac12\,{}^tHMH\geqslant0$. Comme tout $X'$ s'écrit $X+H$, $J_0(X)$ est un minimum global.

*Réciproquement*, supposons que $J_0$ admette en $X$ un minimum global. Pour $t\in\mathbb{R}$, avec $H=tD(X)$ dans (2) :

$$\begin{aligned}
0&\leqslant J_0(X+tD(X))-J_0(X)\\
&=t\|D(X)\|^2+\tfrac{t^2}{2}c,
\end{aligned}$$

où $c={}^tD(X)MD(X)$.

Pour $t<0$, on divise par $t$ : $\|D(X)\|^2+\tfrac t2 c\leqslant 0$.

En faisant tendre $t$ vers $0^-$, $\|D(X)\|^2\leqslant0$, donc $D(X)=0$.

**$J_0$ admet un minimum global en $X$ si et seulement si $D(X)=0$.**

### 14.

Pour $X\in\mathcal{M}_{p,1}(\mathbb{R})$, $D(X)=0$ équivaut à $MX={}^tAY$. Par la question 5 (convention en tête), $\ker(A)^\perp=\operatorname{Im}(u^*)=\operatorname{Im}({}^tA)$. Donc :

$$\mathbb{S}_0\cap\ker(A)^\perp=\{X\in\operatorname{Im}({}^tA)\ |\ w(X)={}^tAY\}.$$

Comme ${}^tAY\in\operatorname{Im}({}^tA)$ et que $w$ est une bijection de $\operatorname{Im}({}^tA)$ (question 7), cet ensemble contient exactement un élément $X_0=w^{-1}({}^tAY)$. **Il existe $X_0\in\ker(A)^\perp$ tel que $\mathbb{S}_0\cap\ker(A)^\perp=\{X_0\}$.**

### 15.

**(a)** Si $X\in\mathbb{S}_0$, alors ${}^tA(AX-Y)=D(X)=0$, donc $Y-AX\in\ker({}^tA)=\operatorname{Im}(A)^\perp$ (question 8(a)).

L'écriture $Y=AX+(Y-AX)$ décompose $Y$ selon $\operatorname{Im}(A)\oplus\operatorname{Im}(A)^\perp$ : $AX$ est le projeté orthogonal de $Y$ sur $\operatorname{Im}(A)$.

Donc $AX=QY$, c'est (3).

**(b)** $X$ et $X_0$ sont dans $\mathbb{S}_0$, donc par (3) $AX=QY=AX_0$, soit $A(X-X_0)=0$ : **$X-X_0\in\ker(A)$.**

Comme $X_0\in\ker(A)^\perp$, le théorème de Pythagore donne :

$$\|X\|^2=\|X_0+(X-X_0)\|^2=\|X_0\|^2+\|X-X_0\|^2.$$

Si $X\neq X_0$, alors $\|X-X_0\|>0$ et **$\|X\|>\|X_0\|$** : $X_0$ est la solution de norme minimale.

**(c)** Si $\operatorname{rg}(A)=p$, $M$ est inversible (question 9), et $D(X)=0\iff MX={}^tAY\iff X=M^{-1}\,{}^tAY$. Donc :

$$\boxed{\mathbb{S}_0=\{M^{-1}\,{}^tAY\}.}$$

### 16.

**(a)** $X=M^{-1}\,{}^tA(AU_0+Z)=M^{-1}MU_0+M^{-1}\,{}^tAZ=U_0+M^{-1}\,{}^tAZ$, donc par la question 10(a) :

$$\begin{aligned}
A(X-U_0)&=AM^{-1}\,{}^tAZ\\
&=QZ\\
T&=\|QZ\|^2\\
&={}^tZ\,{}^tQQZ.
\end{aligned}$$

$M$ est symétrique, donc $M^{-1}$ aussi (${}^t(M^{-1})=({}^tM)^{-1}$), et ${}^tQ=AM^{-1}\,{}^tA=Q$. De plus :

$$\begin{aligned}
Q^2&=AM^{-1}({}^tAA)M^{-1}\,{}^tA\\
&=AM^{-1}\,{}^tA\\
&=Q.
\end{aligned}$$

Donc ${}^tQQ=Q^2=Q$ et $\boxed{T=\|QZ\|^2={}^tZQZ.}$

**(b)**

```python
def simuleT(A, sigma):
    n, p = np.shape(A)
    Q = Calcule_Q(A)
    Z = rd.normal(0, sigma, n)          # n tirages indépendants de loi N(0, sigma^2)
    return np.dot(Z, np.dot(Q, Z))      # tZ Q Z
```

**(c)** Par la loi faible des grands nombres ($T$ admet une variance, cf. (i)), la moyenne de $N$ simulations indépendantes de $T$ approche $\mathbb{E}(T)$. L'énoncé nomme la fonction `esperance` en (c), puis `esperanceT` dans le programme de (d) ; on retient ce second nom.

```python
def esperanceT(A, sigma):
    N = 10000
    s = 0
    for k in range(N):
        s = s + simuleT(A, sigma)
    return s / N
```

**(d)** Les matrices $A_1$, $A_2$ et $A_3$ sont de rang $p$ égal respectivement à 2, 3 et 5 (colonnes échelonnées).

Pour $\sigma=1$, les valeurs obtenues $1{,}99$ ; $3{,}01$ ; $4{,}97$ suggèrent $\mathbb{E}(T)\approx p$.

Pour $A_1$ ($p=2$) et $\sigma=1,\dots,6$, les points du graphique sont proches de $2,\ 8,\ 18,\ 32,\ 50,\ 72$, soit $2\sigma^2$.

**Conjecture : $\mathbb{E}(T)=p\,\sigma^2$.**

**(e)** On écrit $z_1=\sigma N$ avec $N\hookrightarrow\mathcal{N}(0,1)$, de densité $\varphi(x)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2}$. Les intégrales $\int_{\mathbb{R}}|x|^k\varphi(x)\,\mathrm{d}x$ convergent (croissances comparées), donc $N$ admet des moments de tout ordre.

$\mathbb{E}(N^2)=\mathbb{V}(N)=1$ et, $x\mapsto x^3\varphi(x)$ étant impaire et intégrable, $\mathbb{E}(N^3)=0$. Par intégration par parties sur $[-B,B]$ avec $\varphi'(x)=-x\varphi(x)$, puis $B\to+\infty$ :

$$\int_{-B}^{B}x^3\cdot x\varphi(x)\,\mathrm{d}x=\big[-x^3\varphi(x)\big]_{-B}^{B}+3\int_{-B}^{B}x^2\varphi(x)\,\mathrm{d}x\longrightarrow 3.$$

$$\boxed{\begin{aligned}
\mathbb{E}(z_1^2)&=\sigma^2\\
\mathbb{E}(z_1^3)&=0\\
\mathbb{E}(z_1^4)&=3\sigma^4.
\end{aligned}}$$

**(f)** Par (a), en séparant les termes diagonaux et en regroupant $(i,j)$ et $(j,i)$ grâce à la symétrie de $Q$ :

$$\begin{aligned}
T={}^tZQZ&=\sum_{i=1}^{n}\sum_{j=1}^{n}Q_{i,j}z_iz_j\\
&=\sum_{i=1}^{n}Q_{i,i}z_i^2+\sum_{i\neq j}Q_{i,j}z_iz_j\\
&=T_1+2T_2.
\end{aligned}$$

Les $z_i$ sont centrées, indépendantes, et admettent un moment d'ordre 2. Pour $i<j$, $\mathbb{E}(z_iz_j)=\mathbb{E}(z_i)\mathbb{E}(z_j)=0$. Par linéarité de l'espérance, puis les questions 8(b) et $\operatorname{rg}(A)=p$ :

$$\begin{aligned}
\mathbb{E}(T)&=\sigma^2\sum_{i=1}^{n}Q_{i,i}\\
&=\sigma^2\operatorname{Tr}(Q)\\
&=\sigma^2\operatorname{rg}(A).
\end{aligned}$$

$$\boxed{\mathbb{E}(T)=p\,\sigma^2,}$$

ce qui confirme les deux conjectures ($\mathbb{E}(T)=p$ pour $\sigma=1$, et $2\sigma^2$ pour $A_1$).

**(g)** Par linéarité :

$$\mathbb{E}(T_1T_2)=\sum_{k=1}^{n}\sum_{1\leqslant i<j\leqslant n}Q_{k,k}Q_{i,j}\,\mathbb{E}(z_k^2z_iz_j).$$

Soient $k$ et $i<j$. Par indépendance (lemme des coalitions) et existence des moments :

- si $k\notin\{i,j\}$, $\mathbb{E}(z_k^2z_iz_j)=\mathbb{E}(z_k^2)\mathbb{E}(z_i)\mathbb{E}(z_j)=0$ ;
- si $k=i$, alors $j\neq k$ et $\mathbb{E}(z_i^3z_j)=\mathbb{E}(z_i^3)\mathbb{E}(z_j)=0$ ;
- si $k=j$, de même $\mathbb{E}(z_iz_j^3)=\mathbb{E}(z_i)\mathbb{E}(z_j^3)=0$.

**Donc $\mathbb{E}(T_1T_2)=0$.**

**(h)** *Calcul de $\mathbb{E}(T_1^2)$.* Par (e) et l'indépendance, $\mathbb{E}(z_i^2z_k^2)$ vaut $3\sigma^4$ si $i=k$ et $\sigma^4$ sinon. Avec $\operatorname{Tr}(Q)=p$ :

$$\begin{aligned}
\mathbb{E}(T_1^2)&=\sum_{i=1}^{n}\sum_{k=1}^{n}Q_{i,i}Q_{k,k}\,\mathbb{E}(z_i^2z_k^2)\\
&=3\sigma^4\sum_{i=1}^{n}Q_{i,i}^2+\sigma^4\sum_{i\neq k}Q_{i,i}Q_{k,k}\\
&=3\sigma^4q+\sigma^4\big(\operatorname{Tr}(Q)^2-q\big)\\
&=\sigma^4(2q+p^2).
\end{aligned}$$

*Calcul de $\mathbb{E}(T_2^2)$.*

$$\mathbb{E}(T_2^2)=\sum_{i<j}\sum_{k<l}Q_{i,j}Q_{k,l}\,\mathbb{E}(z_iz_jz_kz_l).$$

Si $(i,j)\neq(k,l)$, l'un des indices apparaît une seule fois dans $z_iz_jz_kz_l$ : soit les quatre sont distincts ; soit un seul est commun, par exemple $i=k$ et $j\neq l$, et alors $j$ et $l$ apparaissent une fois.

Par indépendance, l'espérance contient un facteur $\mathbb{E}(z_m)=0$. Il reste les termes $(k,l)=(i,j)$, pour lesquels $\mathbb{E}(z_i^2z_j^2)=\sigma^4$ :

$$\mathbb{E}(T_2^2)=\sigma^4\sum_{i<j}Q_{i,j}^2.$$

Par symétrie de $Q$, puis ${}^tQQ=Q$ :

$$\begin{aligned}
\sum_{i<j}Q_{i,j}^2&=\frac12\Big(\sum_{i,j}Q_{i,j}^2-\sum_{k}Q_{k,k}^2\Big)\\
&=\frac12\big(\operatorname{Tr}({}^tQQ)-q\big)\\
&=\frac12(p-q).
\end{aligned}$$

$$\boxed{\begin{aligned}
\mathbb{E}(T_1^2)&=\sigma^4(2q+p^2)\\
\mathbb{E}(T_2^2)&=\frac{\sigma^4}{2}(p-q).
\end{aligned}}$$

**(i)** $T^2=T_1^2+4T_1T_2+4T_2^2$, donc par (g) et (h) :

$$\begin{aligned}
\mathbb{E}(T^2)&=\sigma^4(2q+p^2)+0+2\sigma^4(p-q)\\
&=\sigma^4(p^2+2p).
\end{aligned}$$

Avec $\mathbb{E}(T)=p\sigma^2$ :

$$\boxed{\mathbb{V}(T)=\mathbb{E}(T^2)-\mathbb{E}(T)^2=2p\sigma^4.}$$

Soit $\alpha>0$ (et $\sigma>0$). L'événement $\big(T>(1+\alpha)p\sigma^2\big)$ est inclus dans $\big(|T-\mathbb{E}(T)|\geqslant\alpha p\sigma^2\big)$. L'inégalité de Bienaymé-Tchebychev donne :

$$\mathbb{P}\big(T>(1+\alpha)p\sigma^2\big)\leqslant\frac{\mathbb{V}(T)}{\alpha^2p^2\sigma^4}=\frac{2}{p\,\alpha^2}.$$

---

## Partie III : minimisation d'une fonction non différentiable

### 17.

Pour $t\neq0$ :

$$\|u+tv\|^2=\|u\|^2+2t\langle u,v\rangle+t^2\|v\|^2.$$

Comme $u\neq0$, le dénominateur ci-dessous est strictement positif et :

$$\frac{\|u+tv\|-\|u\|}{t}=\frac{\|u+tv\|^2-\|u\|^2}{t\big(\|u+tv\|+\|u\|\big)}=\frac{2\langle u,v\rangle+t\|v\|^2}{\|u+tv\|+\|u\|}.$$

La fonction $t\mapsto\|u+tv\|$, racine d'un polynôme positif, est continue ; elle tend vers $\|u\|$ en $0$. Donc :

$$\lim_{t\to0}\frac{\|u+tv\|-\|u\|}{t}=\frac{2\langle u,v\rangle}{2\|u\|}=\frac{\langle u,v\rangle}{\|u\|}.$$

Le calcul vaut dans tout $\mathbb{R}^k$, ce qui servira avec $k=m$.

### 18.

Soit $H\in\mathcal{M}_{p,1}(\mathbb{R})$. Pour $t\neq0$, par (2) et la minimalité de $J(X_0)$ :

$$0\leqslant J(X_0+tH)-J(X_0)=t\langle D(X_0),H\rangle+\frac{t^2}{2}\,{}^tHMH+\|BX_0+tBH\|-\|BX_0\|.$$

On divise par $t$. Par la question 17 (dans $\mathbb{R}^m$, avec $u=BX_0\neq0$ et $v=BH$), le quotient tend, quand $t\to0$, vers :

$$g(H)=\langle D(X_0),H\rangle+\frac{\langle BX_0,BH\rangle}{\|BX_0\|}.$$

Pour $t>0$ le quotient est positif, pour $t<0$ il est négatif : à la limite, $g(H)\geqslant0$ et $g(H)\leqslant0$, donc $g(H)=0$. Or $\langle BX_0,BH\rangle=\langle{}^tBBX_0,H\rangle$, donc :

$$\forall H,\quad\Big\langle D(X_0)+{}^tB\frac{BX_0}{\|BX_0\|},H\Big\rangle=0.$$

Avec $H$ égal à ce vecteur, il est nul :

$$\boxed{-D(X_0)={}^tB\frac{BX_0}{\|BX_0\|}.}$$

Posons $V=\dfrac{BX_0}{\|BX_0\|}\in\mathcal{M}_{m,1}(\mathbb{R})$ : $\|V\|=1\leqslant1$ et $\|BX_0\|V-BX_0=0$. Donc **$-D(X_0)={}^tBV\in\mathscr{N}(X_0)$.**

### 19.

**(a)** L'énoncé écrit $H\in\mathcal{M}_{n,1}(\mathbb{R})$ ; pour que $BH$ et $\langle D(X_0),H\rangle$ aient un sens, il faut lire $H\in\mathcal{M}_{p,1}(\mathbb{R})$. Soit $H$ et $t<0$.

Comme $BX_0=0$, $\|B(X_0+tH)\|=|t|\,\|BH\|=-t\|BH\|$, et :

$$0\leqslant J(X_0+tH)-J(X_0)=t\langle D(X_0),H\rangle+\frac{t^2}{2}\,{}^tHMH-t\|BH\|.$$

En divisant par $t<0$ : $\langle D(X_0),H\rangle+\frac t2\,{}^tHMH-\|BH\|\leqslant0$. Quand $t\to0^-$ :

$$\forall H\in\mathcal{M}_{p,1}(\mathbb{R}),\quad\langle D(X_0),H\rangle\leqslant\|BH\|.$$

**(b)** Soit $H\in\ker(B)$. Par (a) appliqué à $H$ et à $-H$ : $\langle D(X_0),H\rangle\leqslant0$ et $-\langle D(X_0),H\rangle\leqslant0$.

Donc $\langle D(X_0),H\rangle=0$ : **$D(X_0)\in\ker(B)^\perp$.**

**(c)** La question 5, appliquée à $v:X\mapsto BX$ de $\mathbb{R}^p$ dans $\mathbb{R}^m$ (d'adjoint $W\mapsto{}^tBW$), donne $\ker(B)^\perp=\operatorname{Im}({}^tB)$.

**Il existe donc $W\in\mathcal{M}_{m,1}(\mathbb{R})$ tel que $D(X_0)={}^tBW$.**

**(d)** La question 6 appliquée à $v$ donne $\operatorname{Im}({}^tBB)=\operatorname{Im}({}^tB)$. Comme $D(X_0)\in\operatorname{Im}({}^tB)$, **il existe $V\in\mathcal{M}_{p,1}(\mathbb{R})$ tel que $D(X_0)={}^tBBV$.**

**(e)** Par (a) avec $H=V$ :

$$\|BV\|^2={}^tV\,{}^tBBV=\langle D(X_0),V\rangle\leqslant\|BV\|.$$

Si $BV\neq0$, on divise par $\|BV\|>0$ ; sinon c'est immédiat : **$\|BV\|\leqslant1$.**

Posons $V'=-BV\in\mathcal{M}_{m,1}(\mathbb{R})$. Alors $-D(X_0)={}^tBV'$, $\|V'\|\leqslant1$ et, puisque $BX_0=0$, $\|BX_0\|V'-BX_0=0$. **Donc $-D(X_0)\in\mathscr{N}(X_0)$.**

### 20.

**(a)** En développant :

$$\begin{aligned}
\|u+v\|^2-\Big(\|u\|+\frac{\langle u,v\rangle}{\|u\|}\Big)^2&=\|u\|^2+2\langle u,v\rangle+\|v\|^2-\|u\|^2-2\langle u,v\rangle-\frac{\langle u,v\rangle^2}{\|u\|^2}\\
&=\frac{\|u\|^2\|v\|^2-\langle u,v\rangle^2}{\|u\|^2}.
\end{aligned}$$

**(b)** Par l'inégalité de Cauchy-Schwarz, le membre de droite est positif. Donc, la racine carrée étant croissante :

$$\|u+v\|\geqslant\Big|\|u\|+\frac{\langle u,v\rangle}{\|u\|}\Big|\geqslant\|u\|+\frac{\langle u,v\rangle}{\|u\|}.$$

C'est (7) : $\|u+v\|-\|u\|\geqslant\dfrac{\langle u,v\rangle}{\|u\|}$. Le calcul vaut dans tout $\mathbb{R}^k$.

### 21.

**(a)** Écrivons $W={}^tBV$ avec $\|V\|\leqslant1$ et $\|BX_0\|V=BX_0$. Alors :

$$\langle W,X-X_0\rangle=\langle V,B(X-X_0)\rangle.$$

*Cas $BX_0\neq0$.* En prenant la norme, $\|BX_0\|\,\|V\|=\|BX_0\|$, donc $\|V\|=1$ et $V=\dfrac{BX_0}{\|BX_0\|}$.

L'inégalité (7) dans $\mathbb{R}^m$, avec $u=BX_0$ et $v=B(X-X_0)$, donne :

$$\|BX\|-\|BX_0\|\geqslant\frac{\langle BX_0,B(X-X_0)\rangle}{\|BX_0\|}=\langle V,B(X-X_0)\rangle=\langle W,X-X_0\rangle.$$

*Cas $BX_0=0$.* Par Cauchy-Schwarz et $\|V\|\leqslant1$ :

$$\langle W,X-X_0\rangle=\langle V,BX\rangle\leqslant\|V\|\,\|BX\|\leqslant\|BX\|=\|BX\|-\|BX_0\|.$$

**Dans les deux cas, $\|BX\|-\|BX_0\|\geqslant\langle W,X-X_0\rangle$.**

**(b)** Par (2) avec $H=X-X_0$ et la question 11 :

$$J_0(X)-J_0(X_0)=\langle D(X_0),X-X_0\rangle+\frac12\,{}^t(X-X_0)M(X-X_0)\geqslant\langle D(X_0),X-X_0\rangle.$$

Comme $J=J_0+\|B\,\cdot\,\|$, en ajoutant (a) :

$$J(X)-J(X_0)\geqslant\langle D(X_0)+W,X-X_0\rangle.$$

C'est (8).

### 22.

*Condition nécessaire.* Si $X_0$ réalise le minimum global de $J$, alors $-D(X_0)\in\mathscr{N}(X_0)$ par la question 18 si $BX_0\neq0$, et par la question 19 si $BX_0=0$.

*Condition suffisante.* Si $-D(X_0)\in\mathscr{N}(X_0)$, on applique (8) avec $W=-D(X_0)$ : pour tout $X$, $J(X)-J(X_0)\geqslant0$.

**$X_0$ réalise un minimum global de $J$ si et seulement si $-D(X_0)\in\mathscr{N}(X_0)$.**

### 23.

Ici $A=I_n$, donc $M=I_n$ et $D(X)=X-Y$ ; $B$ est diagonale, donc ${}^tB=B$.

**(a)** Pour $\lambda>0$ et $a>0$, $(\lambda+a)^2-4\lambda a=(\lambda-a)^2\geqslant0$. Avec $a=\alpha_i^2>0$ :

$$\frac{\alpha_i^2y_i^2}{(\lambda+\alpha_i^2)^2}\leqslant\frac{\alpha_i^2y_i^2}{4\lambda\alpha_i^2}=\frac{y_i^2}{4\lambda}.$$

En sommant sur $i\in\llbracket1,k\rrbracket$ :

$$\forall\lambda>0,\quad F(\lambda)\leqslant-1+\frac{1}{4\lambda}\sum_{i=1}^{k}y_i^2.$$

**(b)** Comme $\rho(Y)>1$, l'un au moins des $y_i$ ($i\leqslant k$) est non nul. $F$ est dérivable sur $[0,+\infty[$ et :

$$F'(\lambda)=-2\sum_{i=1}^{k}\frac{\alpha_i^2y_i^2}{(\lambda+\alpha_i^2)^3}<0.$$

$F$ est donc continue et strictement décroissante sur $[0,+\infty[$, avec $F(0)=-1+\rho(Y)>0$ et $\lim_{\lambda\to+\infty}F(\lambda)=-1<0$.

Par le théorème de la bijection, $F$ s'annule en un unique point $\lambda_0$ de $[0,+\infty[$, et $\lambda_0\neq0$ puisque $F(0)>0$.

**Il existe un unique $\lambda_0\in\,]0,+\infty[$ tel que $F(\lambda_0)=0$.**

Avec $S=\sum_{i=1}^{k}y_i^2>0$, la question (a) en $\lambda_0>0$ donne $0=F(\lambda_0)\leqslant-1+\dfrac{S}{4\lambda_0}$, d'où :

$$\boxed{\lambda_0\leqslant\frac14\sum_{i=1}^{k}y_i^2.}$$

**(c)** Par la question 22, il suffit de montrer que $-D(X_0)\in\mathscr{N}(X_0)$. On a $-D(X_0)=Y-X_0=BV={}^tBV$. Il reste à vérifier $\|V\|\leqslant1$ et $\|BX_0\|V=BX_0$.

*Calcul de $BX_0$.* Pour $i\leqslant k$ :

$$\begin{aligned}
(BX_0)_i&=\alpha_i(y_i-\alpha_iv_i)\\
&=\alpha_iy_i\Big(1-\frac{\alpha_i^2}{\beta+\alpha_i^2}\Big)\\
&=\frac{\beta\,\alpha_iy_i}{\beta+\alpha_i^2}\\
&=\beta v_i.
\end{aligned}$$

Pour $i>k$, $(BX_0)_i=0=\beta v_i$. Donc $BX_0=\beta V$.

*Calcul de $\|V\|$.* $\|V\|^2=\sum_{i=1}^{k}\dfrac{\alpha_i^2y_i^2}{(\beta+\alpha_i^2)^2}=1+F(\beta)$.

- Si $\rho(Y)\leqslant1$ : $\beta=0$, $\|V\|^2=\sum_{i=1}^{k}y_i^2/\alpha_i^2=\rho(Y)\leqslant1$ et $BX_0=0$, donc $\|BX_0\|V-BX_0=0$.
- Si $\rho(Y)>1$ : $\beta=\lambda_0$ et $\|V\|^2=1+F(\lambda_0)=1$. De plus $BX_0=\lambda_0V$ avec $\lambda_0>0$, donc $\|BX_0\|=\lambda_0$.
  Ainsi $\|BX_0\|V-BX_0=\lambda_0V-\lambda_0V=0$.

Dans les deux cas $-D(X_0)\in\mathscr{N}(X_0)$ : **$X_0$ réalise un minimum global de $J$.**

**(d)** Les tableaux sont indexés à partir de 0 ; `Y` contient les $n$ composantes de $Y$ et `alpha` les $k$ réels $\alpha_i$.

**i.**

```python
def FoncSom(alpha, Y, lda):
    k = len(alpha)
    s = -1
    for i in range(k):
        s = s + alpha[i]**2 * Y[i]**2 / (lda + alpha[i]**2)**2
    return s
```

**ii.** Pour $\rho(Y)>1$, $F$ est strictement décroissante, $F(0)>0$ et $F(b)\leqslant0$ en $b=\frac14\sum_{i\leqslant k}y_i^2$ par la question (a).

On maintient $F(a)>0\geqslant F(b)$ en divisant l'intervalle par deux ; $\lambda_0\in[a,b]$ à chaque étape. On renvoie $0$ si $\rho(Y)\leqslant1$, ce qui sert en iii.

```python
def CalcBeta(alpha, Y, epsilon):
    k = len(alpha)
    rho = 0
    for i in range(k):
        rho = rho + Y[i]**2 / alpha[i]**2
    if rho <= 1:
        return 0
    a = 0
    b = 0
    for i in range(k):
        b = b + Y[i]**2
    b = b / 4
    while b - a > epsilon:
        c = (a + b) / 2
        if FoncSom(alpha, Y, c) > 0:
            a = c
        else:
            b = c
    return (a + b) / 2
```

À la sortie, $\lambda_0\in[a,b]$ et $b-a\leqslant\varepsilon$, donc le milieu est à moins de $\varepsilon$ de $\lambda_0=\beta$.

**iii.**

```python
def CalcSolution(alpha, Y, epsilon):
    n = len(Y)
    k = len(alpha)
    beta = CalcBeta(alpha, Y, epsilon)
    X0 = np.zeros(n)
    for i in range(n):
        X0[i] = Y[i]                     # composantes k+1..n : v_i = 0
    for i in range(k):
        v = alpha[i] * Y[i] / (beta + alpha[i]**2)
        X0[i] = Y[i] - alpha[i] * v      # (Y - BV)_i
    return X0
```
