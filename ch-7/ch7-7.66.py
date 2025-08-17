
import matplotlib
import matplotlib.pyplot as plt
import math
from math import cos, sin
import numpy as np
from matplotlib.ticker import LinearLocator
from matplotlib import cm
matplotlib.use('TkAgg')


def plot_ux():
    x_values = np.linspace(-4, 4, 500)
    y_values = (1 - math.e**(-(x_values**2)))
    plt.plot(x_values, y_values, label=f"")
    plt.xlabel("x")
    plt.ylabel("U(x) and psi(x)")
    plt.legend()

def psi_dot(v):
    return v

def v_dot(m, E, x, psi):
    return 2 * m * (1 - (math.exp(-(x**2))) - E) * psi

def runge_kutta(m, E, x1, psi1, v1):
    h = 0.001

    steps = int(4 // h)
    
    x = [x1]
    psi = [psi1]
    v = [v1]
    for step in range(steps):
        c1 = v_dot(m, E, x[-1], psi[-1])
        d1 = psi_dot(v[-1])

        c2 = v_dot(m, E, x[-1] + (h / 2), psi[-1] + (h * c1 / 2))
        d2 = psi_dot(v[-1] + (h * d1 / 2))

        c3 = v_dot(m, E, x[-1] + (h / 2), psi[-1] + (h * c2 / 2))
        d3 = psi_dot(v[-1] + (h * d2 / 2))

        c4 = v_dot(m, E, x[-1] + h, psi[-1] + (h * c3))
        d4 = psi_dot(v[-1] + (h * d3))

        psi.append(psi[-1] + ((h / 6) * (d1 + (2 * d2) + (2 * d3) + d4)))
        v.append(v[-1] + ((h / 6) * (c1 + (2 * c2) + (2 * c3) + c4)))
        x.append(x1 + (h * step))

    return np.array(x), np.array(psi)

def main():
    fig, ax = plt.subplots(figsize=(10, 10))

    for E in np.arange(0.11, 0.12, 0.0005):
        m = 36
        x1 = -3
        psi1 = 1
        v1 = math.sqrt(2 * m * (1 - E))
        
        x, psi = runge_kutta(m, E, x1, psi1, v1)

        ax.plot(x, psi, label=f"E = {E}")

    ax.set_xlabel("x")
    ax.set_ylabel("psi(x)")
    ax.legend()

    plt.show()

if __name__ == "__main__":
    main()
