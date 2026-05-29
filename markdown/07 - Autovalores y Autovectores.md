# 7. Autovalores y Autovectores

## 7.1. Autovalores y Autovectores (Valores y Vectores Propios)
Sea $T: V \rightarrow V$ un operador lineal (o su matriz asociada $A \in K^{n \times n}$). 

Decimos que un vector $v \in V$ **no nulo** ($v \neq 0_V$) es un **autovector** de $T$ si, al aplicarle la transformación, el resultado es simplemente el mismo vector escalado por un número $\lambda \in K$.
$$T(v) = \lambda \cdot v \quad \iff \quad A \cdot X = \lambda \cdot X$$
A ese escalar $\lambda$ se lo llama **autovalor** asociado al autovector $v$.
*(Nota teórica: Un autovector jamás puede ser el vector nulo por definición, pero un autovalor sí puede ser $\lambda = 0$, lo que implicaría que el autovector pertenece al núcleo).*

---

## 4. Polinomio Característico
Para hallar analíticamente los autovalores de una matriz $A$, se parte de la ecuación $A \cdot X = \lambda \cdot X$. Reagrupando términos:
$$(\lambda I - A) \cdot X = 0$$
Para que existan soluciones no nulas (es decir, para que existan autovectores), el sistema homogéneo debe ser compatible indeterminado. Esto ocurre si y solo si el determinante de la matriz de coeficientes es cero.

Se define el **Polinomio Característico** $p_A(\lambda)$ como:
$$p_A(\lambda) = \det(\lambda I - A) \quad \text{o equivalentemente} \quad p_A(\lambda) = \det(A - \lambda I)$$

**Regla de oro:** Las raíces del polinomio característico son exactamente los **autovalores** de la matriz $A$.

---

## 5. Semejanza y Diagonalización

* **Matrices Semejantes:** Dos matrices $A, B \in K^{n \times n}$ son semejantes si existe una matriz $P$ regular (inversible) tal que $B = P^{-1} \cdot A \cdot P$. Las matrices semejantes representan la misma transformación lineal, pero vista desde distintas bases.
* **Matriz Diagonalizable:** Una matriz $A$ es diagonalizable si es semejante a una matriz diagonal $D$. Es decir, si se puede escribir como:
  $$D = P^{-1} \cdot A \cdot P \quad \iff \quad A = P \cdot D \cdot P^{-1}$$

### Teorema de Diagonalización
> Una matriz $A \in K^{n \times n}$ es diagonalizable **si y solo si** posee $n$ autovectores linealmente independientes (es decir, si sus autovectores forman una base de $K^n$).

**Construcción práctica (La receta del parcial):**
Si la matriz es diagonalizable, las matrices $P$ y $D$ se arman de la siguiente manera:
1.  **Matriz Diagonal ($D$):** Se colocan los autovalores $\lambda_i$ en la diagonal principal (el resto son ceros).
    $$D = \begin{bmatrix} \lambda_1 & 0 & \dots & 0 \\ 0 & \lambda_2 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & \lambda_n \end{bmatrix}$$
2.  **Matriz de Paso ($P$):** Se colocan los autovectores $v_i$ como **columnas**, respetando estrictamente el mismo orden en el que se ubicaron los autovalores en $D$.
    $$P = \Big[ v_1 \Big| v_2 \Big| \dots \Big| v_n \Big]$$