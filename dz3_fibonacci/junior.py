def exponentiation(number: float, power: int) -> float:
    """Итеративный алгоритм возведения числа в степень.

    Сложность O(N)
    """
    result = 1
    for _ in range(power):
        result *= number
    return result


def fibonacci_recursive(number: int) -> int:
    """Рекурсивный алгоритм поиска чисел Фибоначчи.

    Сложность O(2^N)
    """
    if number == 0 or number == 1:
        return 1
    return fibonacci_recursive(number - 1) + fibonacci_recursive(number - 2)


def fibonacci_iterative(number: int) -> int:
    """Итеративный алгоритм поиска чисел Фибоначчи.

    Сложность O(N)
    """
    a = 1
    b = 1
    for _ in range(2, number + 1):
        a, b = b, a + b

    return b
