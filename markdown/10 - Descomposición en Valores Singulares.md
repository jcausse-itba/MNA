# 10. Descomposición en Valores Singulares (SVD)
La descomposición SVD es una "generalización de la diagonalización" que permite trabajar con matrices que no son ni cuadradas ni diagonalizables tradicionalmente. Permite descomponer cualquier matriz $A \in \mathbb{R}^{n \times m}$ en:
$$
A = U \cdot S \cdot V^T
$$
Donde $U$ (de dimensión $n \times n$) y $V$ (de dimensión $m \times m$) son matrices ortogonales, y $S$ es una matriz pseudodiagonal que contiene los escalares denominados **valores singulares** ($\sigma_i$) ordenados de forma decreciente ($\sigma_1 \ge \sigma_2 \ge ... \ge 0$).

**Algoritmo paso a paso:**
* Calcular el producto matricial para obtener la matriz simétrica $A^T A$.
* Hallar las raíces del polinomio característico para extraer los autovalores $\lambda_i$ de $A^T A$. Los valores singulares de $A$ son, por definición, las raíces cuadradas de estos autovalores: $\sigma_i = \sqrt{\lambda_i}$.
* Construir la matriz $S$ ubicando los $\sigma_i$ en la diagonal principal ordenados descendentemente (y rellenando con ceros si sobran dimensiones).
* Hallar los autovectores asociados a cada $\lambda_i$, normalizarlos al módulo unitario y ubicarlos como columnas en su orden respectivo para formar la matriz ortogonal $V$.
* Para construir la matriz ortogonal $U$, calcular cada columna $u_i$ asociada a un valor singular no nulo resolviendo la relación: $u_i = \frac{1}{\sigma_i} A \cdot v_i$.
* Si la matriz $U$ requiere más columnas para ser completamente cuadrada ($n \times n$), se deben completar con vectores ortonormales que pertenezcan al subespacio nulo del sistema homogéneo $A^T X = 0$.

**Ejemplo práctico:**
Dada una matriz no cuadrada $A$:
$$
A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \\ -1 & 1 \end{bmatrix} \implies A^T A = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}
$$
Los autovalores de $A^T A$ ordenados son $\lambda_1 = 3$ y $\lambda_2 = 2$. Luego, sus valores singulares son $\sigma_1 = \sqrt{3}$ y $\sigma_2 = \sqrt{2}$. La pseudodiagonal $S$ queda:
$$
S = \begin{bmatrix} \sqrt{3} & 0 \\ 0 & \sqrt{2} \\ 0 & 0 \end{bmatrix}
$$
Los correspondientes autovectores normalizados para armar $V$ resultan ser los vectores canónicos $v_1 = (0, 1)^T$ y $v_2 = (1, 0)^T$.
$$
V = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}
$$
Para $U$, calculamos las dos primeras columnas mediante $u_1 = \frac{A v_1}{\sigma_1}$ y $u_2 = \frac{A v_2}{\sigma_2}$. La tercera columna se completa buscando un vector perpendicular a $u_1$ y $u_2$ (con producto vectorial o buscando el núcleo).
$$
U = \begin{bmatrix} 1/\sqrt{3} & 1/\sqrt{2} & -1/\sqrt{6} \\ 1/\sqrt{3} & 0 & 2/\sqrt{6} \\ 1/\sqrt{3} & -1/\sqrt{2} & -1/\sqrt{6} \end{bmatrix}
$$
