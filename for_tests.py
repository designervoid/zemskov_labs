import numpy

A = numpy.array([[8., 2., 0., 0.],
              [1., 6., -3., 0.],
              [0., 2., -10., -4.],
              [0., 0., -3., -6.]])

b = numpy.array([[10.5,
               5.5,
               15.0,
               7.5]])

matrix = numpy.hstack([A, b.reshape(-1, 1)])

values = numpy.zeros(4)

ITER = 0

def SimpleIter(values, ITER):

    values_new = numpy.zeros(4)

    for i in range(4):
        values_new[i] += matrix[i][4]
        for p in range(4):
            if i != p:
                values_new[i] += - matrix[i][p] * values[p]
        values_new[i] /= matrix[i][i]

    max_d = abs(values[0] - values_new[0])

    for i in range(4):
        if abs(values[i] - values_new[i]) > max_d:
            max_d = abs(values[i] - values_new[i])
    ITER +=1
    if max_d > 0.001:
        print(values_new)
        print(ITER)
        SimpleIter(values_new, ITER)
        #else:
    return


SimpleIter(values, ITER)