def calculator():
    """Інтерактивний калькулятор з підтримкою +, -, *, /, //, %, **."""
    print("=== Калькулятор ===")
    print("Введіть вираз у форматі: число оператор число")
    print("Введіть 'quit' для виходу, 'history' для історії")

    history = []

    while True:
        #TODO: Зчитати введення від користувача
        user_input = input("\n> ").strip()

        # TODO: Перевірити команди виходу ('quit') та історії ('history')
        # Використати break для виходу з циклу
        if user_input.lower() == 'quit':
            print("Роботу завершено.")
            break

        if user_input.lower() == 'history':
            for record in history:
                print(record)
            continue

        # Використати continue для пропуску некоректного введення
        parts = user_input.split()
        if len(parts) != 3:
            print("помилка. введіть вираз через пробіли")
            continue

        # TODO: Розібрати вираз на число1, оператор, число2
        num1_str, op, num2_str = parts

        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
            print("помилка. операнди мають бути числами")
            continue

        # TODO: Обчислити результат з перевіркою ділення на нуль
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("помилка ділення на нуль")
                continue
            result = num1 / num2
        elif op == '//':
            if num2 == 0:
                print("помилка. цілочисельне ділення на нуль")
                continue
            result = num1 // num2
        elif op == '%':
            if num2 == 0:
                print("Помилка. остача від ділення на нуль!")
                continue
            result = num1 % num2
        elif op == '**':
            result = num1 ** num2
        else:
            print("помилка. невідомий оператор")
            continue

        print(f"результат: {result}")

        # TODO: Зберегти результат в історію
        history.append(f"{num1} {op} {num2} = {result}")


if __name__ == "__main__":
    calculator()