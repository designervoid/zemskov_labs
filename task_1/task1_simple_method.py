import numpy as np

matrix = np.array([[1.12, -0.43, 0.14, -0.17],
                   [-0.07, 1.34, 0.72, 0.62],
                   [1.18, -0.08, -2.25, 1.12]])

A = np.array([[1.12, -0.43, 0.14],
                   [-0.07, 1.34, 0.72],
                   [1.18, -0.08, -2.25]])


b = np.array([-0.17,
              0.62,
              1.12])

values = np.zeros(3)

ITER = 0


def task_1_simple_method(matrix, values, ITER):
    def SimpleIter(values, ITER):
        values_new = np.zeros(3)

        for i in range(3):
            values_new[i] += matrix[i][3]
            for p in range(3):
                if i != p:
                    values_new[i] += - matrix[i][p] * values[p]
            values_new[i] /= matrix[i][i]

        max_d = abs(values[0] - values_new[0])

        for i in range(3):
            if abs(values[i] - values_new[i]) > max_d:
                max_d = abs(values[i] - values_new[i])
        ITER +=1
        if max_d > 0.001:
            print(values_new)
            print(ITER)
            SimpleIter(values_new, ITER)
        return

    SimpleIter(values, ITER)


def test_solution(A, b):
    x = np.linalg.solve(A, b)
    print(f'Найдено верное решение с помощью numpy.linalg.solve => : {x}')
    print('Проверяем верное ли решение?', np.allclose(np.dot(A, x), b))


if __name__ == '__main__':
    task_1_simple_method(matrix, values, ITER)
    test_solution(A, b)