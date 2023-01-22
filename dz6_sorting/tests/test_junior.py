from dz6_sorting.junior import bubble_sort, insertion_sort, shell_sort
from utils.arr import get_random_arr
from utils.decorators import CSVOutput


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
def start(n, arr):
    """"""
    new_sort_arr = shell_sort(arr)


def test_start():

    for n in [100, 1000, 10000]:
        arr = get_random_arr(n)
        start(n=n, arr=arr)
