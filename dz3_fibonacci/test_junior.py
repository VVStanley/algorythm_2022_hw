from dz3_fibonacci.junior import (
    exponentiation, fibonacci_iterative,
    fibonacci_recursive,
)


def test_exponentiation() -> None:
    """Тестируем возведение в степень."""

    assert exponentiation(1.001, 1000) == 2.7169239322355985


def test_fibonacci_recursive() -> None:
    """Тестируем получение числа Фибоначчи
    1,1,2,3,5,8,13,21,34
    """
    assert fibonacci_recursive(8) == 34
    assert fibonacci_recursive(12) == 233
    assert fibonacci_recursive(17) == 2584


def test_fibonacci_iterative() -> None:
    """Тестируем получение числа Фибоначчи
    1,1,2,3,5,8,13,21,34
    """
    assert fibonacci_iterative(8) == 34
    assert fibonacci_iterative(12) == 233
    assert fibonacci_iterative(17) == 2584
