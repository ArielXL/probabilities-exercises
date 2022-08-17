from utils import play, print_values

def main():
    n = 1000
    switch = True
    wins, losses, percent = play(n, switch)
    print_values(n, True, wins, losses, percent)
    print()

    switch = False
    wins, losses, percent = play(n, False)
    print_values(n, False, wins, losses, percent)

if __name__ == '__main__':
    main()