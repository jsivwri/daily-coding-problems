# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 24

# This problem was asked by Google.

# Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

# Design a binary tree node class with the following methods:

# is_locked, which returns whether the node is locked
# lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
# unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.
# You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.

class Tree_node:
    def __init__(self, value, parent=None):
        self.value = value
        self.locked = False
        self.parent = parent 
        self.left = None
        self.right = None
        self.child_locked = 0

    def add_child(self, direction, value):
        if direction == 'left':
            if self.left == None: 
                self.left = Tree_node(value, self)
            
        elif direction == 'right':
            if self.right == None: 
                self.right = Tree_node(value, self)
        
        else: 
            print("Error: can't add node")

    def is_locked(self):
        return self.locked

    def lock(self):
        if self.child_locked == 0 and self.locked == False:
            self.locked = True
            if self.parent != None:
                self.parent.tell_parent(1)
            return True 
        else:
            if self.locked == False:
                print("this implementation won't unlocked an unlocked node")
            return False

    def unlock(self):
        if self.child_locked == 0 and self.locked == True:
            self.locked = False
            if self.parent != None:
                self.parent.tell_parent(-1)
            return True
        else:
            if self.locked == True:
                print("this implementation won't locked a locked node")
            return False 

    def tell_parent(self, lock):
        if self.parent != None:
            self.parent.tell_parent(lock)
        self.child_locked += lock


#          root
#          /    \
#         l      r
#       /  \   /   \
#    l.l  l.r  r.l  r.r
#                    \
#                   r.r.r

root = Tree_node('root')
root.add_child('left','left')
root.add_child('right','right')
root.left.add_child('left','left.left')
root.left.add_child('right','left.right')
root.right.add_child('left','right.left')
root.right.add_child('right','right.right')
root.right.right.add_child('right','right.right.right')

assert root.left.lock() == True
assert root.lock() == False
assert root.right.lock() == True
assert root.right.right.right.lock() == True
assert root.right.lock() == False
assert root.lock() == False
assert root.right.right.right.unlock() == True
assert root.left.lock() == False
assert root.left.unlock() == True
assert root.right.unlock() == True
assert root.lock() == True