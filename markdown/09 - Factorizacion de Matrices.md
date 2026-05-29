# 9. Factorización de Matrices

## 9.1. Factorización LU
Permite descomponer una matriz cuadrada $A$ en el producto de una matriz triangular inferior $L$ (Lower) y una triangular superior $U$ (Upper). Resulta de gran utilidad para resolver sistemas $AX = B$ minimizando cálculos computacionales y sin necesidad de calcular la matriz inversa general.

### 9.1.1. Algoritmo
* Aplicar el método de eliminación de Gauss sobre la matriz $A$ para llevarla a una forma triangular superior. 
  * **Importante:** Solo están permitidas las operaciones elementales de suma de múltiplos de filas del tipo $F_i = F_i - m \cdot F_j$. No se pueden intercambiar filas ni multiplicar una fila por un escalar.
  * **Importante:** La eliminación se realiza avanzando columna por columna (de izquierda a derecha). En cada columna, se utiliza el elemento de la diagonal (pivote) para anular todos los elementos que están *debajo* de él, avanzando de arriba hacia abajo.


* La matriz resultante al final del escalonamiento es directamente la matriz $U$.
* Registrar cada uno de los multiplicadores $m_{ij}$ utilizados para generar los ceros debajo de la diagonal. La regla general para el multiplicador es: $m_{ij} = \frac{\text{elemento a eliminar}}{\text{pivote}}$.
* Construir la matriz $L$ colocando unos ($1$) en su diagonal principal y ubicando cada multiplicador $m_{ij}$ en la misma posición $(i,j)$ donde se eliminó el elemento correspondiente.

> **Importante:** Si durante el proceso de triangulación aparece un cero en la diagonal, no se puede seguir aplicando este método. Hay que aplicar factorización PLU en su lugar. Ver apartado `9.2.`.

### 9.1.2. Ejemplo
Dada la matriz $A$:
$$
A = \begin{bmatrix} 1 & 2 & 4 \\ 3 & 8 & 14 \\ 2 & 6 & 13 \end{bmatrix}
$$

**Paso 1: Eliminar elementos debajo del pivote de la primera columna ($a_{11} = 1$).**
* Para anular el $3$ de la Fila 2, el multiplicador es $m_{21} = \frac{3}{1} = 3$. Operación: $F_2 = F_2 - 3 \cdot F_1$.
* Para anular el $2$ de la Fila 3, el multiplicador es $m_{31} = \frac{2}{1} = 2$. Operación: $F_3 = F_3 - 2 \cdot F_1$.

Aplicando estas operaciones, la matriz se transforma en:
$$
\begin{bmatrix} 1 & 2 & 4 \\ 0 & 2 & 2 \\ 0 & 2 & 5 \end{bmatrix}
$$

**Paso 2: Eliminar elementos debajo del nuevo pivote de la segunda columna ($a_{22} = 2$).**
* Para anular el $2$ de la Fila 3, el multiplicador es $m_{32} = \frac{2}{2} = 1$. Operación: $F_3 = F_3 - 1 \cdot F_2$.

Aplicando esta última operación, obtenemos la matriz triangular superior, que es directamente $U$:
$$
U = \begin{bmatrix} 1 & 2 & 4 \\ 0 & 2 & 2 \\ 0 & 0 & 3 \end{bmatrix}
$$

**Paso 3: Construir la matriz L.**
Tomamos los multiplicadores que fuimos calculando y los ubicamos en sus respectivas posiciones $(i, j)$ por debajo de una diagonal de unos:
$$
L = \begin{bmatrix} 1 & 0 & 0 \\ m_{21} & 1 & 0 \\ m_{31} & m_{32} & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 3 & 1 & 0 \\ 2 & 1 & 1 \end{bmatrix}
$$

## 9.2. Factorización PLU
Si durante el proceso de triangulación clásico aparece un cero en la diagonal (pivote nulo), es matemáticamente obligatorio intercambiar filas, lo cual rompe la estructura de la factorización LU estándar. Para solucionarlo de forma ordenada, se introduce una matriz de permutación $P$.
$$
P \cdot A = L \cdot U
$$

### 9.2.1. Algoritmo
* Comenzar con una matriz $P$ igual a la matriz identidad $I_n$.
* Cada vez que sea estrictamente necesario intercambiar dos filas en $A$ para continuar triangulando, aplicar exactamente el mismo intercambio a las filas de la matriz $P$.
* Las filas correspondientes a los multiplicadores $m_{ij}$ que ya fueron registrados en $L$ también deben intercambiarse de lugar si ocurre una permutación.
* Al finalizar, extraer $L$ y $U$ de manera normal habiendo trabajado, en efecto, sobre la matriz permutada $P \cdot A$.

---

## 9.3. Factorización QR
Toda matriz $A \in \mathbb{K}^{n \times m}$ se puede descomponer como el producto de una matriz $Q$ ortogonal (cuyas columnas conforman una base ortonormal de $\mathbb{R}^n$ y cumple $Q^T Q = I$) y una matriz $R$ triangular superior.

**Algoritmo paso a paso:**
* Extraer ordenadamente las primeras columnas linealmente independientes de $A$ y tratarlas como vectores individuales $a_1, ..., a_k$.
* Aplicar el proceso de ortonormalización de Gram-Schmidt (ver sección `5.5.`) sobre estos vectores de columna para obtener una nueva base ortonormal $u_1, ..., u_k$.
* Construir la matriz $Q$ colocando los vectores ortonormales obtenidos ($u_i$) directamente como sus columnas.
* Calcular la matriz $R$ multiplicando la transpuesta de $Q$ por la matriz original $A$ ($R = Q^T A$).

**Ejemplo práctico:**
Dada la matriz $A$:
$$
A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \\ 1 & 0 \end{bmatrix}
$$
Extraemos la Columna 1 ($a_1 = (1, 0, 1)^T$) y la Columna 2 ($a_2 = (1, 1, 0)^T$).
Aplicando Gram-Schmidt, se obtienen $u_1$ y $u_2$, con los cuales se arma la matriz $Q$:
$$
Q = \begin{bmatrix} 1/\sqrt{2} & 1/\sqrt{6} \\ 0 & 2/\sqrt{6} \\ 1/\sqrt{2} & -1/\sqrt{6} \end{bmatrix}
$$
Finalmente, calculamos $R = Q^T A$:
$$
R = \begin{bmatrix} 2/\sqrt{2} & 1/\sqrt{2} \\ 0 & 3/\sqrt{6} \end{bmatrix}
$$

---

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

---

# 11. Mínimos Cuadrados y Matriz Pseudoinversa

En aplicaciones reales e ingeniería, se presentan sistemas $AX = B$ que son sobredeterminados (tienen más ecuaciones que incógnitas) y carecen de una solución algebraica exacta. En estos casos, se busca la solución aproximada $\hat{X}$ que logre minimizar analíticamente el error cuadrático global $||AX - B||^2$.

## 11.1. Ecuaciones Normales
Desarrollando la derivada del error respecto a las variables y minimizando, se demuestra que el vector $X$ óptimo satisface siempre un nuevo sistema consistente denominado **Ecuaciones Normales**:
$$
A^T \cdot A \cdot X = A^T \cdot B
$$

**Algoritmo paso a paso:**
* Multiplicar a izquierda en ambos términos de la igualdad del sistema original inconsistente por la matriz transpuesta $A^T$.
* Resolver el nuevo sistema cuadrado resultante $A^T A \cdot X$ para obtener la solución óptima (por ejemplo, triangulando por Gauss-Jordan).

## 11.2. Matriz Pseudoinversa de Moore-Penrose
Si la matriz cuadrada proveniente de las ecuaciones normales ($A^T A$) resulta ser regular (o lo que es lo mismo, $det(A^T A) \neq 0$), el sistema posee solución única y se puede despejar multiplicando ambos miembros por su matriz inversa.
$$
X = (A^T A)^{-1} A^T \cdot B
$$
Al bloque analítico $(A^T A)^{-1} A^T$ se lo denomina **Matriz Pseudoinversa** y se lo denota simbólicamente como $A^+$.

**Algoritmo paso a paso:**
* Construir el producto matricial $A^T A$ y verificar rápidamente que su determinante no sea nulo.
* Proceder a calcular la matriz inversa propiamente dicha: $(A^T A)^{-1}$.
* Multiplicar esa nueva inversa a derecha por la matriz transpuesta $A^T$ para finalizar y conformar $A^+$.
* Evaluar que la mejor aproximación al resultado deseado del sistema original es el vector $\hat{X} = A^+ \cdot B$.

**Ejemplo práctico:**
Se busca aproximar $A X = B$ sabiendo que $A = \begin{bmatrix} 1 & 1 \\ 1 & -1 \\ 0 & 1 \end{bmatrix}$ y el vector independiente es $B = \begin{bmatrix} 2 \\ 0 \\ 1 \end{bmatrix}$.
Las matrices correspondientes a las Ecuaciones normales son:
$$
A^T A = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix} \quad , \quad A^T B = \begin{bmatrix} 2 \\ 3 \end{bmatrix}
$$
Calculamos la Pseudoinversa invirtiendo la matriz diagonal y multiplicando por $A^T$:
$$
A^+ = (A^T A)^{-1} A^T = \begin{bmatrix} 1/2 & 0 \\ 0 & 1/3 \end{bmatrix} \begin{bmatrix} 1 & 1 & 0 \\ 1 & -1 & 1 \end{bmatrix} = \begin{bmatrix} 1/2 & 1/2 & 0 \\ 1/3 & -1/3 & 1/3 \end{bmatrix}
$$
Finalmente, el vector que resuelve el modelo de Mínimos Cuadrados es:
$$
\hat{X} = A^+ B = \begin{bmatrix} 1 \\ 1 \end{bmatrix}
$$
