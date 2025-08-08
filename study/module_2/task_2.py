"""
Напиши функцию, которая считает факториал числа.

Функция, которая определяет, является ли число простым.

Функция, которая проверяет, является ли слово палиндромом.

Напиши программу, которая использует эти функции и работает как мини-инструмент.

"""

import re


def factorial():
    result = 1
    fact = int(input("Факториал какого числа вы хотите получить? "))

    for i in range(1, fact + 1):
        result *= i

    print(f"Факториал {fact} равен", result)


def prime_number():
    fact = int(input("Введите число: "))

    if fact < 2:
        print("Это число не простое")
        return  # сразу выходим

    for i in range(2, fact):
        if fact % i == 0:
            print("Это число не простое")
            break
    else:
        print("Это число простое")


def palindrom():

    word = input("Введите слово или фразу: ")

    word = word.lower()
    word = re.sub(r"[^a-zа-я0-9]", "", word)

    if word == word[::-1]:
        print("Это палиндром!")
    else:
        print("Это не палиндром.")


# эту задачу я не особо понял, библиотеку не знаю, сложные схемы какие то


def instrument():
    while True:
        print("\nВыберите действие:")
        print("1. Посчитать факториал")
        print("2. Проверить, простое ли число")
        print("3. Проверить, является ли слово палиндромом")
        print("4. Выйти")

        choice = input("Ваш выбор: ")

        if choice == "1":
            result = 1
            fact = int(input("Факториал какого числа вы хотите получить? "))

            for i in range(1, fact + 1):
                result *= i

            print(f"Факториал {fact} равен", result)

        elif choice == "2":
            fact = int(input("Введите число: "))

            if fact < 2:
                print("Это число не простое")
                return  # сразу выходим

            for i in range(2, fact):
                if fact % i == 0:
                    print("Это число не простое")
                    break
            else:
                print("Это число простое")

        elif choice == "3":
            word = input("Введите слово или фразу: ")

            word = word.lower()
            word = re.sub(r"[^a-zа-я0-9]", "", word)

            if word == word[::-1]:
                print("Это палиндром!")
            else:
                print("Это не палиндром.")

        elif choice == "4":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор, попробуйте снова.")


factorial()
prime_number()
palindrom()
instrument()
