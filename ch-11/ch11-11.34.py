import matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np
matplotlib.use('TkAgg')


def A_n_fn(n):
    factor = (2 * math.sqrt(2)) / (math.pi * n)
    return factor * math.sin(n * math.pi / 2)


def psi_fn(n,x):
    y = math.sqrt(2) * np.cos(n * math.pi * x)
    y[np.abs(x) > 0.5] = 0
    return y

def draw_square_wave(ax):
    x = [-1, -0.5, -0.5, 0.5, 0.5, 1]
    y = [0, 0, 1, 1, 0, 0]
    ax.plot(x, y, linewidth=2, label="psi(x)", color="black")

def main():
    x = np.arange(-1, 1, 0.001)
    fig, ax = plt.subplots(figsize=(10, 10))

    psi = A_n_fn(1) * psi_fn(1, x)
    for n in [3, 5, 7, 9]:
        psi += A_n_fn(n) * psi_fn(n, x)
    ax.plot(x, psi, label="psi(x) 5 terms approx")

    psi = A_n_fn(1) * psi_fn(1, x)
    for n in [3, 5, 7, 9, 11, 13, 15, 17, 19]:
        psi += A_n_fn(n) * psi_fn(n, x)
    ax.plot(x, psi, label="psi(x) 10 terms approx")

    draw_square_wave(ax)
    ax.legend()

    plt.show()


if __name__ == "__main__":
    main()