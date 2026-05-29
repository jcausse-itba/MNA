# 2. Vectores

## 2.1. Operaciones entre Vectores

* **Igualdad:** Dos vectores son iguales si son iguales componente a componente.
* **Adición:** Dos vectores de la misma dimensión pueden sumarse componente a componente, generando un nuevo vector de la misma dimensión.
* **Producto por un escalar:** Se multiplica el escalar por cada componente del vector. Genera un nuevo vector de la misma dimensión.
* **Producto Interno, Producto Escalar o Producto Punto**: Dados dos vectores $u, r\in \mathbb{K}^n$ se define el producto interno (un escalar) entre ellos como:
  $$
  \langle u, r \rangle = \sum_{k = 1}^{n} u_i \overline{r_i}
  $$
  Propiedades:
  * $\langle u, r \rangle = \overline{\langle r, u \rangle}$
  * $\langle u + s, r \rangle = \langle u, r \rangle + \langle s, r \rangle$
  * $\langle u, r + s \rangle = \langle u, r \rangle + \langle u, s \rangle$
  * Con $\alpha$ escalar, $\langle \alpha u, r \rangle = \alpha \langle u, r \rangle$
  * Con $\alpha$ escalar, $\langle u, \alpha r \rangle = \bar{\alpha} \langle u, r \rangle$
  * $\langle u, u \rangle \space \ge 0$
  * $|\langle u, r \rangle|^2 \le \langle u, u \rangle \langle r, r \rangle$
* **Producto Vectorial:** Para dos vectores en $\R^3$ se usa la Regla de Sarrus. Devuelve un vector perpendicular a ambos.

<p align="center">
  <img src="../img/sarrus.png" height="120"/>
</p>

## 2.2. Norma de un Vector

Función $N$ que recibe un vector $u$ y devuelve un escalar, que cumple:
1. $N(u) \ge 0 \land N(u) = 0 \iff u = 0$
2. Con $\lambda$ escalar, $N(\lambda u) = |\lambda| N(u)$
3. Desigualdad triangular: $N(u + r) \le N(u) + N(r)$

### 2.2.1. Tipos de normas

1. **Norma usual (Norma 2):**
  $$
  ||u||_2 = \sqrt{\langle u, u \rangle}
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

## 2.3. Ángulo entre Vectores

El ángulo $\alpha$ (con $0 \le \alpha \le \pi$) entre dos vectores $u$ y $r$ es aquel que cumple:
$$
\cos(\alpha) = \frac{\langle u, r \rangle}{||u||_2 \space ||r||_2}
$$

## 2.4. Paralelismo y Perpendicularidad
* $u$ y $r$ son paralelos si existe un escalar $k$ tal que $r = k \cdot u$
* $u$ y $r$ son perpendiculares si son no nulos y $\langle u, r \rangle = 0$
