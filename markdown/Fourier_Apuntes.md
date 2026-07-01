


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


# 14. Transformadas de Fourier

Si se extiende el período de una señal al infinito ($T \to \infty$), las series (para señales periódicas) se convierten en integrales (para señales aperiódicas). De este modo, la frecuencia discreta se vuelve continua.

## 14.1. Definición Formal
Dada una función módulo integrable $x \in L^1(\R)$, su Transformada de Fourier (espectro) $X(f)$ se define analíticamente como:
$$
X(f) = \mathcal{F}\{x\} = \int_{-\infty}^{\infty} x(t) e^{-i 2\pi f t} dt
$$

Y su Transformada Inversa (para recuperar $x(t)$) es:
$$
x(t) = \mathcal{F}^{-1}\{X\} = \int_{-\infty}^{\infty} X(f) e^{i 2\pi f t} df
$$

> **Nota:** En ingeniería se utiliza frecuentemente la convención con frecuencia lineal $f$ en el exponente en lugar de la angular $\omega$ para evitar arrastrar factores asimétricos constantes como $1/(2\pi)$.

## 14.2. Propiedades Fundamentales
* **Linealidad:** $\mathcal{F}\{ax + by\} = aX(f) + bY(f)$
* **Desplazamiento temporal:** Retrasar en el tiempo gira la fase en frecuencia: $\mathcal{F}\{x(t - t_0)\} = X(f) e^{-i 2\pi f t_0}$
* **Escalamiento:** $\mathcal{F}\{x(at)\} = \frac{1}{|a|} X\left(\frac{f}{a} \right)$. Comprimir en tiempo ($a>1$) implica expandir en frecuencia (cambios bruscos en el tiempo requieren frecuencias muy altas).
* **Derivación:** $\mathcal{F}\{x'(t)\} = i 2\pi f \cdot X(f)$
* **Convolución:** Una convolución en el dominio temporal es equivalente a un simple producto en el dominio frecuencial. Esta es la base de los filtros LTI:
    $$
    \mathcal{F}\{x * y\} = X(f) \cdot Y(f)
    $$
* **Dualidad:** Si $X(f) = \mathcal{F}\{x(t)\}$, entonces invertir los dominios invierte el signo: $\mathcal{F}\{X(t)\} = x(-f)$.

## 14.3. Teorema de Plancherel ($L^2$)
Este teorema permite extender la transformada a funciones que no son módulo integrables pero que sí son cuadrado integrables (señales de energía). Conserva el producto interno, de forma que la energía global de la señal se mantiene invariable entre dominios:
$$
\int_{-\infty}^{\infty} |x(t)|^2 dt = \int_{-\infty}^{\infty} |X(f)|^2 df
$$

## 14.4. Funciones Generalizadas
Para operar con señales que no decaen, se usa la teoría de distribuciones (apoyada en la Delta de Dirac $\delta(t)$).
* $\mathcal{F}\{1\} = \delta(f)$ (La corriente continua o constante concentra absolutamente toda su energía en frecuencia cero).
* $\mathcal{F}\{\delta(t)\} = 1$ (Un impulso perfecto requiere excitar a todas las frecuencias existentes por igual).

### 14.4.1. Algoritmo paso a paso para Transformadas simples
* **Paso 1:** Plantear la integral de la definición reemplazando $x(t)$.
* **Paso 2:** Ajustar los límites de integración al intervalo donde la función sea estrictamente no nula.
* **Paso 3:** Integrar la función respecto al tiempo $t$ asumiendo a $f$ como una constante escalar, y evaluar por Barrow.
* **Paso 4:** Simplificar algebraicamente el resultado utilizando las identidades de Euler si quedan exponenciales simétricas.

### 14.4.2. Ejemplo
Transformada del Pulso Rectangular $\Pi(t)$ (vale $1$ para $|t| \le 1/2$ y $0$ fuera).
Aplicando los pasos del algoritmo:
$$
X(f) = \int_{-1/2}^{1/2} 1 \cdot e^{-i 2 \pi f t} dt = \left[ \frac{e^{-i 2\pi f t}}{-i 2\pi f} \right]_{-1/2}^{1/2}
$$
Evaluando los extremos y reescribiendo con Euler ($\sin(\theta) = \frac{e^{i \theta} - e^{-i \theta}}{2i}$):
$$
X(f) = \frac{e^{-i\pi f} - e^{i\pi f}}{-i 2\pi f} = \frac{\sin(\pi f)}{\pi f} = \text{sinc}(f)
$$
*Conclusión:* Un pulso cuadrado perfecto en el tiempo engendra un espectro en forma de lóbulo infinito ($\text{sinc}$) en el dominio frecuencial.
