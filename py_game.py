field = list(range(1, 10))


wins = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
        (1, 4, 7), (2, 5, 8), (3, 6, 9),
        (1, 5, 9), (3, 5, 7)]


def print_field():
    for a in range(3):
        print(field[0 + a * 3], field[1 + a * 3], field[2 + a * 3])


def input_move(playar):
    while True:
        playar_move = input("Ваш ход " + playar + " ")
        if not (playar_move in "123456789"):
            print("Повторите ввод используя цифры от 1-9")
            continue
        playar_move = int(playar_move)
        if str(field[playar_move - 1]) in 'XO':
            print("Это место уже занято")
            continue
        field[playar_move - 1] = playar
        break


def wins_playar():
    for check in wins:
        if (field[check[0] - 1]) == (field[check[1] - 1]) == (field[check[2] - 1]):
            return field[check[1] - 1]
    else:
        return False


def game():
    turn = 0
    while True:
        print_field()
        if turn % 2 == 0:
            input_move("X")
        else:
            input_move("O")
        if turn > 3:
            playar_wins = wins_playar()
            if playar_wins:
                print_field()
                print("Победил "+playar_wins )
                break
        turn = turn + 1
        if turn>8:
            print_field()
            print("Ничья")
            break
game()