from typing import List


def selection_sort(arr: List[int]) -> List[int]:
    """Сортировка выбором"""
    for i in range(len(arr)):
        min_item = arr[i]
        for item in arr:
            if min_item < item:
                arr[i] = item
                min_item = item
    return arr


def heap_sort(arr: List[int]) -> List[int]:
    """Пирамидальная сортировка"""

    def heapify(root, size):
        x = root
        l = 2 * x + 1
        r = l + 1
        if l < size and arr[l] > arr[x]:
            x = l
        if r < size and arr[r] > arr[x]:
            x = r
        if x == root:
            return
        arr[root], arr[x] = arr[x], arr[root]
        heapify(x, size)

    for h in range(len(arr) // 2 - 1, -1, -1):
        heapify(h, len(arr))
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(0, i)
    return arr
