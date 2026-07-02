import matplotlib.pyplot as plt
import math
from scipy import signal
import numpy as np

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

def plot_common(title, filename, **kwargs):
    plt.plot(x, np.pi * signal.sawtooth([i + np.pi for i in x]), color='black', linestyle='--')
    plt.title(title)
    plt.xlabel("t")
    plt.ylabel("d(t)")
    plt.grid()
    plt.savefig(filename)
    plt.close()

# x values
x = np.linspace(-10, 10, 100000, endpoint=True)

###################################################################################
##############################   PLOTS   ##########################################
###################################################################################

# Plot 1 (last value of K)
K = 10
y, _ = generate(x, K)


plt.plot(x, y)
plot_common(f"Sawtooth Fourier Series (K={K})", 'img/sawtooth_fourier_last_k.png')

# Plot 2 (all values of K)
K = 4
_, y_values = generate(x, K)

for k in y_values:
    plt.plot(x, y_values[k])
plot_common(f"Sawtooth Fourier Series (K in {{{', '.join([str(k) for k in range(1, K + 1)])}}})", 'img/sawtooth_fourier_all_k.png')
