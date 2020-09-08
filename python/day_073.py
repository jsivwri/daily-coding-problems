# This problem was asked by Google.

# Given the head of a singly linked list, reverse it in-place.

class Linked_list:
    def __init__(self):
        self.head = None

    def __repr__(self):
        output_string = ""
        current_node = self.head
        while current_node != None:
            output_string += current_node.val
            current_node = current_node.next_node
        
        return output_string
    
    def add(self, node):
        if self.head == None:
            self.head = node

        else:
            current_node = self.head
            while current_node.next_node != None:
                current_node = current_node.next_node
            current_node.next_node = node
        
class Node:
    def __init__(self, val):
        self.val = val
        self.next_node = None

def reverse_llist(node):
    current_node = node
    next_node = node.next_node
    if next_node != None:
        reverse_llist(next_node)
        next_node.next_node = current_node
        current_node.next_node = None  

node_a = Node('a')
node_b = Node('b')
node_c = Node('c')
node_d = Node('d')
llist = Linked_list()
llist.add(node_a)
llist.add(node_b)
llist.add(node_c)
llist.add(node_d)
assert str(llist) == 'abcd'

reverse_llist(node_a)
llist.head = node_d
assert str(llist) == 'dcba'