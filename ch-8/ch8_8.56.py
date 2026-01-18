
import matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np
matplotlib.use('TkAgg')

a_B = 5.2917e-11


def Prob(rho, K=1):
    return  (4 * (K**3) / a_B) * (rho**2) * math.e**(-2 * K * rho)


def main():
    fig, ax = plt.subplots(figsize=(10, 10))
    ticks = 5
    r = np.arange(0, ticks, 0.01)
    P_1s_H = Prob(r)
    P_1s_He = Prob(r, K=2)
    ax.plot(r, P_1s_H, label="H", color="#b83d25")
    ax.plot(r, P_1s_He, label="He^+", color="#00A3FF")

    ax.set_xlabel("r/a_B")
    ax.set_ylabel("P(r)")
    ax.set_xticks([i for i in range(ticks + 1)] + [0.5])
    ax.legend()
    ax.grid()
    plt.show()


if __name__ == "__main__":
    main()
