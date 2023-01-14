from dataclasses import dataclass, field
from typing import Any, List, Union

from dz4_arrays.exeptions import Empty


@dataclass
class Root:
    value: Union[int, str]
    queue: list[Any] = field(default_factory=list)


class PriorityQueue:
    """Очередь с приоритетом"""

    def __init__(self) -> None:
        self._queue: List[Root] = []

    @property
    def _qsize(self):
        return len(self._queue)

    def _get_root_by_value(self, value: Union[str, int]) -> Root:
        return [root for root in self._queue if root.value == value][0]

    def _sorted_by_value(self) -> None:
        if all([str(root.value).isdigit() for root in self._queue]):
            self._queue = sorted(self._queue, key=lambda root: root.value)
        else:
            self._queue = sorted(self._queue, key=lambda root: str(root.value))

    def enqueue(self, priority: Union[int, str], item: Any) -> None:
        """Добавляем элемент"""
        if priority not in [root.value for root in self._queue]:
            self._queue.append(Root(value=priority))
        root = self._get_root_by_value(priority)
        root.queue.append(item)
        self._sorted_by_value()

    def dequeue(self) -> None:
        """Получить элемент из очереди"""
        if not self._qsize:
            raise Empty
        return self._queue[0].queue.pop(0)
