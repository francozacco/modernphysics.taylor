import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm
import numpy as np
import math

A = _lambda = T = 1


def wave_fn(x, t):
    return A * np.sin(2 * math.pi *  x / _lambda) * np.cos(2 * math.pi * t / T)


def update(frame, x, t0, line):
    line.set_ydata(wave_fn(x, t0 + frame * 0.05))  # Shift the sine wave
    return line,


def main():
    x = np.linspace(0, 2, 100)
    y0 = wave_fn(x, 0)

    fig, ax = plt.subplots()
    line, = ax.plot(x, y0)

    ani = animation.FuncAnimation(
        fig, update, fargs=(x, 0, line), frames=100, interval=100, blit=True
    )

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Wave function")
    plt.show()


main()