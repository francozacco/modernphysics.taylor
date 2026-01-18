import numpy as np
import matplotlib.pyplot as plt


def main():
    n_x, n_y = 4, 3

    x = np.linspace(0, 1, num=100)
    y = np.linspace(0, 1, num=100)
    X, Y = np.meshgrid(x, y)
    psi = (np.sin(n_x * np.pi * X)**2)*(np.sin(n_y * np.pi * Y)**2)

    fig, ax = plt.subplots()
    ax.contour(X, Y, psi, levels=10)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("|psi|^2 contour lines")
    plt.show()



if __name__ == "__main__":
    main()