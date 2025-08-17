import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import math

x_values = np.linspace(0, 1, 100)
y_values = 2 * (np.sin(3 * math.pi * x_values)**2)
print(np.argmax(y_values))
print(x_values[82])
# plt.plot(x_values, y_values, label=f"")

# plt.xlabel("x")
# plt.ylabel("|psi(x)|^2")
# plt.legend()
# plt.title("Probability distribution")


# plt.show()