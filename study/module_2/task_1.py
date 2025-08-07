""" " Вывести таблицу умножения от 1 до 10.

Программа спрашивает 5 чисел и выводит среднее.

Игра: угадай число от 1 до 100 (с ограничением по попыткам).

Найди все чётные числа от 1 до 100 и запиши их в список."""


def cycle():
    count = int(input("размерность таблицы умножения? "))
    for i in range(1, count + 1):
        for j in range(1, count + 1):
            result = i * j
            print(i, "X", j, "=", result)


def middle_number():
    count = int(input("Сколько чисел вы хотите ввести? "))
    numbers = []
    for i in range(count):
        number = float(input(f"Введите число №{i + 1}: "))
        numbers.append(number)
    average = sum(numbers) / len(numbers)
    print("Среднее арифметическое:", average)


def game():
    import random

    secret_number = random.randint(1, 100)
    max_attempts = 5

    for attempt in range(1, max_attempts + 1):
        guess = int(input(f"Попытка {attempt}. Введите число от 1 до 100: "))

        if guess < 0:
            print("нельзя вводить отрицательные числа")
        elif guess < secret_number:
            print("Слишком маленькое число!")
        elif guess > secret_number:
            print("Слишком большое число!")

        else:
            print(f"🎉 Угадал за {attempt} попыток!")
            break
    else:
        print(f"😢 Увы, ты не угадал. Это было число {secret_number}")


def even():
    count = int(input("до какого числа вывести все четные числа? "))
    even_numbers = []

    for i in range(1, count + 1):
        if i % 2 == 0:
            even_numbers.append(i)

    print(f"Чётные числа от 1 до {count} :", even_numbers)


if __name__ == "__main__":
    cycle()
    middle_number()
    game()
    even()
