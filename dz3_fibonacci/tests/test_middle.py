from dz3_fibonacci.middle.exponentiation import (
    exponentiation_exponent,
    exponentiation_multiplication,
)
from dz3_fibonacci.middle.fibonacci import (
    fibonacci_golden_section,
    fibonacci_matrix_exponentiation_exponent, fibonacci_multiplication_matrix,
)
from dz3_fibonacci.middle.primes import get_primes
from utils.matrix import Matrix


def test_fibonacci_matrix_exponentiation_exponent(fibo_payload) -> None:
    """Поиск чисел Фибоначчи через двоичное
    разложение показателя степени
    """
    for test_data in fibo_payload:
        n = int(test_data['in']['N'])
        if n > 10000:
            break
        assert fibonacci_matrix_exponentiation_exponent(n=n) == (
            int(test_data['out'])
        )


def test_get_primes(primes_payload) -> None:
    """Тестируем алгоритм поиска простых чисел"""

    for test_data in primes_payload:
        n = int(test_data['in']['N'])
        if n > 10000:
            break
        assert get_primes(n=n) == int(test_data['out'])


def test_fibonacci_golden_section(fibo_payload) -> None:
    """Тестируем получение числа Фибоначчи"""

    for test_data in fibo_payload:
        n = int(test_data['in']['N'])
        if n > 71:
            break
        assert fibonacci_golden_section(n=n) == int(test_data['out'])


def test_fibonacci_multiplication_matrix(fibo_payload) -> None:
    """Поиск чисел Фибоначчи через умножение матриц"""

    for test_data in fibo_payload:
        n = int(test_data['in']['N'])
        if n > 10000:
            break
        assert fibonacci_multiplication_matrix(n=n) == int(test_data['out'])


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


def test_exponentiation_multiplication(power_payload) -> None:
    """Тестируем возведение в степень."""

    for test_data in power_payload:
        a = float(test_data['in']['A'])
        n = int(test_data['in']['N'])
        assert round(exponentiation_multiplication(n=a, power=n), 11) == round(
            float(test_data['out']), 11
        )


def test_exponentiation_exponent(power_payload) -> None:
    """Тестируем возведение в степень."""

    for test_data in power_payload:
        a = float(test_data['in']['A'])
        n = int(test_data['in']['N'])
        assert round(exponentiation_exponent(n=a, power=n), 6) == round(
            float(test_data['out']), 6
        )
