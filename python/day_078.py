# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 78

# This problem was asked by Google.

# Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.

class Node:
    def __init__(self, val):
        self.val = val
        self.next_node = None

class Linked_list:
    def __init__(self, head):
        self.head = head

    def __repr__(self):
        output = ""
        current_node = self.head
        while current_node != None:
            output += str(current_node.val) + " "
            current_node = current_node.next_node
        
        return output
    
    def add(self, node):
        current_node = self.head

        while current_node.next_node != None:
            current_node = current_node.next_node
        
        current_node.next_node = node

def node_val(node):
    return node.val

def merge_linked_lists(linked_lists):
    cache = [llist.head for llist in linked_lists]
    llist_sorted = None

    while len(cache) > 0:
        cache.sort(key = node_val)
        node_to_add = cache[0]

        if cache[0].next_node == None:
            cache = cache[1:]

        else:
            cache[0] = cache[0].next_node 

        node_to_add.next_node = None
        if llist_sorted == None:
            llist_sorted = Linked_list(node_to_add)

        else:
            llist_sorted.add(node_to_add)

    return llist_sorted
        

llist_a = Linked_list(Node(1))
llist_a.add(Node(1))
llist_a.add(Node(2))
llist_a.add(Node(3))
llist_a.add(Node(5))
llist_a.add(Node(8))

llist_b = Linked_list(Node(1))
llist_b.add(Node(3))
llist_b.add(Node(5))
llist_b.add(Node(7))
llist_b.add(Node(9))

llist_c = Linked_list(Node(2))
llist_c.add(Node(3))
llist_c.add(Node(5))
llist_c.add(Node(7))
llist_c.add(Node(11))
llist_c.add(Node(13))

merge_llist = merge_linked_lists([llist_a, llist_b, llist_c])
print(merge_llist)