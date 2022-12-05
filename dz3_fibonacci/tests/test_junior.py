from dz3_fibonacci.junior import (
    exponentiation, fibonacci_iterative,
    fibonacci_recursive, get_primes,
)


def test_get_primes(primes_payload) -> None:
    """Тестируем алгоритм поиска количества простых чисел"""

    for test_data in primes_payload:
        n = int(test_data['in']['N'])
        if n > 10000:
            break
        assert get_primes(n=n) == int(test_data['out'])


def test_exponentiation(power_payload) -> None:
    """Тестируем возведение в степень."""
    for test_data in power_payload:
        a = float(test_data['in']['A'])
        n = int(test_data['in']['N'])
        if n > 100000000:
            break
        assert round(exponentiation(n=a, power=n), 11) == (
            float(test_data['out'])
        )


def test_fibonacci_recursive(fibo_payload) -> None:
    """Тестируем получение числа Фибоначчи"""
    for test_data in fibo_payload:
        n = int(test_data['in']['N'])
        if n > 50:
            break
        assert fibonacci_recursive(n=n) == int(test_data['out'])


def test_fibonacci_iterative(fibo_payload) -> None:
    """Тестируем получение числа Фибоначчи"""

    for test_data in fibo_payload:
        n = int(test_data['in']['N'])
        if n > 100000:
            break
        assert fibonacci_iterative(n=n) == int(test_data['out'])
