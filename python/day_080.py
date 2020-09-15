# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 80

# This problem was asked by Google.

# Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

#     a
#    / \
#   b   c
#  /
# d

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = root

def dfs(node, depth=0):

    if node.left == None and node.right == None:
        return depth, node.val

    return max([dfs(next_node, depth+1) for next_node in [node.left, node.right] if next_node != None])

def deepest_val(node):
    _, val = dfs(node)
    return val

tree = Tree(Node('a'))
tree.root.left = Node('b')
tree.root.right = Node('c')
tree.root.left.left = Node('d')

assert deepest_val(tree.root) == 'd'