def factorial(n: int) -> int:
    """Обчислює факторіал числа n."""
    # TODO: Реалізувати через цикл for
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def harmonic_sum(n: int) -> float:
    """Обчислює суму гармонічного ряду: 1 + 1/2 + 1/3 + ... + 1/n."""
    # TODO: Реалізувати через цикл for
    total = 0.0
    for i in range(1, n + 1):
        total += 1 / i
    return total

def multiplication_table(n: int) -> None:
    """Виводить таблицю множення n × n."""
    #TODO: Використати вкладені цикли for та форматований вивід
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # :>4 вирівнювання по правому краю
            print(f"{i * j:>4}", end="")
        print()  # Перехід на новий рядок

def main():
    n = int(input("введіть число n: "))
    print(f"{n}! = {factorial(n)}")
    print(f"гармонічна сума H({n}) = {harmonic_sum(n):.6f}")
    print(f"\nтаблиця множення {n}×{n}:")
    multiplication_table(n)

if __name__ == "__main__":
    main()