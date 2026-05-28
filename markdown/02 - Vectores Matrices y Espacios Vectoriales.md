# 02 - Vectores, Matrices y Espacios Vectoriales

# Vectores

## Operaciones entre vectores

* **Igualdad:** Dos vectores son iguales si son iguales componente a componente.
* **Adición:** Dos vectores de la misma dimensión pueden sumarse componente a componente, generando un nuevo vector de la misma dimensión.
* **Producto por un escalar:** Se multiplica el escalar por cada componente del vector. Genera un nuevo vector de la misma dimensión.
* **Producto Interno**: Dados dos vectores $u, r\in \Kappa^n$ se define el producto interno (un escalar) entre ellos como:
  $$
  <u, r> = \sum_{k = 1}^{n} u_i \overline{r_i}
  $$
  Propiedades:
  * $<u, r> = \overline{<r, u>}$
  * $<u + s, r> = <u, r> + <s, r>$
  * $<u, r + s> = <u, r> + <u, s>$
  * Con $\alpha$ escalar, $<\alpha u, r> = \alpha <u, r>$
  * Con $\alpha$ escalar, $<u, \alpha r> = \bar{\alpha} <u, r>$
  * $<u, u> \space \ge 0$
  * $|<u, r>|^2 \le |<u, u>|^2 \space |<r, r>|^2$
* **Producto Vectorial:** Para dos vectores en $\R^3$ se usa la Regla de Sarrus. Devuelve un vector perpendicular a ambos.

<p align="center">
  <img src="../img/sarrus.png" height="120"/>
</p>

## Norma de un vector

Función $N$ que recibe un vector $u$ y devuelve un escalar, que cumple:
1. $N(u) \ge 0 \land N(u) = 0 \iff u = 0$
2. Con $\lambda$ escalar, $N(\lambda u) = |\lambda| N(u)$
3. Desigualdad triangular: $N(u + r) \le N(u) + N(r)$

### Normas

1. **Norma usual (Norma 2):**
  $$
  ||u||_2 = \sqrt{<u, u>}
  $$
2. **Norma 1:**
  $$
  ||u||_1 = \sum_{i = 1}^{n} |u_i|
  $$
3. **Norma $p$:** Para $p \gt 1$:
   $$
   ||u||_p = \bigg( \sum_{i = 1}^{n} |u_i|^p \bigg)^{1/p}   
   $$
4. **Norma infinito:**
   $||u||_\infty = \max\{|u_i| \space / \space 1 \le i \le n \}$

## Ángulo entre vectores

El ángulo $\alpha$ (con $0 \le \alpha \le \pi$) entre dos vectores $u$ y $r$ es aquel que cumple:
$$
\cos(\alpha) = \frac{<u, r>}{||u||_2 \space ||r||_2}
$$

## Paralelismo y perpendicularidad
* $u$ y $r$ son paralelos si existe un escalar $k$ tal que $r = k \cdot u$
* $u$ y $r$ son perpendiculares si son no nulos y $<u, r> = 0$

---

# Matrices

## Operaciones entre matrices

* **Igualdad:** Dos matrices son iguales si son iguales posición a posición.
* **Adición:** Dos matrices de las mismas dimensiones se suman posición a posición. Esto genera una matriz de la misma dimensión.
  
  Propiedades:
  * Es asociativa.
  * Es conmutativa.
  * La matriz que contiene todos sus elementos nulos para el cuerpo sobre el que está definida la matriz es el elemento neutro de esta operación.
  * Para toda matriz existe su inversa aditiva (aquella que al sumar las dos se obtiene la matriz nula).

Sean $A$, $B$ matrices y $\lambda$, $\mu$ escalares.

* **Multiplicación por escalar:** Se multiplica cada posición por el escalar.
  
  Propiedades:
  * $\lambda (A + B) = \lambda A + \lambda B$
  * $(\lambda + \mu) A = \lambda A + \mu A$
  * $(\lambda \mu) A = \lambda (\mu A)$

Sean las matrices $C$ de dimensión $n \times m$, $D$ de dimensión $m \times p$ y  $E$ de dimensión $n \times p$.

* **Multiplicación de matrices:** Se multiplica cada elemento de la fila $i$ de $C$ por su respectivo en la columna $j$ de $D$. Se suman todos los productos realizados. El resultado va en la posición $i$,$j$ de $E$. Se repite $\forall \space 1 \le i \le n \space \forall \space 1 \le j \le p$.
  $$
  e_{ij} = \sum_{k = 1}^{m} c_{ik} d_{kj}
  $$

  Propiedades:
  * Es necesario que la matriz de la izquierda tenga la misma cantidad de columnas que la cantidad de filas de la de la derecha.
  * El resultado es una matriz que tiene la misma cantidad de filas que la de la izquierda, y la misma cantidad de columnas que la de la derecha.
  * **No es conmutativo**.
  * Es asociativo (siempre manteniendo el orden).
  * Es distributivo respecto de la suma de matrices (siempre manteniendo el orden).
* **Potenciación de matrices:** $A^n$ = $AAA...A$, un total de $n$ veces.
  
  Propiedades:
  * $A^{p + q} = A^p + A^q$
  * $(A^p)^q = A^{pq}$

## Matriz transpuesta

Cada elemento $i$,$j$ en la matriz original ocupa la posición $j$,$i$ en la transpuesta. Las filas se transforman en las columnas y viceversa. Si la matriz es de dimensión $n \times p$, queda de $p \times n$.

### Propiedades
1. $(A^T)^T = A$
2. $(A + B)^T = A^T + B^T$
3. $(\lambda A)^T = \lambda A^T$
4. $(AB)^T = B^T A^T$

## Matriz identidad

Tiene unos en la diagonal (todo elemento donde $i = j$) y ceros en todos los otros elementos. Se la denota $I$. Como siempre es cuadrada ($n \times n$), la notación $I_n$ indica, además, la dimensión. Cumple que:
$$
A I = I A = A
$$

## Matriz inversa

Una matriz $A$ es invertible cuando:

* Es cuadrada (dimensión $n \times n$).
* Su determinante es distinto de cero.

Las matriz $A$ y su inversa $A^{-1}$ son ambas de la misma dimensión ($n \times n$), y cumplen:
$$
A A^{-1} = A^{-1} A = I_n
$$

Cuando no es cuadrada, se habla de **pseudoinversa** (viene más adelante).

### Propiedades

1. $A^{-1}$ es única para toda $A$.
2. $(A^{-1})^{-1} = A$
3. Sea $\lambda$ un escalar no nulo: $(\lambda A)^{-1} = \frac{1}{\lambda} A^{-1}$
4. $(AB)^{-1} = B^{-1} A^{-1}$

## Matrices con nombre propio

Ciertas matrices reciben un nombre especial si cumplen alguna propiedad. Se enumeran los nombres y lo que tienen que cumplir para serlo.

* **Matriz Simétrica:** $A = A^T \iff a_{ij} = a_{ji}$
* **Matriz Antisimétrica:** $A = -A^T \iff a_{ii} = 0$
* **Matriz Triangular Superior:** $a_{ij} = 0 \space \forall i \gt j$ (abajo a la izquierda llena de ceros).
* **Matriz Triangular Inferior:** $a_{ij} = 0 \space \forall i \lt j$ (arriba a la derecha llena de ceros).
  * No es un error. El nombre es al revés de lo intuitivo. En realidad habla de donde hay elementos no nulos más que de donde hay ceros, pero es más fácil reconocerlas por los ceros.
* **Matriz Diagonal:** Todos los elementos que no estén en la diagonal son cero. No implica que no pueda haber ceros en la diagonal. La matriz nula es diagonal, por ejemplo.
* **Matriz Escalar:** $A = k I_n$ para algún $k$ (es la identidad multiplicada por un escalar).
* **Matriz Idempotente:** $A^2 = A$, entonces resulta: $A^n = A \space \forall n \in \N$
* **Matriz Involutiva:** $A^2 = I$, entonces resulta:
  * $A^{2n} = I$
  * $A^{2n + 1} = A$
* **Matriz Nilpotente:** Si $A^n$ es la matriz nula $\forall n \ge n_0$, $n_0$ es el índice de nilpotencia.
* **Matriz Ortogonal:** $AA^T = A^TA = I_n$

---

