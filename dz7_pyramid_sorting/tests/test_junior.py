from dz7_pyramid_sorting.junior import heap_sort, selection_sort
from utils.arr import get_random_arr
from utils.decorators import CSVOutput


def test_selection_sort():
    arr = get_random_arr(500)
    new_sort_arr = selection_sort(arr)

    assert new_sort_arr == sorted(arr)


def test_heap_sort():
    arr = get_random_arr(700)
    new_sort_arr = heap_sort(arr)

    assert new_sort_arr == sorted(arr)


@CSVOutput(folder="dz7_pyramid_sorting")
def start(n, arr):
    """"""
    new_sort_arr = heap_sort(arr)


def test_start():

    for n in [100, 1000, 10000, 100000, 1000000]:
        arr = get_random_arr(n)
        start(n=n, arr=arr)
