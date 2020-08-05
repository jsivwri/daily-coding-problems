# This problem was asked by Google.

# Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

# set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
# get(key): gets the value at key. If no such key exists, return null.
# Each operation should run in O(1) time.
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev_node = None
        self.next_node = None

class Linked_list:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        

class LRU:
    def __init__(self, n):
        self.cache_size = n
        self.data = []
        self.dictionary = {}
        self.linked_list = Linked_list()

    def set(self, key, value):
        

        self.dictionary[key] = Node(key, value)

        new_node = self.dictionary[key]

        
        if self.linked_list.head == None:
            self.linked_list.head = new_node
            self.linked_list.tail = new_node


        else:
            if len(self.dictionary.keys()) > self.cache_size:
                del_node_key = self.linked_list.tail.key
                self.linked_list.tail = self.linked_list.tail.prev_node
                self.linked_list.tail.prev_node = None
                self.dictionary.pop(del_node_key)
                
            old_head = self.linked_list.head
            self.linked_list.head = new_node
            old_head.prev_node = new_node
            new_node.next_node = old_head

        
    def get(self, key):

        if key not in self.dictionary:
            return None

        node = self.dictionary[key]
        old_head = self.linked_list.head


        if node == self.linked_list.tail:
            self.linked_list.tail = node.prev_node
        if node.prev_node != None:
            node.prev_node.next_node = node.next_node
        if node.next_node != None:
            node.next_node.prev_node = node.prev_node

        self.linked_list.head = node

        old_head.prev_node = node
        node.next_node = old_head
    
        return node.value

cache = LRU(4)

cache.set("key_1", "value_1")
cache.set("key_2", "value_2")
cache.set("key_3", "value_3")

assert cache.get("key_1") == "value_1"
assert cache.get("key_5") == None
assert cache.get("key_3") == "value_3"
assert cache.get("key_2") == "value_2"
assert cache.get("key_4") == None

cache.set("key_4", "value_4")

assert cache.get("key_3") == "value_3"
assert cache.get("key_1") == "value_1"
assert cache.get("key_5") == None
assert cache.get("key_2") == "value_2"
assert cache.get("key_4") == "value_4"

cache.set("key_5", "value_5")

assert cache.get("key_1") == "value_1"
assert cache.get("key_5") == "value_5"
assert cache.get("key_3") == None
assert cache.get("key_2") == "value_2"
assert cache.get("key_4") == "value_4"