import numpy as np

A = np.array([[3.21, -2.25, 2.13], [7.09, 9.17, -1.23], [0.43, -1.40, -4.62]], dtype='float')
b = np.array([5.06, 4.75, -1.05])

Ab = np.hstack([A, b.reshape(-1, 1)])

n = len(b)

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

x = Ab[:, 3]
print(x)