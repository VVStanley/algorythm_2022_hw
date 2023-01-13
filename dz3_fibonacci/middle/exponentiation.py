import math

from utils.decorators import CSVOutput


@CSVOutput(folder='dz3_fibonacci')
def exponentiation_multiplication(n: float, power: int) -> float:
    """Алгоритм возведения в степень через домножение
    31 -> 16,8,4,2,1

    Сложность O(N/2+LogN)
    """

    result = 1

    tres = []

    while power >= 1:
        res = 2 ** int(math.log2(power))
        tres.append(res)
        power -= res
        result *= n ** res

    return result


@CSVOutput(folder='dz3_fibonacci')
def exponentiation_exponent(n: float, power: int) -> float:
    """Алгоритм возведения в степень
    через двоичное разложение показателя степени

    Сложность O(2LogN)
    """
    d = n
    p = d if power % 2 > 0 else 1

    while power >= 1:
        power = power // 2
        d = d * d
        if power % 2 > 0:
            p = p * d

    return p
