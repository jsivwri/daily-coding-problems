# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 72

# This problem was asked by Google.

# In a directed graph, each node is assigned an uppercase letter. We define a path's value as the number of most frequently-occurring letter along that path. For example, if a path in the graph goes through "ABACA", the value of the path is 3, since there are 3 occurrences of 'A' on the path.

# Given a graph with n nodes and m directed edges, return the largest value path of the graph. If the largest value is infinite, then return null.

# The graph is represented with a string and an edge list. The i-th character represents the uppercase letter of the i-th node. Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to the j-th node. Self-edges are possible, as well as multi-edges.

# For example, the following input graph:

# ABACA
# [(0, 1),
#  (0, 2),
#  (2, 3),
#  (3, 4)]
# Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).

# The following input graph:

# A
# [(0, 0)]
# Should return null, since we have an infinite loop.

class Node:
    def __init__(self, letter):
        self.letter = letter
        self.next_nodes = []
        self.input_string = ""

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, letter):
        self.nodes.append(Node(letter))
    
    def parse_inputs(self, input_string, input_tuples):
        self.input_string = input_string
        for char in input_string:
            self.add_node(char)

        for input_tuple in input_tuples:
            start, destination = input_tuple
            self.nodes[start].next_nodes.append(self.nodes[destination])

    def traverse_nodes(self, start_node, next_nodes, visited_nodes, path):

        output_path = ""

        if len(next_nodes) == 0:
            return path

        for next_node in next_nodes:
            new_start_node = next_node
            if new_start_node not in visited_nodes:
                new_next_nodes = new_start_node.next_nodes
                new_visited_nodes = visited_nodes + [new_start_node]
                new_path = path + new_start_node.letter

                new_output_paths = self.traverse_nodes(new_start_node, new_next_nodes, new_visited_nodes, new_path)
                output_path = max(new_output_paths, output_path, key=len)

        return output_path

    def find_open_path(self):

        longest_path = ""

        for val in range(len(self.input_string)):

            start_node = self.nodes[val]
            next_nodes = start_node.next_nodes
            visited_nodes = [start_node]
            path = start_node.letter
        
            new_path = self.traverse_nodes(start_node, next_nodes, visited_nodes, path)
            longest_path = max(longest_path, new_path, key=len)

        path_dict = {}
        for char in longest_path:
            try:
                path_dict[char] += 1
            except:
                path_dict[char] = 1

        max_val = 0
        max_key = None
        for key in path_dict.keys():
            if path_dict[key] > max_val:
                max_val = path_dict[key]
                max_key = key

        return max_key

graph = Graph()
graph.parse_inputs('ABACA',[(0, 1), (0, 2), (2, 3), (3, 4)])
assert graph.find_open_path() == 'A'

graph = Graph()
assert graph.parse_inputs('A',[(0, 0)]) == None