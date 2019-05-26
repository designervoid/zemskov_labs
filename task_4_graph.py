import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10)
graph = x * x + 4 * np.sin(x)
plt.plot(x, graph)
plt.grid(True)
plt.show()