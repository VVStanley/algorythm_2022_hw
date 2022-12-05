from typing import Any

from dz4_arrays.factor_array import FactorArray
from dz4_arrays.common import ABCArray
from dz4_arrays.single_array import SingleArray


class MatrixArray(ABCArray):
    """Массив матрица

    [
        [1,2,3,4],
        [5,6,7,8],
        [9],
    ]
    """

    def __init__(self) -> None:
        super().__init__()
        self._array = FactorArray()
        self._size_row = 50
        self._size = 0

    def __contains__(self, item):
        return any([item in array for array in self._array if array])

    def __getitem__(self, index):
        row = index // self._size_row
        index = index % self._size_row
        return self._array[row][index]

    @property
    def _row(self) -> int:
        """Текущий массив"""
        return self._size // self._size_row

    @property
    def _index(self) -> int:
        """Текущий индекс"""
        return self._size % self._size_row

    def size(self) -> int:
        """Получение размера массива"""
        return self._size

    def remove(self, index) -> Any:
        """Удаляем и возвращаем элемент по индексу"""
        row = index // self._size_row
        array = self._array[row]
        item = array.remove(index % self._size_row)

        # перестановки в массиве если удаленный элемент не последний
        if index != self._size - 1 and array.size() != self._size - 1:
            for i, array in enumerate(self._array[row:], start=row):
                if array and self._array[i + 1]:
                    array.add(self._array[i + 1].remove(0))
                else:
                    break
        self._size -= 1
        return item

    def insert(self, item, index) -> None:
        """Вставляем элемент по индексу"""
        row = index // self._size_row
        array = self._array[row]
        array.insert(item, index % self._size_row)

        # перестановки если массив вышел за рамки
        if array.size() > self._size_row:
            for i, array in enumerate(self._array[row:], start=row):
                if array and array.size() > self._size_row:
                    if self._array[i + 1] is None:
                        self._array.add(SingleArray())
                    self._array[i + 1].insert(
                        array.remove(array.size() - 1),
                        0
                    )
                else:
                    break
        self._size += 1

    def add(self, item) -> None:
        """Добавляем элемент"""
        if self._index == 0:
            self._array.add(SingleArray())
        self._array[self._row].add(item)
        self._size += 1
