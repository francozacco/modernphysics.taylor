import matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np
matplotlib.use('TkAgg')



def even_psi_fn(n,x):
    y = math.sqrt(2) * np.sin(n * math.pi * x)
    return y


def odd_psi_fn(n,x):
    y = math.sqrt(2) * np.cos(n * math.pi * x)
    return y


def approx_fn(x):
    A_1 = 16 / (9 * (math.pi**2))
    A_2 = 48 / (25 * (math.pi**2))
    y = (A_1 * odd_psi_fn(1, x)) - (A_2 * odd_psi_fn(3, x))
    return y


def part_a(ax, x):
    psi = even_psi_fn(2, x)
    ax.plot(x, psi, label="psi_2(x)")

    x_psi = x * psi
    ax.plot(x, x_psi, label="x psi_2(x)")

    xticks = np.arange(-0.5, 0.6, 0.1)
    ax.set_xticks(xticks)
    ax.legend()


def part_b(ax, x):

    psi = even_psi_fn(2, x)
    x_psi = x * psi
    ax.plot(x, x_psi, label="x psi_2(x)")

    approx = approx_fn(x)
    ax.plot(x, approx, label="A_1 psi_1(x) + A_3 psi_3(x)")

    xticks = np.arange(-0.5, 0.6, 0.1)
    ax.set_xticks(xticks)
    ax.legend()


def main():
    x = np.arange(-1/2, 1/2, 0.001)
    fig, ax = plt.subplots(figsize=(10, 10))

    # part_a(ax, x)
    part_b(ax, x)

    plt.show()


if __name__ == "__main__":
    main()