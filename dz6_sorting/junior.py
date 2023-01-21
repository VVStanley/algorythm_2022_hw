from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """Сортировка пузырьком"""
    amount = len(arr) - 1
    while amount >= 0:
        for index in range(amount):
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
        amount -= 1
    return arr


def insertion_sort(arr: List[int]) -> List[int]:
    """Сортировка вставками"""
    counter = 1
    while counter < len(arr):
        for index in range(counter, 0, -1):
            if arr[index] < arr[index - 1]:
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
            else:
                break
        counter += 1
    return arr


def shell_sort(arr: List[int]) -> List[int]:
    """Шелл сортировка"""
    gap = len(arr) // 2
    while gap > 0:
        tmp_indexes = [i for i in range(0, len(arr), gap)]
        counter = 1
        while counter < len(tmp_indexes):
            for index in range(counter, 0, -1):
                if arr[tmp_indexes[index]] < arr[tmp_indexes[index - 1]]:
                    arr[tmp_indexes[index]], arr[tmp_indexes[index - 1]] = (
                        arr[tmp_indexes[index - 1]],
                        arr[tmp_indexes[index]],
                    )
                else:
                    break
            counter += 1
        gap //= 2
    return arr
