""""Напиши программу, которая проверяет, больше ли первое число второго, и выводит True или False.

Пользователь вводит возраст — выведи, является ли он взрослым (18+).

Напиши логическую проверку: является ли число одновременно больше 10 и чётным.

Пользователь вводит строку — проверь, пуста ли она.
"""


def check_first_number_is_greater_than_second():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    if a > b:
        print("Да, первое число больше второго.")
    else:
        print("Нет, первое число меньше или равно второму.")


def check_age():
    a = float(input('введите ваш возраст'))

    if a < 18:
        print('вы не являетесь совершеннолетним')
    else:
        print('вы являетесь совершеннолетним')


def check_number_is_even_and_greater_10():
    number = int(input("Введите число: "))

    if number > 10 and number % 2 == 0:
        print("Число больше 10 и чётное.")
    else:
        print("Число НЕ одновременно больше 10 и чётное.")


def check_text_is_empty():
    text = input("Введите строку: ")

    if not text:
        print("Строка пустая.")
    else:
        print("Строка не пустая.")


check_first_number_is_greater_than_second()
check_age()
check_number_is_even_and_greater_10()
check_text_is_empty()
