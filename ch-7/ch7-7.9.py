import matplotlib.pyplot as plt
import numpy as np
import math


A = 2.5
k = 1
omega = 10 * math.pi
x_values = np.linspace(0, 2 * math.pi / k, 100)
t1, t2 = 0.05, 0.1

# y_values_1 = A * np.sin(k * x_values) * np.cos(omega * t1)
# vel_1 = -omega * A * np.sin(k * x_values) * np.sin(omega * t1)
# plt.plot(x_values, y_values_1, label="wave function")
# plt.plot(x_values, vel_1, label="velocity")

y_values_2 = A * np.sin(k * x_values) * np.cos(omega * t2)
vel_2 = -omega * A * np.sin(k * x_values) * np.sin(omega * t2)
plt.plot(x_values, y_values_2, label="wave function")
plt.plot(x_values, vel_2, label="velocity")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
# plt.title("Wave function")


plt.show()