# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 56

# This problem was asked by Google.

# Given an undirected graph represented as an adjacency matrix and an integer k, write a function to determine whether each vertex in the graph can be colored such that no two adjacent vertices share the same color using at most k colors.

class Node:
    def __init__(self, name):
        self.name = name
        self.color = None
        self.next_nodes = []

class Graph:
    def __init__(self, matrix):
        self.nodes = []

        for node_name in range(len(matrix)):
            self.nodes.append(Node(node_name))
        
        for index in range(len(matrix)):
            for adjacency_val_index in range(len(matrix[index])):
                next_node = self.nodes[adjacency_val_index]
                next_node_bool = matrix[index][adjacency_val_index]

                if next_node_bool == 1:
                    self.nodes[index].next_nodes.append(next_node)

    def color_graph(self, k):
        uncolored_nodes = self.nodes[:]
        node_queue = [uncolored_nodes.pop(0)]

        while len(uncolored_nodes) > 0 or len(node_queue) > 0:
            current_node = node_queue.pop(0)
            adjacent_nodes = current_node.next_nodes
            
            for node in adjacent_nodes:
                if node in uncolored_nodes:
                    node_queue.append(node)
                    uncolored_nodes.remove(node)

            current_colors = range(k)[:] # '[:]' overcomes pylint bug

            for adjacent_node in adjacent_nodes:
                if adjacent_node.color != None:
                    if adjacent_node.color in current_colors:
                        current_colors.remove(adjacent_node.color)
            
            if len(current_colors) > 0:
                current_node.color = current_colors[0]
            else:
                return False
        
        return True

matrix = [
    [0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0]
]

graph = Graph(matrix)
assert graph.color_graph(3) == True
assert graph.color_graph(2) == False