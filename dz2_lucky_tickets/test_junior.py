from dz2_lucky_tickets.junior import calc_lucky_ticket1, calc_lucky_ticket2


def test_junior_calc_lucky_ticket1() -> None:
    """Тестируем вычисление счастливых билетов. JUNIOR"""
    assert calc_lucky_ticket1() == 55252


def test_junior_calc_lucky_ticket2() -> None:
    """Тестируем вычисление счастливых билетов. JUNIOR"""
    assert calc_lucky_ticket2() == 55252
