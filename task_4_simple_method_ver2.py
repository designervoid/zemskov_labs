import math


def f(x):
    return x*x + 4*math.sin(x)


def MPD(f, a, b, eps=0.01):
    while abs(b - a) > eps:
        x = (a + b) / 2.0
        fx = f(x)
        fa = f(a)
        if (fx < 0 and fa < 0) or (fx > 0 and fa > 0):
            a = x
        else:
            b = x
    return x


x = MPD(f, 0, 1)
print(f'x: {x}')
print(f'f(x): {f(x)}')