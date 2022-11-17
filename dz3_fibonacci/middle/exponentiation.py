import math


def exponentiation_multiplication(number: float, power: int) -> float:
    """Алгоритм возведения в степень через домножение
    31 -> 16,8,4,2,1

    Сложность  O(N/2+LogN) = O(N)
    """

    result = 1

    tres = []
    p = []

    while power >= 1:
        res = 2 ** int(math.log2(power))
        tres.append(res)
        power -= res
        p.append(power)
        result *= number ** res

    return result


def exponentiation_exponent(number: float, power: int) -> float:
    """Алгоритм возведения в степень
    через двоичное разложение показателя степени

    Сложность   O(2LogN) = O(LogN)
    """
    d = number
    p = 1

    while power >= 1:
        power = power // 2
        d = d * d
        if power % 2 > 0:
            p = p * d

    return p
