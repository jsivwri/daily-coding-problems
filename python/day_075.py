# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 75

# This problem was asked by Microsoft.

# Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

# For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = []

def build_graph(array):
    nodes = []
    for val in array:
        new_node = Node(val)
        for node in nodes:
            if node.val < new_node.val:
                node.next.append(new_node)
        nodes.append(new_node)

    return nodes

def count_traversals(node):
    count = 0

    next_nodes = node.next
    for node in next_nodes:
        count = max(count, 1+count_traversals(node))

    return count

def find_longest(nodes):
    min_val = None
    count = 0
    for node in nodes:
        if min_val == None:
            min_val = node.val
            count = max(1 + count_traversals(node), count)

        elif min_val > node.val:
            min_val = node.val
            count = max(1 + count_traversals(node), count)

    return count

nodes = build_graph([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
assert find_longest(nodes) == 6