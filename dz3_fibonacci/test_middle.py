from dz3_fibonacci.middle.exponentiation import (
    exponentiation_exponent,
    exponentiation_multiplication,
)
from dz3_fibonacci.middle.fibonacci import (
    fibonacci_golden_section,
    fibonacci_multiplication_matrix,
)
from dz3_fibonacci.middle.matrix import Matrix


def test_fibonacci_multiplication_matrix() -> None:
    """Поиск чисел Фибоначчи через умножение матриц"""

    assert fibonacci_multiplication_matrix(8) == 21
    assert fibonacci_golden_section(12) == 144
    assert fibonacci_golden_section(17) == 1597


def test_matrix_multiplication() -> None:
    """Тестируем умножение матриц"""

    m1 = Matrix(
        [
            [1, 1],
            [1, 0],
        ]
    )
    m2 = Matrix(
        [
            [1, 1],
            [1, 0]
        ]
    )

    m3 = m1.multiplication(m2)

    assert m3.to_list() == [
        [2, 1],
        [1, 1],
    ]

    m4 = m3.multiplication(m2)

    assert m4.to_list() == [
        [3, 2],
        [2, 1],
    ]


def test_exponentiation_multiplication() -> None:
    """Тестируем возведение в степень."""

    assert exponentiation_multiplication(5, 31) == 5 ** 31
    assert exponentiation_multiplication(8, 65) == 8 ** 65
    assert exponentiation_multiplication(99, 12) == 99 ** 12
    assert exponentiation_multiplication(123, 321) == 123 ** 321


def test_exponentiation_exponent() -> None:
    """Тестируем возведение в степень."""

    assert exponentiation_exponent(2, 100) == 2 ** 100  # Работает

    assert exponentiation_exponent(5, 31) == 5 ** 31  # Не работает


def test_fibonacci_golden_section() -> None:
    """Тестируем получение числа Фибоначчи
    0,1,1,2,3,5,8,13,21,34
    """
    assert fibonacci_golden_section(8) == 21
    assert fibonacci_golden_section(12) == 144
    assert fibonacci_golden_section(17) == 1597
