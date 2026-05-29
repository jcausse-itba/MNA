# 4. Espacios Vectoriales Generales

## 4.1. Definición de Espacio Vectorial
Un **espacio vectorial** se define formalmente como una cuaterna $(V, +, \mathbb{K}, \cdot)$ donde $V$ es un conjunto no vacío, $\mathbb{K}$ es un cuerpo ($\mathbb{R}$ o $\mathbb{C}$ en esta materia), $+$ es la operación de suma interna y $\cdot$ es la multiplicación por un escalar. 

Para que esta estructura sea válida, debe cumplir los siguientes 10 axiomas:

**Respecto a la Suma de Vectores ($+$)**:
1. **Clausura:** $\forall u, v \in V \Rightarrow u+v \in V$.
2. **Asociatividad:** $\forall u, v, w \in V : u+(v+w) = (u+v)+w$.
3. **Elemento neutro:** $\exists 0_V \in V / \space \forall u \in V : u+0_V = 0_V+u = u$.
4. **Inverso aditivo:** $\forall v \in V, \exists -v \in V / v+(-v) = 0_V$.
5. **Conmutatividad:** $\forall u, v \in V : u+v = v+u$

**Respecto al Producto por un Escalar ($\cdot$)**:

6. **Ley externa (Clausura):** $\forall v \in V, \forall \lambda \in \mathbb{K} \Rightarrow \lambda \cdot v \in V$.
7. **Distributividad (respecto a suma de vectores):** $\forall u, v \in V, \forall \lambda \in \mathbb{K} \Rightarrow \lambda \cdot (u+v) = \lambda \cdot u + \lambda \cdot v$.
8. **Distributividad (respecto a suma de escalares):** $\forall v \in V, \forall \lambda, \mu \in \mathbb{K} \Rightarrow (\lambda+\mu) \cdot v = \lambda \cdot v + \mu \cdot v$.
9. **Asociatividad mixta:** $\forall v \in V, \forall \lambda, \mu \in \mathbb{K} \Rightarrow (\lambda \mu) \cdot v = \lambda \cdot (\mu \cdot v)$.
10. **Unitariedad:** $\forall v \in V \Rightarrow 1 \cdot v = v$.

> **Ejemplos clásicos de Espacios Vectoriales:** Vectores en $\mathbb{R}^n$, matrices en $\mathbb{C}^{m \times m}$ y funciones continuas $C[a,b]$.

---

## 4.2. Subespacios Vectoriales
Un subconjunto $S \subseteq V$ es un **subespacio vectorial** de $V$ si, por sí mismo, también es un espacio vectorial. En la práctica, solo hace falta probar dos condiciones para demostrar que lo es:

1. **Cerrado para la suma:** $\forall s_1, s_2 \in S \Rightarrow s_1+s_2 \in S$.
2. **Cerrado para el producto:** $\forall s \in S, \forall \lambda \in \mathbb{K} \Rightarrow \lambda \cdot s \in S$.

> **Propiedad de descarte rápido (El vector nulo):** Todo subespacio **debe** contener al vector nulo ($0_V \in S$). Si al evaluar el cero no pertenece al conjunto, entonces automáticamente no es un subespacio.

---

## 4.3. Combinación Lineal y Espacios Generados

* **Combinación Lineal (CL):** Dado un conjunto de vectores $A = \{v_1, ..., v_n\} \subseteq V$, se dice que un vector $v \in V$ es combinación lineal de $A$ si existen escalares $\alpha_1, ..., \alpha_n \in \mathbb{K}$ que permitan escribirlo como una suma ponderada:

    $$
    v = \alpha_1 v_1 + \alpha_2 v_2 + ... + \alpha_n v_n
    $$

* **Subespacio Generado:** Al conjunto de **todas** las combinaciones lineales posibles que se pueden armar con los vectores de $A$ se lo llama *subespacio generado* por $A$ y se denota $gen(A)$. Los vectores de $A$ actúan como el *conjunto de generadores* de ese subespacio.

---

## 4.4. Dependencia e Independencia Lineal

Dado un conjunto $A = \{v_1, ..., v_n\} \subseteq V$:

* **Linealmente Independiente (LI):** La única forma de obtener el vector nulo mediante una CL de estos vectores es que **todos** los escalares sean obligatoriamente cero.
    
    $$
    \alpha_1 v_1 + \alpha_2 v_2 + ... + \alpha_n v_n = 0 \iff \alpha_i = 0 \quad \forall i
    $$

* **Linealmente Dependiente (LD):** Si el conjunto no es LI, es LD. Esto significa que existe una forma de llegar al cero usando escalares donde al menos uno es distinto de cero ($\alpha_k \neq 0$).
    * *Concepto clave:* En un conjunto LD, al menos un vector es una combinación lineal del resto. "Sobra" información.
  
> **Descarte rápido:** Si en el conjunto hay dos vectores iguales, uno que es múltiplo de otro, o está el vector nulo, es LD. Justificarlo.

---

## 4.5. Base y Dimensión

* **Base:** Un conjunto $B = \{v_1, ..., v_n\} \subseteq V$ es una base del espacio vectorial $V$ si cumple **simultáneamente** dos requisitos:
    1.  $B$ es linealmente independiente (LI). Para probar esto, ver apartado anterior.
    2.  $B$ genera a todo el espacio $V$. Para probar esto, mostrar que cualquier vector de $V$ puede escribirse como una CL de los vectores en $B$.

> **Importante:** No confundir conjunto de generadores con una base; una base es un conjunto de generadores que **no** tiene vectores redundantes (LD)*.

* **Dimensión:** Es la cantidad exacta de vectores que contiene una base de un espacio o subespacio vectorial.

---

## 4.6. Contraejemplos Clásicos de Examen

Al verificar si un conjunto es subespacio, hay que tener cuidado con estas "trampas" habituales:

* **Rectas o planos desplazados:** $A = \{(x,y,z) \in \mathbb{R}^3 : x+y+z-1=0\}$. **No es subespacio**, ya que el vector nulo $(0,0,0)$ no cumple la ecuación ($0-1 \neq 0$).
* **Condiciones con desigualdades:** $A = \{(x,y) \in \mathbb{R}^2 : x \le 0\}$. **No es subespacio**. Falla el producto por un escalar negativo: si se multiplica un vector de $A$ (ej: $(-2,1)$) por $\lambda = -1$, se obtiene $(2,-1)$, cuyo valor de $x$ es positivo y ya no pertenece al conjunto.
* **Matrices singulares:** $P = \{A \in \mathbb{C}^{2 \times 2} : det(A) = 0\}$. **No es subespacio**. Falla la clausura de la suma. Sumar dos matrices que individualmente tienen determinante cero puede dar como resultado la matriz Identidad (cuyo determinante es 1).
* **Polinomios de grado exacto:** $A = \{p \in \mathbb{P}_4 : gr(p) = 2\}$. **No es subespacio**. Si se suman $p(x) = x^2+x-2$ y $q(x) = -x^2+2x+3$, los términos cuadrados se cancelan y se obtiene un polinomio de grado 1, rompiendo la clausura.
