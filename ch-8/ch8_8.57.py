
import matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np
matplotlib.use('TkAgg')


def Theta_dot(u):
    return u

def u_dot(theta, Theta, u):
    # return -(u * (1 / math.tan(theta))) - (6 * Theta)
    return -(u * (1 / math.tan(theta))) - (4.812 * Theta)


def runge_kutta(theta1, Theta1, u1, mult):
    h = 0.0001 * mult

    steps = int(abs((math.pi / 2) // h))
    
    theta = [theta1]
    Theta = [Theta1]
    u = [u1]
    for step in range(steps):
        k1_t = Theta_dot(u[-1])
        k1_u = u_dot(theta[-1], Theta[-1], u[-1])

        k2_t = Theta_dot(u[-1] + (h * k1_u / 2))
        k2_u = u_dot(
            theta[-1] + (h / 2),
            Theta[-1] + (h * k1_t / 2),
            u[-1] + (h * k1_u / 2)
        )

        k3_t = Theta_dot(u[-1] + (h * k2_u / 2))
        k3_u = u_dot(
            theta[-1] + (h / 2),
            Theta[-1] + (h * k2_t / 2),
            u[-1] + (h * k2_u / 2)
        )

        k4_t = Theta_dot(u[-1] + (h * k3_t))
        k4_u = u_dot(
            theta[-1] + h,
            Theta[-1] + (h * k3_t),
            u[-1] + (h * k3_u)
        )

        u.append(u[-1] + ((h / 6) * (k1_u + (2 * k2_u) + (2 * k3_u) + k4_u)))
        Theta.append(Theta[-1] + ((h / 6) * (k1_t + (2 * k2_t) + (2 * k3_t) + k4_t)))
        theta.append(theta[-1] + h)

    return np.array(theta), np.array(Theta)


def main():
    fig, ax = plt.subplots(figsize=(10, 10))

    theta1 = math.pi / 2
    # Theta1 = 1
    # u1 = 0
    Theta1 = 0
    u1 = 1

    theta, Theta = runge_kutta(theta1, Theta1, u1, mult=-1)
    ax.plot(theta, Theta, color="#1f77b4")

    theta, Theta = runge_kutta(theta1, Theta1, u1, mult=1)
    ax.plot(theta, Theta, label="Theta(θ)", color="#1f77b4")
    
    ax.set_xlabel("θ")
    ax.set_ylabel("Theta(θ)")
    ax.legend()
    ax.grid()
    plt.show()


if __name__ == "__main__":
    main()
