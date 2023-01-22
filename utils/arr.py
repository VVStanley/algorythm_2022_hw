from random import choices
from typing import List


def get_random_arr(n: int) -> List[int]:
    sort_arr = [i for i in range(n)]
    return choices(sort_arr, k=len(sort_arr))