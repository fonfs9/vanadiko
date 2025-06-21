""""Преобразуй число в строку и обратно.

Преобразуй строку "1,2,3" в список чисел.

Преобразуй список в множество и обратно.

Проверь, можно ли строку "123abc" превратить в int (подумай, как отловить ошибку)."""

def srok():
    num = 123

    num_str = str(num)
    print("Строка:", num_str, type(num_str))

    num_back = int(num_str)
    print("Число:", num_back, type(num_back))


srok()

def str():
    str = '1,2,3'

    str_list = str.split(',')

    num_list = [int(x) for x in str_list]

    print(num_list)
str()


def ussn():
    numbers_list = [1, 2, 2, 3, 4, 4, 5]

    numbers_set = set(numbers_list)
    print("Множество:", numbers_set)

    numbers_list_unique = list(numbers_set)
    print("Список без повторений:", numbers_list_unique)


ussn()

def check():
    s = input("Введите число: ")

    try:
        num = int(s)
        print("Преобразование прошло успешно:", num)
    except ValueError:
        print("Ошибка: строку нельзя преобразовать в целое число.")

check()

