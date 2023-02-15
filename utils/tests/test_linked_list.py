from utils.linked_list import LinkedList, LinkedListWithSort


def test_list_append():
    linked_list = LinkedList()
    linked_list.append(5)

    assert len(linked_list) == 1

    linked_list.append(9)
    linked_list.append(9)

    assert len(linked_list) == 3

    assert str(linked_list) == "[5, 9, 9]"


def test_list_append_with_sort():
    linked_list = LinkedListWithSort()
    linked_list.append(5)
    linked_list.append(7)
    linked_list.append(2)
    linked_list.append(6)
    linked_list.append(1)
    linked_list.append(1)
    linked_list.append(5)
    linked_list.append(9)
    linked_list.append(2)
    linked_list.append(6)
    linked_list.append(0)

    assert len(linked_list) == 11

    assert str(linked_list) == "[0, 1, 1, 2, 2, 5, 5, 6, 6, 7, 9]"
