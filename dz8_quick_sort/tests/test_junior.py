from dz8_quick_sort.junior import merge_sort, quick_sort
from utils.arr import get_random_arr
from utils.decorators import CSVOutput


def test_quick_sort() -> None:
    arr = get_random_arr(500)
    new_sort_arr = quick_sort(arr)

    assert new_sort_arr == sorted(arr)


def test_merge_sort() -> None:
    arr = get_random_arr(500)
    new_sort_arr = merge_sort(arr)

    assert new_sort_arr == sorted(arr)


@CSVOutput(folder="dz8_quick_sort")
def start(n, arr):
    """"""
    merge_sort(arr)


def test_start():

    for n in [100, 1000, 10000, 100000, 1000000]:
        arr = get_random_arr(n)
        start(n=n, arr=arr)
