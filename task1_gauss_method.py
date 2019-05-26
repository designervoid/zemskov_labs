import numpy as np

A = np.array([[1.12, -0.43, 0.14], [-0.07, 1.34, 0.72], [1.18, -0.08, -2.25]], dtype='float')
b = np.array([-0.17, 0.62, 1.12])

x_true = np.linalg.solve(A, b)
print(f'Найдено верное решение с помощью numpy.linalg.solve => : {x_true}')
print('Проверяем верное ли решение?', np.allclose(np.dot(A, x_true), b))

Ab = np.hstack([A, b.reshape(-1, 1)])

n = len(b)
values_new = np.zeros(3)
iter = 0
epsilon = 0.01

for i in range(n):
    a = Ab[i]

    for j in range(i + 1, n):
        b = Ab[j]
        m = a[i] / b[i]
        Ab[j] = a - m * b

for i in range(n - 1, -1, -1):
    Ab[i] = Ab[i] / Ab[i, i]
    a = Ab[i]

    for j in range(i - 1, -1, -1):
        b = Ab[j]
        m = a[i] / b[i]
        Ab[j] = a - m * b
        if abs(x_true[0] - Ab[0][3]) > epsilon or \
                abs(x_true[1] - Ab[1][3]) > epsilon or \
                abs(x_true[2] - Ab[2][3]) > epsilon:
            iter += 1
            print(f'iteration {iter}')
            print(Ab)

x = Ab[:, 3]
print(x)

print(f'Найдено решение с помощью алгоритма => : {x}')




