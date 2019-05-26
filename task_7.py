import numpy as np
import matplotlib.pyplot as plt


x = np.array([0.180, 0.186, 0.192, 0.198, 0.204, 0.210], dtype=float)
y = np.array([5.61543, 5.46693,  5.32634, 5.19304, 5.06649, 4.94619], dtype=float)
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]

plt.plot(x, y, 'o', label='Original data', markersize=10)
plt.plot(x, m*x + c, 'r', label='Fitted line')
plt.legend()
plt.grid(True)
plt.show()


import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.family'] = 'fantasy'


def mnkGP(x, y):  # функция которую можно использзовать в програме
    n = len(x)  # количество элементов в списках
    s = sum(y)  # сумма значений y
    s1 = sum([1 / x[i] for i in range(0, n)])  # сумма 1/x
    s2 = sum([(1 / x[i]) ** 2 for i in range(0, n)])  # сумма (1/x)**2
    s3 = sum([y[i] / x[i] for i in range(0, n)])  # сумма y/x
    a = round((s * s2 - s1 * s3) / (n * s2 - s1 ** 2), 3)  # коэфициент а с тремя дробными цифрами
    b = round((n * s3 - s1 * s) / (n * s2 - s1 ** 2), 3)  # коэфициент b с тремя дробными цифрами
    s4 = [a + b / x[i] for i in range(0, n)]  # список значений гиперболической функции
    so = round(sum([abs(y[i] - s4[i]) for i in range(0, n)]) / (n * sum(y)) * 100, 3)  # средняя ошибка аппроксимации
    plt.title('Аппроксимация гиперболой Y=' + str(a) + '+' + str(b) + '/x\n Средняя ошибка--' + str(so) + '%', size=14)
    plt.xlabel('Координата X', size=14)
    plt.ylabel('Координата Y', size=14)
    plt.plot(x, y, color='r', linestyle=' ', marker='o', label='Data(x,y)')
    plt.plot(x, s4, color='g', linewidth=2, label='Data(x,f(x)=a+b/x')
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()


mnkGP(x, y)
