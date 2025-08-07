"""Создай множество из списка с повторяющимися значениями.

Проверь, содержится ли элемент в множестве.

Создай два множества и выведи:

их объединение

пересечение

разность
"""


def dasd():
    numbers_list = [1, 2, 2, 3, 4, 4, 5]

    numbers_set = set(numbers_list)

    print("Множество:", numbers_set)


dasd()


def osamason():

    numbers = ["1", "2", "2", "3", "4", "4", "5"]
    key = input("введите число")
    if key in numbers:
        print("Число есть в списке!")
    else:
        print("Числа нет в списке.")


osamason()


def ccc():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}

    union = set1 | set2
    print("Объединение:", union)

    intersection = set1 and set2
    print("Пересечение:", intersection)

    difference = set1 - set2
    print("Разность:", difference)


ccc()
