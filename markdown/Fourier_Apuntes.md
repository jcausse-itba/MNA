# 13. Series de Fourier

La Serie de Fourier formaliza la intuición vista anteriormente abordándola desde el álgebra lineal: se la entiende como una proyección ortogonal en un espacio vectorial de funciones (espacio de Hilbert).

## 13.1. Funciones Periódicas y Espacio L2
Considerando el espacio de funciones de energía finita (cuadrado integrables) $L^2([0,T])$ con el producto interno $\langle f, g 
\rangle = \int_0^T f(t) \overline{g(t)} dt$, el conjunto de exponenciales complejas forma una **Base Ortogonal**. Expresar una función en serie de Fourier es equivalente a hallar sus coordenadas en esta base.

## 13.2. Cálculo de Coeficientes

### 13.2.1. Algoritmo paso a paso (Forma Trigonométrica)
* **Paso 1:** Identificar el período $T$ de la función y la frecuencia angular $\omega_n = \frac{2\pi n}{T}$.
* **Paso 2:** Calcular la componente continua (valor medio) integrando a lo largo de un período:
    $$
    a_0 = \frac{2}{T} \int_T f(t) dt
    $$
* **Paso 3:** Calcular los coeficientes de los cosenos ($a_n$) y de los senos ($b_n$):
    $$
    a_n = \frac{2}{T} \int_T f(t) \cos(\omega_n t) dt \quad , \quad b_n = \frac{2}{T} \int_T f(t) \sin(\omega_n t) dt
    $$
* **Paso 4:** Ensamblar la serie: $f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} (a_n \cos(\omega_n t) + b_n \sin(\omega_n t))$.

> **Descarte rápido:** Si $f(t)$ es una función **impar** (simétrica respecto al origen), entonces su valor medio y todos los coeficientes de los cosenos son nulos ($a_0 = 0$, $a_n = 0$). Si es **par**, todos los coeficientes de los senos son nulos ($b_n = 0$).

### 13.2.2. Algoritmo paso a paso (Forma Exponencial)
* **Paso 1:** Identificar el período $T$.
* **Paso 2:** Calcular el coeficiente $c_n$ proyectando la función sobre la base de exponenciales:
    $$
    c_n = \frac{1}{T} \int_T f(t) e^{-i \frac{2\pi n}{T} t} dt
    $$
* **Paso 3:** Armar la serie sumando para todo $n \in \Z$:
    $$
    f(t) = \sum_{n=-\infty}^{\infty} c_n e^{i \frac{2\pi n}{T} t}
    $$

## 13.3. Identidad de Parseval
> **Nota:** Se define la **norma de una función** como: $||f||^2 = \int_a^b |f(t)|^2 dt$

La energía en el dominio del tiempo es idéntica a la energía proyectada en el dominio de las frecuencias:
$$
||f||^2 = \int_0^T |f(t)|^2 dt = T \sum_{n=-\infty}^{\infty} |c_n|^2
$$

## 13.4. Convergencia y Condiciones de Dirichlet
Para que la serie iguale a la función original punto a punto, esta debe cumplir las Condiciones de Dirichlet (tener un número finito de discontinuidades y extremos en un período). Esto implica que, si la función tiene una discontinuidad,

* En los puntos continuos, la serie converge exactamente a $f(t)$.
* En la discontinuidad sobre algún $t = t_0$, la serie converge al promedio de sus límites laterales:

$$
\underset{N \to \infty}{\lim} S_Nf(t_0) = \frac{f(t_0^{+}) + f(t_0^{-})}{2}
$$

### 13.4.1. Ejemplo
Dada una señal cuadrada que vale $1$ en $(0,1)$ y $-1$ en $(1,2)$. Esta función tiene un salto brusco en $t=1$.
* En los puntos continuos, la serie converge exactamente a $f(t)$.
* En la discontinuidad ($t=1$), la serie convergerá al promedio de sus límites laterales:
    $$
    f(1) = \frac{f(1^-) + f(1^+)}{2} = \frac{1 + (-1)}{2} = 0
    $$
