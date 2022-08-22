from pi import pi


def main():
    print('El valor real de pi es 3.141592654\n')

    list = [10000, 1000000, 100000000]
    for i in list:
        print(
            'El valor de aproximado de pi es {0:2.8f} para N = {1}'.format(pi(i), i))
        print('---------------------------------------------------------------')


if __name__ == '__main__':
    main()
