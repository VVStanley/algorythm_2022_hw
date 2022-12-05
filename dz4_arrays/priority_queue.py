from enum import IntEnum
from typing import Any


class MyPriorities(IntEnum):

    HIGH = 1
    MIDDLE = 2
    LOW = 3


class PriorityQueue:
    """Очередь с приоритетом"""

    def __init__(self) -> None:
        """Создание очереди"""
        self._queue = []

    def enqueue(self, priority: int, item: Any) -> None:
        """Добавляем элемент"""
        pass

    def dequeue(self) -> None:
        """Получить элемент из очереди"""
        pass
