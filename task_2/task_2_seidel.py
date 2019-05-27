import numpy as np

A = np.array([[5., -1., 0., 0.],
              [-1., 7., -2., 0.],
              [0., 2., 11., -4.],
              [0., 0, -1, 5]])
b = [9., 5., 15., 10.]
x = [1, 1, 1, 1]

n = 20


def seidel(A, b, x, n):

    L = np.tril(A)
    U = A - L
    for i in range(n):
        print(L)
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        print(str(i).zfill(2)),
        print(x)
    return x


def check_solution(A, b):
    x = np.linalg.solve(A, b)
    print(f'Найдено верное решение с помощью numpy.linalg.solve => : {x}')
    print('Проверяем верное ли решение?', np.allclose(np.dot(A, x), b))


if __name__ == '__main__':
    seidel(A, b, x, n)
    check_solution(A, b)
