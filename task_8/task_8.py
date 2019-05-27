from scipy.interpolate import lagrange
import numpy as np
from numpy.polynomial.polynomial import Polynomial
import matplotlib as mpl
import matplotlib.pyplot as plt
from sympy import diff, symbols, sin


x = np.array([0.180, 0.186, 0.192, 0.198, 0.204, 0.210], dtype=float)
y = np.array([5.61543, 5.46693,  5.32634, 5.19304, 5.06649, 4.94619], dtype=float)
poly = lagrange(x, y)
print(f'Полином построенный по таблице: {poly}')
result = Polynomial(poly).coef
print(f'Коэффициенты: {result}')
graph = -4.287e+04*x**5 + 4.372e+04*x**4 - 1.822e+04*x**3 + 3957*x**2 - 474.4*x**1 + 31.23


x, y = symbols('x y')

func = -4.287e+04*x**5 + 4.372e+04*x**4 - 1.822e+04*x**3 + 3957*x**2 - 474.4*x**1 + 31.23
first_der_func = diff(func)
print(f'Первая производная полинома: {first_der_func}')


def calc_first_func(x):
    return -214350.0 * x ** 4 + 174880.0 * x ** 3 - 54660.0 * x ** 2 + 7914 * x - 474.4


x0 = 0.1875
print(f'Значение производной в точке х {x0}: {calc_first_func(x)}')

second_der_func = diff(first_der_func)
print(f'Вторая производная полинома: {second_der_func}')


def calc_second_func(x):
    return -857400.0*x**3 + 524640.0*x**2 - 109320.0*x + 7914


print(f'Значение производной в точке х {x0}: {calc_second_func(x)}')