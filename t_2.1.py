def classify_grade(score: int) -> str:
    """Повертає літерну оцінку ЄКТС за числовим балом.

    Args:
        score: числовий бал від 0 до 100.

    Returns:
        Літерна оцінка (A, B, C, D, E, FX, F).
    """
    # TODO: Реалізувати класифікацію за допомогою if/elif/else
    # A: 90-100, B: 82-89, C: 74-81, D: 64-73, E: 60-63, FX: 35-59, F: 0-34
    if score >= 90:
        return "A"
    elif score >= 82:
        return "B"
    elif score >= 74:
        return "C"
    elif score >= 64:
        return "D"
    elif score >= 60:
        return "E"
    elif score >= 35:
        return "FX"
    else:
        return "F"


def main():
    #TODO: Зчитати оцінку, перевірити діапазон, вивести результат
    raw = input("введіть оцінку (0-100): ")

    try:
        score = int(raw)
    except ValueError:
        print("помилка(не ціле число)")
        return

    if score < 0 or score > 100:
        print("Помилка(0 - 100)")
    else:
        grade = classify_grade(score)
        print(f"оцінка {score} → ЄКТС: {grade}")
        passed = grade not in ("FX", "F")
        print(f"результат: {'зараховано' if passed else 'не зараховано'}")


if __name__ == "__main__":
    main()