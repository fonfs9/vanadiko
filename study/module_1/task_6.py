""" Создай кортеж из 3 чисел и выведи его.

Преобразуй кортеж в список, добавь элемент, затем обратно в кортеж.

Используй кортеж как координаты точки (x, y) и выведи их по отдельности."""


def create_tuple():
    numbers = (21, 12, 345)
    numbers_list = list(numbers)
    numbers_list.append(4)
    numbers = tuple(numbers_list)

    print(numbers)


def get_coordinates_by_tuple():
    point = (3, 5)

    print("Координата X:", point[0])
    print("Координата Y:", point[1])


create_tuple()
get_coordinates_by_tuple()
