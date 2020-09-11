# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 77

# This problem was asked by Snapchat.

# Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

# The input list is not necessarily ordered in any way.

# For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].

class Node:
    def __init__(self, interval):
        start, end = interval
        self.start = start
        self.end = end
        self.next_node = None

class Linked_list:
    def __init__(self, head):
        self.head = head

    def add(self, node):
        start = node.start
        end = node.end

        current_node = self.head
        
        while current_node != None:
            next_node = current_node.next_node
        
            if start < current_node.end:
                if start < current_node.start:
                    current_node.start = start

                if end > current_node.end:
                    current_node.end = end
                current_node = None

            elif next_node == None:
                current_node.next_node = node
                current_node = None

            else:
                current_node = next_node

    def return_intervals(self):
        output = []
        current_node = self.head

        while current_node != None:
            output.append((current_node.start, current_node.end))
            current_node = current_node.next_node

        return output

def merge_intervals(intervals):
    nodes = [Node(interval) for interval in intervals]
    llist = Linked_list(nodes[0])

    for node in nodes[1:]:
        llist.add(node)
    
    return llist.return_intervals()

assert merge_intervals([(1, 3), (5, 8), (4, 10), (20, 25)]) == [(1, 3), (4, 10), (20, 25)]