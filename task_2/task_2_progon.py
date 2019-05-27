import numpy as np
from numba import jit, f8

A = np.array([[5., -1., 0., 0.],
              [-1., 7., -2., 0.],
              [0., 2., 11., -4.],
              [0., 0, -1, 5]], dtype=float)

a = np.array([-1., 2., -1.])  # up diagonal of matrix
b = np.array([5., 7., 11., 5.])  # main diagonal of matrix
c = np.array([-1., -2., -4]) # down diagonal of matrix
d = np.array([9., 5., 15., 10.]) # right side of matrix


# Tri Diagonal Matrix Algorithm(a.k.a Thomas algorithm) solver
@jit(f8[:](f8[:], f8[:], f8[:], f8[:]))
def TDMAsolver(a, b, c, d):
    nf = len(d)  # number of equations
    ac, bc, cc, dc = map(np.array, (a, b, c, d))  # copy arrays
    for it in range(1, nf):
        mc = ac[it - 1] / bc[it - 1]
        bc[it] = bc[it] - mc * cc[it - 1]
        dc[it] = dc[it] - mc * dc[it - 1]

    xc = bc
    xc[-1] = dc[-1] / bc[-1]

    for il in range(nf - 2, -1, -1):
        xc[il] = (dc[il] - cc[il] * xc[il + 1]) / bc[il]

    return xc


def check_solution(A, d):
    x = np.linalg.solve(A, d)
    print(f'Найдено верное решение с помощью numpy.linalg.solve => : {x}')
    print('Проверяем верное ли решение?', np.allclose(np.dot(A, x), d))


print(TDMAsolver(a, b, c, d))
check_solution(A, d)