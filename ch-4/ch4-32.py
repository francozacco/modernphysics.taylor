import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math
import numpy as np

def main():
    plt.figure()
    ax = plt.axes()
    lamb = np.arange(1e-8, 10e-6, 1e-8)
    for T in [1000, 1500]:
        factor_1 = ((2 * math.pi * 6.63e-34 * (2.998e8)**2)/(lamb**5))
        factor_2 = (1/((math.e**((6.63e-34 * 2.998e8)/(lamb * 1.38e-23 * T))) - 1))
        I = factor_1 * factor_2
        I_max_idx = np.argmax(I)
        print(f"Max for T: {T} is at {lamb[I_max_idx]}")
        plot(ax, lamb, I, f"T: {T}")
    plt.show()
    # plt.savefig("ch4-32.png")

def plot(ax, x, y, label):
    ax.plot(x, y, label=label)
    ax.legend()
    ax.set_xlabel("lambda")
    ax.set_ylabel("I")


if __name__ == "__main__":
    main()
