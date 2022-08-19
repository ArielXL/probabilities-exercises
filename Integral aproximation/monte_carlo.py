import math
import random
import numpy as np
import matplotlib.pyplot as plt


def monte_carlo(func):

    x = np.linspace(-20, 20, 1000)
    N = 10000

    # definiendo los limites del rectangulo
    rectangle_x = [-10, 10]
    rectangle_y = [-3, 3]

    # generando los puntos aleatorios
    points_x = np.random.uniform(min(rectangle_x), max(rectangle_x), N)
    points_y = np.random.uniform(min(rectangle_y), max(rectangle_y), N)

    # definiendo los puntos bajo la curva
    points_under = [True if points_y[i] <= func(
        points_x[i]) else False for i in range(len(points_x))]

    # ploteando los puntos obtenidos
    plt.figure('Aproximación de la integral')
    plt.plot(x, func(x), linewidth=5, c='k')
    plt.scatter(points_x[points_under], points_y[points_under], c='r', s=15)
    plt.scatter(points_x[np.logical_not(points_under)],
                points_y[np.logical_not(points_under)], c='b', s=15)
    plt.xlim(rectangle_x)
    plt.ylim(rectangle_y)
    plt.show()

    # calculando la integral
    integral = (max(rectangle_x) - min(rectangle_x)) * \
        (max(rectangle_y) - min(rectangle_y)) * sum(points_under) / N

    # imprimiendo el valor de la integral
    print(f'Estimado de la integral: {round(integral, 5)}')
