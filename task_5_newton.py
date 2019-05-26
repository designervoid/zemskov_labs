import numpy as np
import matplotlib.pyplot as plt


def _poly_newton_coefficient(x,y):
    """
    x: list or np array contanining x data points
    y: list or np array contanining y data points
    """

    m = len(x)

    x = np.copy(x)
    a = np.copy(y)
    for k in range(1,m):
        a[k:m] = (a[k:m] - a[k-1])/(x[k:m] - x[k-1])

    return a

def newton_polynomial(x_data, y_data, x):
    """
    x_data: data points at x
    y_data: data points at y
    x: evaluation point(s)
    """
    a = _poly_newton_coefficient(x_data, y_data)
    n = len(x_data) - 1 # Degree of polynomial
    p = a[n]
    for k in range(1,n+1):
        p = a[n-k] + (x -x_data[n-k])*p
    return p




x = np.array([0.180, 0.186, 0.192, 0.198, 0.204, 0.210], dtype=float)
y = np.array([5.61543, 5.46693,  5.32634, 5.19304, 5.06649, 4.94619], dtype=float)
a = _poly_newton_coefficient(x, y)
b = newton_polynomial(x, y, 0.1875)
print(a)
print(b)
