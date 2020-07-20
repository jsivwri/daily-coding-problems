# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 43

# This problem was asked by Amazon.

# Implement a stack that has the following methods:

# push(val), which pushes an element onto the stack
# pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
# max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
# Each method should run in constant time.

class Stack:
    stack = []
    max_stack = []
    size = 0

    def push(self, val):
        self.stack += [val]
        if self.size == 0 or val > self.max_stack[-1]:
            self.max_stack += [val]
        else:
            self.max_stack += [self.max_stack[-1]]
        self.size += 1
        
    def pop(self):
        if self.size == 0:
            return None
        else:
            val = self.stack[-1]
            self.stack = self.stack[:-1]
            self.max_stack = self.max_stack[:-1]
            self.size -= 1
            return val
    
    def max(self):
        if self.size == 0:
            return None
        else:
            return self.max_stack[-1]

stack = Stack()
stack.push(5)
stack.push(8)
stack.push(6)
stack.push(10)
stack.push(3)

assert stack.max() == 10
assert stack.pop() == 3
assert stack.max() == 10
assert stack.pop() == 10
assert stack.max() == 8
assert stack.pop() == 6
assert stack.max() == 8
assert stack.pop() == 8
assert stack.max() == 5