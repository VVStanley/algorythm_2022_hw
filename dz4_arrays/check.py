from random import randint

from dz4_arrays.common import ABCArray
from dz4_arrays.matrix_array import MatrixArray
from utils.decorators import CSVOutput


@CSVOutput(folder='dz4_arrays')
def check_add(array: ABCArray, n: int) -> ABCArray:
    """Запускаем добавление элементов"""
    for item in range(n):
        array.add(item)
    return array


@CSVOutput(folder='dz4_arrays')
def check_insert(array: ABCArray, n: int) -> None:
    """Запускаем вставку элементов"""
    for item in range(n):
        array.insert(item=item, index=randint(0, array.size() - 1))


@CSVOutput(folder='dz4_arrays')
def check_remove(array: ABCArray, n: int) -> None:
    """Запускаем удаление элементов"""
    for _ in range(n):
        array.remove(index=randint(0, array.size() - 1))


if __name__ == '__main__':

    for n in [10, 100, 1000, 10000, 100000, 1000000]:
        array = MatrixArray()
        for _ in range(100):
            array.add(1)
        check_insert(array=array, n=n)
