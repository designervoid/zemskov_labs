import numpy as np

epsilon = 0.01


def func(x):
    return x*x + 4*np.sin(x)


def bisection(a, b):
    if func(a) * func(b) >= 0:
        print('you have not assumed right a and b\n')
        return

    c = a

    while (b-a) >= epsilon:
        c = (a+b)/2
        if func(c) == 0.0:
            break
        elif func(c)*func(a) < 0:
            b = c
        else:
            a = c
    print(f'the value of root is {c}')


if __name__ == '__main__':
    a, b = -10, 10
    bisection(a, b)


def f(x):
    return x*x + 4*np.sin(x)


def bisection_method(a, b, tol):
    if f(a) * f(b) > 0:
        # end function, no root.
        print("No root found.")
    else:
        while (b - a) / 2.0 > tol:
            midpoint = (a + b) / 2.0
            if f(midpoint) == 0:
                return (midpoint)  # The midpoint is the x-intercept/root.
            elif f(a) * f(midpoint) < 0:  # Increasing but below 0 case
                b = midpoint
            else:
                a = midpoint

        return (midpoint)


answer = bisection_method(-1, 5, 0.01)

print("Answer:", answer)


def solve(func, x = 0.0, step=0.01, prec = 0.01):
    """Find a root of func(x) using the bisection method.

    The function may be rising or falling, or a boolean expression, as long as
    the end points have differing signs or boolean values.

    Examples:
        solve(lambda x: x**3 > 1000) to calculate the cubic root of 1000.
        solve(math.sin, x=6, step=1) to solve sin(x)=0 with x=[6,7).
    """
    test = lambda x: func(x) > 0  # Convert into bool function
    begin, end = test(x), test(x + step)
    assert begin is not end  # func(x) and func(x+step) must be on opposite sides
    while abs(step) > prec:
        step *= 0.5
        if test(x + step) is not end:
            x += step
    return x

f = lambda x: x*x + 4*np.sin(x)
print(solve(f))


def root11(x):
    return x * x + 4 * np.sin(x)


def bisection_method(f, a, b, tol):
    if f(a) * f(b) > 0:
        # end function, no root.
        print("No root found.")
    else:
        iter = 0
        while (b - a) / 2.0 > tol:
            midpoint = (a + b) / 2.0

            if f(a) * f(midpoint) < 0:  # Increasing but below 0 case
                b = midpoint
            else:
                a = midpoint

            iter += 1
        return (midpoint, iter)


answer, iterations = bisection_method(root11, -1, 1, 0.01)
print("Answer:", answer, "\nfound in", iterations, "iterations")


