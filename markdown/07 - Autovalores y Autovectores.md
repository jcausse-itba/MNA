# 7. Autovalores, Autovectores y Autoespacios

## 7.1. Autovalores y Autovectores (Valores y Vectores Propios)
Sea $T: V \rightarrow V$ un operador lineal (o su matriz asociada $A \in \mathbb{K}^{n \times n}$). 

Decimos que un vector $v \in V$ **no nulo** ($v \neq 0_V$) es un **autovector** de $T$ si, al aplicarle la transformación, el resultado es simplemente el mismo vector escalado por un número $\lambda \in \mathbb{K}$.
$$
T(v) = \lambda \cdot v \quad \iff \quad A \cdot X = \lambda \cdot X
$$

A ese escalar $\lambda$ se lo llama **autovalor** asociado al autovector $v$.

> **Nota:** Un autovector jamás puede ser el vector nulo por definición, pero un autovalor sí puede ser $\lambda = 0$, lo que implicaría que el autovector pertenece al núcleo).

> **Nota:** Los autovectores y autovalores solo se calculan para transformaciones lineales donde la dimensión de los espacios de salida $V$ y de llegada $W$ son la misma (por lo que la matriz de la TL es cuadrada).

---

## 7.2. Polinomio Característico
Para hallar analíticamente los autovalores de una matriz $A$, se parte de la ecuación $A \cdot X = \lambda \cdot X$. Reagrupando términos:
$$
AX - \lambda X = \vec{0} \implies (A - \lambda I) \cdot X = \vec{0}
$$

Para que existan soluciones no nulas (es decir, para que existan autovectores), el sistema homogéneo debe ser compatible indeterminado. Esto ocurre si y solo si el determinante de la matriz de coeficientes ($\lambda I - A$) es cero.

Se define el **Polinomio Característico** $p_A(\lambda)$ como:
$$
p_A(\lambda) = \det(A - \lambda I)
$$

**Regla de oro:** Las raíces del polinomio característico son exactamente los **autovalores** de la matriz $A$.

---

## 7.3. Autoespacios (Espacios Propios)
Cada autovalor $\lambda_i$ tiene asociado al menos un autovector. Se define el autoespacio asociado a $\lambda_i$ (denotado como $S_{\lambda_i}$) como el conjunto formado por el vector nulo y todos los autovectores asociados a ese autovalor.

Analíticamente, es el núcleo de la transformación $(A - \lambda_i I)$:  
$$
S_{\lambda_i} = \{ v \in V / A \cdot v = \lambda_i \cdot v \} = \text{Nu}(A - \lambda_i I)
$$
