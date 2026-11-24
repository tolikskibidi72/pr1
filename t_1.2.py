def main():
    # TODO: Зчитати рядок від користувача
    raw_input = input("введіть число: ")

    # TODO: Перетворити в int, float, bool та вивести тип кожного
    # Використати функції: int(), float(), bool(), type(), isinstance()
    try:
        val_float = float(raw_input)
    except ValueError:
        print("помилка")
        return

    val_int = int(val_float)
    val_bool = bool(val_float)

    print(f"int: {val_int} | тип: {type(val_int)} | isinstance: {isinstance(val_int, int)}")
    print(f"float: {val_float} | тип: {type(val_float)} | isinstance: {isinstance(val_float, float)}")
    print(f"bool: {val_bool} | тип: {type(val_bool)} | isinstance: {isinstance(val_bool, bool)}")

    # TODO: Зчитати ім'я та вік, вивести форматоване повідомлення
    # Використати f-рядки з різними специфікаторами формату
    name = input("\nвведіть ваше ім'я: ")
    age_input = input("введіть ваш вік: ")

    try:
        age = int(age_input)
        print(f"повідомлення: ім'я: {name:>10} | вік: {age:03d}")
    except ValueError:
        print("помилка")

    # TODO: Продемонструвати роботу функцій id(), len(), range()
    #Наприклад: створити список з range(), вивести довжину, id об'єкта
    my_list = list(range(1, 6))
    print(f"\nсписок з range(): {my_list}")
    print(f"довжина списку len(): {len(my_list)}")
    print(f"id об'єкта: {id(my_list)}")

    pass


if __name__ == "__main__":
    main()