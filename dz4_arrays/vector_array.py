from typing import Any

from dz4_arrays.common import ABCArray


class VectorArray(ABCArray):
    """Вектор массив при расширении прибавляем несколько элементов"""

    def __init__(self) -> None:
        super().__init__()
        self._vector = 20
        self._capacity = 0
        self._size = 0

    def _resize(self):
        """Изменяем размер"""
        self._array = [i for i in self._array] + [None] * self._vector
        self._capacity += self._vector

    def size(self) -> int:
        """Получение размера массива"""
        return self._size

    def insert(self, item, index) -> None:
        """Вставляем элемент по индексу"""
        self._size += 1
        if self._size >= self._capacity:
            self._resize()
        self._array = (
            [item for item in self._array[:index]] + [None] +
            [item for item in self._array[index:]]
        )
        self._array[index] = item

    def remove(self, index) -> Any:
        """Удаляем и возвращаем элемент по индексу"""
        item = self._array[index]
        self._array = (
            [item for item in self._array[:index]] +
            [item for item in self._array[index + 1:]]
        )
        self._size -= 1
        return item

    def add(self, item) -> None:
        """Добавляем элемент"""
        self._size += 1
        if self._size >= self._capacity:
            self._resize()
        self._array[self._size - 1] = item
