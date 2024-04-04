import random
from pystyle import Box

field = [["-"] * 3 for i in range(3)]


def start():
    text = f"{'Крестики-Нолики'.center(26)}\n" \
           f"{'Добро пожаловать в игру!'.center(26)}\n\n" \
           f"{'Меню:'.center(26)}\n\n" \
           f"{' 1. Начать игру'}\n" \
           f"{' 2. Выйти из игры'}"

    print(Box.DoubleCube(text))

    menu = 0
    point = 0

    while True:
        try:
            menu = int(input("Введите номер пункта меню: "))

            if menu in [1, 2]:
                break
            else:
                raise ValueError

        except ValueError:
            print()
            print(Box.DoubleCube(f"{'Номер пункта меню введён не правильно!'.center(40)}\n{'Повторите попытку...'.center(40)}"))
            continue

    if menu == 1:
        text = f'{"Доступные символы:".center(26)}\n' \
               f'{"1. O".center(26)}\n' \
               f'{"2. X".center(26)}'

        print(Box.DoubleCube(text))

        while True:
            try:
                point = int(input("Введите номер знака: "))

                if point in [1, 2]:
                    break
                else:
                    raise ValueError

            except ValueError:
                print()
                print(Box.DoubleCube(f"{'Номер знака введён не правильно!'.center(40)}\n{'Повторите попытку...'.center(40)}"))
                continue

        if point == 1:
            print(Box.DoubleCube(f"Ваш символ: O".center(26)))
            return "O", "X"
        else:
            print(Box.DoubleCube(f"Ваш символ: X".center(26)))
            return "X", "O"
    else:
        print(Box.DoubleCube("Вы вышли из игры!".center(26)))
        exit(0)


def check_win(point):
    # Проверка выигрышных комбинаций по горизонталям и вертикалям
    for i in range(3):
        if all(field[i][j] == point for j in range(3)) or all(field[j][i] == point for j in range(3)):
            return True

    # Проверка выигрышных комбинаций по диагоналям
    if all(field[i][i] == point for i in range(3)) or all(field[i][2 - i] == point for i in range(3)):
        return True

    # Проверка на ничью
    if all(all(cell != "-" for cell in row) for row in field):
        return "Ничья"

    return False


def show():
    text = f"   0 1 2 \n"

    for i in range(3):
        text += f" {i} {field[i][0]} {field[i][1]} {field[i][2]} \n"

    print(f"{'Игровое поле'.center(14)}")
    print(Box.DoubleCube(text))


def computer_move(computer_point):
    available_moves = [(i, j) for i in range(3) for j in range(3) if field[i][j] == "-"]
    move = random.choice(available_moves)
    x, y = move
    field[x][y] = computer_point


def get_cords(user_point, computer_point):
    while True:
        try:
            x, y = map(int, input("Введите ваш ход: ").split())

            if x in [0, 1, 2] and y in [0, 1, 2]:
                break
            else:
                raise ValueError
        except ValueError:
            print()
            text = f"{'Ход введён не правильно!'.center(40)}\n" \
                   f"{'Повторите попытку...'.center(40)}\n"
            print(Box.DoubleCube(text))

    if field[x][y] != "-":
        print(Box.DoubleCube("Ячейка занята!"))
        show()
    else:
        field[x][y] = user_point

        if check_win(user_point):
            if check_win(user_point) == "Ничья":
                print(Box.DoubleCube("Ничья!!!"))
                print()
                show()
                exit(0)
            else:
                print(Box.DoubleCube("Вы победили!!!"))
                print()
                show()
                exit(0)
        else:
            computer_move(computer_point)

        print()
        show()


def main():
    user_point, computer_point = start()
    show()

    while True:
        get_cords(user_point, computer_point)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nВы вышли из программы!")
