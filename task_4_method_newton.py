import numpy as np
from scipy import optimize


def newton(f, Df, x0, epsilon, max_iter):
    '''Приближенное решение функции f(x)=0 с помощью метода Ньютона.

    Параметры
    ----------
    f : функция
        функция для которой мы ищем решение в виде f(x)=0
    Df : функция'
        Производная от f(x)
    x0 : число
        Стартовая точка для решения функции f(x)=0
    epsilon : целое число
        Критерий остановки для условия abs(f(x)) < epsilon
    max_iter : целое число
        Максимальная число операций для метода Ньютона

    Что возвращает
    -------
    xn : число
        Реализация метода Ньютона:
        Вычисление линейного приближения
        из f(x) в точке xn и нахождение точки пересечения x по формуле
            x = xn - f(xn)/Df(xn)
        Продолжаем работу алгоритма пока abs(f(xn)) < epsilon и возвращаем xn
        Если Df(xn) == 0, возвращаем None.
        If Df(xn) == 0, возвращаем None. Если количество итераций
         превышает max_iter, возвращаем None.
    '''
    xn = x0
    for n in range(0, max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Решение найдено после', n, 'итераций')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Производная равна 0. Нет решений.')
            return None
        xn = xn - fxn/Dfxn
    print('Превышено кол-во итераций. Нет решений.')
    return None


def newton_with_epsilon(f, f_, x0, e=0.01):
    """
    Newton method for root finding
    """
    n = 0
    while True:
        n += 1
        x = x0 - (f(x0) / f_(x0))
        if abs(x - x0) < e:
            break
        x0 = x
    print("N\ti=%d\tx=%f\tf(x)=%f" % (n, x, f(x)))
    return x


def f(x):
    return x*x + 4*np.sin(x)


print('___________________________________________')
print('Реализация алгоритма => ')
f = lambda x: (x*x) + (4*np.sin(x))
Df = lambda x: (2*x) + (4*np.cos(x))
solution = newton(f, Df, 1, 0.01, 10)
print(solution)

print('___________________________________________')
print('Реализация алгоритма с epsilon =>')
print(newton_with_epsilon(f, Df, 0.01))

print('___________________________________________')
print('Решение с помощью scipy.optimize.newton =>')
solution_scipy = optimize.newton(f, 0.01)
print(solution_scipy)





