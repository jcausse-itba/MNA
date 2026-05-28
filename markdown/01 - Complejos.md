# 01 - Números Complejos

## Unidad Imaginaria
Se define la unidad imaginaria $i$ de forma tal que:
$$ i^2 = -1$$

Entonces, las potencias de $i$ quedan dadas por:
$$
i ^0 = 1 \\
i^1 = i \\
i^2 = - 1 \\
i^3 = i^2 \cdot i = -i \\
$$

De forma general, se define:
$$
i^k = i^t, \space t \in \{0, 1, 2, 3\} \space \land \space k \equiv t (\text{mod } 4)
$$

o bien,
$$
\forall k \in \N,
\begin{cases}
i^{2k} = (-1)^k \\
i^{2k + 1} = (-1)^k i \\
\end{cases}
$$

---

## Número Complejo

> **Nota:** El cuerpo $\Complex$ de todos los números complejos es un cuerpo no ordenado, ya que no cumple los axiomas de orden que se cumlpen para $\R$.

Se define un número complejo $z$ de las siguientes dos formas:

### Forma Binómica
Dado por su parte real $Re(z)$ y su parte imaginaria $Im(z)$.
$$
z = a + bi \text{, donde } z \in \Complex, a = Re(z) \in \R, b = Im(z) \in \R
$$

Igualdad: $z = w \iff a_z = a_w \land b_z = b_w$.

### Forma Polar
Dado por su módulo $|z|$ y su argumento $arg(z)$ o ángulo $\varphi_z$.
$$
|z| = \sqrt{(a^2 + b^2)} \text{,  } |z| \in \R
$$
$$
\varphi = arg(z) = \arctan(b/a) \text{,  } \varphi \in \R
$$

Representaciones:
$$
z = (|z|, \varphi)
$$
$$
z = |z| \big(\cos(\varphi) + i \sin(\varphi) \big)
$$
$$
z = |z|e^{i \varphi}
$$

Igualdad: $z = w \iff |z| = |w| \land arg(z) = arg(w) + 2k \pi \text{,  } k \in \Z$ 

> **Importante:** El cálculo del argumento requiere un ajuste para los distintos cuadrantes.

### Propiedades

1. $|z| \ge 0 \land |z| = 0 \iff z = 0 + 0i$
2. $|zw| = |z||w| \space  \forall z, w \in \Complex$
3. $|z/w| = |z|/|w| \space \forall z, w \in \Complex, w \ne 0$
4. $|z + w| \le |z| + |w| \space \forall z, w \in \Complex$
5. $|z - w| \ge |z| - |w| \space \forall z, w \in \Complex$
6. $|Re(z)| \le |z| \land |Im(z)| \le |z| \space \forall z \in \Complex$
7. $arg(zw) = arg(z) + arg(w) \space  \forall z, w \in \Complex$
8. $arg(z/w) = arg(z) - arg(w) \space  \forall z, w \in \Complex, w \ne 0$
9. $arg(z^n) = n \space arg(z) \space  \forall z \in \Complex \space \forall n \in \N$
10. $arg(z^{-1}) = -arg(z) \space  \forall z \in \Complex - \{0\}$

Exponencial compleja de Euler:

$$
e^{i \varphi} = \cos(\varphi) + i \sin(\varphi) \space \forall \varphi \in \R
$$

---

## Complejo Conjugado

Sea $z \in \Complex$, se define su conjugado $\bar{z}$ como el único complejo que cumple:
$$
Re(\bar{z}) = Re(z) \land Im(\bar{z}) = -Im(z)
$$

### Propiedades
1. $z = \bar{z} \iff Im(z) = 0$
2. $\overline{z + w} = \bar{z} + \bar{w}$
3. $\overline{zw} = \bar{z} \bar{w}$
4. $\overline{z/w} = \bar{z} / \bar{w}$
5. $z \bar{z} = |z|^2$
6. $z + \bar{z} = 2 Re(z)$
7. $z - \bar{z} = 2 Im(z)$
8. $|z| = |\bar{z}|$
 
---

## Operaciones con Complejos

* Suma: Utilizar forma binómica. Sumar los $a$ y los $b$ por separado.
* Resta: Utilizar forma binómica. Restar los $a$ y los $b$ por separado.
* Multiplicación: Utilizar forma polar. Multiplicar los módulos según propiedad 2 y sumar los ángulos según propiedad 7.
* División: Utilizar forma polar. Dividir los módulos según propiedad 3 y restar los ángulos según propiedad 8.
* Potenciación: Elevar el módulo y multiplicar el ángulo según propiedad 9.
* Radicación: Dado $z$, existen $k$ complejos $w$ que son raíz n-ésima de $w$, dados por:
  $$
  w_k = \big(\sqrt[n]{|z|}, \frac{\varphi_z + 2k\pi}{n}\big) \text{,  } k \in \{0, 1, ..., n - 1\}
  $$
  
  En el caso particular de las raíces cuadradas:
  $$
  Re(w) = \pm \sqrt{\frac{|z| + Re(z)}{2}} \space \space \space \space, \space \space \space \space Im(w) = \pm \sqrt{\frac{|z| - Re(z)}{2}}
  $$
  Para elegir los signos se usa que $2Re(w)Im(w) = Im(z)$.
* Logaritmación: Existen infinitos $w_k$ tal que $w_k = \ln(z)$, dados por:
  $$
  w_k = \ln(|z|) + i(\varphi_z + 2k\pi) \text{,  } k \in \Z
  $$
  Se suele trabajar con $k = 0$.
* Potencia compleja:
  $$
  z^w = e^{w \ln(z)}
  $$
