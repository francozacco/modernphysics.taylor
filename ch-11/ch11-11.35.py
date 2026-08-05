
import matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np
matplotlib.use('TkAgg')


def A_n_odd_fn(n):
    factor = 4 / (math.pi * n)
    return factor * math.sin(n * math.pi / 2)

def A_n_even_fn(n):
    factor = 4 / ((math.pi * n)**2)
    first_term = math.pi * n * math.cos(n * math.pi / 2)
    sec_term = 2 * math.sin(n * math.pi / 2)
    return factor * (first_term - sec_term)

def psi_odd_fn(n,x):
    y = math.sqrt(2) * np.cos(n * math.pi * x)
    y[np.abs(x) > 0.5] = 0
    return y

def psi_even_fn(n,x):
    y = math.sqrt(2) * np.sin(n * math.pi * x)
    y[np.abs(x) > 0.5] = 0
    return y

def draw_square_wave(ax):
    x = [-1, -0.5, -0.5, 0.5, 0.5, 1]
    y = [0, 0, 2 * math.sqrt(2), 0, 0, 0]
    ax.plot(x, y, linewidth=2, label="psi(x)", color="black")

def main():
    x = np.arange(-1, 1, 0.001)
    fig, ax = plt.subplots(figsize=(10, 10))

    psi = A_n_odd_fn(1) * psi_odd_fn(1, x)
    for n in range(2, 6):
        if n % 2 == 0:
            psi += A_n_even_fn(n) * psi_even_fn(n, x)
        else:
            psi += A_n_odd_fn(n) * psi_odd_fn(n, x)
    ax.plot(x, psi, label="psi(x) 5 terms approx")

    psi = A_n_odd_fn(1) * psi_odd_fn(1, x)
    for n in range(2, 11):
        if n % 2 == 0:
            psi += A_n_even_fn(n) * psi_even_fn(n, x)
        else:
            psi += A_n_odd_fn(n) * psi_odd_fn(n, x)
    ax.plot(x, psi, label="psi(x) 10 terms approx")

    draw_square_wave(ax)
    ax.legend()

    plt.show()


if __name__ == "__main__":
    main()