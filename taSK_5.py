def tixo():
    person = {
        "имя": "Константин",
        "возраст": 30,
        "город": "Санкт-Петербург"
    }
    print(person)

    key = input("Введите ключ (имя, возраст или город) ")

    if key in person:
        print("Значение:", person[key])
    else:
        print("Такого ключа нет в словаре.")

    person["email"] = "konst_anisimovgmail.com"
    print(person)

    del person["email"]
    print("Словарь после удаления:", person)

tixo()
