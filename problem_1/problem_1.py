class KeyNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class Queue:
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.num_elements = 0
        self.capacity = capacity

    def enqueue(self, key):
        new_node = KeyNode(key)

        # Dequeues item if queue capacity is full
        if self.num_elements == self.capacity:
            self.dequeue()

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.num_elements += 1

    def dequeue(self):
        if self.num_elements == 0:
            return None
        temp = self.head.key
        self.head = self.head.next
        self.num_elements -= 1
        return temp


class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.queue = Queue(capacity)
        self.cache_is_full = capacity == len(self.cache)

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.

        cached_value = self.cache.get(key, -1)

        if cached_value is not -1:
            self.queue.enqueue(key)

        return cached_value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        # Checks if item already exists in the cache, if it does, returns as we wouldn't want to set it again
        if self.get(key) is not -1:
            return

        # If cache is full, we dequeue the the least recently used key and then pop it from the cache
        if self.cache_is_full:
            key_to_be_removed = self.queue.dequeue()
            self.cache.pop(key_to_be_removed, None)

        # Then finally we add the key to our cache and enqueue it
        self.cache[key] = value
        self.queue.enqueue(key)


our_cache = LRUCache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print('Should return 1:', our_cache.get(1))
# returns 1
print('Should return 2:', our_cache.get(2))
# returns 2
print('Should return -1:', our_cache.get(9))
# returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print('Should return -1:', our_cache.get(3))
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print('Should return 4:', our_cache.get(4))
# returns 4

our_cache.set(7, 7)
our_cache.set(8, 8)

print('Should return -1:', our_cache.get(1))
# returns -1 because the cache reached it's capacity and 1 was the least recently used entry
print('Should return 8:', our_cache.get(8))
# returns 8

print('Should return -1:', our_cache.get(None))
# returns -1

