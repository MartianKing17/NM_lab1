import math


def sgn(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0


def f(x):
    return (x**4) -3*(x**3) - (20*(x**2)) + 44*x + 54


def df(x):
    return 4 * x**3 - 9 * x**2 + 40 * x + 44


def dihotomia(a, b, func, ell):
    n = 0
    x_last = 0
    x_next = (a+b)/2
    asterio = (a+b)/ell
    asterio = math.log2(asterio)
    asterio = math.fabs(asterio) + 1
    asterio = int(asterio)

    while abs(x_next - x_last) > ell:

        x_last = x_next

        if sgn(func(a)) == sgn(func(x_last)):
            a = x_last
        if sgn(func(b)) == sgn(func(x_last)):
            b = x_last

        n += 1
        x_next = (a+b)/2

    return x_next, n, asterio


def mod_newton(a, b, f, dfn, ell):
    x = 1
    n = 0
    x_new = 4.74
    dfn = dfn(x_new)

    while (abs(x_new - x)) > ell or (x_new >= a and x_new <= b):
        x = x_new
        x_new = x - (f(x) / dfn)
        n += 1
    return x, n
