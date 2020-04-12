import sys


class Node(object):
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous


class DoublyLinkedList(object):
    def __init__(self):
        self.root = None
        self.tail = None

    def add(self, value) -> Node:
        if not self.root:
            self.root = Node(value)
            self.tail = self.root
        else:
            old_root = self.root
            self.root = Node(value)
            self.root.next = old_root
            old_root.previous = self.root
        return self.root

    def drop(self) -> Node:
        if self.tail:
            node = self.tail
            self.tail = self.tail.previous
            if self.tail:
                self.tail.next = None
            return node

    def remove(self, node):
        if node == self.root:
            self.root = None
            self.tail = None
        elif node == self.tail:
            self.tail = self.tail.previous
            self.tail.next = None
        else:
            if node.previous:
                node.previous.next = node.next
                node.next.previous = node.previous

    def __str__(self):
        contents = []
        node = self.root
        while node:
            contents.append(node.value)
            node = node.next
        return str(contents)


class CacheValue(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class LRU_Cache(object):

    def __init__(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")

        if capacity == 0:
            raise ValueError("Capacity cannot be zero")

        self.lru = DoublyLinkedList()
        self.cache = {}
        self.capacity = capacity
        self.count = 0

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.lru.remove(node)
            self.cache[key] = self.lru.add(node.value)
            return node.value.value
        else:
            return -1

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            self.lru.remove(node)
            self.cache[key] = self.lru.add(CacheValue(key, value))
        else:
            if self.count == self.capacity:
                node = self.lru.drop()
                if node:
                    del self.cache[node.value.key]
                    self.count -= 1
            self.cache[key] = self.lru.add(CacheValue(key, value))
            self.count += 1


if __name__ == '__main__':
    try:
        LRU_Cache(-1)
    except ValueError:
        print(f"{sys.exc_info()[0].__name__}: {sys.exc_info()[1]}")
    # ValueError: Capacity cannot be negative

    try:
        LRU_Cache(0)
    except ValueError:
        print(f"{sys.exc_info()[0].__name__}: {sys.exc_info()[1]}")
    # ValueError: Capacity cannot be zero

    cache_of_one = LRU_Cache(1)
    cache_of_one.set(1, "One")
    print(cache_of_one.get(1))
    # One

    cache_of_one.set(2, "Two")
    print(cache_of_one.get(2))
    # Two

    our_cache = LRU_Cache(5)

    print(our_cache.get(0))
    # -1

    print(our_cache.get(None))

    our_cache = LRU_Cache(5)
    our_cache.set(1, "One")
    our_cache.set(2, "Two")
    our_cache.set(3, "Three")
    our_cache.set(4, "Four")

    print(our_cache.get(1))
    # One

    print(our_cache.get(2))
    # Two

    print(our_cache.get(9))
    # -1

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    print(our_cache.get(3))
    # -1
