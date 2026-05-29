# 10. Descomposición en Valores Singulares (SVD)
La descomposición SVD es una "generalización de la diagonalización" que permite trabajar con matrices que no son ni cuadradas ni diagonalizables tradicionalmente. Permite descomponer cualquier matriz $A \in \mathbb{R}^{n \times m}$ en:
$$
A = U \cdot S \cdot V^T
$$
Donde $U$ (de dimensión $n \times n$) y $V$ (de dimensión $m \times m$) son matrices ortogonales, y $S$ es una matriz pseudodiagonal que contiene los escalares denominados **valores singulares** ($\sigma_i$) ordenados de forma decreciente ($\sigma_1 \ge \sigma_2 \ge ... \ge 0$).

## 10.1. Algoritmo
* Calcular el producto matricial para obtener la matriz simétrica $A^T A$. Al ser simétrica y semidefinida positiva, esta operación nos garantiza matemáticamente que todos sus autovalores serán números reales y mayores o iguales a cero.
* Hallar las raíces del polinomio característico para extraer los autovalores $\lambda_i$ de $A^T A$. Esto se hace planteando $\det(A^TA - \lambda I) = 0$, del cual se obtiene una ecuación polinómica de variable $\lambda$, y luego buscando las raíces de dicho polinomio.
* Los valores singulares de $A$ son, por definición, las raíces cuadradas de estos autovalores: $\sigma_i = \sqrt{\lambda_i}$. Geométricamente, representan los factores de escala absolutos de la transformación lineal.
* Construir la matriz $S$ ubicando los $\sigma_i$ en la diagonal principal ordenados descendentemente ($\sigma_1 \ge \sigma_2 \ge \dots \ge 0$). Es fundamental recordar que $S$ debe tener **exactamente las mismas dimensiones que la matriz original $A$** ($n \times m$), por lo que se debe rellenar con filas o columnas compuestas enteramente por ceros si sobran dimensiones.
* Hallar los autovectores asociados a cada $\lambda_i$ resolviendo el sistema homogéneo $(A^T A - \lambda_i I) \cdot X = 0$. Luego, normalizarlos al módulo unitario (dividiendo cada vector por su norma) y ubicarlos como columnas respetando el estricto orden decreciente de sus autovalores para formar la matriz ortogonal $V$. Los vectores van en el mismo orden que los autovalores.
* Para construir la matriz ortogonal $U$, calcular cada columna $u_i$ asociada a un valor singular **no nulo** ($\sigma_i > 0$) resolviendo la relación matricial directa: $u_i = \frac{1}{\sigma_i} A \cdot v_i$.
* Si la matriz $U$ requiere más columnas para ser completamente cuadrada ($n \times n$), se deben completar con vectores ortonormales que pertenezcan al subespacio nulo de la matriz transpuesta (es decir, resolviendo el sistema homogéneo $A^T \cdot X = 0$). Si se obtiene más de un vector en este paso, se les debe aplicar Gram-Schmidt para garantizar que sean ortonormales entre sí y encajen en la matriz ortogonal.

## 10.2. Ejemplo
Dada la matriz no cuadrada $A$ de dimensiones $3 \times 2$:
$$
A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \\ -1 & 1 \end{bmatrix}
$$

**Paso 1: Matriz Simétrica y Valores Singulares.**
Calculamos el producto $A^T A$:
$$
A^T A = \begin{bmatrix} 1 & 0 & -1 \\ 1 & 1 & 1 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 0 & 1 \\ -1 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}
$$
Como, por casualidad, el resultado ya es una matriz diagonal, podemos leer sus autovalores directamente de la diagonal principal. Los ordenamos de forma decreciente: $\lambda_1 = 3$ y $\lambda_2 = 2$.
Sus respectivos valores singulares son las raíces: $\sigma_1 = \sqrt{3}$ y $\sigma_2 = \sqrt{2}$.

Construimos la matriz pseudodiagonal $S$. Como $A$ es de $3 \times 2$, la matriz $S$ debe tener obligatoriamente esas mismas dimensiones, rellenando con una fila de ceros al final:
$$
S = \begin{bmatrix} \sqrt{3} & 0 \\ 0 & \sqrt{2} \\ 0 & 0 \end{bmatrix}
$$

**Paso 2: Matriz Ortogonal V.**
Buscamos los autovectores asociados a $\lambda_1$ y $\lambda_2$ resolviendo el sistema $(A^T A - \lambda_i I) \cdot X = 0$.
* Para $\lambda_1 = 3$: Obtenemos el vector director $(0, 1)^T$. Al calcular su norma, ya es $1$, por lo que $v_1 = (0, 1)^T$.
* Para $\lambda_2 = 2$: Obtenemos el vector director $(1, 0)^T$. Su norma también es $1$, por lo que $v_2 = (1, 0)^T$.

Ubicamos estos vectores como columnas para formar $V$:
$$
V = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}
$$

**Paso 3: Matriz Ortogonal U.**
Calculamos las dos primeras columnas de $U$ utilizando la relación directa $u_i = \frac{1}{\sigma_i} A \cdot v_i$:
$$
u_1 = \frac{1}{\sqrt{3}} \begin{bmatrix} 1 & 1 \\ 0 & 1 \\ -1 & 1 \end{bmatrix} \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \frac{1}{\sqrt{3}} \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 1/\sqrt{3} \\ 1/\sqrt{3} \\ 1/\sqrt{3} \end{bmatrix}
$$
$$
u_2 = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 0 & 1 \\ -1 & 1 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ 0 \\ -1 \end{bmatrix} = \begin{bmatrix} 1/\sqrt{2} \\ 0 \\ -1/\sqrt{2} \end{bmatrix}
$$

Como $U$ debe ser una matriz cuadrada de $3 \times 3$, necesitamos encontrar una tercera columna $u_3$ que sea ortonormal a las otras dos. Matemáticamente, este vector debe pertenecer al núcleo de la matriz transpuesta ($A^T \cdot X = 0$):
$$
\begin{bmatrix} 1 & 0 & -1 \\ 1 & 1 & 1 \end{bmatrix} \cdot \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies \begin{cases} x - z = 0 \implies x = z \\ x + y + z = 0 \implies y = -2z \end{cases}
$$
Si le asignamos el valor $z = -1$ (valor completamente arbitrario, solo debe ser distinto de cero), obtenemos el vector director $(-1, 2, -1)^T$. Al calcular su norma obtenemos $\sqrt{(-1)^2 + 2^2 + (-1)^2} = \sqrt{6}$. Dividiendo el vector por su norma, hallamos $u_3$:
$$
u_3 = \begin{bmatrix} -1/\sqrt{6} \\ 2/\sqrt{6} \\ -1/\sqrt{6} \end{bmatrix}
$$

Finalmente, ensamblamos la matriz $U$ juntando los tres vectores calculados:
$$
U = \begin{bmatrix} 1/\sqrt{3} & 1/\sqrt{2} & -1/\sqrt{6} \\ 1/\sqrt{3} & 0 & 2/\sqrt{6} \\ 1/\sqrt{3} & -1/\sqrt{2} & -1/\sqrt{6} \end{bmatrix}
$$
