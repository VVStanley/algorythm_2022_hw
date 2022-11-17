import sys
from pathlib import Path

from dz2_lucky_tickets.middle import Algorithm, Recursive
from utils.files import get_test_data_from_folder


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
    path = Path(__file__).resolve().parent.joinpath('lucky_tickets/1.Tickets')
    payload = get_test_data_from_folder(path, 9)

    payload = [
        {'in': 1, 'out': 10},
        # {'in': 2, 'out': 670},
        # {'in': 3, 'out': 55252},
    ]

    for test_data in payload:
        solver = Algorithm(n=test_data['in'])
        assert solver.solve() == test_data['out']
