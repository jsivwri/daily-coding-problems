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


def unival_count(root):
    
    count = 0

    if root.left != None:
        count += unival_count(root.left)
    
    if root.right != None:
        count += unival_count(root.right)

    if root.left != None and root.right != None:
        if root.left.val == root.right.val:
            count += 1

    if root.left == root.right:
        count +=1
    
    return count 


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

#build the test tree
left = Node(1)
right = Node(0, Node(1,Node(1),Node(1)), Node(0))
root = Node(0, left, right)

assert unival_count(root) == 5