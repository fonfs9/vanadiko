def greet_user():
    name = input("Введите ваше имя: ")
    print("Привет!", name)
    length = len(name)
    upper_text = name.upper()
    lower_text = name.lower()
    print("В верхнем регистре:", upper_text)
    print("В нижнем регистре:", lower_text)

    if length == 0:
        print("Строка пустая.")
    else:
        print("Первый символ:", name[0])
        print("Последний символ:", name[-1])

        if length % 2 == 1:
            middle_index = length // 2
            print("Центральный символ:", name[middle_index])
        else:
            middle_left = length // 2 - 1
            middle_right = length // 2
            print("Средние символы:", name[middle_left], name[middle_right])
def char():
            text = input("Введите текст: ")
            char = input("Введите символ или строку для поиска: ")

            if char in text:
                print("Да, символ или строка найдены!")
            else:
                print("Нет, такого символа или строки в тексте нет.")

greet_user()
char()
