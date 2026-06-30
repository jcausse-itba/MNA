# 12. Serie Trigonométrica de Fourier

## 12.1. Aproximación

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
\omega_n = \frac{2 \pi}{T} n = 2 \pi f_n, \space \space \space \omega_{n + 1} \ge \omega_n
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

