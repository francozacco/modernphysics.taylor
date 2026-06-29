import matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np
from constants import e, k, aB as q, k, aB
matplotlib.use('TkAgg')


def eq_10_40(r, Z, R):
    factor = -((q**2) * k)
    second_term = ((Z - 1) / (2 * (R**2))) * (math.e**(-r/R)) * (R + 1/r)
    return factor * ( 1/r + second_term )


def eq_10_4(r, Z, R):
    factor = -((q**2) * k)
    return factor / r


def eq_10_5(r, Z, R):
    factor = -((q**2) * k)
    return factor * Z / r


def main():
    R = 1
    Z = 4 
    r = np.arange(0.001, 0.5, 0.001)

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.plot(r, eq_10_40(r, Z, R), label="U(r) 10.40")
    ax.plot(r, eq_10_4(r, Z, R), label="U(r) 10.4")
    ax.plot(r, eq_10_5(r, Z, R), label="U(r) 10.5")
    ax.legend()

    plt.show()


if __name__ == "__main__":
    main()