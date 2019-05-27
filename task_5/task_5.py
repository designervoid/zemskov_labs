import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.180, 0.186, 0.192, 0.198, 0.204, 0.210], dtype=float)
y = np.array([5.61543, 5.46693,  5.32634, 5.19304, 5.06649, 4.94619], dtype=float)


def lagranz(x, y, t):
    z = 0
    for j in range(len(y)):
        p1 = 1
        p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1
                p2 = p2 * 1
            else:
                p1 = p1 * (t - x[i])
                p2 = p2 * (x[j] - x[i])
        z = z + y[j] * p1 / p2
    return z


def show_graph(xnew, ynew):
    plt.plot(x, y, 'o', xnew, ynew)
    plt.grid(True)
    plt.legend(("F(x)", "Interpol F(x)"))
    plt.show()


xnew = np.linspace(np.min(x), np.max(x), 100)
ynew = [lagranz(x, y, i) for i in xnew]
show_graph(xnew, ynew)


def product(val, n):
    """ Вспомогательный генератор для вычисления произведения разностей координат """
    mul = 1
    for i in range(n):
        if i:
            mul *= val - x[i - 1]
        yield mul


C = []  # список коэффициентов полинома

# вычисляем коэффициенты
for n in range(len(x)):
    p = product(x[n], n + 1)
    C.append((y[n] - sum(C[k] * next(p) for k in range(n))) / next(p))


def f(v):
    """ Значение полинома в точке v """
    return sum(C[k] * p for k, p in enumerate(product(v, len(C))))


print(C)
