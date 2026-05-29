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
