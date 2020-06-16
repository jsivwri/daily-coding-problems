#JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 8

# This problem was asked by Google.

# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1


def unival_count(root, recursive_call="No"):
    
    count = 0
    return_val_L = return_val_R = None
    return_val = root.val

    if root.left == None and root.right == None: # leaf nodes can return immediately
        count = 1
        return count, root.val

    if root.left != None:
        return_count, return_val_L = unival_count(root.left,"yes")
        count += return_count
    
    if root.right != None:
        return_count, return_val_R = unival_count(root.right,"yes")
        count += return_count
    
    if return_val_L == return_val_R and return_val_L == root.val:
        count += 1
    else:
        return_val = None #'poisions the well' so that parent nodes can't be considered to unival

    if recursive_call == "No":
        return count
    else:
        return count, return_val


#TEST CASE:

#define a Node:

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val

        if isinstance(left,Node) or left == None:
            self.left = left
        else: 
            raise TypeError('Left Node not Class Node') 
        
        if isinstance(right,Node) or right == None:
            self.right = right
        else: 
            raise TypeError('Right Node not Class Node')

#build the given test tree
left = Node(1)
right = Node(0, Node(1,Node(1),Node(1)), Node(0))
root = Node(0, left, right)

assert unival_count(root) == 5


#build another test tree which minimises the number of unival trees:
#    0
#   / \
#  0   0
#     / \
#    0   0
#   / \
#  1   1

left = Node(0)
right = Node(0, Node(0,Node(1),Node(1)), Node(0))
root = Node(0, left, right)

assert unival_count(root) == 4


#build another test tree which maximuses the number of unival trees:
#    0
#   / \
#  0   0
#     / \
#    0   0
#   / \
#  0   0

left = Node(0)
right = Node(0, Node(0,Node(0),Node(0)), Node(0))
root = Node(0, left, right)

assert unival_count(root) == 7

