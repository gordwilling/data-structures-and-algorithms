from queue import Queue


class LRU_Cache(object):

    def __init__(self, capacity):
        self.lru = Queue(capacity)
        self.cache = {}
        self.capacity = capacity
        self.count = 0

    def get(self, key):
        if key in self.cache:
            self._add_most_recently_used(key)
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        self._add_most_recently_used(key)
        self.cache[key] = value

    def _add_most_recently_used(self, key):
        self._ensure_capacity()
        self.lru.put(key)
        self.count += 1

    def _ensure_capacity(self):
        if self.capacity == self.count:
            key = self.lru.get_nowait()
            del self.cache[key]
            self.count -= 1


if __name__ == '__main__':
    our_cache = LRU_Cache(5)

    print(our_cache.get(0))
    # -1

    print(our_cache.get(None))
    # -1

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
