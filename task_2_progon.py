import numpy as np

# [ 1.2907416   0.08824191 -1.22838018 -0.63658135]

A = np.array([[8., 2., 0., 0.],
              [1., 6., -3., 0.],
              [0., 2., -10., -4.],
              [0., 0., -3., -6.]])

b = np.array([10.5,
               5.5,
               15.0,
               7.5])

Ab = np.hstack([A, b.reshape(-1, 1)])

n = len(Ab)

gamma = []
alpha = []
beta = []

for i in range(n):
    if i == 0:
        print(f'iter {i + 1}')
        # calculate
        gamma_to_list = Ab[i][i]  # gamma1 = b1
        alpha_to_list = -(Ab[i][i+1]) / gamma_to_list  # alpha1 = -c1/gamma1
        beta_to_list = Ab[i][-1] / gamma_to_list  # beta1 = d1/y1
        # add to list
        gamma.append(gamma_to_list)
        alpha.append(alpha_to_list)
        beta.append(beta_to_list)
        print(gamma[0], alpha[0], beta[0])
    elif i == 1:
        print(f'iter {i + 1}')
        gamma_to_list = Ab[1][1] + Ab[1][0] * gamma[0]
        alpha_to_list = -(Ab[0][0]) / gamma_to_list
        beta_to_list = (Ab[1][-1] - Ab[1][0] * beta[0]) / gamma_to_list
        gamma.append(gamma_to_list)
        alpha.append(alpha_to_list)
        beta.append(beta_to_list)
        print(gamma[1], alpha[1], beta[1])
    elif i == 2:
        print(f'iter {i + 1}')
        gamma_to_list = Ab[2][2] + Ab[2][1] * gamma[1]
        alpha_to_list = -(Ab[1][1]) / gamma_to_list
        beta_to_list = (Ab[2][-1] - Ab[2][1] * beta[1]) / gamma_to_list
        gamma.append(gamma_to_list)
        alpha.append(alpha_to_list)
        beta.append(beta_to_list)
        print(gamma[2], alpha[2], beta[2])
    elif i == 3:
        print(f'iter {i + 1}')
        gamma_to_list = Ab[3][3] + Ab[3][2] * gamma[2]
        beta_to_list = (Ab[3][-1] - Ab[3][2] * beta[2]) / gamma_to_list
        gamma.append(gamma_to_list)
        beta.append(beta_to_list)
        print(gamma[3], beta[3])

print(alpha, gamma, beta)
print(f'x4 = beta4 = {beta[3]}')
print(f'x3 = alpha3 * x4 + beta3 = {alpha[2] * beta[3] + beta[2] }')
print(f'x2 = alpha2 * x3 + beta2 = {alpha[1] * beta[2] + beta[1] }')
print(f'x3 = alpha1 * x2 + beta1 = {alpha[0] * beta[1] + beta[0] }')

# check solution
x = np.linalg.solve(A, b)
print(f'right solution: {x}')
print('solution right?', np.allclose(np.dot(A, x), b))

