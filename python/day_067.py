# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 67

# This problem was asked by Google.

# Implement an LFU (Least Frequently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

# set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least frequently used item. If there is a tie, then the least recently used key should be removed.
# get(key): gets the value at key. If no such key exists, return null.
# Each operation should run in O(1) time.

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.access_count = 0
        self.prev_node = None
        self.next_node = None

class Frequency_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.dictionary = {}

    def add(self, node):
        key = node.key

        self.dictionary[key] = node

        if self.head == None:
            self.head = node
            self.tail = node
        else:
            old_tail = self.tail
            self.tail = node
            self.tail.prev_node = old_tail
            old_tail.next_node = self.tail

    def remove(self, key):
        node_to_return = self.dictionary[key]
        del self.dictionary[key]

        if node_to_return.prev_node == None:
            self.head = node_to_return.next_node
        
        else:
            node_to_return.prev_node.next_node = node_to_return.next_node

        if node_to_return.next_node != None:
            node_to_return.next_node.prev_node = node_to_return.prev_node
        
        return node_to_return

    def remove_least_used(self):
        node_to_return = self.head
        return self.remove(node_to_return.key).key

class LFU:
    def __init__(self, n):
        self.max_size = n
        self.frequency_dict = {}
        self.frequency_dict[0] = Frequency_list()
        self.dict = {}
        self.current_size = 0
        self.lowest_access_count = 0
        

    def set(self, key, value):
        if self.current_size == self.max_size:
            least_used_key = self.frequency_dict[self.lowest_access_count].remove_least_used()
            del self.dict[least_used_key]

        else:
            self.current_size += 1

        new_node = Node(key, value)
        self.frequency_dict[0].add(new_node)
        self.dict[key] = new_node
        self.lowest_access_count = 0
    
    def get(self, key):
        if key in self.dict.keys():
            node_to_return = self.dict[key]
        else:
            return None
        current_access_count = node_to_return.access_count

        if (current_access_count + 1) not in self.frequency_dict.keys():
            self.frequency_dict[current_access_count+1] = Frequency_list()
        
        self.frequency_dict[current_access_count].remove(key)
        self.frequency_dict[current_access_count+1].add(node_to_return)
        node_to_return.access_count += 1

        return node_to_return.value

lfu = LFU(4)
lfu.set('a','alpha')
lfu.set('b', 'bravo')
lfu.set('c', 'charlie')
lfu.set('d', 'delta')
print(lfu.get('a'))
print(lfu.get('a'))
print(lfu.get('a'))
print(lfu.get('b'))
print(lfu.get('b'))
print(lfu.get('d'))
lfu.set('e','epsilon')
print(lfu.get('c'))