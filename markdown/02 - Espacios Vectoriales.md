# 02 - Espacios Vectoriales

## Vectores

### Operaciones entre vectores

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

### Norma de un vector

Función $N$ que recibe un vector $u$ y devuelve un escalar, que cumple:
1. $N(u) \ge 0 \land N(u) = 0 \iff u = 0$
2. Con $\lambda$ escalar, $N(\lambda u) = |\lambda| N(u)$
3. Desigualdad triangular: $N(u + r) \le N(u) + N(r)$

Existen varias normas:
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

### Ángulo entre vectores

El ángulo $\alpha$ (con $0 \le \alpha \le \pi$) entre dos vectores $u$ y $r$ es aquel que cumple:
$$
\cos(\alpha) = \frac{<u, r>}{||u||_2 \space ||r||_2}
$$

### Paralelismo y perpendicularidad
* $u$ y $r$ son paralelos si existe un escalar $k$ tal que $r = k \cdot u$
* $u$ y $r$ son perpendiculares si son no nulos y $<u, r> = 0$

---

## Espacio Vectorial
