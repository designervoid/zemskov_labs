import numpy

matrix = numpy.array([[3.21, -2.25, 2.13, 5.06],
                      [7.09, 9.17, -1.23, 4.75],
                      [0.43, -1.40, -4.62, -1.05]])

values = numpy.zeros(3)

ITER = 0

def SimpleIter(values, ITER):

    values_new = numpy.zeros(3)

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
        #else:
    return


SimpleIter(values, ITER)