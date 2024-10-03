import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math
import numpy as np

def main():
    plt.figure()
    ax = plt.axes()
    k_B = 8.62e-5
    T_list = [400]
    h = 6.63e-34/1.6e-19
    c = 3e8
    x = np.arange(0.01, 1, 0.01)
    for T in T_list:
        factor = (2*math.pi * (k_B)**5 * T**5)/((h**4) * (c**3))
        I = factor * 1/(x**5) * (1/(math.e**(1/x) - 1))
        dIdT = factor *(math.e**(1/x) * (1 - 5*x) + 5*x)/((math.e**(1/x) - 1)**2 * x**7)  
        plot(ax, x, I, f"T: {T}")
        plot(ax, x, dIdT, "")
        ax.axvline(x=0.2, color="black")
    # plt.show()
    plt.savefig("ch4-33.png")

def plot(ax, x, y, label):
    ax.plot(x, y, label=label)
    ax.grid(visible=True)
    ax.legend()
    ax.set_xlabel("x")
    ax.set_ylabel("I")


if __name__ == "__main__":
    main()
