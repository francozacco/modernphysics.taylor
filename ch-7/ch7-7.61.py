import matplotlib.pyplot as plt
import numpy as np
import math


def psi0(x):
    A0 = 1 / (math.pi**(1/4))
    power = -(x**2)/2
    return A0 * np.exp(power)


def psi1(x):
    A1 = 4 / (math.pi**(1/4))
    power = -(x**2)/2
    return A1 * x * np.exp(power)


def main():
    fig, ax = plt.subplots()

    x = np.linspace(-5, 5, 100)
    psi0_arr = psi0(x)
    psi1_arr = psi1(x)

    ax.plot(x, psi0_arr, label="psi0")
    ax.plot(x, psi1_arr, label="psi1")

    plt.xlabel("x")
    plt.legend()
    plt.title("Wave functions")
    plt.show()


main()