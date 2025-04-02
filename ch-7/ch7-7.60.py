import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import math


A = _lambda = T = 1
x_values = np.linspace(0, 2, 100)
ts = [0, 0.05, 0.1, 0.15, 0.2]

cmap = cm.get_cmap("coolwarm", 3 * len(ts))
for i, t in enumerate(ts):
    y_values_2 = A * np.sin(2 * math.pi *  x_values / _lambda) * np.cos(2 * math.pi * t / T)
    plt.plot(x_values, y_values_2, color=cmap(i), label=f"t={t}")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Wave function")


plt.show()