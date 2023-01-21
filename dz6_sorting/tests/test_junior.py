from random import choices
from typing import List

from dz6_sorting.junior import bubble_sort, insertion_sort, shell_sort
from utils.decorators import CSVOutput


def get_random_arr(n: int) -> List[int]:
    sort_arr = [i for i in range(n)]
    return choices(sort_arr, k=len(sort_arr))


def test_bubble_sort() -> None:
    arr = get_random_arr(500)
    new_sort_arr = bubble_sort(arr)

    assert new_sort_arr == sorted(arr)


def test_insertion_sort() -> None:
    arr = get_random_arr(500)
    new_sort_arr = insertion_sort(arr)

    assert new_sort_arr == sorted(arr)


def test_shell_sort() -> None:
    arr = get_random_arr(500)
    new_sort_arr = shell_sort(arr)

    assert new_sort_arr == sorted(arr)


@CSVOutput(folder="dz6_sorting")
def start(n):
    """"""
    arr = get_random_arr(n)
    new_sort_arr = shell_sort(arr)
    assert new_sort_arr == sorted(arr)


def test_start():
    start(n=100)
    start(n=1000)
    start(n=10000)
