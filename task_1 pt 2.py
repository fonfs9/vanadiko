""""сделал таблицу умножения до 10. сделал игру и добавил вывод всех четных чиселпш"""
def cycle():
 for i in range(1,11):
    for j in range(1,11):
        result = i * j
        print(i, "x", j, "=", result)
cycle()

def middle_number():
    count = int(input("Сколько чисел вы хотите ввести? "))
    numbers = []
    for i in range(count):
        number = float(input(f"Введите число №{i + 1}: "))
        numbers.append(number)
        average = sum(numbers) / len(numbers)
        print("Среднее арифметическое:", average)
middle_number()

def game():
    import random

    secret_number = random.randint(1, 100)
    max_attempts = 5

    for attempt in range(1, max_attempts + 1):
        guess = int(input(f"Попытка {attempt}. Введите число от 1 до 100: "))

        if guess < secret_number:
            print("Слишком маленькое число!")
        elif guess > secret_number:
            print("Слишком большое число!")
        else:
            print(f"🎉 Угадал за {attempt} попыток!")
            break
    else:
        print(f"😢 Увы, ты не угадал. Это было число {secret_number}")


game()


def even():
    even_numbers = []

    for i in range(1, 101):
        if i % 2 == 0:
            even_numbers.append(i)

    print("Чётные числа от 1 до 100:", even_numbers)

even()






