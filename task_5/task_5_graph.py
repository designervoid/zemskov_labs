from scipy.interpolate import lagrange
import numpy as np
from numpy.polynomial.polynomial import Polynomial
import matplotlib as mpl
import matplotlib.pyplot as plt


x = np.array([0.180, 0.186, 0.192, 0.198, 0.204, 0.210], dtype=float)
y = np.array([5.61543, 5.46693,  5.32634, 5.19304, 5.06649, 4.94619], dtype=float)
poly = lagrange(x, y)
print(poly)

result = Polynomial(poly).coef
print(result)


x = np.linspace(-10, 10)

graph = -4.287e+04*x + 4.372e+04*x - 1.822e+04*x + 3957*x - 474.4*x + 31.23
plt.plot(x, graph)
plt.grid(True)
plt.show()