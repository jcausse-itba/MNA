# 6. Transformaciones Lineales

## 6.1. Definición de Transformación Lineal

Sean $V$ y $W$ dos espacios vectoriales definidos sobre el mismo cuerpo de escalares $\mathbb{K}$. Una función $T: V \rightarrow W$ es una **Transformación Lineal (TL)** si preserva la estructura algebraica de los espacios vectoriales bajo las operaciones de suma y producto por escalar. 

Para que una función sea una TL, debe cumplir estrictamente con las siguientes tres condiciones básicas:

1. **Aditividad (Preserva la suma de vectores):** 
   $$
   T(u + v) = T(u) + T(v) \quad \forall u, v \in V
   $$
2. **Homogeneidad (Preserva el producto por un escalar):** 
   $$
   T(\lambda \cdot v) = \lambda \cdot T(v) \quad \forall v \in V, \forall \lambda \in \mathbb{K}
   $$
3. **Preserva el elemento neutro:**
   $$
   T(0_V) = 0_W
   $$

> **Condición unificada (Criterio rápido):** En los exámenes, para demostrar `(1)` y `(2)` en un solo paso, se suele aplicar la combinación lineal de ambas propiedades:
> $$T(\alpha u + \beta v) = \alpha T(u) + \beta T(v) \quad \forall u, v \in V, \forall \alpha, \beta \in \mathbb{K}$$

> **Descarte rápido:**. Si al evaluar la función en el vector nulo el resultado es distinto de cero, la función **no es una transformación lineal**. (Cuidado: que dé cero no asegura que lo sea, pero que no dé cero asegura que no lo es).

> **Nota:** Si $V$ = $W$, entonces $T: V \rightarrow V$. $T$ es un **endomorfismo**.

### 6.1.1. Propiedades Inmediatas (Consecuencias de la definición)
Si se demuestra que $T$ es una transformación lineal, se cumplen de forma directa las siguientes propiedades:

* **Mapeo del vector nulo:** La imagen del vector nulo del espacio de salida $V$ siempre es el vector nulo del espacio de llegada $W$.
  $$
  T(0_V) = 0_W
  $$
* **Mapeo del inverso aditivo:** La transformación del opuesto de un vector es igual al opuesto de su transformación.
  $$T(-v) = -T(v) \quad \forall v \in V$$

---

## 6.2. Núcleo e Imagen de una Transformación Lineal

Dada una transformación lineal $T: V \rightarrow W$, existen dos subconjuntos fundamentales (que además tienen la estructura de subespacios vectoriales) asociados a ella: el **Núcleo** (asociado al espacio de salida $V$) y la **Imagen** (asociada al espacio de llegada $W$).

### 6.2.1. El Núcleo (Kernel)
El **Núcleo** de una transformación lineal $T$ (denotado como $N(T)$ o $\text{Nu}(T)$) es el conjunto de todos los vectores del espacio de salida $V$ que, al aplicárseles la transformación, se mapean directamente al vector nulo del espacio de llegada $W$.

$$
\text{Nu}(T) = \{ v \in V : T(v) = 0_W \}
$$

**Propiedades del Núcleo:**
1. **Es un subespacio:** $\text{Nu}(T)$ es siempre un subespacio vectorial del espacio de salida $V$.
2. **Dimensión (Nulidad):** A la dimensión del núcleo ($dim(\text{Nu}(T))$) se la conoce formalmente como la *nulidad* de la transformación lineal.
3. **Interpretación práctica:** Hallar el núcleo equivale a resolver un sistema de ecuaciones lineales homogéneo ($A \cdot x = 0$).

### 6.2.2. La Imagen (Recorrido)
El otro subconjunto es la **Imagen** (denotada como $\text{Im}(T)$ o $R(T)$). Es el conjunto de todos los vectores del espacio de llegada $W$ que tienen, al menos, una preimagen en el espacio de salida $V$. En términos sencillos, representa a todos los vectores que pueden ser "alcanzados" por la función.

$$
\text{Im}(T) = \{ w \in W : \exists v \in V / T(v) = w \}
$$

**Propiedades de la Imagen:**
1. **Es un subespacio:** $\text{Im}(T)$ es siempre un subespacio vectorial del espacio de llegada $W$.
2. **Generadores automáticos:** Si $\{v_1, v_2, ..., v_n\}$ es una base del espacio de salida $V$, entonces el conjunto de sus imágenes $\{T(v_1), T(v_2), ..., T(v_n)\}$ es, de forma garantizada, un conjunto de generadores de la imagen.
   $$\text{Im}(T) = gen(\{T(v_1), T(v_2), ..., T(v_n)\})$$
3. **Dimensión (Rango):** A la dimensión de la imagen ($dim(R(T))$) se la conoce como el *rango* de la transformación lineal (habitualmente denotado como $\rho(T)$ o $rango(T)$).

### 6.2.3. Guía Práctica de Examen: ¿Cómo calcularlos?

Cuando se trabaja con coordenadas y se tiene la matriz asociada a la transformación lineal $[T]_{B_V \rightarrow B_W}$:

> **Nota:** La matriz asociada tiene dimensión $m \times n$, donde $dim(V) = n$ y $dim(W) = m$. Ver `6.8.`.

1. **Para calcular el Núcleo:** Plantear y resolver el sistema homogéneo utilizando la matriz asociada como matriz de coeficientes:
   $$
   [T]_{B_V \rightarrow B_W} \cdot [v]_{B_V} = 0_W
   $$
   Multiplicar la matriz de la transformación lineal por el vector vertical de variables y resolver el sistema de ecuaciones por Gauss-Jordan. Las variables libres (aquellas que no queden en función de otras) proveerán los vectores paramétricos que conforman la base del núcleo. La dimensión del núcleo es igual a la cantidad de grados de libertad (cantidad de variables libres) que quedan.

2. **Para calcular la Imagen:**
   * **Método por generadores (el más rápido):** Se toman los vectores de la base canónica del espacio de salida, se calculan sus transformados (aplicar $T$) y se colocan esos vectores transformados como columnas (o filas) de una matriz. Luego se triangula para eliminar los vectores que sean linealmente dependientes (LD). Los vectores restantes (LI) forman la base de la imagen.
   * **Método por Matriz Asociada:** Las columnas de la matriz asociada $[T]_{B_V \rightarrow B_W}$ ya son un conjunto de generadores de la imagen (expresados en las coordenadas de la base $B_W$). Solo debes seleccionar las columnas que sean linealmente independientes tras el proceso de escalonamiento.

---

## 6.3. Caracterización de una Transformación Lineal (TL)
Dada una Transformación Lineal $T: V \rightarrow W$, podemos clasificarla analizando su Núcleo ($N(T)$) y su Imagen ($R(T)$ o $Im(T)$):

* **Inyectiva (Monormorfismo):** Una TL es inyectiva si y solo si su núcleo contiene únicamente al vector nulo.
    $$
    N(T) = \{0_V\} \implies dim(N(T)) = 0
    $$
    *Demostración rápida:* Si $T(v_1) = T(v_2) \implies T(v_1) - T(v_2) = 0 \implies T(v_1 - v_2) = 0 \implies v_1 - v_2 \in N(T)$. Como el núcleo es solo el $\{0\}$, entonces $v_1 - v_2 = 0 \implies v_1 = v_2$.
* **Sobreyectiva (Epimorfismo):** Una TL es sobreyectiva si su Imagen cubre todo el espacio de llegada (Codominio).
    $$
    R(T) = W
    $$
    Esto significa que $\forall w \in W, \exists v \in V : w = T(v)$.
* **Biyectiva (Isomorfismo):** Es biyectiva si es simultáneamente inyectiva y sobreyectiva.

---

## 6.4. Teorema de las Dimensiones
Este es uno de los teoremas más importantes de la materia y sirve para verificar cálculos. Sean $V$ y $W$ espacios vectoriales de dimensión finita, y $T: V \rightarrow W$ una TL, se cumple siempre que:

$$
dim(V) = dim(N(T)) + dim(R(T))
$$
*(La dimensión del espacio de salida $V$ es igual a la dimensión del núcleo $N(T)$ más la dimensión de la imagen $R(T)$).*

### 6.4.1. Corolario
Si la **dimensión del espacio de salida $V$** es **igual a la del espacio de llegada $W$** ($dim(V) = dim(W)$), entonces las condiciones colapsan y:
$$
T \text{ es inyectiva} \iff T \text{ es sobreyectiva}
$$

o, equivalentemente,
$$
dim(N(T)) = 0 \iff dim(R(T)) = dim(V) = dim(W)
$$

> **Nota:** La primera de las igualdades a la derecha de $\iff$ se debe al teorema, y la segunda a la condición asumida por el corolario.

---

## 6.5. Teorema de Existencia y Unicidad de una TL
Este teorema asegura que **una Transformación Lineal queda unívocamente definida si sabemos cómo transforma a los vectores de una base**.

Sean $V, W$ espacios vectoriales. Si $B = \{v_1, ..., v_n\}$ es una **base** de $V$, y tomamos vectores cualesquiera $\{w_1, ..., w_n\} \subseteq W$, entonces existe una **única** Transformación Lineal tal que $T(v_i) = w_i$ para todo $i$.

---

## 6.6. Ejemplos para Exámenes

### 6.6.1. Ejercicio de Examen: Análisis de Existencia y Unicidad
Si te dan un conjunto de vectores transformados (ej: $T(v_1) = w_1, T(v_2) = w_2, T(v_3) = w_3$) y te piden analizar si la TL existe y si es única, los pasos son:

1.  **¿Los vectores de salida ($v_1, v_2, v_3$) son forman una base de $V$?**
    * **SÍ:** Por el Teorema de Existencia y Unicidad, la TL **existe y es única**.
    * **NO (Son LD):** Existe una dependencia lineal (ejemplo: $v_3 = \alpha v_1 + \beta v_2$). Pasamos al paso 2.
2.  **Verificar la compatibilidad de las imágenes (Solo si son LD):**
    Dado que $T$ debe ser lineal, la dependencia geométrica debe mantenerse en las imágenes. Se debe chequear si:
    $$w_3 = \alpha w_1 + \beta w_2$$
    * **Si se cumple la igualdad:** La TL **existe, pero NO es única** (hay infinitas formas de definir a dónde van los vectores que faltan para completar una base).
    * **Si NO se cumple la igualdad:** Hay una contradicción matemática. La TL **NO existe**.

### 6.6.2. Casos Prácticos de Funciones: ¿Son o no son TL?

**Caso 1: Rango de una matriz**
* $T: \mathbb{R}^{2\times2} \rightarrow \mathbb{R}$ definida como $T(A) = \rho(A)$ (Rango de la matriz).
* **NO es TL.** El rango no distribuye con la suma: $\rho(A+B) \neq \rho(A) + \rho(B)$. 

**Caso 2: Suma de la matriz con su transpuesta**
* $T: \mathbb{R}^{n\times n} \rightarrow \mathbb{R}^{n\times n}$ definida como $T(A) = A + A^T$.
* **SÍ es TL.** Cumple $T(A+B) = T(A) + T(B)$ y $T(\lambda A) = \lambda T(A)$.
* **Núcleo:** $T(A) = 0 \implies A + A^T = 0 \implies A = -A^T$. El núcleo está formado por todas las **matrices antisimétricas**.
* **Imagen:** La suma de una matriz y su transpuesta siempre da como resultado una matriz simétrica. Por lo tanto, la imagen son todas las **matrices simétricas**.

---

## 6.7. Coordenadas de un Vector en una Base
Sea $V$ un espacio vectorial de dimensión $n$ y $B = \{v_1, v_2, ..., v_n\}$ una base de $V$. Todo vector $v \in V$ se puede escribir de forma única como combinación lineal de los elementos de la base:
$$
v = \alpha_1 v_1 + \alpha_2 v_2 + ... + \alpha_n v_n
$$

Se define el **vector de coordenadas** de $v$ en la base $B$ (notado como $[v]_B$) al vector columna formado por los escalares de la combinación lineal:
$$
[v]_B = \begin{bmatrix} \alpha_1 \\ \alpha_2 \\ \vdots \\ \alpha_n \end{bmatrix} \in \mathbb{K}^n
$$

### 6.7.1. Isomorfismo fundamental
La función que asigna a cada vector sus coordenadas ($\varphi(v) = [v]_B$) es una Transformación Lineal biyectiva (un isomorfismo). Esto implica que operar con vectores abstractos (polinomios, matrices, funciones) es algebraicamente idéntico a operar con sus vectores de coordenadas en $\mathbb{R}^n$ o $\mathbb{C}^n$. Formalmente: $V \cong \mathbb{K}^n$.

---

## 6.8. Matriz Asociada a una Transformación Lineal
Sean $V$ (con $dim(V) = n$) y $W$ (con $dim(W) = m$) espacios vectoriales con bases $B_V = \{v_1, ..., v_n\}$ y $B_W = \{w_1, ..., w_m\}$ respectivamente. Dada una TL $T: V \rightarrow W$, se puede representar toda la transformación mediante una única matriz $A$ (o $M_{B_V \rightarrow B_W}$), de dimensiones $m \times n$.

La ecuación fundamental que relaciona la TL abstracta con su versión matricial es:
$$
[T(v)]_{B_W} = M_{B_V \rightarrow B_W} \cdot [v]_{B_V}
$$

**¿Cómo se construye esta matriz?**
Cada columna de la matriz $M$ es el vector de coordenadas (en la base de llegada $B_W$) del transformado de cada vector de la base de salida $B_V$.
$$
M_{B_V \rightarrow B_W} = \Big[ [T(v_1)]_{B_W} \Big| [T(v_2)]_{B_W} \Big| \dots \Big| [T(v_n)]_{B_W} \Big]
$$
