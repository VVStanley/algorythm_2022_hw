from dz9_line_sort.junior import bucket_sort, counting_sort, radix_sort
from utils.arr import get_random_arr, get_random_arr_three_digits
from utils.decorators import CSVOutput


def test_bucket_sort() -> None:
    arr = get_random_arr(500)
    new_sort_arr = bucket_sort(arr)

    assert new_sort_arr == sorted(arr)


def test_counting_sort() -> None:
    arr = get_random_arr(500)
    new_sort_arr = counting_sort(arr)

    assert new_sort_arr == sorted(arr)


def test_radix_sort() -> None:
    arr = get_random_arr_three_digits(500)
    new_sort_arr = radix_sort(arr)

    assert new_sort_arr == sorted(arr)


@CSVOutput(folder="dz9_line_sort")
def start(n, arr):
    """"""
    radix_sort(arr)


def test_start():

    for n in [100, 1000, 10000, 100000, 1000000]:
        arr = get_random_arr_three_digits(n)
        start(n=n, arr=arr)
