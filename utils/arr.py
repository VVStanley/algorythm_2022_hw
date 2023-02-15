from random import choices, randrange
from typing import List


def get_random_arr(n: int) -> List[int]:
    sort_arr = [i for i in range(n)]
    return choices(sort_arr, k=len(sort_arr))


def get_random_arr_three_digits(n: int) -> List[int]:
    return [randrange(99, 1000) for i in range(n)]
