'''
import numpy as np
import math

def simps(f,a,b,N=50):

    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S

solution = simps(lambda x: (np.sin(x))/x+1, 0, 1, 10)
print(solution)
'''


def simpsons_rule(f, a, b):
    c = (a + b) / 2.000
    h3 = abs(b - a) / 6.0
    return h3 * (f(a) + 4.0 * f(c) + f(b))


def recursive_asr(f, a, b, eps, whole):
    "Recursive implementation of adaptive Simpson's rule."
    c = (a + b) / 2.0
    left = simpsons_rule(f, a, c)
    right = simpsons_rule(f, c, b)
    if abs(left + right - whole) <= 15 * eps:
        return left + right + (left + right - whole) / 15.0
    return recursive_asr(f, a, c, eps / 2.0, left) + recursive_asr(f, c, b, eps / 2.0, right)


def adaptive_simpsons_rule(f, a, b, eps):
    "Calculate integral of f from a to b with max error of eps."
    return recursive_asr(f, a, b, eps, simpsons_rule(f, a, b))


import math


def f(x):
    result = (math.sin(x))/x+1
    return result


print(adaptive_simpsons_rule(f, 0.0001, 1, 0.0001))


# check integral with scipy
from scipy.integrate import quad
def integrand(x):
    return (math.sin(x))/x+1

I = quad(integrand, 0, 1)
print(I)


# check integral with numpy
import numpy as np
def integrate(f, a, b, N):
    x = np.linspace(a+(b-a)/(2*N), b-(b-a)/(2*N), N)
    fx = f(x)
    area = np.sum(fx)*(b-a)/N
    return area

print(integrate(lambda x: np.sin(x)/x+1, 0, 1, 100))
