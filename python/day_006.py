#JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 6

#This problem was asked by Google.

#An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

#If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.


import ctypes

_nodes=[] #necessary to prevent garbage collection

def reference_pointer(node):
    return id(node)


def dereference_pointer(pointer):
    if pointer==0:
        return None
    return ctypes.cast(pointer, ctypes.py_object).value
    

class Node:
    def __init__(self, value, link_nXp=0):
        self.value = value
        self.link_nXp = link_nXp
        _nodes.append(self) #necessary to prevent garbage collection

    def get_value(self):
        return self.value

    def get_link_nXp(self):
        return self.link_nXp

    def set_link_nXp(self, link_nXp):
        self.link_nXp = link_nXp

    def pointer(self):
        return reference_pointer(self)


class XOR_List:
    def __init__(self, value=None):
        self.tail_node = self.head_node = Node(value)
    
    def get_head_node(self):
        return self.head_node

    def get_tail_node(self):
        return self.tail_node

    def set_tail_node(self, node):
        self.tail_node = node

    def get_index(self, index):
        current_node = self.get_head_node()
        count = 0

        if count == index:
            return current_node.get_value()

        else:
            count+=1
            previous_node = current_node
            next_node = dereference_pointer(current_node.get_link_nXp())

            while (current_node.get_value() != self.tail_node.get_value()):
                if count == index:
                    return next_node.get_value()

                count+=1
                previous_node = current_node
                current_node = next_node
                next_node = dereference_pointer(previous_node.pointer() ^ current_node.get_link_nXp())

        raise IndexError('Index out of range')

            
    def add_node(self, value=None):
        new_node = Node(value, self.tail_node.pointer())
        self.tail_node.set_link_nXp(self.tail_node.get_link_nXp()^new_node.pointer())
        self.set_tail_node(new_node)


# make list:
linked_list = XOR_List('a')
linked_list.add_node('b')
linked_list.add_node('c')
linked_list.add_node('d')


#Test Conditions
assert linked_list.get_index(0) == 'a'
assert linked_list.get_index(1) == 'b'
assert linked_list.get_index(2) == 'c'
assert linked_list.get_index(3) == 'd'