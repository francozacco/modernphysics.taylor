import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import math

def psi_prime_prime_fn(x):
    return ((math.e**x) - (math.e**(-x)))/2

def psi_prime_fn(i, psi_prime, x_range, delta_x):
    return psi_prime[i] + (psi_prime_prime_fn(x_range[i]) * delta_x)

def psi_fn(i, psi, psi_prime, delta_x):
    return psi[i] + (psi_prime[i] * delta_x)

def compute_psi(n):
    delta_x = 1/n
    x_range = np.arange(0, 1 + delta_x, delta_x)

    psi_prime = [1 for i in range(len(x_range))]
    psi = [0 for i in range(len(x_range))]
    for i in range(len(x_range) - 1):
        psi[i + 1] = psi_fn(i, psi, psi_prime, delta_x)
        psi_prime[i + 1] = psi_prime_fn(i, psi_prime, x_range, delta_x)
    print(psi[-1])
    return psi, x_range

def main():
    psi, x_range = compute_psi(n=4)
    plt.plot(x_range, psi, label="Approximation n=4")
    psi, x_range = compute_psi(n=3)
    plt.plot(x_range, psi, label="Approximation n=3")
    psi, x_range = compute_psi(n=100)
    plt.plot(x_range, psi, label="Approximation n=100")

    exact_psi = [psi_prime_prime_fn(x) for x in x_range]
    plt.plot(x_range, exact_psi, label="Exact")
    plt.xlabel("x")
    plt.ylabel("psi(x)")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()