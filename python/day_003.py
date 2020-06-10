#JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 3

#This problem was asked by Google.

#Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# serialize by using recursion to traverse the tree
def serialize( node ): 

    out=[]

    # the logic will attempt to go as deepand as far to the right as it can before backtracking up and left
    # as it traverses the array, it will recursively add the values to a string

    if isinstance(node.right, Node): # checks for a 'deeper' node to the right, traverses to it if possible
        out=out+serialize(node.right)
    else: 
        out=out+[None]

    if isinstance(node.left, Node): # check for a 'deeper' node to the left, traverses to it if possible
        out=out+serialize(node.left)
    else:
        out=out+[None]
    
    out=out+[node.val]

    return out


# deconstructs the string in reverse recursively
def deserialize( string ): 

    val = string.pop()

    if val==None:
        return None

    else:
        return Node(val, deserialize(string),deserialize(string))


### TEST CODE ###
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'