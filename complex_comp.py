import numpy as np


def phi(z):
    return z + 3


def phi_inv(z):
    return z - 3


def f(z):
    return z**2 - 5


def p(z):
    return phi_inv(f(phi(z)))


def p2(z):
    return p(p(z))


print(p2(np.sqrt(2j + 5) - 3))
