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

---

## 9.2. Factorización PLU
Si durante el proceso de triangulación clásico aparece un cero en la diagonal (pivote nulo), es matemáticamente obligatorio intercambiar filas, lo cual rompe la estructura de la factorización LU estándar. Para solucionarlo de forma ordenada, se introduce una matriz de permutación $P$.
$$
P \cdot A = L \cdot U
$$

### 9.2.1. Algoritmo
* Comenzar con una matriz $P$ igual a la matriz identidad $I_n$.
* Aplicar el algoritmo de factorización LU visto en `9.1.`, pero manteniendo esta matriz $P$ del lado izquierdo de $A$.
* Cada vez que sea estrictamente necesario intercambiar dos filas en $A$ para continuar triangulando, aplicar exactamente el mismo intercambio a las filas de la matriz $P$.
* Las filas correspondientes a los multiplicadores $m_{ij}$ que ya fueron registrados en $L$ también deben intercambiarse de lugar si ocurre una permutación.
* Al finalizar, extraer $L$ y $U$ de manera normal habiendo trabajado, en efecto, sobre la matriz permutada $P \cdot A$.

### 9.2.2. Ejemplo
Dada la matriz $A$ y definiendo $P = I_3$:
$$
A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 1 \\ -1 & 1 & 2 \end{bmatrix} \quad , \quad P = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$

**Paso 1: Eliminar elementos debajo del pivote de la primera columna ($a_{11} = 1$).**
* Multiplicador $m_{21} = \frac{2}{1} = 2$. Operación: $F_2 = F_2 - 2 \cdot F_1$.
* Multiplicador $m_{31} = \frac{-1}{1} = -1$. Operación: $F_3 = F_3 - (-1) \cdot F_1 = F_3 + F_1$.

Aplicando las operaciones, la matriz se transforma en:
$$
\begin{bmatrix} 1 & 2 & 3 \\ 0 & 0 & -5 \\ 0 & 3 & 5 \end{bmatrix}
$$

**Paso 2: Pivote nulo y permutación.**
Al pasar a la segunda columna, el pivote en la diagonal es $a_{22} = 0$. Como no se puede dividir por cero para calcular los siguientes multiplicadores, estamos obligados a permutar la Fila 2 con la Fila 3 ($F_2 \leftrightarrow F_3$).

Esta permutación debe aplicarse a tres lugares simultáneamente:
1. **En la matriz de trabajo:**
   $$
   U = \begin{bmatrix} 1 & 2 & 3 \\ 0 & 3 & 5 \\ 0 & 0 & -5 \end{bmatrix}
   $$
   *(Como ya quedó triangular superior, esta es directamente nuestra matriz $U$).*
2. **En la matriz $P$:**
   $$
   P = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix}
   $$
3. **En los multiplicadores ya calculados:** Se intercambia de lugar el $m_{21}$ con el $m_{31}$. 
   Nuevos multiplicadores: $m_{21}' = -1$ y $m_{31}' = 2$.

**Paso 3: Construir la matriz L.**
Colocamos los multiplicadores (ya permutados) debajo de la diagonal de unos:
$$
L = \begin{bmatrix} 1 & 0 & 0 \\ m_{21}' & 1 & 0 \\ m_{31}' & 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 2 & 0 & 1 \end{bmatrix}
$$

> **Comprobación:** Puede verificarse fácilmente que se cumple la igualdad $P \cdot A = L \cdot U$.

---

## 9.3. Factorización QR
Toda matriz $A \in \mathbb{K}^{n \times m}$ se puede descomponer como el producto de una matriz $Q$ ortogonal (cuyas columnas conforman una base ortonormal de $\mathbb{R}^n$ y cumple $Q^T Q = I$) y una matriz $R$ triangular superior.

### 9.3.1. Algoritmo
* Extraer ordenadamente las primeras columnas linealmente independientes de $A$ y tratarlas como vectores individuales $a_1, ..., a_k$.
* Aplicar el proceso de ortonormalización de Gram-Schmidt (ver sección `5.5.`) sobre estos vectores de columna para obtener una nueva base ortonormal $u_1, ..., u_k$.
* Construir la matriz $Q$ colocando los vectores ortonormales obtenidos ($u_i$) directamente como sus columnas.
* Calcular la matriz $R$ multiplicando la transpuesta de $Q$ por la matriz original $A$ ($R = Q^T A$).

### 9.3.2. Ejemplo
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
