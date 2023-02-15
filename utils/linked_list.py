from typing import Any


class LinkedList:
    """Односвязный список"""

    head: "Node" = None
    _length: int = 0

    class Node:
        element: Any = None
        next_node = None

        def __init__(self, element: Any, next_node=None):
            self.next_node = next_node
            self.element = element

        def __str__(self):
            return str(self.element)

    def append(self, element):
        if not self.head:
            self.head = self.Node(element)
            self._length += 1
            return element

        node = self.head
        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(element)
        self._length += 1
        return element

    def __len__(self):
        return self._length

    def __str__(self):
        node = self.head
        elems = [node]
        while node.next_node:
            node = node.next_node
            elems.append(node)
        return "[{}]".format(", ".join([str(element) for element in elems]))


class LinkedListWithSort(LinkedList):
    """Односвязный список с сортировкой при вставке элемента"""

    def append(self, element: int):
        if not self.head:
            self.head = self.Node(element)
            self._length += 1
            return element

        new_node = self.Node(element)

        if element < self.head.element:
            tmp_node = self.head
            new_node.next_node = tmp_node
            self.head = new_node
            self._length += 1
            return element

        node = self.head
        while node.next_node and element > node.next_node.element:
            node = node.next_node

        if not node.next_node:
            node.next_node = new_node
            self._length += 1
            return element

        new_node.next_node = node.next_node
        node.next_node = new_node
        self._length += 1
        return element
