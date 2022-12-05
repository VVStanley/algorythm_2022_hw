from abc import ABC, abstractmethod
from typing import Any, Iterable, List


class ABCArray(ABC):
    """Абстрактный класс для создания массивов"""

    def __init__(self) -> None:
        self._array: List = []

    def __len__(self) -> int:
        return self._array.__len__()

    def __str__(self) -> str:
        return self._array.__str__()

    def __repr__(self) -> str:
        return self._array.__repr__()

    def __iter__(self) -> Iterable:
        return self._array.__iter__()

    def __getitem__(self, index: int) -> Any:
        return self._array.__getitem__(index)

    def __setitem__(self, key: int, value: Any) -> Any:
        return self._array.__setitem__(key, value)

    @abstractmethod
    def size(self) -> int:
        """Получение размера массива"""
        raise NotImplementedError

    @abstractmethod
    def remove(self, index: int) -> Any:
        """Удаляем и возвращаем элемент по индексу"""
        raise NotImplementedError

    @abstractmethod
    def insert(self, item: Any, index: int) -> None:
        """Вставляем элемент по индексу"""
        raise NotImplementedError

    @abstractmethod
    def add(self, item: Any) -> None:
        """Добавляем элемент"""
        raise NotImplementedError
