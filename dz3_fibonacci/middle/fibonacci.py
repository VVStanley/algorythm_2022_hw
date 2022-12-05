import math

from utils.decorators import CSVOutput
from utils.matrix import Matrix


@CSVOutput(folder='dz3_fibonacci')
def fibonacci_matrix_exponentiation_exponent(n: int) -> int:
    """Алгоритм возведения матрицы в степень через двоичное
    разложение показателя степени

    Сложность   O(2LogN) = O(LogN)
    """
    d_matrix = Matrix(
        [
            [1, 1],
            [1, 0],
        ]
    )
    p_matrix = Matrix(
        [
            [1, 1],
            [1, 0],
        ]
    )

    power = n

    p_matrix = p_matrix.multiplication(p_matrix) if power % 2 > 0 else d_matrix

    while power >= 1:
        power = power // 2
        d_matrix = d_matrix.multiplication(d_matrix)
        if power % 2 > 0:
            p_matrix = p_matrix.multiplication(d_matrix)

    return p_matrix.get_item(1, 1)


@CSVOutput(folder='dz3_fibonacci')
def fibonacci_multiplication_matrix(n: int) -> int:
    """Алгоритм поиска чисел Фибоначчи через умножение матриц

    Сложность O(LogN)
    """
    start_matrix = Matrix(
        [
            [1, 1],
            [1, 0],
        ]
    )
    matrix = Matrix(
        [
            [1, 1],
            [1, 0],
        ]
    )

    for _ in range(n):
        matrix = matrix.multiplication(start_matrix)

    return matrix.get_item(1, 1)


@CSVOutput(folder='dz3_fibonacci')
def fibonacci_golden_section(n: int) -> int:
    """Алгоритм поиска чисел Фибоначчи по формуле золотого сечения.
    0,1,1,2,3,5,8,13,21,34

    Сложность O(1)
    """
    fi = (1 + math.sqrt(5)) / 2
    return int((fi ** n) / math.sqrt(5) + 0.5)
