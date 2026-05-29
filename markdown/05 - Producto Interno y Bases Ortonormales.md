# 5. Producto Interno Generalizado y Bases Ortonormales

## 5.1. Generalización de Paralelismo y Perpendicularidad
En espacios vectoriales abstractos, buscamos generalizar los conceptos geométricos clásicos:
* **Paralelismo:** Dos vectores $v, w \in V$ son paralelos (o proporcionales) si existe un escalar $\lambda \in \mathbb{K}$ tal que $w = \lambda \cdot v$.
* **Perpendicularidad (Ortogonalidad):** Requiere definir previamente una nueva operación matemática llamada **Producto Interno**.

---

## 5.2. Espacio con Producto Interno (Espacio Euclídeo)
Un **Producto Interno** es una función $\langle u, v \rangle$ que toma dos vectores de $V$ y devuelve un escalar de $\mathbb{K}$ (generalmente $\mathbb{R}$ o $\mathbb{C}$). Para ser considerado como tal, debe cumplir estrictamente los siguientes axiomas:

1.  **Linealidad en la primera componente:**
    * $\langle u+v, w \rangle = \langle u, w \rangle + \langle v, w \rangle$ 
    * $\langle \alpha u, v \rangle = \alpha \langle u, v \rangle$ 
    *(Nota: En la segunda componente, los escalares salen conjugados: $\langle u, \beta v \rangle = \overline{\beta} \langle u, v \rangle$)*.
2.  **Simetría Conjugada:** $\langle u, v \rangle = \overline{\langle v, u \rangle}$. (Si se trabaja en $\mathbb{R}$, es simplemente conmutativo: $\langle u, v \rangle = \langle v, u \rangle$).
3.  **Definida Positiva:** $\langle u, u \rangle \ge 0$ para todo $u \in V$. Además, $\langle u, u \rangle = 0 \iff u = 0_V$.

> **Definición de Ortogonalidad:** Dos vectores $u, v$ (no nulos) son ortogonales (perpendiculares) si y sólo si $\langle u, v \rangle = 0$.

---

### 5.2.1. Ejemplos Clásicos de Producto Interno
Dependiendo del espacio vectorial, el producto interno toma diferentes formas:

* **En $\mathbb{R}^n$ (El clásico producto escalar):**
    $\langle u, v \rangle = \sum_{i=1}^{n} u_i v_i$ 
* **En Matrices $\mathbb{R}^{n \times n}$:**
    $\langle A, B \rangle = tr(A B^T)$. *(La traza de la multiplicación de A por B transpuesta)*.
* **En Polinomios $\mathbb{P}_n$ y Funciones Continuas:**
    $\langle p, q \rangle = \int_{a}^{b} p(x)\overline{q(x)} dx$ 

---

## 5.3. Norma Inducida y Proyección Ortogonal
Todo producto interno "induce" (crea) automáticamente una **Norma** (longitud del vector), definida como:
$$
||u|| = \sqrt{\langle u, u \rangle} \implies ||u||^2 = \langle u, u \rangle
$$ 

**Proyección Ortogonal:**
Para proyectar un vector $u$ sobre la dirección de otro vector $v$, se utiliza la fórmula:
$$
P_v u = \frac{\langle u, v \rangle}{\langle v, v \rangle} \cdot v = \frac{\langle u, v \rangle}{||v||^2} \cdot v
$$ 

---

## 5.4. Bases Ortonormales (BON) y Coordenadas
Una **Base Ortonormal (BON)** es una base $B = \{v_1, ..., v_n\}$ que cumple dos condiciones excepcionales:
1.  **Normalizados:** Todos sus vectores tienen norma 1 ($||v_i|| = 1$).
2.  **Ortogonales entre sí:** $\langle v_i, v_j \rangle = 0$ para todo $i \neq j$.

**Gran ventaja de las BON (Cálculo de Coordenadas):**
Si se tiene un vector $v$ y se quiere escribirlo como combinación lineal de una BON, no hace falta resolver sistemas de ecuaciones. Cada escalar $\alpha_k$ se calcula directamente con el producto interno:
$$
\alpha_k = \langle v, v_k \rangle
$$

Por lo tanto, el vector se expresa directamente como:
$$
v = \sum_{i=1}^{n} \langle v, v_i \rangle v_i
$$

---

## 5.5. Proceso de Ortonormalización de Gram-Schmidt
Todo espacio euclídeo de dimensión finita posee al menos una BON. El algoritmo de Gram-Schmidt permite construir una BON $\{u_1, ..., u_n\}$ a partir de cualquier base genérica $B = \{v_1, ..., v_n\}$.

**Algoritmo paso a paso:**
* **Paso 1 (Primer vector):** Tomamos el primero y lo normalizamos.
    $$
    u_1 = \frac{v_1}{||v_1||}
    $$

* **Paso 2:** Al segundo vector le restamos su proyección sobre el primero, y luego normalizamos el resultado.
    $$
    \tilde{u}_2 = v_2 - \langle v_2, u_1 \rangle u_1
    $$ 
    $$
    u_2 = \frac{\tilde{u}_2}{||\tilde{u}_2||}
    $$ 

* **Paso $k$-ésimo (Fórmula general):** A cada nuevo vector se le restan sus proyecciones sobre **todos** los vectores ya ortonormalizados anteriores, y finalmente se lo normaliza.
    $$
    \tilde{u}_k = v_k - \sum_{i=1}^{k-1} \langle v_k, u_i \rangle u_i
    $$ 
    $$
    u_k = \frac{\tilde{u}_k}{||\tilde{u}_k||}
    $$
