import random


def pi(N=10000000):
    inside = 0
    i = 0

    while i < N:
        x = random.random()
        y = random.random()
        if ((x ** 2 + y ** 2) <= 1):
            inside += 1

        i += 1

    return 4.0 * float(inside) / N
