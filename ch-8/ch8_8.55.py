
import matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np
matplotlib.use('TkAgg')

a_B = 5.2917e-11


def R_1s(rho):
    # rho = r/a_B
    return (math.e**(-rho)) / (2 * math.sqrt(a_B**3))


def R_2s(rho):
    # rho = r/a_B
    num = (1 - (rho / 2)) * (math.e**(-rho / 2))
    return num / (math.sqrt(2 * (a_B**3)))


def R_2p(rho):
    # rho = r/a_B
    num = rho * (math.e**(-rho / 2))
    return num / (math.sqrt(24 * (a_B**3)))


def R_3s(rho):
    # rho = r/a_B
    num = (1 - (2 * rho / 3) + (2 * (rho**2) / 27) ) * (math.e**(-rho / 3))
    return  (2 * num) / (math.sqrt(27 * (a_B**3)))


def R_3p(rho):
    # rho = r/a_B
    num = (1 - (rho / 6)) * rho * (math.e**(-rho / 3))
    return  (8 * num) / (27 * math.sqrt(6 * (a_B**3)))


def R_3d(rho):
    # rho = r/a_B
    num = (rho**2) * (math.e**(-rho / 3))
    return  (4 * num) / (81 * math.sqrt(30 * (a_B**3)))


def Prob(r, fn):
    return  4 * math.pi * (r**2) * (fn(r)**2)


def main():
    fig, ax = plt.subplots(figsize=(10, 10))
    ticks = 25
    r = np.arange(0, ticks, 0.1)
    P_1s = Prob(r, R_1s)
    P_2s = Prob(r, R_2s)
    P_2p = Prob(r, R_2p)
    P_3s = Prob(r, R_3s)
    P_3p = Prob(r, R_3p)
    P_3d = Prob(r, R_3d)
    ax.plot(r, P_1s, label="P_1s(r)", color="#b83d25")
    ax.plot(r, P_2s, label="P_2s(r)", color="#00A3FF")
    ax.plot(r, P_2p, label="P_2p(r)", color="#00CCFF")
    ax.plot(r, P_3s, label="P_3s(r)", color="#0B6623")
    ax.plot(r, P_3p, label="P_3p(r)", color="#1E5631")
    ax.plot(r, P_3d, label="P_3d(r)", color="#043927")

    ax.set_xlabel("r/a_B")
    ax.set_ylabel("P(r)")
    ax.set_xticks([i for i in range(ticks + 1)])
    ax.legend()
    ax.grid()
    plt.show()


if __name__ == "__main__":
    main()
