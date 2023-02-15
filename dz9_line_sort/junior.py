from typing import List

from utils.linked_list import LinkedListWithSort


def radix_sort(arr: List[int]) -> List[int]:
    """Поразрядная сортировка"""

    def in_counting_sort(exp1):
        counting = [0] * 10
        new_arr = [0] * len(arr)

        for elem in arr:
            index = elem // exp1
            counting[index % 10] += 1

        for index in range(1, 10):
            counting[index] += counting[index - 1]

        i = len(arr) - 1
        while i >= 0:
            index = arr[i] // exp1
            new_arr[counting[index % 10] - 1] = arr[i]
            counting[index % 10] -= 1
            i -= 1

        return new_arr

    max_elem = max(arr)
    exp = 1
    while max_elem / exp >= 1:
        arr = in_counting_sort(exp)
        exp *= 10

    return arr


def counting_sort(arr: List[int]) -> List[int]:
    """Сортировка подсчетом"""
    counting = [0] * (max(arr) + 1)
    new_arr = [0] * len(arr)

    for elem in arr:
        counting[elem] += 1

    for index in range(1, len(counting)):
        counting[index] = counting[index] + counting[index - 1]

    for index in range(len(arr) - 1, -1, -1):
        counting[arr[index]] -= 1
        new_index = counting[arr[index]]
        new_arr[new_index] = arr[index]

    return new_arr


def bucket_sort(arr: List[int]) -> List[int]:
    """Ведерная сортировка"""
    buckets = [LinkedListWithSort() for _ in range(len(arr))]
    max_elem = max(arr)
    for elem in arr:
        index = int(elem * len(arr) / (max_elem + 1))
        buckets[index].append(elem)

    new_arr = []

    for bucket in buckets:
        if bucket.head:
            node = bucket.head
            new_arr.append(node.element)
            while node.next_node:
                node = node.next_node
                new_arr.append(node.element)
    return new_arr
