# 8. Semejanza y Diagonalización de Matrices

* **Matrices Semejantes:** Dos matrices $A, B \in \mathbb{K}^{n \times n}$ son semejantes si existe una matriz $P$ regular (inversible) tal que:
  $$
  B = P^{-1} \cdot A \cdot P
  $$  
  Las matrices semejantes representan la misma transformación lineal, pero vista desde distintas bases.

* **Matriz Diagonalizable:** Una matriz $A$ es diagonalizable si es semejante a una matriz diagonal $D$. Es decir, si se puede escribir como:
  $$D = P^{-1} \cdot A \cdot P \quad \iff \quad A = P \cdot D \cdot P^{-1}$$

## 8.1. Teorema de Diagonalización
Una matriz $A \in \mathbb{K}^{n \times n}$ es diagonalizable **si y solo si** posee $n$ autovectores linealmente independientes (es decir, si sus autovectores forman una base de $\mathbb{K}^n$).

### 8.1.1. Construcción de una Matriz Diagonalizable
Si la matriz es diagonalizable, las matrices $P$ y $D$ se arman de la siguiente manera:
1.  **Matriz Diagonal ($D$):** Se colocan los autovalores $\lambda_i$ en la diagonal principal (el resto son ceros).
    $$
    D = \begin{bmatrix} \lambda_1 & 0 & \dots & 0 \\ 0 & \lambda_2 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & \lambda_n \end{bmatrix}
    $$

2.  **Matriz de Paso ($P$):** Se colocan los autovectores $v_i$ como **columnas**, respetando estrictamente el **mismo orden en el que se ubicaron los autovalores** en $D$.
    $$
    P = \Big[ v_1 \Big| v_2 \Big| \dots \Big| v_n \Big]
    $$
