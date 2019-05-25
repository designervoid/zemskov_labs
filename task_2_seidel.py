# [ 1.2907416   0.08824191 -1.22838018 -0.63658135]

import numpy as np
from scipy.linalg import solve


def gauss(A, b, x, n):

    L = np.tril(A)
    U = A - L
    for i in range(n):
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        print(str(i).zfill(2)),
        print(x)
    return x


'''___MAIN___'''


A = np.array([[8, 2, 0, 0], [1, 6, -3, 0], [0, 2, -10, -4], [0, 0, -3, -6]])
b = [10.5, 5.5, 15.0, 7.5]
x = [1, 1, 1, 1]

n = 20

print(gauss(A, b, x, n))
print(solve(A, b))

# check solution
x = np.linalg.solve(A, b)
print(f'right solution: {x}')
print('solution right?', np.allclose(np.dot(A, x), b))