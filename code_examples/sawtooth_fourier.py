import matplotlib.pyplot as plt
import math
from scipy import signal
import numpy as np

# x values
x = np.linspace(-10, 10, 100000, endpoint=True)

def generate(x, k):
    # y values initialization
    y = [0] * len(x)
    y_values = {}

    # Fourier series coefficients
    for k in range(1, k + 1):
        for i in range(len(x)):
            y[i] += 2 * (-1 if k % 2 == 0 else 1) * math.sin(k * x[i]) / k
        y_values[k] = y[:]

    return y, y_values

# Plot 1 (last value of K)
K = 10
y, _ = generate(x, K)

plt.plot(x, np.pi * signal.sawtooth([i + np.pi for i in x]), color='black', linestyle='--')
plt.plot(x, y)
plt.title(f"Sawtooth Fourier Series (K={K})")
plt.xlabel("x")
plt.ylabel("d(t)")
plt.grid()
plt.savefig('sawtooth_fourier_last_k.png')
plt.close()

# Plot 2 (all values of K)
K = 4
_, y_values = generate(x, K)

plt.plot(x, np.pi * signal.sawtooth([i + np.pi for i in x]), color='black', linestyle='--')
for k in y_values:
    plt.plot(x, y_values[k])
plt.title(f"Sawtooth Fourier Series (K in {{{', '.join([str(k) for k in range(1, K + 1)])}}})")
plt.xlabel("x")
plt.ylabel("d(t)")
plt.grid()
plt.savefig('sawtooth_fourier_all_k.png')
plt.close()
