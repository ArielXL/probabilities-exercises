from function import f
from monte_carlo import monte_carlo
from plot_function import plot_function


def main():

    plot_function(f)

    monte_carlo(f)


if __name__ == '__main__':
    main()
