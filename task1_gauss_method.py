import numpy as np

A = np.array([[3.21, -2.25, 2.13], [7.09, 9.17, -1.23], [0.43, -1.40, -4.62]], dtype='float')
b = np.array([5.06, 4.75, -1.05])

Ab = np.hstack([A, b.reshape(-1, 1)])

n = len(b)
values_new = np.zeros(3)
iter = 0

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

    max_d = abs(a[0] - values_new[0])
    for i in range(3):
        if abs(a[i] - values_new[i]) > max_d:
            max_d = abs(a[i] - values_new[i])
    iter +=1
    if max_d > 0.01:
        print(Ab)
        print(iter)

x = Ab[:, 3]
print(x)


#check solution
x_new = np.linalg.solve(A, b)
print(f'right solution: {x_new}')
print('solution right?', np.allclose(np.dot(A, x), b))