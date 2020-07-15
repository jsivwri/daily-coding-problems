# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 36

# This problem was asked by Dropbox.

# Given the root to a binary search tree, find the second largest node in the tree.

class Sorted_tree:
    def __init__(self, root):
        self.root = root
        
    def add_node(self, node, parent_node = None):
        if parent_node == None:
            parent_node = self.root

        if node.value > parent_node.value:
            if parent_node.right == None:
         
                parent_node.right = node
            else:
                self.add_node(node, parent_node.right)
        
        elif node.value < parent_node.value:
            if parent_node.left == None:
                parent_node.left = node
            else: 
                self.add_node(node, parent_node.left)

    def find_second_largest(self, queue = None, pointer=None, stop=None):
        if pointer == None:
            queue = [self.root]
            pointer = 0
            stop = 2

        while len(queue) > pointer:
            current_node = queue[pointer]
            
            if current_node.right != None:
                queue += [current_node.right]
                pointer += 1
                return self.find_second_largest(queue, pointer, stop)

            else:
                stop -= 1
                if stop == 0:
                    return current_node.value
            
            if current_node.left != None:
                queue += [current_node.left]
                pointer += 1
                return self.find_second_largest(queue, pointer, stop)

            if pointer + 1 == len(queue):
                return queue[pointer-1].value

            pointer += 1

    
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 

node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)
node_6 = Node(6)
node_7 = Node(7)
node_8 = Node(8)
node_9 = Node(9)

node_list = [node_1, node_2, node_3, node_4, node_5, node_6, node_7, node_8, node_9]

# create a random binary search tree with nodes 0-9
import random
node = node_list.pop(random.randint(0,len(node_list)-1))
binary_tree= Sorted_tree(node)

for _ in range(len(node_list)):
    node = node_list.pop(random.randint(0,len(node_list)-1))
    binary_tree.add_node(node)



assert binary_tree.find_second_largest() == 8