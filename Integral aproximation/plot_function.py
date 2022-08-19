import numpy as np
import matplotlib.pyplot as plt


def plot_function(func):

    x = np.linspace(-20, 20, 1000)

    plt.figure('Gráfico de la integral')
    plt.plot(x, func(x), linewidth=3)
    plt.show()
