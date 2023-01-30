from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """Сортировка слиянием"""

    def merge(low: int, middle: int, high: int):
        n1 = middle - low + 1
        n2 = high - middle

        L = [0] * n1
        R = [0] * n2

        for i in range(0, n1):
            L[i] = arr[low + i]

        for j in range(0, n2):
            R[j] = arr[middle + 1 + j]

        i = 0
        j = 0
        k = low

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def sort(low: int, high: int):
        if low >= high:
            return
        middle = low + (high - low) // 2
        sort(low, middle)
        sort(middle + 1, high)
        merge(low, middle, high)

    sort(0, len(arr) - 1)

    return arr


def quick_sort(arr: List[int]) -> List[int]:
    """Быстрая сортировка"""

    def partition(low: int, high: int):
        p = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= p:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def sort(low: int, high: int):
        if low >= high:
            return
        m = partition(low, high)
        sort(low, m - 1)
        sort(m + 1, high)

    sort(0, len(arr) - 1)

    return arr
