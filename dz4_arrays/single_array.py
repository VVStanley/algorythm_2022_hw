from typing import Any

from dz4_arrays.common import ABCArray


class SingleArray(ABCArray):
    """Простой массив при добавлении расширяется на один элемент"""

    def size(self) -> int:
        """Получение размера массива"""
        return self._array.__len__()

    def remove(self, index) -> Any:
        """Удаляем и возвращаем элемент по индексу"""
        item = self._array[index]
        self._array = (
            [item for item in self._array[:index]] +
            [item for item in self._array[index + 1:]]
        )
        return item

    def insert(self, item, index) -> None:
        """Вставляем элемент по индексу"""
        self._array = (
            [item for item in self._array[:index]] + [None] +
            [item for item in self._array[index:]]
        )
        self._array[index] = item

    def add(self, item) -> None:
        """Добавляем элемент"""
        self._array = [item for item in self._array] + [None]
        self._array[self.size() - 1] = item
