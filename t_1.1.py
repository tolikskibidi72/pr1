import math

def main():
    a = float(input("Введіть a: "))
    b = float(input("Введіть b: "))
    c = float(input("Введіть c: "))

    #1. сума квадратів: a² + b² + c²
    sum_squares = a**2 + b**2 + c**2

    # 2. середнє арифметичне
    average = (a + b + c) / 3

    # 3. дискримінант квадратного рівняння ax² + bx + c = 0
    discriminant = b**2 - 4 * a * c

    # 4. гіпотенуза прямокутного трикутника з катетами a, b
    hypotenuse = math.sqrt(a**2 + b**2)

    # 5.чи утворюють a, b, c сторони трикутника (нерівність трикутника)
    is_triangle = (a + b > c) and (a + c > b) and (b + c > a) and (a > 0 and b > 0 and c > 0)

    print("\n--- Результати обчислень ---")
    print(f"Сума квадратів: {sum_squares:.2f}")
    print(f"Середнє арифметичне: {average:.2f}")
    print(f"Дискримінант: {discriminant:.2f}")
    print(f"Гіпотенуза (за a та b): {hypotenuse:.2f}")
    print(f"Чи утворюють трикутник: {'Так' if is_triangle else 'Ні'}")

if __name__ == "__main__":
    main()