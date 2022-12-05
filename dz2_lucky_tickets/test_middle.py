import sys

from dz2_lucky_tickets.middle import Algorithm, Recursive


def test_recursive_calc_lucky_ticket() -> None:
    """Тестируем вычисление счастливых билетов. MIDDLE"""
    sys.setrecursionlimit(19000)

    payload = [
        {'in': 1, 'out': 10},
        # {'in': 2, 'out': 670},  # TODO Fatal Python error: Segmentation fault
        # {'in': 3, 'out': 55252},
    ]

    for test_data in payload:
        solver = Recursive(n=test_data['in'])
        assert solver.solve() == test_data['out']


def test_algorithm_calc_lucky_ticket() -> None:
    payload = [
        {'in': 1, 'out': 10},
        # {'in': 2, 'out': 670},
        # {'in': 3, 'out': 55252},
    ]

    for test_data in payload:
        solver = Algorithm(n=test_data['in'])
        assert solver.solve() == test_data['out']
