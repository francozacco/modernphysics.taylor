import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm
import numpy as np
import math

a = 1
omega_21 = 2


def wave_fn(x, t):
    psi_1 = math.sqrt(2/a) * np.sin(math.pi * x / a)
    psi_2 = math.sqrt(2/a) * np.sin(2 * math.pi * x / a)
    return 0.5 * ((psi_1**2) + (psi_2**2) + (2 * psi_1 * psi_2 * np.cos(omega_21 * t)))


def update(frame, x, t0, line):
    line.set_ydata(wave_fn(x, t0 + frame * 0.05))
    return line,


def main():
    x = np.linspace(0, a, 100)
    y0 = wave_fn(x, 0)

    fig, ax = plt.subplots()
    line, = ax.plot(x, y0)

    ani = animation.FuncAnimation(
        fig, update, fargs=(x, 0, line), frames=100, interval=100, blit=True
    )

    plt.xlabel("x")
    plt.ylabel("|psi(x,t)|^2")
    plt.title("Wave function")
    plt.show()


main()