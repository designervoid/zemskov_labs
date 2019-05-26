import numpy as np
from numba import jit, f8


## Tri Diagonal Matrix Algorithm(a.k.a Thomas algorithm) solver
@jit(f8[:](f8[:], f8[:], f8[:], f8[:]))
def TDMAsolver(a, b, c, d):
    '''
    TDMA solver, a b c d can be NumPy array type or Python list type.
    refer to http://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm
    and to http://www.cfd-online.com/Wiki/Tridiagonal_matrix_algorithm_-_TDMA_(Thomas_algorithm)
    '''
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


a = np.array([-1., 2., -1.])
b = np.array([5., 7., 11., 5.])
c = np.array([-1., -2., -4])
d = np.array([9., 5., 15., 10.])
print(TDMAsolver(a, b, c, d))
A = np.array([[5., -1., 0., 0.],
              [-1., 7., -2., 0.],
              [0., 2., 11., -4.],
              [0., 0, -1, 5]], dtype=float)
x = np.linalg.solve(A, d)
print(f'Найдено верное решение с помощью numpy.linalg.solve => : {x}')
print('Проверяем верное ли решение?', np.allclose(np.dot(A, x), d))