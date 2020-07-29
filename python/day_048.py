# # JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 48

# This problem was asked by Google.

# Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

# For example, given the following preorder traversal:

# [a, b, d, e, c, f, g]

# And the following inorder traversal:

# [d, b, e, a, f, c, g]

# You should return the following tree:

#     a
#    / \
#   b   c
#  / \ / \
# d  e f  g

class Node:
    
    left_node = None
    right_node = None

    def __init__(self, name):
        self.name = name

def reconstruct(preorder, inorder):
    root_name = preorder[0]
    root = Node(root_name)

    middle_index = inorder.index(root_name)

    left_inorder = inorder[:middle_index]
    left_preorder = [node for node in preorder if node in left_inorder]
    right_inorder = inorder[middle_index+1:]
    right_preorder = [node for node in preorder if node in right_inorder]

    if len(left_inorder) > 1:
        root.left_node = reconstruct(left_preorder, left_inorder)
    else:
        root.left_node = Node(left_inorder[0])

    if len(right_inorder) > 1:
        root.right_node = reconstruct(right_preorder, right_inorder)
    else:
        root.right_node = Node(right_inorder[0])

    return root


root = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'], ['d', 'b', 'e', 'a', 'f', 'c', 'g'])