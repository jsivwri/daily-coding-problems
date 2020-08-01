# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 50

# This problem was asked by Microsoft.

# Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '-', '*', or '/'.

# Given the root to such a tree, write a function to evaluate it.

# For example, given the following tree:

#     *
#    / \
#   +    +
#  / \  / \
# 3  2  4  5

# You should return 45, as it is (3 + 2) * (4 + 5).

class Node:
    left_node = None
    right_node = None

    def __init__(self, val):
        self.val = val

root = Node('*')
root.left_node = Node('+')
root.left_node.left_node = Node(3)
root.left_node.right_node = Node(2)
root.right_node = Node('+')
root.right_node.left_node = Node(4)
root.right_node.right_node = Node(5)

def evaluate(root):
    if root.val == "*":
        return evaluate(root.left_node) * evaluate(root.right_node)

    elif root.val == "/":
        return evaluate(root.left_node) / evaluate(root.right_node)

    elif root.val == "+":
        return evaluate(root.left_node) + evaluate(root.right_node)   

    elif root.val == "-":
        return evaluate(root.left_node) - evaluate(root.right_node)
    
    else:
        return root.val
    
assert evaluate(root) == 45