from utils import variations


def birthday(n):
    return 1 - (variations(366, n) / (366 ** n))


def main():

    people = [10, 20, 35, 60]

    for person in people:
        print(
            f'En un grupo de {person} personas, la probabilidad de que al menos dos personas cumplan años el mismo dia es {round(birthday(person), 5)}.')
        print('-----------------------------------------------------------------')


if __name__ == '__main__':
    main()
