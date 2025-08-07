"""Создай список из 5 любых чисел — выведи сумму, максимум и минимум.

Пользователь вводит 3 строки — помести их в список и выведи в обратном порядке.

Дан список чисел — выведи только чётные.

Удали из списка все повторяющиеся элементы.

Добавь элемент в список, затем удали его."""


def get_info_about_numbers(numbers: list):
    print("Список чисел:", numbers)
    print("Сумма чисел:", sum(numbers))
    print("Максимум:", max(numbers))
    print("Минимум:", min(numbers))


def get_reverse_list():
    numbers = []

    for i in range(3):
        num = float(input(f"Введите число {i + 1}: "))
        numbers.append(num)

    print("Ваш список чисел:", numbers)
    reversed_list = list(reversed(numbers))
    print("Список в обратном порядке:", reversed_list)


def get_only_even_from_numbers(numbers: list):
    print("Ваш список чисел:", numbers)

    for number in numbers:
        if number % 2 == 0:
            print(number, "— чётное")
        else:
            print(number, "— нечётное")


def get_only_unique_from_numbers(numbers: list):
    unique_numbers = list(set(numbers))
    print("Список без повторов:", unique_numbers)


def add_and_delete_number_from_list(numbers: list):
    print("Исходный список:", numbers)

    numbers.append(10)
    print("После добавления 10:", numbers)

    numbers.remove(10)
    print("После удаления 10:", numbers)


get_info_about_numbers([12, 7, 25, 3, 18])
get_reverse_list()
get_only_even_from_numbers([12, 23, 91237, 1231, 122, 230, 2001, 29234])
get_only_unique_from_numbers([12, 23, 12, 7, 23, 5, 7, 9])
add_and_delete_number_from_list([12, 21, 36, 412, 5313])
