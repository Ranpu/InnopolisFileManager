import random


def print_field(field):
    for row in field:
        print("|\t", "\t|\t".join(row), "\t|")


def start_field():
    furniture = ["Стол", "Стул", "Шкаф", "Стул", "Кресло", "     "]
    field = [[], []]

    for index in range(0, len(furniture)):
        new_index = random.randint(0, len(furniture) - 1)
        furniture[index], furniture[new_index] = furniture[new_index], furniture[index]

    while True:
        row = random.randint(0, 1)
        if len(field[row]) < 3:
            field[row].append(furniture.pop())
        if len(field[0]) == 3 and len(field[1]) == 3:
            break

    return field


def solution(field, sol):
    closet = []
    chair = []
    sol_closet = []
    sol_chair = []

    for row in range(2):
        chair_index = -1
        closet_index = -1
        sol_chair_index = -1
        sol_closet_index = -1

        try:
            chair_index = sol[row].index("Кресло")
        except ValueError:
            pass

        try:
            closet_index = sol[row].index("Шкаф")
        except ValueError:
            pass

        try:
            sol_closet_index = field[row].index("Кресло")
        except ValueError:
            pass

        try:
            sol_chair_index = field[row].index("Шкаф")
        except ValueError:
            pass

        if closet_index > -1:
            closet = [row, closet_index]

        if chair_index > -1:
            chair = [row, chair_index]

        if sol_chair_index > -1:
            sol_closet = [row, sol_chair_index]

        if sol_closet_index > -1:
            sol_chair = [row, sol_closet_index]

    return not (chair == sol_closet and closet == sol_chair)


def main():
    field = start_field()
    sol = [x[:] for x in field]

    while solution(field, sol):
        try:
            print_field(sol)
            print(
                "Введите координаты предмета, который"
                "хотите переместить (строка (0-1) столбец (0-2)): "
            )
            first_x, first_y = map(int, input().split())
        except ValueError:
            print("Для продолжения нужно ввести пару чисел через пробел")

        try:
            print_field(sol)
            print(
                "Введите координаты ячейки, куда"
                "хотите переместить выбранный предмет (строка (0-1) столбец (0-2)): "
            )
            second_x, second_y = map(int, input().split())
        except ValueError:
            print("Для продолжения нужно ввести пару чисел через пробел")

        if abs(first_x - second_x) + abs(first_y - second_y) != 1:
            print("Вы можете переместить предмет только на соседнюю ячейку.")
            continue

        if "     " not in [sol[first_x][first_y], sol[second_x][second_y]]:
            print("Один из элементов должен быть пустой ячейкой")
            continue

        try:
            sol[first_x][first_y], sol[second_x][second_y] = (
                sol[second_x][second_y],
                sol[first_x][first_y],
            )
        except IndexError:
            print("Строка должна быть в диапазоне от 0 до 1, а столбец от 0 до 2")
            continue

    print("Поздравляем, вы поменяли шкаф и кресло местами!")


if __name__ == "__main__":
    main()
