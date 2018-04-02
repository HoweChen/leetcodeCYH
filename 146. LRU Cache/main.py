class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev_node = None
        self.next_node = None


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = dict()
        self.head_node = Node()
        self.tail_node = Node()
        self.head_node.next_node = self.tail_node
        self.head_node.prev_node = self.tail_node
        self.tail_node.next_node = self.head_node
        self.tail_node.prev_node = self.head_node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            # the key hit the cache
            hit_node = self.cache[key]
            if hit_node.value == value:
                self._remove(hit_node)
                self._add(hit_node)
            else:
                # when the key is the same but value is not, this should be a new Node
                new_node = Node(key=key, value=value)
                self._remove(hit_node)
                self._add(new_node)
                self.cache[key] = new_node

        else:
            # not hit
            new_node = Node(key=key, value=value)
            if len(self.cache) == self.capacity:
                # which means we need to remove the oldest than add the new node
                del self.cache[self.tail_node.next_node.key]
                self._remove(self.tail_node.next_node)
            self._add(new_node)
            self.cache[key] = new_node

    def _remove(self, node):
        # we don't delete the key from the dict because it might be the situation when it is just an update for the frequently visit node
        node.prev_node.next_node = node.next_node
        node.next_node.prev_node = node.prev_node

    def _add(self, node):
        # add the new node into the latest_one, we don't need to care about the capacity in this private function
        last_head = self.head_node.prev_node
        last_head.next_node = node
        node.prev_node = last_head
        node.next_node = self.head_node
        self.head_node.prev_node = node

    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)


cache = LRUCache(2)

# cache.put(1, 1)
# cache.put(2, 2)
# print(cache.get(1))
# cache.put(3, 3)
# print(cache.get(2))
# cache.put(4, 4)
# print(cache.get(1))
# print(cache.get(3))
# print(cache.get(4))

cache.put(2, 1)
cache.put(2, 2)
print(cache.get(2))
# cache.put(1, 1)
# cache.put(4, 1)
# print(cache.get(2))
