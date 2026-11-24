import math


def triangle_type(a: float, b: float, c: float) -> str:
    """Визначає тип трикутника за сторонами.

    Returns:
        Рядок з типом: 'рівносторонній', 'рівнобедрений',
        'прямокутний', 'різносторонній' або 'не є трикутником'.
    """
    # TODO: Перевірити нерівність трикутника
    if (a + b > c) and (a + c > b) and (b + c > a):

        # TODO: Визначити тип за допомогою вкладених if/elif/else
        # Перевірити: рівносторонній, рівнобедрений, прямокутний, різносторонній
        if a == b == c:
            return "рівносторонній"
        elif a == b or b == c or a == c:
            return "рівнобедрений"
        elif abs(a ** 2 + b ** 2 - c ** 2) < 1e-9 or abs(a ** 2 + c ** 2 - b ** 2) < 1e-9 or abs(
                b ** 2 + c ** 2 - a ** 2) < 1e-9:
            return "прямокутний"
        else:
            return "різносторонній"
    else:
        return "не є трикутником"


def triangle_area(a: float, b: float, c: float) -> float:
    """Обчислює площу трикутника за формулою Герона."""
    #TODO: Реалізувати формулу Герона
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area


def main():
    # TODO: Зчитати три сторони, вивести тип та площу
    a = float(input("введіть сторону a: "))
    b = float(input("Введіть сторону b: "))
    c = float(input("введіть сторону c: "))

    t_type = triangle_type(a, b, c)
    print(f"\nтип фігури: {t_type}")

    if t_type != "не є трикутником":
        area = triangle_area(a, b, c)
        print(f"Площа: {area:.4f}")


if __name__ == "__main__":
    main()