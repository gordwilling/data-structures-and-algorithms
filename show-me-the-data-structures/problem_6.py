from typing import Set, List


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        out_string += "None"
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    element_set = set()
    _add_all_to_set(element_set, llist_1)
    _add_all_to_set(element_set, llist_2)

    union_list = LinkedList()
    for value in element_set:
        union_list.append(value)

    return union_list


def intersection(llist_1, llist_2):
    llist1_set = set()
    _add_all_to_set(llist1_set, llist_1)

    intersection_set = set()
    node = llist_2.head
    while node:
        if node.value in llist1_set:
            intersection_set.add(node.value)
        node = node.next

    intersection_list = LinkedList()
    for value in intersection_set:
        intersection_list.append(value)

    return intersection_list


def _add_all_to_set(s: Set, ll: LinkedList):
    node = ll.head
    while node:
        s.add(node.value)
        node = node.next


def _ll(*args):
    linked_list = LinkedList()
    for i in args:
        linked_list.append(i)
    return linked_list


if __name__ == '__main__':
    print(union(_ll(3, 2, 4, 35, 6, 65, 6, 4, 3, 21), _ll(6, 32, 4, 9, 6, 1, 11, 21, 1)))
    # 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> None

    print(union(_ll(6, 32, 4, 9, 6, 1, 11, 21, 1), _ll(3, 2, 4, 35, 6, 65, 6, 4, 3, 21)))
    # 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> None

    print(union(LinkedList(), _ll(3, 2, 4, 35, 6, 65, 6, 4, 3, 21)))
    # 3, 2, 4, 35, 6, 65, 6, 4, 3, 21 -> None

    print(union(_ll(3, 2, 4, 35, 6, 65, 6, 4, 3, 21), LinkedList()))
    # 3, 2, 4, 35, 6, 65, 6, 4, 3, 21 -> None

    print(intersection(_ll(3, 2, 4, 35, 6, 65, 6, 4, 3, 21), _ll(6, 32, 4, 9, 6, 1, 11, 21, 1)))
    # 4 -> 21 -> 6 -> None

    print(intersection(_ll(6, 32, 4, 9, 6, 1, 11, 21, 1), _ll(3, 2, 4, 35, 6, 65, 6, 4, 3, 21)))
    # 4 -> 21 -> 6 -> None

    print(intersection(LinkedList(), _ll(3, 2, 4, 35, 6, 65, 6, 4, 3, 21)))
    # None

    print(intersection(_ll(3, 2, 4, 35, 6, 65, 6, 4, 3, 21), LinkedList()))
    # None
