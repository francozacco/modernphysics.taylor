import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import math

def psi_prime_fn(i, psi_prime):
    return psi_prime[i] - (math.sin(x_range[i]) * delta_x)

def psi_fn(i, psi, psi_prime):
    return psi[i] + (psi_prime[i] * delta_x)

n = 10000
delta_x = 1/n
x_range = np.arange(0, 1 + delta_x, delta_x)

def main():

    psi_prime = [1 for i in range(len(x_range))]
    psi = [0 for i in range(len(x_range))]
    for i in range(len(x_range) - 1):
        psi[i + 1] = psi_fn(i, psi, psi_prime)
        psi_prime[i + 1] = psi_prime_fn(i, psi_prime)
    print(psi[-1])

    plt.plot(x_range, psi, label="Approximation")
    plt.plot(x_range, np.sin(x_range), label="Exact")
    plt.xlabel("x")
    plt.ylabel("psi(x)")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()