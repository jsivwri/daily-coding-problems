#JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 20

# This problem was asked by Google.

# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

# In this example, assume nodes with the same value are the exact same node objects.

# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

class Linked_list:
    def __init__(self, lst):
        self.head = None
        self.tail = None

        current_node = None
        previous_node = None

        for index in range(len(lst)):
            current_node = Node(lst[index])
            if previous_node != None:
                previous_node.next_node = current_node
            if index == 0:
                self.head = current_node
            if index == len(lst)-1:
                self.tail = current_node
            previous_node = current_node


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class List_evaluator:
    def __init__(self):
        self.value_dictionary = {}

    def add_to_dictionary(self, value):
        if value in self.value_dictionary:
            return "intersect", value
        else:
            self.value_dictionary[value] = True
            return "added", value

    def find_intersecting_nodes(self, list_a, list_b):

        current_node_a = list_a.head
        current_node_b = list_b.head

        while current_node_a != None:

            response, value = self.add_to_dictionary(current_node_a.value)

            if response == "intersect":
                return value

            current_node_a = current_node_a.next_node

        while current_node_b != None:

            response, value = self.add_to_dictionary(current_node_b.value)

            if response == "intersect":
                return value

            current_node_b = current_node_b.next_node

        if current_node_a and current_node_b == None:
            return None 


#TEST CODE:
llist_a = Linked_list([3, 7, 8, 10])
llist_b = Linked_list([99, 1, 8, 10])
evaluator = List_evaluator()
assert evaluator.find_intersecting_nodes(llist_a, llist_b) == 8

llist_a = Linked_list([3, 7, 4, 0, 2, 10])
llist_b = Linked_list([99, 1, 8, 10])
evaluator = List_evaluator()
assert evaluator.find_intersecting_nodes(llist_a, llist_b) == 10

llist_a = Linked_list([3, 7, 4, 0, 2, 10])
llist_b = Linked_list([99, 1, 8, 6])
evaluator = List_evaluator()
assert evaluator.find_intersecting_nodes(llist_a, llist_b) == None