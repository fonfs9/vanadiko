def simple_calculator_for_two_numbers():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    print("Сумма:", a + b)
    print("Разность:", a - b)
    print("Произведение:", a * b)
    print("Частное:", a / b)


def area():
    length = float(input("Введите длину прямоугольника: "))
    width = float(input("Введите ширину прямоугольника: "))
    area = length * width
    print('площадь прямоугольника',area)

simple_calculator_for_two_numbers()
area()
