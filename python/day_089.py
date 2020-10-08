# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 89

# This problem was asked by LinkedIn.

# Determine whether a tree is a valid binary search tree.

# A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key in the left child must be less than or equal to the root and the key in the right child must be greater than or equal to the root.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def validate_tree(root, min = None, max = None):

    if root.left != None:
        if root.left.val >= root.val:
            return False

        if min != None:
            if root.left.val <= min:
                return False
        
        else:
            if validate_tree(root.left, min, root.val) == False:
                return False
        
    if root.right != None:
        if root.right.val <= root.val:
            return False

        if max != None:
            if root.right.val >= max:
                return False

        else:
            if validate_tree(root.right, root.val, max) == False:
                return False

    return True

root = Node(6)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(7)
root.right.right = Node(9)
assert validate_tree(root) == True

root = Node(6)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(6) # False entry
root.right.right = Node(9)

assert validate_tree(root) == False