# 13. Serie Trigonométrica de Fourier

## 13.1. Aproximación

La Serie Trigonométrica de Fourier se basa en expresar una función $f(x)$ como una sumatoria infinita (una serie) de otras funciones, de la siguiente forma:

$$
f(t) = \sum_{n = 1}^{\infty} f_n(t)
$$

Las mejores funciones $f_n$ que podemos utilizar suelen ser funciones periódicas. En este sentido, llamamos a la serie "trigonométrica" debido a que utilizamos funciones trigonométricas como $\sin(t)$ o $\cos(t)$ (ya que son funciones periódicas "buenas", en el sentido de que tienen propiedades convenientes: son continuas, derivables, etc.).

Estas funciones periódicas deben ser funciones $f: \R \rightarrow \R$ periódicas de período $T$, es decir:

$$
f(t) = f(t + T)
$$

Se busca expresar a $f(t)$ como:

$$
f(t) = \frac{a_0}{2} + \sum_{n = 1}^{\infty} \bigg( a_n \cos(\omega_n t) + b_n \sin(\omega_n t) \bigg)
$$

donde:

$$
\omega_n = \frac{2 \pi}{T} n = 2 \pi f_n \qquad \text{y} \qquad \omega_{n + 1} \ge \omega_n
$$

$$
\frac{a_0}{2} = \frac{1}{T} \int_T f(t) dt
$$

$$
a_n = \frac{2}{T} \int_T f(t) \cos(\omega_n t) dt
$$

$$
b_n = \frac{2}{T} \int_T f(t) \sin(\omega_n t) dt
$$

Todas las integrales son sobre intervalos de longitud igual a un período de la función, puede ser $[0, T]$, $[-T/2, T/2]$, etc. El intervalo puede elegirse de la forma que resulte más conveniente.

### 13.1.1. Truco de las funciones pares e impares

Para hacer más fácil estas integrales, es útil recordar lo siguiente:

$$
\int_{-a}^{a} f(t) dt = \begin{cases}
0 \qquad \text{si } f \text { es impar, es decir, } f(t) = -f(-t) \\
2 \int_{0}^{a} f(t) dt \qquad \text{si } f \text{ es par, es decir, } f(t) = f(-t)
\end{cases}
$$

Además, al multiplicar entre sí funciones pares o impares, se cumple que:

* $\text{Par} \cdot \text{Par} = \text{Par}$
* $\text{Impar} \cdot \text{Impar} = \text{Par}$
* $\text{Par} \cdot \text{Impar} = \text{Impar}$
* $\text{Impar} \cdot \text{Par} = \text{Impar}$


## 13.2. Formas de la Serie de Fourier

Existen tres formas equivalentes de escribir la serie de Fourier. La elección entre una u otra dependerá de la aplicación y la complejidad matemática del problema.

**1. Forma Trigonométrica:**
Es la forma clásica detallada en la sección anterior.
$$
f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \bigg( a_n \cos(\omega_n x) + b_n \sin(\omega_n x) \bigg)
$$

**2. Forma de Laboratorio:**
Muy recomendada en aplicaciones reales, agrupa la suma de senos y cosenos de una misma frecuencia en un único coseno con un ángulo de desfase.
$$
f(x) = p_0 + \sum_{n=1}^{\infty} p_n \cos(\omega_n x + \varphi_n)
$$
Donde:
* $p_0 = a_0 / 2$
* $p_n = \sqrt{a_n^2 + b_n^2}$ (Magnitud o amplitud del armónico)
* $\varphi_n = -\arctan(b_n / a_n)$ (Fase)

**3. Forma Exponencial:**
Utiliza exponenciales complejas en lugar de funciones trigonométricas.
$$
f(x) = \sum_{n=-\infty}^{\infty} c_n e^{i \omega_n x}
$$
Donde:
* $c_0 = a_0 / 2$
* $c_n = \frac{a_n - i b_n}{2}$
* $c_{-n} = \frac{a_n + i b_n}{2} = \overline{c_n}$


## 13.3. Cálculo de Coeficientes

### 13.3.1. Algoritmo paso a paso
* **Paso 1:** Identificar el período $L$ (o $T$) de la función y su frecuencia angular $\omega_n = \frac{2\pi n}{L}$.
* **Paso 2:** Analizar gráficamente la paridad. Si la función es par, calcular solo $a_0$ y $a_n$ (ya que $b_n = 0$). Si es impar, calcular solo $b_n$ (ya que $a_0 = 0$ y $a_n = 0$).
* **Paso 3:** Calcular la componente continua ($a_0/2$) integrando la función sobre un período y dividiendo por $L$.
* **Paso 4:** Plantear y resolver las integrales para $a_n$ y $b_n$ multiplicando la función por $\cos(\omega_n x)$ y $\sin(\omega_n x)$ respectivamente.
* **Paso 5:** Reemplazar los coeficientes hallados en la fórmula general de la sumatoria.

### 13.3.2. Ejemplo: Función Mantisa
Se desea hallar el desarrollo en serie de Fourier de la función $f(x) = x - [x]$. Su período es $L = 1$, por lo que $\omega_n = 2\pi n$.
* **Cálculo de $a_0/2$:**
  $$ \frac{a_0}{2} = \int_0^1 x dx = \frac{x^2}{2} \bigg|_0^1 = \frac{1}{2} $$
* **Cálculo de $a_n$:**
  $$ a_n = 2 \int_0^1 x \cos(2\pi n x) dx = 0 $$
* **Cálculo de $b_n$:**
  $$ b_n = 2 \int_0^1 x \sin(2\pi n x) dx = 2 \bigg[ \frac{\sin(2\pi n x)}{(2\pi n)^2} - \frac{x \cos(2\pi n x)}{2\pi n} \bigg]_0^1 = -\frac{1}{\pi n} $$
* **Resultado final:**
  $$ f(x) = \frac{1}{2} - \sum_{n=1}^{\infty} \frac{1}{n\pi} \sin(2\pi n x) $$


## 13.4. Errores de Aproximación e Identidad de Parseval

Al aproximar una función $f(x)$ tomando solo los primeros $N$ términos de la serie (truncamiento), se comete un error. El **Error Cuadrático Medio ($E_N$)** suministra una medida de la "energía" que se pierde en la aproximación sobre todo el período.

> **Propiedad fundamental:** Los coeficientes de Fourier ($a_n, b_n$) son exactamente los valores que hacen que este error $E_N$ sea mínimo.

**Identidad de Parseval:**
Establece que, si tomamos infinitos términos, la energía total de la señal en el tiempo es igual a la suma de las energías de todos sus armónicos:
$$
\frac{1}{L} \int_L |f(x)|^2 dx = \frac{a_0^2}{4} + \frac{1}{2} \sum_{n=1}^{\infty} (a_n^2 + b_n^2)
$$

**Desigualdad de Bessel:**
Es el corolario directo de Parseval para una aproximación truncada. Indica que la energía de la serie finita (hasta $N$) siempre es menor o igual a la energía de la función original.


## 13.5. Convergencia y Teorema de Dirichlet

Hasta aquí se dio un tratamiento formal asumiendo que la serie converge a la función, pero deben cumplirse ciertas condiciones.

Para asegurar la convergencia, la función debe ser **seccionalmente continua** (o continua por tramos), lo que implica que puede tener discontinuidades, pero deben ser saltos finitos y la función debe permanecer acotada.

**Teorema de Convergencia (Dirichlet):**
Si $f(x)$ es periódica de período $L$ y continua por tramos, la serie de Fourier converge a:
* $f(x_0)$ si la función es continua en ese punto.
* $\frac{f(x_0^+) + f(x_0^-)}{2}$ en cada punto de discontinuidad (es decir, converge exactamente al promedio matemático de los límites laterales de ese salto).

> **Corolario (Lema de Riemann-Lebesgue):** Como la energía de la señal es finita (el área bajo la curva no es infinita), los coeficientes deben decaer hacia cero cuando la frecuencia tiende a infinito. Por lo tanto, $\lim_{n \rightarrow \infty} a_n = 0$ y $\lim_{n \rightarrow \infty} b_n = 0$.


## 13.6. Derivación e Integración de Series

* **Derivación:** Si $f$ y su derivada $f'$ son seccionalmente continuas, se puede derivar la serie término a término:
  $$
  f'(x) = \sum_{n=1}^{\infty} \bigg( \omega_n b_n \cos(\omega_n x) - \omega_n a_n \sin(\omega_n x) \bigg)
  $$
* **Integración:** Definiendo $F(x) = \int_0^x f(t) dt$, se puede integrar la serie término a término:
  $$
  F(x) = \frac{a_0}{2}x + \sum_{n=1}^{\infty} \bigg( -\frac{b_n}{\omega_n} \cos(\omega_n x) + \frac{a_n}{\omega_n} \sin(\omega_n x) \bigg)
  $$
  > **Cuidado:** Si la componente continua no es nula ($a_0 \neq 0$), aparece un término lineal ($\frac{a_0}{2}x$), por lo que la función $F(x)$ resultante **no será periódica**, y esa expresión dejará de representar estrictamente una serie de Fourier convencional.


## 13.7. Desarrollo de una Función No Periódica (Extensiones)

Si se tiene un problema definido en un intervalo cerrado $[0, k]$, la función no es naturalmente periódica. Sin embargo, para aplicar Fourier, podemos "extender" artificialmente la función hacia los negativos $[-k, 0]$ y luego repetirla periódicamente con período $L=2k$. 

Existen infinitas formas de extenderla, pero las dos más útiles para simplificar cálculos son:

* **Extensión Impar:**
  Se refleja la función definiendo $\tilde{f}(x) = -f(-x)$ para $-k \le x < 0$.
  Como la función resultante es impar, todos los $a_0 = 0$ y $a_n = 0$. La serie de Fourier resultante estará compuesta **exclusivamente por senos**.
* **Extensión Par:**
  Se refleja la función definiendo $\tilde{f}(x) = f(-x)$ para $-k \le x < 0$.
  Como la función resultante es par, todos los $b_n = 0$. La serie de Fourier resultante estará compuesta **exclusivamente por cosenos**.
