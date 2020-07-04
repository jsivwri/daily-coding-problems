# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 26

# This problem was asked by Google.

# Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

# The list is very long, so making more than one pass is prohibitively expensive.

# Do this in constant space and in one pass.

def remove_from_end(llist, k):
    current_node = llist.head
    k_node = llist.head
    while current_node != None:
        k -= 1
        if k < -1:
            k_node=k_node.next_node

        current_node=current_node.next_node

    k_node.next_node = k_node.next_node.next_node


class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None


class Linked_list:
    def __init__(self):
        self.head = None

    def __repr__(self):
        output = ""
        current_node = self.head
        while current_node != None:
            output += current_node.value+" -> "
            current_node = current_node.next_node  

        return output+"None"
    
    def add_node(self, node):
        if self.head == None:
            self.head = node

        else:
            current_node = self.head
            while current_node.next_node != None:
                current_node = current_node.next_node

            current_node.next_node = node


#TEST CODE
node_a = Node('a')
node_b = Node('b')
node_c = Node('c')
node_d = Node('d')
node_e = Node('e')
node_f = Node('f')

llist = Linked_list()
llist.add_node(node_a)
llist.add_node(node_b)
llist.add_node(node_c)
llist.add_node(node_d)
llist.add_node(node_e)
llist.add_node(node_f)

print(llist) # "a -> b -> c -> d -> e -> f -> None"
remove_from_end(llist, 4)
print(llist) # "a -> b -> c -> e -> f -> None"