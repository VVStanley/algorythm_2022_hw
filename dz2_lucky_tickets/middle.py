"""Счастливые билеты. MIDDLE"""
import abc


class CalcLuckyTicket(abc.ABC):
    """Абстрактный класс"""

    def __init__(self, n: int) -> None:
        """
        :param n: половина цифр билета
        """
        self.n = n
        self.counter = 0  # Кол-во счастливых билетов

    def solve(self) -> int:
        """Возвращаем кол-во счастливых билетов"""
        raise NotImplemented


class Algorithm(CalcLuckyTicket):
    """Вариант с алгоритмом"""

    # TODO доделать !!!!!!

    def solve(self) -> int:
        sum_digits_number = 9 * self.n
        for x in range(10):
            for total in range(sum_digits_number + 1):

                if x == total:
                    self.counter += 1
        return self.counter


class Recursive(CalcLuckyTicket):
    """Вариант с рекурсией"""

    def recursive(self, n: int, sum_a: int, sum_b: int) -> None:
        """Решение

        Сложность O(100 ^ n)
        """
        if n == 0:
            if sum_a == sum_b:
                self.counter += 1
            return

        for a in range(10):
            for b in range(10):
                self.recursive(self.n - 1, sum_a + a, sum_b + b)

    def solve(self) -> int | None:
        self.recursive(self.n, 0, 0)
        return self.counter
