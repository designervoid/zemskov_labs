import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from task_3 import task_3_jacobi

n = 10
matrix = np.array([[50+3*n, 10-n, 3],
               [10-n, 20+2*n, 10-n],
               [3, 10-n, 90-n]])

solution = task_3_jacobi.jacobi(matrix)

A = np.array([[50+3*n, 10-n, 3],
               [10-n, 20+2*n, 10-n],
               [3, 10-n, 90-n]], dtype='float')
b = np.array([solution[0][2],
              solution[0][1],
              solution[0][0]])


def task_1_graph_gauss(A, b):
    point1 = np.array([(-(b[0]) / A[0][0]), (0), (0)])
    normal1 = np.array([A[0][0], A[0][1], A[0][2]])

    point2 = np.array([0, -(b[1]) / A[1][1], 0])
    normal2 = np.array([A[1][0], A[1][1], A[1][2]])

    point3 = np.array([0, 0, -(b[2]) / A[2][2]])
    normal3 = np.array([A[2][0], A[2][1], A[2][2]])

    # a plane is a*x+b*y+c*z+d=0
    # [a,b,c] is the normal. Thus, we have to calculate
    # d and we're set
    d1 = -np.sum(point1 * normal1)  # dot product
    d2 = -np.sum(point2 * normal2)  # dot product
    d3 = -np.sum(point3 * normal3)  # dot product

    # create x,y
    xx, yy = np.meshgrid(range(5), range(5))

    # calculate corresponding z
    z1 = (-normal1[0] * xx - normal1[1] * yy - d1) * 1. / normal1[2]
    z2 = (-normal2[0] * xx - normal2[1] * yy - d2) * 1. / normal2[2]
    z3 = (-normal3[0] * xx - normal3[1] * yy - d3) * 1. / normal3[2]

    # plot the surface
    plt3d = plt.figure().gca(projection='3d')
    plt3d.plot_surface(xx, yy, z1, color='blue')
    plt3d.plot_surface(xx, yy, z2, color='yellow')
    plt3d.plot_surface(xx, yy, z3, color='cyan')
    plt.show()
    plt.savefig('task_1_graph_gauss', bbox_inches='tight')


task_1_graph_gauss(A, b)