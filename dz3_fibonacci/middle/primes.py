from utils.decorators import CSVOutput
import math


def is_prime(n: int) -> int:
    """Проверяем простое ли число"""
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n) + 1), 2):
        if n % i == 0:
            return False

    return True


@CSVOutput(folder='dz3_fibonacci')
def get_primes(n: int) -> int:
    """Алгоритм поиска простых чисел с оптимизациями поиска
    и делением только на простые числа,

    Сложность O(N * Sqrt(N) / Ln (N))
    """
    dividers_count = 0

    for i in range(1, n + 1):
        dividers_count += 1 if is_prime(i) else 0

    return dividers_count
