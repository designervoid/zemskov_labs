import scipy.optimize as opt
import numpy as np
import timeit
import math

st1 = timeit.default_timer()


def f(variables):
    x = variables

    first_eq = x*x + 4*math.sin(x)
    return first_eq


solution = opt.fsolve(f, (0.1))
print(solution)


from sympy import Symbol, solve, sin
x = Symbol('x')
a = solve(4*sin(x), x)
b = solve(x*x, x)
print(a, b)


st2 = timeit.default_timer()
print("RUN TIME : {0}".format(st2-st1))