import math

from dz3_fibonacci.middle.matrix import Matrix


def fibonacci_multiplication_matrix(number: int) -> int:
    """Алгоритм поиска чисел Фибоначчи через умножение матриц

    Сложность O(LogN)
    """
    start_matrix = Matrix(
        [
            [1, 1],
            [1, 0],
        ]
    )
    matrix = start_matrix.multiplication(start_matrix)

    for i in range(number - 3):
        matrix = matrix.multiplication(start_matrix)

    return matrix.get_item(0, 0)


def fibonacci_golden_section(number: int) -> int:
    """Алгоритм поиска чисел Фибоначчи по формуле золотого сечения.
    0,1,1,2,3,5,8,13,21,34

    Сложность O(1)
    """
    fi = (1 + math.sqrt(5)) / 2
    return int((fi ** number) / math.sqrt(5) + 0.5)