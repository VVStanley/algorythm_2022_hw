"""Счастливые билеты. JUNIOR"""


def calc_lucky_ticket1() -> int:
    """Считаем кол-во счастливых билетов в 6 значном билете

    Сложность O(N^6)
    """
    result = 0
    for a1 in range(10):
        for a2 in range(10):
            for a3 in range(10):
                for b1 in range(10):
                    for b2 in range(10):
                        for b3 in range(10):
                            s1 = a1 + a2 + a3
                            s2 = b1 + b2 + b3
                            if s1 == s2:
                                result += 1
    return result


def calc_lucky_ticket2() -> int:
    """Считаем кол-во счастливых билетов в 6 значном билете

    Сложность O(N^2)
    """
    zeros = {
        1: '00000',
        2: '0000',
        3: '000',
        4: '00',
        5: '0',
        6: '',
    }

    result = 0

    calc = lambda str_number: sum(map(int, [digit for digit in str_number]))

    for i in range(0, 1_000_000):
        str_number_ticket = '{}{}'.format(zeros.get(len(str(i))), i)
        if calc(str_number_ticket[:3]) == calc(str_number_ticket[3:]):
            result += 1

    return result


if __name__ == '__main__':

    calc_lucky_ticket1()
    calc_lucky_ticket2()

    # Ответ: 55252 Счастливых билетиков в 6 значном билете
