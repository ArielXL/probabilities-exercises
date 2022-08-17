from monty_hall import MontyHall


def print_values(n, switch, wins, losses, percent):
    if switch:
        print(f'Para {n} juegos de Monty Hall cambiando de puerta:')
    else:
        print(f'Para {n} juegos de Monty Hall sin cambiar de puerta:')

    print(f'-> juegos ganados = {wins}')
    print(f'-> juegos perdidos = {losses}')

    if switch:
        print(
            f'-> por ciento de juegos ganados cambiando de puerta = {round(percent, 5)}%')
    else:
        print(
            f'-> por ciento de juegos ganados sin cambiar de puerta = {round(percent, 5)}%')


def play(n, switch):

    wins, losses = 0, 0

    for i in range(n):
        monty_hall = MontyHall()
        if monty_hall.run_game(switch):
            wins += 1
        else:
            losses += 1

    total = wins + losses
    if switch:
        percent = 100 * wins / total
    else:
        percent = 100 * wins / total

    return (wins, losses, percent)
