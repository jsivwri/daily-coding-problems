# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 83

# This problem was asked by Google.

# Invert a binary tree.

# For example, given the following tree:

#     a
#    / \
#   b   c
#  / \  /
# d   e f
# should become:

#   a
#  / \
#  c  b
#  \  / \
#   f e  d

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def invert(root):
    if root.left != None:
        invert(root.left)
    
    if root.right != None:
        invert(root.right)

    root.left, root.right = root.right, root.left


node_a = Node('a')
node_b = Node('b')
node_c = Node('c')
node_d = Node('d')
node_e = Node('f')
node_f = Node('f')

node_a.left = node_b
node_a.right = node_c
node_b.left = node_d
node_b.right = node_e
node_c.left = node_f

invert(node_a)

assert node_a.left == node_c
assert node_a.right == node_b
assert node_c.left == None
assert node_c.right == node_f
assert node_b.left == node_e
assert node_b.right == node_d