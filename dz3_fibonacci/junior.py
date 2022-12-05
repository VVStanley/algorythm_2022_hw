from utils.decorators import CSVOutput


@CSVOutput(folder='dz3_fibonacci')
def get_primes(n: int) -> int:
    """Алгоритм поиска количества простых чисел через перебор делителей

    Сложность O(N^2)
    """
    dividers_count = 0

    for n in range(1, n + 1):  # noqa
        dividers = 0
        for i in range(1, n + 1):
            if n % i == 0:
                dividers += 1
        if dividers == 2:
            dividers_count += 1

    return dividers_count


@CSVOutput(folder='dz3_fibonacci')
def exponentiation(n: float, power: int) -> float:
    """Итеративный алгоритм возведения числа в степень.

    Сложность O(N)
    """
    result = 1
    for _ in range(power):
        result *= n
    return result


@CSVOutput(folder='dz3_fibonacci')
def fibonacci_recursive(n: int) -> int:
    """Рекурсивный алгоритм поиска чисел Фибоначчи.

    Сложность O(2^N)
    """
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


@CSVOutput(folder='dz3_fibonacci')
def fibonacci_iterative(n: int) -> int:
    """Итеративный алгоритм поиска чисел Фибоначчи.

    Сложность O(N)
    """
    if n == 0:
        return 0
    a = 1
    b = 1
    for _ in range(3, n + 1):
        a, b = b, a + b

    return b
