import numpy as np

alpha = .8
n = 10
M = np.array([[50+3*n, 10-n, 3],
               [10-n, 20+2*n, 10-n],
               [3, 10-n, 90-n]])
n = len(M)
rj = [1.0/n for _ in range(n)]
p = [1.0/n for _ in range(n)]

for _ in range(100):
    p_old = [x for x in p]
    for i in range(n):
        pi = 0.0
        for j in range(n):
            pi += alpha * M[i][j] * p_old[j]
        pi += (1-alpha) * rj[i]
        p[i] = pi
print(p)